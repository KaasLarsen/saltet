import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { JsonLd } from "@/components/JsonLd";
import { RecipeCard } from "@/components/RecipeCard";
import { RecipeFaqSection } from "@/components/RecipeFaq";
import { FailSuccessCompare } from "@/components/fejlfinding/FailSuccessCompare";
import { FejlMatrix } from "@/components/fejlfinding/FejlMatrix";
import {
  getAllFejlfindingSlugs,
  getFejlfinding,
  getRelatedFejlfinding,
  getRelatedFejlfindingGrej,
  getRelatedFejlfindingRecipes,
} from "@/lib/fejlfinding";
import { getFejlfindingGearName } from "@/lib/fejlfinding-nav";
import { formatDate } from "@/lib/format";
import {
  absoluteUrl,
  buildBreadcrumbJsonLd,
  buildFaqJsonLd,
  buildFejlfindingArticleJsonLd,
  buildFejlfindingMetadata,
} from "@/lib/seo";

interface FejlfindingPageProps {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  return getAllFejlfindingSlugs().map((slug) => ({ slug }));
}

export async function generateMetadata({
  params,
}: FejlfindingPageProps): Promise<Metadata> {
  const { slug } = await params;
  const item = getFejlfinding(slug);
  if (!item) return {};
  return buildFejlfindingMetadata(item);
}

export default async function FejlfindingPage({
  params,
}: FejlfindingPageProps) {
  const { slug } = await params;
  const item = getFejlfinding(slug);
  if (!item) notFound();

  const recipes = getRelatedFejlfindingRecipes(item);
  const relatedGrej = getRelatedFejlfindingGrej(item);
  const related = getRelatedFejlfinding(item);
  const gearName = getFejlfindingGearName(item.gear);
  const pageUrl = absoluteUrl(`/fejlfinding/${item.slug}`);

  const breadcrumbItems = [
    { name: "Forside", url: absoluteUrl("/") },
    { name: "Fejlfinding", url: absoluteUrl("/fejlfinding") },
    { name: item.title, url: pageUrl },
  ];

  const faqJsonLd = buildFaqJsonLd(item.faq);
  const jsonLd = [
    buildFejlfindingArticleJsonLd(item),
    buildBreadcrumbJsonLd(breadcrumbItems),
    ...(faqJsonLd ? [faqJsonLd] : []),
  ];

  return (
    <>
      <JsonLd data={jsonLd} />

      <article>
        <div className="mx-auto max-w-5xl px-5 md:px-8">
          <div className="mx-auto max-w-2xl py-10 md:py-14">
            <div className="flex justify-center">
              <Breadcrumbs
                items={[
                  { label: "Forside", href: "/" },
                  { label: "Fejlfinding", href: "/fejlfinding" },
                  { label: item.title },
                ]}
              />
            </div>

            <header className="text-center">
              <p className="mb-4 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-wood px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
                {gearName} · Fejlfinding
              </p>
              <h1 className="font-serif text-4xl uppercase leading-tight tracking-wide text-bone md:text-5xl md:leading-[1.05]">
                {item.title}
              </h1>
              <p className="mx-auto mt-5 max-w-xl text-lg leading-relaxed text-bone/60">
                {item.description}
              </p>
              <p className="mt-4 text-[11px] font-bold uppercase tracking-[0.14em] text-smoke">
                Opdateret {formatDate(item.updatedAt ?? item.publishedAt)}
              </p>
            </header>

            <div className="mt-10">
              <FailSuccessCompare
                successImage={item.image}
                successAlt={item.imageAlt}
                failImage={item.failImage}
                failImageAlt={item.failImageAlt}
                symptom={item.symptom}
              />
            </div>

            <div className="mt-8 rounded-2xl border-2 border-wood/40 bg-wood/10 px-5 py-4 text-center">
              <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-wood">
                Symptomet
              </p>
              <p className="mt-1 font-serif text-2xl uppercase tracking-wide text-bone">
                {item.symptom}
              </p>
            </div>

            {item.content ? (
              <p className="mt-8 text-center leading-relaxed text-bone/55">
                {item.content}
              </p>
            ) : null}

            <div className="mt-10">
              <h2 className="mb-6 text-center font-serif text-2xl uppercase tracking-wide text-bone">
                Fejl-matrix
              </h2>
              <FejlMatrix rows={item.matrices} />
            </div>

            <RecipeFaqSection items={item.faq} />

            {relatedGrej.length > 0 ? (
              <section
                className="mt-14 text-left"
                aria-labelledby="fejlfinding-grej-heading"
              >
                <h2
                  id="fejlfinding-grej-heading"
                  className="mb-4 text-center font-serif text-2xl uppercase tracking-wide text-bone"
                >
                  Grej der hjælper
                </h2>
                <ul className="space-y-3">
                  {relatedGrej.map((grej) => (
                    <li key={grej.slug}>
                      <Link
                        href={`/grej/${grej.slug}`}
                        className="block rounded-2xl border-2 border-bone/15 bg-ash/30 px-4 py-3 transition-colors hover:border-herb"
                      >
                        <span className="font-serif text-lg uppercase tracking-wide text-bone">
                          {grej.title}
                        </span>
                        <span className="mt-1 block text-sm text-bone/55">
                          Læs testen eller købsguiden — så du undgår næste kiks.
                        </span>
                      </Link>
                    </li>
                  ))}
                </ul>
              </section>
            ) : null}

            {recipes.length > 0 ? (
              <section className="mt-14 text-left">
                <h2 className="mb-6 text-center font-serif text-2xl uppercase tracking-wide text-bone">
                  Relaterede opskrifter
                </h2>
                <div className="grid gap-10 sm:grid-cols-2">
                  {recipes.map((recipe) => (
                    <RecipeCard
                      key={`${recipe.category}/${recipe.slug}`}
                      recipe={recipe}
                    />
                  ))}
                </div>
              </section>
            ) : null}
          </div>
        </div>

        {related.length > 0 ? (
          <section className="border-t-2 border-bone/15 bg-ash/40 py-14">
            <div className="mx-auto max-w-5xl px-5 text-center md:px-8">
              <h2 className="mb-8 font-serif text-3xl uppercase tracking-wide text-bone">
                Flere fejlfindinger
              </h2>
              <div className="grid gap-6 text-left sm:grid-cols-2 lg:grid-cols-3">
                {related.map((other) => (
                  <Link
                    key={other.slug}
                    href={`/fejlfinding/${other.slug}`}
                    className="rounded-2xl border-2 border-bone/15 bg-iron/40 p-4 transition-colors hover:border-wood"
                  >
                    <p className="text-[11px] font-bold uppercase tracking-[0.14em] text-wood">
                      {getFejlfindingGearName(other.gear)}
                    </p>
                    <p className="mt-2 font-serif text-lg uppercase tracking-wide text-bone">
                      {other.title}
                    </p>
                    <p className="mt-2 line-clamp-3 text-sm text-bone/50">
                      {other.description}
                    </p>
                  </Link>
                ))}
              </div>
            </div>
          </section>
        ) : null}
      </article>
    </>
  );
}
