import type { MetadataRoute } from "next";
import { getAllCategorySlugs } from "@/lib/categories";
import { getAllHolidaySlugs, getRecipesByHoliday } from "@/lib/holidays";
import { getAllSeasonSlugs, getRecipesBySeason } from "@/lib/seasons";
import { getAllTopicSlugs, getRecipesByTopic } from "@/lib/topics";
import { getAllAnmeldelser } from "@/lib/anmeldelser";
import { getAllGrej } from "@/lib/grej";
import { getAllGuides } from "@/lib/guides";
import { getAllRecipes, getRecipesByCategory } from "@/lib/recipes";
import { getBrowseTags, getRecipesByTagSlug } from "@/lib/tags";
import { absoluteUrl } from "@/lib/seo";

/**
 * Alle offentlige sider skal med i sitemap.
 *
 * - Nye faste sider (fx /kontakt): tilføj i STATIC_ROUTES
 * - Guides: auto fra content/guides/*.mdx
 * - Grej: auto fra content/grej/*.mdx
 * - Anmeldelser: auto fra content/anmeldelser/*.mdx
 * - Kategorier: auto fra lib/categories + content/recipes/*
 * - Højtider: auto fra lib/holidays
 * - Sæsoner: auto fra lib/seasons
 * - Emner: auto fra lib/topics
 * - Tags: auto fra opskrifters tags (kun tags med ≥2 opskrifter; højtids-/sæson-/emne-tags omdirigeres)
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
  { path: "/anmeldelser", changeFrequency: "weekly", priority: 0.88 },
  { path: "/hoejtider", changeFrequency: "weekly", priority: 0.85 },
  { path: "/saeson", changeFrequency: "weekly", priority: 0.85 },
  { path: "/emner", changeFrequency: "weekly", priority: 0.85 },
  { path: "/tags", changeFrequency: "weekly", priority: 0.7 },
  { path: "/om", changeFrequency: "monthly", priority: 0.5 },
  { path: "/kontakt", changeFrequency: "yearly", priority: 0.3 },
  { path: "/vilkaar", changeFrequency: "yearly", priority: 0.3 },
  { path: "/cookies", changeFrequency: "yearly", priority: 0.2 },
  { path: "/privatliv", changeFrequency: "yearly", priority: 0.2 },
];

/** Stabil site-baseline når der ikke er indhold at tage dato fra. */
const SITE_EPOCH = new Date("2026-01-01T00:00:00.000Z");

function latestDate(
  dates: Array<string | Date | undefined | null>
): Date {
  let max = 0;
  for (const value of dates) {
    if (!value) continue;
    const t = value instanceof Date ? value.getTime() : new Date(value).getTime();
    if (Number.isFinite(t) && t > max) max = t;
  }
  return max > 0 ? new Date(max) : SITE_EPOCH;
}

function latestRecipePublishedAt(
  recipes: Array<{ publishedAt: string }>
): Date {
  return latestDate(recipes.map((r) => r.publishedAt));
}

export default function sitemap(): MetadataRoute.Sitemap {
  const recipes = getAllRecipes();
  const guides = getAllGuides();
  const grej = getAllGrej();
  const anmeldelser = getAllAnmeldelser();
  const tags = getBrowseTags().filter((tag) => tag.count >= 2);
  const categorySlugs = getAllCategorySlugs();
  const holidaySlugs = getAllHolidaySlugs();
  const seasonSlugs = getAllSeasonSlugs();
  const topicSlugs = getAllTopicSlugs();

  const contentFreshness = latestDate([
    ...recipes.map((r) => r.publishedAt),
    ...guides.map((g) => g.updatedAt ?? g.publishedAt),
    ...grej.map((g) => g.updatedAt ?? g.publishedAt),
    ...anmeldelser.map((a) => a.updatedAt ?? a.publishedAt),
  ]);

  const staticPages: MetadataRoute.Sitemap = STATIC_ROUTES.map((route) => ({
    url: absoluteUrl(route.path),
    lastModified: contentFreshness,
    changeFrequency: route.changeFrequency,
    priority: route.priority,
  }));

  const categoryPages: MetadataRoute.Sitemap = categorySlugs.map((slug) => ({
    url: absoluteUrl(`/opskrifter/${slug}`),
    lastModified: latestRecipePublishedAt(getRecipesByCategory(slug)),
    changeFrequency: "weekly" as const,
    priority: 0.8,
  }));

  const holidayPages: MetadataRoute.Sitemap = holidaySlugs.map((slug) => ({
    url: absoluteUrl(`/hoejtider/${slug}`),
    lastModified: latestRecipePublishedAt(getRecipesByHoliday(slug)),
    changeFrequency: "weekly" as const,
    priority: 0.8,
  }));

  const seasonPages: MetadataRoute.Sitemap = seasonSlugs.map((slug) => ({
    url: absoluteUrl(`/saeson/${slug}`),
    lastModified: latestRecipePublishedAt(getRecipesBySeason(slug)),
    changeFrequency: "weekly" as const,
    priority: 0.8,
  }));

  const topicPages: MetadataRoute.Sitemap = topicSlugs.map((slug) => ({
    url: absoluteUrl(`/emner/${slug}`),
    lastModified: latestRecipePublishedAt(getRecipesByTopic(slug)),
    changeFrequency: "weekly" as const,
    priority: 0.8,
  }));

  const tagPages: MetadataRoute.Sitemap = tags.map((tag) => ({
    url: absoluteUrl(`/tags/${tag.slug}`),
    lastModified: latestRecipePublishedAt(getRecipesByTagSlug(tag.slug)),
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

  const anmeldelsePages: MetadataRoute.Sitemap = anmeldelser.map((item) => ({
    url: absoluteUrl(`/anmeldelser/${item.slug}`),
    lastModified: new Date(item.updatedAt ?? item.publishedAt),
    changeFrequency: "monthly" as const,
    priority: 0.82,
  }));

  return [
    ...staticPages,
    ...categoryPages,
    ...holidayPages,
    ...seasonPages,
    ...topicPages,
    ...tagPages,
    ...recipePages,
    ...guidePages,
    ...grejPages,
    ...anmeldelsePages,
  ];
}
