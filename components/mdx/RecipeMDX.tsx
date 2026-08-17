import Link from "next/link";
import { Fragment, type ReactNode } from "react";

export function LinkedText({ text }: { text: string }) {
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

export const mdxComponents = {
  Ingredients,
  Steps,
  Tip,
};
