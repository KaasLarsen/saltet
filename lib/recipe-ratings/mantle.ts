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

type RecipeVotes = {
  voters: Record<string, number>;
};

type MantleDoc = {
  v: 1;
  recipes: Record<string, RecipeVotes>;
};

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

function summarizeVoters(voters: Record<string, number>): RecipeRatingSummary {
  const ratings = Object.values(voters).filter(
    (n) => Number.isInteger(n) && n >= 1 && n <= 5
  );
  if (ratings.length === 0) return EMPTY_RECIPE_RATING;
  const sum = ratings.reduce((a, b) => a + b, 0);
  return { average: roundRating(sum / ratings.length), count: ratings.length };
}

async function readDoc(): Promise<MantleDoc> {
  const res = await fetch(MANTLE_BASE, {
    cache: "no-store",
    headers: MANTLE_HEADERS,
  });
  if (res.status === 404) return emptyDoc();
  if (!res.ok) {
    throw new Error(`MantleDB read failed: ${res.status}`);
  }
  const data: unknown = await res.json();
  return isMantleDoc(data) ? data : emptyDoc();
}

async function writeDoc(doc: MantleDoc): Promise<void> {
  const res = await fetch(MANTLE_BASE, {
    method: "POST",
    cache: "no-store",
    headers: {
      ...MANTLE_HEADERS,
      "Content-Type": "application/json",
      "X-Mantle-Key": MANTLE_WRITE_KEY,
    },
    body: JSON.stringify(doc),
  });
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

  // Optimistic concurrency: re-read on each attempt.
  for (let attempt = 0; attempt < 4; attempt++) {
    try {
      const doc = await readDoc();
      const existing = doc.recipes[key]?.voters ?? {};
      const voters = { ...existing, [input.voterHash]: input.rating };
      doc.recipes[key] = { voters };
      await writeDoc(doc);
      return summarizeVoters(voters);
    } catch (err) {
      lastError = err;
    }
  }

  throw lastError instanceof Error
    ? lastError
    : new Error("MantleDB cast failed");
}
