import type { Metadata } from "next";
import { FejlfindingHub } from "@/components/fejlfinding/FejlfindingHub";
import {
  getAllFejlfinding,
  getLegacyFejlfindingGuides,
} from "@/lib/fejlfinding";
import { buildFejlfindingIndexMetadata } from "@/lib/seo";

export const metadata: Metadata = buildFejlfindingIndexMetadata();

interface FejlfindingIndexPageProps {
  searchParams: Promise<{ grej?: string }>;
}

export default async function FejlfindingIndexPage({
  searchParams,
}: FejlfindingIndexPageProps) {
  const params = await searchParams;
  const items = getAllFejlfinding().map((item) => ({
    title: item.title,
    slug: item.slug,
    description: item.description,
    symptom: item.symptom,
    gear: item.gear,
    image: item.image,
    imageAlt: item.imageAlt,
    matrixCount: item.matrices.length,
  }));

  const legacyGuides = getLegacyFejlfindingGuides().map((guide) => ({
    title: guide.title,
    slug: guide.slug,
    description: guide.description,
  }));

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 md:px-8 md:py-16">
      <div className="mx-auto max-w-2xl text-center">
        <p className="mb-4 inline-flex animate-pulse rotate-[-2deg] rounded-lg border-2 border-iron bg-wood px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
          SOS · Red min mad
        </p>
        <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
          Hjælp, min session fejlede!
        </h1>
        <p className="mx-auto mt-4 max-w-xl leading-relaxed text-bone/55">
          Drop de lange historier. Vælg dit grej, find symptomet, få fysikken og
          action-planen — redningen lige nu, og hvordan du undgår det næste gang.
        </p>
      </div>

      <FejlfindingHub
        key={params.grej ?? "alle"}
        items={items}
        legacyGuides={legacyGuides}
        initialGear={params.grej}
      />
    </div>
  );
}
