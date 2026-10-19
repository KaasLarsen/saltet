/**
 * Produktbilleder fra Partner-ads feeds (`billedurl`).
 * Matchet manuelt til AFFILIATE_OFFERS via vareurl/produktnavn.
 * Hotlink til forhandler-CDN — kopier ikke lokalt (Partner-ads-anbefaling).
 *
 * PriceRunner-only grej (Lodge, Petromax, Weber, Ninja, Ooni, …) har intet
 * Partner-ads-feed her — dem viser vi uden billede indtil videre.
 */
export const AFFILIATE_FEED_IMAGES: Record<string, string> = {
  // Homeshop — feed 67428/1383
  "homeshop-airfryer":
    "https://cdn.homeshop.dk/357435-large_default/philips-na352-00-dual-basket-airfryer.jpg",
  "meater-plus":
    "https://cdn.homeshop.dk/425489-large_default/meater-plus-tasty-perk-tradlost-stege-termometer-til-iphoneandroid.jpg",
  "meater-pro":
    "https://cdn.homeshop.dk/326259-large_default/meater-2-plus-tradlost-stege-termometer.jpg",
  "homeshop-smash-burger-jern":
    "https://cdn.homeshop.dk/374921-large_default/broil-king-smash-burger-jern.jpg",
  "homeshop-grillspartel-bred":
    "https://cdn.homeshop.dk/46159-large_default/broil-king-imperial-grillspartel-bred---64011.jpg",
  "homeshop-burger-palet":
    "https://cdn.homeshop.dk/387652-large_default/napoleon-plancha-burgerpalet-gatl015.jpg",

  // KitchenOne — feed 79283/1862
  "kitchenone-instant-pot":
    "https://media.enad.io/20dccf88-6cf1-4912-a8a3-40dbcf6e8e0f/ygvdpXfuJEyL-instant-pot-duo-plus-trykkoger-81-112-3079-01-eu-65827-1.jpg?format=jpeg",

  // Boligcenter — feed 106581/3324
  "boligcenter-stegepande":
    "https://cdn.ecdn.dk/boligcenter/img/p/7/6/9/7/7/5/769775.jpg",
  "boligcenter-stoebjernsgryde":
    "https://cdn.ecdn.dk/boligcenter/img/p/6/0/3/2/3/9/3/6032393.jpg",
  "boligcenter-gryder":
    "https://cdn.ecdn.dk/boligcenter/img/p/6/0/3/2/3/9/3/6032393.jpg",
  "boligcenter-saucegryde":
    "https://cdn.ecdn.dk/boligcenter/img/p/1/1/6/3/6/0/0/9/11636009.jpg",

  // Fredstone — feed 109359/3559
  fredstone:
    "https://shop91320.sfstatic.io/upload_dir/shop/20251012_7576_Original-ratio_1920x1440_U_100-2.jpg",
  "fredstone-bagesten":
    "https://shop91320.sfstatic.io/upload_dir/shop/20251012_7571_Original-ratio_1920x1440_U_100-2.jpg",

  // Rito — feed 30371/218
  "rito-sylteglas": "https://assets1.rito.link/194288-rito_product/194288.jpg",

  // DH Wines — feed 108173/3461
  "dh-wines-hvid":
    "https://cdn.shopify.com/s/files/1/0816/5435/0170/files/Simonsig-Chenin-Blanc.jpg?v=1754387339",
  "dh-wines-rood":
    "https://cdn.shopify.com/s/files/1/0816/5435/0170/files/quinta-sebastiao-syrah-tinta-roriz-2021-81693.jpg",
  "dh-wines":
    "https://cdn.shopify.com/s/files/1/0816/5435/0170/files/Simonsig-Chenin-Blanc.jpg?v=1754387339",

  // Økologisk-Supermarked — feed 99972/2863
  "oko-hvedemel":
    "https://www.okologisk-supermarked.dk/images/produkter/1467.jpg",
  "oko-olivenolie":
    "https://www.okologisk-supermarked.dk/images/produkter/10603.jpg",
  "okologisk-supermarked":
    "https://www.okologisk-supermarked.dk/images/produkter/1467.jpg",
};
