import fs from "fs";
import path from "path";
import matter from "gray-matter";
import type { Anmeldelse, AnmeldelseFrontmatter } from "./types";
import { getRecipe } from "./recipes";
import type { Recipe } from "./types";

const contentDir = path.join(process.cwd(), "content/anmeldelser");

function parseAnmeldelseMeta(filePath: string): Anmeldelse {
  const raw = fs.readFileSync(filePath, "utf-8");
  const close = raw.indexOf("\n---", 4);
  const yaml = close === -1 ? raw : raw.slice(0, close + 4);
  const { data } = matter(`${yaml}\n`);
  const frontmatter = data as AnmeldelseFrontmatter;

  return {
    ...frontmatter,
    relatedRecipes: frontmatter.relatedRecipes ?? [],
    relatedGuides: frontmatter.relatedGuides ?? [],
    relatedGrej: frontmatter.relatedGrej ?? [],
    relatedAnmeldelser: frontmatter.relatedAnmeldelser ?? [],
    widgets: frontmatter.widgets ?? [],
    affiliateOffers: frontmatter.affiliateOffers ?? [],
    faq: frontmatter.faq ?? [],
    content: "",
  };
}

function parseAnmeldelseFile(filePath: string): Anmeldelse {
  const raw = fs.readFileSync(filePath, "utf-8");
  const { data, content } = matter(raw);
  const frontmatter = data as AnmeldelseFrontmatter;

  return {
    ...frontmatter,
    relatedRecipes: frontmatter.relatedRecipes ?? [],
    relatedGuides: frontmatter.relatedGuides ?? [],
    relatedGrej: frontmatter.relatedGrej ?? [],
    relatedAnmeldelser: frontmatter.relatedAnmeldelser ?? [],
    widgets: frontmatter.widgets ?? [],
    affiliateOffers: frontmatter.affiliateOffers ?? [],
    faq: frontmatter.faq ?? [],
    content: content.trim(),
  };
}

let anmeldelseCache: Anmeldelse[] | null = null;

export function getAllAnmeldelser(): Anmeldelse[] {
  if (anmeldelseCache) return anmeldelseCache;
  if (!fs.existsSync(contentDir)) {
    anmeldelseCache = [];
    return anmeldelseCache;
  }

  anmeldelseCache = fs
    .readdirSync(contentDir)
    .filter((file) => file.endsWith(".mdx"))
    .map((file) => parseAnmeldelseMeta(path.join(contentDir, file)))
    .sort(
      (a, b) =>
        new Date(b.publishedAt).getTime() - new Date(a.publishedAt).getTime()
    );
  return anmeldelseCache;
}

export function getAnmeldelse(slug: string): Anmeldelse | undefined {
  const filePath = path.join(contentDir, `${slug}.mdx`);
  if (!fs.existsSync(filePath)) return undefined;
  return parseAnmeldelseFile(filePath);
}

export function getAllAnmeldelseSlugs(): string[] {
  return getAllAnmeldelser().map((item) => item.slug);
}

export function getRelatedAnmeldelseRecipes(item: Anmeldelse): Recipe[] {
  return item.relatedRecipes
    .map((ref) => {
      const [category, slug] = ref.split("/");
      if (!category || !slug) return undefined;
      return getRecipe(category, slug);
    })
    .filter((r): r is Recipe => Boolean(r));
}

export function getRelatedAnmeldelser(
  item: Anmeldelse,
  limit = 4
): Anmeldelse[] {
  const explicit = (item.relatedAnmeldelser ?? [])
    .map((relatedSlug) =>
      getAllAnmeldelser().find((a) => a.slug === relatedSlug)
    )
    .filter((a): a is Anmeldelse => Boolean(a));

  if (explicit.length >= limit) return explicit.slice(0, limit);

  const sameSeries = getAllAnmeldelser().filter(
    (a) =>
      a.slug !== item.slug &&
      a.series === item.series &&
      !explicit.some((e) => e.slug === a.slug)
  );

  const rest = getAllAnmeldelser().filter(
    (a) =>
      a.slug !== item.slug &&
      !explicit.some((e) => e.slug === a.slug) &&
      !sameSeries.some((e) => e.slug === a.slug)
  );

  return [...explicit, ...sameSeries, ...rest].slice(0, limit);
}
