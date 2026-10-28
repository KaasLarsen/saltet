/**
 * Outbound affiliate/PriceRunner attribution.
 * `data-outbound-surface` lets analytics split clicks by page type
 * (opskrift vs grej vs anmeldelse vs guide vs home).
 */

export type OutboundSurface =
  | "recipe"
  | "grej"
  | "anmeldelse"
  | "guide"
  | "home"
  | "other";

export const OUTBOUND_ATTR = "data-outbound" as const;
export const OUTBOUND_SURFACE_ATTR = "data-outbound-surface" as const;
export const OUTBOUND_OFFER_ATTR = "data-outbound-offer" as const;
export const OUTBOUND_MERCHANT_ATTR = "data-outbound-merchant" as const;

export interface OutboundAttrs {
  [OUTBOUND_ATTR]: "";
  [OUTBOUND_SURFACE_ATTR]: OutboundSurface;
  [OUTBOUND_OFFER_ATTR]?: string;
  [OUTBOUND_MERCHANT_ATTR]?: string;
}

export function outboundLinkAttrs(
  surface: OutboundSurface,
  options?: { offerId?: string; merchant?: string }
): OutboundAttrs {
  const attrs: OutboundAttrs = {
    [OUTBOUND_ATTR]: "",
    [OUTBOUND_SURFACE_ATTR]: surface,
  };
  if (options?.offerId) attrs[OUTBOUND_OFFER_ATTR] = options.offerId;
  if (options?.merchant) attrs[OUTBOUND_MERCHANT_ATTR] = options.merchant;
  return attrs;
}

/** Append surface so PriceRunner / partner reports can segment clicks. */
export function withOutboundSurface(
  href: string,
  surface: OutboundSurface
): string {
  try {
    const url = new URL(href);
    url.searchParams.set("saltet_surface", surface);
    return url.toString();
  } catch {
    return href;
  }
}

const PRICE_RUNNER_WIDGET_RE =
  /<PriceRunnerWidget\s+([\s\S]*?)\s*\/>/;

function attrValue(attrs: string, name: string): string | undefined {
  const match = attrs.match(new RegExp(`${name}="([^"]*)"`));
  return match?.[1];
}

/** First PriceRunner widget in MDX — used for early commercial CTAs. */
export function extractPrimaryPriceRunnerFromContent(content: string): {
  query: string;
  label?: string;
  productId?: string;
  categoryId?: string;
} | null {
  const match = content.match(PRICE_RUNNER_WIDGET_RE);
  if (!match) return null;
  const attrs = match[1];
  const query = attrValue(attrs, "query");
  if (!query) return null;
  return {
    query,
    label: attrValue(attrs, "label"),
    productId: attrValue(attrs, "productId"),
    categoryId: attrValue(attrs, "categoryId"),
  };
}
