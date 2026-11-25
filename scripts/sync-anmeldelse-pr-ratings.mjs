/**
 * Synk PriceRunner reviewSummary → frontmatter rating/ratingCount.
 * Usage: node scripts/sync-anmeldelse-pr-ratings.mjs [--dry-run] [--only=slug]
 */
import fs from "node:fs";
import path from "node:path";

const ROOT = path.resolve("content/anmeldelser");
const DRY = process.argv.includes("--dry-run");
const onlyArg = process.argv.find((a) => a.startsWith("--only="));
const ONLY = onlyArg ? onlyArg.slice("--only=".length).split(",") : null;
const UA =
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36";

function parseFrontmatter(raw) {
  if (!raw.startsWith("---\n")) return null;
  const end = raw.indexOf("\n---\n", 4);
  if (end < 0) return null;
  return { fm: raw.slice(4, end), body: raw.slice(end + 5) };
}

function getScalar(fm, key) {
  const m = fm.match(new RegExp(`^${key}:\\s*(.+)$`, "m"));
  if (!m) return null;
  return m[1].trim().replace(/^["']|["']$/g, "");
}

function widgetIds(body) {
  const m = body.match(/<PriceRunnerWidget\b[^>]*>/);
  if (!m) return null;
  const tag = m[0];
  const productId = tag.match(/productId="([^"]+)"/)?.[1];
  const categoryId = tag.match(/categoryId="([^"]+)"/)?.[1];
  if (!productId || !categoryId) return null;
  return { productId, categoryId, slugPath: undefined };
}

function loadCatalog() {
  const src = fs.readFileSync("lib/pricerunner-products.ts", "utf8");
  const entries = [];
  // Match each product block with optional slugPath
  const blockRe =
    /(?:^|\n)\s*(?:"([^"]+)"|([A-Za-zÆØÅæøå0-9][^:\n]*?)):\s*\{([^}]+)\}/g;
  let m;
  while ((m = blockRe.exec(src))) {
    const body = m[3];
    const productId = body.match(/productId:\s*"(\d+)"/)?.[1];
    const categoryId = body.match(/categoryId:\s*"(\d+)"/)?.[1];
    if (!productId || !categoryId) continue;
    const slugPath =
      body.match(/slugPath:\s*\n?\s*"([^"]+)"/)?.[1] ??
      body.match(/slugPath:\s*"([^"]+)"/)?.[1];
    entries.push({
      key: (m[1] ?? m[2]).trim(),
      productId,
      categoryId,
      slugPath,
    });
  }
  return entries;
}

function findCatalogExact(catalog, productName) {
  if (!productName) return null;
  return catalog.find((e) => e.key === productName) ?? null;
}

async function fetchReviewSummary(categoryId, productId, slugPath) {
  const pathPart = slugPath
    ? `/pl/${categoryId}-${productId}/${slugPath.replace(/^\/+/, "")}`
    : `/pl/${categoryId}-${productId}/`;
  const url = `https://www.pricerunner.dk${pathPart}`;

  for (let attempt = 0; attempt < 4; attempt++) {
    if (attempt > 0) await sleep(1500 * attempt);
    const res = await fetch(url, {
      headers: {
        "User-Agent": UA,
        Accept: "text/html,application/xhtml+xml",
        "Accept-Language": "da-DK,da;q=0.9,en;q=0.8",
      },
      signal: AbortSignal.timeout(20000),
      redirect: "follow",
    });
    if (res.status === 429) {
      await sleep(4000 * (attempt + 1));
      continue;
    }
    if (!res.ok) return { error: `HTTP ${res.status}`, url };

    const html = await res.text();
    const match = html.match(
      /<script[^>]*id="initial_payload"[^>]*>([\s\S]*?)<\/script>/
    );
    if (!match?.[1]) {
      // Soft block / empty shell — retry
      if (attempt < 3) continue;
      return { error: "no payload", url };
    }

    const payload = JSON.parse(match[1]);
    const queries = payload?.__DEHYDRATED_QUERY_STATE__?.queries ?? [];
    for (const query of queries) {
      const key = JSON.stringify(query.queryKey ?? "");
      if (!key.includes("product-detail-initial")) continue;
      const data = query.state?.data;
      const average = data?.reviewSummary?.average;
      const count = data?.reviewSummary?.count ?? 0;
      if (
        typeof average === "number" &&
        Number.isFinite(average) &&
        average > 0 &&
        count > 0
      ) {
        return {
          rating: Math.round(average * 100) / 100,
          ratingCount: count,
          url,
        };
      }
      return { error: "no reviewSummary", url, average, count };
    }
    return { error: "no product-detail-initial", url };
  }
  return { error: "retries exhausted", url };
}

function upsertRatings(fm, rating, ratingCount) {
  let next = fm;
  if (/^rating:/m.test(next)) {
    next = next.replace(/^rating:\s*.+$/m, `rating: ${rating}`);
  } else if (/^updatedAt:/m.test(next)) {
    next = next.replace(
      /^(updatedAt:\s*.+)$/m,
      `$1\nrating: ${rating}\nratingCount: ${ratingCount}`
    );
    return next;
  } else {
    return `rating: ${rating}\nratingCount: ${ratingCount}\n` + next;
  }

  if (/^ratingCount:/m.test(next)) {
    next = next.replace(/^ratingCount:\s*.+$/m, `ratingCount: ${ratingCount}`);
  } else {
    next = next.replace(
      /^(rating:\s*.+)$/m,
      `$1\nratingCount: ${ratingCount}`
    );
  }
  return next;
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

/**
 * Undgå at overskrive en solid eksisterende rating med en tynd/forkert SKU
 * (fx 170 → 1). Tillad refresh når ny count er ≥ 40% af gammel, eller gammel mangler.
 */
function shouldWrite(prevCount, nextCount) {
  if (prevCount == null || !Number.isFinite(prevCount) || prevCount <= 0) {
    return true;
  }
  if (nextCount >= prevCount * 0.4) return true;
  if (nextCount >= 50) return true;
  return false;
}

const catalog = loadCatalog();
let files = fs
  .readdirSync(ROOT)
  .filter((f) => f.endsWith(".mdx"))
  .sort();
if (ONLY) {
  files = files.filter((f) => ONLY.some((s) => f.startsWith(s) || f === `${s}.mdx`));
}

const summary = {
  updated: [],
  skippedThin: [],
  unchanged: [],
  noStars: [],
  noProduct: [],
  errors: [],
};

for (const file of files) {
  const filePath = path.join(ROOT, file);
  const raw = fs.readFileSync(filePath, "utf8");
  const parsed = parseFrontmatter(raw);
  if (!parsed) {
    summary.errors.push({ file, error: "bad frontmatter" });
    continue;
  }

  const productName = getScalar(parsed.fm, "productName");
  const fromWidget = widgetIds(parsed.body);
  const fromCatalog = findCatalogExact(catalog, productName);
  const ids = fromWidget
    ? {
        ...fromWidget,
        slugPath: fromCatalog?.slugPath,
      }
    : fromCatalog
      ? {
          productId: fromCatalog.productId,
          categoryId: fromCatalog.categoryId,
          slugPath: fromCatalog.slugPath,
        }
      : null;

  if (!ids) {
    summary.noProduct.push(file);
    continue;
  }

  const result = await fetchReviewSummary(
    ids.categoryId,
    ids.productId,
    ids.slugPath
  );
  await sleep(900);

  if (result.error) {
    if (result.error === "no reviewSummary") {
      summary.noStars.push({
        file,
        productId: ids.productId,
        count: result.count ?? 0,
      });
    } else {
      summary.errors.push({
        file,
        productId: ids.productId,
        error: result.error,
      });
    }
    continue;
  }

  const prevRating = getScalar(parsed.fm, "rating");
  const prevCountRaw = getScalar(parsed.fm, "ratingCount");
  const prevCount = prevCountRaw != null ? Number(prevCountRaw) : null;

  if (!shouldWrite(prevCount, result.ratingCount)) {
    summary.skippedThin.push({
      file,
      kept: `${prevRating}/${prevCount}`,
      pr: `${result.rating}/${result.ratingCount}`,
      productId: ids.productId,
    });
    continue;
  }

  const same =
    prevRating != null &&
    Number(prevRating) === result.rating &&
    prevCount != null &&
    prevCount === result.ratingCount;

  if (same) {
    summary.unchanged.push(file);
    continue;
  }

  const nextFm = upsertRatings(parsed.fm, result.rating, result.ratingCount);
  const nextRaw = `---\n${nextFm}\n---\n${parsed.body}`;
  if (!DRY) fs.writeFileSync(filePath, nextRaw);

  summary.updated.push({
    file,
    from: prevRating ? `${prevRating}/${prevCount}` : null,
    to: `${result.rating}/${result.ratingCount}`,
    productId: ids.productId,
  });
}

console.log(JSON.stringify(summary, null, 2));
console.log(
  `\n${DRY ? "DRY RUN — " : ""}updated=${summary.updated.length} unchanged=${summary.unchanged.length} skippedThin=${summary.skippedThin.length} noStars=${summary.noStars.length} noProduct=${summary.noProduct.length} errors=${summary.errors.length}`
);
