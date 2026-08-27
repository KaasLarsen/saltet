import {
  DH_WINES_PRODUCTS,
  FREDSTONE_PRODUCTS,
  OKO_PRODUCTS,
  detectGroceryLanding,
} from "@/lib/affiliate-products";
import { PRICERUNNER_PRODUCTS } from "@/lib/pricerunner-products";
import {
  pricerunnerProductUrl,
  pricerunnerSearchUrl,
} from "@/lib/pricerunner";
import type { Recipe } from "@/lib/types";
import {
  DH_WINES_BANNER_ID,
  DH_WINES_SHOP_URL,
  FREDSTONE_BANNER_ID,
  OKO_SUPERMARKED_BANNER_ID,
  barsetBanner,
  oaterBanner,
  partnerAdsProductUrl,
} from "@/lib/partners";

/** CTA-varianter — grocery / meal_kit aktiveres når partnere lander. */
export type AffiliateVariant = "grej" | "grocery" | "meal_kit" | "wine";

export type WineStyle = "red" | "white" | "any";

export interface AffiliateOffer {
  id: string;
  href: string;
  label: string;
  merchant: string;
  description: string;
  ctaLabel: string;
  variant: AffiliateVariant;
  /** Grej-slugs der auto-matcher denne anbefaling på opskrifter. */
  grejSlugs?: string[];
  /** Kategorier hvor tilbuddet er relevant (fallback). */
  categories?: string[];
  /** Sat til false for stub-partnere der endnu ikke er live. */
  enabled?: boolean;
}

function fromPriceRunner(queryKey: string): string {
  const mapped = PRICERUNNER_PRODUCTS[queryKey];
  if (!mapped) return pricerunnerSearchUrl(queryKey);
  return pricerunnerProductUrl(mapped.categoryId, mapped.productId);
}

/**
 * Centralt affiliate-register. Skift tracking-URL her — alle CTA’er og
 * `affiliate:id`-links følger med.
 */
export const AFFILIATE_OFFERS: Record<string, AffiliateOffer> = {
  "meater-plus": {
    id: "meater-plus",
    href: fromPriceRunner("trådløst stegetermometer"),
    label: "MEATER Plus",
    merchant: "via PriceRunner",
    description:
      "Trådløs sonde med base uden for grillen — så du rammer kernen uden at åbne låget.",
    ctaLabel: "Se aktuel pris",
    variant: "grej",
    grejSlugs: [
      "tradlost-stegetermometer",
      "instant-read-vs-bluetooth-termometer",
    ],
  },
  "meater-pro": {
    id: "meater-pro",
    href: fromPriceRunner("Meater termometer"),
    label: "MEATER Pro",
    merchant: "via PriceRunner",
    description:
      "Flere sonder og stærkere rækkevidde, når du kører flere stege eller rotisseri.",
    ctaLabel: "Se aktuel pris",
    variant: "grej",
    grejSlugs: ["tradlost-stegetermometer"],
  },
  "weber-rotisserie": {
    id: "weber-rotisserie",
    href: fromPriceRunner("rotisseri grill universal"),
    label: "Weber rotisserie",
    merchant: "via PriceRunner",
    description:
      "Jævn rotation giver sprød svær hele vejen rundt — klassisk grej til flæskesteg og and.",
    ctaLabel: "Se aktuel pris",
    variant: "grej",
    grejSlugs: ["rotisseri-til-grillen"],
  },
  "lodge-dutch-oven": {
    id: "lodge-dutch-oven",
    href: fromPriceRunner("dutch oven støbejern"),
    label: "Lodge Dutch Oven 26 cm",
    merchant: "via PriceRunner",
    description:
      "Tungt låg, jævn varme — det der gør grydebrød og langtidssimrede gryderetter til bageri-kvalitet.",
    ctaLabel: "Se aktuel pris",
    variant: "grej",
    grejSlugs: ["stoebjernsgryde-storrelsesguide", "stoebjern-rene-skole"],
    categories: ["stobejern", "gryde"],
  },
  "petromax-dutch-oven": {
    id: "petromax-dutch-oven",
    href: fromPriceRunner("Dutch Oven støbejern 8 liter"),
    label: "Petromax Dutch Oven ft18",
    merchant: "via PriceRunner",
    description:
      "Stor bål-gryde med fødder — til gullasch, chili og alt der skal simre i gløderne.",
    ctaLabel: "Se aktuel pris",
    variant: "grej",
    grejSlugs: ["baalgrej-til-baghaven"],
    categories: ["baalmad"],
  },
  "lodge-skillet": {
    id: "lodge-skillet",
    href: fromPriceRunner("Lodge støbejernspande"),
    label: "Lodge støbejernspande 26 cm",
    merchant: "via PriceRunner",
    description:
      "Den pande vi når efter til smash, chili-start og alt der skal have skorpe.",
    ctaLabel: "Se aktuel pris",
    variant: "grej",
    grejSlugs: ["stoebejern-vs-carbonstaal", "smashburger-grej"],
  },
  "ninja-airfryer": {
    id: "ninja-airfryer",
    href: fromPriceRunner("Ninja airfryer"),
    label: "Ninja Foodi Max Dual Zone",
    merchant: "via PriceRunner",
    description:
      "To zoner, så sticky vinger og tilbehør lander samtidig — uden at fylde ovnen.",
    ctaLabel: "Se aktuel pris",
    variant: "grej",
    grejSlugs: ["airfryer-vs-ovn-opgoer", "airfryer-tilbehoer"],
    categories: ["airfryer"],
  },
  "ooni-infrared": {
    id: "ooni-infrared",
    href: fromPriceRunner("infrarødt termometer"),
    label: "Ooni infrarødt termometer",
    merchant: "via PriceRunner",
    description:
      "Mål stenens overflade på et sekund — så du ved, hvornår pizzaovnen er klar.",
    ctaLabel: "Se aktuel pris",
    variant: "grej",
    grejSlugs: [
      "infrared-termometer-pizza",
      "infrared-termometer-test",
      "hvilken-pizzaovn",
    ],
    categories: ["pizzaovn"],
  },
  fredstone: {
    id: "fredstone",
    href: partnerAdsProductUrl(FREDSTONE_BANNER_ID, FREDSTONE_PRODUCTS.rund36),
    label: "Fredstone pizzasten Ø 36 cm",
    merchant: "Fredstone",
    description:
      "Danskproduceret rund sten til grill — holder varmen, så bunden bliver sprød pizza efter pizza.",
    ctaLabel: "Se Fredstone Ø 36",
    variant: "grej",
    grejSlugs: ["bagestaal-vs-bagesten", "pizzasten-rengoering"],
  },
  "fredstone-bagesten": {
    id: "fredstone-bagesten",
    href: partnerAdsProductUrl(
      FREDSTONE_BANNER_ID,
      FREDSTONE_PRODUCTS.bagesten60
    ),
    label: "Fredstone bagesten 60×30,5 cm",
    merchant: "Fredstone",
    description:
      "Rektangulær bagesten til focaccia og brød på grillen — jævn undervarme uden at brænde igennem.",
    ctaLabel: "Se Fredstone bagesten",
    variant: "grej",
  },
  "dh-wines": {
    id: "dh-wines",
    href: partnerAdsProductUrl(DH_WINES_BANNER_ID, DH_WINES_PRODUCTS.shop),
    label: "DH Wines",
    merchant: "DH Wines",
    description:
      "Retten bruger vin — find en flaske der matcher hos DH Wines.",
    ctaLabel: "Find vin til retten",
    variant: "wine",
  },
  "dh-wines-hvid": {
    id: "dh-wines-hvid",
    href: partnerAdsProductUrl(
      DH_WINES_BANNER_ID,
      DH_WINES_PRODUCTS.simonsigChenin
    ),
    label: "Simonsig Chenin Blanc",
    merchant: "DH Wines",
    description:
      "Tør, frisk Chenin Blanc til madlavning og skaldyr — 119 kr hos DH Wines.",
    ctaLabel: "Køb hvidvinen",
    variant: "wine",
  },
  "dh-wines-rood": {
    id: "dh-wines-rood",
    href: partnerAdsProductUrl(
      DH_WINES_BANNER_ID,
      DH_WINES_PRODUCTS.rodCollection
    ),
    label: "Rødvin til madlavning",
    merchant: "DH Wines",
    description:
      "Hverdagsrødvin i 100–200 kr-klassen — til gryderetter, sauce og glasset ved siden af.",
    ctaLabel: "Se rødvine",
    variant: "wine",
  },
  "okologisk-supermarked": {
    id: "okologisk-supermarked",
    href: partnerAdsProductUrl(
      OKO_SUPERMARKED_BANNER_ID,
      OKO_PRODUCTS.madOgDrikke
    ),
    label: "Økologisk-Supermarked",
    merchant: "Økologisk-Supermarked",
    description:
      "Mangler du økologisk mel, olie eller krydderier? Find basisvarerne hos Økologisk-Supermarked.",
    ctaLabel: "Find ingredienserne",
    variant: "grocery",
  },
  "oko-hvedemel": {
    id: "oko-hvedemel",
    href: partnerAdsProductUrl(
      OKO_SUPERMARKED_BANNER_ID,
      OKO_PRODUCTS.fintHvedemel
    ),
    label: "Økologisk hvedemel",
    merchant: "Økologisk-Supermarked",
    description: "Fint økologisk hvedemel til brød, focaccia og dej.",
    ctaLabel: "Køb melet",
    variant: "grocery",
  },
  "oko-olivenolie": {
    id: "oko-olivenolie",
    href: partnerAdsProductUrl(
      OKO_SUPERMARKED_BANNER_ID,
      OKO_PRODUCTS.olivenolie
    ),
    label: "Økologisk olivenolie",
    merchant: "Økologisk-Supermarked",
    description: "Ekstra jomfru olivenolie — til stegning, dressing og dej.",
    ctaLabel: "Køb olien",
    variant: "grocery",
  },
  rullepoelsepresser: {
    id: "rullepoelsepresser",
    href: pricerunnerSearchUrl("rullepølsepresse"),
    label: "Rullepølsepresse",
    merchant: "via PriceRunner",
    description:
      "Jævnt natte-tryk giver tætte skiver — bedre end bræt-og-gryde, når du laver mere end én rulle.",
    ctaLabel: "Find priser",
    variant: "grej",
    grejSlugs: ["rullepoelsepresser-trae-vs-staal"],
  },
  palaegsmaskine: {
    id: "palaegsmaskine",
    href: pricerunnerSearchUrl("pålægsmaskine"),
    label: "Pålægsmaskine",
    merchant: "via PriceRunner",
    description:
      "Papirtynde skiver af rullepølse og sprængt oksebryst — kniven skal være skarp, kødet koldt.",
    ctaLabel: "Find priser",
    variant: "grej",
    grejSlugs: ["palaegsmaskine-pro-vs-billig", "elektrisk-palaegskniv"],
  },
  oater: {
    id: "oater",
    href: oaterBanner.href,
    label: "Oater 2.0",
    merchant: "Partner-ads",
    description: "Frisk havremælk på få minutter — til kaffe, grød og bagning.",
    ctaLabel: "Se tilbud",
    variant: "grej",
  },
  barset: {
    id: "barset",
    href: barsetBanner.href,
    label: "Barsæt",
    merchant: "Partner-ads",
    description: "Dit eget barsæt — til drinks der matcher det fede køkkenbord.",
    ctaLabel: "Se tilbud",
    variant: "grej",
  },

  // --- Fase 2+ stubs (enabled: false indtil partneraftale) ---
  nemlig: {
    id: "nemlig",
    href: "#",
    label: "Nemlig.com",
    merchant: "Nemlig",
    description:
      "Mangler du ingredienserne? Føj dem til kurven og få dem leveret.",
    ctaLabel: "Tilføj til kurv",
    variant: "grocery",
    enabled: false,
  },
  hellofresh: {
    id: "hellofresh",
    href: "#",
    label: "HelloFresh",
    merchant: "HelloFresh",
    description:
      "Kniber det med tiden? Få en måltidskasse leveret — klar opskrift, målte ingredienser.",
    ctaLabel: "Få rabat på første kasse",
    variant: "meal_kit",
    enabled: false,
    categories: [],
  },
};

const AFFILIATE_PREFIX = "affiliate:";

const COOKING_WINE_RE =
  /\b(rødvin|hvidvin|portvin|madeira|marsala|sherry|champagne|prosecco|cava|vin)\b/i;

/**
 * Pantry-/basisvarer Økologisk-Supermarked typisk fører.
 * Salt/peber alene tæller ikke — så rene kød-grillopskrifter springes over.
 */
const PANTRY_INGREDIENT_RE =
  /olivenolie|rapsolie|sesamolie|hvedemel|tipo\s*00|rugmel|sennep|eddike|honning|sukker|bouillon|tomatpur[eé]|sojasauce|soya\b|gochujang|mayonnaise|cr[eè]me fraiche|paprika|kommen|oregano|rosmarin|timian|dijon|kokos|sesam|bønner|linser|kikært|\bris\b|pasta|nudler|gær|bagepulver|flagesalt|havsalt|smør\b|olie\b|mel\b/i;

/** True når opskriften bruger vin som ingrediens (ikke eddike/vinrester). */
export function recipeUsesCookingWine(ingredients: string[]): boolean {
  return ingredients.some((item) => {
    const lower = item.toLowerCase();
    if (lower.includes("eddike")) return false;
    if (lower.includes("vinrester")) return false;
    return COOKING_WINE_RE.test(item);
  });
}

/** True når opskriften har pantry-varer relevante for Økologisk-Supermarked. */
export function recipeHasPantryIngredients(ingredients: string[]): boolean {
  return ingredients.some((item) => PANTRY_INGREDIENT_RE.test(item));
}

export function detectWineStyle(ingredients: string[]): WineStyle {
  const text = ingredients.join(" ").toLowerCase();
  const hasRed = /rødvin|portvin|madeira/.test(text);
  const hasWhite = /hvidvin|champagne|prosecco|cava|sherry/.test(text);
  if (hasRed && !hasWhite) return "red";
  if (hasWhite && !hasRed) return "white";
  return "any";
}

function wineOfferForStyle(style: WineStyle): AffiliateOffer | undefined {
  if (style === "white") return getAffiliateOffer("dh-wines-hvid");
  if (style === "red") return getAffiliateOffer("dh-wines-rood");
  return getAffiliateOffer("dh-wines");
}

/**
 * Byg tracked DH Wines-link til en konkret produkt-URL fra shoppen.
 * Brug i frontmatter: affiliateWineUrl: https://dhwines.dk/products/...
 */
export function dhWinesTrackedUrl(
  productUrl: string = DH_WINES_SHOP_URL
): string {
  return partnerAdsProductUrl(DH_WINES_BANNER_ID, productUrl);
}

/** Tracked Fredstone-link til konkret produkt-URL på fredstone.dk. */
export function fredstoneTrackedUrl(
  productUrl: string = FREDSTONE_PRODUCTS.rund36
): string {
  return partnerAdsProductUrl(FREDSTONE_BANNER_ID, productUrl);
}

/** Tracked Økologisk-Supermarked-link. */
export function okoSupermarkedTrackedUrl(
  productUrl: string = OKO_PRODUCTS.madOgDrikke
): string {
  return partnerAdsProductUrl(OKO_SUPERMARKED_BANNER_ID, productUrl);
}

export function getAffiliateOffer(id: string): AffiliateOffer | undefined {
  const offer = AFFILIATE_OFFERS[id];
  if (!offer || offer.enabled === false) return undefined;
  return offer;
}

export function getAffiliateOffersByVariant(
  variant: AffiliateVariant
): AffiliateOffer[] {
  return Object.values(AFFILIATE_OFFERS).filter(
    (o) => o.variant === variant && o.enabled !== false
  );
}

/** Eyebrow-tekst til native CTA efter variant. */
export function affiliateVariantLabel(variant: AffiliateVariant): string {
  switch (variant) {
    case "grocery":
      return "Indkøb";
    case "meal_kit":
      return "Måltidskasse";
    case "wine":
      return "Vin til retten";
    default:
      return "Grej vi bruger";
  }
}

/**
 * Resolve `affiliate:id` (og almindelige URL’er) til et klikbart link.
 * Ukendt affiliate-id returnerer null, så teksten kan renderes uden link.
 */
export function resolveAffiliateLink(rawHref: string): {
  href: string;
  external: boolean;
  rel?: string;
} | null {
  if (rawHref.startsWith(AFFILIATE_PREFIX)) {
    const id = rawHref.slice(AFFILIATE_PREFIX.length);
    const offer = getAffiliateOffer(id);
    if (!offer) return null;
    return {
      href: offer.href,
      external: true,
      rel: "nofollow noopener sponsored",
    };
  }

  if (/^https?:\/\//i.test(rawHref)) {
    return {
      href: rawHref,
      external: true,
      rel: "nofollow noopener sponsored",
    };
  }

  return { href: rawHref, external: false };
}

/**
 * Vælg ét grej-produkt til en opskrift: eksplicit frontmatter → grej-match → kategori.
 */
export function getAffiliateOfferForRecipe(
  recipe: Pick<Recipe, "category" | "affiliateProduct" | "relatedGrej">,
  relatedGrejSlugs: string[] = []
): AffiliateOffer | undefined {
  if (recipe.affiliateProduct) {
    const offer = getAffiliateOffer(recipe.affiliateProduct);
    if (offer?.variant === "grej") return offer;
  }

  const grejSlugs = [
    ...(recipe.relatedGrej ?? []),
    ...relatedGrejSlugs,
  ];

  for (const slug of grejSlugs) {
    const match = Object.values(AFFILIATE_OFFERS).find(
      (o) =>
        o.enabled !== false &&
        o.variant === "grej" &&
        o.grejSlugs?.includes(slug)
    );
    if (match) return match;
  }

  const byCategory = Object.values(AFFILIATE_OFFERS).find(
    (o) =>
      o.enabled !== false &&
      o.variant === "grej" &&
      o.categories?.includes(recipe.category)
  );
  return byCategory;
}

/**
 * Vin-CTA når opskriften bruger vin som ingrediens.
 * Valgfri `affiliateWineUrl` = direkte produktlink fra dhwines.dk (wrap'es i tracking).
 */
export function getWineAffiliateOfferForRecipe(
  recipe: Pick<Recipe, "ingredients" | "affiliateWineUrl">
): AffiliateOffer | undefined {
  if (recipe.affiliateWineUrl) {
    const base = getAffiliateOffer("dh-wines");
    if (!base) return undefined;
    return {
      ...base,
      href: dhWinesTrackedUrl(recipe.affiliateWineUrl),
      description:
        "Vi bruger denne vin til retten — se aktuel pris hos DH Wines.",
    };
  }

  if (!recipeUsesCookingWine(recipe.ingredients)) return undefined;

  const style = detectWineStyle(recipe.ingredients);
  return wineOfferForStyle(style);
}

/**
 * Grocery-CTA under ingredienser (Økologisk-Supermarked).
 * Vælger konkret vare/kategori (mel, olie, krydderier…) ud fra opskriften.
 */
export function getGroceryAffiliateOfferForRecipe(
  recipe: Pick<
    Recipe,
    | "ingredients"
    | "featured"
    | "affiliateGrocery"
    | "affiliateGroceryUrl"
    | "tags"
  >
): AffiliateOffer | undefined {
  if (recipe.affiliateGrocery === false) return undefined;

  const base = getAffiliateOffer("okologisk-supermarked");
  if (!base) return undefined;

  if (recipe.affiliateGroceryUrl) {
    return {
      ...base,
      href: okoSupermarkedTrackedUrl(recipe.affiliateGroceryUrl),
      description:
        "Find den økologiske vare til retten hos Økologisk-Supermarked.",
    };
  }

  const forceOn = recipe.affiliateGrocery === true;
  const hasPantry = recipeHasPantryIngredients(recipe.ingredients);
  const organicTag = (recipe.tags ?? []).some((t) =>
    /økologisk|organic|vegetar|vegan/i.test(t)
  );

  if (!forceOn && !hasPantry && !recipe.featured && !organicTag) {
    return undefined;
  }

  const landing = detectGroceryLanding(recipe.ingredients);
  if (landing.kind === "mel") {
    const mel = getAffiliateOffer("oko-hvedemel");
    if (mel) return { ...mel, description: landing.hint };
  }
  if (landing.kind === "olie") {
    const olie = getAffiliateOffer("oko-olivenolie");
    if (olie) return { ...olie, description: landing.hint };
  }

  return {
    ...base,
    href: okoSupermarkedTrackedUrl(landing.url),
    description: landing.hint,
  };
}
