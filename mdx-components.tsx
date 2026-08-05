import type { MDXComponents } from "mdx/types";

export function useMDXComponents(components: MDXComponents): MDXComponents {
  return {
    h2: ({ children }) => (
      <h2 className="font-serif text-2xl font-medium text-charcoal mt-10 mb-4">
        {children}
      </h2>
    ),
    p: ({ children }) => (
      <p className="text-charcoal/80 leading-relaxed mb-4">{children}</p>
    ),
    ...components,
  };
}
