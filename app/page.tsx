import Link from "next/link";
import { RecipeCard } from "@/components/RecipeCard";
import { getFeaturedRecipes } from "@/lib/recipes";
import { categories } from "@/lib/categories";

export default function HomePage() {
  const featured = getFeaturedRecipes(3);

  return (
    <>
      <section className="mx-auto max-w-6xl px-5 pt-16 pb-12 md:px-8 md:pt-24">
        <div className="max-w-2xl">
          <p className="mb-4 text-sm font-medium uppercase tracking-widest text-accent">
            Opskrifter til hverdagen
          </p>
          <h1 className="font-serif text-4xl font-medium leading-tight text-charcoal md:text-5xl md:leading-tight">
            Enkelt. Lækkert.{" "}
            <span className="text-accent">Saltet.</span>
          </h1>
          <p className="mt-6 text-lg text-charcoal/70 leading-relaxed">
            Vi starter med airfryer — sprødt, saftigt og klar på ingen tid.
            Flere kategorier kommer snart.
          </p>
          <Link
            href="/opskrifter/airfryer"
            className="mt-8 inline-flex items-center rounded-full bg-charcoal px-6 py-3 text-sm font-medium text-cream transition-colors hover:bg-charcoal/90"
          >
            Se airfryer opskrifter
          </Link>
        </div>
      </section>

      <section className="mx-auto max-w-6xl px-5 pb-20 md:px-8">
        <div className="mb-8 flex items-end justify-between">
          <h2 className="font-serif text-2xl font-medium text-charcoal">
            Udvalgte opskrifter
          </h2>
          <Link
            href="/opskrifter"
            className="text-sm text-charcoal/60 hover:text-charcoal"
          >
            Se alle →
          </Link>
        </div>
        <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
          {featured.map((recipe, index) => (
            <RecipeCard key={recipe.slug} recipe={recipe} priority={index === 0} />
          ))}
        </div>
      </section>

      <section className="border-t border-charcoal/5 bg-white/50">
        <div className="mx-auto max-w-6xl px-5 py-16 md:px-8">
          <h2 className="font-serif text-2xl font-medium text-charcoal mb-8">
            Kategorier
          </h2>
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {categories.map((cat) => (
              <Link
                key={cat.slug}
                href={`/opskrifter/${cat.slug}`}
                className="group rounded-2xl border border-charcoal/5 bg-cream p-6 transition-colors hover:border-accent/30 hover:bg-white"
              >
                <h3 className="font-serif text-xl font-medium text-charcoal group-hover:text-accent transition-colors">
                  {cat.name}
                </h3>
                <p className="mt-2 text-sm text-charcoal/60 leading-relaxed">
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
