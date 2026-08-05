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
      <h1 className="font-serif text-3xl font-medium text-charcoal md:text-4xl">
        Om {siteConfig.name}
      </h1>
      <div className="mt-8 space-y-5 text-charcoal/75 leading-relaxed">
        <p>
          {siteConfig.name} er en opskriftsside for dig, der vil lave god mad
          uden bøvl. Vi tror på enkle opskrifter med få ingredienser, klare
          trin og resultater, der smager af mere end de tager tid at lave.
        </p>
        <p>
          Vi starter med airfryer-opskrifter — fordi airfryeren er genial til
          hverdagen: hurtig opvarmning, sprøde resultater og mindre rod end en
          traditionel ovn.
        </p>
        <p>
          Flere kategorier kommer løbende. Alle opskrifter er skrevet fra
          bunden med unikt indhold og egne billeder.
        </p>
      </div>
    </div>
  );
}
