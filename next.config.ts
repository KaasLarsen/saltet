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
        source: "/tags/mortensaften",
        destination: "/hoejtider/mortensaften",
        permanent: true,
      },
      ...topicRedirects,
    ];
  },
};

export default nextConfig;
