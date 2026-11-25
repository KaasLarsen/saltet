import {
  INGREDIENT_NAV,
  ingredientNavBySlug,
  type IngredientNavItem,
} from "@/lib/ingredient-nav";
import {
  aliasPattern,
  normalizeIngredientLine,
  recipeMatchesIngredient,
} from "@/lib/ingredient-match";
import { getAllRecipes } from "@/lib/recipes";
import type { Recipe } from "@/lib/types";

export type { IngredientNavItem };
export {
  normalizeIngredientLine,
  lineMatchesAlias,
  recipeMatchesIngredient,
} from "@/lib/ingredient-match";

export interface IngredientInfo {
  slug: string;
  name: string;
  count: number;
  seasonSlugs?: readonly string[];
}

/** Min. opskrifter før en råvare må i sitemap, indeks og SSG. */
export const MIN_INGREDIENT_COUNT = 2;

type IngredientIndex = {
  infos: IngredientInfo[];
  recipesBySlug: Map<string, Recipe[]>;
};

let cachedIndex: IngredientIndex | null = null;

function buildIndex(): IngredientIndex {
  const recipes = getAllRecipes();
  const recipesBySlug = new Map<string, Recipe[]>();

  for (const item of INGREDIENT_NAV) {
    recipesBySlug.set(item.slug, []);
  }

  for (const recipe of recipes) {
    const normalizedLines = recipe.ingredients.map(normalizeIngredientLine);
    for (const item of INGREDIENT_NAV) {
      const matched = item.match.some((alias) => {
        const pattern = aliasPattern(alias.trim().toLowerCase());
        return normalizedLines.some((line) => line && pattern.test(line));
      });
      if (matched) {
        recipesBySlug.get(item.slug)!.push(recipe);
      }
    }
  }

  const infos: IngredientInfo[] = INGREDIENT_NAV.map((item) => ({
    slug: item.slug,
    name: item.name,
    count: recipesBySlug.get(item.slug)?.length ?? 0,
    seasonSlugs: item.seasonSlugs,
  })).sort((a, b) => a.name.localeCompare(b.name, "da"));

  return { infos, recipesBySlug };
}

function getIndex(): IngredientIndex {
  if (!cachedIndex) cachedIndex = buildIndex();
  return cachedIndex;
}

export function getAllIngredients(): IngredientInfo[] {
  return getIndex().infos;
}

export function getIndexableIngredients(
  minCount: number = MIN_INGREDIENT_COUNT
): IngredientInfo[] {
  return getAllIngredients().filter((item) => item.count >= minCount);
}

export function isIndexableIngredient(
  item: IngredientInfo,
  minCount: number = MIN_INGREDIENT_COUNT
): boolean {
  return item.count >= minCount;
}

export function getIngredientBySlug(slug: string): IngredientInfo | undefined {
  return getAllIngredients().find((item) => item.slug === slug);
}

export function getRecipesByIngredientSlug(slug: string): Recipe[] {
  if (!ingredientNavBySlug(slug)) return [];
  return getIndex().recipesBySlug.get(slug) ?? [];
}

export function getAllIngredientSlugs(
  minCount: number = MIN_INGREDIENT_COUNT
): string[] {
  return getIndexableIngredients(minCount).map((item) => item.slug);
}

/** Gruppér indexable råvarer under A–Å (dansk sortering inden for bogstav). */
export function groupIngredientsByLetter(
  items: IngredientInfo[] = getIndexableIngredients()
): { letter: string; items: IngredientInfo[] }[] {
  const groups = new Map<string, IngredientInfo[]>();

  for (const item of items) {
    const letter = [...item.name][0]?.toLocaleUpperCase("da") ?? "#";
    const list = groups.get(letter);
    if (list) list.push(item);
    else groups.set(letter, [item]);
  }

  return Array.from(groups.entries())
    .sort(([a], [b]) => a.localeCompare(b, "da"))
    .map(([letter, groupItems]) => ({
      letter,
      items: groupItems.sort((a, b) => a.name.localeCompare(b.name, "da")),
    }));
}

export function ingredientHref(slug: string): string {
  return `/raavare-indeks/${slug}`;
}
