/** Client-safe grej-filtre til SOS-hub og header (ingen fs). */

export const FEJLFINDING_GEAR_NAV = [
  { slug: "airfryer", name: "Airfryer" },
  { slug: "stobejern", name: "Støbejern" },
  { slug: "plancha", name: "Plancha" },
  { slug: "trykkoger", name: "Trykkoger" },
  { slug: "ovn", name: "Ovn" },
  { slug: "generelt", name: "Generelt" },
] as const;

export type FejlfindingGearNavSlug =
  (typeof FEJLFINDING_GEAR_NAV)[number]["slug"];

export function getFejlfindingGearName(slug: string): string {
  return (
    FEJLFINDING_GEAR_NAV.find((g) => g.slug === slug)?.name ?? slug
  );
}
