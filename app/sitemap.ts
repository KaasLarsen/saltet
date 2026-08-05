import type { MetadataRoute } from "next";
import { categories } from "@/lib/categories";
import { getAllRecipes } from "@/lib/recipes";
import { absoluteUrl } from "@/lib/seo";

export default function sitemap(): MetadataRoute.Sitemap {
  const recipes = getAllRecipes();
  const now = new Date();

  const staticPages: MetadataRoute.Sitemap = [
    {
      url: absoluteUrl("/"),
      lastModified: now,
      changeFrequency: "weekly",
      priority: 1,
    },
    {
      url: absoluteUrl("/opskrifter"),
      lastModified: now,
      changeFrequency: "weekly",
      priority: 0.9,
    },
    {
      url: absoluteUrl("/om"),
      lastModified: now,
      changeFrequency: "monthly",
      priority: 0.5,
    },
  ];

  const categoryPages: MetadataRoute.Sitemap = categories.map((cat) => ({
    url: absoluteUrl(`/opskrifter/${cat.slug}`),
    lastModified: now,
    changeFrequency: "weekly" as const,
    priority: 0.8,
  }));

  const recipePages: MetadataRoute.Sitemap = recipes.map((recipe) => ({
    url: absoluteUrl(`/opskrifter/${recipe.category}/${recipe.slug}`),
    lastModified: new Date(recipe.publishedAt),
    changeFrequency: "monthly" as const,
    priority: 0.7,
  }));

  return [...staticPages, ...categoryPages, ...recipePages];
}
