export type Difficulty = "nem" | "mellem" | "svær";

export interface RecipeFaq {
  question: string;
  answer: string;
}

export interface RecipeFrontmatter {
  title: string;
  slug: string;
  category: string;
  description: string;
  prepTime: string;
  cookTime: string;
  totalTime: string;
  servings: number;
  difficulty: Difficulty;
  tags: string[];
  image: string;
  imageAlt: string;
  publishedAt: string;
  featured?: boolean;
  relatedGrej?: string[];
  /** Id fra lib/affiliate.ts — eksplicit grej/produkt-CTA på opskriften. */
  affiliateProduct?: string;
  /** Direkte dhwines.dk-produkt-URL — wrap'es i Partner-ads tracking. */
  affiliateWineUrl?: string;
  /**
   * Grocery-CTA (Økologisk-Supermarked).
   * true = tving frem, false = skjul, undefined = auto (pantry/featured/tags).
   */
  affiliateGrocery?: boolean;
  /** Direkte produkt-URL på okologisk-supermarked.dk. */
  affiliateGroceryUrl?: string;
  ingredients: string[];
  steps: string[];
  faq: RecipeFaq[];
}

export interface Recipe extends RecipeFrontmatter {
  content: string;
}

export interface Category {
  slug: string;
  name: string;
  description: string;
  headline: string;
}

export interface Holiday {
  slug: string;
  name: string;
  description: string;
  headline: string;
}

export interface Topic {
  slug: string;
  name: string;
  description: string;
  headline: string;
}

export interface GuideFaq {
  question: string;
  answer: string;
}

export interface GuideFrontmatter {
  title: string;
  slug: string;
  description: string;
  tags: string[];
  image: string;
  imageAlt: string;
  publishedAt: string;
  updatedAt?: string;
  faq: GuideFaq[];
  relatedRecipes: string[];
  relatedGuides?: string[];
}

export interface Guide extends GuideFrontmatter {
  content: string;
}

export type GrejTrack = "test" | "koebsguide" | "vedligeholdelse";

export interface GrejFaq {
  question: string;
  answer: string;
}

export interface PriceRunnerWidgetConfig {
  label: string;
  query: string;
  productId?: string;
  categoryId?: string;
  sku?: string;
}

export interface GrejFrontmatter {
  title: string;
  slug: string;
  description: string;
  track: GrejTrack;
  tags: string[];
  image: string;
  imageAlt: string;
  publishedAt: string;
  updatedAt?: string;
  faq: GrejFaq[];
  relatedRecipes: string[];
  relatedGuides?: string[];
  relatedGrej?: string[];
  widgets?: PriceRunnerWidgetConfig[];
}

export interface Grej extends GrejFrontmatter {
  content: string;
}
