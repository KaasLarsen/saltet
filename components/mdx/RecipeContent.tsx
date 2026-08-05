import { compileMDX } from "next-mdx-remote/rsc";
import { mdxComponents } from "./RecipeMDX";

interface RecipeContentProps {
  source: string;
}

export async function RecipeContent({ source }: RecipeContentProps) {
  if (!source) return null;

  const { content } = await compileMDX({
    source,
    components: mdxComponents,
  });

  return <div className="recipe-prose">{content}</div>;
}
