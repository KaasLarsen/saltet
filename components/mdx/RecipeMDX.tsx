import Link from "next/link";
import { Children, Fragment, isValidElement, type ReactNode } from "react";
import { RecipeCard } from "@/components/RecipeCard";
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

function LinkedText({ text }: { text: string }) {
  const parts = text.split(/(\[[^\]]+\]\([^)]+\))/g);
  return (
    <>
      {parts.map((part, index) => {
        const match = part.match(/^\[([^\]]+)\]\(([^)]+)\)$/);
        if (!match) {
          return <Fragment key={index}>{part}</Fragment>;
        }
        return (
          <Link
            key={index}
            href={match[2]}
            className="font-semibold text-herb underline decoration-herb/40 underline-offset-2 hover:text-pool hover:decoration-pool"
          >
            {match[1]}
          </Link>
        );
      })}
    </>
  );
}

interface IngredientsProps {
  items: string[];
}

export function Ingredients({ items }: IngredientsProps) {
  return (
    <ul className="divide-y divide-bone/10 overflow-hidden rounded-2xl border-2 border-bone/20 bg-ash/40">
      {items.map((item) => (
        <li
          key={item}
          className="flex items-start gap-3 px-4 py-3 leading-relaxed text-bone/80"
        >
          <span className="mt-1.5 h-2.5 w-2.5 shrink-0 rotate-45 rounded-[2px] bg-herb" />
          <LinkedText text={item} />
        </li>
      ))}
    </ul>
  );
}

interface StepsProps {
  items: string[];
}

export function Steps({ items }: StepsProps) {
  return (
    <ol className="space-y-5">
      {items.map((step, index) => (
        <li key={step} className="flex gap-4">
          <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-xl border-2 border-herb bg-herb/15 font-serif text-sm text-herb">
            {index + 1}
          </span>
          <p className="pt-1.5 leading-relaxed text-bone/80">
            <LinkedText text={step} />
          </p>
        </li>
      ))}
    </ol>
  );
}

interface TipProps {
  children: ReactNode;
}

export function Tip({ children }: TipProps) {
  return (
    <aside className="my-8 -rotate-1 rounded-2xl border-2 border-wood bg-wood/10 px-5 py-4 text-left shadow-[4px_4px_0_0_rgba(255,92,57,0.45)]">
      <p className="mb-1 text-[11px] font-bold uppercase tracking-[0.16em] text-wood">
        Tip
      </p>
      <div className="leading-relaxed text-bone/75">{children}</div>
    </aside>
  );
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

export const mdxComponents = {
  Ingredients,
  Steps,
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
  a: ({
    href,
    children,
  }: {
    href?: string;
    children?: ReactNode;
  }) => (
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
      <table className="w-full min-w-[32rem] text-left text-sm text-bone/75">
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
