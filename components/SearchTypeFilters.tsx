"use client";

import { useCallback, useEffect, useState } from "react";
import { usePathname, useRouter } from "next/navigation";

export const SEARCH_TYPES = ["opskrifter", "guides", "grej"] as const;
export type SearchType = (typeof SEARCH_TYPES)[number];

const TYPE_LABELS: Record<SearchType, string> = {
  opskrifter: "Opskrifter",
  guides: "Guides",
  grej: "Grej",
};

export function isSearchType(value: string | undefined): value is SearchType {
  return (
    value === "opskrifter" || value === "guides" || value === "grej"
  );
}

interface SearchTypeFiltersProps {
  query: string;
  available: SearchType[];
  initialType?: SearchType;
}

function chipClass(active: boolean): string {
  return `rounded-lg border-2 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.12em] transition-colors ${
    active
      ? "border-herb bg-herb text-iron"
      : "border-bone/25 text-bone/55 hover:border-herb hover:text-herb"
  }`;
}

function readTypeFromLocation(): SearchType | undefined {
  if (typeof window === "undefined") return undefined;
  const value =
    new URLSearchParams(window.location.search).get("type") ?? undefined;
  return isSearchType(value) ? value : undefined;
}

export function SearchTypeFilters({
  query,
  available,
  initialType,
}: SearchTypeFiltersProps) {
  const router = useRouter();
  const pathname = usePathname();
  const [type, setType] = useState<SearchType | undefined>(initialType);

  useEffect(() => {
    setType(readTypeFromLocation() ?? initialType);
  }, [initialType]);

  const activeType =
    type && available.includes(type) ? type : undefined;

  const updateType = useCallback(
    (next: SearchType | undefined) => {
      setType(next);

      const params = new URLSearchParams(window.location.search);
      if (query) params.set("q", query);
      else params.delete("q");

      if (next) params.set("type", next);
      else params.delete("type");

      // Metode only applies to opskrifter — clear when filtering elsewhere
      if (next && next !== "opskrifter") {
        params.delete("metode");
      }

      const qs = params.toString();
      router.replace(qs ? `${pathname}?${qs}` : pathname, { scroll: false });
    },
    [pathname, query, router]
  );

  if (available.length < 2) return null;

  return (
    <div className="mt-8 flex flex-wrap items-center justify-center gap-2">
      <span className="mr-1 text-[10px] uppercase tracking-[0.16em] text-bone/35">
        Type
      </span>
      <button
        type="button"
        className={chipClass(!activeType)}
        onClick={() => updateType(undefined)}
        aria-pressed={!activeType}
      >
        Alle
      </button>
      {available.map((slug) => (
        <button
          key={slug}
          type="button"
          className={chipClass(activeType === slug)}
          onClick={() =>
            updateType(activeType === slug ? undefined : slug)
          }
          aria-pressed={activeType === slug}
        >
          {TYPE_LABELS[slug]}
        </button>
      ))}
    </div>
  );
}
