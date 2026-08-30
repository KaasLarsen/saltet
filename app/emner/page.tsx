import type { Metadata } from "next";
import Link from "next/link";
import { getTopicCounts } from "@/lib/topics";
import { absoluteUrl, siteConfig } from "@/lib/seo";

export const metadata: Metadata = {
  title: "Emner",
  description: `Sovs, kage, kylling, fisk, vegetar og mere på ${siteConfig.name} — opskrifter efter madtype på tværs af airfryer, grill, ovn og gryde.`,
  alternates: { canonical: absoluteUrl("/emner") },
};

export default function TopicsIndexPage() {
  const counts = getTopicCounts();

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 text-center md:px-8 md:py-16">
      <p className="mb-3 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
        Emner
      </p>
      <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
        Opskrifter efter emne
      </h1>
      <p className="mx-auto mt-4 max-w-xl leading-relaxed text-bone/55">
        Sovs, kylling, brød, snack og mere — samlet efter madtype. Tilberedningsmetoder
        finder du stadig under Opskrifter.
      </p>
      <div className="mx-auto mt-12 grid max-w-3xl gap-3 sm:grid-cols-2">
        {counts.map(({ topic, count }) => (
          <Link
            key={topic.slug}
            href={`/emner/${topic.slug}`}
            className="group rounded-2xl border-2 border-bone/20 bg-ash/50 px-5 py-6 text-left shadow-[3px_3px_0_0_rgba(212,255,0,0.35)] transition-[transform,border-color,box-shadow] hover:-translate-y-0.5 hover:border-herb hover:shadow-[4px_4px_0_0_rgba(212,255,0,0.7)]"
          >
            <h2 className="font-serif text-2xl uppercase tracking-wide text-bone transition-colors group-hover:text-herb">
              {topic.name}
            </h2>
            <p className="mt-2 text-sm leading-relaxed text-bone/50">
              {topic.description}
            </p>
            <p className="mt-3 text-[11px] font-semibold uppercase tracking-[0.14em] text-smoke">
              {count} opskrift{count === 1 ? "" : "er"}
            </p>
          </Link>
        ))}
      </div>
    </div>
  );
}
