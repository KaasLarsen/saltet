import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { CategoryFilters } from "@/components/CategoryFilters";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { getCategory } from "@/lib/categories";
import { MIN_RECIPES_FOR_FILTERS } from "@/lib/recipe-filters";
import { getRecipesByCategory } from "@/lib/recipes";
import { buildCategoryMetadata } from "@/lib/seo";
import type { RecipeFrontmatter } from "@/lib/types";

interface CategoryPageProps {
  params: Promise<{ category: string }>;
}

export async function generateStaticParams() {
  const { getAllCategorySlugs } = await import("@/lib/categories");
  return getAllCategorySlugs().map((slug) => ({ category: slug }));
}

export async function generateMetadata({
  params,
}: CategoryPageProps): Promise<Metadata> {
  const { category: categorySlug } = await params;
  const category = getCategory(categorySlug);
  if (!category) return {};

  return buildCategoryMetadata(
    category.slug,
    category.headline,
    category.description
  );
}

function toListItem(
  recipe: { content: string } & RecipeFrontmatter
): RecipeFrontmatter {
  const { content: _content, ...rest } = recipe;
  return rest;
}

export default async function CategoryPage({ params }: CategoryPageProps) {
  const { category: categorySlug } = await params;
  const category = getCategory(categorySlug);
  if (!category) notFound();

  const recipes = getRecipesByCategory(categorySlug).map(toListItem);
  const showFilters = recipes.length >= MIN_RECIPES_FOR_FILTERS;

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 text-center md:px-8 md:py-16">
      <div className="flex justify-center">
        <Breadcrumbs
          items={[
            { label: "Forside", href: "/" },
            { label: "Opskrifter", href: "/opskrifter" },
            { label: category.name },
          ]}
        />
      </div>
      <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
        {category.headline}
      </h1>
      <p className="mx-auto mt-4 max-w-xl leading-relaxed text-bone/55">
        {category.description}
      </p>

      <CategoryFilters recipes={recipes} showFilters={showFilters} />
    </div>
  );
}
