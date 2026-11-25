import type { Metadata } from "next";
import Link from "next/link";
import { groupIngredientsByLetter } from "@/lib/ingredients";
import { absoluteUrl, siteConfig } from "@/lib/seo";

export const metadata: Metadata = {
  title: "Råvareindeks",
  description: `Find opskrifter efter råvare på ${siteConfig.name} — kartoffel, løg, grønkål og mere. Mindre madspild, mere sæson.`,
  alternates: { canonical: absoluteUrl("/raavare-indeks") },
};

export default function RaavareIndeksPage() {
  const groups = groupIngredientsByLetter();
  const total = groups.reduce((sum, group) => sum + group.items.length, 0);

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 md:px-8 md:py-16">
      <div className="mx-auto max-w-2xl text-center">
        <p className="mb-3 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
          Opslagsværk
        </p>
        <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
          Råvareindeks
        </h1>
        <p className="mx-auto mt-4 max-w-xl leading-relaxed text-bone/55">
          {total} råvarer — slå op hvad du har i køleskabet, og find opskrifter
          der bruger det. Godt mod madspild, og nemt at spise efter sæson.
        </p>
      </div>

      <nav
        aria-label="Hop til bogstav"
        className="mx-auto mt-10 flex max-w-3xl flex-wrap justify-center gap-2"
      >
        {groups.map((group) => (
          <a
            key={group.letter}
            href={`#bogstav-${encodeURIComponent(group.letter)}`}
            className="inline-flex min-w-9 items-center justify-center rounded-lg border-2 border-bone/20 bg-ash/40 px-2.5 py-1.5 text-[12px] font-bold uppercase tracking-[0.12em] text-bone/70 transition-[transform,border-color] hover:-translate-y-0.5 hover:border-herb hover:text-bone"
          >
            {group.letter}
          </a>
        ))}
      </nav>

      <div className="mt-14 space-y-12">
        {groups.map((group) => (
          <section
            key={group.letter}
            id={`bogstav-${group.letter}`}
            className="scroll-mt-28"
          >
            <h2 className="border-b-2 border-bone/15 pb-3 font-serif text-3xl uppercase tracking-wide text-herb">
              {group.letter}
            </h2>
            <ul className="mt-5 columns-1 gap-x-10 sm:columns-2 md:columns-3">
              {group.items.map((item) => (
                <li key={item.slug} className="mb-2 break-inside-avoid">
                  <Link
                    href={`/raavare-indeks/${item.slug}`}
                    className="inline-flex items-baseline gap-2 text-bone/80 transition-colors hover:text-herb"
                  >
                    <span>{item.name}</span>
                    <span className="text-[11px] font-semibold uppercase tracking-[0.12em] text-smoke">
                      {item.count}
                    </span>
                  </Link>
                </li>
              ))}
            </ul>
          </section>
        ))}
      </div>
    </div>
  );
}
