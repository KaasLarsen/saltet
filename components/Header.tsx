import Link from "next/link";

const navLinks = [
  { href: "/opskrifter", label: "Opskrifter" },
  { href: "/opskrifter/airfryer", label: "Airfryer" },
  { href: "/om", label: "Om" },
];

export function Header() {
  return (
    <header className="sticky top-0 z-50 border-b border-ink/15 bg-linen/92 backdrop-blur-sm">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-5 py-4 md:px-8">
        <Link
          href="/"
          className="font-serif text-3xl tracking-tight text-ink"
        >
          Saltet
        </Link>
        <nav className="flex items-center gap-5 md:gap-8">
          {navLinks.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              className="text-[13px] uppercase tracking-[0.14em] text-ink/65 transition-colors hover:text-ink"
            >
              {link.label}
            </Link>
          ))}
        </nav>
      </div>
    </header>
  );
}
