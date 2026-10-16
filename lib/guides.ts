import fs from "fs";
import path from "path";
import matter from "gray-matter";
import type { Guide, GuideFrontmatter } from "./types";
import { getRecipe } from "./recipes";
import type { Recipe } from "./types";

const contentDir = path.join(process.cwd(), "content/guides");

function parseGuideMeta(filePath: string): Guide {
  const raw = fs.readFileSync(filePath, "utf-8");
  const close = raw.indexOf("\n---", 4);
  const yaml = close === -1 ? raw : raw.slice(0, close + 4);
  const { data } = matter(`${yaml}\n`);
  const frontmatter = data as GuideFrontmatter;

  return {
    ...frontmatter,
    relatedRecipes: frontmatter.relatedRecipes ?? [],
    faq: frontmatter.faq ?? [],
    content: "",
  };
}

function parseGuideFile(filePath: string): Guide {
  const raw = fs.readFileSync(filePath, "utf-8");
  const { data, content } = matter(raw);
  const frontmatter = data as GuideFrontmatter;

  return {
    ...frontmatter,
    relatedRecipes: frontmatter.relatedRecipes ?? [],
    faq: frontmatter.faq ?? [],
    content: content.trim(),
  };
}

let guidesCache: Guide[] | null = null;
let guidesByRecipe: Map<string, Guide[]> | null = null;

export function getAllGuides(): Guide[] {
  if (guidesCache) return guidesCache;
  if (!fs.existsSync(contentDir)) {
    guidesCache = [];
    return guidesCache;
  }

  guidesCache = fs
    .readdirSync(contentDir)
    .filter((file) => file.endsWith(".mdx"))
    .map((file) => parseGuideMeta(path.join(contentDir, file)))
    .sort(
      (a, b) =>
        new Date(b.publishedAt).getTime() - new Date(a.publishedAt).getTime()
    );
  return guidesCache;
}

function recipeGuideIndex(): Map<string, Guide[]> {
  if (guidesByRecipe) return guidesByRecipe;
  guidesByRecipe = new Map();
  for (const guide of getAllGuides()) {
    for (const ref of guide.relatedRecipes) {
      const list = guidesByRecipe.get(ref) ?? [];
      list.push(guide);
      guidesByRecipe.set(ref, list);
    }
  }
  return guidesByRecipe;
}

export function getGuide(slug: string): Guide | undefined {
  const filePath = path.join(contentDir, `${slug}.mdx`);
  if (!fs.existsSync(filePath)) return undefined;
  return parseGuideFile(filePath);
}

export function getAllGuideSlugs(): string[] {
  return getAllGuides().map((g) => g.slug);
}

export function getRelatedGuideRecipes(guide: Guide): Recipe[] {
  return guide.relatedRecipes
    .map((ref) => {
      const [category, slug] = ref.split("/");
      if (!category || !slug) return undefined;
      return getRecipe(category, slug);
    })
    .filter((r): r is Recipe => Boolean(r));
}

export function getGuidesForRecipe(category: string, slug: string): Guide[] {
  return recipeGuideIndex().get(`${category}/${slug}`) ?? [];
}

export function getRelatedGuides(guide: Guide, limit = 4): Guide[] {
  const explicit = (guide.relatedGuides ?? [])
    .map((relatedSlug) => getAllGuides().find((g) => g.slug === relatedSlug))
    .filter((g): g is Guide => Boolean(g));

  if (explicit.length >= limit) return explicit.slice(0, limit);

  const rest = getAllGuides().filter(
    (g) => g.slug !== guide.slug && !explicit.some((e) => e.slug === g.slug)
  );
  return [...explicit, ...rest].slice(0, limit);
}
