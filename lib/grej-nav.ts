/** Client-safe grej-meta (ingen fs). Hold synk med content/grej/*.mdx. */

export const GREJ_NAV = [
  { slug: "stoebjern-rene-skole", name: "Støbejerns-rene-skole" },
  { slug: "plancha-vs-stobejern", name: "Plancha vs. støbejern" },
  { slug: "airfryer-vs-ovn-opgoer", name: "Airfryer vs. ovn" },
  { slug: "airfryer-tilbehoer", name: "Airfryer-tilbehør" },
  { slug: "traekul-og-briketter-i-indkoebskurven", name: "Trækul og briketter" },
  { slug: "rygesmuld-flis-og-chunks", name: "Rygesmuld og chunks" },
  { slug: "rotisseri-til-grillen", name: "Rotisseri" },
  { slug: "hvilken-pizzaovn", name: "Hvilken pizzaovn" },
  { slug: "bagestaal-vs-bagesten", name: "Bagestål vs. sten" },
  { slug: "baalgrej-til-baghaven", name: "Bålgrej til baghaven" },
  { slug: "sous-vide-stave", name: "Sous vide-stave" },
  { slug: "trykkoger-vs-slowcooker", name: "Trykkoger vs. slowcooker" },
  { slug: "dehydrator-koebsguide", name: "Dehydrator" },
  { slug: "fermenteringsglas", name: "Fermenteringsglas" },
  { slug: "slibesten-vs-strygestaal", name: "Slibesten og stål" },
] as const;

export type GrejNavSlug = (typeof GREJ_NAV)[number]["slug"];
