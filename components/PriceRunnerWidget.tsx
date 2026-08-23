"use client";

import { pricerunnerSearchUrl, pricerunnerWidgetSrc } from "@/lib/pricerunner";

interface PriceRunnerWidgetProps {
  query: string;
  label?: string;
  productId?: string;
  sku?: string;
}

export function PriceRunnerWidget({
  query,
  label,
  productId,
  sku,
}: PriceRunnerWidgetProps) {
  const heading = label ?? query;
  const searchUrl = pricerunnerSearchUrl(query);
  const src = pricerunnerWidgetSrc({ query, productId, sku });

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
      <iframe
        title={`PriceRunner: ${heading}`}
        src={src}
        className="h-[280px] w-full bg-bone"
        loading="lazy"
        referrerPolicy="no-referrer-when-downgrade"
      />
      <p className="px-4 py-2.5 text-[11px] leading-relaxed text-bone/40">
        Priser via PriceRunner. Vi kan tjene provision, hvis du køber via
        linket. Adrunner: adrunner_dk_online-opskrift.
      </p>
    </aside>
  );
}
