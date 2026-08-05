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
        <div className="relative aspect-[16/10] w-full overflow-hidden bg-iron md:aspect-[21/9] md:max-h-[520px]">
          <Image
            src={recipe.image}
            alt={recipe.imageAlt}
            fill
            className="object-cover"
            sizes="100vw"
            priority
          />
          <div className="absolute inset-0 bg-gradient-to-t from-ink/40 to-transparent" />
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
              <h1 className="font-serif text-4xl leading-tight text-ink md:text-5xl md:leading-[1.1]">
                {recipe.title}
              </h1>
              <p className="mt-5 text-lg leading-relaxed text-ink/65">
                {recipe.description}
              </p>

              <dl className="mt-8 grid grid-cols-2 gap-4 border-y border-ink/15 py-5 text-sm sm:grid-cols-3 md:grid-cols-5">
                <div>
                  <dt className="text-[11px] uppercase tracking-[0.14em] text-smoke">
                    Forberedelse
                  </dt>
                  <dd className="mt-1 text-ink">{formatDuration(recipe.prepTime)}</dd>
                </div>
                <div>
                  <dt className="text-[11px] uppercase tracking-[0.14em] text-smoke">
                    Tilberedning
                  </dt>
                  <dd className="mt-1 text-ink">{formatDuration(recipe.cookTime)}</dd>
                </div>
                <div>
                  <dt className="text-[11px] uppercase tracking-[0.14em] text-smoke">
                    Portioner
                  </dt>
                  <dd className="mt-1 text-ink">{recipe.servings}</dd>
                </div>
                <div>
                  <dt className="text-[11px] uppercase tracking-[0.14em] text-smoke">
                    Sværhedsgrad
                  </dt>
                  <dd className="mt-1 text-ink">{difficultyLabel(recipe.difficulty)}</dd>
                </div>
                <div>
                  <dt className="text-[11px] uppercase tracking-[0.14em] text-smoke">
                    Publiceret
                  </dt>
                  <dd className="mt-1 text-ink">{formatDate(recipe.publishedAt)}</dd>
                </div>
              </dl>
            </header>

            <div className="mt-10">
              <RecipeContent source={recipe.content} />
            </div>

            <div className="mt-12 grid gap-12 lg:grid-cols-2">
              <section>
                <h2 className="mb-5 font-serif text-2xl text-ink">
                  Ingredienser
                </h2>
                <Ingredients items={recipe.ingredients} />
              </section>

              <section>
                <h2 className="mb-5 font-serif text-2xl text-ink">
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
                    className="border border-ink/20 px-3 py-1 text-[11px] uppercase tracking-[0.12em] text-ink/55"
                  >
                    {tag}
                  </span>
                ))}
              </div>
            )}
          </div>
        </div>

        {related.length > 0 && (
          <section className="border-t border-ink/15 bg-paper/50 py-14">
            <div className="mx-auto max-w-6xl px-5 md:px-8">
              <h2 className="mb-8 font-serif text-3xl text-ink">
                Flere {categoryName.toLowerCase()}-opskrifter
              </h2>
              <div className="grid gap-10 sm:grid-cols-2 lg:grid-cols-3">
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
