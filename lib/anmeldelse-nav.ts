/** Client-safe anmeldelse-kategori-hubs (ingen fs). Hold synk med ANMELDELSE_SERIES. */

export const ANMELDELSE_NAV = [
  { slug: "airfryer", name: "Airfryer" },
  { slug: "plancha", name: "Plancha" },
  { slug: "trykkoger", name: "Trykkoger" },
  { slug: "indbygningsovn", name: "Indbygningsovn" },
] as const;

export type AnmeldelseNavSlug = (typeof ANMELDELSE_NAV)[number]["slug"];
