import { compileMDX } from "next-mdx-remote/rsc";
import { guideMdxComponents } from "./GuideMDX";

interface GuideContentProps {
  source: string;
}

export async function GuideContent({ source }: GuideContentProps) {
  if (!source) return null;

  const { content } = await compileMDX({
    source,
    components: guideMdxComponents,
  });

  return <div className="recipe-prose overflow-x-auto">{content}</div>;
}
