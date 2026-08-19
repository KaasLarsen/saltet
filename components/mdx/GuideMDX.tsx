import Link from "next/link";
import { Children, isValidElement, type ReactNode } from "react";
import { RecipeCard } from "@/components/RecipeCard";
import { Tip } from "@/components/mdx/RecipeMDX";
import { getRecipe } from "@/lib/recipes";
import { slugifyTag } from "@/lib/slug";

function headingText(children: ReactNode): string {
  return Children.toArray(children)
    .map((child) => {
      if (typeof child === "string" || typeof child === "number") {
        return String(child);
      }
      if (isValidElement<{ children?: ReactNode }>(child)) {
        return headingText(child.props.children);
      }
      return "";
    })
    .join("");
}

function headingId(children: ReactNode): string {
  return slugifyTag(headingText(children));
}

interface RecipeGridProps {
  items: string[];
}

export function RecipeGrid({ items }: RecipeGridProps) {
  const recipes = items
    .map((ref) => {
      const [category, slug] = ref.split("/");
      if (!category || !slug) return undefined;
      return getRecipe(category, slug);
    })
    .filter((r): r is NonNullable<typeof r> => Boolean(r));

  if (recipes.length === 0) return null;

  return (
    <div className="my-10 grid gap-8 text-left sm:grid-cols-2">
      {recipes.map((recipe) => (
        <RecipeCard
          key={`${recipe.category}/${recipe.slug}`}
          recipe={recipe}
        />
      ))}
    </div>
  );
}

const linkClass =
  "font-semibold text-herb underline decoration-herb/40 underline-offset-2 hover:text-pool hover:decoration-pool";

export const guideMdxComponents = {
  Tip,
  RecipeGrid,
  h2: ({ children }: { children?: ReactNode }) => (
    <h2
      id={headingId(children)}
      className="mt-12 mb-4 scroll-mt-28 font-serif text-2xl uppercase tracking-wide text-bone md:text-3xl"
    >
      {children}
    </h2>
  ),
  h3: ({ children }: { children?: ReactNode }) => (
    <h3
      id={headingId(children)}
      className="mt-8 mb-3 scroll-mt-28 font-serif text-xl uppercase tracking-wide text-bone"
    >
      {children}
    </h3>
  ),
  p: ({ children }: { children?: ReactNode }) => (
    <p className="mb-4 leading-relaxed text-bone/70">{children}</p>
  ),
  a: ({ href, children }: { href?: string; children?: ReactNode }) => (
    <Link href={href ?? "#"} className={linkClass}>
      {children}
    </Link>
  ),
  ul: ({ children }: { children?: ReactNode }) => (
    <ul className="mb-6 list-disc space-y-2 pl-5 text-bone/70">{children}</ul>
  ),
  ol: ({ children }: { children?: ReactNode }) => (
    <ol className="mb-6 list-decimal space-y-2 pl-5 text-bone/70">{children}</ol>
  ),
  li: ({ children }: { children?: ReactNode }) => (
    <li className="leading-relaxed">{children}</li>
  ),
  strong: ({ children }: { children?: ReactNode }) => (
    <strong className="font-semibold text-bone">{children}</strong>
  ),
  table: ({ children }: { children?: ReactNode }) => (
    <div className="my-8 overflow-x-auto rounded-2xl border-2 border-bone/20">
      <table className="w-full min-w-[36rem] text-left text-sm text-bone/75">
        {children}
      </table>
    </div>
  ),
  thead: ({ children }: { children?: ReactNode }) => (
    <thead className="bg-ash/80 text-[11px] font-bold uppercase tracking-[0.12em] text-herb">
      {children}
    </thead>
  ),
  th: ({ children }: { children?: ReactNode }) => (
    <th className="px-3 py-2.5">{children}</th>
  ),
  td: ({ children }: { children?: ReactNode }) => (
    <td className="border-t border-bone/10 px-3 py-2.5">{children}</td>
  ),
  blockquote: ({ children }: { children?: ReactNode }) => (
    <blockquote className="my-6 border-l-4 border-herb pl-4 text-bone/65">
      {children}
    </blockquote>
  ),
};
