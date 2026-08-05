import fs from "fs";
import path from "path";
import matter from "gray-matter";
import type { Recipe, RecipeFrontmatter } from "./types";

const contentDir = path.join(process.cwd(), "content/recipes");

function parseRecipeFile(filePath: string): Recipe {
  const raw = fs.readFileSync(filePath, "utf-8");
  const { data, content } = matter(raw);
  const frontmatter = data as RecipeFrontmatter;

  return {
    ...frontmatter,
    content: content.trim(),
  };
}

function getRecipeFiles(): string[] {
  if (!fs.existsSync(contentDir)) return [];

  const files: string[] = [];

  for (const category of fs.readdirSync(contentDir)) {
    const categoryPath = path.join(contentDir, category);
    if (!fs.statSync(categoryPath).isDirectory()) continue;

    for (const file of fs.readdirSync(categoryPath)) {
      if (file.endsWith(".mdx")) {
        files.push(path.join(categoryPath, file));
      }
    }
  }

  return files;
}

export function getAllRecipes(): Recipe[] {
  return getRecipeFiles()
    .map(parseRecipeFile)
    .sort(
      (a, b) =>
        new Date(b.publishedAt).getTime() - new Date(a.publishedAt).getTime()
    );
}

export function getRecipesByCategory(category: string): Recipe[] {
  return getAllRecipes().filter((r) => r.category === category);
}

export function getFeaturedRecipes(limit = 3): Recipe[] {
  const featured = getAllRecipes().filter((r) => r.featured);
  if (featured.length >= limit) return featured.slice(0, limit);
  return getAllRecipes().slice(0, limit);
}

export function getRecipe(category: string, slug: string): Recipe | undefined {
  return getAllRecipes().find(
    (r) => r.category === category && r.slug === slug
  );
}

export function getRelatedRecipes(recipe: Recipe, limit = 3): Recipe[] {
  return getAllRecipes()
    .filter(
      (r) =>
        r.category === recipe.category &&
        r.slug !== recipe.slug
    )
    .slice(0, limit);
}

export function getAllCategoriesFromRecipes(): string[] {
  const cats = new Set(getAllRecipes().map((r) => r.category));
  return Array.from(cats);
}

export function getAllRecipeParams(): { category: string; slug: string }[] {
  return getAllRecipes().map((r) => ({
    category: r.category,
    slug: r.slug,
  }));
}

export function searchRecipes(query: string): Recipe[] {
  const q = query.trim().toLowerCase();
  if (!q) return getAllRecipes();

  return getAllRecipes().filter((r) => {
    const haystack = [
      r.title,
      r.description,
      r.category,
      ...r.tags,
      ...r.ingredients,
    ]
      .join(" ")
      .toLowerCase();

    return haystack.includes(q);
  });
}
