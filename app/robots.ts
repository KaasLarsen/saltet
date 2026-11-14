import type { MetadataRoute } from "next";
import { absoluteUrl } from "@/lib/seo";

/** Bots der typisk scraper image-CDN uden SEO-værdi. */
const IMAGE_SCRAPER_AGENTS = [
  "Bytespider",
  "GPTBot",
  "CCBot",
  "PetalBot",
  "SemrushBot",
  "AhrefsBot",
  "DotBot",
  "MJ12bot",
  "DataForSeoBot",
] as const;

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      {
        userAgent: "*",
        allow: "/",
        disallow: ["/api/"],
      },
      ...IMAGE_SCRAPER_AGENTS.map((userAgent) => ({
        userAgent,
        allow: "/",
        disallow: ["/api/", "/_next/image"],
      })),
    ],
    sitemap: absoluteUrl("/sitemap.xml"),
  };
}
