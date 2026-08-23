export const PRICERUNNER_ADRUNNER_ID = "adrunner_dk_online-opskrift";

export const PRICERUNNER_ORIGIN = "https://www.pricerunner.dk";

export const PRICERUNNER_WIDGET_API =
  "https://api.pricerunner.com/publisher-widgets";

export type PriceRunnerWidgetKind =
  | "product"
  | "singleproduct"
  | "bestprice"
  | "category"
  | "products";

export function pricerunnerSearchUrl(query: string): string {
  const params = new URLSearchParams({
    q: query,
    adrunnerId: PRICERUNNER_ADRUNNER_ID,
  });
  return `${PRICERUNNER_ORIGIN}/search?${params.toString()}`;
}

export function pricerunnerWidgetId(
  kind: PriceRunnerWidgetKind,
  key: string
): string {
  return `pr-${kind}-widget-${key}`;
}

export function pricerunnerPublisherScriptSrc(opts: {
  kind: PriceRunnerWidgetKind;
  widgetId: string;
  productId?: string;
  categoryId?: string;
  productIds?: string;
  offerLimit?: number;
  productLimit?: number;
}): string {
  const params = new URLSearchParams({
    widgetId: opts.widgetId,
    partnerId: PRICERUNNER_ADRUNNER_ID,
  });

  if (opts.productId) params.set("productId", opts.productId);
  if (opts.categoryId) params.set("categoryId", opts.categoryId);
  if (opts.productIds) params.set("productIds", opts.productIds);

  if (opts.kind === "product") {
    params.set("offerLimit", String(opts.offerLimit ?? 5));
    params.set("onlyInStock", "true");
    params.set("offerOrigin", "NATIONAL");
  }

  if (opts.kind === "category") {
    params.set("productLimit", String(opts.productLimit ?? 4));
    params.set("onlyInStock", "true");
  }

  return `${PRICERUNNER_WIDGET_API}/dk/${opts.kind}.js?${params.toString()}`;
}
