import type { MDXComponents } from "mdx/types";

export function useMDXComponents(components: MDXComponents): MDXComponents {
  return {
    h2: ({ children }) => (
      <h2 className="mt-10 mb-4 font-serif text-2xl text-bone">{children}</h2>
    ),
    p: ({ children }) => (
      <p className="mb-4 leading-relaxed text-bone/70">{children}</p>
    ),
    ...components,
  };
}
