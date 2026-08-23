import Image from "next/image";
import { PRICERUNNER_PRODUCTS } from "@/lib/pricerunner-products";
import {
  formatDkk,
  getPriceRunnerComparison,
} from "@/lib/pricerunner-offers";
import {
  pricerunnerProductUrl,
  pricerunnerSearchUrl,
} from "@/lib/pricerunner";

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
  const href =
    productId && categoryId
      ? pricerunnerProductUrl(categoryId, productId)
      : pricerunnerSearchUrl(query);

  const comparison =
    productId && categoryId
      ? await getPriceRunnerComparison(categoryId, productId)
      : null;

  if (!comparison) {
    return (
      <aside className="my-8 overflow-hidden rounded-2xl border-2 border-bone/15 bg-ash/40">
        <p className="border-b border-bone/10 px-4 py-3 text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
          Se priser — {heading}
        </p>
        <div className="bg-bone px-5 py-6 text-iron">
          <p className="font-serif text-xl leading-snug">{heading}</p>
          <p className="mt-2 text-sm leading-relaxed text-iron/70">
            Aktuelle priser hos danske butikker på PriceRunner.
          </p>
          <a
            href={href}
            target="_blank"
            rel="noopener noreferrer sponsored"
            className="mt-4 inline-block rounded-full bg-herb px-5 py-2.5 text-[11px] font-bold uppercase tracking-[0.12em] text-stone hover:brightness-110"
          >
            Sammenlign priser
          </a>
        </div>
        <p className="px-4 py-2.5 text-[11px] leading-relaxed text-bone/40">
          Priser via PriceRunner. Vi kan tjene provision, hvis du køber via
          linket.
        </p>
      </aside>
    );
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
              Fra <span className="font-semibold text-iron">{formatDkk(lowest.price)}</span>{" "}
              hos {lowest.merchant}
            </p>
          </div>
        </div>
        <ul className="divide-y divide-iron/10 border-t border-iron/10">
          {comparison.offers.map((offer) => (
            <li
              key={`${offer.merchant}-${offer.price}`}
              className="flex items-baseline justify-between gap-3 px-5 py-2.5 text-sm"
            >
              <span>
                {offer.merchant}
                <span className="ml-2 text-xs text-iron/50">
                  {offer.inStock ? "På lager" : "Ikke på lager"}
                  {offer.shipping ? ` · ${offer.shipping}` : ""}
                </span>
              </span>
              <span className="shrink-0 font-semibold">{formatDkk(offer.price)}</span>
            </li>
          ))}
        </ul>
        <div className="px-5 pb-5 pt-3">
          <a
            href={comparison.href}
            target="_blank"
            rel="noopener noreferrer sponsored"
            className="inline-block rounded-full bg-herb px-5 py-2.5 text-[11px] font-bold uppercase tracking-[0.12em] text-stone hover:brightness-110"
          >
            Sammenlign priser
          </a>
        </div>
      </div>
      <p className="px-4 py-2.5 text-[11px] leading-relaxed text-bone/40">
        Priser via PriceRunner. Vi kan tjene provision, hvis du køber via
        linket.
      </p>
    </aside>
  );
}
