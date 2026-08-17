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
    ];
  },
};

export default nextConfig;
