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
        className={`flex overflow-hidden rounded-2xl border-2 ${
          isHero
            ? "border-bone/40 bg-iron/70 shadow-[4px_4px_0_0_rgba(212,255,0,0.85)] backdrop-blur-sm"
            : "border-bone/25 bg-ash shadow-[3px_3px_0_0_rgba(255,92,57,0.55)]"
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
          className={`shrink-0 border-l-2 px-5 text-[12px] font-bold uppercase tracking-[0.14em] transition-colors ${
            isHero
              ? "border-bone/40 bg-herb text-iron hover:bg-bone"
              : "border-bone/25 bg-wood text-bone hover:bg-herb hover:text-iron"
          }`}
        >
          Søg
        </button>
      </div>
    </form>
  );
}
