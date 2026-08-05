import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { RecipeCard } from "@/components/RecipeCard";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { getCategory } from "@/lib/categories";
import { getRecipesByCategory } from "@/lib/recipes";
import { buildCategoryMetadata } from "@/lib/seo";

interface CategoryPageProps {
  params: Promise<{ category: string }>;
}

export async function generateStaticParams() {
  const { categories } = await import("@/lib/categories");
  return categories.map((c) => ({ category: c.slug }));
}

export async function generateMetadata({
  params,
}: CategoryPageProps): Promise<Metadata> {
  const { category: categorySlug } = await params;
  const category = getCategory(categorySlug);
  if (!category) return {};

  return buildCategoryMetadata(
    category.slug,
    category.headline,
    category.description
  );
}

export default async function CategoryPage({ params }: CategoryPageProps) {
  const { category: categorySlug } = await params;
  const category = getCategory(categorySlug);
  if (!category) notFound();

  const recipes = getRecipesByCategory(categorySlug);

  return (
    <div className="mx-auto max-w-6xl px-5 py-12 md:px-8 md:py-16">
      <Breadcrumbs
        items={[
          { label: "Forside", href: "/" },
          { label: "Opskrifter", href: "/opskrifter" },
          { label: category.name },
        ]}
      />
      <h1 className="font-serif text-3xl font-medium text-charcoal md:text-4xl">
        {category.headline}
      </h1>
      <p className="mt-3 max-w-xl text-charcoal/65 leading-relaxed">
        {category.description}
      </p>
      <div className="mt-10 grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
        {recipes.map((recipe) => (
          <RecipeCard key={recipe.slug} recipe={recipe} />
        ))}
      </div>
    </div>
  );
}
