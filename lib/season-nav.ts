/** Client-safe sæson-meta (ingen fs / recipes-import). */

export interface SeasonWindow {
  /** Måned 1–12, dag 1–31. Kan wrappe over nytår (vinter). */
  startMonth: number;
  startDay: number;
  endMonth: number;
  endDay: number;
}

export interface SeasonNavItem {
  slug: string;
  name: string;
  /** Tag-slugs der knytter en opskrift til sæsonen. */
  matchTagSlugs: readonly string[];
  windows: readonly SeasonWindow[];
}

export const SEASON_NAV: readonly SeasonNavItem[] = [
  {
    slug: "foraar",
    name: "Forår",
    matchTagSlugs: ["foraar"],
    windows: [{ startMonth: 3, startDay: 1, endMonth: 5, endDay: 31 }],
  },
  {
    slug: "sommer",
    name: "Sommer",
    matchTagSlugs: ["sommer"],
    windows: [{ startMonth: 6, startDay: 1, endMonth: 8, endDay: 31 }],
  },
  {
    slug: "efteraar",
    name: "Efterår",
    matchTagSlugs: ["efteraar"],
    windows: [{ startMonth: 9, startDay: 1, endMonth: 11, endDay: 30 }],
  },
  {
    slug: "vinter",
    name: "Vinter",
    matchTagSlugs: ["vinter"],
    windows: [{ startMonth: 12, startDay: 1, endMonth: 2, endDay: 29 }],
  },
];

export type SeasonNavSlug = (typeof SEASON_NAV)[number]["slug"];

export const SEASON_NAV_LABELS: Record<string, string> = Object.fromEntries(
  SEASON_NAV.map((s) => [s.slug, s.name])
);

export function seasonNavLabel(slug: string): string {
  return SEASON_NAV_LABELS[slug] ?? slug;
}

export function getSeasonNav(slug: string): SeasonNavItem | undefined {
  return SEASON_NAV.find((s) => s.slug === slug);
}

export function isSeasonTagSlug(slug: string): boolean {
  return SEASON_NAV.some(
    (s) => s.slug === slug || s.matchTagSlugs.includes(slug)
  );
}

export function seasonForTagSlug(tagSlug: string): SeasonNavItem | undefined {
  return SEASON_NAV.find(
    (s) => s.slug === tagSlug || s.matchTagSlugs.includes(tagSlug)
  );
}

export function recipeMatchesSeason(
  tags: readonly string[],
  season: SeasonNavItem,
  slugify: (tag: string) => string
): boolean {
  return tags.some((tag) => season.matchTagSlugs.includes(slugify(tag)));
}

function dateKey(month: number, day: number): number {
  return month * 100 + day;
}

function inWindow(month: number, day: number, window: SeasonWindow): boolean {
  const now = dateKey(month, day);
  const start = dateKey(window.startMonth, window.startDay);
  const end = dateKey(window.endMonth, window.endDay);
  if (start <= end) return now >= start && now <= end;
  return now >= start || now <= end;
}

export function isSeasonActive(
  season: SeasonNavItem,
  date: Date = new Date()
): boolean {
  const month = date.getMonth() + 1;
  const day = date.getDate();
  return season.windows.some((window) => inWindow(month, day, window));
}

/** Aktuel meteorologisk sæson (altid én). */
export function getCurrentSeason(date: Date = new Date()): SeasonNavItem {
  const current = SEASON_NAV.find((s) => isSeasonActive(s, date));
  return current ?? SEASON_NAV[2]; // efterår som fallback
}

/**
 * Sæson i vinduet nu (status "now"), ellers den næste på kalenderen.
 * Bruges til “Nu” / “Næste” på /saeson.
 */
export function getHighlightedSeason(date: Date = new Date()): {
  season: SeasonNavItem;
  status: "now" | "next";
} {
  const current = SEASON_NAV.find((s) => isSeasonActive(s, date));
  if (current) return { season: current, status: "now" };

  const year = date.getFullYear();
  const now = date.getTime();
  let best: { season: SeasonNavItem; at: number } | undefined;

  for (const season of SEASON_NAV) {
    for (const offsetYear of [year, year + 1]) {
      for (const window of season.windows) {
        const start = new Date(
          offsetYear,
          window.startMonth - 1,
          window.startDay
        ).getTime();
        if (start >= now && (!best || start < best.at)) {
          best = { season, at: start };
        }
      }
    }
  }

  return { season: best?.season ?? SEASON_NAV[0], status: "next" };
}
