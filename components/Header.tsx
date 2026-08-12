"use client";

import Link from "next/link";
import { useEffect, useId, useState } from "react";
import { usePathname } from "next/navigation";
import { SaltShakerMark } from "@/components/SaltShakerMark";

const navLinks = [
  { href: "/opskrifter", label: "Opskrifter" },
  { href: "/opskrifter/airfryer", label: "Airfryer" },
  { href: "/opskrifter/grill", label: "Grill" },
  { href: "/opskrifter/plancha", label: "Plancha" },
  { href: "/opskrifter/gryde", label: "Gryde" },
  { href: "/opskrifter/pande", label: "Pande" },
  { href: "/opskrifter/sylte", label: "Sylte" },
  { href: "/opskrifter/dips", label: "Dips" },
];

export function Header() {
  const pathname = usePathname();
  const menuId = useId();
  const [openedPath, setOpenedPath] = useState<string | null>(null);
  const open = openedPath === pathname;

  useEffect(() => {
    if (!open) return;

    function onKeyDown(e: KeyboardEvent) {
      if (e.key === "Escape") setOpenedPath(null);
    }

    document.addEventListener("keydown", onKeyDown);
    return () => document.removeEventListener("keydown", onKeyDown);
  }, [open]);

  function closeMenu() {
    setOpenedPath(null);
  }

  function toggleMenu() {
    setOpenedPath((current) => (current === pathname ? null : pathname));
  }

  return (
    <header className="sticky top-0 z-50 border-b-2 border-bone/15 bg-iron/95 backdrop-blur-sm">
      <div className="mx-auto flex max-w-5xl items-center justify-between px-5 py-3.5 md:px-8">
        <Link
          href="/"
          className="inline-flex items-center gap-1.5 font-serif text-2xl uppercase tracking-wide text-bone transition-colors hover:text-herb md:text-3xl"
        >
          Saltet
          <SaltShakerMark className="mb-0.5 h-[0.85em] w-[0.85em] shrink-0 text-herb" />
        </Link>

        <nav
          aria-label="Hovedmenu"
          className="hidden items-center gap-1 md:flex"
        >
          {navLinks.map((link) => {
            const active =
              pathname === link.href ||
              (link.href !== "/opskrifter" && pathname.startsWith(link.href));
            return (
              <Link
                key={link.href}
                href={link.href}
                className={`rounded-lg px-2.5 py-1.5 text-[12px] font-semibold uppercase tracking-[0.12em] transition-colors ${
                  active
                    ? "bg-herb text-iron"
                    : "text-bone/55 hover:bg-bone/10 hover:text-bone"
                }`}
              >
                {link.label}
              </Link>
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
        className={`grid md:hidden ${
          open ? "grid-rows-[1fr]" : "grid-rows-[0fr]"
        } transition-[grid-template-rows] duration-300 ease-out`}
      >
        <div className="overflow-hidden">
          <nav
            aria-label="Mobilmenu"
            className="border-t-2 border-bone/15 px-5 pb-5 pt-3"
          >
            <ul className="flex flex-col gap-1">
              {navLinks.map((link, index) => (
                <li key={link.href}>
                  <Link
                    href={link.href}
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
                    {link.label}
                  </Link>
                </li>
              ))}
            </ul>
          </nav>
        </div>
      </div>
    </header>
  );
}
