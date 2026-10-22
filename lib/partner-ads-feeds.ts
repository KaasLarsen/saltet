import { PARTNER_ADS_PARTNER_ID } from "@/lib/partners";

/**
 * Partner-ads produktfeeds (XML med billedurl).
 * Feed-bannerid ≠ tracking-bannerid i partners.ts — begge hører til partner 57393.
 */
export interface PartnerAdsFeed {
  /** Kort navn til logs / scripts */
  id: string;
  bannerId: string;
  feedId: string;
  merchant: string;
}

export const PARTNER_ADS_FEEDS: readonly PartnerAdsFeed[] = [
  {
    id: "homeshop",
    bannerId: "67428",
    feedId: "1383",
    merchant: "Homeshop",
  },
  {
    id: "kitchenone",
    bannerId: "79283",
    feedId: "1862",
    merchant: "KitchenOne",
  },
  {
    id: "boligcenter",
    bannerId: "106581",
    feedId: "3324",
    merchant: "Boligcenter.dk",
  },
  {
    id: "boligcenter-alt",
    bannerId: "112106",
    feedId: "3794",
    merchant: "Boligcenter.dk",
  },
  {
    id: "fredstone",
    bannerId: "109359",
    feedId: "3559",
    merchant: "Fredstone",
  },
  {
    id: "rito",
    bannerId: "30371",
    feedId: "218",
    merchant: "Rito.dk",
  },
  {
    id: "dh-wines",
    bannerId: "108173",
    feedId: "3461",
    merchant: "DH Wines",
  },
  {
    id: "oko-supermarked",
    bannerId: "99972",
    feedId: "2863",
    merchant: "Økologisk-Supermarked",
  },
  {
    id: "helsebixen",
    bannerId: "28715",
    feedId: "181",
    merchant: "Helsebixen.dk",
  },
  {
    id: "med24",
    bannerId: "42807",
    feedId: "522",
    merchant: "Med24",
  },
] as const;

export function partnerAdsFeedUrl(
  feed: Pick<PartnerAdsFeed, "bannerId" | "feedId">,
  partnerId: string = PARTNER_ADS_PARTNER_ID
): string {
  const params = new URLSearchParams({
    partnerid: partnerId,
    bannerid: feed.bannerId,
    feedid: feed.feedId,
  });
  return `https://www.partner-ads.com/dk/feed_udlaes.php?${params.toString()}`;
}
