import {
  getHolidayNav,
  recipeMatchesHoliday,
} from "./holiday-nav";
import { getAllRecipes } from "./recipes";
import { slugifyTag } from "./slug";
import type { Holiday, Recipe } from "./types";

export const holidays: Holiday[] = [
  {
    slug: "jul",
    name: "Jul",
    headline: "Juleopskrifter",
    description:
      "Flæskesteg, and, gås, rødkål og risengrød — det danske julebord på tværs af airfryer, grill, ovn og gryde.",
  },
  {
    slug: "nytaar",
    name: "Nytår",
    headline: "Nytårsopskrifter",
    description:
      "Festmad til nytårsaften — hummer, oksemørbrad, tomahawk og de retter der hører champagne til.",
  },
  {
    slug: "paaske",
    name: "Påske",
    headline: "Påskeopskrifter",
    description:
      "Lam, sild og det salte påskebord — opskrifter til frokosten og den store middag.",
  },
  {
    slug: "mortensaften",
    name: "Mortensaften",
    headline: "Mortensaften opskrifter",
    description:
      "Andesteg til Mortensaften den 10. november — sprødt skind, saftigt kød og klassisk tilbehør.",
  },
];

export function getHoliday(slug: string): Holiday | undefined {
  return holidays.find((h) => h.slug === slug);
}

export function getAllHolidaySlugs(): string[] {
  return holidays.map((h) => h.slug);
}

export function recipeMatchesHolidaySlug(
  recipe: Pick<Recipe, "tags">,
  holidaySlug: string
): boolean {
  const nav = getHolidayNav(holidaySlug);
  if (!nav) return false;
  return recipeMatchesHoliday(recipe.tags, nav, slugifyTag);
}

export function getRecipesByHoliday(slug: string): Recipe[] {
  return getAllRecipes().filter((recipe) =>
    recipeMatchesHolidaySlug(recipe, slug)
  );
}

export function getHolidayCounts(): { holiday: Holiday; count: number }[] {
  const recipes = getAllRecipes();
  return holidays.map((holiday) => ({
    holiday,
    count: recipes.filter((recipe) =>
      recipeMatchesHolidaySlug(recipe, holiday.slug)
    ).length,
  }));
}
