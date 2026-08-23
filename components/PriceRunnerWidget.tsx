import Image from "next/image";
import { PRICERUNNER_PRODUCTS } from "@/lib/pricerunner-products";
import {
  formatDkk,
  getPriceRunnerComparison,
} from "@/lib/pricerunner-offers";

interface PriceRunnerWidgetProps {
  query: string;
  label?: string;
  productId?: string;
  categoryId?: string;
  sku?: string;
}

export async function PriceRunnerWidget({
  query,
  label,
  productId: productIdProp,
  categoryId: categoryIdProp,
}: PriceRunnerWidgetProps) {
  const mapped = PRICERUNNER_PRODUCTS[query];
  const productId = productIdProp ?? mapped?.productId;
  const categoryId = categoryIdProp ?? mapped?.categoryId;
  const heading = label ?? mapped?.label ?? query;

  const comparison =
    productId && categoryId
      ? await getPriceRunnerComparison(categoryId, productId)
      : null;

  if (!comparison) {
    return null;
  }

  const lowest = comparison.offers[0];

  return (
    <aside className="my-8 overflow-hidden rounded-2xl border-2 border-bone/15 bg-ash/40">
      <p className="border-b border-bone/10 px-4 py-3 text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
        Se priser — {heading}
      </p>
      <div className="bg-bone text-iron">
        <div className="flex gap-4 px-5 py-5">
          {comparison.image ? (
            <Image
              src={comparison.image}
              alt=""
              width={80}
              height={80}
              className="h-20 w-20 shrink-0 rounded-lg bg-white object-contain"
            />
          ) : null}
          <div>
            <p className="font-serif text-xl leading-snug">{heading}</p>
            <p className="mt-1 text-sm text-iron/70">
              Fra{" "}
              <span className="font-semibold text-iron">
                {formatDkk(lowest.price)}
              </span>{" "}
              hos {lowest.merchant}
            </p>
          </div>
        </div>
        <ul className="divide-y divide-iron/10 border-t border-iron/10">
          {comparison.offers.map((offer) => (
            <li key={`${offer.merchant}-${offer.price}`}>
              <a
                href={offer.href}
                target="_blank"
                rel="noopener noreferrer sponsored"
                className="flex items-center justify-between gap-3 px-5 py-3 text-sm hover:bg-herb/15"
              >
                <span>
                  <span className="font-semibold">{offer.merchant}</span>
                  <span className="ml-2 text-xs text-iron/50">
                    {offer.inStock ? "På lager" : "Ikke på lager"}
                    {offer.shipping ? ` · ${offer.shipping}` : ""}
                  </span>
                </span>
                <span className="shrink-0 text-right">
                  <span className="block font-semibold">
                    {formatDkk(offer.price)}
                  </span>
                  <span className="text-[10px] font-bold uppercase tracking-[0.12em] text-herb">
                    Gå til butik
                  </span>
                </span>
              </a>
            </li>
          ))}
        </ul>
      </div>
    </aside>
  );
}
