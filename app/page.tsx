import Image from "next/image";
import Link from "next/link";
import { CardCarousel, CarouselSlide } from "@/components/CardCarousel";
import { GuideCard } from "@/components/GuideCard";
import { PartnerBanner } from "@/components/PartnerBanner";
import { RecipeCard } from "@/components/RecipeCard";
import { SearchForm } from "@/components/SearchForm";
import { getAllGrej } from "@/lib/grej";
import { getAllGuides } from "@/lib/guides";
import { getActivePartnerBanner } from "@/lib/partners";
import { getFeaturedRecipes } from "@/lib/recipes";

export default function HomePage() {
  const featuredRecipes = getFeaturedRecipes(12);
  const latestGuides = getAllGuides()
    .slice(0, 8)
    .map((guide) => ({
      title: guide.title,
      slug: guide.slug,
      description: guide.description,
      tags: guide.tags,
      image: guide.image,
      imageAlt: guide.imageAlt,
    }));
  const latestGrej = getAllGrej()
    .slice(0, 8)
    .map((item) => ({
      title: item.title,
      slug: item.slug,
      description: item.description,
      tags: item.tags,
      image: item.image,
      imageAlt: item.imageAlt,
    }));
  const partnerBanner = getActivePartnerBanner();

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
            Opskrifter, guides og grej med kant — sprødt, enkelt og klar til
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

      {featuredRecipes.length > 0 ? (
        <section className="mx-auto max-w-5xl px-5 py-16 md:px-8 md:py-20">
          <div className="mb-10 flex flex-col items-center gap-3 text-center">
            <h2 className="font-serif text-3xl uppercase tracking-wide text-bone md:text-4xl">
              Udvalgte opskrifter
            </h2>
            <Link
              href="/opskrifter"
              className="rounded-lg border-2 border-wood/60 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.14em] text-wood transition-colors hover:bg-wood hover:text-bone"
            >
              Se alle
            </Link>
          </div>
          <CardCarousel label="Udvalgte opskrifter">
            {featuredRecipes.map((recipe, index) => (
              <CarouselSlide key={`${recipe.category}/${recipe.slug}`}>
                <RecipeCard recipe={recipe} priority={index === 0} />
              </CarouselSlide>
            ))}
          </CardCarousel>
        </section>
      ) : null}

      {partnerBanner ? <PartnerBanner banner={partnerBanner} /> : null}

      {latestGuides.length > 0 ? (
        <section className="mx-auto max-w-5xl px-5 py-16 md:px-8 md:py-20">
          <div className="mb-10 flex flex-col items-center gap-3 text-center">
            <h2 className="font-serif text-3xl uppercase tracking-wide text-bone md:text-4xl">
              Guides
            </h2>
            <p className="max-w-md text-sm text-bone/50">
              Metode, teknik og fejlfinding — før du tænder for grejet.
            </p>
            <Link
              href="/guides"
              className="rounded-lg border-2 border-wood/60 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.14em] text-wood transition-colors hover:bg-wood hover:text-bone"
            >
              Se alle
            </Link>
          </div>
          <CardCarousel label="Guides">
            {latestGuides.map((guide) => (
              <CarouselSlide key={guide.slug}>
                <GuideCard guide={guide} />
              </CarouselSlide>
            ))}
          </CardCarousel>
        </section>
      ) : null}

      {latestGrej.length > 0 ? (
        <section className="mx-auto max-w-5xl px-5 py-16 md:px-8 md:py-20">
          <div className="mb-10 flex flex-col items-center gap-3 text-center">
            <h2 className="font-serif text-3xl uppercase tracking-wide text-bone md:text-4xl">
              Grej
            </h2>
            <p className="max-w-md text-sm text-bone/50">
              Tests og købsguider — airfryer, pizzaovn, støbejern og bål.
            </p>
            <Link
              href="/grej"
              className="rounded-lg border-2 border-wood/60 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.14em] text-wood transition-colors hover:bg-wood hover:text-bone"
            >
              Se alt grej
            </Link>
          </div>
          <CardCarousel label="Grej">
            {latestGrej.map((item) => (
              <CarouselSlide key={item.slug}>
                <GuideCard href={`/grej/${item.slug}`} guide={item} />
              </CarouselSlide>
            ))}
          </CardCarousel>
        </section>
      ) : null}
    </>
  );
}
