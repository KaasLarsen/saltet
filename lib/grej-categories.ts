/** Client-safe grej-kategorier (ingen fs). Hold synk med grej.ts-forbrug. */

import { categoryNavLabel } from "./category-nav";

/** Opskriftskategori → grej-slugs (krydslinks + nav-filtre). */
export const CATEGORY_GREJ: Record<string, readonly string[]> = {
  airfryer: [
    "airfryer-vs-ovn-opgoer",
    "airfryer-tilbehoer",
    "airfryer-tilbehoer-test",
    "oliesprayflasker-airfryer",
    "airfryer-rengoering",
    "instant-read-vs-bluetooth-termometer",
    "sukkertermometer",
    "tangsaet-pincet-grilltang",
    "koekkenvaegt-vs-maalebaeger",
    "bagestaal-til-airfryer",
    "tarteletjern-vs-koebte-skaller",
  ],
  stobejern: [
    "stoebjern-rene-skole",
    "plancha-vs-stobejern",
    "stoebejern-vs-carbonstaal",
    "smashburger-grej",
    "stoebejern-boerster-skrabere",
    "stoebjernsgryde-storrelsesguide",
    "smedejern-vs-stobejern-baalpande",
    "belaegning-teflon-keramik-staal",
    "induktion-vs-gas",
    "tangsaet-pincet-grilltang",
    "opvaskeboerste-stoebjern",
    "grillhandske-laeder-silikone-kevlar",
    "knivslibning-for-noerdere",
  ],
  plancha: [
    "plancha-vs-stobejern",
    "stoebejern-vs-carbonstaal",
    "smashburger-grej",
    "stoebjern-rene-skole",
    "gas-plancha-vs-kul-grill",
  ],
  pizzaovn: [
    "hvilken-pizzaovn",
    "bagestaal-vs-bagesten",
    "infrared-termometer-pizza",
    "infrared-termometer-test",
    "pizzaspader",
    "pizzasten-rengoering",
    "gasregulatorer-slanger-sikkerhed",
    "haevekasser-pizzadej",
    "koekkenvaegt-vs-maalebaeger",
    "spiral-vs-planetarisk-roeremaskine",
    "grillhandske-laeder-silikone-kevlar",
  ],
  ovn: [
    "bagestaal-vs-bagesten",
    "koekkenvaegt-vs-maalebaeger",
    "haevekasser-pizzadej",
    "koedsnore-og-koednaale",
    "termometer-til-andesteg",
  ],
  baalmad: [
    "baalgrej-til-baghaven",
    "baaltang-log-lifter",
    "stoebjernsgryde-storrelsesguide",
    "smedejern-vs-stobejern-baalpande",
    "grillhandske-laeder-silikone-kevlar",
    "koeleboks-passiv-vs-kompressor",
  ],
  grill: [
    "traekul-og-briketter-i-indkoebskurven",
    "rotisseri-til-grillen",
    "rygesmuld-flis-og-chunks",
    "tradlost-stegetermometer",
    "instant-read-vs-bluetooth-termometer",
    "termometer-til-andesteg",
    "infrared-termometer-test",
    "gas-plancha-vs-kul-grill",
    "gasregulatorer-slanger-sikkerhed",
    "koldroegningsbakke",
    "grillboerster-sikkerhed",
    "tangsaet-pincet-grilltang",
    "induktion-vs-gas",
    "koedsnore-og-koednaale",
    "taendblokke-opgoer",
    "grillhandske-laeder-silikone-kevlar",
    "koeleboks-passiv-vs-kompressor",
  ],
  "sous-vide": [
    "sous-vide-stave",
    "vakuumpakkere",
    "chiffonflaske-sifon",
    "ismaskine-kompressor-vs-fryseelement",
    "termokande-til-mad",
  ],
  roeremaskine: [
    "koedhakkere",
    "spiral-vs-planetarisk-roeremaskine",
    "poelseroer-vs-poelsestopper",
  ],
  trykkoger: ["trykkoger-vs-slowcooker"],
  dehydrator: ["dehydrator-koebsguide"],
  fermentering: [
    "fermenteringsglas",
    "toerreposer-umi-bags",
    "lage-sproejte-vs-toersaltning",
    "poelseroer-vs-poelsestopper",
  ],
  palaeg: [
    "palaegsmaskine-pro-vs-billig",
    "rullepoelsepresser-trae-vs-staal",
    "poelseroer-vs-poelsestopper",
    "toerreposer-umi-bags",
    "lage-sproejte-vs-toersaltning",
    "laksekniv-fleksibel",
    "elektrisk-palaegskniv",
    "sildekrukker-patentglas",
    "tarteletjern-vs-koebte-skaller",
  ],
  roeg: [
    "rygesmuld-flis-og-chunks",
    "koldroegningsbakke",
    "lage-sproejte-vs-toersaltning",
    "roegpistol-smoking-gun",
    "laksekniv-fleksibel",
  ],
  sylte: ["sildekrukker-patentglas", "fermenteringsglas"],
  dips: [
    "stavblender",
    "chiffonflaske-sifon",
    "espresso-vs-moccamaster",
    "maelkeskummer-mikroskum",
    "termokande-til-mad",
    "roegpistol-smoking-gun",
  ],
  pande: [
    "belaegning-teflon-keramik-staal",
    "kobbergryder",
    "peberkvaern-keramik-vs-plastik",
    "microplane-vs-kasserivejern",
    "koekkensakse-fjerkrae-saks",
    "induktion-vs-gas",
    "tangsaet-pincet-grilltang",
    "multihakker-loegsnitter",
    "knivmagnet-vs-knivblok",
    "opvaskeboerste-stoebjern",
  ],
  gryde: [
    "kobbergryder",
    "stoebjernsgryde-storrelsesguide",
    "koekkensakse-fjerkrae-saks",
    "multihakker-loegsnitter",
  ],
};

/** Kuraterede udstyrshubs i header-dropdownen. */
export const GREJ_CATEGORY_NAV = [
  { slug: "airfryer", name: "Airfryer" },
  { slug: "grill", name: "Grill" },
  { slug: "plancha", name: "Plancha" },
  { slug: "stobejern", name: "Støbejern" },
  { slug: "pizzaovn", name: "Pizzaovn" },
  { slug: "baalmad", name: "Bålmad" },
  { slug: "sous-vide", name: "Sous vide" },
  { slug: "palaeg", name: "Pålæg" },
  { slug: "roeg", name: "Røg" },
  { slug: "trykkoger", name: "Trykkoger" },
  { slug: "dehydrator", name: "Dehydrator" },
  { slug: "fermentering", name: "Fermentering" },
] as const;

export type GrejCategoryNavSlug = (typeof GREJ_CATEGORY_NAV)[number]["slug"];

export function isGrejCategory(
  value: string | undefined
): value is GrejCategoryNavSlug {
  return GREJ_CATEGORY_NAV.some((c) => c.slug === value);
}

export function grejBelongsToCategory(
  grejSlug: string,
  kategori: string
): boolean {
  const members = CATEGORY_GREJ[kategori];
  return Boolean(members?.includes(grejSlug));
}

export function grejCategoryLabel(slug: string): string {
  const fromNav = GREJ_CATEGORY_NAV.find((c) => c.slug === slug);
  if (fromNav) return fromNav.name;
  return categoryNavLabel(slug);
}
