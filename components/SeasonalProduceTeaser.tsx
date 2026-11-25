import Link from "next/link";
import { getSeasonalProduceForSeason } from "@/lib/ingredient-ideas";
import { ingredientNavBySlug } from "@/lib/ingredient-nav";
import { getCurrentSeason } from "@/lib/season-nav";
import { getSeason } from "@/lib/seasons";

const SEASON_PRODUCE_HEADLINES: Record<string, string> = {
  foraar: "Forårets råvarer",
  sommer: "Sommerens råvarer",
  efteraar: "Efterårets råvarer",
  vinter: "Vinterens råvarer",
};

function seasonProduceHeadline(slug: string, name: string): string {
  return SEASON_PRODUCE_HEADLINES[slug] ?? `${name}s råvarer`;
}

export function SeasonalProduceTeaser() {
  const currentSeasonNav = getCurrentSeason();
  const currentSeason = getSeason(currentSeasonNav.slug);
  const produce = getSeasonalProduceForSeason(currentSeasonNav.slug);

  if (produce.length === 0 || !currentSeason) return null;

  return (
    <section className="mx-auto max-w-5xl px-5 py-16 md:px-8 md:py-20">
      <div className="mb-10 flex flex-col items-center gap-3 text-center">
        <p className="inline-flex rotate-[-1.5deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.16em] text-iron">
          Sæsonens råvarer
        </p>
        <h2 className="font-serif text-3xl uppercase tracking-wide text-bone md:text-4xl">
          {seasonProduceHeadline(currentSeason.slug, currentSeason.name)}
        </h2>
        <p className="max-w-md text-sm text-bone/50">
          Inspiration til det, der er i sæson — og til at få brugt resten op.
        </p>
        <Link
          href="/raavare-indeks"
          className="rounded-lg border-2 border-wood/60 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.14em] text-wood transition-colors hover:bg-wood hover:text-bone"
        >
          Se alle råvarer
        </Link>
      </div>
      <ul className="mx-auto grid max-w-4xl gap-6 sm:grid-cols-2 md:grid-cols-3 md:gap-5">
        {produce.map((entry, index) => {
          const nav = ingredientNavBySlug(entry.slug);
          const name = nav?.name ?? entry.slug;
          const teaser =
            entry.blurb.split(/(?<=\.)\s/)[0] ?? entry.blurb;
          return (
            <li key={entry.slug}>
              <Link
                href={`/raavare-indeks/${entry.slug}`}
                className="group animate-rise block text-center sm:text-left"
                style={{ animationDelay: `${index * 60}ms` }}
              >
                <div className="relative aspect-[4/3] overflow-hidden rounded-2xl border-2 border-bone/20 bg-ash shadow-[4px_4px_0_0_rgba(212,255,0,0.35)] transition-[transform,box-shadow,border-color] duration-300 group-hover:-translate-y-1 group-hover:border-herb group-hover:shadow-[6px_6px_0_0_rgba(212,255,0,0.7)]">
                  {/* eslint-disable-next-line @next/next/no-img-element -- grid CDN budget: skip optimizer */}
                  <img
                    src={entry.image}
                    alt={entry.imageAlt}
                    width={800}
                    height={600}
                    decoding="async"
                    loading="lazy"
                    className="absolute inset-0 h-full w-full object-cover transition-transform duration-500 ease-out group-hover:scale-[1.05]"
                  />
                  <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-iron/55 via-transparent to-transparent" />
                </div>
                <span className="mt-4 block font-serif text-xl uppercase tracking-wide text-bone transition-colors group-hover:text-herb">
                  {name}
                </span>
                <span className="mt-2 block text-sm leading-relaxed text-bone/45 group-hover:text-bone/60">
                  {teaser}
                </span>
              </Link>
            </li>
          );
        })}
      </ul>
    </section>
  );
}
