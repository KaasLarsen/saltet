import type { Metadata } from "next";
import Image from "next/image";
import { notFound } from "next/navigation";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { JsonLd } from "@/components/JsonLd";
import { RecipeCard } from "@/components/RecipeCard";
import { RecipeContent } from "@/components/mdx/RecipeContent";
import { Ingredients } from "@/components/mdx/RecipeMDX";
import { Steps } from "@/components/mdx/RecipeMDX";
import { getCategoryName } from "@/lib/categories";
import {
  formatDate,
  formatDuration,
  difficultyLabel,
} from "@/lib/format";
import {
  getAllRecipeParams,
  getRecipe,
  getRelatedRecipes,
} from "@/lib/recipes";
import {
  absoluteUrl,
  buildBreadcrumbJsonLd,
  buildRecipeJsonLd,
  buildRecipeMetadata,
} from "@/lib/seo";

interface RecipePageProps {
  params: Promise<{ category: string; slug: string }>;
}

export async function generateStaticParams() {
  return getAllRecipeParams();
}

export async function generateMetadata({
  params,
}: RecipePageProps): Promise<Metadata> {
  const { category, slug } = await params;
  const recipe = getRecipe(category, slug);
  if (!recipe) return {};
  return buildRecipeMetadata(recipe);
}

export default async function RecipePage({ params }: RecipePageProps) {
  const { category, slug } = await params;
  const recipe = getRecipe(category, slug);
  if (!recipe) notFound();

  const related = getRelatedRecipes(recipe);
  const categoryName = getCategoryName(recipe.category);
  const recipeUrl = absoluteUrl(`/opskrifter/${recipe.category}/${recipe.slug}`);

  const breadcrumbItems = [
    { name: "Forside", url: absoluteUrl("/") },
    { name: "Opskrifter", url: absoluteUrl("/opskrifter") },
    {
      name: categoryName,
      url: absoluteUrl(`/opskrifter/${recipe.category}`),
    },
    { name: recipe.title, url: recipeUrl },
  ];

  return (
    <>
      <JsonLd
        data={[
          buildRecipeJsonLd(recipe),
          buildBreadcrumbJsonLd(breadcrumbItems),
        ]}
      />

      <article>
        <div className="relative aspect-[16/9] w-full max-h-[480px] overflow-hidden bg-charcoal/5 md:aspect-[21/9]">
          <Image
            src={recipe.image}
            alt={recipe.imageAlt}
            fill
            className="object-cover"
            sizes="100vw"
            priority
          />
        </div>

        <div className="mx-auto max-w-6xl px-5 md:px-8">
          <div className="mx-auto max-w-3xl py-10 md:py-14">
            <Breadcrumbs
              items={[
                { label: "Forside", href: "/" },
                { label: "Opskrifter", href: "/opskrifter" },
                {
                  label: categoryName,
                  href: `/opskrifter/${recipe.category}`,
                },
                { label: recipe.title },
              ]}
            />

            <header>
              <h1 className="font-serif text-3xl font-medium leading-tight text-charcoal md:text-4xl md:leading-tight">
                {recipe.title}
              </h1>
              <p className="mt-4 text-lg text-charcoal/70 leading-relaxed">
                {recipe.description}
              </p>

              <dl className="mt-6 flex flex-wrap gap-x-6 gap-y-2 text-sm text-charcoal/55">
                <div className="flex gap-1.5">
                  <dt className="font-medium text-charcoal/70">Forberedelse:</dt>
                  <dd>{formatDuration(recipe.prepTime)}</dd>
                </div>
                <div className="flex gap-1.5">
                  <dt className="font-medium text-charcoal/70">Tilberedning:</dt>
                  <dd>{formatDuration(recipe.cookTime)}</dd>
                </div>
                <div className="flex gap-1.5">
                  <dt className="font-medium text-charcoal/70">Portioner:</dt>
                  <dd>{recipe.servings}</dd>
                </div>
                <div className="flex gap-1.5">
                  <dt className="font-medium text-charcoal/70">Sværhedsgrad:</dt>
                  <dd>{difficultyLabel(recipe.difficulty)}</dd>
                </div>
                <div className="flex gap-1.5">
                  <dt className="font-medium text-charcoal/70">Publiceret:</dt>
                  <dd>{formatDate(recipe.publishedAt)}</dd>
                </div>
              </dl>
            </header>

            <div className="mt-10">
              <RecipeContent source={recipe.content} />
            </div>

            <div className="mt-12 grid gap-12 lg:grid-cols-2">
              <section>
                <h2 className="font-serif text-2xl font-medium text-charcoal mb-5">
                  Ingredienser
                </h2>
                <Ingredients items={recipe.ingredients} />
              </section>

              <section>
                <h2 className="font-serif text-2xl font-medium text-charcoal mb-5">
                  Fremgangsmåde
                </h2>
                <Steps items={recipe.steps} />
              </section>
            </div>

            {recipe.tags.length > 0 && (
              <div className="mt-12 flex flex-wrap gap-2">
                {recipe.tags.map((tag) => (
                  <span
                    key={tag}
                    className="rounded-full bg-charcoal/5 px-3 py-1 text-xs text-charcoal/60"
                  >
                    {tag}
                  </span>
                ))}
              </div>
            )}
          </div>
        </div>

        {related.length > 0 && (
          <section className="border-t border-charcoal/5 bg-white/50 py-14">
            <div className="mx-auto max-w-6xl px-5 md:px-8">
              <h2 className="font-serif text-2xl font-medium text-charcoal mb-8">
                Flere {categoryName.toLowerCase()}-opskrifter
              </h2>
              <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
                {related.map((r) => (
                  <RecipeCard key={r.slug} recipe={r} />
                ))}
              </div>
            </div>
          </section>
        )}
      </article>
    </>
  );
}
