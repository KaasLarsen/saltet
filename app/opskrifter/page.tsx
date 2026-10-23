import type { Metadata } from "next";
import { GuideCard } from "@/components/GuideCard";
import { RecipeCard } from "@/components/RecipeCard";
import { SearchForm } from "@/components/SearchForm";
import { SearchMethodFilters } from "@/components/SearchMethodFilters";
import {
  isSearchType,
  SearchTypeFilters,
  type SearchType,
} from "@/components/SearchTypeFilters";
import { anmeldelseMatchesQuery } from "@/lib/anmeldelse-filters";
import { getAllAnmeldelser } from "@/lib/anmeldelser";
import {
  CATEGORY_NAV_ORDER,
} from "@/lib/category-nav";
import { grejMatchesQuery } from "@/lib/grej-filters";
import { getAllGrej } from "@/lib/grej";
import { guideMatchesQuery } from "@/lib/guide-filters";
import { getAllGuides } from "@/lib/guides";
import {
  getAllRecipes,
  searchRecipes,
  SEARCH_RECIPE_LIMIT,
  toRecipeListItem,
} from "@/lib/recipes";
import { absoluteUrl, siteConfig } from "@/lib/seo";
import type { RecipeListItem } from "@/lib/types";

export const metadata: Metadata = {
  title: "Alle opskrifter",
  description: `Gennemse alle opskrifter på ${siteConfig.name}. Airfryer og mere.`,
  alternates: { canonical: absoluteUrl("/opskrifter") },
};

interface AllRecipesPageProps {
  searchParams: Promise<{ q?: string; type?: string; metode?: string }>;
}

function summaryForType(
  type: SearchType | undefined,
  recipeLabel: string,
  guideLabel: string,
  grejLabel: string,
  anmeldelseLabel: string,
  query: string
): string {
  if (type === "opskrifter") return `${recipeLabel} for “${query}”`;
  if (type === "guides") return `${guideLabel} for “${query}”`;
  if (type === "grej") return `${grejLabel} for “${query}”`;
  if (type === "anmeldelser") return `${anmeldelseLabel} for “${query}”`;
  return `${recipeLabel}, ${guideLabel}, ${grejLabel} og ${anmeldelseLabel} for “${query}”`;
}

function methodsInResults(recipes: RecipeListItem[]): string[] {
  const present = new Set(recipes.map((r) => r.category));
  const knownOrder = CATEGORY_NAV_ORDER.filter((slug) => present.has(slug));
  const knownSet = new Set<string>(knownOrder);
  const extras = Array.from(present)
    .filter((slug) => !knownSet.has(slug))
    .sort((a, b) => a.localeCompare(b, "da"));
  return [...knownOrder, ...extras];
}

export default async function AllRecipesPage({
  searchParams,
}: AllRecipesPageProps) {
  const { q, type: typeParam, metode: metodeParam } = await searchParams;
  const query = q?.trim() ?? "";
  const matchedRecipes = (
    query ? searchRecipes(query) : getAllRecipes()
  ).map(toRecipeListItem);

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
  const anmeldelser = query
    ? getAllAnmeldelser()
        .filter((item) => anmeldelseMatchesQuery(item, query))
        .map((item) => ({
          title: item.title,
          slug: item.slug,
          description: item.description,
          series: item.series,
          productName: item.productName,
          tags: item.tags,
          image: item.image,
          imageAlt: item.imageAlt,
          rating: item.rating,
        }))
    : [];

  const availableTypes: SearchType[] = [];
  if (matchedRecipes.length > 0) availableTypes.push("opskrifter");
  if (guides.length > 0) availableTypes.push("guides");
  if (grej.length > 0) availableTypes.push("grej");
  if (anmeldelser.length > 0) availableTypes.push("anmeldelser");

  const activeType: SearchType | undefined =
    isSearchType(typeParam) && availableTypes.includes(typeParam)
      ? typeParam
      : undefined;

  const showRecipes =
    !activeType || activeType === "opskrifter"
      ? matchedRecipes.length > 0
      : false;
  const showGuides =
    !activeType || activeType === "guides" ? guides.length > 0 : false;
  const showGrej =
    !activeType || activeType === "grej" ? grej.length > 0 : false;
  const showAnmeldelser =
    !activeType || activeType === "anmeldelser"
      ? anmeldelser.length > 0
      : false;

  const methods = methodsInResults(matchedRecipes);
  const activeMetode =
    showRecipes && metodeParam && methods.includes(metodeParam)
      ? metodeParam
      : undefined;
  const recipesForMetode = activeMetode
    ? matchedRecipes.filter((r) => r.category === activeMetode)
    : matchedRecipes;
  const recipesTruncated =
    Boolean(query) && recipesForMetode.length > SEARCH_RECIPE_LIMIT;
  const recipes = query
    ? recipesForMetode.slice(0, SEARCH_RECIPE_LIMIT)
    : matchedRecipes;

  const recipeLabel =
    matchedRecipes.length === 1
      ? "1 opskrift"
      : `${matchedRecipes.length} opskrifter`;
  const guideLabel =
    guides.length === 1 ? "1 guide" : `${guides.length} guides`;
  const grejLabel = grej.length === 1 ? "1 grej" : `${grej.length} grej`;
  const anmeldelseLabel =
    anmeldelser.length === 1
      ? "1 anmeldelse"
      : `${anmeldelser.length} anmeldelser`;

  const hasAnyResults =
    matchedRecipes.length > 0 ||
    guides.length > 0 ||
    grej.length > 0 ||
    anmeldelser.length > 0;

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 text-center md:px-8 md:py-16">
      <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
        {query ? "Søgeresultater" : "Alle opskrifter"}
      </h1>
      <p className="mx-auto mt-4 max-w-xl text-bone/55 leading-relaxed">
        {query
          ? summaryForType(
              activeType,
              recipeLabel,
              guideLabel,
              grejLabel,
              anmeldelseLabel,
              query
            )
          : `${matchedRecipes.length} opskrifter — og flere på vej.`}
      </p>

      <div className="mx-auto mt-8 max-w-lg text-left">
        <SearchForm variant="page" initialQuery={query} />
      </div>

      {query && hasAnyResults ? (
        <SearchTypeFilters
          query={query}
          available={availableTypes}
          initialType={activeType}
        />
      ) : null}

      {query && !hasAnyResults ? (
        <p className="mt-12 text-bone/50">
          Ingen opskrifter, guides, grej eller anmeldelser matchede din
          søgning. Prøv et andet ord.
        </p>
      ) : query ? (
        <>
          {showRecipes ? (
            <section aria-labelledby="search-recipes-heading">
              <h2 id="search-recipes-heading" className="sr-only">
                Opskrifter
              </h2>
              <SearchMethodFilters
                query={query}
                methods={methods}
                initialMetode={activeMetode}
              />
              {activeMetode || recipesTruncated ? (
                <p className="mt-8 text-[12px] uppercase tracking-[0.14em] text-bone/40">
                  {activeMetode
                    ? `Viser ${recipes.length} af ${matchedRecipes.length}`
                    : `Viser de første ${SEARCH_RECIPE_LIMIT}`}
                  {recipesTruncated
                    ? " — prøv et mere præcist søgeord."
                    : null}
                </p>
              ) : null}
              <div
                className={`grid gap-10 text-left sm:grid-cols-2 lg:grid-cols-3 ${
                  methods.length > 1
                    ? activeMetode || recipesTruncated
                      ? "mt-8"
                      : "mt-12"
                    : "mt-10"
                }`}
              >
                {recipes.map((recipe) => (
                  <RecipeCard
                    key={`${recipe.category}-${recipe.slug}`}
                    recipe={recipe}
                  />
                ))}
              </div>
            </section>
          ) : null}
          {showGuides ? (
            <section
              className={showRecipes ? "mt-16" : "mt-10"}
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
          {showGrej ? (
            <section
              className={showRecipes || showGuides ? "mt-16" : "mt-10"}
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
          {showAnmeldelser ? (
            <section
              className={
                showRecipes || showGuides || showGrej ? "mt-16" : "mt-10"
              }
              aria-labelledby="search-anmeldelser-heading"
            >
              <h2
                id="search-anmeldelser-heading"
                className="font-serif text-2xl uppercase tracking-wide text-bone md:text-3xl"
              >
                Anmeldelser
              </h2>
              <div className="mt-10 grid gap-10 text-left sm:grid-cols-2">
                {anmeldelser.map((item) => (
                  <GuideCard
                    key={item.slug}
                    href={`/anmeldelser/${item.slug}`}
                    guide={item}
                    productShot
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
