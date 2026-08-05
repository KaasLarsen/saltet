import Link from "next/link";
import { categories } from "@/lib/categories";

export function Footer() {
  return (
    <footer className="mt-auto border-t border-charcoal/5 bg-cream">
      <div className="mx-auto max-w-6xl px-5 py-12 md:px-8">
        <div className="flex flex-col gap-8 md:flex-row md:justify-between">
          <div>
            <Link
              href="/"
              className="font-serif text-xl font-medium text-charcoal"
            >
              Saltet
            </Link>
            <p className="mt-2 max-w-xs text-sm text-charcoal/60 leading-relaxed">
              Enkle opskrifter til hverdagen. Lækker mad uden bøvl.
            </p>
          </div>
          <div>
            <p className="mb-3 text-xs font-medium uppercase tracking-wider text-charcoal/50">
              Kategorier
            </p>
            <ul className="space-y-2">
              {categories.map((cat) => (
                <li key={cat.slug}>
                  <Link
                    href={`/opskrifter/${cat.slug}`}
                    className="text-sm text-charcoal/70 hover:text-charcoal"
                  >
                    {cat.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        </div>
        <p className="mt-10 text-xs text-charcoal/40">
          © {new Date().getFullYear()} Saltet · saltet.dk
        </p>
      </div>
    </footer>
  );
}
