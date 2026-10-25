import type { Metadata } from "next";
import Link from "next/link";
import { getHighlightedSeason } from "@/lib/season-nav";
import { getSeasonCounts } from "@/lib/seasons";
import { absoluteUrl, siteConfig } from "@/lib/seo";

export const metadata: Metadata = {
  title: "Sæson",
  description: `Efterår, vinter, forår og sommer på ${siteConfig.name} — sæsonopskrifter med rodfrugter, grill, svampe og det der hører årstiden til.`,
  alternates: { canonical: absoluteUrl("/saeson") },
};

export default function SeasonsIndexPage() {
  const counts = getSeasonCounts();
  const highlighted = getHighlightedSeason();

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 text-center md:px-8 md:py-16">
      <p className="mb-3 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
        Sæson
      </p>
      <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
        Opskrifter til sæsonen
      </h1>
      <p className="mx-auto mt-4 max-w-xl leading-relaxed text-bone/55">
        Forår, sommer, efterår og vinter — samlet, så du laver mad der matcher
        markedet og vejret. Kategorierne er stadig tilberedningsmetode.
      </p>
      <div className="mx-auto mt-12 grid max-w-3xl gap-3 sm:grid-cols-2">
        {counts.map(({ season, count }) => {
          const isHighlight = season.slug === highlighted.season.slug;
          return (
            <Link
              key={season.slug}
              href={`/saeson/${season.slug}`}
              className={`group rounded-2xl border-2 bg-ash/50 px-5 py-6 text-left shadow-[3px_3px_0_0_rgba(212,255,0,0.35)] transition-[transform,border-color,box-shadow] hover:-translate-y-0.5 hover:border-herb hover:shadow-[4px_4px_0_0_rgba(212,255,0,0.7)] ${
                isHighlight ? "border-herb" : "border-bone/20"
              }`}
            >
              <div className="flex items-center justify-between gap-3">
                <h2 className="font-serif text-2xl uppercase tracking-wide text-bone transition-colors group-hover:text-herb">
                  {season.name}
                </h2>
                {isHighlight ? (
                  <span className="rounded-lg border-2 border-iron bg-herb px-2 py-0.5 text-[10px] font-bold uppercase tracking-[0.12em] text-iron">
                    {highlighted.status === "now" ? "Nu" : "Næste"}
                  </span>
                ) : null}
              </div>
              <p className="mt-2 text-sm leading-relaxed text-bone/50">
                {season.description}
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
