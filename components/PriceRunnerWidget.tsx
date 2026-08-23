"use client";

import { useEffect } from "react";
import {
  pricerunnerPublisherScriptSrc,
  pricerunnerSearchUrl,
  pricerunnerWidgetId,
  type PriceRunnerWidgetKind,
} from "@/lib/pricerunner";

const QUERY_RESOLVE: Record<
  string,
  { productId?: string; categoryId?: string }
> = {
  kødhakker: { categoryId: "10023" },
  "kødhakker tilbehør røremaskine": { productId: "5167693" },
  vakuumpakker: { categoryId: "10021" },
  "Lodge støbejernspande": { productId: "3202827022" },
};

interface PriceRunnerWidgetProps {
  query: string;
  label?: string;
  productId?: string;
  categoryId?: string;
  sku?: string;
  kind?: PriceRunnerWidgetKind;
  offerLimit?: number;
}

export function PriceRunnerWidget({
  query,
  label,
  productId: productIdProp,
  categoryId: categoryIdProp,
  kind: kindProp,
  offerLimit,
}: PriceRunnerWidgetProps) {
  const heading = label ?? query;
  const searchUrl = pricerunnerSearchUrl(query);
  const resolved = QUERY_RESOLVE[query] ?? {};
  const productId = productIdProp ?? resolved.productId;
  const categoryId = categoryIdProp ?? resolved.categoryId;
  const kind: PriceRunnerWidgetKind | undefined =
    kindProp ??
    (categoryId ? "category" : productId ? "product" : undefined);
  const key = categoryId ?? productId ?? "";
  const widgetId = kind && key ? pricerunnerWidgetId(kind, key) : "";
  const scriptSrc =
    kind && widgetId
      ? pricerunnerPublisherScriptSrc({
          kind,
          widgetId,
          productId,
          categoryId,
          offerLimit,
        })
      : "";

  useEffect(() => {
    if (!scriptSrc) return;
    const script = document.createElement("script");
    script.src = scriptSrc;
    script.async = true;
    document.body.appendChild(script);
    return () => {
      script.remove();
    };
  }, [scriptSrc]);

  return (
    <aside className="my-8 overflow-hidden rounded-2xl border-2 border-bone/15 bg-ash/40">
      <div className="flex flex-wrap items-center justify-between gap-2 border-b border-bone/10 px-4 py-3">
        <p className="text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
          Se priser — {heading}
        </p>
        <a
          href={searchUrl}
          target="_blank"
          rel="noopener noreferrer sponsored"
          className="text-[11px] font-semibold uppercase tracking-[0.12em] text-bone/55 underline decoration-herb/40 underline-offset-2 hover:text-herb"
        >
          Åbn på PriceRunner
        </a>
      </div>
      {widgetId ? (
        <div
          id={widgetId}
          className="min-h-[220px] w-full bg-bone px-3 py-3"
          style={{ display: "block", width: "100%" }}
        />
      ) : (
        <div className="bg-bone px-4 py-5 text-iron">
          <p className="text-sm leading-relaxed">
            Sammenlign aktuelle priser på {heading.toLowerCase()} hos danske
            butikker.
          </p>
          <a
            href={searchUrl}
            target="_blank"
            rel="noopener noreferrer sponsored"
            className="mt-3 inline-block text-sm font-semibold uppercase tracking-[0.08em] text-herb underline underline-offset-2"
          >
            Se priser på PriceRunner
          </a>
        </div>
      )}
      <p className="px-4 py-2.5 text-[11px] leading-relaxed text-bone/40">
        Priser via PriceRunner. Vi kan tjene provision, hvis du køber via
        linket. Adrunner: adrunner_dk_online-opskrift.
      </p>
    </aside>
  );
}
