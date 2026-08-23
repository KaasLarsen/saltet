import type { Metadata } from "next";
import { GrejFilters } from "@/components/GrejFilters";
import { getAllGrej } from "@/lib/grej";
import { absoluteUrl } from "@/lib/seo";

export const metadata: Metadata = {
  title: "Grej",
  description:
    "Udstyr og grej fra Saltet — tests, købsguider og vedligeholdelse af airfryer, pizzaovn, støbejern, trækul og båludstyr. Hardware først, opskrifter bagefter.",
  alternates: { canonical: absoluteUrl("/grej") },
};

export default function GrejIndexPage() {
  const items = getAllGrej().map((item) => ({
    title: item.title,
    slug: item.slug,
    description: item.description,
    tags: item.tags,
    track: item.track,
    image: item.image,
    imageAlt: item.imageAlt,
  }));

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 md:px-8 md:py-16">
      <div className="mx-auto max-w-2xl text-center">
        <p className="mb-4 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
          Hardware · Test · Setup
        </p>
        <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
          Grej
        </h1>
        <p className="mx-auto mt-4 max-w-xl leading-relaxed text-bone/55">
          {items.length} artikler — pander, ovne og kul, med priser via
          PriceRunner og links til opskrifterne grejet skal bruges i.
        </p>
      </div>

      <GrejFilters items={items} />
    </div>
  );
}
