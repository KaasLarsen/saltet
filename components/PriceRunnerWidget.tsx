import { formatDkk, getPriceRunnerComparison } from "@/lib/pricerunner-offers";
import { PRICERUNNER_PRODUCTS } from "@/lib/pricerunner-products";
import { pricerunnerProductUrl, pricerunnerSearchUrl } from "@/lib/pricerunner";
import { PriceRunnerOfficialWidget } from "@/components/PriceRunnerOfficialWidget";
import {
  outboundLinkAttrs,
  withOutboundSurface,
  type OutboundSurface,
} from "@/lib/outbound";

interface PriceRunnerWidgetProps {
  query: string;
  label?: string;
  productId?: string;
  categoryId?: string;
  sku?: string;
  /** Page type for click attribution — set by MDX wrappers / page shells. */
  surface?: OutboundSurface;
}

/**
 * PriceRunner-priser: SSR-forhandlerliste (pålidelig) + officiel widget som bonus.
 * Nye produkter med få tilbud (fx CRISPi DualZone) viser stadig mindst ét klart tilbud.
 */
export async function PriceRunnerWidget({
  query,
  label,
  productId: productIdProp,
  categoryId: categoryIdProp,
  surface = "other",
}: PriceRunnerWidgetProps) {
  const mapped = PRICERUNNER_PRODUCTS[query];
  const productId = productIdProp ?? mapped?.productId;
  const categoryId = categoryIdProp ?? mapped?.categoryId;
  const slugPath = mapped?.slugPath;
  const heading = label ?? mapped?.label ?? query;
  const productHref = withOutboundSurface(
    productId && categoryId
      ? pricerunnerProductUrl(categoryId, productId, slugPath)
      : pricerunnerSearchUrl(query),
    surface
  );
  const searchHref = withOutboundSurface(pricerunnerSearchUrl(query), surface);
  const linkAttrs = outboundLinkAttrs(surface, { merchant: "PriceRunner" });

  const comparison =
    productId && categoryId
      ? await getPriceRunnerComparison(categoryId, productId, slugPath)
      : null;

  if (!productId) {
    return (
      <aside className="my-8 overflow-hidden rounded-2xl border-2 border-bone/15 bg-ash/40">
        <div className="flex items-center justify-between gap-3 border-b border-bone/10 px-4 py-3">
          <p className="text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
            Se priser — {heading}
          </p>
          <p className="text-[10px] font-bold uppercase tracking-[0.14em] text-bone/35">
            Annonce
          </p>
        </div>
        <a
          href={searchHref}
          target="_blank"
          rel="noopener noreferrer sponsored"
          className="block bg-herb px-5 py-4 text-sm font-semibold text-iron hover:bg-herb/85"
          {...linkAttrs}
        >
          Se laveste pris hos PriceRunner
        </a>
      </aside>
    );
  }

  const offers = comparison?.offers ?? [];

  return (
    <aside className="my-8 overflow-hidden rounded-2xl border-2 border-bone/15 bg-ash/40">
      <div className="flex items-center justify-between gap-3 border-b border-bone/10 px-4 py-3">
        <p className="text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
          Se priser — {heading}
        </p>
        <p className="text-[10px] font-bold uppercase tracking-[0.14em] text-bone/35">
          Annonce
        </p>
      </div>

      {offers.length > 0 ? (
        <ul className="divide-y divide-bone/10 bg-ash/20">
          {offers.map((offer) => (
            <li key={`${offer.merchant}-${offer.href}`}>
              <a
                href={withOutboundSurface(offer.href, surface)}
                target="_blank"
                rel="noopener noreferrer sponsored"
                className="flex items-center justify-between gap-4 px-5 py-3.5 transition-colors hover:bg-herb/10"
                {...outboundLinkAttrs(surface, { merchant: offer.merchant })}
              >
                <span className="min-w-0">
                  <span className="block truncate text-sm font-semibold text-bone">
                    {offer.merchant}
                  </span>
                  {offer.shipping ? (
                    <span className="mt-0.5 block text-[11px] text-bone/45">
                      {offer.shipping}
                      {offer.inStock ? " · På lager" : ""}
                    </span>
                  ) : offer.inStock ? (
                    <span className="mt-0.5 block text-[11px] text-bone/45">
                      På lager
                    </span>
                  ) : null}
                </span>
                <span className="shrink-0 font-serif text-lg text-herb">
                  {formatDkk(offer.price)}
                </span>
              </a>
            </li>
          ))}
        </ul>
      ) : null}

      <div className="border-t border-bone/10 px-5 py-4">
        <a
          href={productHref}
          target="_blank"
          rel="noopener noreferrer sponsored"
          className="inline-flex w-full items-center justify-center gap-2 rounded-xl border-2 border-herb bg-herb px-4 py-2.5 text-sm font-semibold text-iron transition-colors hover:bg-herb/85 sm:w-auto"
          {...linkAttrs}
        >
          Se laveste pris hos PriceRunner
          <span aria-hidden>→</span>
        </a>
      </div>

      <div className="bg-bone p-2 sm:p-3">
        <PriceRunnerOfficialWidget
          productId={productId}
          fallbackHref={productHref}
          surface={surface}
        />
      </div>

      <div className="flex flex-wrap gap-x-4 gap-y-2 border-t border-bone/10 px-5 py-3 text-[12px]">
        <a
          href={productHref}
          target="_blank"
          rel="noopener noreferrer sponsored"
          className="font-semibold text-herb underline-offset-2 hover:underline"
          {...linkAttrs}
        >
          Find billigste forhandler
        </a>
        {offers.length <= 1 ? (
          <a
            href={searchHref}
            target="_blank"
            rel="noopener noreferrer sponsored"
            className="text-bone/55 underline-offset-2 hover:text-herb hover:underline"
            {...linkAttrs}
          >
            Søg flere forhandlere
          </a>
        ) : null}
      </div>
    </aside>
  );
}
