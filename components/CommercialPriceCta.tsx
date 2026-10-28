import {
  outboundLinkAttrs,
  withOutboundSurface,
  type OutboundSurface,
} from "@/lib/outbound";
import {
  pricerunnerProductUrl,
  pricerunnerSearchUrl,
} from "@/lib/pricerunner";
import { PRICERUNNER_PRODUCTS } from "@/lib/pricerunner-products";

interface CommercialPriceCtaProps {
  surface: OutboundSurface;
  /** Search query or catalog key in PRICERUNNER_PRODUCTS. */
  query: string;
  label?: string;
  productId?: string;
  categoryId?: string;
  className?: string;
}

/**
 * Early, active price CTA for grej/anmeldelse — Saltet herb styling,
 * not generic Amazon-green “Køb nu”.
 */
export function CommercialPriceCta({
  surface,
  query,
  label,
  productId: productIdProp,
  categoryId: categoryIdProp,
  className = "",
}: CommercialPriceCtaProps) {
  const mapped = PRICERUNNER_PRODUCTS[query];
  const productId = productIdProp ?? mapped?.productId;
  const categoryId = categoryIdProp ?? mapped?.categoryId;
  const slugPath = mapped?.slugPath;
  const heading = label ?? mapped?.label ?? query;
  const rawHref =
    productId && categoryId
      ? pricerunnerProductUrl(categoryId, productId, slugPath)
      : pricerunnerSearchUrl(query);
  const href = withOutboundSurface(rawHref, surface);

  return (
    <aside
      className={`mt-8 overflow-hidden rounded-2xl border-2 border-herb/45 bg-herb/10 text-left shadow-[4px_4px_0_0_rgba(212,255,0,0.25)] ${className}`}
      aria-label="Se priser"
    >
      <div className="flex items-center justify-between gap-3 border-b border-herb/25 px-4 py-3">
        <p className="text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
          Klar til at købe?
        </p>
        <p className="text-[10px] font-bold uppercase tracking-[0.14em] text-bone/35">
          Annonce
        </p>
      </div>
      <div className="px-5 py-5">
        <p className="font-serif text-xl uppercase tracking-wide text-bone">
          {heading}
        </p>
        <p className="mt-2 text-sm leading-relaxed text-bone/65">
          Se laveste pris hos forhandlerne — sammenlign på PriceRunner før du
          køber.
        </p>
        <a
          href={href}
          target="_blank"
          rel="noopener noreferrer sponsored"
          className="mt-4 inline-flex items-center gap-2 rounded-xl border-2 border-herb bg-herb px-4 py-2.5 text-sm font-semibold text-iron transition-colors hover:bg-herb/85"
          {...outboundLinkAttrs(surface, { merchant: "PriceRunner" })}
        >
          Se laveste pris hos PriceRunner
          <span aria-hidden>→</span>
        </a>
      </div>
    </aside>
  );
}
