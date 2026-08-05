"use client";

import { FormEvent, useState } from "react";
import { useRouter } from "next/navigation";

interface SearchFormProps {
  initialQuery?: string;
  variant?: "hero" | "page";
  className?: string;
}

export function SearchForm({
  initialQuery = "",
  variant = "hero",
  className = "",
}: SearchFormProps) {
  const router = useRouter();
  const [query, setQuery] = useState(initialQuery);

  function onSubmit(e: FormEvent) {
    e.preventDefault();
    const q = query.trim();
    router.push(q ? `/opskrifter?q=${encodeURIComponent(q)}` : "/opskrifter");
  }

  const isHero = variant === "hero";

  return (
    <form onSubmit={onSubmit} className={`w-full ${className}`} role="search">
      <label htmlFor="recipe-search" className="sr-only">
        Søg efter opskrift
      </label>
      <div
        className={`flex border ${
          isHero
            ? "border-bone/35 bg-iron/55 backdrop-blur-sm"
            : "border-bone/20 bg-ash"
        }`}
      >
        <input
          id="recipe-search"
          type="search"
          name="q"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Søg efter en opskrift…"
          className={`min-w-0 flex-1 bg-transparent px-4 py-3.5 text-bone outline-none placeholder:text-smoke ${
            isHero ? "text-base md:text-lg" : "text-sm"
          }`}
          autoComplete="off"
        />
        <button
          type="submit"
          className={`shrink-0 border-l px-5 text-[11px] uppercase tracking-[0.16em] transition-colors ${
            isHero
              ? "border-bone/35 text-bone hover:bg-bone hover:text-iron"
              : "border-bone/20 text-bone/80 hover:bg-bone hover:text-iron"
          }`}
        >
          Søg
        </button>
      </div>
    </form>
  );
}
