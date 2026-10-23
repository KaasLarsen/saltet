"use client";

import { useCallback, useEffect, useState } from "react";
import { usePathname, useRouter } from "next/navigation";
import { categoryNavLabel } from "@/lib/category-nav";

interface SearchMethodFiltersProps {
  query: string;
  methods: string[];
  initialMetode?: string;
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

export function SearchMethodFilters({
  query,
  methods,
  initialMetode,
}: SearchMethodFiltersProps) {
  const router = useRouter();
  const pathname = usePathname();
  const [metode, setMetode] = useState<string | undefined>(initialMetode);

  useEffect(() => {
    const fromUrl = readMetodeFromLocation();
    setMetode(
      fromUrl && methods.includes(fromUrl)
        ? fromUrl
        : initialMetode && methods.includes(initialMetode)
          ? initialMetode
          : undefined
    );
  }, [initialMetode, methods]);

  const activeMetode =
    metode && methods.includes(metode) ? metode : undefined;

  const updateMetode = useCallback(
    (next: string | undefined) => {
      setMetode(next);

      const params = new URLSearchParams(window.location.search);
      if (query) params.set("q", query);
      else params.delete("q");

      if (next) params.set("metode", next);
      else params.delete("metode");

      const qs = params.toString();
      router.replace(qs ? `${pathname}?${qs}` : pathname, { scroll: false });
    },
    [pathname, query, router]
  );

  if (methods.length < 2) return null;

  return (
    <div className="mt-10 flex flex-wrap items-center justify-center gap-2">
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
          {categoryNavLabel(slug)}
        </button>
      ))}
    </div>
  );
}
