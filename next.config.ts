import type { NextConfig } from "next";
import { TOPIC_NAV } from "./lib/topic-nav";

const topicRedirects = TOPIC_NAV.flatMap((topic) => {
  const slugs = new Set([topic.slug, ...topic.matchTagSlugs]);
  return Array.from(slugs).map((tagSlug) => ({
    source: `/tags/${tagSlug}`,
    destination: `/emner/${topic.slug}`,
    permanent: true,
  }));
});

const nextConfig: NextConfig = {
  staticPageGenerationTimeout: 180,
  images: {
    qualities: [75, 90],
    remotePatterns: [
      { protocol: "https", hostname: "owp.klarna.com" },
      { protocol: "https", hostname: "assets.klarnacdn.net" },
      // Partner-ads feed billedurl CDN’er
      { protocol: "https", hostname: "cdn.homeshop.dk" },
      { protocol: "https", hostname: "media.enad.io" },
      { protocol: "https", hostname: "cdn.ecdn.dk" },
      { protocol: "https", hostname: "shop91320.sfstatic.io" },
      { protocol: "https", hostname: "assets1.rito.link" },
      { protocol: "https", hostname: "cdn.shopify.com" },
      { protocol: "https", hostname: "www.okologisk-supermarked.dk" },
      { protocol: "https", hostname: "cdn.helsebixen.dk" },
      { protocol: "https", hostname: "www.med24.dk" },
    ],
  },
  async redirects() {
    return [
      { source: "/tags/jul", destination: "/hoejtider/jul", permanent: true },
      {
        source: "/tags/nytaar",
        destination: "/hoejtider/nytaar",
        permanent: true,
      },
      {
        source: "/tags/paaske",
        destination: "/hoejtider/paaske",
        permanent: true,
      },
      {
        source: "/tags/halloween",
        destination: "/hoejtider/halloween",
        permanent: true,
      },
      {
        source: "/tags/mortensaften",
        destination: "/hoejtider/mortensaften",
        permanent: true,
      },
      {
        source: "/tags/sommerhoejtider",
        destination: "/hoejtider/sommerhoejtider",
        permanent: true,
      },
      {
        source: "/tags/sankt-hans",
        destination: "/hoejtider/sommerhoejtider",
        permanent: true,
      },
      {
        source: "/tags/pinse",
        destination: "/hoejtider/sommerhoejtider",
        permanent: true,
      },
      ...topicRedirects,
      // Produktanmeldelser flyttet fra /grej til /anmeldelser
      ...[
        "ninja-flexdrawer-af500",
        "ninja-double-stack-xl",
        "cosori-dual-blaze",
        "philips-na352-dual-basket",
        "onyx-airfryer-8l",
        "siemens-iq700-hb776",
        "bosch-series-8-hbg7741",
        "gorenje-pizza-go66",
        "miele-vitroline-h2863",
        "aeg-steamcrisp-bxs6400",
        "sage-fast-slow-pro",
        "tefal-secure-5-neo",
        "instant-pot-duo-crisp",
        "onyx-multicooker-11i1",
        "wmf-perfect-plus",
      ].map((slug) => ({
        source: `/grej/${slug}`,
        destination: `/anmeldelser/${slug}`,
        permanent: true,
      })),
    ];
  },
};

export default nextConfig;
