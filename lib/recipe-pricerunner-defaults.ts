/**
 * Default PriceRunner-produkt pr. opskriftskategori — vist under «Grejet bag retten».
 * Queries skal findes i PRICERUNNER_PRODUCTS.
 */
const RECIPE_PRICERUNNER_DEFAULTS: Record<string, string> = {
  airfryer: "Philips 3000 Series NA352",
  grill: "kuglegrill kul",
  baalmad: "dutch oven med fødder",
  roeg: "koldrøgningsgenerator grill",
  plancha: "Blackstone 2144EU",
  gryde: "dutch oven støbejern",
  pande: "De Buyer Mineral B pande",
  ovn: "bagestål pizza 6 mm",
  sylte: "patentglas",
  dips: "stavblender",
  "sous-vide": "Anova sous vide",
  trykkoger: "Instant Pot trykkoger",
  dehydrator: "dehydrator skuffer",
  roeremaskine: "KitchenAid Artisan 5KSM125",
  pizzaovn: "Ooni Koda gas pizzaovn",
  stobejern: "Lodge støbejernspande",
  fermentering: "patentglas fermentering",
  palaeg: "pålægsmaskine",
  antipasti: "Microplane rivejern",
};

export function getRecipePriceRunnerQuery(
  category: string
): string | undefined {
  return RECIPE_PRICERUNNER_DEFAULTS[category];
}
