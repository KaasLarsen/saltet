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
