import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { RecipeCard } from "@/components/RecipeCard";
import {
  getAllTags,
  getRecipesByTagSlug,
  getTagBySlug,
} from "@/lib/tags";
import { absoluteUrl, siteConfig } from "@/lib/seo";

interface TagPageProps {
  params: Promise<{ tag: string }>;
}

export async function generateStaticParams() {
  return getAllTags().map((t) => ({ tag: t.slug }));
}

export async function generateMetadata({
  params,
}: TagPageProps): Promise<Metadata> {
  const { tag: tagSlug } = await params;
  const tag = getTagBySlug(tagSlug);
  if (!tag) return {};

  const title = `Opskrifter med tagget “${tag.label}”`;
  const description = `Se alle opskrifter på ${siteConfig.name} tagged med ${tag.label}.`;
  const url = absoluteUrl(`/tags/${tag.slug}`);

  return {
    title,
    description,
    alternates: { canonical: url },
    openGraph: {
      title: `${title} | ${siteConfig.name}`,
      description,
      url,
      siteName: siteConfig.name,
      locale: siteConfig.locale,
      type: "website",
    },
  };
}

export default async function TagPage({ params }: TagPageProps) {
  const { tag: tagSlug } = await params;
  const tag = getTagBySlug(tagSlug);
  if (!tag) notFound();

  const recipes = getRecipesByTagSlug(tagSlug);

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 text-center md:px-8 md:py-16">
      <div className="flex justify-center">
        <Breadcrumbs
          items={[
            { label: "Forside", href: "/" },
            { label: "Tags", href: "/tags" },
            { label: tag.label },
          ]}
        />
      </div>
      <p className="mb-3 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
        Tag
      </p>
      <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
        {tag.label}
      </h1>
      <p className="mx-auto mt-4 max-w-xl leading-relaxed text-bone/55">
        {recipes.length} opskrift{recipes.length === 1 ? "" : "er"} med dette
        tag.
      </p>
      <div className="mt-12 grid gap-10 text-left sm:grid-cols-2 lg:grid-cols-3">
        {recipes.map((recipe) => (
          <RecipeCard
            key={`${recipe.category}-${recipe.slug}`}
            recipe={recipe}
          />
        ))}
      </div>
    </div>
  );
}
