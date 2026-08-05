import Link from "next/link";

const navLinks = [
  { href: "/opskrifter", label: "Opskrifter" },
  { href: "/opskrifter/airfryer", label: "Airfryer" },
  { href: "/om", label: "Om" },
];

export function Header() {
  return (
    <header className="sticky top-0 z-50 border-b border-charcoal/5 bg-cream/90 backdrop-blur-md">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-5 py-4 md:px-8">
        <Link
          href="/"
          className="font-serif text-2xl font-medium tracking-tight text-charcoal"
        >
          Saltet
        </Link>
        <nav className="flex items-center gap-6">
          {navLinks.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              className="text-sm text-charcoal/70 transition-colors hover:text-charcoal"
            >
              {link.label}
            </Link>
          ))}
        </nav>
      </div>
    </header>
  );
}
