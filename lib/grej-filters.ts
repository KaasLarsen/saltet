import type { GrejTrack } from "./types";

export const GREJ_TRACKS: { slug: GrejTrack; label: string }[] = [
  { slug: "test", label: "Test & anmeldelser" },
  { slug: "koebsguide", label: "Købsguider" },
  { slug: "vedligeholdelse", label: "Vedligeholdelse & setup" },
];

export interface GrejListItem {
  title: string;
  slug: string;
  description: string;
  tags: string[];
  track: GrejTrack;
  image: string;
  imageAlt: string;
}

export interface GrejFilterValues {
  spor?: GrejTrack;
  q?: string;
}

export function grejMatchesQuery(item: GrejListItem, query: string): boolean {
  const q = query.trim().toLowerCase();
  if (!q) return true;

  const haystack = [item.title, item.description, item.track, ...item.tags]
    .join(" ")
    .toLowerCase();

  return haystack.includes(q);
}

export function filterGrej(
  items: GrejListItem[],
  filters: GrejFilterValues
): GrejListItem[] {
  return items.filter((item) => {
    if (filters.q && !grejMatchesQuery(item, filters.q)) return false;
    if (filters.spor && item.track !== filters.spor) return false;
    return true;
  });
}

export function hasActiveGrejFilters(filters: GrejFilterValues): boolean {
  return Boolean(filters.spor) || Boolean(filters.q?.trim());
}

export function isGrejTrack(value: string | undefined): value is GrejTrack {
  return (
    value === "test" || value === "koebsguide" || value === "vedligeholdelse"
  );
}
