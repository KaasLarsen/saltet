import {
  DH_WINES_PRODUCTS,
  FREDSTONE_PRODUCTS,
  HOMESHOP_PRODUCTS,
  KITCHENONE_PRODUCTS,
  BOLIGCENTER_PRODUCTS,
  OKO_PRODUCTS,
  RITO_PRODUCTS,
  detectGroceryLanding,
} from "@/lib/affiliate-products";
import { PRICERUNNER_PRODUCTS } from "@/lib/pricerunner-products";
import {
  pricerunnerProductUrl,
  pricerunnerSearchUrl,
} from "@/lib/pricerunner";
import type { Recipe } from "@/lib/types";
import {
  BOLIGCENTER_BANNER_ID,
  DH_WINES_BANNER_ID,
  DH_WINES_SHOP_URL,
  FREDSTONE_BANNER_ID,
  HOMESHOP_BANNER_ID,
  KITCHENONE_BANNER_ID,
  OKO_SUPERMARKED_BANNER_ID,
  RITO_BANNER_ID,
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
    href: partnerAdsProductUrl(
      HOMESHOP_BANNER_ID,
      HOMESHOP_PRODUCTS.meaterPlus
    ),
    label: "MEATER Plus",
    merchant: "Homeshop",
    description:
      "Trådløs sonde med base uden for grillen — så du rammer kernen uden at åbne låget.",
    ctaLabel: "Se hos Homeshop",
    variant: "grej",
    grejSlugs: [
      "tradlost-stegetermometer",
      "instant-read-vs-bluetooth-termometer",
      "termometer-til-andesteg",
    ],
  },
  "meater-pro": {
    id: "meater-pro",
    href: partnerAdsProductUrl(
      HOMESHOP_BANNER_ID,
      HOMESHOP_PRODUCTS.meaterPro
    ),
    label: "MEATER Pro",
    merchant: "Homeshop",
    description:
      "Flere sonder og stærkere varme-tolerance — når du kører grill, rotisseri eller åben ild.",
    ctaLabel: "Se hos Homeshop",
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
    categories: ["stobejern"],
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
  "homeshop-airfryer": {
    id: "homeshop-airfryer",
    href: partnerAdsProductUrl(
      HOMESHOP_BANNER_ID,
      HOMESHOP_PRODUCTS.philipsDual
    ),
    label: "Philips Dual Basket Airfryer",
    merchant: "Homeshop",
    description:
      "To kurve, så sticky vinger og tilbehør lander samtidig — uden at fylde ovnen.",
    ctaLabel: "Se hos Homeshop",
    variant: "grej",
    grejSlugs: ["airfryer-vs-ovn-opgoer", "airfryer-tilbehoer"],
    categories: ["airfryer"],
  },
  "homeshop-smash-burger-jern": {
    id: "homeshop-smash-burger-jern",
    href: partnerAdsProductUrl(
      HOMESHOP_BANNER_ID,
      HOMESHOP_PRODUCTS.broilKingSmashBurger
    ),
    label: "Broil King Smash Burger Jern",
    merchant: "Homeshop",
    description:
      "Rustfrit stål med tresidet konstruktion — tryk bøfferne flade på plancha eller støbejern uden at brænde fingrene.",
    ctaLabel: "Se hos Homeshop",
    variant: "grej",
    grejSlugs: ["smashburger-grej"],
  },
  "homeshop-grillspartel-bred": {
    id: "homeshop-grillspartel-bred",
    href: partnerAdsProductUrl(
      HOMESHOP_BANNER_ID,
      HOMESHOP_PRODUCTS.broilKingGrillSpartelBred
    ),
    label: "Broil King Imperial Grillspartel Bred",
    merchant: "Homeshop",
    description:
      "1,8 mm rustfrit stål med bred flade — flip smash-bøffer og skrab skorpen løs uden at bøje bladet.",
    ctaLabel: "Se hos Homeshop",
    variant: "grej",
    grejSlugs: ["smashburger-grej"],
  },
  "homeshop-burger-palet": {
    id: "homeshop-burger-palet",
    href: partnerAdsProductUrl(
      HOMESHOP_BANNER_ID,
      HOMESHOP_PRODUCTS.napoleonBurgerPalet
    ),
    label: "Napoleon Plancha Burgerpalet",
    merchant: "Homeshop",
    description:
      "Bred palet i rustfrit stål med skrå kanter — løft og vend smash-burgere på plancha uden at rive skorpen.",
    ctaLabel: "Se hos Homeshop",
    variant: "grej",
    grejSlugs: ["smashburger-grej"],
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
  },
  "kitchenone-instant-pot": {
    id: "kitchenone-instant-pot",
    href: partnerAdsProductUrl(
      KITCHENONE_BANNER_ID,
      KITCHENONE_PRODUCTS.instantPotDuoPlus
    ),
    label: "Instant Pot Duo Plus 5,7 L",
    merchant: "KitchenOne",
    description:
      "Trykkoger til hverdags-simreretter — pulled pork, gullasch og supper på en brøkdel af tiden.",
    ctaLabel: "Se hos KitchenOne",
    variant: "grej",
    grejSlugs: ["trykkoger-vs-slowcooker"],
    categories: ["trykkoger"],
  },
  "boligcenter-stegepande": {
    id: "boligcenter-stegepande",
    href: partnerAdsProductUrl(
      BOLIGCENTER_BANNER_ID,
      BOLIGCENTER_PRODUCTS.stegepande30
    ),
    label: "Støbejernspande 30 cm",
    merchant: "Boligcenter.dk",
    description:
      "Rund støbejernspande til skorpe på hakkebøf, frikadeller og one-pan-retter.",
    ctaLabel: "Se hos Boligcenter",
    variant: "grej",
    grejSlugs: ["smashburger-grej", "plancha-vs-stobejern"],
    categories: ["pande"],
  },
  "boligcenter-stoebjernsgryde": {
    id: "boligcenter-stoebjernsgryde",
    href: partnerAdsProductUrl(
      BOLIGCENTER_BANNER_ID,
      BOLIGCENTER_PRODUCTS.stoebjernsgryde5l
    ),
    label: "Støbejernsgryde 5 L (Ø26,5 cm)",
    merchant: "Boligcenter.dk",
    description:
      "Klassisk størrelse til gullasch, bolognese og alt der skal simre under låg.",
    ctaLabel: "Se hos Boligcenter",
    variant: "grej",
    categories: ["gryde"],
  },
  /** Alias — ældre id’er / eksplicit frontmatter */
  "boligcenter-gryder": {
    id: "boligcenter-gryder",
    href: partnerAdsProductUrl(
      BOLIGCENTER_BANNER_ID,
      BOLIGCENTER_PRODUCTS.stoebjernsgryde5l
    ),
    label: "Støbejernsgryde 5 L (Ø26,5 cm)",
    merchant: "Boligcenter.dk",
    description:
      "Klassisk størrelse til gullasch, bolognese og alt der skal simre under låg.",
    ctaLabel: "Se hos Boligcenter",
    variant: "grej",
  },
  "boligcenter-saucegryde": {
    id: "boligcenter-saucegryde",
    href: partnerAdsProductUrl(
      BOLIGCENTER_BANNER_ID,
      BOLIGCENTER_PRODUCTS.gryderOgStegepander
    ),
    label: "Saucekasserolle / kogegrej",
    merchant: "Boligcenter.dk",
    description:
      "Det rigtige grej sikrer, at sovsen ikke skiller — jævn varme i en god kasserolle slår billig tynd bund hver gang.",
    ctaLabel: "Se kogegrej",
    variant: "grej",
    grejSlugs: ["kobbergryder"],
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
      "Du må aldrig koge sauce på en vin, du ikke vil drikke — find madlavnings- og drikkevin hos DH Wines.",
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
      "Tør hvidvin til sauce og glasset — aldrig den billigste «madlavningsvin», du ikke selv vil drikke.",
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
      "Du må aldrig koge rødvinssauce på en vin, du ikke vil drikke. Find den her i 100–200 kr-klassen.",
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
  "rito-sylteglas": {
    id: "rito-sylteglas",
    href: partnerAdsProductUrl(RITO_BANNER_ID, RITO_PRODUCTS.sylteglas370),
    label: "Sylteglas 370 ml (6 stk.)",
    merchant: "Rito.dk",
    description:
      "Klare henkogningsglas med skruelåg — til asier, pickles og det der skal på hylden.",
    ctaLabel: "Se sylteglas",
    variant: "grej",
    grejSlugs: ["sildekrukker-patentglas"],
    categories: ["sylte"],
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

/** Tracked Rito-link (kun brug til sylteglas — ikke garn). */
export function ritoTrackedUrl(
  productUrl: string = RITO_PRODUCTS.sylteglas370
): string {
  return partnerAdsProductUrl(RITO_BANNER_ID, productUrl);
}

/** Tracked Homeshop-link. */
export function homeshopTrackedUrl(
  productUrl: string = HOMESHOP_PRODUCTS.philipsDual
): string {
  return partnerAdsProductUrl(HOMESHOP_BANNER_ID, productUrl);
}

export function kitchenoneTrackedUrl(
  productUrl: string = KITCHENONE_PRODUCTS.instantPotDuoPlus
): string {
  return partnerAdsProductUrl(KITCHENONE_BANNER_ID, productUrl);
}

export function boligcenterTrackedUrl(
  productUrl: string = BOLIGCENTER_PRODUCTS.stegepande30
): string {
  return partnerAdsProductUrl(BOLIGCENTER_BANNER_ID, productUrl);
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
