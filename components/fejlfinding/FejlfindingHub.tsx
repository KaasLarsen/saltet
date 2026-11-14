"use client";

import Image from "next/image";
import Link from "next/link";
import { useMemo, useState } from "react";
import {
  FEJLFINDING_GEAR_NAV,
  getFejlfindingGearName,
  type FejlfindingGearNavSlug,
} from "@/lib/fejlfinding-nav";

export interface FejlfindingHubCard {
  title: string;
  slug: string;
  description: string;
  symptom: string;
  gear: string;
  image: string;
  imageAlt: string;
  matrixCount: number;
}

interface LegacyGuideCard {
  title: string;
  slug: string;
  description: string;
}

interface FejlfindingHubProps {
  items: FejlfindingHubCard[];
  legacyGuides: LegacyGuideCard[];
  initialGear?: string;
}

function isGearSlug(value: string): value is FejlfindingGearNavSlug {
  return FEJLFINDING_GEAR_NAV.some((g) => g.slug === value);
}

export function FejlfindingHub({
  items,
  legacyGuides,
  initialGear,
}: FejlfindingHubProps) {
  const [gear, setGear] = useState<string>(
    initialGear && isGearSlug(initialGear) ? initialGear : "alle"
  );

  const filtered = useMemo(() => {
    if (gear === "alle") return items;
    return items.filter((item) => item.gear === gear);
  }, [gear, items]);

  function selectGear(next: string) {
    setGear(next);
    const url = new URL(window.location.href);
    if (next === "alle") {
      url.searchParams.delete("grej");
    } else {
      url.searchParams.set("grej", next);
    }
    window.history.replaceState({}, "", url.pathname + url.search);
  }

  return (
    <div>
      <div
        className="mt-10 flex flex-wrap items-center justify-center gap-2"
        role="group"
        aria-label="Filtrer efter grej"
      >
        <button
          type="button"
          onClick={() => selectGear("alle")}
          className={`rounded-lg px-3 py-1.5 text-[11px] font-bold uppercase tracking-[0.14em] transition-colors ${
            gear === "alle"
              ? "bg-wood text-iron"
              : "border-2 border-bone/20 bg-ash/40 text-bone/60 hover:border-wood/50 hover:text-bone"
          }`}
        >
          Alle
        </button>
        {FEJLFINDING_GEAR_NAV.map((g) => (
          <button
            key={g.slug}
            type="button"
            onClick={() => selectGear(g.slug)}
            className={`rounded-lg px-3 py-1.5 text-[11px] font-bold uppercase tracking-[0.14em] transition-colors ${
              gear === g.slug
                ? "bg-wood text-iron"
                : "border-2 border-bone/20 bg-ash/40 text-bone/60 hover:border-wood/50 hover:text-bone"
            }`}
          >
            {g.name}
          </button>
        ))}
      </div>

      {filtered.length === 0 ? (
        <p className="mt-12 text-center text-bone/50">
          Ingen fejlfinding for det grej endnu — vælg en anden kategori.
        </p>
      ) : (
        <ul className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {filtered.map((item) => (
            <li key={item.slug}>
              <Link
                href={`/fejlfinding/${item.slug}`}
                className="group flex h-full flex-col overflow-hidden rounded-2xl border-2 border-bone/15 bg-ash/30 transition-colors hover:border-wood"
              >
                <div className="relative aspect-[16/10] overflow-hidden bg-iron">
                  <Image
                    src={item.image}
                    alt={item.imageAlt}
                    fill
                    className="object-cover transition-transform duration-300 group-hover:scale-[1.03]"
                    sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"
                  />
                  <span className="absolute left-3 top-3 rotate-[-2deg] rounded-md border-2 border-iron bg-wood px-2 py-0.5 text-[10px] font-bold uppercase tracking-[0.14em] text-iron">
                    {getFejlfindingGearName(item.gear)}
                  </span>
                </div>
                <div className="flex flex-1 flex-col p-4 text-left">
                  <p className="text-[11px] font-bold uppercase tracking-[0.14em] text-wood">
                    {item.symptom}
                  </p>
                  <h2 className="mt-2 font-serif text-xl uppercase leading-snug tracking-wide text-bone">
                    {item.title}
                  </h2>
                  <p className="mt-2 line-clamp-2 flex-1 text-sm text-bone/55">
                    {item.description}
                  </p>
                  <p className="mt-3 text-[11px] font-semibold uppercase tracking-[0.12em] text-bone/40">
                    {item.matrixCount} fejl · action-plan
                  </p>
                </div>
              </Link>
            </li>
          ))}
        </ul>
      )}

      {legacyGuides.length > 0 ? (
        <section className="mt-16 border-t-2 border-bone/15 pt-12">
          <h2 className="text-center font-serif text-2xl uppercase tracking-wide text-bone">
            Flere redningsguides
          </h2>
          <p className="mx-auto mt-3 max-w-lg text-center text-sm text-bone/50">
            Klassiske fejlguides der stadig redder middagen — samme tone, længere
            Q&A.
          </p>
          <ul className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {legacyGuides.map((guide) => (
              <li key={guide.slug}>
                <Link
                  href={`/guides/${guide.slug}`}
                  className="block h-full rounded-2xl border-2 border-bone/15 bg-iron/40 p-4 transition-colors hover:border-herb"
                >
                  <p className="font-serif text-lg uppercase tracking-wide text-bone">
                    {guide.title}
                  </p>
                  <p className="mt-2 line-clamp-3 text-sm text-bone/50">
                    {guide.description}
                  </p>
                </Link>
              </li>
            ))}
          </ul>
        </section>
      ) : null}
    </div>
  );
}
