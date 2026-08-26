export interface PartnerBannerConfig {
  href: string;
  imgSrc: string;
  alt: string;
}

export const partnerBanners: PartnerBannerConfig[] = [
  {
    href: "https://www.partner-ads.com/dk/klikbanner.php?partnerid=57393&bannerid=116078",
    imgSrc:
      "https://www.partner-ads.com/dk/visbanner.php?partnerid=57393&bannerid=116078",
    alt: "Oater 2.0 — frisk havremælk på få minutter",
  },
];

export function getActivePartnerBanner(
  date = new Date()
): PartnerBannerConfig | undefined {
  if (partnerBanners.length === 0) return undefined;
  const start = Date.UTC(date.getUTCFullYear(), 0, 1);
  const week = Math.floor(
    (date.getTime() - start) / (7 * 24 * 60 * 60 * 1000)
  );
  return partnerBanners[week % partnerBanners.length];
}
