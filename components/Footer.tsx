import Link from "next/link";
import { siteConfig } from "@/lib/seo";

const footerLinks = [
  { href: "/om", label: "Om" },
  { href: "/kontakt", label: "Kontakt" },
  { href: "/cookies", label: "Cookies" },
  { href: "/privatliv", label: "Privatliv" },
];

export function Footer() {
  return (
    <footer className="mt-auto border-t border-bone/10 bg-iron">
      <div className="mx-auto max-w-5xl px-5 py-8 text-center md:px-8">
        <nav
          aria-label="Sidefod"
          className="flex flex-wrap items-center justify-center gap-x-5 gap-y-2"
        >
          {footerLinks.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              className="text-[11px] uppercase tracking-[0.16em] text-bone/40 transition-colors hover:text-bone/70"
            >
              {link.label}
            </Link>
          ))}
        </nav>
        <p className="mt-5 text-xs text-bone/25">
          © {new Date().getFullYear()} {siteConfig.name}
        </p>
      </div>
    </footer>
  );
}
