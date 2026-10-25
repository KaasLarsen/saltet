import {
  getSeasonNav,
  recipeMatchesSeason,
} from "./season-nav";
import { getAllRecipes } from "./recipes";
import { slugifyTag } from "./slug";
import type { Recipe, Season } from "./types";

export const seasons: Season[] = [
  {
    slug: "foraar",
    name: "Forår",
    headline: "Forårsopskrifter",
    description:
      "Ramsløg, asparges, nye kartofler og det første grønne — let mad når lyset vender tilbage.",
    relatedGuideSlugs: [],
    relatedHolidaySlugs: ["paaske"],
  },
  {
    slug: "sommer",
    name: "Sommer",
    headline: "Sommeropskrifter",
    description:
      "Grill, salater, bær og det lette bord — når det er varmt og man vil have smag uden tungt grej.",
    relatedGuideSlugs: [],
    relatedHolidaySlugs: ["sommerhoejtider"],
  },
  {
    slug: "efteraar",
    name: "Efterår",
    headline: "Efterårsopskrifter",
    description:
      "Græskar, svampe, rodfrugter, vildt og lange gryder — comfort-mad til kølige aftener. Halloween og Mortensaften ligger her også.",
    relatedGuideSlugs: [
      "rodfrugter-i-saeson",
      "svampe-saeson",
      "efteraarsgryder-og-braise",
      "sylte-hoest",
      "toerstegning-af-svampe",
      "rensning-af-svampe",
      "syltning",
      "andesteg-komplet-guide",
      "mortensaften-tilbehoer",
      "trykkoger-og-slowcooker",
      "baalmad",
    ],
    relatedHolidaySlugs: ["halloween", "mortensaften"],
  },
  {
    slug: "vinter",
    name: "Vinter",
    headline: "Vinteropskrifter",
    description:
      "Braiser, supper, rodfrugter og det tunge bord — når det er koldt, og gryden skal stå længe.",
    relatedGuideSlugs: [],
    relatedHolidaySlugs: ["jul", "nytaar"],
  },
];

export function getSeason(slug: string): Season | undefined {
  return seasons.find((s) => s.slug === slug);
}

export function getAllSeasonSlugs(): string[] {
  return seasons.map((s) => s.slug);
}

export function recipeMatchesSeasonSlug(
  recipe: Pick<Recipe, "tags">,
  seasonSlug: string
): boolean {
  const nav = getSeasonNav(seasonSlug);
  if (!nav) return false;
  return recipeMatchesSeason(recipe.tags, nav, slugifyTag);
}

export function getRecipesBySeason(slug: string): Recipe[] {
  return getAllRecipes().filter((recipe) =>
    recipeMatchesSeasonSlug(recipe, slug)
  );
}

/** Featured først, ellers nyeste — til forsiden. */
export function getSeasonRecipesForHome(
  slug: string,
  limit = 8
): Recipe[] {
  const matching = getRecipesBySeason(slug);
  const featured = matching.filter((r) => r.featured);
  const pool = featured.length > 0 ? featured : matching;
  return [...pool]
    .sort(
      (a, b) =>
        new Date(b.publishedAt).getTime() - new Date(a.publishedAt).getTime()
    )
    .slice(0, limit);
}

export function getSeasonCounts(): { season: Season; count: number }[] {
  const recipes = getAllRecipes();
  return seasons.map((season) => ({
    season,
    count: recipes.filter((recipe) =>
      recipeMatchesSeasonSlug(recipe, season.slug)
    ).length,
  }));
}
