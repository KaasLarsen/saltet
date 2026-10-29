/** Client-safe guide-emne-hubs til header (ingen fs). Slugs matcher slugifyTag. */

export const GUIDE_CATEGORY_NAV = [
  { slug: "airfryer", name: "Airfryer" },
  { slug: "grill", name: "Grill" },
  { slug: "plancha", name: "Plancha" },
  { slug: "stoebejern", name: "Støbejern" },
  { slug: "trykkoger", name: "Trykkoger" },
  { slug: "salt", name: "Salt" },
  { slug: "pizza", name: "Pizza" },
  { slug: "baalmad", name: "Bålmad" },
  { slug: "boern", name: "Børn" },
  { slug: "meal-prep", name: "Meal prep" },
  { slug: "fermentering", name: "Fermentering" },
  { slug: "sous-vide", name: "Sous vide" },
] as const;

export type GuideCategoryNavSlug = (typeof GUIDE_CATEGORY_NAV)[number]["slug"];
