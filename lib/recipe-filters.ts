import { HOLIDAY_NAV } from "./holiday-nav";
import { slugifyTag } from "./slug";
import type { Difficulty, RecipeFrontmatter } from "./types";

export const MIN_RECIPES_FOR_FILTERS = 12;
export const TOP_TAG_LIMIT = 6;
export const TIME_FILTERS = [30, 45] as const;

export type TimeFilter = (typeof TIME_FILTERS)[number];

export interface CategoryFilterValues {
  tid?: TimeFilter;
  svar?: Difficulty;
  emne?: string;
  hoejtid?: string;
  q?: string;
}

export interface TagFacet {
  label: string;
  slug: string;
  count: number;
}

export interface HolidayFacet {
  label: string;
  slug: string;
  count: number;
}

/** Konverter ISO 8601-varighed (PT1H10M) til minutter. */
export function parseDurationMinutes(iso: string): number | null {
  const match = iso.match(/PT(?:(\d+)H)?(?:(\d+)M)?/);
  if (!match) return null;

  const hours = match[1] ? parseInt(match[1], 10) : 0;
  const minutes = match[2] ? parseInt(match[2], 10) : 0;
  if (hours === 0 && minutes === 0) return null;

  return hours * 60 + minutes;
}

export function parseTimeFilter(value: string | undefined): TimeFilter | undefined {
  if (value === "30" || value === "45") return Number(value) as TimeFilter;
  return undefined;
}

export function parseDifficultyFilter(
  value: string | undefined
): Difficulty | undefined {
  if (value === "nem" || value === "mellem" || value === "svær") return value;
  return undefined;
}

export function recipeMatchesQuery(
  recipe: RecipeFrontmatter,
  query: string
): boolean {
  const q = query.trim().toLowerCase();
  if (!q) return true;

  const haystack = [
    recipe.title,
    recipe.description,
    recipe.category,
    ...recipe.tags,
    ...recipe.ingredients,
  ]
    .join(" ")
    .toLowerCase();

  return haystack.includes(q);
}

export function filterRecipes<T extends RecipeFrontmatter>(
  recipes: T[],
  filters: CategoryFilterValues
): T[] {
  return recipes.filter((recipe) => {
    if (filters.q && !recipeMatchesQuery(recipe, filters.q)) return false;

    if (filters.svar && recipe.difficulty !== filters.svar) return false;

    if (filters.tid != null) {
      const minutes = parseDurationMinutes(recipe.totalTime);
      if (minutes == null || minutes > filters.tid) return false;
    }

    if (filters.emne) {
      const hasTag = recipe.tags.some(
        (tag) => slugifyTag(tag) === filters.emne
      );
      if (!hasTag) return false;
    }

    if (filters.hoejtid) {
      const holiday = HOLIDAY_NAV.find((h) => h.slug === filters.hoejtid);
      if (!holiday) return false;
      const matches = recipe.tags.some((tag) =>
        holiday.matchTagSlugs.includes(slugifyTag(tag))
      );
      if (!matches) return false;
    }

    return true;
  });
}

/** Sværhedsgrader der faktisk findes i listen, i fast rækkefølge. */
export function getAvailableDifficulties(
  recipes: RecipeFrontmatter[]
): Difficulty[] {
  const present = new Set(recipes.map((r) => r.difficulty));
  return (["nem", "mellem", "svær"] as const).filter((d) => present.has(d));
}

/**
 * Mest brugte tags i kategorien.
 * Springer tags over der dækker næsten hele listen (fx "grill" på grill-siden).
 */
export function getTopTagsForRecipes(
  recipes: RecipeFrontmatter[],
  limit = TOP_TAG_LIMIT
): TagFacet[] {
  if (recipes.length === 0) return [];

  const counts = new Map<string, { label: string; count: number }>();

  for (const recipe of recipes) {
    for (const tag of recipe.tags) {
      const slug = slugifyTag(tag);
      const existing = counts.get(slug);
      if (existing) {
        existing.count += 1;
      } else {
        counts.set(slug, { label: tag, count: 1 });
      }
    }
  }

  // Skjul tags der dækker næsten hele kategorien (fx "grill" på grill-siden)
  const coverageCeiling = recipes.length * 0.75;

  const holidayTagSlugs = new Set(
    HOLIDAY_NAV.flatMap((h) => [h.slug, ...h.matchTagSlugs])
  );

  return Array.from(counts.entries())
    .map(([slug, { label, count }]) => ({ slug, label, count }))
    .filter((tag) => tag.count < coverageCeiling)
    .filter((tag) => !holidayTagSlugs.has(tag.slug))
    .sort((a, b) => b.count - a.count || a.label.localeCompare(b.label, "da"))
    .slice(0, limit);
}

/** Højtider der faktisk findes blandt opskrifterne. */
export function getAvailableHolidays(
  recipes: RecipeFrontmatter[]
): HolidayFacet[] {
  if (recipes.length === 0) return [];

  return HOLIDAY_NAV.flatMap((holiday) => {
    const count = recipes.filter((recipe) =>
      recipe.tags.some((tag) =>
        holiday.matchTagSlugs.includes(slugifyTag(tag))
      )
    ).length;
    const coverageCeiling = recipes.length * 0.75;
    if (count === 0 || count >= coverageCeiling) return [];
    return [{ slug: holiday.slug, label: holiday.name, count }];
  });
}

export function parseHolidayFilter(
  value: string | undefined
): string | undefined {
  if (!value) return undefined;
  return HOLIDAY_NAV.some((h) => h.slug === value) ? value : undefined;
}

export function hasActiveFilters(filters: CategoryFilterValues): boolean {
  return (
    filters.tid != null ||
    filters.svar != null ||
    Boolean(filters.emne) ||
    Boolean(filters.hoejtid) ||
    Boolean(filters.q?.trim())
  );
}
