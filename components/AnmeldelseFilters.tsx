"use client";

import {
  useCallback,
  useEffect,
  useId,
  useMemo,
  useRef,
  useState,
  type ReactNode,
} from "react";
import { usePathname, useRouter } from "next/navigation";
import { GuideCard } from "@/components/GuideCard";
import {
  ANMELDELSE_SERIES,
  filterAnmeldelser,
  hasActiveAnmeldelseFilters,
  isAnmeldelseSeries,
  type AnmeldelseFilterValues,
  type AnmeldelseListItem,
} from "@/lib/anmeldelse-filters";

interface AnmeldelseFiltersProps {
  items: AnmeldelseListItem[];
}

function chipClass(active: boolean): string {
  return `rounded-lg border-2 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.12em] transition-colors ${
    active
      ? "border-herb bg-herb text-iron"
      : "border-bone/25 text-bone/55 hover:border-herb hover:text-herb"
  }`;
}

function FilterGroup({
  label,
  children,
}: {
  label: string;
  children: ReactNode;
}) {
  return (
    <div className="flex flex-wrap items-center justify-center gap-2">
      <span className="mr-1 text-[10px] uppercase tracking-[0.16em] text-bone/35">
        {label}
      </span>
      {children}
    </div>
  );
}

function readFiltersFromLocation(): AnmeldelseFilterValues {
  if (typeof window === "undefined") return {};
  const params = new URLSearchParams(window.location.search);
  const serie = params.get("serie") ?? undefined;
  return {
    serie: isAnmeldelseSeries(serie) ? serie : undefined,
    q: params.get("q") ?? undefined,
  };
}

function LoopIcon({ className }: { className?: string }) {
  return (
    <svg
      aria-hidden
      viewBox="0 0 24 24"
      className={className}
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="11" cy="11" r="6.5" />
      <path d="M16 16 L21 21" />
    </svg>
  );
}

export function AnmeldelseFilters({ items }: AnmeldelseFiltersProps) {
  const router = useRouter();
  const pathname = usePathname();
  const searchId = useId();
  const searchRef = useRef<HTMLInputElement>(null);
  const searchWrapRef = useRef<HTMLDivElement>(null);
  const [filters, setFilters] = useState<AnmeldelseFilterValues>({});
  const [searchOpen, setSearchOpen] = useState(false);

  useEffect(() => {
    const next = readFiltersFromLocation();
    setFilters(next);
    if (next.q?.trim()) setSearchOpen(true);
  }, []);

  useEffect(() => {
    if (searchOpen) searchRef.current?.focus();
  }, [searchOpen]);

  useEffect(() => {
    if (!searchOpen) return;
    function onPointerDown(event: PointerEvent) {
      if (
        searchWrapRef.current &&
        !searchWrapRef.current.contains(event.target as Node)
      ) {
        if (!searchRef.current?.value.trim()) setSearchOpen(false);
      }
    }
    document.addEventListener("pointerdown", onPointerDown);
    return () => document.removeEventListener("pointerdown", onPointerDown);
  }, [searchOpen]);

  const filtered = useMemo(
    () => filterAnmeldelser(items, filters),
    [items, filters]
  );

  const updateFilters = useCallback(
    (next: AnmeldelseFilterValues) => {
      setFilters(next);
      const params = new URLSearchParams();
      if (next.serie) params.set("serie", next.serie);
      if (next.q?.trim()) params.set("q", next.q.trim());
      const qs = params.toString();
      router.replace(qs ? `${pathname}?${qs}` : pathname, { scroll: false });
    },
    [pathname, router]
  );

  const active = hasActiveAnmeldelseFilters(filters);

  return (
    <div className="mt-10">
      <div className="flex flex-col items-center gap-4">
        <FilterGroup label="Serie">
          <button
            type="button"
            className={chipClass(!filters.serie)}
            onClick={() => updateFilters({ ...filters, serie: undefined })}
            aria-pressed={!filters.serie}
          >
            Alle
          </button>
          {ANMELDELSE_SERIES.map((series) => (
            <button
              key={series.slug}
              type="button"
              className={chipClass(filters.serie === series.slug)}
              onClick={() =>
                updateFilters({
                  ...filters,
                  serie:
                    filters.serie === series.slug ? undefined : series.slug,
                })
              }
              aria-pressed={filters.serie === series.slug}
            >
              {series.label}
            </button>
          ))}
        </FilterGroup>

        <div ref={searchWrapRef} className="flex items-center gap-2">
          {searchOpen ? (
            <label htmlFor={searchId} className="sr-only">
              Søg i anmeldelser
            </label>
          ) : null}
          {searchOpen ? (
            <input
              ref={searchRef}
              id={searchId}
              type="search"
              value={filters.q ?? ""}
              onChange={(event) =>
                updateFilters({ ...filters, q: event.target.value })
              }
              placeholder="Søg model, brand…"
              className="w-56 rounded-lg border-2 border-bone/25 bg-iron px-3 py-1.5 text-sm text-bone placeholder:text-bone/35 focus:border-herb focus:outline-none"
            />
          ) : (
            <button
              type="button"
              className={chipClass(Boolean(filters.q?.trim()))}
              onClick={() => setSearchOpen(true)}
              aria-label="Åbn søgning"
            >
              <LoopIcon className="h-3.5 w-3.5" />
            </button>
          )}
          {active ? (
            <button
              type="button"
              className={chipClass(false)}
              onClick={() => {
                setSearchOpen(false);
                updateFilters({});
              }}
            >
              Nulstil
            </button>
          ) : null}
        </div>
      </div>

      <p className="mt-6 text-center text-[11px] font-bold uppercase tracking-[0.14em] text-bone/40">
        {filtered.length === 1
          ? "1 anmeldelse"
          : `${filtered.length} anmeldelser`}
      </p>

      <div className="mt-10 grid gap-10 text-left sm:grid-cols-2">
        {filtered.map((item) => (
          <GuideCard
            key={item.slug}
            href={`/anmeldelser/${item.slug}`}
            guide={item}
            rating={item.rating}
            ratingCount={item.ratingCount}
            productShot
          />
        ))}
      </div>

      {filtered.length === 0 ? (
        <p className="mt-10 text-center text-bone/50">
          Ingen anmeldelser matchede filtrene.
        </p>
      ) : null}
    </div>
  );
}
