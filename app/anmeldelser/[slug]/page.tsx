import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { notFound } from "next/navigation";
import { AffiliateCta } from "@/components/AffiliateCta";
import { AnmeldelseStars } from "@/components/AnmeldelseStars";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { JsonLd } from "@/components/JsonLd";
import { PriceRunnerWidget } from "@/components/PriceRunnerWidget";
import { RecipeCard } from "@/components/RecipeCard";
import { RecipeFaqSection } from "@/components/RecipeFaq";
import { AnmeldelseContent } from "@/components/mdx/AnmeldelseContent";
import {
  getAllAnmeldelseSlugs,
  getAnmeldelse,
  getRelatedAnmeldelseRecipes,
  getRelatedAnmeldelser,
} from "@/lib/anmeldelser";
import { formatDate } from "@/lib/format";
import { getPriceRunnerComparison } from "@/lib/pricerunner-offers";
import { findPriceRunnerProduct } from "@/lib/pricerunner-products";
import {
  absoluteUrl,
  buildAnmeldelseArticleJsonLd,
  buildAnmeldelseMetadata,
  buildBreadcrumbJsonLd,
  buildFaqJsonLd,
} from "@/lib/seo";
import { slugifyTag } from "@/lib/slug";

interface AnmeldelsePageProps {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  return getAllAnmeldelseSlugs().map((slug) => ({ slug }));
}

export async function generateMetadata({
  params,
}: AnmeldelsePageProps): Promise<Metadata> {
  const { slug } = await params;
  const item = getAnmeldelse(slug);
  if (!item) return {};
  return buildAnmeldelseMetadata(item);
}

export default async function AnmeldelsePage({ params }: AnmeldelsePageProps) {
  const { slug } = await params;
  const item = getAnmeldelse(slug);
  if (!item) notFound();

  const recipes = getRelatedAnmeldelseRecipes(item);
  const related = getRelatedAnmeldelser(item);
  const pageUrl = absoluteUrl(`/anmeldelser/${item.slug}`);

  const prProduct = findPriceRunnerProduct(item.productName);
  const comparison = prProduct
    ? await getPriceRunnerComparison(
        prProduct.categoryId,
        prProduct.productId,
        prProduct.slugPath
      )
    : null;
  const rating =
    comparison?.ratingAverage ??
    (item.rating != null && item.rating > 0 ? item.rating : null);
  const ratingCount =
    comparison?.ratingAverage != null
      ? comparison.ratingCount
      : (item.ratingCount ?? 0);

  const headingMatches = [...item.content.matchAll(/^## (.+)$/gm)];
  const toc = headingMatches.map((match) => ({
    id: slugifyTag(match[1]),
    label: match[1],
  }));

  const breadcrumbItems = [
    { name: "Forside", url: absoluteUrl("/") },
    { name: "Anmeldelser", url: absoluteUrl("/anmeldelser") },
    { name: item.title, url: pageUrl },
  ];

  const faqJsonLd = buildFaqJsonLd(item.faq);
  const jsonLdItem =
    rating != null && ratingCount > 0
      ? { ...item, rating, ratingCount }
      : { ...item, rating: undefined, ratingCount: undefined };
  const jsonLd = [
    buildAnmeldelseArticleJsonLd(jsonLdItem),
    buildBreadcrumbJsonLd(breadcrumbItems),
    ...(faqJsonLd ? [faqJsonLd] : []),
  ];

  return (
    <>
      <JsonLd data={jsonLd} />

      <article>
        <div className="relative aspect-[16/10] w-full overflow-hidden border-b-2 border-bone/15 bg-white md:aspect-[21/9] md:max-h-[520px]">
          <Image
            src={item.image}
            alt={item.imageAlt}
            fill
            quality={90}
            className="object-contain object-center"
            sizes="100vw"
            priority
          />
        </div>

        <div className="mx-auto max-w-5xl px-5 md:px-8">
          <div className="mx-auto max-w-2xl py-10 md:py-14">
            <div className="flex justify-center">
              <Breadcrumbs
                items={[
                  { label: "Forside", href: "/" },
                  { label: "Anmeldelser", href: "/anmeldelser" },
                  { label: item.title },
                ]}
              />
            </div>

            <header className="text-center">
              <p className="mb-4 text-[11px] font-bold uppercase tracking-[0.16em] text-herb">
                Anmeldelse
              </p>
              <h1 className="font-serif text-4xl uppercase leading-tight tracking-wide text-bone md:text-5xl md:leading-[1.05]">
                {item.title}
              </h1>
              {rating != null ? (
                <AnmeldelseStars
                  rating={rating}
                  count={ratingCount}
                  className="mt-5"
                />
              ) : null}
              <p className="mx-auto mt-5 max-w-xl text-lg leading-relaxed text-bone/60">
                {item.description}
              </p>
              {item.verdict ? (
                <p className="mx-auto mt-5 max-w-xl rounded-2xl border-2 border-herb/40 bg-herb/10 px-5 py-4 text-left text-sm leading-relaxed text-bone/80">
                  <span className="mb-1 block text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
                    Dom
                  </span>
                  {item.verdict}
                </p>
              ) : null}
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
              <AnmeldelseContent source={item.content} />
            </div>

            {(item.affiliateOffers ?? []).length > 0 && (
              <section className="mt-10 text-left" aria-label="Forhandlere">
                <h2 className="mb-2 text-center font-serif text-2xl uppercase tracking-wide text-bone">
                  Forhandlere
                </h2>
                <p className="mb-6 text-center text-sm text-bone/50">
                  Sammenlign hos vores partnere — eller brug PriceRunner
                  herunder.
                </p>
                {(item.affiliateOffers ?? []).map((id) => (
                  <AffiliateCta key={id} id={id} />
                ))}
              </section>
            )}

            {(item.widgets ?? []).length > 0 && (
              <div className="mt-10">
                {(item.widgets ?? []).map((widget) => (
                  <PriceRunnerWidget
                    key={`${widget.query}-${widget.productId ?? ""}`}
                    query={widget.query}
                    label={widget.label}
                    productId={widget.productId}
                    categoryId={widget.categoryId}
                    sku={widget.sku}
                  />
                ))}
              </div>
            )}

            {recipes.length > 0 && (
              <section className="mt-14 text-left">
                <h2 className="mb-6 text-center font-serif text-2xl uppercase tracking-wide text-bone">
                  Prøv den i køkkenet
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
                Flere anmeldelser
              </h2>
              <div className="grid gap-6 text-left sm:grid-cols-2 lg:grid-cols-3">
                {related.map((a) => (
                  <Link
                    key={a.slug}
                    href={`/anmeldelser/${a.slug}`}
                    className="rounded-2xl border-2 border-bone/15 bg-iron/40 p-4 transition-colors hover:border-herb"
                  >
                    <p className="font-serif text-lg uppercase tracking-wide text-bone">
                      {a.title}
                    </p>
                    {a.rating != null && a.rating > 0 ? (
                      <AnmeldelseStars
                        rating={a.rating}
                        count={a.ratingCount}
                        size="sm"
                        align="start"
                        className="mt-2"
                      />
                    ) : null}
                    <p className="mt-2 line-clamp-3 text-sm text-bone/50">
                      {a.description}
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
