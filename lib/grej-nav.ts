/** Client-safe grej-meta (ingen fs). Hold synk med content/grej/*.mdx. */

export const GREJ_NAV = [
  { slug: "stoebjern-rene-skole", name: "Støbejerns-rene-skole" },
  { slug: "airfryer-vs-ovn-opgoer", name: "Airfryer vs. ovn" },
  { slug: "traekul-og-briketter-i-indkoebskurven", name: "Trækul og briketter" },
  { slug: "hvilken-pizzaovn", name: "Hvilken pizzaovn" },
  { slug: "baalgrej-til-baghaven", name: "Bålgrej til baghaven" },
] as const;

export type GrejNavSlug = (typeof GREJ_NAV)[number]["slug"];
