import type { Category } from "./types";

export const categories: Category[] = [
  {
    slug: "airfryer",
    name: "Airfryer",
    description:
      "Sprøde, saftige retter fra airfryeren — hurtigt, nemt og fuld af smag.",
    headline: "Airfryer opskrifter",
  },
];

export function getCategory(slug: string): Category | undefined {
  return categories.find((c) => c.slug === slug);
}

export function getCategoryName(slug: string): string {
  return getCategory(slug)?.name ?? slug;
}
