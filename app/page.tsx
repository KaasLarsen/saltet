import Link from "next/link";
import Image from "next/image";
import { CardCarousel, CarouselSlide } from "@/components/CardCarousel";
import { FeaturedRecipeSpotlight } from "@/components/FeaturedRecipeSpotlight";
import { GuideCard } from "@/components/GuideCard";
import { HomeShortcuts } from "@/components/HomeShortcuts";
import { PartnerBanner } from "@/components/PartnerBanner";
import { SaltlageBeregner } from "@/components/SaltlageBeregner";
import { SearchForm } from "@/components/SearchForm";
import { getAllGrej } from "@/lib/grej";
import { getAllGuides } from "@/lib/guides";
import { barsetBanner, oaterBanner } from "@/lib/partners";
import { getFeaturedRecipes, toRecipeListItem } from "@/lib/recipes";

export default function HomePage() {
  const featuredRecipes = getFeaturedRecipes(8).map(toRecipeListItem);
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
        </div>
      </section>

      <HomeShortcuts />

      {featuredRecipes.length > 0 ? (
        <section className="mx-auto max-w-6xl px-5 py-16 md:px-8 md:py-20">
          <div className="mb-10 flex flex-col items-center gap-3 text-center">
            <h2 className="font-serif text-3xl uppercase tracking-wide text-bone md:text-4xl">
              Ugens ret
            </h2>
            <p className="max-w-md text-sm text-bone/50">
              Én session i fokus — plus de stærkeste udvalgte lige nu.
            </p>
            <Link
              href="/opskrifter"
              className="rounded-lg border-2 border-wood/60 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.14em] text-wood transition-colors hover:bg-wood hover:text-bone"
            >
              Se alle opskrifter
            </Link>
          </div>
          <FeaturedRecipeSpotlight recipes={featuredRecipes} />
        </section>
      ) : null}

      <PartnerBanner banner={oaterBanner} />

      <section className="border-y-2 border-wood/40 bg-stone">
        <div className="mx-auto max-w-3xl px-5 py-16 md:px-8 md:py-20">
          <div className="mb-8 text-center">
            <p className="mb-3 inline-flex rotate-[-1.5deg] rounded-lg border-2 border-iron bg-wood px-3 py-1 text-[11px] font-bold uppercase tracking-[0.16em] text-bone shadow-[3px_3px_0_0_rgba(212,255,0,0.75)]">
              Hurtigt værktøj
            </p>
            <h2 className="font-serif text-3xl uppercase tracking-wide text-bone md:text-4xl">
              Saltlage på 5 sekunder
            </h2>
            <p className="mx-auto mt-3 max-w-md text-sm text-bone/55">
              Liter vand × procent = gram fint salt. Klar til sprængning,
              fermentering og sild.
            </p>
          </div>
          <SaltlageBeregner className="my-0" />
          <p className="mt-6 text-center">
            <Link
              href="/guides/saltguide"
              className="text-[12px] font-bold uppercase tracking-[0.14em] text-pool transition-colors hover:text-herb"
            >
              Læs saltguiden →
            </Link>
          </p>
        </div>
      </section>

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

      <PartnerBanner banner={barsetBanner} />

      {latestGrej.length > 0 ? (
        <section className="relative overflow-hidden border-t-2 border-herb/30 bg-iron">
          <div
            className="pointer-events-none absolute inset-0 opacity-40"
            aria-hidden
          >
            <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top,rgba(255,92,57,0.18),transparent_55%)]" />
            <div className="absolute inset-0 bg-[repeating-linear-gradient(-18deg,transparent,transparent_12px,rgba(212,255,0,0.04)_12px,rgba(212,255,0,0.04)_13px)]" />
          </div>
          <div className="relative mx-auto max-w-5xl px-5 py-16 md:px-8 md:py-24">
            <div className="mb-10 flex flex-col items-center gap-3 text-center">
              <p className="inline-flex rounded-lg border-2 border-herb bg-iron px-3 py-1 text-[11px] font-bold uppercase tracking-[0.16em] text-herb">
                Grej & værktøj
              </p>
              <h2 className="font-serif text-3xl uppercase tracking-wide text-bone md:text-4xl">
                Det vi tester og torturerer
              </h2>
              <p className="max-w-md text-sm text-bone/55">
                Pålægsmaskiner, knive, støbejern og airfryere — rå tests uden
                brochure-sprog.
              </p>
              <Link
                href="/grej"
                className="rounded-lg border-2 border-herb/70 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.14em] text-herb transition-colors hover:bg-herb hover:text-iron"
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
          </div>
        </section>
      ) : null}
    </>
  );
}
