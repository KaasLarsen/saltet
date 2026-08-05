import Link from "next/link";

const navLinks = [
  { href: "/opskrifter", label: "Opskrifter" },
  { href: "/opskrifter/airfryer", label: "Airfryer" },
  { href: "/om", label: "Om" },
];

export function Header() {
  return (
    <header className="sticky top-0 z-50 border-b border-bone/10 bg-iron/90 backdrop-blur-sm">
      <div className="mx-auto flex max-w-5xl items-center justify-between px-5 py-4 md:px-8">
        <Link
          href="/"
          className="font-serif text-3xl tracking-tight text-bone"
        >
          Saltet
        </Link>
        <nav className="flex items-center gap-5 md:gap-8">
          {navLinks.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              className="text-[13px] uppercase tracking-[0.14em] text-bone/55 transition-colors hover:text-bone"
            >
              {link.label}
            </Link>
          ))}
        </nav>
      </div>
    </header>
  );
}
