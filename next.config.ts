import type { NextConfig } from "next";

const nextConfig: NextConfig = {
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
    ];
  },
};

export default nextConfig;
