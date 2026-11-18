"use client";

import Link from "next/link";
import { useEffect, useId, useRef, useState } from "react";
import { usePathname, useSearchParams } from "next/navigation";
import { SaltShakerMark } from "@/components/SaltShakerMark";
import { ANMELDELSE_NAV } from "@/lib/anmeldelse-nav";
import { CATEGORY_NAV } from "@/lib/category-nav";
import { FEJLFINDING_GEAR_NAV } from "@/lib/fejlfinding-nav";
import { GREJ_CATEGORY_NAV } from "@/lib/grej-categories";
import { GUIDE_CATEGORY_NAV } from "@/lib/guide-category-nav";
import { HOLIDAY_NAV } from "@/lib/holiday-nav";
import { SEASON_NAV } from "@/lib/season-nav";
import { TOPIC_NAV } from "@/lib/topic-nav";

type NavChild = { href: string; label: string };

type NavGroup = {
  id: string;
  label: string;
  /** Hub-link øverst i gruppen (fx «Alle emner»). */
  hubHref?: string;
  hubLabel?: string;
  children: NavChild[];
};

type NavItem = {
  href: string;
  label: string;
  children?: NavChild[];
  groups?: NavGroup[];
  /** Path-prefixes der også markerer sektionen aktiv (ud over href). */
  activePrefixes?: string[];
};

const OPSKRIFTER_PREFIXES = [
  "/opskrifter",
  "/emner",
  "/grej",
  "/saeson",
  "/hoejtider",
] as const;

const sosNav: NavItem = {
  href: "/fejlfinding",
  label: "SOS",
  children: [
    { href: "/fejlfinding", label: "Alle fejlfindinger" },
    ...FEJLFINDING_GEAR_NAV.map((g) => ({
      href: `/fejlfinding?grej=${g.slug}`,
      label: g.name,
    })),
  ],
};

const navItems: NavItem[] = [
  {
    href: "/opskrifter",
    label: "Opskrifter",
    activePrefixes: [...OPSKRIFTER_PREFIXES],
    children: [{ href: "/opskrifter", label: "Alle opskrifter" }],
    groups: [
      {
        id: "kategorier",
        label: "Kategorier",
        children: CATEGORY_NAV.map((c) => ({
          href: `/opskrifter/${c.slug}`,
          label: c.name,
        })),
      },
      {
        id: "emner",
        label: "Emner",
        hubHref: "/emner",
        hubLabel: "Alle emner",
        children: TOPIC_NAV.map((t) => ({
          href: `/emner/${t.slug}`,
          label: t.name,
        })),
      },
      {
        id: "grej",
        label: "Grej",
        hubHref: "/grej",
        hubLabel: "Alt grej",
        children: GREJ_CATEGORY_NAV.map((g) => ({
          href: `/grej?kategori=${g.slug}`,
          label: g.name,
        })),
      },
      {
        id: "saeson",
        label: "Sæson",
        hubHref: "/saeson",
        hubLabel: "Alle sæsoner",
        children: SEASON_NAV.map((s) => ({
          href: `/saeson/${s.slug}`,
          label: s.name,
        })),
      },
      {
        id: "hoejtider",
        label: "Højtider",
        hubHref: "/hoejtider",
        hubLabel: "Alle højtider",
        children: HOLIDAY_NAV.map((h) => ({
          href: `/hoejtider/${h.slug}`,
          label: h.name,
        })),
      },
    ],
  },
  {
    href: "/anmeldelser",
    label: "Anmeldelser",
    children: [
      { href: "/anmeldelser", label: "Alle anmeldelser" },
      ...ANMELDELSE_NAV.map((a) => ({
        href: `/anmeldelser?serie=${a.slug}`,
        label: a.name,
      })),
    ],
  },
  {
    href: "/guides",
    label: "Guides",
    children: [
      { href: "/guides", label: "Alle guides" },
      ...GUIDE_CATEGORY_NAV.map((g) => ({
        href: `/guides?emne=${g.slug}`,
        label: g.name,
      })),
    ],
  },
];

function pathIsActive(pathname: string, href: string, exact = false): boolean {
  const pathOnly = href.split("?")[0] ?? href;
  if (exact) return pathname === pathOnly;
  return pathname === pathOnly || pathname.startsWith(`${pathOnly}/`);
}

function sectionIsActive(pathname: string, item: NavItem): boolean {
  if (item.activePrefixes?.length) {
    return item.activePrefixes.some((prefix) => pathIsActive(pathname, prefix));
  }
  return pathIsActive(pathname, item.href);
}

function navChildIsActive(
  pathname: string,
  searchParams: URLSearchParams,
  href: string,
  sectionHref: string
): boolean {
  const [pathOnly, query = ""] = href.split("?");
  if (!pathOnly) return false;

  if (href === sectionHref) {
    if (pathname !== pathOnly) return false;
    // «Alle …» er aktiv når index er åben uden kategori-query.
    return (
      !searchParams.get("serie") &&
      !searchParams.get("emne") &&
      !searchParams.get("kategori") &&
      !searchParams.get("grej")
    );
  }

  if (query) {
    if (pathname !== pathOnly) return false;
    const wanted = new URLSearchParams(query);
    for (const [key, value] of wanted) {
      if (searchParams.get(key) !== value) return false;
    }
    return true;
  }

  return pathIsActive(pathname, href);
}

function dropdownItemClass(active: boolean) {
  return `block px-3.5 py-2 text-[12px] font-semibold uppercase tracking-[0.12em] transition-colors ${
    active
      ? "bg-herb/20 text-herb"
      : "text-bone/70 hover:bg-bone/10 hover:text-bone"
  }`;
}

function Chevron({ open }: { open: boolean }) {
  return (
    <svg
      aria-hidden
      viewBox="0 0 12 12"
      className={`h-2.5 w-2.5 shrink-0 transition-transform duration-200 ${
        open ? "rotate-180" : ""
      }`}
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M2.5 4.5 L6 8 L9.5 4.5" />
    </svg>
  );
}

function closeDesktopMenus(
  setDesktopOpenHref: (value: string | null) => void,
  setDesktopGroupId: (value: string | null) => void
) {
  setDesktopOpenHref(null);
  setDesktopGroupId(null);
}

export function Header() {
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const menuId = useId();
  const desktopNavRef = useRef<HTMLElement>(null);
  const menuScrollRef = useRef<HTMLDivElement>(null);
  const [openedPath, setOpenedPath] = useState<string | null>(null);
  const [desktopOpenHref, setDesktopOpenHref] = useState<string | null>(null);
  const [desktopGroupId, setDesktopGroupId] = useState<string | null>(null);
  const [mobileOpen, setMobileOpen] = useState<Record<string, boolean>>({});
  const [mobileGroupOpen, setMobileGroupOpen] = useState<
    Record<string, boolean>
  >({});
  const [menuPath, setMenuPath] = useState(pathname);
  if (pathname !== menuPath) {
    setMenuPath(pathname);
    setOpenedPath(null);
    setDesktopOpenHref(null);
    setDesktopGroupId(null);
  }
  const open = openedPath === pathname;

  useEffect(() => {
    if (!open) return;

    const html = document.documentElement;
    const { body } = document;
    const scrollY = window.scrollY;
    const previous = {
      htmlOverflow: html.style.overflow,
      htmlOverscroll: html.style.overscrollBehavior,
      bodyOverflow: body.style.overflow,
      bodyPosition: body.style.position,
      bodyTop: body.style.top,
      bodyLeft: body.style.left,
      bodyRight: body.style.right,
      bodyWidth: body.style.width,
    };

    html.style.overflow = "hidden";
    html.style.overscrollBehavior = "none";
    body.style.overflow = "hidden";
    body.style.position = "fixed";
    body.style.top = `-${scrollY}px`;
    body.style.left = "0";
    body.style.right = "0";
    body.style.width = "100%";

    function onTouchMove(e: TouchEvent) {
      const panel = menuScrollRef.current;
      if (panel && panel.contains(e.target as Node)) return;
      e.preventDefault();
    }

    document.addEventListener("touchmove", onTouchMove, { passive: false });

    return () => {
      document.removeEventListener("touchmove", onTouchMove);
      html.style.overflow = previous.htmlOverflow;
      html.style.overscrollBehavior = previous.htmlOverscroll;
      body.style.overflow = previous.bodyOverflow;
      body.style.position = previous.bodyPosition;
      body.style.top = previous.bodyTop;
      body.style.left = previous.bodyLeft;
      body.style.right = previous.bodyRight;
      body.style.width = previous.bodyWidth;
      window.scrollTo(0, scrollY);
    };
  }, [open]);

  useEffect(() => {
    if (!open && !desktopOpenHref) return;

    function onKeyDown(e: KeyboardEvent) {
      if (e.key === "Escape") {
        setOpenedPath(null);
        setDesktopOpenHref(null);
        setDesktopGroupId(null);
      }
    }

    document.addEventListener("keydown", onKeyDown);
    return () => document.removeEventListener("keydown", onKeyDown);
  }, [open, desktopOpenHref]);

  useEffect(() => {
    if (!desktopOpenHref) return;

    function onPointerDown(e: MouseEvent) {
      const el = desktopNavRef.current;
      if (el && !el.contains(e.target as Node)) {
        setDesktopOpenHref(null);
        setDesktopGroupId(null);
      }
    }

    document.addEventListener("click", onPointerDown);
    return () => document.removeEventListener("click", onPointerDown);
  }, [desktopOpenHref]);

  function closeMenu() {
    setOpenedPath(null);
  }

  function toggleMenu() {
    setOpenedPath((current) => (current === pathname ? null : pathname));
  }

  function handleLogoClick(event: React.MouseEvent<HTMLAnchorElement>) {
    setOpenedPath(null);
    setDesktopOpenHref(null);
    setDesktopGroupId(null);
    if (pathname === "/") {
      event.preventDefault();
      window.scrollTo({ top: 0, behavior: "smooth" });
    }
  }

  function toggleDesktopItem(href: string) {
    setDesktopGroupId(null);
    setDesktopOpenHref((current) => (current === href ? null : href));
  }

  function renderDesktopDropdown(item: NavItem, isSos = false) {
    const sectionActive = sectionIsActive(pathname, item);
    const dropdownOpen = desktopOpenHref === item.href;
    const dropdownId = `${menuId}-desktop-${item.href.replace(/\W+/g, "-")}`;
    const hasGroups = Boolean(item.groups?.length);
    const allChild = item.children?.find((child) => child.href === item.href);
    const flatChildren =
      item.children?.filter((child) => child.href !== item.href) ?? [];
    const wide = hasGroups || flatChildren.length > 6;

    return (
      <div key={item.href} className="relative">
        <button
          type="button"
          className={`inline-flex items-center gap-1.5 rounded-lg px-2.5 py-1.5 text-[12px] font-semibold uppercase tracking-[0.12em] transition-colors ${
            isSos
              ? sectionActive || dropdownOpen
                ? "bg-wood text-iron ring-2 ring-wood/50"
                : "bg-wood/90 text-iron hover:bg-wood"
              : sectionActive || dropdownOpen
                ? "bg-herb text-iron"
                : "text-bone/55 hover:bg-bone/10 hover:text-bone"
          }`}
          aria-expanded={dropdownOpen}
          aria-haspopup="menu"
          aria-controls={dropdownId}
          onClick={() => toggleDesktopItem(item.href)}
        >
          {item.label}
          <Chevron open={dropdownOpen} />
        </button>

        {dropdownOpen ? (
          <div
            id={dropdownId}
            role="menu"
            className={`absolute right-0 top-full z-50 mt-2 max-h-[min(70vh,24rem)] overflow-y-auto overscroll-contain rounded-xl border-2 border-bone/15 bg-iron py-1.5 shadow-lg shadow-black/30 ${
              wide
                ? "w-[min(28rem,calc(100vw-2.5rem))]"
                : "w-56"
            }`}
          >
            {allChild ? (
              <Link
                role="menuitem"
                href={allChild.href}
                className={dropdownItemClass(
                  navChildIsActive(
                    pathname,
                    searchParams,
                    allChild.href,
                    item.href
                  )
                )}
                onClick={() =>
                  closeDesktopMenus(setDesktopOpenHref, setDesktopGroupId)
                }
              >
                {allChild.label}
              </Link>
            ) : null}

            {hasGroups ? (
              <div className="mt-1 border-t border-bone/15 pt-1">
                {item.groups!.map((group) => {
                  const groupOpen = desktopGroupId === group.id;
                  const groupPanelId = `${dropdownId}-group-${group.id}`;
                  const groupWide = group.children.length > 6;

                  return (
                    <div key={group.id} className="px-1">
                      <button
                        type="button"
                        className={`flex w-full items-center justify-between rounded-lg px-2.5 py-2 text-left text-[11px] font-semibold uppercase tracking-[0.14em] transition-colors ${
                          groupOpen
                            ? "bg-bone/10 text-bone"
                            : "text-bone/55 hover:bg-bone/10 hover:text-bone"
                        }`}
                        aria-expanded={groupOpen}
                        aria-controls={groupPanelId}
                        onClick={() =>
                          setDesktopGroupId((current) =>
                            current === group.id ? null : group.id
                          )
                        }
                      >
                        {group.label}
                        <Chevron open={groupOpen} />
                      </button>

                      {groupOpen ? (
                        <div id={groupPanelId} className="pb-1.5">
                          {group.hubHref && group.hubLabel ? (
                            <Link
                              role="menuitem"
                              href={group.hubHref}
                              className={dropdownItemClass(
                                navChildIsActive(
                                  pathname,
                                  searchParams,
                                  group.hubHref,
                                  group.hubHref
                                )
                              )}
                              onClick={() =>
                                closeDesktopMenus(
                                  setDesktopOpenHref,
                                  setDesktopGroupId
                                )
                              }
                            >
                              {group.hubLabel}
                            </Link>
                          ) : null}
                          <div
                            className={groupWide ? "grid grid-cols-2" : ""}
                          >
                            {group.children.map((child) => (
                              <Link
                                key={`${child.href}-${child.label}`}
                                role="menuitem"
                                href={child.href}
                                className={dropdownItemClass(
                                  navChildIsActive(
                                    pathname,
                                    searchParams,
                                    child.href,
                                    group.hubHref ?? item.href
                                  )
                                )}
                                onClick={() =>
                                  closeDesktopMenus(
                                    setDesktopOpenHref,
                                    setDesktopGroupId
                                  )
                                }
                              >
                                {child.label}
                              </Link>
                            ))}
                          </div>
                        </div>
                      ) : null}
                    </div>
                  );
                })}
              </div>
            ) : (
              <>
                <div
                  className="mx-2 my-1 border-t border-bone/15"
                  aria-hidden
                />
                <div className={wide ? "grid grid-cols-2" : ""}>
                  {flatChildren.map((child) => (
                    <Link
                      key={`${child.href}-${child.label}`}
                      role="menuitem"
                      href={child.href}
                      className={dropdownItemClass(
                        navChildIsActive(
                          pathname,
                          searchParams,
                          child.href,
                          item.href
                        )
                      )}
                      onClick={() =>
                        closeDesktopMenus(
                          setDesktopOpenHref,
                          setDesktopGroupId
                        )
                      }
                    >
                      {child.label}
                    </Link>
                  ))}
                </div>
              </>
            )}
          </div>
        ) : null}
      </div>
    );
  }

  function renderMobileChildLink(
    child: NavChild,
    sectionHref: string,
    childIndex: number,
    isAll: boolean,
    sectionOpen: boolean
  ) {
    const active = navChildIsActive(
      pathname,
      searchParams,
      child.href,
      sectionHref
    );
    return (
      <Link
        href={child.href}
        className={`mt-1 block rounded-xl border-2 px-3 py-2.5 text-[12px] font-semibold uppercase tracking-[0.14em] transition-colors ${
          isAll ? "pl-6" : "text-center"
        } ${open ? "animate-rise" : ""} ${
          active
            ? "border-herb bg-herb text-iron"
            : "border-bone/10 bg-ash/40 text-bone/70 hover:border-herb hover:text-herb"
        }`}
        style={
          open && sectionOpen
            ? { animationDelay: `${0.1 + childIndex * 0.03}s` }
            : undefined
        }
        onClick={closeMenu}
      >
        {child.label}
      </Link>
    );
  }

  function renderMobileItem(
    item: NavItem,
    index: number,
    isSos = false
  ) {
    const sectionActive = sectionIsActive(pathname, item);
    const hasGroups = Boolean(item.groups?.length);
    const hasChildren = Boolean(item.children?.length) || hasGroups;

    if (!hasChildren) {
      return (
        <li key={item.href}>
          <Link
            href={item.href}
            className={`block rounded-xl border-2 px-4 py-3 text-[13px] font-semibold uppercase tracking-[0.14em] transition-colors ${
              open ? "animate-rise" : ""
            } ${
              isSos
                ? "border-wood bg-wood text-iron hover:bg-wood/90"
                : "border-bone/10 bg-ash/60 text-bone/80 hover:border-herb hover:text-herb"
            }`}
            style={
              open ? { animationDelay: `${0.06 + index * 0.05}s` } : undefined
            }
            onClick={closeMenu}
          >
            {item.label}
          </Link>
        </li>
      );
    }

    const sectionId = `${menuId}-section-${item.href.replace(/\W+/g, "-")}`;
    const sectionOpen = mobileOpen[item.href] ?? false;
    const allChild = item.children?.find((child) => child.href === item.href);
    const flatChildren =
      item.children?.filter((child) => child.href !== item.href) ?? [];

    return (
      <li key={item.href} className="flex flex-col gap-1">
        <button
          type="button"
          className={`flex w-full items-center justify-between rounded-xl border-2 px-4 py-3 text-left text-[13px] font-semibold uppercase tracking-[0.14em] transition-colors ${
            open ? "animate-rise" : ""
          } ${
            isSos
              ? sectionActive || sectionOpen
                ? "border-wood bg-wood text-iron"
                : "border-wood/60 bg-wood/90 text-iron hover:bg-wood"
              : sectionActive || sectionOpen
                ? "border-herb bg-herb/15 text-herb"
                : "border-bone/10 bg-ash/60 text-bone/80 hover:border-herb hover:text-herb"
          }`}
          style={
            open ? { animationDelay: `${0.06 + index * 0.05}s` } : undefined
          }
          aria-expanded={sectionOpen}
          aria-controls={sectionId}
          onClick={() =>
            setMobileOpen((current) => ({
              ...current,
              [item.href]: !sectionOpen,
            }))
          }
        >
          {item.label}
          <Chevron open={sectionOpen} />
        </button>

        <div
          id={sectionId}
          className={`grid ${
            sectionOpen ? "grid-rows-[1fr]" : "grid-rows-[0fr]"
          } transition-[grid-template-rows] duration-300 ease-out`}
        >
          <ul className="overflow-hidden">
            {allChild ? (
              <li>
                {renderMobileChildLink(
                  allChild,
                  item.href,
                  0,
                  true,
                  sectionOpen
                )}
              </li>
            ) : null}

            {hasGroups
              ? item.groups!.map((group, groupIndex) => {
                  const groupKey = `${item.href}::${group.id}`;
                  const groupOpen = mobileGroupOpen[groupKey] ?? false;
                  const groupId = `${sectionId}-group-${group.id}`;

                  return (
                    <li key={group.id} className="mt-1">
                      <button
                        type="button"
                        className={`flex w-full items-center justify-between rounded-xl border-2 px-3 py-2.5 text-left text-[12px] font-semibold uppercase tracking-[0.14em] transition-colors ${
                          groupOpen
                            ? "border-herb/40 bg-herb/10 text-herb"
                            : "border-bone/10 bg-ash/40 text-bone/70 hover:border-herb hover:text-herb"
                        }`}
                        aria-expanded={groupOpen}
                        aria-controls={groupId}
                        onClick={() =>
                          setMobileGroupOpen((current) => ({
                            ...current,
                            [groupKey]: !groupOpen,
                          }))
                        }
                      >
                        {group.label}
                        <Chevron open={groupOpen} />
                      </button>

                      <div
                        id={groupId}
                        className={`grid ${
                          groupOpen ? "grid-rows-[1fr]" : "grid-rows-[0fr]"
                        } transition-[grid-template-rows] duration-300 ease-out`}
                      >
                        <ul className="overflow-hidden pl-1">
                          {group.hubHref && group.hubLabel ? (
                            <li>
                              {renderMobileChildLink(
                                {
                                  href: group.hubHref,
                                  label: group.hubLabel,
                                },
                                group.hubHref,
                                groupIndex,
                                true,
                                groupOpen
                              )}
                            </li>
                          ) : null}
                          <li>
                            <ul className="grid grid-cols-2 gap-x-1">
                              {group.children.map((child, childIndex) => (
                                <li key={`${child.href}-${child.label}`}>
                                  {renderMobileChildLink(
                                    child,
                                    group.hubHref ?? item.href,
                                    childIndex + 1,
                                    false,
                                    groupOpen
                                  )}
                                </li>
                              ))}
                            </ul>
                          </li>
                        </ul>
                      </div>
                    </li>
                  );
                })
              : (
                <li>
                  <ul className="grid grid-cols-2 gap-x-1">
                    {flatChildren.map((child, childIndex) => (
                      <li key={`${child.href}-${child.label}`}>
                        {renderMobileChildLink(
                          child,
                          item.href,
                          childIndex + 1,
                          false,
                          sectionOpen
                        )}
                      </li>
                    ))}
                  </ul>
                </li>
              )}
          </ul>
        </div>
      </li>
    );
  }

  return (
    <header
      className={`relative isolate z-50 flex flex-col border-b-2 border-bone/15 ${
        open
          ? "fixed inset-0 bg-iron md:sticky md:inset-auto md:top-0 md:bg-iron/95 md:backdrop-blur-sm"
          : "sticky top-0 bg-iron/95 backdrop-blur-sm"
      }`}
    >
      <div className="relative z-10 mx-auto flex w-full max-w-5xl shrink-0 items-center justify-between px-5 py-3.5 md:px-8">
        <Link
          href="/"
          aria-label="Saltet — gå til forsiden"
          onClick={handleLogoClick}
          className="relative z-10 -my-1 inline-flex min-h-11 cursor-pointer items-center gap-1.5 py-1 font-serif text-2xl uppercase tracking-wide text-bone transition-colors hover:text-herb md:text-3xl"
        >
          Saltet
          <SaltShakerMark className="pointer-events-none mb-0.5 h-[0.85em] w-[0.85em] shrink-0 text-herb" />
        </Link>

        <nav
          ref={desktopNavRef}
          aria-label="Hovedmenu"
          className="hidden items-center gap-1 md:flex"
        >
          {navItems.map((item) => renderDesktopDropdown(item))}
          {renderDesktopDropdown(sosNav, true)}
        </nav>

        <button
          type="button"
          className="relative flex h-10 w-10 items-center justify-center rounded-lg border-2 border-bone/25 text-bone md:hidden"
          aria-expanded={open}
          aria-controls={menuId}
          aria-label={open ? "Luk menu" : "Åbn menu"}
          onClick={toggleMenu}
        >
          <span aria-hidden className="relative block h-3.5 w-5">
            <span
              className={`absolute left-0 top-0 block h-0.5 w-full bg-current transition-transform duration-300 ease-out ${
                open ? "translate-y-[6.5px] rotate-45" : ""
              }`}
            />
            <span
              className={`absolute left-0 top-[6.5px] block h-0.5 w-full bg-current transition-opacity duration-200 ${
                open ? "opacity-0" : "opacity-100"
              }`}
            />
            <span
              className={`absolute left-0 top-[13px] block h-0.5 w-full bg-current transition-transform duration-300 ease-out ${
                open ? "-translate-y-[6.5px] -rotate-45" : ""
              }`}
            />
          </span>
        </button>
      </div>

      <div
        id={menuId}
        className={`min-h-0 flex-col md:hidden ${
          open ? "flex flex-1" : "hidden"
        }`}
      >
        <div
          ref={menuScrollRef}
          className="min-h-0 flex-1 overflow-y-auto overscroll-contain touch-pan-y [-webkit-overflow-scrolling:touch]"
        >
          <nav
            aria-label="Mobilmenu"
            className="border-t-2 border-bone/15 px-5 pb-[max(2rem,env(safe-area-inset-bottom))] pt-3"
          >
            <ul className="flex flex-col gap-1">
              {renderMobileItem(sosNav, 0, true)}
              {navItems.map((item, index) =>
                renderMobileItem(item, index + 1)
              )}
            </ul>
          </nav>
        </div>
      </div>
    </header>
  );
}
