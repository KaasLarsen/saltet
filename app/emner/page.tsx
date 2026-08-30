import type { Metadata } from "next";
import { TopicCard } from "@/components/TopicCard";
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
        {counts.length} emner — vælg et og se opskrifterne. Tilberedningsmetoder
        finder du stadig under Opskrifter.
      </p>

      <div className="mt-12 grid gap-10 text-left sm:grid-cols-2 lg:grid-cols-3">
        {counts.map(({ topic, count, image, imageAlt }, index) => (
          <TopicCard
            key={topic.slug}
            topic={topic}
            count={count}
            image={image}
            imageAlt={imageAlt}
            priority={index < 3}
          />
        ))}
      </div>
    </div>
  );
}
