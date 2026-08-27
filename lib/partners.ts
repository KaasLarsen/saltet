export interface PartnerBannerConfig {
  href: string;
  imgSrc: string;
  alt: string;
}

export const PARTNER_ADS_PARTNER_ID = "57393";

/** DH Wines — deep link via htmlurl=produktlink */
export const DH_WINES_BANNER_ID = "108257";
export const DH_WINES_SHOP_URL = "https://dhwines.dk/";

/** Fredstone pizza- og bagesten — deep link via htmlurl=produktlink */
export const FREDSTONE_BANNER_ID = "109380";
export const FREDSTONE_SHOP_URL = "https://fredstone.dk/";

/** Økologisk-Supermarked — deep link via htmlurl=produktlink */
export const OKO_SUPERMARKED_BANNER_ID = "100052";
export const OKO_SUPERMARKED_SHOP_URL =
  "https://www.okologisk-supermarked.dk/";

/** Rito.dk — kun sylteglas (butikken er ellers garn/hobby) */
export const RITO_BANNER_ID = "30292";
export const RITO_SHOP_URL = "https://rito.dk/";

/** Homeshop — airfryere, termometre og køkkenudstyr */
export const HOMESHOP_BANNER_ID = "74171";
export const HOMESHOP_SHOP_URL = "https://www.homeshop.dk/";

/**
 * Partner-ads produktlink:
 * klikbanner.php?partnerid=…&bannerid=…&htmlurl=PRODUKTLINK
 */
export function partnerAdsProductUrl(
  bannerId: string,
  productUrl: string,
  partnerId: string = PARTNER_ADS_PARTNER_ID
): string {
  const params = new URLSearchParams({
    partnerid: partnerId,
    bannerid: bannerId,
    htmlurl: productUrl,
  });
  return `https://www.partner-ads.com/dk/klikbanner.php?${params.toString()}`;
}

/** Mellem opskrifter og guides */
export const oaterBanner: PartnerBannerConfig = {
  href: "https://www.partner-ads.com/dk/klikbanner.php?partnerid=57393&bannerid=116078",
  imgSrc:
    "https://www.partner-ads.com/dk/visbanner.php?partnerid=57393&bannerid=116078",
  alt: "Oater 2.0 — frisk havremælk på få minutter",
};

/** Mellem guides og grej */
export const barsetBanner: PartnerBannerConfig = {
  href: "https://www.partner-ads.com/dk/klikbanner.php?partnerid=57393&bannerid=34571",
  imgSrc:
    "https://www.partner-ads.com/dk/visbanner.php?partnerid=57393&bannerid=34571",
  alt: "Få dit eget barsæt",
};

/** Kuraterede produkt-URL’er: se lib/affiliate-products.ts */
/** Produkt-CTA’er og affiliate:id-links: se lib/affiliate.ts */
