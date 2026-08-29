import { holidayForTagSlug } from "./holiday-nav";
import { isTopicTagSlug, topicForTagSlug } from "./topic-nav";
import { getAllRecipes } from "./recipes";
import { slugifyTag } from "./slug";
import type { Recipe } from "./types";

export { slugifyTag };

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

export function getBrowseTags(): TagInfo[] {
  return getAllTags().filter(
    (tag) => !holidayForTagSlug(tag.slug) && !isTopicTagSlug(tag.slug)
  );
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
  const slug = slugifyTag(tag);
  const holiday = holidayForTagSlug(slug);
  if (holiday) return `/hoejtider/${holiday.slug}`;
  const topic = topicForTagSlug(slug);
  if (topic) return `/emner/${topic.slug}`;
  return `/tags/${slug}`;
}
