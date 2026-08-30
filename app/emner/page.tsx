import type { Metadata } from "next";
import Link from "next/link";
import { CategoryFilters } from "@/components/CategoryFilters";
import { getAllTopicRecipes, getTopicCounts } from "@/lib/topics";
import { absoluteUrl, siteConfig } from "@/lib/seo";
import type { Recipe, RecipeFrontmatter } from "@/lib/types";

export const metadata: Metadata = {
  title: "Emner",
  description: `Sovs, kage, kylling, fisk, vegetar og mere på ${siteConfig.name} — opskrifter efter madtype på tværs af airfryer, grill, ovn og gryde.`,
  alternates: { canonical: absoluteUrl("/emner") },
};

function toListItem(recipe: Recipe): RecipeFrontmatter {
  const { content: _content, ...rest } = recipe;
  return rest;
}

export default function TopicsIndexPage() {
  const counts = getTopicCounts();
  const recipes = getAllTopicRecipes().map(toListItem);

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 text-center md:px-8 md:py-16">
      <p className="mb-3 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
        Emner
      </p>
      <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
        Opskrifter efter emne
      </h1>
      <p className="mx-auto mt-4 max-w-xl leading-relaxed text-bone/55">
        {recipes.length} opskrifter på tværs af {counts.length} emner — filtrér
        efter madtype, metode, tid og mere. Tilberedningsmetoder finder du
        stadig under Opskrifter.
      </p>

      <div className="mx-auto mt-10 grid max-w-4xl gap-2 sm:grid-cols-2 lg:grid-cols-3">
        {counts.map(({ topic, count }) => (
          <Link
            key={topic.slug}
            href={`/emner/${topic.slug}`}
            className="group rounded-xl border-2 border-bone/20 bg-ash/50 px-4 py-3 text-left shadow-[2px_2px_0_0_rgba(212,255,0,0.25)] transition-[transform,border-color,box-shadow] hover:-translate-y-0.5 hover:border-herb hover:shadow-[3px_3px_0_0_rgba(212,255,0,0.55)]"
          >
            <div className="flex items-baseline justify-between gap-2">
              <h2 className="font-serif text-lg uppercase tracking-wide text-bone transition-colors group-hover:text-herb">
                {topic.name}
              </h2>
              <span className="text-[10px] font-semibold uppercase tracking-[0.12em] text-smoke">
                {count}
              </span>
            </div>
          </Link>
        ))}
      </div>

      <CategoryFilters
        recipes={recipes}
        showTopicFilter
        searchPlaceholder="Søg i emner…"
      />
    </div>
  );
}
