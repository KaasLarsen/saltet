import { ReactNode } from "react";

interface IngredientsProps {
  items: string[];
}

export function Ingredients({ items }: IngredientsProps) {
  return (
    <ul className="divide-y divide-ink/10 border-y border-ink/15">
      {items.map((item) => (
        <li
          key={item}
          className="flex items-start gap-3 py-3 text-ink/85 leading-relaxed"
        >
          <span className="mt-2 h-1.5 w-1.5 shrink-0 rotate-45 bg-herb" />
          {item}
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
    <ol className="space-y-6">
      {items.map((step, index) => (
        <li key={step} className="flex gap-4">
          <span className="flex h-8 w-8 shrink-0 items-center justify-center border border-ink/25 font-serif text-sm text-ink">
            {index + 1}
          </span>
          <p className="pt-1 leading-relaxed text-ink/85">{step}</p>
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
    <aside className="my-8 border-l-2 border-herb bg-paper/70 px-5 py-4">
      <p className="mb-1 text-[11px] font-medium uppercase tracking-[0.16em] text-herb">
        Tip
      </p>
      <div className="leading-relaxed text-ink/75">{children}</div>
    </aside>
  );
}

export const mdxComponents = {
  Ingredients,
  Steps,
  Tip,
};
