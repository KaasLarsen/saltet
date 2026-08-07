import type { Category } from "./types";
import { getAllCategoriesFromRecipes } from "./recipes";

export const categories: Category[] = [
  {
    slug: "airfryer",
    name: "Airfryer",
    description:
      "Sprøde, saftige retter fra airfryeren — hurtigt, nemt og fuld af smag.",
    headline: "Airfryer opskrifter",
  },
  {
    slug: "grill",
    name: "Grill",
    description:
      "Sommer på grillen — saftigt kød, grønt med røg og klassiske sides til haven.",
    headline: "Grill opskrifter",
  },
  {
    slug: "plancha",
    name: "Plancha",
    description:
      "Høj varme på stålpladen — skorpe, saft og plancha-klassikere til have og terrasse.",
    headline: "Plancha opskrifter",
  },
];

export function getCategory(slug: string): Category | undefined {
  const known = categories.find((c) => c.slug === slug);
  if (known) return known;

  // Fallback for kategorier der kun findes via content/recipes/
  if (getAllCategoriesFromRecipes().includes(slug)) {
    const name = slug.charAt(0).toUpperCase() + slug.slice(1);
    return {
      slug,
      name,
      description: `Opskrifter i kategorien ${name}.`,
      headline: `${name} opskrifter`,
    };
  }

  return undefined;
}

export function getCategoryName(slug: string): string {
  return getCategory(slug)?.name ?? slug;
}

export function getAllCategorySlugs(): string[] {
  const fromConfig = categories.map((c) => c.slug);
  const fromRecipes = getAllCategoriesFromRecipes();
  return Array.from(new Set([...fromConfig, ...fromRecipes])).sort();
}
