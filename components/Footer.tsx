import Link from "next/link";
import { siteConfig } from "@/lib/seo";

const footerLinks = [
  { href: "/guides", label: "Guides" },
  { href: "/grej", label: "Grej" },
  { href: "/hoejtider", label: "Højtider" },
  { href: "/om", label: "Om" },
  { href: "/kontakt", label: "Kontakt" },
  { href: "/cookies", label: "Cookies" },
  { href: "/privatliv", label: "Privatliv" },
];

export function Footer() {
  return (
    <footer className="mt-auto border-t-2 border-bone/15 bg-iron">
      <div className="mx-auto max-w-5xl px-5 py-10 text-center md:px-8">
        <p className="font-serif text-xl uppercase tracking-wide text-herb">
          Saltet
        </p>
        <nav
          aria-label="Sidefod"
          className="mt-5 flex flex-wrap items-center justify-center gap-2"
        >
          {footerLinks.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              className="rounded-lg px-3 py-1.5 text-[11px] font-semibold uppercase tracking-[0.14em] text-bone/45 transition-colors hover:bg-bone/10 hover:text-bone"
            >
              {link.label}
            </Link>
          ))}
        </nav>
        <p className="mt-6 text-xs text-bone/30">
          © {new Date().getFullYear()} {siteConfig.name} — salt on everything
        </p>
      </div>
    </footer>
  );
}
