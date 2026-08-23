import { PRICERUNNER_PRODUCTS } from "@/lib/pricerunner-products";
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

export function PriceRunnerWidget({
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
        linket. Adrunner: adrunner_dk_online-opskrift.
      </p>
    </aside>
  );
}
