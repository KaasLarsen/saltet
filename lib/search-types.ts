export const SEARCH_TYPES = [
  "opskrifter",
  "guides",
  "grej",
  "anmeldelser",
] as const;

export type SearchType = (typeof SEARCH_TYPES)[number];

export function isSearchType(value: string | undefined): value is SearchType {
  return (
    value === "opskrifter" ||
    value === "guides" ||
    value === "grej" ||
    value === "anmeldelser"
  );
}
