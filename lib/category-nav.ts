/** Client-safe kategori-meta (ingen fs / recipes-import). */

export const CATEGORY_NAV = [
  { slug: "airfryer", name: "Airfryer" },
  { slug: "grill", name: "Grill" },
  { slug: "baalmad", name: "Bålmad" },
  { slug: "roeg", name: "Røg" },
  { slug: "plancha", name: "Plancha" },
  { slug: "gryde", name: "Gryde" },
  { slug: "pande", name: "Pande" },
  { slug: "ovn", name: "Ovn" },
  { slug: "sylte", name: "Sylte" },
  { slug: "dips", name: "Dips" },
  { slug: "sous-vide", name: "Sous Vide" },
  { slug: "trykkoger", name: "Trykkoger" },
  { slug: "dehydrator", name: "Dehydrator" },
  { slug: "roeremaskine", name: "Røremaskine" },
  { slug: "pizzaovn", name: "Pizzaovn" },
  { slug: "stobejern", name: "Støbejern" },
  { slug: "fermentering", name: "Fermentering" },
  { slug: "palaeg", name: "Pålæg" },
] as const;

export type CategoryNavSlug = (typeof CATEGORY_NAV)[number]["slug"];

export const CATEGORY_NAV_ORDER: readonly CategoryNavSlug[] = CATEGORY_NAV.map(
  (c) => c.slug
);

export const CATEGORY_NAV_LABELS: Record<string, string> = Object.fromEntries(
  CATEGORY_NAV.map((c) => [c.slug, c.name])
);

export function categoryNavLabel(slug: string): string {
  return (
    CATEGORY_NAV_LABELS[slug] ??
    slug.charAt(0).toUpperCase() + slug.slice(1)
  );
}
