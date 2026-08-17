/** Client-safe højtid-meta (ingen fs / recipes-import). */

export interface HolidayWindow {
  /** Måned 1–12, dag 1–31. Kan wrappe over nytår. */
  startMonth: number;
  startDay: number;
  endMonth: number;
  endDay: number;
}

export interface HolidayNavItem {
  slug: string;
  name: string;
  /** Tag-slugs der knytter en opskrift til højtiden. */
  matchTagSlugs: readonly string[];
  windows: readonly HolidayWindow[];
}

export const HOLIDAY_NAV: readonly HolidayNavItem[] = [
  {
    slug: "jul",
    name: "Jul",
    matchTagSlugs: ["jul", "julegaas", "juleand", "juleroedkaal"],
    windows: [{ startMonth: 11, startDay: 16, endMonth: 12, endDay: 26 }],
  },
  {
    slug: "nytaar",
    name: "Nytår",
    matchTagSlugs: ["nytaar"],
    windows: [
      { startMonth: 12, startDay: 27, endMonth: 12, endDay: 31 },
      { startMonth: 1, startDay: 1, endMonth: 1, endDay: 7 },
    ],
  },
  {
    slug: "paaske",
    name: "Påske",
    matchTagSlugs: ["paaske"],
    windows: [],
  },
  {
    slug: "mortensaften",
    name: "Mortensaften",
    matchTagSlugs: ["mortensaften"],
    windows: [{ startMonth: 11, startDay: 1, endMonth: 11, endDay: 15 }],
  },
];

export type HolidayNavSlug = (typeof HOLIDAY_NAV)[number]["slug"];

export const HOLIDAY_NAV_LABELS: Record<string, string> = Object.fromEntries(
  HOLIDAY_NAV.map((h) => [h.slug, h.name])
);

export function holidayNavLabel(slug: string): string {
  return HOLIDAY_NAV_LABELS[slug] ?? slug;
}

export function getHolidayNav(slug: string): HolidayNavItem | undefined {
  return HOLIDAY_NAV.find((h) => h.slug === slug);
}

export function isHolidayTagSlug(slug: string): boolean {
  return HOLIDAY_NAV.some(
    (h) => h.slug === slug || h.matchTagSlugs.includes(slug)
  );
}

export function holidayForTagSlug(tagSlug: string): HolidayNavItem | undefined {
  return HOLIDAY_NAV.find(
    (h) => h.slug === tagSlug || h.matchTagSlugs.includes(tagSlug)
  );
}

export function recipeMatchesHoliday(
  tags: readonly string[],
  holiday: HolidayNavItem,
  slugify: (tag: string) => string
): boolean {
  return tags.some((tag) => holiday.matchTagSlugs.includes(slugify(tag)));
}

/** Vestlig påske (gregoriansk) — returnerer dato ved midnat lokal tid. */
export function easterSunday(year: number): Date {
  const a = year % 19;
  const b = Math.floor(year / 100);
  const c = year % 100;
  const d = Math.floor(b / 4);
  const e = b % 4;
  const f = Math.floor((b + 8) / 25);
  const g = Math.floor((b - f + 1) / 16);
  const h = (19 * a + b - d - g + 15) % 30;
  const i = Math.floor(c / 4);
  const k = c % 4;
  const l = (32 + 2 * e + 2 * i - h - k) % 7;
  const m = Math.floor((a + 11 * h + 22 * l) / 451);
  const month = Math.floor((h + l - 7 * m + 114) / 31);
  const day = ((h + l - 7 * m + 114) % 31) + 1;
  return new Date(year, month - 1, day);
}

function dateKey(month: number, day: number): number {
  return month * 100 + day;
}

function inWindow(month: number, day: number, window: HolidayWindow): boolean {
  const now = dateKey(month, day);
  const start = dateKey(window.startMonth, window.startDay);
  const end = dateKey(window.endMonth, window.endDay);
  if (start <= end) return now >= start && now <= end;
  return now >= start || now <= end;
}

function paaskeWindow(year: number): HolidayWindow {
  const easter = easterSunday(year);
  const start = new Date(easter);
  start.setDate(easter.getDate() - 21);
  const end = new Date(easter);
  end.setDate(easter.getDate() + 7);
  return {
    startMonth: start.getMonth() + 1,
    startDay: start.getDate(),
    endMonth: end.getMonth() + 1,
    endDay: end.getDate(),
  };
}

function windowsForHoliday(holiday: HolidayNavItem, year: number): HolidayWindow[] {
  if (holiday.slug === "paaske") return [paaskeWindow(year)];
  return [...holiday.windows];
}

export function isHolidayInSeason(
  holiday: HolidayNavItem,
  date: Date = new Date()
): boolean {
  const month = date.getMonth() + 1;
  const day = date.getDate();
  return windowsForHoliday(holiday, date.getFullYear()).some((window) =>
    inWindow(month, day, window)
  );
}

/**
 * Højtid i vinduet nu, ellers den næste på kalenderen.
 * Bruges til “Nu” / “Næste” på forsiden.
 */
export function getHighlightedHoliday(date: Date = new Date()): {
  holiday: HolidayNavItem;
  status: "now" | "next";
} {
  const current = HOLIDAY_NAV.find((h) => isHolidayInSeason(h, date));
  if (current) return { holiday: current, status: "now" };

  const year = date.getFullYear();
  const now = date.getTime();
  let best: { holiday: HolidayNavItem; at: number } | undefined;

  for (const holiday of HOLIDAY_NAV) {
    for (const offsetYear of [year, year + 1]) {
      for (const window of windowsForHoliday(holiday, offsetYear)) {
        const start = new Date(
          offsetYear,
          window.startMonth - 1,
          window.startDay
        ).getTime();
        if (start >= now && (!best || start < best.at)) {
          best = { holiday, at: start };
        }
      }
    }
  }

  return { holiday: best?.holiday ?? HOLIDAY_NAV[0], status: "next" };
}
