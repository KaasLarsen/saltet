"use client";

import { useCallback, useEffect, useRef, useState, type ReactNode } from "react";

interface CardCarouselProps {
  label: string;
  children: ReactNode;
}

export function CardCarousel({ label, children }: CardCarouselProps) {
  const scrollerRef = useRef<HTMLDivElement>(null);
  const [canPrev, setCanPrev] = useState(false);
  const [canNext, setCanNext] = useState(false);

  const update = useCallback(() => {
    const el = scrollerRef.current;
    if (!el) return;
    const max = el.scrollWidth - el.clientWidth;
    setCanPrev(el.scrollLeft > 4);
    setCanNext(el.scrollLeft < max - 4);
  }, []);

  useEffect(() => {
    const el = scrollerRef.current;
    if (!el) return;
    update();
    el.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    const ro = new ResizeObserver(update);
    ro.observe(el);
    for (const child of el.children) {
      ro.observe(child);
    }
    const images = el.querySelectorAll("img");
    images.forEach((img) => img.addEventListener("load", update));
    return () => {
      el.removeEventListener("scroll", update);
      window.removeEventListener("resize", update);
      ro.disconnect();
      images.forEach((img) => img.removeEventListener("load", update));
    };
  }, [update, children]);

  function scrollByPage(direction: -1 | 1) {
    const el = scrollerRef.current;
    if (!el) return;
    const distance = el.clientWidth * 0.9;
    el.scrollTo({ left: el.scrollLeft + direction * distance, behavior: "smooth" });
  }

  return (
    <div className="relative">
      <div
        ref={scrollerRef}
        role="region"
        aria-label={label}
        className="flex snap-x snap-mandatory gap-6 overflow-x-auto pb-2 [scrollbar-width:none] [&::-webkit-scrollbar]:hidden"
      >
        {children}
      </div>
      {canPrev ? (
        <button
          type="button"
          aria-label="Forrige"
          onClick={() => scrollByPage(-1)}
          className="absolute left-0 top-[28%] z-10 -translate-x-1 rounded-lg border-2 border-iron bg-herb px-2.5 py-2 text-[11px] font-bold uppercase tracking-[0.14em] text-iron shadow-[3px_3px_0_0_rgba(255,92,57,0.9)] transition-transform hover:-translate-x-1.5 sm:-translate-x-3"
        >
          ←
        </button>
      ) : null}
      {canNext ? (
        <button
          type="button"
          aria-label="Næste"
          onClick={() => scrollByPage(1)}
          className="absolute right-0 top-[28%] z-10 translate-x-1 rounded-lg border-2 border-iron bg-herb px-2.5 py-2 text-[11px] font-bold uppercase tracking-[0.14em] text-iron shadow-[3px_3px_0_0_rgba(255,92,57,0.9)] transition-transform hover:translate-x-1.5 sm:translate-x-3"
        >
          →
        </button>
      ) : null}
    </div>
  );
}

export function CarouselSlide({ children }: { children: ReactNode }) {
  return (
    <div className="w-[85%] min-w-[85%] shrink-0 snap-start sm:w-[48%] sm:min-w-[48%] lg:w-[32%] lg:min-w-[32%]">
      {children}
    </div>
  );
}
