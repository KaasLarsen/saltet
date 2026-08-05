import type { Metadata } from "next";
import { absoluteUrl, siteConfig } from "@/lib/seo";

export const metadata: Metadata = {
  title: "Om Saltet",
  description:
    "Saltet er en dansk opskriftsside med fokus på enkle, lækre retter — startende med airfryer.",
  alternates: { canonical: absoluteUrl("/om") },
};

export default function AboutPage() {
  return (
    <div className="mx-auto max-w-3xl px-5 py-12 md:px-8 md:py-16">
      <p className="mb-4 text-[12px] uppercase tracking-[0.18em] text-herb">
        Om os
      </p>
      <h1 className="font-serif text-4xl text-ink md:text-5xl">
        Om {siteConfig.name}
      </h1>
      <div className="mt-8 space-y-5 leading-relaxed text-ink/70">
        <p>
          {siteConfig.name} er for dig, der vil lave god mad uden bøvl — men
          med smag. Vi tror på enkle opskrifter, klare trin og et køkken der
          føles ægte: træbord, sort jern og friske krydderurter.
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
