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
  filterGrej,
  GREJ_TRACKS,
  hasActiveGrejFilters,
  isGrejTrack,
  type GrejFilterValues,
  type GrejListItem,
} from "@/lib/grej-filters";

interface GrejFiltersProps {
  items: GrejListItem[];
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

function readFiltersFromLocation(): GrejFilterValues {
  if (typeof window === "undefined") return {};
  const params = new URLSearchParams(window.location.search);
  const spor = params.get("spor") ?? undefined;
  return {
    spor: isGrejTrack(spor) ? spor : undefined,
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

export function GrejFilters({ items }: GrejFiltersProps) {
  const router = useRouter();
  const pathname = usePathname();
  const searchId = useId();
  const searchRef = useRef<HTMLInputElement>(null);
  const searchWrapRef = useRef<HTMLDivElement>(null);
  const [filters, setFilters] = useState<GrejFilterValues>({});
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

    function onPointerDown(e: MouseEvent) {
      const el = searchWrapRef.current;
      if (el && !el.contains(e.target as Node)) {
        setSearchOpen(false);
      }
    }

    function onKeyDown(e: KeyboardEvent) {
      if (e.key === "Escape") setSearchOpen(false);
    }

    document.addEventListener("mousedown", onPointerDown);
    document.addEventListener("keydown", onKeyDown);
    return () => {
      document.removeEventListener("mousedown", onPointerDown);
      document.removeEventListener("keydown", onKeyDown);
    };
  }, [searchOpen]);

  const filtered = useMemo(() => filterGrej(items, filters), [items, filters]);
  const active = hasActiveGrejFilters(filters);

  const updateFilters = useCallback(
    (patch: Partial<GrejFilterValues> & { clear?: boolean }) => {
      setFilters((current) => {
        const next: GrejFilterValues = patch.clear
          ? {}
          : {
              ...current,
              ...patch,
            };

        const params = new URLSearchParams();
        if (next.spor) params.set("spor", next.spor);
        if (next.q?.trim()) params.set("q", next.q.trim());

        const qs = params.toString();
        router.replace(qs ? `${pathname}?${qs}` : pathname, { scroll: false });
        return next;
      });
    },
    [pathname, router]
  );

  function clearAll() {
    setSearchOpen(false);
    updateFilters({ clear: true });
  }

  const queryActive = Boolean(filters.q?.trim());

  return (
    <div className="mt-10">
      <div className="flex flex-col items-center gap-4">
        <FilterGroup label="Spor">
          <button
            type="button"
            className={chipClass(!filters.spor)}
            onClick={() => updateFilters({ spor: undefined })}
            aria-pressed={!filters.spor}
          >
            Alle
          </button>
          {GREJ_TRACKS.map((track) => (
            <button
              key={track.slug}
              type="button"
              className={chipClass(filters.spor === track.slug)}
              onClick={() =>
                updateFilters({
                  spor: filters.spor === track.slug ? undefined : track.slug,
                })
              }
              aria-pressed={filters.spor === track.slug}
            >
              {track.label}
            </button>
          ))}
        </FilterGroup>
      </div>

      <div className="relative mt-8 flex items-center justify-center gap-1">
        <p className="text-[12px] uppercase tracking-[0.14em] text-bone/40">
          {active
            ? `Viser ${filtered.length} af ${items.length}`
            : `${items.length} grej-artikler`}
        </p>
        <div ref={searchWrapRef} className="relative">
          <button
            type="button"
            onClick={() => setSearchOpen((open) => !open)}
            className={`flex h-7 w-7 items-center justify-center rounded-md transition-colors ${
              searchOpen || queryActive
                ? "text-herb"
                : "text-bone/35 hover:text-bone"
            }`}
            aria-expanded={searchOpen}
            aria-controls={searchId}
            aria-label="Søg i grej"
          >
            <LoopIcon className="h-4 w-4" />
          </button>
          {searchOpen ? (
            <div className="absolute left-1/2 top-full z-20 mt-1 w-[min(18rem,calc(100vw-2.5rem))] -translate-x-1/2 overflow-hidden rounded-xl border-2 border-bone/25 bg-ash shadow-lg shadow-black/30">
              <label htmlFor={searchId} className="sr-only">
                Søg i grej
              </label>
              <input
                ref={searchRef}
                id={searchId}
                type="search"
                value={filters.q ?? ""}
                onChange={(e) =>
                  updateFilters({ q: e.target.value || undefined })
                }
                placeholder="Søg i grej…"
                className="w-full bg-transparent px-3 py-2.5 text-sm text-bone outline-none placeholder:text-smoke"
                autoComplete="off"
              />
            </div>
          ) : null}
        </div>
      </div>

      {filtered.length === 0 ? (
        <div className="mt-12">
          <p className="text-bone/50">
            Intet grej matcher {filters.q?.trim() ? "søgningen" : "sporet"}.
          </p>
          <button
            type="button"
            onClick={clearAll}
            className="mt-4 text-[12px] uppercase tracking-[0.14em] text-bone/55 transition-colors hover:text-bone"
          >
            Nulstil filtre
          </button>
        </div>
      ) : (
        <div className="mt-12 grid gap-10 text-left sm:grid-cols-2">
          {filtered.map((item) => (
            <GuideCard
              key={item.slug}
              href={`/grej/${item.slug}`}
              guide={item}
            />
          ))}
        </div>
      )}
    </div>
  );
}
