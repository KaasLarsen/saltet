import Link from "next/link";

const SHORTCUTS = [
  { href: "/opskrifter/airfryer", label: "Airfryer", hint: "Sprødt uden drama" },
  { href: "/opskrifter/stobejern", label: "Støbejern", hint: "Skorpe og varme" },
  { href: "/opskrifter/grill", label: "Grill", hint: "Røg og flamme" },
  { href: "/emner/keto", label: "Keto", hint: "Fedt, salt, umami" },
] as const;

export function HomeShortcuts() {
  return (
    <section
      className="border-y border-bone/10 bg-ash/50"
      aria-label="Hurtige genveje"
    >
      <div className="mx-auto grid max-w-5xl grid-cols-2 gap-3 px-5 py-8 md:grid-cols-4 md:gap-4 md:px-8 md:py-10">
        {SHORTCUTS.map((item, index) => (
          <Link
            key={item.href}
            href={item.href}
            className="group animate-rise relative flex flex-col justify-between overflow-hidden rounded-2xl border-2 border-bone/20 bg-iron px-4 py-5 shadow-[4px_4px_0_0_rgba(255,92,57,0.45)] transition-[transform,border-color,box-shadow] duration-300 hover:-translate-y-1 hover:border-herb hover:shadow-[6px_6px_0_0_rgba(212,255,0,0.65)]"
            style={{ animationDelay: `${index * 60}ms` }}
          >
            <span className="pointer-events-none absolute -right-2 -top-3 font-serif text-6xl leading-none text-bone/[0.06] transition-colors group-hover:text-herb/15">
              {String(index + 1).padStart(2, "0")}
            </span>
            <span className="relative font-serif text-xl uppercase tracking-wide text-bone transition-colors group-hover:text-herb md:text-2xl">
              {item.label}
            </span>
            <span className="relative mt-3 text-[11px] font-bold uppercase tracking-[0.14em] text-smoke group-hover:text-bone/70">
              {item.hint} →
            </span>
          </Link>
        ))}
      </div>
    </section>
  );
}
