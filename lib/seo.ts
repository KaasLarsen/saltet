import type { Metadata } from "next";
import type { Recipe } from "./types";
import { getCategoryName } from "./categories";

const siteUrl =
  process.env.NEXT_PUBLIC_SITE_URL?.replace(/\/$/, "") ?? "https://saltet.dk";

export const siteConfig = {
  name: "Saltet",
  url: siteUrl,
  email: "info@saltet.dk",
  description:
    "Salt på maden. Opskrifter med kant til airfryer, grill, plancha, gryde, pande, sylte, dips, sous vide, trykkoger og dehydrator — enkelt, sprødt og med smag.",
  locale: "da_DK",
  language: "da",
};

export function absoluteUrl(path: string): string {
  return `${siteConfig.url}${path.startsWith("/") ? path : `/${path}`}`;
}

export function buildRecipeMetadata(recipe: Recipe): Metadata {
  const url = absoluteUrl(`/opskrifter/${recipe.category}/${recipe.slug}`);

  return {
    title: `${recipe.title} | Saltet`,
    description: recipe.description,
    alternates: { canonical: url },
    openGraph: {
      title: recipe.title,
      description: recipe.description,
      url,
      siteName: siteConfig.name,
      locale: siteConfig.locale,
      type: "article",
      publishedTime: recipe.publishedAt,
      images: [
        {
          url: absoluteUrl(recipe.image),
          alt: recipe.imageAlt,
          width: 1200,
          height: 800,
        },
      ],
    },
    twitter: {
      card: "summary_large_image",
      title: recipe.title,
      description: recipe.description,
      images: [absoluteUrl(recipe.image)],
    },
  };
}

export function buildCategoryMetadata(
  categorySlug: string,
  headline: string,
  description: string
): Metadata {
  const url = absoluteUrl(`/opskrifter/${categorySlug}`);

  return {
    title: `${headline} | Saltet`,
    description,
    alternates: { canonical: url },
    openGraph: {
      title: `${headline} | Saltet`,
      description,
      url,
      siteName: siteConfig.name,
      locale: siteConfig.locale,
      type: "website",
    },
  };
}

export function buildBreadcrumbJsonLd(
  items: { name: string; url: string }[]
): object {
  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: items.map((item, index) => ({
      "@type": "ListItem",
      position: index + 1,
      name: item.name,
      item: item.url,
    })),
  };
}

export function buildRecipeJsonLd(recipe: Recipe): object {
  const url = absoluteUrl(`/opskrifter/${recipe.category}/${recipe.slug}`);

  return {
    "@context": "https://schema.org",
    "@type": "Recipe",
    name: recipe.title,
    description: recipe.description,
    image: [absoluteUrl(recipe.image)],
    datePublished: recipe.publishedAt,
    prepTime: recipe.prepTime,
    cookTime: recipe.cookTime,
    totalTime: recipe.totalTime,
    recipeYield: `${recipe.servings} portioner`,
    recipeCategory: getCategoryName(recipe.category),
    recipeCuisine: "Dansk",
    keywords: recipe.tags.join(", "),
    author: {
      "@type": "Organization",
      name: siteConfig.name,
      url: siteConfig.url,
    },
    recipeIngredient: recipe.ingredients,
    recipeInstructions: recipe.steps.map((text, index) => ({
      "@type": "HowToStep",
      position: index + 1,
      text,
    })),
    mainEntityOfPage: {
      "@type": "WebPage",
      "@id": url,
    },
  };
}

export function buildFaqJsonLd(faq: Recipe["faq"]): object | null {
  if (!faq?.length) return null;

  return {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: faq.map((item) => ({
      "@type": "Question",
      name: item.question,
      acceptedAnswer: {
        "@type": "Answer",
        text: item.answer,
      },
    })),
  };
}

export function buildWebsiteJsonLd(): object {
  return {
    "@context": "https://schema.org",
    "@type": "WebSite",
    name: siteConfig.name,
    url: siteConfig.url,
    description: siteConfig.description,
    inLanguage: "da-DK",
  };
}
