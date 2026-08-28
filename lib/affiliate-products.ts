/**
 * Kuraterede produkt-URL’er til Partner-ads (htmlurl=…).
 * Skift her når en vare er udsolgt — tracking-banner-ID’er ligger i partners.ts.
 */

export const DH_WINES_PRODUCTS = {
  shop: "https://dhwines.dk/",
  /** Madlavnings-/hverdagsrødvin */
  rodCollection: "https://dhwines.dk/collections/rodvine-100-200-kr",
  /** Sprød hvidvin til madlavning og skaldyr */
  simonsigChenin:
    "https://dhwines.dk/products/simonsig-chenin-blanc-stellenbosch-2024",
  proteaChenin:
    "https://dhwines.dk/products/anthonij-rupert-protea-chenin-blanc-2025",
} as const;

export const FREDSTONE_PRODUCTS = {
  shop: "https://fredstone.dk/",
  catalog: "https://fredstone.dk/shop/10-pizza--bagesten-til-grill/",
  /** Mest alsidige rund sten til kuglegrill / almindelig grill */
  rund36:
    "https://fredstone.dk/shop/10-pizza--bagesten-til-grill/92-fredstone-rund-pizzasten-oe-36-x-16-cm/",
  /** Rektangulær bagesten til focaccia og brød */
  bagesten60:
    "https://fredstone.dk/shop/10-pizza--bagesten-til-grill/26-fredstone-bagesten-600-x-305-cm-20-cm-tykkelse/",
  pizzasten60:
    "https://fredstone.dk/shop/10-pizza--bagesten-til-grill/35-fredstone-pizzasten-600-x-305-cm-16-cm-tykkelse/",
  pizzakit:
    "https://fredstone.dk/shop/43-spar-10---pizzakit---pakketilbud/",
} as const;

const OKO = "https://www.okologisk-supermarked.dk";

export const OKO_PRODUCTS = {
  shop: `${OKO}/`,
  madOgDrikke: `${OKO}/shop/mad-og-drikke-8s1.html`,
  mel: `${OKO}/shop/mel-527c1.html`,
  olier: `${OKO}/shop/olier-515c1.html`,
  krydderier: `${OKO}/shop/krydderier-og-urter-186c1.html`,
  saltBouillon: `${OKO}/shop/salt-bouillon-og-185c1.html`,
  sennep: `${OKO}/shop/ketchup-og-sennep-514c1.html`,
  /** Konkrete favoritter */
  fintHvedemel: `${OKO}/shop/fint-hvede-mel-5417p.html`,
  olivenolie: `${OKO}/shop/ekstra-jomfru-olivenolie-6103p.html`,
} as const;

/** Rito.dk — kun sylteglas (ikke garn/hobby-resten af sortimentet). */
export const RITO_PRODUCTS = {
  shop: "https://rito.dk/",
  /** 370 ml skruelåg — god standardstørrelse til asier og pickles */
  sylteglas370:
    "https://rito.dk/lysglas-skale-og-krukker-til-dekoration/28727-sylteglas-h-11-cm-diam-75-cm-370-ml-transparent-6-stk-1-pk-5712854072816.html",
  /** 240 ml — til mindre portioner / gaver */
  sylteglas240:
    "https://rito.dk/lysglas-skale-og-krukker-til-dekoration/28726-sylteglas-h-91-cm-diam-68-cm-240-ml-transparent-12-stk-1-pk-5712854072793.html",
  /** 100 ml — til smagsprøver og chili */
  sylteglas100:
    "https://rito.dk/lysglas-skale-og-krukker-til-dekoration/28725-sylteglas-h-65-cm-diam-57-cm-transparent-12stk-100-ml-5712854072779.html",
} as const;

/** Homeshop.dk — airfryere, termometre, grilltilbehør */
export const HOMESHOP_PRODUCTS = {
  shop: "https://www.homeshop.dk/",
  airfryerCategory: "https://www.homeshop.dk/airfryer/",
  /** Dual basket — to zoner til hovedret + tilbehør */
  philipsDual:
    "https://www.homeshop.dk/airfryer/philips-na352-00-dual-basket-airfryer",
  philipsXxl:
    "https://www.homeshop.dk/airfryer/philips-hd9285-96-xxl-connected-airfryer",
  meaterPlus:
    "https://www.homeshop.dk/termometre/meater-plus-tasty-perk-tradlost-stege-termometer-til-iphoneandroid",
  meaterPro:
    "https://www.homeshop.dk/termometre/meater-2-plus-tradlost-stege-termometer",
  /** Rustfrit smash-jern til plancha og stegeplade */
  broilKingSmashBurger:
    "https://www.homeshop.dk/broil-king-tilbehor/broil-king-smash-burger-jern",
} as const;

/** KitchenOne — Instant Pot / trykkogere */
export const KITCHENONE_PRODUCTS = {
  shop: "https://www.kitchenone.dk/",
  trykkogerCategory:
    "https://www.kitchenone.dk/c/madlavning/kogegrej-stegepander/trykkoger/",
  instantPotDuoPlus:
    "https://www.kitchenone.dk/p/instant-pot-duo-plus-trykkoger_65827/",
  instantDuoCrisp:
    "https://www.kitchenone.dk/p/instant-duo-crisp-airfryer-trykkoger-11-i-1-5-7-liter_65815/",
} as const;

/** Boligcenter.dk — kogegrej */
export const BOLIGCENTER_PRODUCTS = {
  shop: "https://www.boligcenter.dk/",
  gryderOgStegepander:
    "https://www.boligcenter.dk/hjem-og-husholdning/kokken/gryder-og-stegepander/",
  /** Rund støbejernspande — hverdagsstegepande til pande-retter */
  stegepande30:
    "https://www.boligcenter.dk/hjem-og-husholdning/kokken/gryder-og-stegepander/pander/grillpande/xl-bbq-grill-stegepande-i-stobejern-30-cm-rund",
  /** Tre størrelser — godt start-sæt */
  stegepandeSaet3:
    "https://www.boligcenter.dk/hjem-og-husholdning/kokken/gryder-og-stegepander/pander/grillpande/bbq-stegepander-saet-af-3-stobejern",
  /** Klassisk 5 l støbejernsgryde til simreretter */
  stoebjernsgryde5l:
    "https://www.boligcenter.dk/hjem-og-husholdning/kokken/gryder-og-stegepander/gryder/suppegryder/gryde-o265-cm-stobejern",
  /** Hollandsk ovn med tilbehør — bål / udendørs */
  hollandskOvn56:
    "https://www.boligcenter.dk/hjem-og-husholdning/kokken/gryder-og-stegepander/pander/stegepander/stobejern/hollandsk-ovn-56-l-inklusiv-tilbehor",
  kokkenknive:
    "https://www.boligcenter.dk/hjem-og-husholdning/kokken/kokkenknive/",
  airfryer:
    "https://www.boligcenter.dk/hjem-og-husholdning/kokken/kokkenapparater/airfryer/",
} as const;

export type GroceryLandingKind =
  | "mel"
  | "olie"
  | "krydderi"
  | "sennep"
  | "salt"
  | "general";

/** Vælg den mest relevante Øko-kategori ud fra ingredienslisten. */
export function detectGroceryLanding(
  ingredients: string[]
): { kind: GroceryLandingKind; url: string; hint: string } {
  const text = ingredients.join(" ").toLowerCase();

  if (/hvedemel|tipo|rugmel|speltmel|\bmel\b|gær|bagepulver/.test(text)) {
    return {
      kind: "mel",
      url: OKO_PRODUCTS.fintHvedemel,
      hint: "Økologisk hvedemel til dejen — find det hos Økologisk-Supermarked.",
    };
  }
  if (/olivenolie|rapsolie|sesamolie|\bolie\b/.test(text)) {
    return {
      kind: "olie",
      url: OKO_PRODUCTS.olivenolie,
      hint: "Økologisk olivenolie til retten — find den hos Økologisk-Supermarked.",
    };
  }
  if (/sennep|dijon|ketchup/.test(text)) {
    return {
      kind: "sennep",
      url: OKO_PRODUCTS.sennep,
      hint: "Økologisk sennep og dressing — hos Økologisk-Supermarked.",
    };
  }
  if (
    /paprika|kommen|oregano|rosmarin|timian|krydderi|chili|bouillon|havsalt|flagesalt/.test(
      text
    )
  ) {
    return {
      kind: "krydderi",
      url: OKO_PRODUCTS.krydderier,
      hint: "Økologiske krydderier og urter — hos Økologisk-Supermarked.",
    };
  }

  return {
    kind: "general",
    url: OKO_PRODUCTS.madOgDrikke,
    hint: "Mangler du økologiske basisvarer? Find dem hos Økologisk-Supermarked.",
  };
}
