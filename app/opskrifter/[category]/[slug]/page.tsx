import type { Metadata } from "next";
import Image from "next/image";
import { notFound } from "next/navigation";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { JsonLd } from "@/components/JsonLd";
import { RecipeCard } from "@/components/RecipeCard";
import { RecipeFaqSection } from "@/components/RecipeFaq";
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
  buildFaqJsonLd,
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

  const faqJsonLd = buildFaqJsonLd(recipe.faq);
  const jsonLd = [
    buildRecipeJsonLd(recipe),
    buildBreadcrumbJsonLd(breadcrumbItems),
    ...(faqJsonLd ? [faqJsonLd] : []),
  ];

  return (
    <>
      <JsonLd data={jsonLd} />

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
          <div className="absolute inset-0 bg-gradient-to-t from-stone via-transparent to-iron/30" />
        </div>

        <div className="mx-auto max-w-5xl px-5 md:px-8">
          <div className="mx-auto max-w-2xl py-10 text-center md:py-14">
            <div className="flex justify-center">
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
            </div>

            <header>
              <h1 className="font-serif text-4xl leading-tight text-bone md:text-5xl md:leading-[1.1]">
                {recipe.title}
              </h1>
              <p className="mx-auto mt-5 max-w-xl text-lg leading-relaxed text-bone/60">
                {recipe.description}
              </p>

              <dl className="mt-8 grid grid-cols-2 gap-4 border-y border-bone/10 py-5 text-sm sm:grid-cols-3 md:grid-cols-5">
                <div>
                  <dt className="text-[11px] uppercase tracking-[0.14em] text-smoke">
                    Forberedelse
                  </dt>
                  <dd className="mt-1 text-bone">{formatDuration(recipe.prepTime)}</dd>
                </div>
                <div>
                  <dt className="text-[11px] uppercase tracking-[0.14em] text-smoke">
                    Tilberedning
                  </dt>
                  <dd className="mt-1 text-bone">{formatDuration(recipe.cookTime)}</dd>
                </div>
                <div>
                  <dt className="text-[11px] uppercase tracking-[0.14em] text-smoke">
                    Portioner
                  </dt>
                  <dd className="mt-1 text-bone">{recipe.servings}</dd>
                </div>
                <div>
                  <dt className="text-[11px] uppercase tracking-[0.14em] text-smoke">
                    Sværhedsgrad
                  </dt>
                  <dd className="mt-1 text-bone">{difficultyLabel(recipe.difficulty)}</dd>
                </div>
                <div>
                  <dt className="text-[11px] uppercase tracking-[0.14em] text-smoke">
                    Publiceret
                  </dt>
                  <dd className="mt-1 text-bone">{formatDate(recipe.publishedAt)}</dd>
                </div>
              </dl>
            </header>

            <div className="mt-10 text-left">
              <RecipeContent source={recipe.content} />
            </div>

            <div className="mt-12 grid gap-12 text-left lg:grid-cols-2">
              <section>
                <h2 className="mb-5 font-serif text-2xl text-bone">
                  Ingredienser
                </h2>
                <Ingredients items={recipe.ingredients} />
              </section>

              <section>
                <h2 className="mb-5 font-serif text-2xl text-bone">
                  Fremgangsmåde
                </h2>
                <Steps items={recipe.steps} />
              </section>
            </div>

            {recipe.tags.length > 0 && (
              <div className="mt-12 flex flex-wrap justify-center gap-2">
                {recipe.tags.map((tag) => (
                  <span
                    key={tag}
                    className="border border-bone/20 px-3 py-1 text-[11px] uppercase tracking-[0.12em] text-bone/50"
                  >
                    {tag}
                  </span>
                ))}
              </div>
            )}

            <RecipeFaqSection items={recipe.faq} />
          </div>
        </div>

        {related.length > 0 && (
          <section className="border-t border-bone/10 bg-ash/30 py-14">
            <div className="mx-auto max-w-5xl px-5 text-center md:px-8">
              <h2 className="mb-8 font-serif text-3xl text-bone">
                Flere {categoryName.toLowerCase()}-opskrifter
              </h2>
              <div className="grid gap-10 text-left sm:grid-cols-2 lg:grid-cols-3">
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
