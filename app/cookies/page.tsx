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
      <p className="mb-4 inline-flex rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-3 py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-iron">
        Cookiepolitik
      </p>
      <h1 className="font-serif text-4xl uppercase tracking-wide text-bone md:text-5xl">
        Cookies
      </h1>
      <div className="mt-8 space-y-5 text-left leading-relaxed text-bone/65 md:text-center">
        <p>
          {siteConfig.name} bruger teknisk nødvendige cookies, der får sitet
          til at virke — fx i forbindelse med hosting og sikkerhed.
        </p>
        <p>
          På grej-sider indlejrer vi PriceRunner-widgets, så du kan se aktuelle
          priser. PriceRunner kan sætte egne cookies og måle klik, når du
          interagerer med widgetten eller åbner deres site. Vi bruger
          adrunner-id <span className="text-bone/80">adrunner_dk_online-opskrift</span>,
          så provision kan tilskrives Saltet.
        </p>
        <p>
          Vi sætter ikke egne cookies til markedsføring eller statistik. Google
          AdSense kan indlæse tredjepartsscripts på sider, hvor annoncer vises.
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
            className="font-semibold text-herb underline decoration-herb/40 underline-offset-4 transition-colors hover:decoration-herb"
          >
            privatlivspolitik
          </Link>
          .
        </p>
      </div>
    </div>
  );
}
