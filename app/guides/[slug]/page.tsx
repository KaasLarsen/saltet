import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { JsonLd } from "@/components/JsonLd";
import { RecipeCard } from "@/components/RecipeCard";
import { RecipeFaqSection } from "@/components/RecipeFaq";
import { RecipeContent } from "@/components/mdx/RecipeContent";
import {
  getAllGuideSlugs,
  getGuide,
  getRelatedGuideRecipes,
  getRelatedGuides,
} from "@/lib/guides";
import { formatDate } from "@/lib/format";
import {
  absoluteUrl,
  buildArticleJsonLd,
  buildBreadcrumbJsonLd,
  buildFaqJsonLd,
  buildGuideMetadata,
} from "@/lib/seo";
import { slugifyTag } from "@/lib/slug";

interface GuidePageProps {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  return getAllGuideSlugs().map((slug) => ({ slug }));
}

export async function generateMetadata({
  params,
}: GuidePageProps): Promise<Metadata> {
  const { slug } = await params;
  const guide = getGuide(slug);
  if (!guide) return {};
  return buildGuideMetadata(guide);
}

export default async function GuidePage({ params }: GuidePageProps) {
  const { slug } = await params;
  const guide = getGuide(slug);
  if (!guide) notFound();

  const recipes = getRelatedGuideRecipes(guide);
  const relatedGuides = getRelatedGuides(guide);
  const guideUrl = absoluteUrl(`/guides/${guide.slug}`);

  const headingMatches = [...guide.content.matchAll(/^## (.+)$/gm)];
  const toc = headingMatches.map((match) => ({
    id: slugifyTag(match[1]),
    label: match[1],
  }));

  const breadcrumbItems = [
    { name: "Forside", url: absoluteUrl("/") },
    { name: "Guides", url: absoluteUrl("/guides") },
    { name: guide.title, url: guideUrl },
  ];

  const faqJsonLd = buildFaqJsonLd(guide.faq);
  const jsonLd = [
    buildArticleJsonLd(guide),
    buildBreadcrumbJsonLd(breadcrumbItems),
    ...(faqJsonLd ? [faqJsonLd] : []),
  ];

  return (
    <>
      <JsonLd data={jsonLd} />

      <article>
        <div className="relative aspect-[16/10] w-full overflow-hidden bg-iron md:aspect-[21/9] md:max-h-[520px]">
          <Image
            src={guide.image}
            alt={guide.imageAlt}
            fill
            className="object-cover"
            sizes="100vw"
            priority
          />
          <div className="absolute inset-0 bg-gradient-to-t from-stone via-transparent to-iron/40" />
        </div>

        <div className="mx-auto max-w-5xl px-5 md:px-8">
          <div className="mx-auto max-w-2xl py-10 md:py-14">
            <div className="flex justify-center">
              <Breadcrumbs
                items={[
                  { label: "Forside", href: "/" },
                  { label: "Guides", href: "/guides" },
                  { label: guide.title },
                ]}
              />
            </div>

            <header className="text-center">
              <h1 className="font-serif text-4xl uppercase leading-tight tracking-wide text-bone md:text-5xl md:leading-[1.05]">
                {guide.title}
              </h1>
              <p className="mx-auto mt-5 max-w-xl text-lg leading-relaxed text-bone/60">
                {guide.description}
              </p>
              <p className="mt-4 text-[11px] font-bold uppercase tracking-[0.14em] text-smoke">
                Opdateret {formatDate(guide.updatedAt ?? guide.publishedAt)}
              </p>
            </header>

            {toc.length > 0 && (
              <nav
                aria-label="Indhold"
                className="mt-10 rounded-2xl border-2 border-bone/15 bg-ash/40 p-5 text-left"
              >
                <p className="mb-3 text-[11px] font-bold uppercase tracking-[0.16em] text-herb">
                  På denne side
                </p>
                <ol className="space-y-2">
                  {toc.map((item, index) => (
                    <li key={item.id}>
                      <a
                        href={`#${item.id}`}
                        className="text-sm text-bone/70 underline-offset-2 hover:text-herb hover:underline"
                      >
                        {index + 1}. {item.label}
                      </a>
                    </li>
                  ))}
                </ol>
              </nav>
            )}

            <div className="mt-10 text-left">
              <RecipeContent source={guide.content} />
            </div>

            {recipes.length > 0 && (
              <section className="mt-14 text-left">
                <h2 className="mb-6 text-center font-serif text-2xl uppercase tracking-wide text-bone">
                  Opskrifter i guiden
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
            )}

            <RecipeFaqSection items={guide.faq} />
          </div>
        </div>

        {relatedGuides.length > 0 && (
          <section className="border-t-2 border-bone/15 bg-ash/40 py-14">
            <div className="mx-auto max-w-5xl px-5 text-center md:px-8">
              <h2 className="mb-8 font-serif text-3xl uppercase tracking-wide text-bone">
                Flere guides
              </h2>
              <div className="grid gap-6 text-left sm:grid-cols-2 lg:grid-cols-4">
                {relatedGuides.map((g) => (
                  <Link
                    key={g.slug}
                    href={`/guides/${g.slug}`}
                    className="rounded-2xl border-2 border-bone/15 bg-iron/40 p-4 transition-colors hover:border-herb"
                  >
                    <p className="font-serif text-lg uppercase tracking-wide text-bone">
                      {g.title}
                    </p>
                    <p className="mt-2 line-clamp-3 text-sm text-bone/50">
                      {g.description}
                    </p>
                  </Link>
                ))}
              </div>
            </div>
          </section>
        )}
      </article>
    </>
  );
}
