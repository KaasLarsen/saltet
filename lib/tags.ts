import { getAllRecipes } from "./recipes";
import type { Recipe } from "./types";

export function slugifyTag(tag: string): string {
  return tag
    .toLowerCase()
    .trim()
    .replace(/æ/g, "ae")
    .replace(/ø/g, "oe")
    .replace(/å/g, "aa")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
}

export interface TagInfo {
  label: string;
  slug: string;
  count: number;
}

export function getAllTags(): TagInfo[] {
  const counts = new Map<string, { label: string; count: number }>();

  for (const recipe of getAllRecipes()) {
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

  return Array.from(counts.entries())
    .map(([slug, { label, count }]) => ({ slug, label, count }))
    .sort((a, b) => a.label.localeCompare(b.label, "da"));
}

export function getTagBySlug(slug: string): TagInfo | undefined {
  return getAllTags().find((t) => t.slug === slug);
}

export function getRecipesByTagSlug(slug: string): Recipe[] {
  return getAllRecipes().filter((recipe) =>
    recipe.tags.some((tag) => slugifyTag(tag) === slug)
  );
}

export function tagHref(tag: string): string {
  return `/tags/${slugifyTag(tag)}`;
}
