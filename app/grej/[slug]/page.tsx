import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { JsonLd } from "@/components/JsonLd";
import { PriceRunnerWidget } from "@/components/PriceRunnerWidget";
import { RecipeCard } from "@/components/RecipeCard";
import { RecipeFaqSection } from "@/components/RecipeFaq";
import { GrejContent } from "@/components/mdx/GrejContent";
import {
  getAllGrejSlugs,
  getGrej,
  getRelatedGrej,
  getRelatedGrejRecipes,
} from "@/lib/grej";
import { GREJ_TRACKS } from "@/lib/grej-filters";
import { formatDate } from "@/lib/format";
import {
  absoluteUrl,
  buildBreadcrumbJsonLd,
  buildFaqJsonLd,
  buildGrejArticleJsonLd,
  buildGrejMetadata,
} from "@/lib/seo";
import { slugifyTag } from "@/lib/slug";

interface GrejPageProps {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  return getAllGrejSlugs().map((slug) => ({ slug }));
}

export async function generateMetadata({
  params,
}: GrejPageProps): Promise<Metadata> {
  const { slug } = await params;
  const item = getGrej(slug);
  if (!item) return {};
  return buildGrejMetadata(item);
}

export default async function GrejPage({ params }: GrejPageProps) {
  const { slug } = await params;
  const item = getGrej(slug);
  if (!item) notFound();

  const recipes = getRelatedGrejRecipes(item);
  const related = getRelatedGrej(item);
  const grejUrl = absoluteUrl(`/grej/${item.slug}`);
  const trackLabel =
    GREJ_TRACKS.find((track) => track.slug === item.track)?.label ?? item.track;

  const headingMatches = [...item.content.matchAll(/^## (.+)$/gm)];
  const toc = headingMatches.map((match) => ({
    id: slugifyTag(match[1]),
    label: match[1],
  }));

  const breadcrumbItems = [
    { name: "Forside", url: absoluteUrl("/") },
    { name: "Grej", url: absoluteUrl("/grej") },
    { name: item.title, url: grejUrl },
  ];

  const faqJsonLd = buildFaqJsonLd(item.faq);
  const jsonLd = [
    buildGrejArticleJsonLd(item),
    buildBreadcrumbJsonLd(breadcrumbItems),
    ...(faqJsonLd ? [faqJsonLd] : []),
  ];

  return (
    <>
      <JsonLd data={jsonLd} />

      <article>
        <div className="relative aspect-[16/10] w-full overflow-hidden bg-iron md:aspect-[21/9] md:max-h-[520px]">
          <Image
            src={item.image}
            alt={item.imageAlt}
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
                  { label: "Grej", href: "/grej" },
                  { label: item.title },
                ]}
              />
            </div>

            <header className="text-center">
              <p className="mb-4 text-[11px] font-bold uppercase tracking-[0.16em] text-herb">
                {trackLabel}
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

            {toc.length > 0 && (
              <nav
                aria-label="Indhold"
                className="mt-10 rounded-2xl border-2 border-bone/15 bg-ash/40 p-5 text-left"
              >
                <p className="mb-3 text-[11px] font-bold uppercase tracking-[0.16em] text-herb">
                  På denne side
                </p>
                <ol className="space-y-2">
                  {toc.map((heading, index) => (
                    <li key={heading.id}>
                      <a
                        href={`#${heading.id}`}
                        className="text-sm text-bone/70 underline-offset-2 hover:text-herb hover:underline"
                      >
                        {index + 1}. {heading.label}
                      </a>
                    </li>
                  ))}
                </ol>
              </nav>
            )}

            <div className="mt-10 text-left">
              <GrejContent source={item.content} />
            </div>

            {(item.widgets ?? []).length > 0 && (
              <div className="mt-10">
                {(item.widgets ?? []).map((widget) => (
                  <PriceRunnerWidget
                    key={`${widget.query}-${widget.productId ?? ""}`}
                    query={widget.query}
                    label={widget.label}
                    productId={widget.productId}
                    sku={widget.sku}
                  />
                ))}
              </div>
            )}

            {recipes.length > 0 && (
              <section className="mt-14 text-left">
                <h2 className="mb-6 text-center font-serif text-2xl uppercase tracking-wide text-bone">
                  Prøv grejet i køkkenet
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

            <RecipeFaqSection items={item.faq} />
          </div>
        </div>

        {related.length > 0 && (
          <section className="border-t-2 border-bone/15 bg-ash/40 py-14">
            <div className="mx-auto max-w-5xl px-5 text-center md:px-8">
              <h2 className="mb-8 font-serif text-3xl uppercase tracking-wide text-bone">
                Mere grej
              </h2>
              <div className="grid gap-6 text-left sm:grid-cols-2 lg:grid-cols-4">
                {related.map((g) => (
                  <Link
                    key={g.slug}
                    href={`/grej/${g.slug}`}
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
