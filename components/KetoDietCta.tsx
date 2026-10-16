import Link from "next/link";
import { slugifyTag } from "@/lib/slug";

const KETO_TAG_SLUGS = new Set([
  "keto",
  "low-carb",
  "carnivore",
  "elektrolyt",
  "pemmican",
  "keto-flu",
]);

export function recipeMatchesKetoDiet(tags: readonly string[]): boolean {
  return tags.some((tag) => KETO_TAG_SLUGS.has(slugifyTag(tag)));
}

interface KetoDietCtaProps {
  className?: string;
}

/**
 * Soft cross-sell til Low-Carb & Keto-hubben — vises på matching opskrifter.
 */
export function KetoDietCta({ className = "" }: KetoDietCtaProps) {
  return (
    <aside
      className={`my-10 overflow-hidden rounded-2xl border-2 border-herb/40 bg-herb/10 text-left shadow-[4px_4px_0_0_rgba(212,255,0,0.25)] ${className}`}
      aria-labelledby="keto-diet-cta-heading"
    >
      <div className="border-b border-herb/25 px-4 py-3">
        <p className="text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
          Low-Carb &amp; Keto
        </p>
      </div>
      <div className="px-5 py-5">
        <h2
          id="keto-diet-cta-heading"
          className="font-serif text-xl uppercase tracking-wide text-bone"
        >
          Lever du efter keto eller carnivore?
        </h2>
        <p className="mt-2 text-sm leading-relaxed text-bone/65">
          Se vores fulde spor til maksimal smag uden kulhydrater — fra keto-flu
          og flagesalt til osteskaller, pemmican og bone broth.
        </p>
        <div className="mt-4 flex flex-wrap gap-3">
          <Link
            href="/emner/keto"
            className="inline-flex items-center justify-center rounded-xl border-2 border-herb bg-herb px-4 py-2 text-sm font-bold uppercase tracking-wide text-iron transition-colors hover:bg-bone hover:border-bone"
          >
            Se Low-Carb &amp; Keto
          </Link>
          <Link
            href="/guides/keto-flu-og-flagesalt"
            className="inline-flex items-center justify-center rounded-xl border-2 border-bone/25 bg-ash/40 px-4 py-2 text-sm font-bold uppercase tracking-wide text-bone transition-colors hover:border-herb hover:text-herb"
          >
            Keto-flu &amp; salt
          </Link>
        </div>
      </div>
    </aside>
  );
}
