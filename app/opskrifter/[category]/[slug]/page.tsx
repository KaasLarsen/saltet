import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { JsonLd } from "@/components/JsonLd";
import { RecipeCard } from "@/components/RecipeCard";
import { RecipeFaqSection } from "@/components/RecipeFaq";
import { RecipeTags } from "@/components/RecipeTags";
import { RecipeContent } from "@/components/mdx/RecipeContent";
import { Ingredients } from "@/components/mdx/RecipeMDX";
import { Steps } from "@/components/mdx/RecipeMDX";
import { getCategoryName } from "@/lib/categories";
import {
  formatDate,
  formatDuration,
  difficultyLabel,
} from "@/lib/format";
import { getGuidesForRecipe } from "@/lib/guides";
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
  const mentionedInGuides = getGuidesForRecipe(recipe.category, recipe.slug);
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
          <div className="absolute inset-0 bg-gradient-to-t from-stone via-transparent to-iron/40" />
          <div className="absolute inset-0 bg-[repeating-linear-gradient(-18deg,transparent,transparent_16px,rgba(212,255,0,0.03)_16px,rgba(212,255,0,0.03)_17px)]" />
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
              <h1 className="font-serif text-4xl uppercase leading-tight tracking-wide text-bone md:text-5xl md:leading-[1.05]">
                {recipe.title}
              </h1>
              <p className="mx-auto mt-5 max-w-xl text-lg leading-relaxed text-bone/60">
                {recipe.description}
              </p>

              <dl className="mt-8 grid grid-cols-2 gap-3 rounded-2xl border-2 border-bone/15 bg-ash/40 p-4 text-sm sm:grid-cols-3 md:grid-cols-5">
                <div>
                  <dt className="text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
                    Forberedelse
                  </dt>
                  <dd className="mt-1 font-semibold text-bone">
                    {formatDuration(recipe.prepTime)}
                  </dd>
                </div>
                <div>
                  <dt className="text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
                    Tilberedning
                  </dt>
                  <dd className="mt-1 font-semibold text-bone">
                    {formatDuration(recipe.cookTime)}
                  </dd>
                </div>
                <div>
                  <dt className="text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
                    Portioner
                  </dt>
                  <dd className="mt-1 font-semibold text-bone">
                    {recipe.servings}
                  </dd>
                </div>
                <div>
                  <dt className="text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
                    Sværhedsgrad
                  </dt>
                  <dd className="mt-1 font-semibold text-bone">
                    {difficultyLabel(recipe.difficulty)}
                  </dd>
                </div>
                <div>
                  <dt className="text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
                    Publiceret
                  </dt>
                  <dd className="mt-1 font-semibold text-bone">
                    {formatDate(recipe.publishedAt)}
                  </dd>
                </div>
              </dl>
            </header>

            <div className="mt-10 text-left">
              <RecipeContent source={recipe.content} />
            </div>

            <div className="mt-12 grid gap-12 text-left lg:grid-cols-2">
              <section>
                <h2 className="mb-5 font-serif text-2xl uppercase tracking-wide text-bone">
                  Ingredienser
                </h2>
                <Ingredients items={recipe.ingredients} />
              </section>

              <section>
                <h2 className="mb-5 font-serif text-2xl uppercase tracking-wide text-bone">
                  Fremgangsmåde
                </h2>
                <Steps items={recipe.steps} />
              </section>
            </div>

            <RecipeTags tags={recipe.tags} className="mt-12" />

            <RecipeFaqSection items={recipe.faq} />

            {mentionedInGuides.length > 0 && (
              <section className="mt-14 text-left" aria-labelledby="guides-heading">
                <h2
                  id="guides-heading"
                  className="mb-4 text-center font-serif text-2xl uppercase tracking-wide text-bone"
                >
                  Nævnt i guide
                </h2>
                <ul className="space-y-3">
                  {mentionedInGuides.map((guide) => (
                    <li key={guide.slug}>
                      <Link
                        href={`/guides/${guide.slug}`}
                        className="block rounded-2xl border-2 border-bone/15 bg-ash/30 px-4 py-3 transition-colors hover:border-herb"
                      >
                        <span className="font-serif text-lg uppercase tracking-wide text-bone">
                          {guide.title}
                        </span>
                        <span className="mt-1 block text-sm text-bone/55">
                          {guide.description}
                        </span>
                      </Link>
                    </li>
                  ))}
                </ul>
              </section>
            )}
          </div>
        </div>

        {related.length > 0 && (
          <section className="border-t-2 border-bone/15 bg-ash/40 py-14">
            <div className="mx-auto max-w-5xl px-5 text-center md:px-8">
              <h2 className="mb-8 font-serif text-3xl uppercase tracking-wide text-bone">
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
