import { compileMDX } from "next-mdx-remote/rsc";
import { grejMdxComponents } from "./GrejMDX";

interface AnmeldelseContentProps {
  source: string;
}

export async function AnmeldelseContent({ source }: AnmeldelseContentProps) {
  if (!source) return null;

  const { content } = await compileMDX({
    source,
    components: grejMdxComponents,
  });

  return <div className="recipe-prose overflow-x-auto">{content}</div>;
}
