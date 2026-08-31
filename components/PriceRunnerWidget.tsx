import { PriceRunnerOfficialWidget } from "@/components/PriceRunnerOfficialWidget";
import { PRICERUNNER_PRODUCTS } from "@/lib/pricerunner-products";
import { pricerunnerProductUrl, pricerunnerSearchUrl } from "@/lib/pricerunner";

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
  const fallbackHref =
    productId && categoryId
      ? pricerunnerProductUrl(categoryId, productId)
      : pricerunnerSearchUrl(query);

  if (!productId) {
    return (
      <aside className="my-8 overflow-hidden rounded-2xl border-2 border-bone/15 bg-ash/40">
        <p className="border-b border-bone/10 px-4 py-3 text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
          Se priser — {heading}
        </p>
        <a
          href={fallbackHref}
          target="_blank"
          rel="noopener noreferrer sponsored"
          className="block bg-bone px-5 py-4 text-sm font-semibold text-iron hover:bg-herb/15"
        >
          Sammenlign priser på PriceRunner
        </a>
      </aside>
    );
  }

  return (
    <aside className="my-8 overflow-hidden rounded-2xl border-2 border-bone/15 bg-ash/40">
      <p className="border-b border-bone/10 px-4 py-3 text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
        Se priser — {heading}
      </p>
      <div className="bg-bone p-3">
        <PriceRunnerOfficialWidget
          productId={productId}
          fallbackHref={fallbackHref}
        />
      </div>
    </aside>
  );
}
