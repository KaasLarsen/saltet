export interface AnmeldelseListItem {
  title: string;
  slug: string;
  description: string;
  series: string;
  productName: string;
  tags: string[];
  image: string;
  imageAlt: string;
  rating?: number;
}

export interface AnmeldelseFilterValues {
  serie?: string;
  q?: string;
}

export const ANMELDELSE_SERIES = [
  { slug: "ninja-crispi", label: "Ninja CRISPi" },
] as const;

export type AnmeldelseSeriesSlug = (typeof ANMELDELSE_SERIES)[number]["slug"];

export function isAnmeldelseSeries(
  value: string | undefined
): value is AnmeldelseSeriesSlug {
  return ANMELDELSE_SERIES.some((series) => series.slug === value);
}

export function anmeldelseMatchesQuery(
  item: AnmeldelseListItem,
  query: string
): boolean {
  const q = query.trim().toLowerCase();
  if (!q) return true;

  const haystack = [
    item.title,
    item.description,
    item.productName,
    item.series,
    ...item.tags,
  ]
    .join(" ")
    .toLowerCase();

  return haystack.includes(q);
}

export function filterAnmeldelser(
  items: AnmeldelseListItem[],
  filters: AnmeldelseFilterValues
): AnmeldelseListItem[] {
  return items.filter((item) => {
    if (filters.serie && item.series !== filters.serie) return false;
    if (filters.q && !anmeldelseMatchesQuery(item, filters.q)) return false;
    return true;
  });
}

export function hasActiveAnmeldelseFilters(
  filters: AnmeldelseFilterValues
): boolean {
  return Boolean(filters.serie || filters.q?.trim());
}
