import Link from "next/link";
import { categories } from "@/lib/categories";

export function Footer() {
  return (
    <footer className="mt-auto border-t border-ink/15 bg-iron text-linen">
      <div className="mx-auto max-w-6xl px-5 py-14 md:px-8">
        <div className="flex flex-col gap-10 md:flex-row md:justify-between">
          <div>
            <Link href="/" className="font-serif text-2xl text-linen">
              Saltet
            </Link>
            <p className="mt-3 max-w-xs text-sm leading-relaxed text-linen/55">
              Groft. Enkelt. Mad med smag af køkkenbordet — træ, jern og
              krydderurter.
            </p>
          </div>
          <div>
            <p className="mb-3 text-[11px] uppercase tracking-[0.18em] text-linen/40">
              Kategorier
            </p>
            <ul className="space-y-2">
              {categories.map((cat) => (
                <li key={cat.slug}>
                  <Link
                    href={`/opskrifter/${cat.slug}`}
                    className="text-sm text-linen/70 transition-colors hover:text-linen"
                  >
                    {cat.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        </div>
        <p className="mt-12 border-t border-linen/10 pt-6 text-xs text-linen/35">
          © {new Date().getFullYear()} Saltet · saltet.dk
        </p>
      </div>
    </footer>
  );
}
