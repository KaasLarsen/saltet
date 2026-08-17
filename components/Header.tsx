"use client";

import Link from "next/link";
import { useEffect, useId, useRef, useState } from "react";
import { usePathname } from "next/navigation";
import { SaltShakerMark } from "@/components/SaltShakerMark";
import { CATEGORY_NAV } from "@/lib/category-nav";
import { HOLIDAY_NAV } from "@/lib/holiday-nav";

type NavChild = { href: string; label: string };
type NavItem = {
  href: string;
  label: string;
  children?: NavChild[];
};

const navItems: NavItem[] = [
  {
    href: "/opskrifter",
    label: "Opskrifter",
    children: [
      { href: "/opskrifter", label: "Alle opskrifter" },
      ...CATEGORY_NAV.map((c) => ({
        href: `/opskrifter/${c.slug}`,
        label: c.name,
      })),
    ],
  },
  {
    href: "/hoejtider",
    label: "Højtider",
    children: [
      { href: "/hoejtider", label: "Alle højtider" },
      ...HOLIDAY_NAV.map((h) => ({
        href: `/hoejtider/${h.slug}`,
        label: h.name,
      })),
    ],
  },
];

function pathIsActive(pathname: string, href: string, exact = false): boolean {
  if (exact) return pathname === href;
  return pathname === href || pathname.startsWith(`${href}/`);
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

export function Header() {
  const pathname = usePathname();
  const menuId = useId();
  const desktopNavRef = useRef<HTMLElement>(null);
  const menuScrollRef = useRef<HTMLDivElement>(null);
  const [openedPath, setOpenedPath] = useState<string | null>(null);
  const [desktopOpenHref, setDesktopOpenHref] = useState<string | null>(null);
  const [mobileOpen, setMobileOpen] = useState<Record<string, boolean>>({
    "/opskrifter": true,
    "/hoejtider": false,
  });
  const [menuPath, setMenuPath] = useState(pathname);
  if (pathname !== menuPath) {
    setMenuPath(pathname);
    setOpenedPath(null);
    setDesktopOpenHref(null);
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
      }
    }

    document.addEventListener("mousedown", onPointerDown);
    return () => document.removeEventListener("mousedown", onPointerDown);
  }, [desktopOpenHref]);

  function closeMenu() {
    setOpenedPath(null);
  }

  function toggleMenu() {
    setOpenedPath((current) => (current === pathname ? null : pathname));
  }

  return (
    <header
      className={`z-50 flex flex-col border-b-2 border-bone/15 ${
        open
          ? "fixed inset-0 bg-iron md:sticky md:inset-auto md:top-0 md:bg-iron/95 md:backdrop-blur-sm"
          : "sticky top-0 bg-iron/95 backdrop-blur-sm"
      }`}
    >
      <div className="mx-auto flex w-full max-w-5xl shrink-0 items-center justify-between px-5 py-3.5 md:px-8">
        <Link
          href="/"
          className="inline-flex items-center gap-1.5 font-serif text-2xl uppercase tracking-wide text-bone transition-colors hover:text-herb md:text-3xl"
        >
          Saltet
          <SaltShakerMark className="mb-0.5 h-[0.85em] w-[0.85em] shrink-0 text-herb" />
        </Link>

        <nav
          ref={desktopNavRef}
          aria-label="Hovedmenu"
          className="hidden items-center gap-1 md:flex"
        >
          {navItems.map((item) => {
            const sectionActive = pathIsActive(pathname, item.href);
            const dropdownOpen = desktopOpenHref === item.href;
            const dropdownId = `${menuId}-desktop-${item.href.replace(/\W+/g, "-")}`;

            if (!item.children?.length) {
              return (
                <Link
                  key={item.href}
                  href={item.href}
                  className={`rounded-lg px-2.5 py-1.5 text-[12px] font-semibold uppercase tracking-[0.12em] transition-colors ${
                    sectionActive
                      ? "bg-herb text-iron"
                      : "text-bone/55 hover:bg-bone/10 hover:text-bone"
                  }`}
                >
                  {item.label}
                </Link>
              );
            }

            const allChild = item.children.find(
              (child) => child.href === item.href
            );
            const childItems = item.children.filter(
              (child) => child.href !== item.href
            );
            const wide = childItems.length > 6;

            return (
              <div key={item.href} className="relative">
                <button
                  type="button"
                  className={`inline-flex items-center gap-1.5 rounded-lg px-2.5 py-1.5 text-[12px] font-semibold uppercase tracking-[0.12em] transition-colors ${
                    sectionActive || dropdownOpen
                      ? "bg-herb text-iron"
                      : "text-bone/55 hover:bg-bone/10 hover:text-bone"
                  }`}
                  aria-expanded={dropdownOpen}
                  aria-haspopup="menu"
                  aria-controls={dropdownId}
                  onClick={() =>
                    setDesktopOpenHref((current) =>
                      current === item.href ? null : item.href
                    )
                  }
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
                          pathname === allChild.href
                        )}
                        onClick={() => setDesktopOpenHref(null)}
                      >
                        {allChild.label}
                      </Link>
                    ) : null}

                    <div
                      className="mx-2 my-1 border-t border-bone/15"
                      aria-hidden
                    />

                    <div className={wide ? "grid grid-cols-2" : ""}>
                      {childItems.map((child) => (
                        <Link
                          key={`${child.href}-${child.label}`}
                          role="menuitem"
                          href={child.href}
                          className={dropdownItemClass(
                            pathIsActive(pathname, child.href)
                          )}
                          onClick={() => setDesktopOpenHref(null)}
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
              {navItems.map((item, index) => {
                const sectionActive = pathIsActive(pathname, item.href);

                if (!item.children?.length) {
                  return (
                    <li key={item.href}>
                      <Link
                        href={item.href}
                        className={`block rounded-xl border-2 border-bone/10 bg-ash/60 px-4 py-3 text-[13px] font-semibold uppercase tracking-[0.14em] text-bone/80 transition-colors hover:border-herb hover:text-herb ${
                          open ? "animate-rise" : ""
                        }`}
                        style={
                          open
                            ? { animationDelay: `${0.06 + index * 0.05}s` }
                            : undefined
                        }
                        onClick={closeMenu}
                      >
                        {item.label}
                      </Link>
                    </li>
                  );
                }

                const sectionId = `${menuId}-section-${index}`;
                const sectionOpen = mobileOpen[item.href] ?? false;

                return (
                  <li key={item.href} className="flex flex-col gap-1">
                    <button
                      type="button"
                      className={`flex w-full items-center justify-between rounded-xl border-2 px-4 py-3 text-left text-[13px] font-semibold uppercase tracking-[0.14em] transition-colors ${
                        open ? "animate-rise" : ""
                      } ${
                        sectionActive || sectionOpen
                          ? "border-herb bg-herb/15 text-herb"
                          : "border-bone/10 bg-ash/60 text-bone/80 hover:border-herb hover:text-herb"
                      }`}
                      style={
                        open
                          ? { animationDelay: `${0.06 + index * 0.05}s` }
                          : undefined
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
                        sectionOpen
                          ? "grid-rows-[1fr]"
                          : "grid-rows-[0fr]"
                      } transition-[grid-template-rows] duration-300 ease-out`}
                    >
                      <ul className="overflow-hidden">
                        {(() => {
                          const allChild = item.children.find(
                            (child) => child.href === item.href
                          );
                          const childItems = item.children.filter(
                            (child) => child.href !== item.href
                          );

                          function childLink(
                            child: NavChild,
                            childIndex: number,
                            isAll: boolean
                          ) {
                            const active = isAll
                              ? pathname === child.href
                              : pathIsActive(pathname, child.href);
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
                                    ? {
                                        animationDelay: `${
                                          0.1 + childIndex * 0.03
                                        }s`,
                                      }
                                    : undefined
                                }
                                onClick={closeMenu}
                              >
                                {child.label}
                              </Link>
                            );
                          }

                          return (
                            <>
                              {allChild ? (
                                <li>
                                  {childLink(allChild, 0, true)}
                                </li>
                              ) : null}
                              <li>
                                <ul className="grid grid-cols-2 gap-x-1">
                                  {childItems.map((child, childIndex) => (
                                    <li
                                      key={`${child.href}-${child.label}`}
                                    >
                                      {childLink(child, childIndex + 1, false)}
                                    </li>
                                  ))}
                                </ul>
                              </li>
                            </>
                          );
                        })()}
                      </ul>
                    </div>
                  </li>
                );
              })}
            </ul>
          </nav>
        </div>
      </div>
    </header>
  );
}
