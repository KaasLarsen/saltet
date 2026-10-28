import { compileMDX } from "next-mdx-remote/rsc";
import { anmeldelseMdxComponents } from "./GrejMDX";

interface AnmeldelseContentProps {
  source: string;
}

export async function AnmeldelseContent({ source }: AnmeldelseContentProps) {
  if (!source) return null;

  const { content } = await compileMDX({
    source,
    components: anmeldelseMdxComponents,
  });

  return <div className="recipe-prose overflow-x-auto">{content}</div>;
}
