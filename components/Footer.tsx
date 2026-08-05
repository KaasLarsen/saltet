import Link from "next/link";
import { categories } from "@/lib/categories";

export function Footer() {
  return (
    <footer className="mt-auto border-t border-bone/10 bg-iron text-bone">
      <div className="mx-auto max-w-5xl px-5 py-14 text-center md:px-8">
        <Link href="/" className="font-serif text-2xl text-bone">
          Saltet
        </Link>
        <p className="mx-auto mt-3 max-w-sm text-sm leading-relaxed text-bone/50">
          Groft. Enkelt. Mad med smag af køkkenbordet — træ, jern og
          krydderurter.
        </p>
        <div className="mt-8 flex flex-wrap items-center justify-center gap-5">
          {categories.map((cat) => (
            <Link
              key={cat.slug}
              href={`/opskrifter/${cat.slug}`}
              className="text-[12px] uppercase tracking-[0.14em] text-bone/55 transition-colors hover:text-bone"
            >
              {cat.name}
            </Link>
          ))}
          <Link
            href="/tags"
            className="text-[12px] uppercase tracking-[0.14em] text-bone/55 transition-colors hover:text-bone"
          >
            Tags
          </Link>
        </div>
        <p className="mt-10 border-t border-bone/10 pt-6 text-xs text-bone/30">
          © {new Date().getFullYear()} Saltet · saltet.dk
        </p>
      </div>
    </footer>
  );
}
