import { getTopicNav, recipeMatchesTopic } from "./topic-nav";
import { getAllRecipes } from "./recipes";
import { slugifyTag } from "./slug";
import type { Recipe, Topic } from "./types";

export const topics: Topic[] = [
  {
    slug: "sovs",
    name: "Sovs",
    headline: "Sovsopskrifter",
    description:
      "Bearnaise, brun sovs, aioli, remoulade og dips — saucer og tilbehør på tværs af pande, grill, ovn og airfryer.",
  },
  {
    slug: "kage",
    name: "Kage",
    headline: "Kageopskrifter",
    description:
      "Banankage, scones, muffins og pandekager — bagværk fra airfryer, ovn og pande uden unødig fuss.",
  },
  {
    slug: "dessert",
    name: "Dessert",
    headline: "Dessertopskrifter",
    description:
      "Dessert, is og chokolade — sødt til sidst, uanset om du bager, steger eller køler ned.",
  },
  {
    slug: "pasta",
    name: "Pasta",
    headline: "Pastaopskrifter",
    description:
      "Pasta i alle afskygninger — hurtige hverdagsretter og festmad med sauce, kød eller grønt.",
  },
  {
    slug: "suppe",
    name: "Suppe",
    headline: "Suppeopskrifter",
    description:
      "Varmende supper til efterår og vinter — gryde, trykkoger og det der gør en kedelig dag bedre.",
  },
  {
    slug: "salat",
    name: "Salat",
    headline: "Salatopskrifter",
    description:
      "Salater til frokost og middag — friske, mættende og nemme at skalere op til flere.",
  },
];

export function getTopic(slug: string): Topic | undefined {
  return topics.find((t) => t.slug === slug);
}

export function getAllTopicSlugs(): string[] {
  return topics.map((t) => t.slug);
}

export function recipeMatchesTopicSlug(
  recipe: Pick<Recipe, "tags">,
  topicSlug: string
): boolean {
  const nav = getTopicNav(topicSlug);
  if (!nav) return false;
  return recipeMatchesTopic(recipe.tags, nav, slugifyTag);
}

export function getRecipesByTopic(slug: string): Recipe[] {
  return getAllRecipes().filter((recipe) =>
    recipeMatchesTopicSlug(recipe, slug)
  );
}

export function getTopicCounts(): { topic: Topic; count: number }[] {
  const recipes = getAllRecipes();
  return topics.map((topic) => ({
    topic,
    count: recipes.filter((recipe) =>
      recipeMatchesTopicSlug(recipe, topic.slug)
    ).length,
  }));
}
