export type Difficulty = "nem" | "mellem" | "svær";

export interface RecipeFaq {
  question: string;
  answer: string;
}

/** Felter der skal med på opskriftskort / lister — uden tung body-data. */
export interface RecipeListItem {
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
}

/** Grej vist som ikon i opskriftens meta-header. */
export interface RecipeEquipmentItem {
  /** Stabilt id (airfryer, meater, plancha, …). */
  id: string;
  /** Valgfri kort label — ellers default fra id. */
  label?: string;
}

export interface RecipeFrontmatter extends RecipeListItem {
  relatedGrej?: string[];
  /**
   * Specifikt grej til meta-ikoner. Tom/udefineret → kategori-default.
   * Brug label til præcise callouts (fx «8L Airfryer», «250°C Plancha»).
   */
  equipment?: RecipeEquipmentItem[];
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

export interface Season {
  slug: string;
  name: string;
  description: string;
  headline: string;
  /** Guide-slugs vist på sæson-hubben. */
  relatedGuideSlugs?: string[];
  /** Højtider der falder i sæsonen (fx Halloween i efterår). */
  relatedHolidaySlugs?: string[];
}

export interface Topic {
  slug: string;
  name: string;
  description: string;
  headline: string;
  /** Valgfrit cover — ellers tages et opskriftsbillede. */
  image?: string;
  imageAlt?: string;
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
  relatedGrej?: string[];
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

export interface AnmeldelseFaq {
  question: string;
  answer: string;
}

export interface AnmeldelseFrontmatter {
  title: string;
  slug: string;
  description: string;
  /** Produkttype til filtre/nav (fx airfryer, plancha). */
  series: string;
  productName: string;
  modelNumber?: string;
  tags: string[];
  image: string;
  imageAlt: string;
  publishedAt: string;
  updatedAt?: string;
  faq: AnmeldelseFaq[];
  relatedRecipes: string[];
  relatedGuides?: string[];
  relatedGrej?: string[];
  relatedAnmeldelser?: string[];
  widgets?: PriceRunnerWidgetConfig[];
  /** Affiliate-offer ids vist som forhandler-CTA’er. */
  affiliateOffers?: string[];
  verdict?: string;
  /** Gennemsnit 1–5 — synk med PriceRunner reviewSummary.average. */
  rating?: number;
  /** Antal bedømmelser — synk med PriceRunner reviewSummary.count. */
  ratingCount?: number;
}

export interface Anmeldelse extends AnmeldelseFrontmatter {
  content: string;
}

/** Grej-kategori for SOS-fejlfinding. */
export type FejlfindingGear =
  | "airfryer"
  | "stobejern"
  | "plancha"
  | "trykkoger"
  | "ovn"
  | "generelt";

/** Én fejl i den faste tre-trins-skabelon. */
export interface FejlMatrixRow {
  /** Hvad brugeren ser/smager lige nu. */
  symptom: string;
  /** Kemisk/termisk årsag. */
  physics: string;
  /** Redning lige nu. */
  now: string;
  /** Forebyggelse næste gang. */
  nextTime: string;
}

export interface FejlfindingFrontmatter {
  title: string;
  slug: string;
  description: string;
  gear: FejlfindingGear;
  /** Kort symptom til hub-kort (fx «Paneringen falder af»). */
  symptom: string;
  image: string;
  imageAlt: string;
  /** Valgfri «kiks»-foto til fail/success-compare. */
  failImage?: string;
  failImageAlt?: string;
  publishedAt: string;
  updatedAt?: string;
  matrices: FejlMatrixRow[];
  faq: GuideFaq[];
  relatedRecipes: string[];
  relatedGuides?: string[];
  relatedGrej?: string[];
}

export interface Fejlfinding extends FejlfindingFrontmatter {
  content: string;
}
