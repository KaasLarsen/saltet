import fs from "fs";
import path from "path";
import matter from "gray-matter";
import type { Grej, GrejFrontmatter } from "./types";
import { getRecipe } from "./recipes";
import type { Recipe } from "./types";

const contentDir = path.join(process.cwd(), "content/grej");

const CATEGORY_GREJ: Record<string, string[]> = {
  airfryer: [
    "airfryer-vs-ovn-opgoer",
    "airfryer-tilbehoer",
    "airfryer-tilbehoer-test",
    "oliesprayflasker-airfryer",
    "airfryer-rengoering",
    "instant-read-vs-bluetooth-termometer",
    "sukkertermometer",
    "tangsaet-pincet-grilltang",
    "koekkenvaegt-vs-maalebaeger",
    "bagestaal-til-airfryer",
    "tarteletjern-vs-koebte-skaller",
  ],
  stobejern: [
    "stoebjern-rene-skole",
    "plancha-vs-stobejern",
    "stoebejern-vs-carbonstaal",
    "smashburger-grej",
    "stoebejern-boerster-skrabere",
    "stoebjernsgryde-storrelsesguide",
    "smedejern-vs-stobejern-baalpande",
    "belaegning-teflon-keramik-staal",
    "induktion-vs-gas",
    "tangsaet-pincet-grilltang",
    "opvaskeboerste-stoebjern",
    "grillhandske-laeder-silikone-kevlar",
    "knivslibning-for-noerdere",
  ],
  plancha: [
    "plancha-vs-stobejern",
    "stoebejern-vs-carbonstaal",
    "smashburger-grej",
    "stoebjern-rene-skole",
    "gas-plancha-vs-kul-grill",
  ],
  pizzaovn: [
    "hvilken-pizzaovn",
    "bagestaal-vs-bagesten",
    "infrared-termometer-pizza",
    "infrared-termometer-test",
    "pizzaspader",
    "pizzasten-rengoering",
    "gasregulatorer-slanger-sikkerhed",
    "haevekasser-pizzadej",
    "koekkenvaegt-vs-maalebaeger",
    "spiral-vs-planetarisk-roeremaskine",
    "grillhandske-laeder-silikone-kevlar",
  ],
  ovn: [
    "bagestaal-vs-bagesten",
    "koekkenvaegt-vs-maalebaeger",
    "haevekasser-pizzadej",
    "koedsnore-og-koednaale",
    "termometer-til-andesteg",
  ],
  baalmad: [
    "baalgrej-til-baghaven",
    "baaltang-log-lifter",
    "stoebjernsgryde-storrelsesguide",
    "smedejern-vs-stobejern-baalpande",
    "grillhandske-laeder-silikone-kevlar",
    "koeleboks-passiv-vs-kompressor",
  ],
  grill: [
    "traekul-og-briketter-i-indkoebskurven",
    "rotisseri-til-grillen",
    "rygesmuld-flis-og-chunks",
    "tradlost-stegetermometer",
    "instant-read-vs-bluetooth-termometer",
    "termometer-til-andesteg",
    "infrared-termometer-test",
    "gas-plancha-vs-kul-grill",
    "gasregulatorer-slanger-sikkerhed",
    "koldroegningsbakke",
    "grillboerster-sikkerhed",
    "tangsaet-pincet-grilltang",
    "induktion-vs-gas",
    "koedsnore-og-koednaale",
    "taendblokke-opgoer",
    "grillhandske-laeder-silikone-kevlar",
    "koeleboks-passiv-vs-kompressor",
  ],
  "sous-vide": [
    "sous-vide-stave",
    "vakuumpakkere",
    "chiffonflaske-sifon",
    "ismaskine-kompressor-vs-fryseelement",
    "termokande-til-mad",
  ],
  roeremaskine: [
    "koedhakkere",
    "spiral-vs-planetarisk-roeremaskine",
    "poelseroer-vs-poelsestopper",
  ],
  trykkoger: ["trykkoger-vs-slowcooker"],
  dehydrator: ["dehydrator-koebsguide"],
  fermentering: [
    "fermenteringsglas",
    "toerreposer-umi-bags",
    "lage-sproejte-vs-toersaltning",
    "poelseroer-vs-poelsestopper",
  ],
  palaeg: [
    "palaegsmaskine-pro-vs-billig",
    "rullepoelsepresser-trae-vs-staal",
    "poelseroer-vs-poelsestopper",
    "toerreposer-umi-bags",
    "lage-sproejte-vs-toersaltning",
    "laksekniv-fleksibel",
    "elektrisk-palaegskniv",
    "sildekrukker-patentglas",
    "tarteletjern-vs-koebte-skaller",
  ],
  roeg: [
    "rygesmuld-flis-og-chunks",
    "koldroegningsbakke",
    "lage-sproejte-vs-toersaltning",
    "roegpistol-smoking-gun",
    "laksekniv-fleksibel",
  ],
  dips: [
    "stavblender",
    "chiffonflaske-sifon",
    "espresso-vs-moccamaster",
    "maelkeskummer-mikroskum",
    "termokande-til-mad",
    "roegpistol-smoking-gun",
  ],
  pande: [
    "belaegning-teflon-keramik-staal",
    "kobbergryder",
    "peberkvaern-keramik-vs-plastik",
    "microplane-vs-kasserivejern",
    "koekkensakse-fjerkrae-saks",
    "induktion-vs-gas",
    "tangsaet-pincet-grilltang",
    "multihakker-loegsnitter",
    "knivmagnet-vs-knivblok",
    "opvaskeboerste-stoebjern",
  ],
  gryde: [
    "kobbergryder",
    "stoebjernsgryde-storrelsesguide",
    "koekkensakse-fjerkrae-saks",
    "multihakker-loegsnitter",
  ],
};

function parseGrejMeta(filePath: string): Grej {
  const raw = fs.readFileSync(filePath, "utf-8");
  const close = raw.indexOf("\n---", 4);
  const yaml = close === -1 ? raw : raw.slice(0, close + 4);
  const { data } = matter(`${yaml}\n`);
  const frontmatter = data as GrejFrontmatter;

  return {
    ...frontmatter,
    relatedRecipes: frontmatter.relatedRecipes ?? [],
    relatedGuides: frontmatter.relatedGuides ?? [],
    relatedGrej: frontmatter.relatedGrej ?? [],
    widgets: frontmatter.widgets ?? [],
    faq: frontmatter.faq ?? [],
    content: "",
  };
}

function parseGrejFile(filePath: string): Grej {
  const raw = fs.readFileSync(filePath, "utf-8");
  const { data, content } = matter(raw);
  const frontmatter = data as GrejFrontmatter;

  return {
    ...frontmatter,
    relatedRecipes: frontmatter.relatedRecipes ?? [],
    relatedGuides: frontmatter.relatedGuides ?? [],
    relatedGrej: frontmatter.relatedGrej ?? [],
    widgets: frontmatter.widgets ?? [],
    faq: frontmatter.faq ?? [],
    content: content.trim(),
  };
}

let grejCache: Grej[] | null = null;
let grejByRecipe: Map<string, Grej[]> | null = null;

export function getAllGrej(): Grej[] {
  if (grejCache) return grejCache;
  if (!fs.existsSync(contentDir)) {
    grejCache = [];
    return grejCache;
  }

  grejCache = fs
    .readdirSync(contentDir)
    .filter((file) => file.endsWith(".mdx"))
    .map((file) => parseGrejMeta(path.join(contentDir, file)))
    .sort(
      (a, b) =>
        new Date(b.publishedAt).getTime() - new Date(a.publishedAt).getTime()
    );
  return grejCache;
}

function recipeGrejIndex(): Map<string, Grej[]> {
  if (grejByRecipe) return grejByRecipe;
  grejByRecipe = new Map();
  for (const item of getAllGrej()) {
    for (const ref of item.relatedRecipes) {
      const list = grejByRecipe.get(ref) ?? [];
      list.push(item);
      grejByRecipe.set(ref, list);
    }
  }
  return grejByRecipe;
}

export function getGrej(slug: string): Grej | undefined {
  const filePath = path.join(contentDir, `${slug}.mdx`);
  if (!fs.existsSync(filePath)) return undefined;
  return parseGrejFile(filePath);
}

export function getAllGrejSlugs(): string[] {
  return getAllGrej().map((g) => g.slug);
}

export function getRelatedGrejRecipes(item: Grej): Recipe[] {
  return item.relatedRecipes
    .map((ref) => {
      const [category, slug] = ref.split("/");
      if (!category || !slug) return undefined;
      return getRecipe(category, slug);
    })
    .filter((r): r is Recipe => Boolean(r));
}

export function getRelatedGrej(item: Grej, limit = 4): Grej[] {
  const explicit = (item.relatedGrej ?? [])
    .map((relatedSlug) => getAllGrej().find((g) => g.slug === relatedSlug))
    .filter((g): g is Grej => Boolean(g));

  if (explicit.length >= limit) return explicit.slice(0, limit);

  const rest = getAllGrej().filter(
    (g) => g.slug !== item.slug && !explicit.some((e) => e.slug === g.slug)
  );
  return [...explicit, ...rest].slice(0, limit);
}

function uniqueGrej(items: Grej[]): Grej[] {
  const seen = new Set<string>();
  const out: Grej[] = [];
  for (const item of items) {
    if (seen.has(item.slug)) continue;
    seen.add(item.slug);
    out.push(item);
  }
  return out;
}

export function getGrejForRecipe(
  category: string,
  slug: string,
  relatedGrej?: string[]
): Grej[] {
  const explicit = (relatedGrej ?? [])
    .map((grejSlug) => getAllGrej().find((g) => g.slug === grejSlug))
    .filter((g): g is Grej => Boolean(g));

  const fromFrontmatter = recipeGrejIndex().get(`${category}/${slug}`) ?? [];
  const fromCategory = (CATEGORY_GREJ[category] ?? [])
    .map((grejSlug) => getAllGrej().find((g) => g.slug === grejSlug))
    .filter((g): g is Grej => Boolean(g));

  return uniqueGrej([...explicit, ...fromFrontmatter, ...fromCategory]).slice(
    0,
    3
  );
}
