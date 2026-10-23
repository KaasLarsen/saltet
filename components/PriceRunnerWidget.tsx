import { formatDkk, getPriceRunnerComparison } from "@/lib/pricerunner-offers";
import { PRICERUNNER_PRODUCTS } from "@/lib/pricerunner-products";
import { pricerunnerProductUrl, pricerunnerSearchUrl } from "@/lib/pricerunner";
import { PriceRunnerOfficialWidget } from "@/components/PriceRunnerOfficialWidget";

interface PriceRunnerWidgetProps {
  query: string;
  label?: string;
  productId?: string;
  categoryId?: string;
  sku?: string;
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
}: PriceRunnerWidgetProps) {
  const mapped = PRICERUNNER_PRODUCTS[query];
  const productId = productIdProp ?? mapped?.productId;
  const categoryId = categoryIdProp ?? mapped?.categoryId;
  const slugPath = mapped?.slugPath;
  const heading = label ?? mapped?.label ?? query;
  const productHref =
    productId && categoryId
      ? pricerunnerProductUrl(categoryId, productId, slugPath)
      : pricerunnerSearchUrl(query);
  const searchHref = pricerunnerSearchUrl(query);

  const comparison =
    productId && categoryId
      ? await getPriceRunnerComparison(categoryId, productId, slugPath)
      : null;

  if (!productId) {
    return (
      <aside className="my-8 overflow-hidden rounded-2xl border-2 border-bone/15 bg-ash/40">
        <p className="border-b border-bone/10 px-4 py-3 text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
          Se priser — {heading}
        </p>
        <a
          href={searchHref}
          target="_blank"
          rel="noopener noreferrer sponsored"
          className="block bg-bone px-5 py-4 text-sm font-semibold text-iron hover:bg-herb/15"
        >
          Sammenlign priser på PriceRunner
        </a>
      </aside>
    );
  }

  const offers = comparison?.offers ?? [];

  return (
    <aside className="my-8 overflow-hidden rounded-2xl border-2 border-bone/15 bg-ash/40">
      <p className="border-b border-bone/10 px-4 py-3 text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
        Se priser — {heading}
      </p>

      {offers.length > 0 ? (
        <ul className="divide-y divide-bone/10 bg-ash/20">
          {offers.map((offer) => (
            <li key={`${offer.merchant}-${offer.href}`}>
              <a
                href={offer.href}
                target="_blank"
                rel="noopener noreferrer sponsored"
                className="flex items-center justify-between gap-4 px-5 py-3.5 transition-colors hover:bg-herb/10"
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

      <div className="bg-bone p-2 sm:p-3">
        <PriceRunnerOfficialWidget
          productId={productId}
          fallbackHref={productHref}
        />
      </div>

      <div className="flex flex-wrap gap-x-4 gap-y-2 border-t border-bone/10 px-5 py-3 text-[12px]">
        <a
          href={productHref}
          target="_blank"
          rel="noopener noreferrer sponsored"
          className="font-semibold text-herb underline-offset-2 hover:underline"
        >
          Åbn på PriceRunner
        </a>
        {offers.length <= 1 ? (
          <a
            href={searchHref}
            target="_blank"
            rel="noopener noreferrer sponsored"
            className="text-bone/55 underline-offset-2 hover:text-herb hover:underline"
          >
            Søg flere forhandlere
          </a>
        ) : null}
      </div>
    </aside>
  );
}
