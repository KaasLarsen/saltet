import type { Metadata } from "next";
import Link from "next/link";
import { absoluteUrl, siteConfig } from "@/lib/seo";

export const metadata: Metadata = {
  title: "Cookies",
  description: `Sådan bruger ${siteConfig.name} cookies.`,
  alternates: { canonical: absoluteUrl("/cookies") },
};

export default function CookiesPage() {
  return (
    <div className="mx-auto max-w-2xl px-5 py-12 text-center md:px-8 md:py-16">
      <p className="mb-4 text-[12px] uppercase tracking-[0.18em] text-herb">
        Cookiepolitik
      </p>
      <h1 className="font-serif text-4xl text-bone md:text-5xl">Cookies</h1>
      <div className="mt-8 space-y-5 text-left leading-relaxed text-bone/65 md:text-center">
        <p>
          {siteConfig.name} bruger kun teknisk nødvendige cookies, der får
          sitet til at virke — fx i forbindelse med hosting og sikkerhed.
        </p>
        <p>
          Vi sætter ikke cookies til markedsføring eller statistik, og vi
          deler ikke cookie-data med tredjeparter til annoncering.
        </p>
        <p>
          Du kan altid slette eller blokere cookies i din browsers
          indstillinger. Bemærk, at sitet kan fungere dårligere, hvis
          nødvendige cookies blokeres.
        </p>
        <p>
          Læs også vores{" "}
          <Link
            href="/privatliv"
            className="text-bone underline decoration-bone/25 underline-offset-4 transition-colors hover:decoration-wood"
          >
            privatlivspolitik
          </Link>
          .
        </p>
      </div>
    </div>
  );
}
