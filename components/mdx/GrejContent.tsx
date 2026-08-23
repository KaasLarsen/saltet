import { compileMDX } from "next-mdx-remote/rsc";
import { grejMdxComponents } from "./GrejMDX";

interface GrejContentProps {
  source: string;
}

export async function GrejContent({ source }: GrejContentProps) {
  if (!source) return null;

  const { content } = await compileMDX({
    source,
    components: grejMdxComponents,
  });

  return <div className="recipe-prose overflow-x-auto">{content}</div>;
}
