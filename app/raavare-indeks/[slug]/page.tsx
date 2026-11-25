import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { PaginatedRecipeGrid } from "@/components/PaginatedRecipeGrid";
import {
  getAllIngredientSlugs,
  getIngredientBySlug,
  getRecipesByIngredientSlug,
  isIndexableIngredient,
  MIN_INGREDIENT_COUNT,
} from "@/lib/ingredients";
import { toRecipeListItem } from "@/lib/recipes";
import { buildIngredientMetadata } from "@/lib/seo";

interface IngredientPageProps {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  return getAllIngredientSlugs().map((slug) => ({ slug }));
}

export async function generateMetadata({
  params,
}: IngredientPageProps): Promise<Metadata> {
  const { slug } = await params;
  const ingredient = getIngredientBySlug(slug);
  if (!ingredient || !isIndexableIngredient(ingredient)) return {};

  return buildIngredientMetadata(
    ingredient.slug,
    ingredient.name,
    `Se ${ingredient.count} opskrifter med ${ingredient.name.toLowerCase()} på Saltet — inspiration til det du allerede har i køleskabet.`
  );
}

export default async function IngredientPage({ params }: IngredientPageProps) {
  const { slug } = await params;
  const ingredient = getIngredientBySlug(slug);
  if (!ingredient) notFound();

  if (ingredient.count < MIN_INGREDIENT_COUNT) {
    notFound();
  }

  const recipes = getRecipesByIngredientSlug(slug).map(toRecipeListItem);

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 text-center md:px-8 md:py-16">
      <div className="flex justify-center">
        <Breadcrumbs
          items={[
            { label: "Forside", href: "/" },
            { label: "Råvareindeks", href: "/raavare-indeks" },
            { label: ingredient.name },
          ]}
        />
      </div>
      <p className="mb-3 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
        Råvare
      </p>
      <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
        {ingredient.name}
      </h1>
      <p className="mx-auto mt-4 max-w-xl leading-relaxed text-bone/55">
        {recipes.length} opskrift{recipes.length === 1 ? "" : "er"} med{" "}
        {ingredient.name.toLowerCase()}.
      </p>
      <PaginatedRecipeGrid recipes={recipes} />
    </div>
  );
}
