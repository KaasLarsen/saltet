export const PRICERUNNER_ADRUNNER_ID = "adrunner_dk_online-opskrift";

export const PRICERUNNER_ORIGIN = "https://www.pricerunner.dk";

export function pricerunnerSearchUrl(query: string): string {
  const params = new URLSearchParams({
    q: query,
    adrunnerId: PRICERUNNER_ADRUNNER_ID,
  });
  return `${PRICERUNNER_ORIGIN}/search?${params.toString()}`;
}

export function pricerunnerWidgetSrc(opts: {
  query: string;
  productId?: string;
  sku?: string;
}): string {
  const params = new URLSearchParams({
    adrunnerId: PRICERUNNER_ADRUNNER_ID,
  });

  if (opts.sku) params.set("sku", opts.sku);

  if (opts.productId) {
    return `${PRICERUNNER_ORIGIN}/widget/cheapest/backlink/${opts.productId}?${params.toString()}`;
  }

  params.set("q", opts.query);
  return `${PRICERUNNER_ORIGIN}/widget?${params.toString()}`;
}
