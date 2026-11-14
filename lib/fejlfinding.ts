import fs from "fs";
import path from "path";
import matter from "gray-matter";
import type {
  Fejlfinding,
  FejlfindingFrontmatter,
  FejlfindingGear,
  Grej,
  Guide,
  Recipe,
} from "./types";
import { getAllGrej } from "./grej";
import { getAllGuides } from "./guides";
import { getRecipe } from "./recipes";

const contentDir = path.join(process.cwd(), "content/fejlfinding");

function normalize(frontmatter: FejlfindingFrontmatter): FejlfindingFrontmatter {
  return {
    ...frontmatter,
    matrices: frontmatter.matrices ?? [],
    relatedRecipes: frontmatter.relatedRecipes ?? [],
    relatedGuides: frontmatter.relatedGuides ?? [],
    relatedGrej: frontmatter.relatedGrej ?? [],
    faq: frontmatter.faq ?? [],
  };
}

function parseFejlfindingMeta(filePath: string): Fejlfinding {
  const raw = fs.readFileSync(filePath, "utf-8");
  const close = raw.indexOf("\n---", 4);
  const yaml = close === -1 ? raw : raw.slice(0, close + 4);
  const { data } = matter(`${yaml}\n`);
  const frontmatter = normalize(data as FejlfindingFrontmatter);

  return {
    ...frontmatter,
    content: "",
  };
}

function parseFejlfindingFile(filePath: string): Fejlfinding {
  const raw = fs.readFileSync(filePath, "utf-8");
  const { data, content } = matter(raw);
  const frontmatter = normalize(data as FejlfindingFrontmatter);

  return {
    ...frontmatter,
    content: content.trim(),
  };
}

let fejlfindingCache: Fejlfinding[] | null = null;
let fejlfindingByRecipe: Map<string, Fejlfinding[]> | null = null;

export function getAllFejlfinding(): Fejlfinding[] {
  if (fejlfindingCache) return fejlfindingCache;
  if (!fs.existsSync(contentDir)) {
    fejlfindingCache = [];
    return fejlfindingCache;
  }

  fejlfindingCache = fs
    .readdirSync(contentDir)
    .filter((file) => file.endsWith(".mdx"))
    .map((file) => parseFejlfindingMeta(path.join(contentDir, file)))
    .sort(
      (a, b) =>
        new Date(b.publishedAt).getTime() - new Date(a.publishedAt).getTime()
    );
  return fejlfindingCache;
}

function recipeFejlfindingIndex(): Map<string, Fejlfinding[]> {
  if (fejlfindingByRecipe) return fejlfindingByRecipe;
  fejlfindingByRecipe = new Map();
  for (const item of getAllFejlfinding()) {
    for (const ref of item.relatedRecipes) {
      const list = fejlfindingByRecipe.get(ref) ?? [];
      list.push(item);
      fejlfindingByRecipe.set(ref, list);
    }
  }
  return fejlfindingByRecipe;
}

export function getFejlfinding(slug: string): Fejlfinding | undefined {
  const filePath = path.join(contentDir, `${slug}.mdx`);
  if (!fs.existsSync(filePath)) return undefined;
  return parseFejlfindingFile(filePath);
}

export function getAllFejlfindingSlugs(): string[] {
  return getAllFejlfinding().map((item) => item.slug);
}

export function getFejlfindingByGear(gear: FejlfindingGear): Fejlfinding[] {
  return getAllFejlfinding().filter((item) => item.gear === gear);
}

export function getFejlfindingForRecipe(
  category: string,
  slug: string
): Fejlfinding[] {
  return recipeFejlfindingIndex().get(`${category}/${slug}`) ?? [];
}

export function getRelatedFejlfindingRecipes(item: Fejlfinding): Recipe[] {
  return item.relatedRecipes
    .map((ref) => {
      const [category, slug] = ref.split("/");
      if (!category || !slug) return undefined;
      return getRecipe(category, slug);
    })
    .filter((r): r is Recipe => Boolean(r));
}

export function getRelatedFejlfindingGrej(item: Fejlfinding): Grej[] {
  return (item.relatedGrej ?? [])
    .map((slug) => getAllGrej().find((g) => g.slug === slug))
    .filter((g): g is Grej => Boolean(g));
}

/** Eksisterende guides tagged fejlfinding — til hub uden URL-migrering. */
export function getLegacyFejlfindingGuides(): Guide[] {
  return getAllGuides().filter((guide) =>
    guide.tags.some((tag) => tag.toLowerCase() === "fejlfinding")
  );
}

export function getRelatedFejlfinding(
  item: Fejlfinding,
  limit = 3
): Fejlfinding[] {
  const sameGear = getAllFejlfinding().filter(
    (other) => other.slug !== item.slug && other.gear === item.gear
  );
  if (sameGear.length >= limit) return sameGear.slice(0, limit);

  const rest = getAllFejlfinding().filter(
    (other) =>
      other.slug !== item.slug &&
      !sameGear.some((s) => s.slug === other.slug)
  );
  return [...sameGear, ...rest].slice(0, limit);
}
