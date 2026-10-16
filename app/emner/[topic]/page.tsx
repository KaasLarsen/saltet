import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { CategoryFilters } from "@/components/CategoryFilters";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { buildTopicMetadata } from "@/lib/seo";
import { getTopic, getAllTopicSlugs, getRecipesByTopic } from "@/lib/topics";
import type { Recipe, RecipeFrontmatter } from "@/lib/types";

interface TopicPageProps {
  params: Promise<{ topic: string }>;
}

export async function generateStaticParams() {
  return getAllTopicSlugs().map((topic) => ({ topic }));
}

export async function generateMetadata({
  params,
}: TopicPageProps): Promise<Metadata> {
  const { topic: topicSlug } = await params;
  const topic = getTopic(topicSlug);
  if (!topic) return {};

  return buildTopicMetadata(topic.slug, topic.headline, topic.description);
}

function toListItem(recipe: Recipe): RecipeFrontmatter {
  const copy: RecipeFrontmatter & { content?: string } = { ...recipe };
  delete copy.content;
  return copy;
}

export default async function TopicPage({ params }: TopicPageProps) {
  const { topic: topicSlug } = await params;
  const topic = getTopic(topicSlug);
  if (!topic) notFound();

  const recipes = getRecipesByTopic(topicSlug).map(toListItem);

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 text-center md:px-8 md:py-16">
      <div className="flex justify-center">
        <Breadcrumbs
          items={[
            { label: "Forside", href: "/" },
            { label: "Emner", href: "/emner" },
            { label: topic.name },
          ]}
        />
      </div>
      <p className="mb-3 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
        Emne
      </p>
      <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
        {topic.headline}
      </h1>
      <p className="mx-auto mt-4 max-w-xl leading-relaxed text-bone/55">
        {topic.description}
      </p>

      <CategoryFilters
        recipes={recipes}
        searchPlaceholder={`Søg i ${topic.name.toLowerCase()}…`}
      />
    </div>
  );
}
