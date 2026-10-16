import type { Metadata } from "next";
import { GuideCard } from "@/components/GuideCard";
import { RecipeCard } from "@/components/RecipeCard";
import { SearchForm } from "@/components/SearchForm";
import { SearchResults } from "@/components/SearchResults";
import { grejMatchesQuery } from "@/lib/grej-filters";
import { getAllGrej } from "@/lib/grej";
import { guideMatchesQuery } from "@/lib/guide-filters";
import { getAllGuides } from "@/lib/guides";
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
  const guides = query
    ? getAllGuides()
        .filter((guide) => guideMatchesQuery(guide, query))
        .map((guide) => ({
          title: guide.title,
          slug: guide.slug,
          description: guide.description,
          tags: guide.tags,
          image: guide.image,
          imageAlt: guide.imageAlt,
        }))
    : [];
  const grej = query
    ? getAllGrej()
        .filter((item) => grejMatchesQuery(item, query))
        .map((item) => ({
          title: item.title,
          slug: item.slug,
          description: item.description,
          tags: item.tags,
          track: item.track,
          image: item.image,
          imageAlt: item.imageAlt,
        }))
    : [];

  const recipeLabel =
    recipes.length === 1 ? "1 opskrift" : `${recipes.length} opskrifter`;
  const guideLabel =
    guides.length === 1 ? "1 guide" : `${guides.length} guides`;
  const grejLabel = grej.length === 1 ? "1 grej" : `${grej.length} grej`;

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 text-center md:px-8 md:py-16">
      <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
        {query ? "Søgeresultater" : "Alle opskrifter"}
      </h1>
      <p className="mx-auto mt-4 max-w-xl text-bone/55 leading-relaxed">
        {query
          ? `${recipeLabel}, ${guideLabel} og ${grejLabel} for “${query}”`
          : `${recipes.length} opskrifter — og flere på vej.`}
      </p>

      <div className="mx-auto mt-8 max-w-lg text-left">
        <SearchForm variant="page" initialQuery={query} />
      </div>

      {query &&
      recipes.length === 0 &&
      guides.length === 0 &&
      grej.length === 0 ? (
        <p className="mt-12 text-bone/50">
          Ingen opskrifter, guides eller grej matchede din søgning. Prøv et
          andet ord.
        </p>
      ) : query ? (
        <>
          {recipes.length > 0 ? (
            <SearchResults recipes={recipes} query={query} />
          ) : null}
          {guides.length > 0 ? (
            <section
              className={recipes.length > 0 ? "mt-16" : "mt-10"}
              aria-labelledby="search-guides-heading"
            >
              <h2
                id="search-guides-heading"
                className="font-serif text-2xl uppercase tracking-wide text-bone md:text-3xl"
              >
                Guides
              </h2>
              <div className="mt-10 grid gap-10 text-left sm:grid-cols-2">
                {guides.map((guide) => (
                  <GuideCard key={guide.slug} guide={guide} />
                ))}
              </div>
            </section>
          ) : null}
          {grej.length > 0 ? (
            <section
              className={
                recipes.length > 0 || guides.length > 0 ? "mt-16" : "mt-10"
              }
              aria-labelledby="search-grej-heading"
            >
              <h2
                id="search-grej-heading"
                className="font-serif text-2xl uppercase tracking-wide text-bone md:text-3xl"
              >
                Grej
              </h2>
              <div className="mt-10 grid gap-10 text-left sm:grid-cols-2">
                {grej.map((item) => (
                  <GuideCard
                    key={item.slug}
                    href={`/grej/${item.slug}`}
                    guide={item}
                  />
                ))}
              </div>
            </section>
          ) : null}
        </>
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
