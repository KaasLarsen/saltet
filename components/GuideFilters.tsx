"use client";

import Image from "next/image";
import Link from "next/link";
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
import {
  filterGuides,
  getTopTagsForGuides,
  hasActiveGuideFilters,
  type GuideFilterValues,
  type GuideListItem,
} from "@/lib/guide-filters";

interface GuideFiltersProps {
  guides: GuideListItem[];
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

function readFiltersFromLocation(): GuideFilterValues {
  if (typeof window === "undefined") return {};
  const params = new URLSearchParams(window.location.search);
  return {
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

export function GuideFilters({ guides }: GuideFiltersProps) {
  const router = useRouter();
  const pathname = usePathname();
  const searchId = useId();
  const searchRef = useRef<HTMLInputElement>(null);
  const searchWrapRef = useRef<HTMLDivElement>(null);
  const [filters, setFilters] = useState<GuideFilterValues>({});
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

  const topTags = useMemo(() => getTopTagsForGuides(guides), [guides]);
  const filtered = useMemo(
    () => filterGuides(guides, filters),
    [guides, filters]
  );
  const active = hasActiveGuideFilters(filters);

  const updateFilters = useCallback(
    (patch: Partial<GuideFilterValues> & { clear?: boolean }) => {
      setFilters((current) => {
        const next: GuideFilterValues = patch.clear
          ? {}
          : {
              ...current,
              ...patch,
            };

        const params = new URLSearchParams();
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
      {topTags.length > 0 ? (
        <div className="flex flex-col items-center gap-4">
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
        </div>
      ) : null}

      <div className="relative mt-8 flex items-center justify-center gap-1">
        <p className="text-[12px] uppercase tracking-[0.14em] text-bone/40">
          {active
            ? `Viser ${filtered.length} af ${guides.length}`
            : `${guides.length} guides`}
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
            aria-label="Søg i guides"
          >
            <LoopIcon className="h-4 w-4" />
          </button>
          {searchOpen ? (
            <div className="absolute left-1/2 top-full z-20 mt-1 w-[min(18rem,calc(100vw-2.5rem))] -translate-x-1/2 overflow-hidden rounded-xl border-2 border-bone/25 bg-ash shadow-lg shadow-black/30">
              <label htmlFor={searchId} className="sr-only">
                Søg i guides
              </label>
              <input
                ref={searchRef}
                id={searchId}
                type="search"
                value={filters.q ?? ""}
                onChange={(e) =>
                  updateFilters({ q: e.target.value || undefined })
                }
                placeholder="Søg i guides…"
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
            Ingen guides matcher {filters.q?.trim() ? "søgningen" : "filteret"}.
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
          {filtered.map((guide) => (
            <Link
              key={guide.slug}
              href={`/guides/${guide.slug}`}
              className="group block text-left"
            >
              <article>
                <div className="relative aspect-[16/10] overflow-hidden rounded-2xl border-2 border-bone/20 bg-ash shadow-[4px_4px_0_0_rgba(212,255,0,0.35)] transition-[transform,box-shadow,border-color] duration-300 group-hover:-translate-y-1 group-hover:border-herb group-hover:shadow-[6px_6px_0_0_rgba(212,255,0,0.7)]">
                  <Image
                    src={guide.image}
                    alt={guide.imageAlt}
                    fill
                    className="object-cover transition-transform duration-500 ease-out group-hover:scale-[1.05]"
                    sizes="(max-width: 768px) 100vw, 50vw"
                  />
                  <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-iron/55 via-transparent to-transparent" />
                </div>
                <h2 className="mt-4 font-serif text-xl uppercase leading-snug tracking-wide text-bone transition-colors group-hover:text-herb sm:text-2xl">
                  {guide.title}
                </h2>
                <p className="mt-2 line-clamp-3 text-sm leading-relaxed text-bone/55">
                  {guide.description}
                </p>
              </article>
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}
