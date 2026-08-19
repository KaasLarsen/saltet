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

export const GUIDE_LINKS: {
  slug: GuideNavSlug;
  title: string;
  description: string;
  recipes: string[];
}[] = [
  {
    slug: "airfryer-for-begyndere",
    title: "Airfryer for begyndere — sprød mad uden gætteri",
    description:
      "Komplet guide til airfryer: temperatur, tid, forvarmning, olie og de fejl der gør maden blød.",
    recipes: [
      "airfryer/pommes-frites-bagekartofler",
      "airfryer/frosne-pomfritter",
      "airfryer/crispy-chicken-tenders",
      "airfryer/hjemmelavede-kyllingenuggets",
      "airfryer/flaeskesvaer-sennepsstoev",
      "airfryer/bacon",
      "airfryer/hel-kylling",
      "airfryer/fiskefileter-panko",
      "airfryer/smashed-potato-salad",
      "airfryer/haardkogte-aeg-meal-prep",
      "airfryer/frosne-rundstykker",
      "airfryer/spidskaal",
    ],
  },
  {
    slug: "kernetemperatur",
    title: "Kernetemperatur — komplet tabel til grill, pande, ovn og sous vide",
    description:
      "Kernetemperatur for okse, svin, lam, kylling og fisk. Træk-temperatur, carryover og probe-placering.",
    recipes: [
      "grill/kernetemperatur-grill",
      "grill/tomahawk-steak",
      "grill/culottesteg-paa-grill",
      "grill/oksemoerbrad-paa-grill",
      "sous-vide/ribeye-sous-vide",
      "sous-vide/culottesteg-sous-vide",
      "sous-vide/hel-kylling-sous-vide",
      "grill/hel-kylling-gasgrill-tid",
      "grill/pulled-pork",
      "roeg/smoked-pulled-pork",
      "sous-vide/pulled-pork-sous-vide",
      "sous-vide/laksefilet-sous-vide",
      "grill/grillet-lakseside-citron",
    ],
  },
  {
    slug: "culottesteg",
    title: "Culottesteg — fra rå til rosa på grill, ovn, airfryer og sous vide",
    description:
      "Culottesteg komplet: udskæring, fedtkappe, kernetemperatur, reverse sear og hvile.",
    recipes: [
      "grill/culottesteg-paa-grill",
      "grill/culottesteg-rotisseri",
      "grill/grillet-kalveculotte-urtemarinade",
      "sous-vide/culottesteg-sous-vide",
      "airfryer/rosa-culottesteg",
      "grill/klassisk-kartoffelsalat",
      "grill/kartoffelsalat-radiser",
      "dips/chimichurri",
      "dips/mormordressing",
      "grill/groentsager-paa-grill",
    ],
  },
  {
    slug: "hjemmelavet-pizza",
    title: "Hjemmelavet pizza — dej, varme og ovn",
    description:
      "Pizzadej, koldhæv, neapolitansk varme og fejl som våd midte.",
    recipes: [
      "roeremaskine/neapolitansk-pizzadej-roeremaskine",
      "roeremaskine/koldhaevet-pizzadej-roeremaskine",
      "roeremaskine/hurtig-pizzadej-roeremaskine",
      "grill/pizzadej-grill",
      "pizzaovn/neapolitansk-pizza-pizzaovn",
      "pizzaovn/pizza-margherita-pizzaovn",
      "pizzaovn/detroit-style-pizza-pizzaovn",
      "pizzaovn/calzone-skinke-ricotta-pizzaovn",
      "pizzaovn/panuozzo-pizza-sandwich-pizzaovn",
      "pizzaovn/focaccia-rosmarin-cherrytomater-pizzaovn",
      "grill/grillet-focaccia-pizzasten",
      "stobejern/overnight-sourdough-cast-iron-pizza",
      "roeremaskine/detroit-pizzadej-roeremaskine",
    ],
  },
  {
    slug: "pulled-pork",
    title: "Pulled pork — nakkefilet til trækbar",
    description:
      "Pulled pork komplet: nakkefilet, rub, stall, probe tender og 93–95 °C.",
    recipes: [
      "grill/pulled-pork",
      "grill/asiatisk-sticky-pulled-pork",
      "roeg/smoked-pulled-pork",
      "stobejern/pulled-pork-dutch-oven",
      "sous-vide/pulled-pork-sous-vide",
      "trykkoger/pulled-pork-trykkoger",
      "roeg/smoked-pork-belly-sliders",
      "dips/bbq-sauce",
      "grill/klassisk-kartoffelsalat",
      "sylte/syltede-roedloeg-10-minutter",
      "roeremaskine/brioche-burgerboller-roeremaskine",
    ],
  },
  {
    slug: "fermentering-for-begyndere",
    title: "Fermentering for begyndere — salt, lage og mælkesyre",
    description:
      "Fermentering hjemme: 2 % salt, lage, kahm versus skimmel og temperatur.",
    recipes: [
      "fermentering/klassisk-sauerkraut",
      "fermentering/autentisk-koreansk-kimchi",
      "fermentering/maelkesyregaerde-agurker",
      "fermentering/fermenterede-roedloeg",
      "fermentering/nordisk-gravad-laks",
      "fermentering/saltkonserverede-citroner",
      "fermentering/fermenteret-chili-hot-sauce",
      "fermentering/hjemmelavet-bacon-saltning",
      "fermentering/fermenterede-guleroedsstave-ingefaer",
      "fermentering/curtido",
    ],
  },
  {
    slug: "syltning",
    title: "Syltning — lage, forhold og glas der holder",
    description:
      "Syltning med eddike: forhold, hurtigsylt versus kogning, agurker, rødløg og asier.",
    recipes: [
      "sylte/syltede-agurker",
      "sylte/hurtigsyltede-agurker-10-minutter",
      "sylte/gammeldags-agurkesalat-peberkorn",
      "sylte/asier",
      "sylte/syltede-roedloeg",
      "sylte/syltede-roedloeg-10-minutter",
      "sylte/syltede-jalapenos",
      "sylte/cowboy-candy",
      "sylte/syltede-roedbeder",
      "sylte/syltede-radiser",
      "grill/hjemmelavet-burger",
    ],
  },
  {
    slug: "roegning-hjemme",
    title: "Røgning hjemme — koldrøg versus varmrøg",
    description:
      "Røgning hjemme: koldrøget laks, varmrøg, træsorter, temperatur og sikkerhed.",
    recipes: [
      "roeg/koldroget-laks",
      "grill/koldroget-laks-paa-grill",
      "roeg/hjemmelavet-koldroget-bacon",
      "roeg/varmroget-lakseside",
      "roeg/varmroget-sild",
      "roeg/smoked-beef-brisket",
      "roeg/smoked-pork-ribs",
      "roeg/smoked-pulled-pork",
      "roeg/roget-salt",
      "roeg/smoked-cream-cheese",
      "fermentering/hjemmelavet-bacon-saltning",
    ],
  },
  {
    slug: "grydebroed-og-focaccia",
    title: "Grydebrød og focaccia — skorpe i støbejern",
    description:
      "Grydebrød og focaccia: hydrering, salt i dejen, damp under låg, surdej versus gær.",
    recipes: [
      "stobejern/klassisk-grydebroed",
      "stobejern/grydebroed-oel-kerner",
      "stobejern/grydebroed-hytteost",
      "stobejern/rugbroeds-grydebroed",
      "stobejern/hvidloegs-krydderurte-focaccia",
      "roeremaskine/focaccia-havsalt-roeremaskine",
      "roeremaskine/grydebroad-roeremaskine",
      "pizzaovn/focaccia-rosmarin-cherrytomater-pizzaovn",
      "pizzaovn/roedbede-focaccia-timian-pizzaovn",
      "grill/grillet-focaccia-pizzasten",
      "roeremaskine/ciabatta-roeremaskine",
      "roeremaskine/naanbroed-roeremaskine",
    ],
  },
  {
    slug: "smash-burger",
    title: "Smash burger — plancha, grill og sauce",
    description:
      "Smash burger hjemme: fedtprocent, smash-teknik, ost, bolle og pickles.",
    recipes: [
      "plancha/smash-burger-paa-plancha",
      "plancha/smash-burger-sliders-paa-plancha",
      "stobejern/smash-burgers-stobejern",
      "pizzaovn/smash-burgers-pizzaovn",
      "grill/hjemmelavet-burger",
      "roeremaskine/brioche-burgerboller-roeremaskine",
      "dips/burgersauce",
      "dips/aioli",
      "sylte/syltede-roedloeg-10-minutter",
      "sylte/hurtigsyltede-agurker-10-minutter",
      "airfryer/frosne-pomfritter",
      "airfryer/bacon",
    ],
  },
];

export function getGuidesMentioningRecipe(category: string, slug: string) {
  const key = `${category}/${slug}`;
  return GUIDE_LINKS.filter((guide) => guide.recipes.includes(key));
}
