export const RECIPE_RATING_KINDS = ["recipe"] as const;

export type RecipeRatingKind = (typeof RECIPE_RATING_KINDS)[number];

export type RecipeRatingSummary = {
  average: number | null;
  count: number;
};

export const EMPTY_RECIPE_RATING: RecipeRatingSummary = {
  average: null,
  count: 0,
};

export function isRecipeRatingKind(
  value: unknown
): value is RecipeRatingKind {
  return value === "recipe";
}

/** `slug` is `{category}/{slug}` for saltet recipes. */
export function recipeRatingPath(kind: RecipeRatingKind, slug: string): string {
  void kind;
  return `/opskrifter/${slug}`;
}

export function recipeRatingCacheTag(
  kind: RecipeRatingKind,
  slug: string
): string {
  return `recipe-rating:${kind}:${slug}`;
}

export function recipeRatingKey(category: string, slug: string): string {
  return `${category}/${slug}`;
}

export function parseRecipeRatingKey(
  key: string
): { category: string; slug: string } | null {
  const slash = key.indexOf("/");
  if (slash <= 0 || slash === key.length - 1) return null;
  const category = key.slice(0, slash).trim();
  const slug = key.slice(slash + 1).trim();
  if (!category || !slug || slug.includes("/")) return null;
  return { category, slug };
}

export function roundRating(average: number): number {
  return Math.round(average * 10) / 10;
}

export function summarizeRatings(ratings: number[]): RecipeRatingSummary {
  if (ratings.length === 0) return EMPTY_RECIPE_RATING;
  const sum = ratings.reduce((total, rating) => total + rating, 0);
  return { average: roundRating(sum / ratings.length), count: ratings.length };
}

/** Synlig tekst, samme tal som i Recipe-markup. */
export function formatRatingLabel(summary: RecipeRatingSummary): string {
  if (summary.count <= 0 || summary.average == null) {
    return "Ingen anmeldelser";
  }
  const value = summary.average.toFixed(1).replace(".", ",");
  const votes = summary.count === 1 ? "stemme" : "stemmer";
  return `${value} fra ${summary.count} ${votes}`;
}
