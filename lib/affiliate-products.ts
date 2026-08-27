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
