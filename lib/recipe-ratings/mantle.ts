import {
  EMPTY_RECIPE_RATING,
  roundRating,
  type RecipeRatingKind,
  type RecipeRatingSummary,
} from "@/lib/recipe-ratings/format";

/**
 * Production: MantleDB fallback when Supabase env is unset.
 * Zero-config durable store used when Supabase env is missing on Vercel.
 * Namespace is claimed; writes require the key (server-only). Reads are public.
 */
const MANTLE_NAMESPACE = "saltet-dk-recipe-ratings";
const MANTLE_PATH = "all";
/** Claim key for saltet-dk-recipe-ratings — server-only, not NEXT_PUBLIC. */
const MANTLE_WRITE_KEY =
  "475794ced8e9883547b03966df497045bf862d0d8362f7fc372eea090f245cb2";

const MANTLE_BASE = `https://mantledb.sh/v2/${MANTLE_NAMESPACE}/${MANTLE_PATH}`;

const MANTLE_HEADERS = {
  Accept: "application/json",
  "User-Agent": "saltet-recipe-ratings/1.0",
} as const;

/** Fresh doc cache — one Mantle doc holds all recipe votes. */
const DOC_CACHE_TTL_MS = 60_000;
/** Hold failed/429 responses briefly so error loops do not burn more ops. */
const ERROR_CACHE_TTL_MS = 30_000;

type RecipeVotes = {
  voters: Record<string, number>;
};

type MantleDoc = {
  v: 1;
  recipes: Record<string, RecipeVotes>;
};

type CacheEntry =
  | { kind: "doc"; doc: MantleDoc; expiresAt: number }
  | { kind: "error"; error: Error; expiresAt: number };

export class MantleRateLimitError extends Error {
  constructor(message = "MantleDB rate limited") {
    super(message);
    this.name = "MantleRateLimitError";
  }
}

let cache: CacheEntry | null = null;
let inflight: Promise<MantleDoc> | null = null;
let mantleFetch: typeof fetch = fetch;

function recipeKey(kind: RecipeRatingKind, slug: string): string {
  return `${kind}:${slug}`;
}

function emptyDoc(): MantleDoc {
  return { v: 1, recipes: {} };
}

function isMantleDoc(value: unknown): value is MantleDoc {
  if (!value || typeof value !== "object") return false;
  const doc = value as MantleDoc;
  return doc.v === 1 && !!doc.recipes && typeof doc.recipes === "object";
}

function cloneDoc(doc: MantleDoc): MantleDoc {
  const recipes: Record<string, RecipeVotes> = {};
  for (const [key, entry] of Object.entries(doc.recipes)) {
    recipes[key] = { voters: { ...entry.voters } };
  }
  return { v: 1, recipes };
}

function summarizeVoters(voters: Record<string, number>): RecipeRatingSummary {
  const ratings = Object.values(voters).filter(
    (n) => Number.isInteger(n) && n >= 1 && n <= 5
  );
  if (ratings.length === 0) return EMPTY_RECIPE_RATING;
  const sum = ratings.reduce((a, b) => a + b, 0);
  return { average: roundRating(sum / ratings.length), count: ratings.length };
}

function setDocCache(doc: MantleDoc, ttlMs = DOC_CACHE_TTL_MS): void {
  cache = { kind: "doc", doc: cloneDoc(doc), expiresAt: Date.now() + ttlMs };
}

function setErrorCache(error: Error, ttlMs = ERROR_CACHE_TTL_MS): void {
  cache = { kind: "error", error, expiresAt: Date.now() + ttlMs };
}

function clearCache(): void {
  cache = null;
}

function readCache(now = Date.now()): CacheEntry | null {
  if (!cache || cache.expiresAt <= now) {
    if (cache) cache = null;
    return null;
  }
  return cache;
}

async function fetchDocFromNetwork(): Promise<MantleDoc> {
  const res = await mantleFetch(MANTLE_BASE, {
    cache: "no-store",
    headers: MANTLE_HEADERS,
  });
  if (res.status === 404) {
    const doc = emptyDoc();
    setDocCache(doc);
    return doc;
  }
  if (res.status === 429) {
    const err = new MantleRateLimitError(
      `MantleDB read failed: ${res.status}`
    );
    setErrorCache(err);
    throw err;
  }
  if (!res.ok) {
    const err = new Error(`MantleDB read failed: ${res.status}`);
    setErrorCache(err);
    throw err;
  }
  const data: unknown = await res.json();
  const doc = isMantleDoc(data) ? data : emptyDoc();
  setDocCache(doc);
  return doc;
}

async function readDoc(options?: {
  bypassCache?: boolean;
}): Promise<MantleDoc> {
  if (!options?.bypassCache) {
    const hit = readCache();
    if (hit?.kind === "doc") return cloneDoc(hit.doc);
    if (hit?.kind === "error") throw hit.error;
  }

  if (inflight) return cloneDoc(await inflight);

  inflight = fetchDocFromNetwork().finally(() => {
    inflight = null;
  });

  return cloneDoc(await inflight);
}

async function writeDoc(doc: MantleDoc): Promise<void> {
  const res = await mantleFetch(MANTLE_BASE, {
    method: "POST",
    cache: "no-store",
    headers: {
      ...MANTLE_HEADERS,
      "Content-Type": "application/json",
      "X-Mantle-Key": MANTLE_WRITE_KEY,
    },
    body: JSON.stringify(doc),
  });
  if (res.status === 429) {
    const err = new MantleRateLimitError(
      `MantleDB write failed: ${res.status}`
    );
    setErrorCache(err);
    throw err;
  }
  if (!res.ok) {
    const text = await res.text().catch(() => "");
    throw new Error(`MantleDB write failed: ${res.status} ${text}`);
  }
}

export function isMantleRatingsConfigured(): boolean {
  return Boolean(MANTLE_NAMESPACE && MANTLE_WRITE_KEY);
}

export async function mantleReadSummary(
  kind: RecipeRatingKind,
  slug: string
): Promise<RecipeRatingSummary> {
  try {
    const doc = await readDoc();
    const entry = doc.recipes[recipeKey(kind, slug)];
    if (!entry?.voters) return EMPTY_RECIPE_RATING;
    return summarizeVoters(entry.voters);
  } catch {
    return EMPTY_RECIPE_RATING;
  }
}

export async function mantleReadVoterRating(
  kind: RecipeRatingKind,
  slug: string,
  voterHash: string
): Promise<number | null> {
  try {
    const doc = await readDoc();
    const rating = doc.recipes[recipeKey(kind, slug)]?.voters?.[voterHash];
    return Number.isInteger(rating) ? Number(rating) : null;
  } catch {
    return null;
  }
}

export async function mantleCastRating(input: {
  kind: RecipeRatingKind;
  slug: string;
  rating: number;
  voterHash: string;
}): Promise<RecipeRatingSummary> {
  const key = recipeKey(input.kind, input.slug);
  let lastError: unknown;

  // Optimistic concurrency: re-read on each attempt. Never retry 429.
  for (let attempt = 0; attempt < 4; attempt++) {
    try {
      const doc = await readDoc({ bypassCache: attempt > 0 });
      const existing = doc.recipes[key]?.voters ?? {};
      const voters = { ...existing, [input.voterHash]: input.rating };
      const next: MantleDoc = {
        v: 1,
        recipes: { ...doc.recipes, [key]: { voters } },
      };
      await writeDoc(next);
      setDocCache(next);
      return summarizeVoters(voters);
    } catch (err) {
      if (err instanceof MantleRateLimitError) throw err;
      lastError = err;
      clearCache();
    }
  }

  throw lastError instanceof Error
    ? lastError
    : new Error("MantleDB cast failed");
}

/** Test-only: swap fetch implementation. Pass null to restore. */
export function __setMantleFetchForTests(fn: typeof fetch | null): void {
  mantleFetch = fn ?? fetch;
}

/** Test-only: clear module cache / inflight. */
export function __resetMantleCacheForTests(): void {
  cache = null;
  inflight = null;
}
