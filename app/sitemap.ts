import type { MetadataRoute } from "next";
import { getAllCategorySlugs } from "@/lib/categories";
import { getAllHolidaySlugs } from "@/lib/holidays";
import { getAllTopicSlugs } from "@/lib/topics";
import { getAllGrej } from "@/lib/grej";
import { getAllGuides } from "@/lib/guides";
import { getAllRecipes } from "@/lib/recipes";
import { getBrowseTags } from "@/lib/tags";
import { absoluteUrl } from "@/lib/seo";

/**
 * Alle offentlige sider skal med i sitemap.
 *
 * - Nye faste sider (fx /kontakt): tilføj i STATIC_ROUTES
 * - Guides: auto fra content/guides/*.mdx
 * - Grej: auto fra content/grej/*.mdx
 * - Kategorier: auto fra lib/categories + content/recipes/*
 * - Højtider: auto fra lib/holidays
 * - Emner: auto fra lib/topics
 * - Tags: auto fra opskrifters tags (højtids- og emne-tags omdirigeres)
 * - Opskrifter: auto fra content/recipes/**\/*.mdx
 */
const STATIC_ROUTES: {
  path: string;
  changeFrequency: MetadataRoute.Sitemap[number]["changeFrequency"];
  priority: number;
}[] = [
  { path: "/", changeFrequency: "weekly", priority: 1 },
  { path: "/opskrifter", changeFrequency: "weekly", priority: 0.9 },
  { path: "/guides", changeFrequency: "weekly", priority: 0.88 },
  { path: "/grej", changeFrequency: "weekly", priority: 0.88 },
  { path: "/hoejtider", changeFrequency: "weekly", priority: 0.85 },
  { path: "/emner", changeFrequency: "weekly", priority: 0.85 },
  { path: "/tags", changeFrequency: "weekly", priority: 0.7 },
  { path: "/om", changeFrequency: "monthly", priority: 0.5 },
  { path: "/kontakt", changeFrequency: "yearly", priority: 0.3 },
  { path: "/cookies", changeFrequency: "yearly", priority: 0.2 },
  { path: "/privatliv", changeFrequency: "yearly", priority: 0.2 },
];

export default function sitemap(): MetadataRoute.Sitemap {
  const recipes = getAllRecipes();
  const guides = getAllGuides();
  const grej = getAllGrej();
  const tags = getBrowseTags();
  const categorySlugs = getAllCategorySlugs();
  const holidaySlugs = getAllHolidaySlugs();
  const topicSlugs = getAllTopicSlugs();
  const now = new Date();

  const staticPages: MetadataRoute.Sitemap = STATIC_ROUTES.map((route) => ({
    url: absoluteUrl(route.path),
    lastModified: now,
    changeFrequency: route.changeFrequency,
    priority: route.priority,
  }));

  const categoryPages: MetadataRoute.Sitemap = categorySlugs.map((slug) => ({
    url: absoluteUrl(`/opskrifter/${slug}`),
    lastModified: now,
    changeFrequency: "weekly" as const,
    priority: 0.8,
  }));

  const holidayPages: MetadataRoute.Sitemap = holidaySlugs.map((slug) => ({
    url: absoluteUrl(`/hoejtider/${slug}`),
    lastModified: now,
    changeFrequency: "weekly" as const,
    priority: 0.8,
  }));

  const topicPages: MetadataRoute.Sitemap = topicSlugs.map((slug) => ({
    url: absoluteUrl(`/emner/${slug}`),
    lastModified: now,
    changeFrequency: "weekly" as const,
    priority: 0.8,
  }));

  const tagPages: MetadataRoute.Sitemap = tags.map((tag) => ({
    url: absoluteUrl(`/tags/${tag.slug}`),
    lastModified: now,
    changeFrequency: "weekly" as const,
    priority: 0.65,
  }));

  const recipePages: MetadataRoute.Sitemap = recipes.map((recipe) => ({
    url: absoluteUrl(`/opskrifter/${recipe.category}/${recipe.slug}`),
    lastModified: new Date(recipe.publishedAt),
    changeFrequency: "monthly" as const,
    priority: 0.7,
  }));

  const guidePages: MetadataRoute.Sitemap = guides.map((guide) => ({
    url: absoluteUrl(`/guides/${guide.slug}`),
    lastModified: new Date(guide.updatedAt ?? guide.publishedAt),
    changeFrequency: "monthly" as const,
    priority: 0.8,
  }));

  const grejPages: MetadataRoute.Sitemap = grej.map((item) => ({
    url: absoluteUrl(`/grej/${item.slug}`),
    lastModified: new Date(item.updatedAt ?? item.publishedAt),
    changeFrequency: "monthly" as const,
    priority: 0.8,
  }));

  return [
    ...staticPages,
    ...categoryPages,
    ...holidayPages,
    ...topicPages,
    ...tagPages,
    ...recipePages,
    ...guidePages,
    ...grejPages,
  ];
}
