/** Client-safe anmeldelse-kategori-hubs (ingen fs). Hold synk med ANMELDELSE_SERIES. */

export const ANMELDELSE_NAV = [
  { slug: "airfryer", name: "Airfryer" },
  { slug: "plancha", name: "Plancha" },
  { slug: "gasgrill", name: "Gasgrill" },
  { slug: "trykkoger", name: "Trykkoger" },
  { slug: "indbygningsovn", name: "Indbygningsovn" },
  { slug: "friture", name: "Friture" },
] as const;

export type AnmeldelseNavSlug = (typeof ANMELDELSE_NAV)[number]["slug"];
