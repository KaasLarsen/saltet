import type { Metadata } from "next";
import Link from "next/link";
import { absoluteUrl, siteConfig } from "@/lib/seo";

export const metadata: Metadata = {
  title: "Privatlivspolitik",
  description: `Privatlivspolitik for ${siteConfig.name}.`,
  alternates: { canonical: absoluteUrl("/privatliv") },
};

export default function PrivacyPage() {
  return (
    <div className="mx-auto max-w-2xl px-5 py-12 text-center md:px-8 md:py-16">
      <p className="mb-4 text-[12px] uppercase tracking-[0.18em] text-herb">
        Privatliv
      </p>
      <h1 className="font-serif text-4xl text-bone md:text-5xl">
        Privatlivspolitik
      </h1>
      <div className="mt-8 space-y-5 text-left leading-relaxed text-bone/65 md:text-center">
        <p>
          {siteConfig.name} respekterer dit privatliv. Vi indsamler ikke
          personoplysninger via formularer, konti eller nyhedsbreve.
        </p>
        <p>
          Skriver du til os på{" "}
          <a
            href={`mailto:${siteConfig.email}`}
            className="text-bone underline decoration-bone/25 underline-offset-4 transition-colors hover:decoration-wood"
          >
            {siteConfig.email}
          </a>
          , behandler vi din mail kun for at kunne svare dig. Vi sælger eller
          deler ikke dine oplysninger.
        </p>
        <p>
          Sitet hostes hos en hostingudbyder, som kan logge tekniske data
          (fx IP-adresse og tidspunkt) af hensyn til drift og sikkerhed.
        </p>
        <p>
          Om cookies: se vores{" "}
          <Link
            href="/cookies"
            className="text-bone underline decoration-bone/25 underline-offset-4 transition-colors hover:decoration-wood"
          >
            cookiepolitik
          </Link>
          .
        </p>
        <p>
          Spørgsmål om privatliv? Skriv til{" "}
          <a
            href={`mailto:${siteConfig.email}`}
            className="text-bone underline decoration-bone/25 underline-offset-4 transition-colors hover:decoration-wood"
          >
            {siteConfig.email}
          </a>
          .
        </p>
      </div>
    </div>
  );
}
