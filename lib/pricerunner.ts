export const PRICERUNNER_ADRUNNER_ID = "adrunner_dk_online-opskrift";

export const PRICERUNNER_ORIGIN = "https://www.pricerunner.dk";

export function pricerunnerSearchUrl(query: string): string {
  const params = new URLSearchParams({
    q: query,
    adrunnerId: PRICERUNNER_ADRUNNER_ID,
  });
  return `${PRICERUNNER_ORIGIN}/search?${params.toString()}`;
}

export function pricerunnerProductUrl(
  categoryId: string,
  productId: string
): string {
  const params = new URLSearchParams({
    adrunnerId: PRICERUNNER_ADRUNNER_ID,
  });
  return `${PRICERUNNER_ORIGIN}/pl/${categoryId}-${productId}/?${params.toString()}`;
}

export function pricerunnerGotoStoreUrl(path: string): string {
  const url = new URL(path, PRICERUNNER_ORIGIN);
  url.searchParams.set("adrunnerId", PRICERUNNER_ADRUNNER_ID);
  return url.toString();
}
