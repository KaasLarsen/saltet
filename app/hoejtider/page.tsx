import type { Metadata } from "next";
import Link from "next/link";
import { getHighlightedHoliday } from "@/lib/holiday-nav";
import { getHolidayCounts } from "@/lib/holidays";
import { absoluteUrl, siteConfig } from "@/lib/seo";

export const metadata: Metadata = {
  title: "Højtider",
  description: `Juleopskrifter, nytår, påske og Mortensaften på ${siteConfig.name} — festmad på tværs af airfryer, grill, ovn og gryde.`,
  alternates: { canonical: absoluteUrl("/hoejtider") },
};

export default function HolidaysIndexPage() {
  const counts = getHolidayCounts();
  const highlighted = getHighlightedHoliday();

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 text-center md:px-8 md:py-16">
      <p className="mb-3 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
        Højtider
      </p>
      <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
        Opskrifter til højtider
      </h1>
      <p className="mx-auto mt-4 max-w-xl leading-relaxed text-bone/55">
        Jul, nytår, påske og Mortensaften — samlet, så du ikke skal lede i
        tags. Kategorierne er stadig tilberedningsmetode.
      </p>
      <div className="mx-auto mt-12 grid max-w-3xl gap-3 sm:grid-cols-2">
        {counts.map(({ holiday, count }) => {
          const isHighlight = holiday.slug === highlighted.holiday.slug;
          return (
            <Link
              key={holiday.slug}
              href={`/hoejtider/${holiday.slug}`}
              className={`group rounded-2xl border-2 bg-ash/50 px-5 py-6 text-left shadow-[3px_3px_0_0_rgba(212,255,0,0.35)] transition-[transform,border-color,box-shadow] hover:-translate-y-0.5 hover:border-herb hover:shadow-[4px_4px_0_0_rgba(212,255,0,0.7)] ${
                isHighlight ? "border-herb" : "border-bone/20"
              }`}
            >
              <div className="flex items-center justify-between gap-3">
                <h2 className="font-serif text-2xl uppercase tracking-wide text-bone transition-colors group-hover:text-herb">
                  {holiday.name}
                </h2>
                {isHighlight ? (
                  <span className="rounded-lg border-2 border-iron bg-herb px-2 py-0.5 text-[10px] font-bold uppercase tracking-[0.12em] text-iron">
                    {highlighted.status === "now" ? "Nu" : "Næste"}
                  </span>
                ) : null}
              </div>
              <p className="mt-2 text-sm leading-relaxed text-bone/50">
                {holiday.description}
              </p>
              <p className="mt-3 text-[11px] font-semibold uppercase tracking-[0.14em] text-smoke">
                {count} opskrift{count === 1 ? "" : "er"}
              </p>
            </Link>
          );
        })}
      </div>
    </div>
  );
}
