import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { CategoryFilters } from "@/components/CategoryFilters";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { getHoliday, getAllHolidaySlugs, getRecipesByHoliday } from "@/lib/holidays";
import { MIN_RECIPES_FOR_FILTERS } from "@/lib/recipe-filters";
import { buildHolidayMetadata } from "@/lib/seo";
import type { Recipe, RecipeFrontmatter } from "@/lib/types";

interface HolidayPageProps {
  params: Promise<{ holiday: string }>;
}

export async function generateStaticParams() {
  return getAllHolidaySlugs().map((holiday) => ({ holiday }));
}

export async function generateMetadata({
  params,
}: HolidayPageProps): Promise<Metadata> {
  const { holiday: holidaySlug } = await params;
  const holiday = getHoliday(holidaySlug);
  if (!holiday) return {};

  return buildHolidayMetadata(
    holiday.slug,
    holiday.headline,
    holiday.description
  );
}

function toListItem(recipe: Recipe): RecipeFrontmatter {
  const copy: RecipeFrontmatter & { content?: string } = { ...recipe };
  delete copy.content;
  return copy;
}

export default async function HolidayPage({ params }: HolidayPageProps) {
  const { holiday: holidaySlug } = await params;
  const holiday = getHoliday(holidaySlug);
  if (!holiday) notFound();

  const recipes = getRecipesByHoliday(holidaySlug).map(toListItem);
  const showFilters = recipes.length >= MIN_RECIPES_FOR_FILTERS;

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 text-center md:px-8 md:py-16">
      <div className="flex justify-center">
        <Breadcrumbs
          items={[
            { label: "Forside", href: "/" },
            { label: "Højtider", href: "/hoejtider" },
            { label: holiday.name },
          ]}
        />
      </div>
      <p className="mb-3 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
        Højtid
      </p>
      <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
        {holiday.headline}
      </h1>
      <p className="mx-auto mt-4 max-w-xl leading-relaxed text-bone/55">
        {holiday.description}
      </p>

      <CategoryFilters recipes={recipes} showFilters={showFilters} />
    </div>
  );
}
