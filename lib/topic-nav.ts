/** Client-safe emne-meta (ingen fs / recipes-import). */

export interface TopicNavItem {
  slug: string;
  name: string;
  /** Tag-slugs der knytter en opskrift til emnet. */
  matchTagSlugs: readonly string[];
}

export const TOPIC_NAV: readonly TopicNavItem[] = [
  {
    slug: "sovs",
    name: "Sovs",
    matchTagSlugs: [
      "sauce",
      "dip",
      "bearnaise",
      "bearnaisesovs",
      "brun-sovs",
      "remoulade",
      "aioli",
      "mayonnaise",
    ],
  },
  {
    slug: "kage",
    name: "Kage",
    matchTagSlugs: [
      "kage",
      "banankage",
      "klatkager",
      "scones",
      "muffins",
      "brownie",
      "pandekager",
    ],
  },
  {
    slug: "dessert",
    name: "Dessert",
    matchTagSlugs: ["dessert", "is", "chokolade"],
  },
  {
    slug: "pasta",
    name: "Pasta",
    matchTagSlugs: ["pasta"],
  },
  {
    slug: "suppe",
    name: "Suppe",
    matchTagSlugs: ["suppe"],
  },
  {
    slug: "salat",
    name: "Salat",
    matchTagSlugs: ["salat"],
  },
  {
    slug: "kylling",
    name: "Kylling",
    matchTagSlugs: [
      "kylling",
      "kyllingebryst",
      "kyllingelaar",
      "hel-kylling",
      "kyllingespyd",
    ],
  },
  {
    slug: "fisk",
    name: "Fisk",
    matchTagSlugs: [
      "fisk",
      "laks",
      "torsk",
      "oerred",
      "aborre",
      "makrel",
      "sild",
      "fiskefilet",
      "fiskefileter",
    ],
  },
  {
    slug: "vegetar",
    name: "Vegetar",
    matchTagSlugs: ["vegetar", "vegetarisk"],
  },
  {
    slug: "broed",
    name: "Brød",
    matchTagSlugs: [
      "broed",
      "rugbroed",
      "fladbroed",
      "focaccia",
      "boller",
      "surdej",
      "ciabatta",
      "lepinja",
    ],
  },
  {
    slug: "snack",
    name: "Snack",
    matchTagSlugs: ["snack", "snacks", "forret"],
  },
  {
    slug: "palaeg",
    name: "Pålæg",
    matchTagSlugs: ["paalaeg"],
  },
  {
    slug: "kartofler",
    name: "Kartofler",
    matchTagSlugs: ["kartofler", "kartoffel", "roesti", "pommes", "fritter"],
  },
  {
    slug: "ost",
    name: "Ost",
    matchTagSlugs: ["ost"],
  },
  {
    slug: "tilbehoer",
    name: "Tilbehør",
    matchTagSlugs: ["tilbehoer"],
  },
  {
    slug: "oksekoed",
    name: "Oksekød",
    matchTagSlugs: ["oksekoed", "bof", "entrecote", "moerkbrad"],
  },
  {
    slug: "svinekoed",
    name: "Svinekød",
    matchTagSlugs: ["svinekoed", "flaeskesteg", "ribben", "medister"],
  },
  {
    slug: "frokost",
    name: "Frokost",
    matchTagSlugs: ["frokost"],
  },
  {
    slug: "smoerrebroed",
    name: "Smørrebrød",
    matchTagSlugs: ["smoerrebroed"],
  },
  {
    slug: "bacon",
    name: "Bacon",
    matchTagSlugs: ["bacon"],
  },
  {
    slug: "pizza",
    name: "Pizza",
    matchTagSlugs: ["pizza", "calzone"],
  },
  {
    slug: "chili",
    name: "Chili",
    matchTagSlugs: ["chili"],
  },
  {
    slug: "dansk-klassiker",
    name: "Dansk klassiker",
    matchTagSlugs: ["dansk-klassiker", "mormormad", "hygge"],
  },
  {
    slug: "protein",
    name: "Protein",
    matchTagSlugs: ["protein", "hojprotein", "proteinrig"],
  },
  {
    slug: "festmad",
    name: "Festmad",
    matchTagSlugs: ["festmad", "gourmet", "gastromad"],
  },
  {
    slug: "hvidloeg",
    name: "Hvidløg",
    matchTagSlugs: ["hvidloeg"],
  },
];

export type TopicNavSlug = (typeof TOPIC_NAV)[number]["slug"];

export const TOPIC_NAV_LABELS: Record<string, string> = Object.fromEntries(
  TOPIC_NAV.map((t) => [t.slug, t.name])
);

export function topicNavLabel(slug: string): string {
  return TOPIC_NAV_LABELS[slug] ?? slug;
}

export function getTopicNav(slug: string): TopicNavItem | undefined {
  return TOPIC_NAV.find((t) => t.slug === slug);
}

export function isTopicTagSlug(slug: string): boolean {
  return TOPIC_NAV.some(
    (t) => t.slug === slug || t.matchTagSlugs.includes(slug)
  );
}

export function topicForTagSlug(tagSlug: string): TopicNavItem | undefined {
  return TOPIC_NAV.find(
    (t) => t.slug === tagSlug || t.matchTagSlugs.includes(tagSlug)
  );
}

export function recipeMatchesTopic(
  tags: readonly string[],
  topic: TopicNavItem,
  slugify: (tag: string) => string
): boolean {
  return tags.some((tag) => topic.matchTagSlugs.includes(slugify(tag)));
}
