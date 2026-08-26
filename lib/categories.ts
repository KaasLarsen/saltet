import type { Category } from "./types";
import { getAllCategoriesFromRecipes } from "./recipes";

export const categories: Category[] = [
  {
    slug: "airfryer",
    name: "Airfryer",
    description:
      "Sprøde, saftige retter fra airfryeren — hurtigt, nemt og fuld af smag.",
    headline: "Airfryer opskrifter",
  },
  {
    slug: "grill",
    name: "Grill",
    description:
      "Sommer på grillen — saftigt kød, grønt med røg og klassiske sides til haven.",
    headline: "Grill opskrifter",
  },
  {
    slug: "baalmad",
    name: "Bålmad",
    description:
      "Mad over åben ild — gryderetter i Dutch Oven, kød på risten, fisk med røg og sødt til kaffen, når mørket falder på.",
    headline: "Bålmad opskrifter",
  },
  {
    slug: "roeg",
    name: "Røg",
    description:
      "Koldrøgning, varmrøgning og røgpistol — bacon, laks, BBQ og hurtige indendørs røghacks.",
    headline: "Røg opskrifter",
  },
  {
    slug: "plancha",
    name: "Plancha",
    description:
      "Høj varme på stålpladen — skorpe, saft og plancha-klassikere til have og terrasse.",
    headline: "Plancha opskrifter",
  },
  {
    slug: "gryde",
    name: "Gryde",
    description:
      "Langsom varme i gryden — gryderetter, supper og one-pot-klassikere med dyb smag.",
    headline: "Gryde opskrifter",
  },
  {
    slug: "pande",
    name: "Pande",
    description:
      "Høj varme på panden — skorpe, saft og hverdagsretter der er klar på komfuret.",
    headline: "Pande opskrifter",
  },
  {
    slug: "ovn",
    name: "Ovn",
    description:
      "Almindelig ovn og varmluft — bradepande, bageplade og hverdagsbagning uden pizzaovn.",
    headline: "Ovn opskrifter",
  },
  {
    slug: "sylte",
    name: "Sylte",
    description:
      "Klassisk dansk syltning — syrlige, søde og krydrede glas til smørrebrød, grill og vinterens fade.",
    headline: "Sylte opskrifter",
  },
  {
    slug: "dips",
    name: "Dips",
    description:
      "Dips, dressinger og saucer — fra tzatziki og aioli til mormordressing, mayo-varianter og BBQ.",
    headline: "Dips & dressinger",
  },
  {
    slug: "sous-vide",
    name: "Sous Vide",
    description:
      "Præcise tider og temperaturer til sous vide — oksekød, svin, fjerkræ, fisk og grønt uden gætteri.",
    headline: "Sous vide opskrifter",
  },
  {
    slug: "trykkoger",
    name: "Trykkoger",
    description:
      "Hurtige simreretter i trykkoger og Instant Pot — gullasch, supper, pulled pork og hverdagsretter på en brøkdel af tiden.",
    headline: "Trykkoger opskrifter",
  },
  {
    slug: "dehydrator",
    name: "Dehydrator",
    description:
      "Tørrede snacks, jerky, chips og pulver i dehydrator — frugtlæder, grøntsagschips, krydderier og turmad med præcise temperaturer.",
    headline: "Dehydrator opskrifter",
  },
  {
    slug: "roeremaskine",
    name: "Røremaskine",
    description:
      "Dej, fars og salte klassikere i røremaskine — pizza, brød, pasta, smør og tærtedej med præcis æltning.",
    headline: "Røremaskine opskrifter",
  },
  {
    slug: "pizzaovn",
    name: "Pizzaovn",
    description:
      "Høj varme i pizzaovnen — neapolitansk pizza, fladbrød, støbejernsstegning og after-bake med char og leopard-skorpe.",
    headline: "Pizzaovn opskrifter",
  },
  {
    slug: "stobejern",
    name: "Støbejern",
    description:
      "Støbejern og Dutch Oven — grydebrød med knasende skorpe, langtidssimmer under tungt låg, steak på pande og bålmad.",
    headline: "Støbejern opskrifter",
  },
  {
    slug: "fermentering",
    name: "Fermentering",
    description:
      "Saltning, sprængning og mælkesyregæring — sauerkraut, kimchi, gravad laks, bacon, citroner og umami-nørderi med salt som motor.",
    headline: "Fermentering & saltning",
  },
  {
    slug: "palaeg",
    name: "Pålæg",
    description:
      "Hjemmelavet pålæg, rørte salater og frokostklassikere til rugbrød og madpakke — med syltevarer fra Sylte og remoulade fra Dips som det naturlige tilbehør.",
    headline: "Pålæg opskrifter",
  },
];

export function getCategory(slug: string): Category | undefined {
  const known = categories.find((c) => c.slug === slug);
  if (known) return known;

  // Fallback for kategorier der kun findes via content/recipes/
  if (getAllCategoriesFromRecipes().includes(slug)) {
    const name = slug.charAt(0).toUpperCase() + slug.slice(1);
    return {
      slug,
      name,
      description: `Opskrifter i kategorien ${name}.`,
      headline: `${name} opskrifter`,
    };
  }

  return undefined;
}

export function getCategoryName(slug: string): string {
  return getCategory(slug)?.name ?? slug;
}

export function getAllCategorySlugs(): string[] {
  const fromConfig = categories.map((c) => c.slug);
  const fromRecipes = getAllCategoriesFromRecipes();
  return Array.from(new Set([...fromConfig, ...fromRecipes])).sort();
}
