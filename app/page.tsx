import Image from "next/image";
import Link from "next/link";
import { RecipeCard } from "@/components/RecipeCard";
import { getFeaturedRecipes } from "@/lib/recipes";
import { categories } from "@/lib/categories";

export default function HomePage() {
  const featured = getFeaturedRecipes(3);

  return (
    <>
      <section className="relative min-h-[88vh] overflow-hidden">
        <Image
          src="/brand/hero.jpg"
          alt="Træbord med jernpande, salt og friske krydderurter"
          fill
          className="object-cover animate-fade"
          sizes="100vw"
          priority
        />
        <div className="absolute inset-0 bg-gradient-to-r from-ink/85 via-ink/55 to-ink/25" />
        <div className="absolute inset-0 bg-gradient-to-t from-ink/50 via-transparent to-ink/20" />

        <div className="relative mx-auto flex min-h-[88vh] max-w-6xl flex-col justify-end px-5 pb-16 pt-28 md:px-8 md:pb-24">
          <p className="animate-rise mb-4 text-[12px] uppercase tracking-[0.22em] text-linen/70">
            Nordisk køkken · Airfryer først
          </p>
          <h1 className="animate-rise delay-1 font-serif text-5xl leading-[1.05] text-linen md:text-7xl md:leading-[1.02]">
            Saltet
          </h1>
          <p className="animate-rise delay-2 mt-5 max-w-md text-base leading-relaxed text-linen/75 md:text-lg">
            Groft, enkelt og med smag. Opskrifter der føles som et træbord,
            sort jern og friske krydderurter.
          </p>
          <div className="animate-rise delay-3 mt-8">
            <Link
              href="/opskrifter/airfryer"
              className="inline-flex items-center border border-linen/40 bg-linen/10 px-6 py-3 text-[12px] uppercase tracking-[0.16em] text-linen backdrop-blur-sm transition-colors hover:bg-linen hover:text-ink"
            >
              Se airfryer opskrifter
            </Link>
          </div>
        </div>
      </section>

      <section className="mx-auto max-w-6xl px-5 py-16 md:px-8 md:py-20">
        <div className="mb-10 flex items-end justify-between border-b border-ink/15 pb-4">
          <h2 className="font-serif text-3xl text-ink md:text-4xl">
            Udvalgte opskrifter
          </h2>
          <Link
            href="/opskrifter"
            className="text-[12px] uppercase tracking-[0.14em] text-smoke transition-colors hover:text-ink"
          >
            Se alle
          </Link>
        </div>
        <div className="grid gap-10 sm:grid-cols-2 lg:grid-cols-3">
          {featured.map((recipe, index) => (
            <RecipeCard
              key={recipe.slug}
              recipe={recipe}
              priority={index === 0}
            />
          ))}
        </div>
      </section>

      <section className="border-y border-ink/15 bg-paper/60">
        <div className="mx-auto max-w-6xl px-5 py-16 md:px-8">
          <h2 className="mb-8 font-serif text-3xl text-ink">Kategorier</h2>
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {categories.map((cat) => (
              <Link
                key={cat.slug}
                href={`/opskrifter/${cat.slug}`}
                className="group border border-ink/20 bg-linen/50 p-6 transition-colors hover:border-ink hover:bg-linen"
              >
                <p className="mb-2 text-[11px] uppercase tracking-[0.18em] text-herb">
                  Kategori
                </p>
                <h3 className="font-serif text-2xl text-ink transition-colors group-hover:text-wood">
                  {cat.name}
                </h3>
                <p className="mt-3 text-sm leading-relaxed text-ink/60">
                  {cat.description}
                </p>
              </Link>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}
