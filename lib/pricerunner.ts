export const PRICERUNNER_ADRUNNER_ID = "adrunner_dk_online-opskrift";

export const PRICERUNNER_ORIGIN = "https://www.pricerunner.dk";

const PUBLISHER_WIDGETS_ORIGIN =
  "https://api.pricerunner.com/publisher-widgets";

function withRefSite(url: URL): string {
  url.searchParams.set("ref-site", PRICERUNNER_ADRUNNER_ID);
  return url.toString();
}

export function pricerunnerSearchUrl(query: string): string {
  const url = new URL("/search", PRICERUNNER_ORIGIN);
  url.searchParams.set("q", query);
  return withRefSite(url);
}

/**
 * Byg produkt-URL. Korte `/pl/{cat}-{id}/`-URLs kan redirecte til kategori —
 * brug `slugPath` (efter id) når den kendes, fx
 * `Frituregryder/Ninja-CRISPi-4-i-1-FN101EUGY-Sammenlign-Priser`.
 */
export function pricerunnerProductUrl(
  categoryId: string,
  productId: string,
  slugPath?: string
): string {
  const base = `/pl/${categoryId}-${productId}`;
  const path = slugPath
    ? `${base}/${slugPath.replace(/^\/+/, "")}`
    : `${base}/`;
  const url = new URL(path, PRICERUNNER_ORIGIN);
  return withRefSite(url);
}

export function pricerunnerGotoStoreUrl(path: string): string {
  const url = new URL(path, PRICERUNNER_ORIGIN);
  return withRefSite(url);
}

export function pricerunnerProductWidgetSrc(
  productId: string,
  widgetId: string,
  offerLimit = 5
): string {
  const params = new URLSearchParams({
    productId,
    widgetId,
    partnerId: PRICERUNNER_ADRUNNER_ID,
    offerLimit: String(offerLimit),
  });
  return `${PUBLISHER_WIDGETS_ORIGIN}/dk/product.js?${params.toString()}`;
}
