import Image from "next/image";
import Link from "next/link";
import { RecipeCard } from "@/components/RecipeCard";
import { SearchForm } from "@/components/SearchForm";
import { categories } from "@/lib/categories";
import { getHighlightedHoliday } from "@/lib/holiday-nav";
import { holidays, getRecipesByHoliday } from "@/lib/holidays";
import { getFeaturedRecipes } from "@/lib/recipes";

export default function HomePage() {
  const featuredByCategory = categories.map((cat) => ({
    category: cat,
    recipes: getFeaturedRecipes(3, cat.slug),
  }));
  const highlighted = getHighlightedHoliday();
  const highlightedHoliday = holidays.find(
    (h) => h.slug === highlighted.holiday.slug
  );
  const seasonalRecipes =
    highlighted.status === "now" && highlightedHoliday
      ? getRecipesByHoliday(highlightedHoliday.slug).slice(0, 3)
      : [];

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
        <div className="absolute inset-0 bg-gradient-to-t from-iron via-iron/45 to-iron/20" />
        <div className="absolute inset-0 bg-[repeating-linear-gradient(-18deg,transparent,transparent_14px,rgba(212,255,0,0.055)_14px,rgba(212,255,0,0.055)_15px)]" />

        <div className="relative mx-auto flex min-h-[88vh] max-w-3xl flex-col items-center justify-end px-5 pb-16 pt-28 text-center md:pb-24">
          <p className="animate-sticker mb-5 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron shadow-[3px_3px_0_0_rgba(255,92,57,0.9)]">
            Kitchen session · Airfryer til grill
          </p>
          <h1 className="animate-rise delay-1 font-serif text-6xl uppercase leading-[0.95] tracking-wide text-bone drop-shadow-[4px_4px_0_rgba(255,92,57,0.95)] md:text-8xl md:leading-[0.92]">
            Saltet
          </h1>
          <p className="animate-rise delay-2 mx-auto mt-5 max-w-md text-base leading-relaxed text-bone/75 md:text-lg">
            Salt på maden. Opskrifter med kant — sprøde, enkle og klar til
            hverdagens session.
          </p>
          <div className="animate-rise delay-3 mt-8 w-full max-w-lg">
            <SearchForm variant="hero" />
          </div>
          <Link
            href="/opskrifter/airfryer"
            className="animate-rise delay-3 mt-5 inline-flex rounded-lg border-2 border-bone/30 bg-bone/5 px-4 py-2 text-[12px] font-bold uppercase tracking-[0.14em] text-bone/80 transition-colors hover:border-herb hover:bg-herb hover:text-iron"
          >
            Drop ind i airfryer →
          </Link>
        </div>
      </section>

      {highlightedHoliday && seasonalRecipes.length > 0 ? (
        <section className="mx-auto max-w-5xl px-5 py-16 md:px-8 md:py-20">
          <div className="mb-10 flex flex-col items-center gap-3 text-center">
            <p className="inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
              I sæson
            </p>
            <h2 className="font-serif text-3xl uppercase tracking-wide text-bone md:text-4xl">
              {highlightedHoliday.headline}
            </h2>
            <Link
              href={`/hoejtider/${highlightedHoliday.slug}`}
              className="rounded-lg border-2 border-wood/60 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.14em] text-wood transition-colors hover:bg-wood hover:text-bone"
            >
              Se alle
            </Link>
          </div>
          <div className="grid gap-10 sm:grid-cols-2 lg:grid-cols-3">
            {seasonalRecipes.map((recipe, index) => (
              <RecipeCard
                key={`${recipe.category}/${recipe.slug}`}
                recipe={recipe}
                priority={index === 0}
              />
            ))}
          </div>
        </section>
      ) : null}

      {featuredByCategory.map(({ category, recipes }, sectionIndex) =>
        recipes.length === 0 ? null : (
          <section
            key={category.slug}
            className="mx-auto max-w-5xl px-5 py-16 md:px-8 md:py-20"
          >
            <div className="mb-10 flex flex-col items-center gap-3 text-center">
              <h2 className="font-serif text-3xl uppercase tracking-wide text-bone md:text-4xl">
                Udvalgte {category.name.toLowerCase()}
              </h2>
              <Link
                href={`/opskrifter/${category.slug}`}
                className="rounded-lg border-2 border-wood/60 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.14em] text-wood transition-colors hover:bg-wood hover:text-bone"
              >
                Se alle
              </Link>
            </div>
            <div className="grid gap-10 sm:grid-cols-2 lg:grid-cols-3">
              {recipes.map((recipe, index) => (
                <RecipeCard
                  key={`${recipe.category}/${recipe.slug}`}
                  recipe={recipe}
                  priority={sectionIndex === 0 && index === 0}
                />
              ))}
            </div>
          </section>
        )
      )}

      <section className="border-y-2 border-bone/15 bg-ash/60">
        <div className="mx-auto max-w-5xl px-5 py-12 md:px-8 md:py-14">
          <div className="mb-8 flex flex-col items-center gap-3 text-center">
            <h2 className="font-serif text-2xl uppercase tracking-wide text-bone md:text-3xl">
              Højtider
            </h2>
            <Link
              href="/hoejtider"
              className="rounded-lg border-2 border-wood/60 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.14em] text-wood transition-colors hover:bg-wood hover:text-bone"
            >
              Se alle
            </Link>
          </div>
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
            {holidays.map((holiday) => {
              const isHighlight = holiday.slug === highlighted.holiday.slug;
              return (
                <Link
                  key={holiday.slug}
                  href={`/hoejtider/${holiday.slug}`}
                  className={`group rounded-2xl border-2 bg-stone px-3 py-5 text-center shadow-[3px_3px_0_0_rgba(212,255,0,0.35)] transition-[transform,border-color,box-shadow] hover:-rotate-1 hover:border-herb hover:shadow-[4px_4px_0_0_rgba(212,255,0,0.7)] ${
                    isHighlight ? "border-herb" : "border-bone/20"
                  }`}
                >
                  {isHighlight ? (
                    <span className="mb-2 inline-flex rounded-md border-2 border-iron bg-herb px-2 py-0.5 text-[10px] font-bold uppercase tracking-[0.12em] text-iron">
                      {highlighted.status === "now" ? "Nu" : "Næste"}
                    </span>
                  ) : null}
                  <h3 className="font-serif text-base uppercase tracking-wide text-bone transition-colors group-hover:text-herb sm:text-lg">
                    {holiday.name}
                  </h3>
                </Link>
              );
            })}
          </div>

          <h2 className="mb-8 mt-14 text-center font-serif text-2xl uppercase tracking-wide text-bone md:text-3xl">
            Kategorier
          </h2>
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-5">
            {categories.map((cat, i) => (
              <Link
                key={cat.slug}
                href={`/opskrifter/${cat.slug}`}
                className={`group rounded-2xl border-2 border-bone/20 bg-stone px-3 py-5 text-center shadow-[3px_3px_0_0_rgba(0,229,192,0.35)] transition-[transform,border-color,box-shadow] hover:-rotate-1 hover:border-pool hover:shadow-[4px_4px_0_0_rgba(0,229,192,0.7)] sm:px-4 sm:py-6 ${
                  i % 2 === 1 ? "lg:translate-y-2" : ""
                }`}
              >
                <h3 className="font-serif text-base uppercase tracking-wide text-bone transition-colors group-hover:text-pool sm:text-lg">
                  {cat.name}
                </h3>
                <p className="mt-1.5 line-clamp-2 text-[11px] leading-snug text-bone/45 sm:text-xs">
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
