import type { Metadata } from "next";
import { absoluteUrl, siteConfig } from "@/lib/seo";

export const metadata: Metadata = {
  title: "Om Saltet",
  description:
    "Saltet er en dansk opskriftsside med kant — enkle retter til airfryer, grill og mere.",
  alternates: { canonical: absoluteUrl("/om") },
};

export default function AboutPage() {
  return (
    <div className="mx-auto max-w-2xl px-5 py-12 text-center md:px-8 md:py-16">
      <p className="mb-4 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
        Om os
      </p>
      <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
        Om {siteConfig.name}
      </h1>
      <div className="mt-8 space-y-5 text-left leading-relaxed text-bone/65 md:text-center">
        <p>
          {siteConfig.name} er for dig, der vil lave god mad uden bøvl — men med
          smag og lidt attitude. Enkle opskrifter, klare trin, og et køkken der
          føles som en session: salt på alt, heat på højt, og zero snobberi.
        </p>
        <p>
          Vi starter med airfryer-opskrifter, fordi airfryeren er genial til
          hverdagen: hurtig, sprød og uden for meget rod.
        </p>
        <p>
          Flere kategorier kommer. Alle opskrifter skrives fra bunden med unikt
          indhold og egne billeder.
        </p>
      </div>
    </div>
  );
}
