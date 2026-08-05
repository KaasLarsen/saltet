export type Difficulty = "nem" | "mellem" | "svær";

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
