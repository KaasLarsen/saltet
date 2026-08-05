import type { Metadata } from "next";
import { RecipeCard } from "@/components/RecipeCard";
import { getAllRecipes } from "@/lib/recipes";
import { absoluteUrl, siteConfig } from "@/lib/seo";

export const metadata: Metadata = {
  title: "Alle opskrifter",
  description: `Gennemse alle opskrifter på ${siteConfig.name}. Airfryer og mere.`,
  alternates: { canonical: absoluteUrl("/opskrifter") },
};

export default function AllRecipesPage() {
  const recipes = getAllRecipes();

  return (
    <div className="mx-auto max-w-6xl px-5 py-12 md:px-8 md:py-16">
      <h1 className="font-serif text-4xl text-ink md:text-5xl">
        Alle opskrifter
      </h1>
      <p className="mt-4 max-w-xl text-ink/60 leading-relaxed">
        {recipes.length} opskrifter — og flere på vej.
      </p>
      <div className="mt-12 grid gap-10 sm:grid-cols-2 lg:grid-cols-3">
        {recipes.map((recipe) => (
          <RecipeCard
            key={`${recipe.category}-${recipe.slug}`}
            recipe={recipe}
          />
        ))}
      </div>
    </div>
  );
}
