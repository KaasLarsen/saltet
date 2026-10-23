import type { Metadata } from "next";
import { AnmeldelseFilters } from "@/components/AnmeldelseFilters";
import { getAllAnmeldelser } from "@/lib/anmeldelser";
import { absoluteUrl } from "@/lib/seo";

export const metadata: Metadata = {
  title: "Anmeldelser",
  description:
    "Dybdegående produktanmeldelser fra Saltet — én side per model, ærlig vurdering og klar købsguide.",
  alternates: { canonical: absoluteUrl("/anmeldelser") },
};

export default function AnmeldelserIndexPage() {
  const items = getAllAnmeldelser().map((item) => ({
    title: item.title,
    slug: item.slug,
    description: item.description,
    series: item.series,
    productName: item.productName,
    tags: item.tags,
    image: item.image,
    imageAlt: item.imageAlt,
    rating: item.rating,
    ratingCount: item.ratingCount,
  }));

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 md:px-8 md:py-16">
      <div className="mx-auto max-w-2xl text-center">
        <p className="mb-4 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
          Test · Dom · Købsguide
        </p>
        <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
          Anmeldelser
        </h1>
        <p className="mx-auto mt-4 max-w-xl leading-relaxed text-bone/55">
          Dybdegående produktanmeldelser — én side per model. Vi tester, vejer
          fordele og ulemper, og siger klart hvem grejet er til.
        </p>
      </div>

      <AnmeldelseFilters items={items} />
    </div>
  );
}
