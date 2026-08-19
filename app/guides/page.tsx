import type { Metadata } from "next";
import { GuideFilters } from "@/components/GuideFilters";
import { getAllGuides } from "@/lib/guides";
import { absoluteUrl } from "@/lib/seo";

export const metadata: Metadata = {
  title: "Guides",
  description:
    "Grundige madguides fra Saltet — saltprocenter, kernetemperatur, sous vide, røgning, koji, confit, bål, trykkoger og stegeoverflader. Metode først, opskrifter bagefter.",
  alternates: { canonical: absoluteUrl("/guides") },
};

export default function GuidesIndexPage() {
  const guides = getAllGuides().map((guide) => ({
    title: guide.title,
    slug: guide.slug,
    description: guide.description,
    tags: guide.tags,
    image: guide.image,
    imageAlt: guide.imageAlt,
  }));

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 md:px-8 md:py-16">
      <div className="mx-auto max-w-2xl text-center">
        <p className="mb-4 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
          Metode · Teknik · Links
        </p>
        <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
          Guides
        </h1>
        <p className="mx-auto mt-4 max-w-xl leading-relaxed text-bone/55">
          {guides.length} guides — temperatur, saltprocent og fejlfinding, med
          links til opskrifterne evidensen ligger i.
        </p>
      </div>

      <GuideFilters guides={guides} />
    </div>
  );
}
