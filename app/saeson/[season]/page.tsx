import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { CategoryFilters } from "@/components/CategoryFilters";
import { GuideCard } from "@/components/GuideCard";
import { getGuide } from "@/lib/guides";
import { getHoliday } from "@/lib/holidays";
import { MIN_RECIPES_FOR_FILTERS } from "@/lib/recipe-filters";
import { toRecipeListItem } from "@/lib/recipes";
import {
  getAllSeasonSlugs,
  getRecipesBySeason,
  getSeason,
} from "@/lib/seasons";
import { buildSeasonMetadata } from "@/lib/seo";

interface SeasonPageProps {
  params: Promise<{ season: string }>;
}

export async function generateStaticParams() {
  return getAllSeasonSlugs().map((season) => ({ season }));
}

export async function generateMetadata({
  params,
}: SeasonPageProps): Promise<Metadata> {
  const { season: seasonSlug } = await params;
  const season = getSeason(seasonSlug);
  if (!season) return {};

  return buildSeasonMetadata(
    season.slug,
    season.headline,
    season.description
  );
}

export default async function SeasonPage({ params }: SeasonPageProps) {
  const { season: seasonSlug } = await params;
  const season = getSeason(seasonSlug);
  if (!season) notFound();

  const recipes = getRecipesBySeason(seasonSlug).map(toRecipeListItem);
  const showFilters = recipes.length >= MIN_RECIPES_FOR_FILTERS;

  const guides = (season.relatedGuideSlugs ?? [])
    .map((slug) => getGuide(slug))
    .filter((g): g is NonNullable<typeof g> => Boolean(g))
    .map((guide) => ({
      title: guide.title,
      slug: guide.slug,
      description: guide.description,
      tags: guide.tags,
      image: guide.image,
      imageAlt: guide.imageAlt,
    }));

  const holidays = (season.relatedHolidaySlugs ?? [])
    .map((slug) => getHoliday(slug))
    .filter((h): h is NonNullable<typeof h> => Boolean(h));

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 text-center md:px-8 md:py-16">
      <div className="flex justify-center">
        <Breadcrumbs
          items={[
            { label: "Forside", href: "/" },
            { label: "Sæson", href: "/saeson" },
            { label: season.name },
          ]}
        />
      </div>
      <p className="mb-3 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
        Sæson
      </p>
      <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
        {season.headline}
      </h1>
      <p className="mx-auto mt-4 max-w-xl leading-relaxed text-bone/55">
        {season.description}
      </p>

      {holidays.length > 0 ? (
        <div className="mx-auto mt-6 flex flex-wrap items-center justify-center gap-2">
          <span className="text-[10px] uppercase tracking-[0.16em] text-bone/35">
            Højtider
          </span>
          {holidays.map((holiday) => (
            <Link
              key={holiday.slug}
              href={`/hoejtider/${holiday.slug}`}
              className="rounded-lg border-2 border-bone/25 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.12em] text-bone/55 transition-colors hover:border-herb hover:text-herb"
            >
              {holiday.name}
            </Link>
          ))}
        </div>
      ) : null}

      {guides.length > 0 ? (
        <section className="mt-14 text-left">
          <div className="mb-8 flex flex-col items-center gap-2 text-center">
            <h2 className="font-serif text-2xl uppercase tracking-wide text-bone md:text-3xl">
              Guides til sæsonen
            </h2>
            <p className="max-w-md text-sm text-bone/50">
              Teknik og inspiration — før du fylder gryden.
            </p>
          </div>
          <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
            {guides.map((guide) => (
              <GuideCard key={guide.slug} guide={guide} />
            ))}
          </div>
        </section>
      ) : null}

      <div className={guides.length > 0 ? "mt-16" : "mt-10"}>
        {guides.length > 0 ? (
          <div className="mb-8 flex flex-col items-center gap-2 text-center">
            <h2 className="font-serif text-2xl uppercase tracking-wide text-bone md:text-3xl">
              Opskrifter
            </h2>
            <p className="max-w-md text-sm text-bone/50">
              {recipes.length} retter til {season.name.toLowerCase()}.
            </p>
          </div>
        ) : null}
        <CategoryFilters recipes={recipes} showFilters={showFilters} />
      </div>
    </div>
  );
}
