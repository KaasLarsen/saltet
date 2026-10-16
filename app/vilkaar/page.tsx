import type { Metadata } from "next";
import Link from "next/link";
import { absoluteUrl, siteConfig } from "@/lib/seo";

export const metadata: Metadata = {
  title: "Vilkår",
  description: `Vilkår for brug af ${siteConfig.name}, herunder hvordan vi bruger AI i indhold og billeder.`,
  alternates: { canonical: absoluteUrl("/vilkaar") },
};

export default function TermsPage() {
  return (
    <div className="mx-auto max-w-2xl px-5 py-12 text-center md:px-8 md:py-16">
      <p className="mb-4 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
        Vilkår
      </p>
      <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
        Vilkår for brug
      </h1>
      <div className="mt-8 space-y-5 text-left leading-relaxed text-bone/65 md:text-center">
        <p>
          Ved at bruge {siteConfig.name} accepterer du vilkårene herunder. De
          gælder for sitet og det indhold, vi viser.
        </p>

        <h2 className="pt-2 font-serif text-xl uppercase tracking-wide text-bone">
          AI i indhold og billeder
        </h2>
        <p>
          Vi bruger kunstig intelligens (AI) som hjælp til at producere
          indhold på {siteConfig.name} — herunder tekster til opskrifter,
          guides og beskrivelser samt billeder og visuelt materiale. AI er et
          værktøj i vores arbejdsgang; vi bestræber os på at gennemgå og
          tilpasse materialet, før det publiceres.
        </p>
        <p>
          Indholdet er ment som inspiration og vejledning i køkkenet. Det er
          ikke en garanti for resultat, smag, allergivenlighed eller
          fødevaresikkerhed. Du er selv ansvarlig for, hvordan du følger en
          opskrift — herunder temperaturer, tilberedningstid og håndtering af
          råvarer.
        </p>

        <h2 className="pt-2 font-serif text-xl uppercase tracking-wide text-bone">
          Brug af sitet
        </h2>
        <p>
          Du må læse, printe og bruge opskrifter til privat, ikke-kommerciel
          brug. Du må ikke kopiere, scrape eller genudgive store dele af
          indholdet uden tilladelse, eller udgive dig for at stå bag{" "}
          {siteConfig.name}.
        </p>

        <h2 className="pt-2 font-serif text-xl uppercase tracking-wide text-bone">
          Links og anbefalinger
        </h2>
        <p>
          Vi linker til produkter og butikker via affiliate-partnere (fx
          PriceRunner og Partner-ads). Det betyder, at vi kan få kommission,
          hvis du køber noget via et link. Anbefalingerne er valgt ud fra
          relevans for indholdet. Se også vores{" "}
          <Link
            href="/cookies"
            className="font-semibold text-herb underline decoration-herb/40 underline-offset-4 transition-colors hover:decoration-herb"
          >
            cookiepolitik
          </Link>{" "}
          og{" "}
          <Link
            href="/privatliv"
            className="font-semibold text-herb underline decoration-herb/40 underline-offset-4 transition-colors hover:decoration-herb"
          >
            privatlivspolitik
          </Link>
          .
        </p>

        <h2 className="pt-2 font-serif text-xl uppercase tracking-wide text-bone">
          Ansvar
        </h2>
        <p>
          {siteConfig.name} leveres som den er. Vi kan ikke holdes ansvarlige
          for tab, skader eller uheld, der opstår i forbindelse med brug af
          sitet eller forsøg på at følge vores opskrifter og guides — herunder
          fejl, mangler eller unøjagtigheder i tekst eller billeder, også når
          de er produceret med AI-hjælp.
        </p>
        <p>
          Vi kan ændre, rette eller fjerne indhold uden varsel. Vilkårene kan
          opdateres; den gældende version er altid den, der står på denne side.
        </p>

        <h2 className="pt-2 font-serif text-xl uppercase tracking-wide text-bone">
          Kontakt
        </h2>
        <p>
          Spørgsmål til vilkårene? Skriv til{" "}
          <a
            href={`mailto:${siteConfig.email}`}
            className="font-semibold text-herb underline decoration-herb/40 underline-offset-4 transition-colors hover:decoration-herb"
          >
            {siteConfig.email}
          </a>
          .
        </p>
      </div>
    </div>
  );
}
