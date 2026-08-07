"use client";

import { useCallback, useMemo, type ReactNode } from "react";
import { usePathname, useRouter, useSearchParams } from "next/navigation";
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
}

function chipClass(active: boolean): string {
  return `border px-3 py-1 text-[11px] uppercase tracking-[0.12em] transition-colors ${
    active
      ? "border-bone/45 text-bone"
      : "border-bone/20 text-bone/50 hover:border-bone/45 hover:text-bone"
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

export function CategoryFilters({ recipes }: CategoryFiltersProps) {
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();

  const filters: CategoryFilterValues = useMemo(
    () => ({
      tid: parseTimeFilter(searchParams.get("tid") ?? undefined),
      svar: parseDifficultyFilter(searchParams.get("svar") ?? undefined),
      emne: searchParams.get("emne") ?? undefined,
    }),
    [searchParams]
  );

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
      const params = new URLSearchParams(searchParams.toString());

      if (patch.clear) {
        params.delete("tid");
        params.delete("svar");
        params.delete("emne");
      } else {
        if ("tid" in patch) {
          if (patch.tid == null) params.delete("tid");
          else params.set("tid", String(patch.tid));
        }
        if ("svar" in patch) {
          if (patch.svar == null) params.delete("svar");
          else params.set("svar", patch.svar);
        }
        if ("emne" in patch) {
          if (!patch.emne) params.delete("emne");
          else params.set("emne", patch.emne);
        }
      }

      const qs = params.toString();
      router.replace(qs ? `${pathname}?${qs}` : pathname, { scroll: false });
    },
    [pathname, router, searchParams]
  );

  return (
    <div className="mt-10">
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
                  tid: filters.tid === minutes ? undefined : (minutes as TimeFilter),
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

      <p className="mt-8 text-[12px] uppercase tracking-[0.14em] text-bone/40">
        {active
          ? `Viser ${filtered.length} af ${recipes.length}`
          : `${recipes.length} opskrifter`}
      </p>

      {filtered.length === 0 ? (
        <div className="mt-12">
          <p className="text-bone/50">
            Ingen opskrifter matcher filtrene.
          </p>
          <button
            type="button"
            onClick={() => updateFilters({ clear: true })}
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
