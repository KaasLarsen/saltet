import { ReactNode } from "react";

interface IngredientsProps {
  items: string[];
}

export function Ingredients({ items }: IngredientsProps) {
  return (
    <ul className="divide-y divide-bone/10 border-y border-bone/15">
      {items.map((item) => (
        <li
          key={item}
          className="flex items-start gap-3 py-3 leading-relaxed text-bone/80"
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
          <span className="flex h-8 w-8 shrink-0 items-center justify-center border border-bone/25 font-serif text-sm text-bone">
            {index + 1}
          </span>
          <p className="pt-1 leading-relaxed text-bone/80">{step}</p>
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
    <aside className="my-8 border-l-2 border-herb bg-ash/50 px-5 py-4 text-left">
      <p className="mb-1 text-[11px] font-medium uppercase tracking-[0.16em] text-herb">
        Tip
      </p>
      <div className="leading-relaxed text-bone/70">{children}</div>
    </aside>
  );
}

export const mdxComponents = {
  Ingredients,
  Steps,
  Tip,
};
