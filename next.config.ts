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
    ];
  },
};

export default nextConfig;
