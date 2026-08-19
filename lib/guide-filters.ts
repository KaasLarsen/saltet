import { slugifyTag } from "./slug";

export const TOP_GUIDE_TAG_LIMIT = 8;

export interface GuideListItem {
  title: string;
  slug: string;
  description: string;
  tags: string[];
  image: string;
  imageAlt: string;
}

export interface GuideFilterValues {
  emne?: string;
  q?: string;
}

export interface GuideTagFacet {
  label: string;
  slug: string;
  count: number;
}

export function guideMatchesQuery(guide: GuideListItem, query: string): boolean {
  const q = query.trim().toLowerCase();
  if (!q) return true;

  const haystack = [guide.title, guide.description, ...guide.tags]
    .join(" ")
    .toLowerCase();

  return haystack.includes(q);
}

export function filterGuides(
  guides: GuideListItem[],
  filters: GuideFilterValues
): GuideListItem[] {
  return guides.filter((guide) => {
    if (filters.q && !guideMatchesQuery(guide, filters.q)) return false;

    if (filters.emne) {
      const hasTag = guide.tags.some(
        (tag) => slugifyTag(tag) === filters.emne
      );
      if (!hasTag) return false;
    }

    return true;
  });
}

export function getTopTagsForGuides(
  guides: GuideListItem[],
  limit = TOP_GUIDE_TAG_LIMIT
): GuideTagFacet[] {
  if (guides.length === 0) return [];

  const counts = new Map<string, { label: string; count: number }>();

  for (const guide of guides) {
    for (const tag of guide.tags) {
      const slug = slugifyTag(tag);
      const existing = counts.get(slug);
      if (existing) {
        existing.count += 1;
      } else {
        counts.set(slug, { label: tag, count: 1 });
      }
    }
  }

  const coverageCeiling = guides.length * 0.75;

  return Array.from(counts.entries())
    .map(([slug, { label, count }]) => ({ slug, label, count }))
    .filter((tag) => tag.count < coverageCeiling)
    .sort((a, b) => b.count - a.count || a.label.localeCompare(b.label, "da"))
    .slice(0, limit);
}

export function hasActiveGuideFilters(filters: GuideFilterValues): boolean {
  return Boolean(filters.emne) || Boolean(filters.q?.trim());
}
