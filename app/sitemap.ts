import type { MetadataRoute } from "next";
import { getAllCategorySlugs } from "@/lib/categories";
import { getAllRecipes } from "@/lib/recipes";
import { getAllTags } from "@/lib/tags";
import { absoluteUrl } from "@/lib/seo";

/**
 * Alle offentlige sider skal med i sitemap.
 *
 * - Nye faste sider (fx /kontakt): tilføj i STATIC_ROUTES
 * - Kategorier: auto fra lib/categories + content/recipes/*
 * - Tags: auto fra opskrifters tags
 * - Opskrifter: auto fra content/recipes/**\/*.mdx
 */
const STATIC_ROUTES: {
  path: string;
  changeFrequency: MetadataRoute.Sitemap[number]["changeFrequency"];
  priority: number;
}[] = [
  { path: "/", changeFrequency: "weekly", priority: 1 },
  { path: "/opskrifter", changeFrequency: "weekly", priority: 0.9 },
  { path: "/tags", changeFrequency: "weekly", priority: 0.7 },
  { path: "/om", changeFrequency: "monthly", priority: 0.5 },
];

export default function sitemap(): MetadataRoute.Sitemap {
  const recipes = getAllRecipes();
  const tags = getAllTags();
  const categorySlugs = getAllCategorySlugs();
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

  return [...staticPages, ...categoryPages, ...tagPages, ...recipePages];
}
