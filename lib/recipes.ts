import { execSync } from "child_process";
import fs from "fs";
import path from "path";
import matter from "gray-matter";
import type { Recipe, RecipeFrontmatter } from "./types";

const contentDir = path.join(process.cwd(), "content/recipes");

interface RecipeRecord {
  recipe: Recipe;
  filePath: string;
}

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

function getAllRecipeRecords(): RecipeRecord[] {
  return getRecipeFiles().map((filePath) => ({
    filePath,
    recipe: parseRecipeFile(filePath),
  }));
}

let recipeCommitTimes: Map<string, number> | null = null;

/** Seneste commit-dato per opskriftsfil (nyeste tilføjelse/ændring vinder ved samme publishedAt). */
function getRecipeCommitTimes(): Map<string, number> {
  if (recipeCommitTimes) return recipeCommitTimes;

  const times = new Map<string, number>();

  try {
    const output = execSync(
      'git log --format=COMMIT:%cI --name-only -- content/recipes/',
      {
        encoding: "utf-8",
        cwd: process.cwd(),
        maxBuffer: 10 * 1024 * 1024,
      }
    );

    let currentTime = 0;
    for (const line of output.split("\n")) {
      if (line.startsWith("COMMIT:")) {
        currentTime = new Date(line.slice(7)).getTime();
      } else if (line.endsWith(".mdx")) {
        const filePath = path.join(process.cwd(), line.trim());
        if (!times.has(filePath)) {
          times.set(filePath, currentTime);
        }
      }
    }
  } catch {
    // Git utilgængeligt — falder tilbage til filens mtime nedenfor.
  }

  recipeCommitTimes = times;
  return times;
}

function getRecipeRecencyTime(filePath: string): number {
  const commitTime = getRecipeCommitTimes().get(filePath);
  if (commitTime !== undefined) return commitTime;

  try {
    return fs.statSync(filePath).mtimeMs;
  } catch {
    return 0;
  }
}

function compareRecipesByRecency(a: RecipeRecord, b: RecipeRecord): number {
  const byDate =
    new Date(b.recipe.publishedAt).getTime() -
    new Date(a.recipe.publishedAt).getTime();
  if (byDate !== 0) return byDate;

  return getRecipeRecencyTime(b.filePath) - getRecipeRecencyTime(a.filePath);
}

export function getAllRecipes(): Recipe[] {
  return getAllRecipeRecords()
    .sort(compareRecipesByRecency)
    .map((record) => record.recipe);
}

export function getRecipesByCategory(category: string): Recipe[] {
  return getAllRecipes().filter((r) => r.category === category);
}

/**
 * Seneste opskrifter til forsiden — sorteret efter publishedAt, derefter seneste commit.
 */
export function getFeaturedRecipes(limit = 3, category?: string): Recipe[] {
  const records = category
    ? getAllRecipeRecords().filter((r) => r.recipe.category === category)
    : getAllRecipeRecords();

  return records
    .sort(compareRecipesByRecency)
    .slice(0, limit)
    .map((record) => record.recipe);
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
