"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import { usePathname, useRouter } from "next/navigation";
import { RecipeCard } from "@/components/RecipeCard";
import type { RecipeFrontmatter } from "@/lib/types";

interface SearchResultsProps {
  recipes: RecipeFrontmatter[];
  query: string;
}

/** Fast rækkefølge for kendte metoder — undgår server-only categories-import i client. */
const METHOD_ORDER = [
  "airfryer",
  "grill",
  "plancha",
  "gryde",
  "pande",
  "sylte",
  "dips",
  "sous-vide",
] as const;

const METHOD_LABELS: Record<string, string> = {
  airfryer: "Airfryer",
  grill: "Grill",
  plancha: "Plancha",
  gryde: "Gryde",
  pande: "Pande",
  sylte: "Sylte",
  dips: "Dips",
  "sous-vide": "Sous Vide",
};

function methodLabel(slug: string): string {
  return METHOD_LABELS[slug] ?? slug.charAt(0).toUpperCase() + slug.slice(1);
}

function chipClass(active: boolean): string {
  return `rounded-lg border-2 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.12em] transition-colors ${
    active
      ? "border-herb bg-herb text-iron"
      : "border-bone/25 text-bone/55 hover:border-herb hover:text-herb"
  }`;
}

function readMetodeFromLocation(): string | undefined {
  if (typeof window === "undefined") return undefined;
  return new URLSearchParams(window.location.search).get("metode") ?? undefined;
}

function getMethodsInResults(recipes: RecipeFrontmatter[]): string[] {
  const present = new Set(recipes.map((r) => r.category));
  const knownOrder = METHOD_ORDER.filter((slug) => present.has(slug));
  const extras = Array.from(present)
    .filter((slug) => !knownOrder.includes(slug as (typeof METHOD_ORDER)[number]))
    .sort((a, b) => a.localeCompare(b, "da"));
  return [...knownOrder, ...extras];
}

export function SearchResults({ recipes, query }: SearchResultsProps) {
  const router = useRouter();
  const pathname = usePathname();
  const [metode, setMetode] = useState<string | undefined>(undefined);

  useEffect(() => {
    setMetode(readMetodeFromLocation());
  }, []);

  const methods = useMemo(() => getMethodsInResults(recipes), [recipes]);
  const showMethodFilter = methods.length > 1;

  const filtered = useMemo(() => {
    if (!metode || !methods.includes(metode)) return recipes;
    return recipes.filter((r) => r.category === metode);
  }, [recipes, metode, methods]);

  const activeMetode = metode && methods.includes(metode) ? metode : undefined;

  const updateMetode = useCallback(
    (next: string | undefined) => {
      setMetode(next);

      const params = new URLSearchParams();
      if (query) params.set("q", query);
      if (next) params.set("metode", next);

      const qs = params.toString();
      router.replace(qs ? `${pathname}?${qs}` : pathname, { scroll: false });
    },
    [pathname, query, router]
  );

  return (
    <div className="mt-10">
      {showMethodFilter ? (
        <div className="flex flex-wrap items-center justify-center gap-2">
          <span className="mr-1 text-[10px] uppercase tracking-[0.16em] text-bone/35">
            Metode
          </span>
          <button
            type="button"
            className={chipClass(!activeMetode)}
            onClick={() => updateMetode(undefined)}
            aria-pressed={!activeMetode}
          >
            Alle
          </button>
          {methods.map((slug) => (
            <button
              key={slug}
              type="button"
              className={chipClass(activeMetode === slug)}
              onClick={() =>
                updateMetode(activeMetode === slug ? undefined : slug)
              }
              aria-pressed={activeMetode === slug}
            >
              {methodLabel(slug)}
            </button>
          ))}
        </div>
      ) : null}

      {showMethodFilter && activeMetode ? (
        <p className="mt-8 text-[12px] uppercase tracking-[0.14em] text-bone/40">
          Viser {filtered.length} af {recipes.length}
        </p>
      ) : null}

      <div
        className={`grid gap-10 text-left sm:grid-cols-2 lg:grid-cols-3 ${
          showMethodFilter ? (activeMetode ? "mt-8" : "mt-12") : "mt-2"
        }`}
      >
        {filtered.map((recipe) => (
          <RecipeCard
            key={`${recipe.category}-${recipe.slug}`}
            recipe={recipe}
          />
        ))}
      </div>
    </div>
  );
}
