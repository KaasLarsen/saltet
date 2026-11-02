"use client";

import { useState } from "react";
import { RecipeCard } from "@/components/RecipeCard";
import { LISTING_PAGE_SIZE } from "@/lib/listing";
import type { RecipeListItem } from "@/lib/types";

interface PaginatedRecipeGridProps {
  recipes: RecipeListItem[];
  pageSize?: number;
  className?: string;
}

export function PaginatedRecipeGrid({
  recipes,
  pageSize = LISTING_PAGE_SIZE,
  className = "mt-12 grid gap-10 text-left sm:grid-cols-2 lg:grid-cols-3",
}: PaginatedRecipeGridProps) {
  const [visibleCount, setVisibleCount] = useState(pageSize);
  const visible = recipes.slice(0, visibleCount);
  const remaining = recipes.length - visible.length;

  return (
    <>
      <div className={className}>
        {visible.map((recipe) => (
          <RecipeCard
            key={`${recipe.category}-${recipe.slug}`}
            recipe={recipe}
          />
        ))}
      </div>
      {remaining > 0 ? (
        <div className="mt-10 flex flex-col items-center gap-3">
          <p className="text-[12px] uppercase tracking-[0.14em] text-bone/40">
            Viser {visible.length} af {recipes.length}
          </p>
          <button
            type="button"
            onClick={() =>
              setVisibleCount((count) =>
                Math.min(count + pageSize, recipes.length)
              )
            }
            className="rounded-lg border-2 border-bone/25 px-5 py-2 text-[11px] font-bold uppercase tracking-[0.14em] text-bone/70 transition-colors hover:border-herb hover:text-herb"
          >
            Vis flere
            {remaining > pageSize ? ` (${pageSize})` : ` (${remaining})`}
          </button>
        </div>
      ) : null}
    </>
  );
}
