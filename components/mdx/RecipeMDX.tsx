import { ReactNode } from "react";

interface IngredientsProps {
  items: string[];
}

export function Ingredients({ items }: IngredientsProps) {
  return (
    <ul className="space-y-2">
      {items.map((item) => (
        <li
          key={item}
          className="flex items-start gap-3 text-charcoal/85 leading-relaxed"
        >
          <span className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-accent" />
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
          <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-accent/15 font-serif text-sm font-medium text-accent">
            {index + 1}
          </span>
          <p className="pt-1 text-charcoal/85 leading-relaxed">{step}</p>
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
    <aside className="my-8 rounded-2xl border border-accent/20 bg-accent/5 px-5 py-4">
      <p className="mb-1 text-xs font-medium uppercase tracking-wider text-accent">
        Tip
      </p>
      <div className="text-charcoal/80 leading-relaxed">{children}</div>
    </aside>
  );
}

export const mdxComponents = {
  Ingredients,
  Steps,
  Tip,
};
