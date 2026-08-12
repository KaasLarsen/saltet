import type { Metadata } from "next";
import { absoluteUrl, siteConfig } from "@/lib/seo";

export const metadata: Metadata = {
  title: "Kontakt",
  description: `Kontakt ${siteConfig.name} på ${siteConfig.email}.`,
  alternates: { canonical: absoluteUrl("/kontakt") },
};

export default function ContactPage() {
  return (
    <div className="mx-auto max-w-2xl px-5 py-12 text-center md:px-8 md:py-16">
      <p className="mb-4 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
        Skriv til os
      </p>
      <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
        Kontakt
      </h1>
      <div className="mt-8 space-y-5 text-left leading-relaxed text-bone/65 md:text-center">
        <p>
          Har du et spørgsmål, en rettelse eller bare lyst til at sige hej? Vi
          læser al mail — det kan bare tage et par dage.
        </p>
        <p>
          <a
            href={`mailto:${siteConfig.email}`}
            className="font-semibold text-herb underline decoration-herb/40 underline-offset-4 transition-colors hover:decoration-herb"
          >
            {siteConfig.email}
          </a>
        </p>
      </div>
    </div>
  );
}
