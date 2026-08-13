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
import { RecipeCard } from "@/components/RecipeCard";
import { difficultyLabel } from "@/lib/format";
import {
  TIME_FILTERS,
  filterRecipes,
  getAvailableDifficulties,
  getTopTagsForRecipes,
  hasActiveFilters,
  parseDifficultyFilter,
  parseTimeFilter,
  type CategoryFilterValues,
  type TimeFilter,
} from "@/lib/recipe-filters";
import type { Difficulty, RecipeFrontmatter } from "@/lib/types";

interface CategoryFiltersProps {
  recipes: RecipeFrontmatter[];
  showFilters?: boolean;
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

function readFiltersFromLocation(): CategoryFilterValues {
  if (typeof window === "undefined") return {};
  const params = new URLSearchParams(window.location.search);
  return {
    tid: parseTimeFilter(params.get("tid") ?? undefined),
    svar: parseDifficultyFilter(params.get("svar") ?? undefined),
    emne: params.get("emne") ?? undefined,
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

export function CategoryFilters({
  recipes,
  showFilters = true,
}: CategoryFiltersProps) {
  const router = useRouter();
  const pathname = usePathname();
  const searchId = useId();
  const searchRef = useRef<HTMLInputElement>(null);
  const searchWrapRef = useRef<HTMLDivElement>(null);
  const [filters, setFilters] = useState<CategoryFilterValues>({});
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

  const difficulties = useMemo(
    () => getAvailableDifficulties(recipes),
    [recipes]
  );
  const topTags = useMemo(() => getTopTagsForRecipes(recipes), [recipes]);
  const filtered = useMemo(
    () => filterRecipes(recipes, filters),
    [recipes, filters]
  );
  const active = hasActiveFilters(filters);

  const updateFilters = useCallback(
    (patch: Partial<CategoryFilterValues> & { clear?: boolean }) => {
      setFilters((current) => {
        const next: CategoryFilterValues = patch.clear
          ? {}
          : {
              ...current,
              ...patch,
            };

        const params = new URLSearchParams();
        if (next.tid != null) params.set("tid", String(next.tid));
        if (next.svar) params.set("svar", next.svar);
        if (next.emne) params.set("emne", next.emne);
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
      {showFilters ? (
        <div className="flex flex-col items-center gap-4">
        <FilterGroup label="Tid">
          <button
            type="button"
            className={chipClass(filters.tid == null)}
            onClick={() => updateFilters({ tid: undefined })}
            aria-pressed={filters.tid == null}
          >
            Alle
          </button>
          {TIME_FILTERS.map((minutes) => (
            <button
              key={minutes}
              type="button"
              className={chipClass(filters.tid === minutes)}
              onClick={() =>
                updateFilters({
                  tid:
                    filters.tid === minutes
                      ? undefined
                      : (minutes as TimeFilter),
                })
              }
              aria-pressed={filters.tid === minutes}
            >
              Under {minutes} min
            </button>
          ))}
        </FilterGroup>

        {difficulties.length > 1 ? (
          <FilterGroup label="Sværhedsgrad">
            <button
              type="button"
              className={chipClass(filters.svar == null)}
              onClick={() => updateFilters({ svar: undefined })}
              aria-pressed={filters.svar == null}
            >
              Alle
            </button>
            {difficulties.map((difficulty) => (
              <button
                key={difficulty}
                type="button"
                className={chipClass(filters.svar === difficulty)}
                onClick={() =>
                  updateFilters({
                    svar:
                      filters.svar === difficulty
                        ? undefined
                        : (difficulty as Difficulty),
                  })
                }
                aria-pressed={filters.svar === difficulty}
              >
                {difficultyLabel(difficulty)}
              </button>
            ))}
          </FilterGroup>
        ) : null}

        {topTags.length > 0 ? (
          <FilterGroup label="Emne">
            <button
              type="button"
              className={chipClass(!filters.emne)}
              onClick={() => updateFilters({ emne: undefined })}
              aria-pressed={!filters.emne}
            >
              Alle
            </button>
            {topTags.map((tag) => (
              <button
                key={tag.slug}
                type="button"
                className={chipClass(filters.emne === tag.slug)}
                onClick={() =>
                  updateFilters({
                    emne: filters.emne === tag.slug ? undefined : tag.slug,
                  })
                }
                aria-pressed={filters.emne === tag.slug}
              >
                {tag.label}
              </button>
            ))}
          </FilterGroup>
        ) : null}
        </div>
      ) : null}

      <div className="relative mt-8 flex items-center justify-center gap-1">
        <p className="text-[12px] uppercase tracking-[0.14em] text-bone/40">
          {active
            ? `Viser ${filtered.length} af ${recipes.length}`
            : `${recipes.length} opskrifter`}
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
            aria-label="Søg i kategorien"
          >
            <LoopIcon className="h-4 w-4" />
          </button>
          {searchOpen ? (
            <div className="absolute left-1/2 top-full z-20 mt-1 w-[min(18rem,calc(100vw-2.5rem))] -translate-x-1/2 overflow-hidden rounded-xl border-2 border-bone/25 bg-ash shadow-lg shadow-black/30">
              <label htmlFor={searchId} className="sr-only">
                Søg i kategorien
              </label>
              <input
                ref={searchRef}
                id={searchId}
                type="search"
                value={filters.q ?? ""}
                onChange={(e) =>
                  updateFilters({ q: e.target.value || undefined })
                }
                placeholder="Søg i kategorien…"
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
            Ingen opskrifter matcher {filters.q?.trim() ? "søgningen" : "filtrene"}.
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
        <div className="mt-12 grid gap-10 text-left sm:grid-cols-2 lg:grid-cols-3">
          {filtered.map((recipe) => (
            <RecipeCard key={recipe.slug} recipe={recipe} />
          ))}
        </div>
      )}
    </div>
  );
}
