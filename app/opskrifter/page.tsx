import type { Metadata } from "next";
import { RecipeCard } from "@/components/RecipeCard";
import { SearchForm } from "@/components/SearchForm";
import { SearchResults } from "@/components/SearchResults";
import { getAllRecipes, searchRecipes } from "@/lib/recipes";
import { absoluteUrl, siteConfig } from "@/lib/seo";
import type { Recipe, RecipeFrontmatter } from "@/lib/types";

export const metadata: Metadata = {
  title: "Alle opskrifter",
  description: `Gennemse alle opskrifter på ${siteConfig.name}. Airfryer og mere.`,
  alternates: { canonical: absoluteUrl("/opskrifter") },
};

interface AllRecipesPageProps {
  searchParams: Promise<{ q?: string }>;
}

function toListItem(recipe: Recipe): RecipeFrontmatter {
  const { content: _content, ...rest } = recipe;
  return rest;
}

export default async function AllRecipesPage({
  searchParams,
}: AllRecipesPageProps) {
  const { q } = await searchParams;
  const query = q?.trim() ?? "";
  const recipes = (query ? searchRecipes(query) : getAllRecipes()).map(
    toListItem
  );

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 text-center md:px-8 md:py-16">
      <h1 className="font-serif text-4xl text-bone md:text-5xl">
        {query ? "Søgeresultater" : "Alle opskrifter"}
      </h1>
      <p className="mx-auto mt-4 max-w-xl text-bone/55 leading-relaxed">
        {query
          ? `${recipes.length} resultat${recipes.length === 1 ? "" : "er"} for “${query}”`
          : `${recipes.length} opskrifter — og flere på vej.`}
      </p>

      <div className="mx-auto mt-8 max-w-lg text-left">
        <SearchForm variant="page" initialQuery={query} />
      </div>

      {recipes.length === 0 ? (
        <p className="mt-12 text-bone/50">
          Ingen opskrifter matchede din søgning. Prøv et andet ord.
        </p>
      ) : query ? (
        <SearchResults recipes={recipes} query={query} />
      ) : (
        <div className="mt-12 grid gap-10 text-left sm:grid-cols-2 lg:grid-cols-3">
          {recipes.map((recipe) => (
            <RecipeCard
              key={`${recipe.category}-${recipe.slug}`}
              recipe={recipe}
            />
          ))}
        </div>
      )}
    </div>
  );
}
