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

export function pricerunnerProductUrl(
  categoryId: string,
  productId: string
): string {
  const url = new URL(`/pl/${categoryId}-${productId}/`, PRICERUNNER_ORIGIN);
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
