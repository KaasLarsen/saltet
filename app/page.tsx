import Image from "next/image";
import Link from "next/link";
import { RecipeCard } from "@/components/RecipeCard";
import { SearchForm } from "@/components/SearchForm";
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
        <div className="absolute inset-0 bg-gradient-to-t from-iron via-iron/55 to-iron/30" />
        <div className="absolute inset-0 bg-iron/25" />

        <div className="relative mx-auto flex min-h-[88vh] max-w-3xl flex-col items-center justify-end px-5 pb-16 pt-28 text-center md:pb-24">
          <p className="animate-rise mb-4 text-[12px] uppercase tracking-[0.22em] text-bone/65">
            Nordisk køkken · Airfryer først
          </p>
          <h1 className="animate-rise delay-1 font-serif text-5xl leading-[1.05] text-bone md:text-7xl md:leading-[1.02]">
            Saltet
          </h1>
          <p className="animate-rise delay-2 mx-auto mt-5 max-w-md text-base leading-relaxed text-bone/70 md:text-lg">
            Groft, enkelt og med smag. Opskrifter der føles som et træbord,
            sort jern og friske krydderurter.
          </p>
          <div className="animate-rise delay-3 mt-8 w-full max-w-lg">
            <SearchForm variant="hero" />
          </div>
          <Link
            href="/opskrifter/airfryer"
            className="animate-rise delay-3 mt-5 inline-flex text-[12px] uppercase tracking-[0.16em] text-bone/55 transition-colors hover:text-bone"
          >
            Eller se alle airfryer opskrifter →
          </Link>
        </div>
      </section>

      <section className="mx-auto max-w-5xl px-5 py-16 md:px-8 md:py-20">
        <div className="mb-10 border-b border-bone/10 pb-4 text-center">
          <h2 className="font-serif text-3xl text-bone md:text-4xl">
            Udvalgte opskrifter
          </h2>
          <Link
            href="/opskrifter"
            className="mt-3 inline-block text-[12px] uppercase tracking-[0.14em] text-smoke transition-colors hover:text-bone"
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

      <section className="border-y border-bone/10 bg-ash/40">
        <div className="mx-auto max-w-5xl px-5 py-16 text-center md:px-8">
          <h2 className="mb-8 font-serif text-3xl text-bone">Kategorier</h2>
          <div className="mx-auto grid max-w-xl gap-4">
            {categories.map((cat) => (
              <Link
                key={cat.slug}
                href={`/opskrifter/${cat.slug}`}
                className="group border border-bone/15 bg-stone/60 p-6 transition-colors hover:border-bone/40 hover:bg-ash"
              >
                <p className="mb-2 text-[11px] uppercase tracking-[0.18em] text-herb">
                  Kategori
                </p>
                <h3 className="font-serif text-2xl text-bone transition-colors group-hover:text-wood">
                  {cat.name}
                </h3>
                <p className="mx-auto mt-3 max-w-sm text-sm leading-relaxed text-bone/55">
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
