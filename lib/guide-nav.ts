/** Client-safe guide-meta (ingen fs). Hold synk med content/guides/*.mdx. */

export const GUIDE_NAV = [
  { slug: "airfryer-for-begyndere", name: "Airfryer for begyndere" },
  { slug: "kernetemperatur", name: "Kernetemperatur" },
  { slug: "culottesteg", name: "Culottesteg" },
  { slug: "hjemmelavet-pizza", name: "Hjemmelavet pizza" },
  { slug: "pulled-pork", name: "Pulled pork" },
  { slug: "fermentering-for-begyndere", name: "Fermentering" },
  { slug: "syltning", name: "Syltning" },
  { slug: "roegning-hjemme", name: "Røgning hjemme" },
  { slug: "grydebroed-og-focaccia", name: "Grydebrød og focaccia" },
  { slug: "smash-burger", name: "Smash burger" },
] as const;

export type GuideNavSlug = (typeof GUIDE_NAV)[number]["slug"];
