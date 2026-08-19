import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { getAllGuides } from "@/lib/guides";
import { absoluteUrl } from "@/lib/seo";

export const metadata: Metadata = {
  title: "Guides",
  description:
    "Grundige madguides fra Saltet — airfryer, kernetemperatur, culotte, pizza, pulled pork, fermentering, syltning, røgning, grydebrød og smash burger. Metode først, opskrifter bagefter.",
  alternates: { canonical: absoluteUrl("/guides") },
};

export default function GuidesIndexPage() {
  const guides = getAllGuides();

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
          Lange, søgbare hub-artikler. Temperatur, saltprocent og fejlfinding —
          med direkte links til opskrifterne der evidensen ligger i.
        </p>
      </div>

      <div className="mt-14 grid gap-10 sm:grid-cols-2">
        {guides.map((guide) => (
          <Link
            key={guide.slug}
            href={`/guides/${guide.slug}`}
            className="group block text-left"
          >
            <article>
              <div className="relative aspect-[16/10] overflow-hidden rounded-2xl border-2 border-bone/20 bg-ash shadow-[4px_4px_0_0_rgba(212,255,0,0.35)] transition-[transform,box-shadow,border-color] duration-300 group-hover:-translate-y-1 group-hover:border-herb group-hover:shadow-[6px_6px_0_0_rgba(212,255,0,0.7)]">
                <Image
                  src={guide.image}
                  alt={guide.imageAlt}
                  fill
                  className="object-cover transition-transform duration-500 ease-out group-hover:scale-[1.05]"
                  sizes="(max-width: 768px) 100vw, 50vw"
                />
                <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-iron/55 via-transparent to-transparent" />
              </div>
              <h2 className="mt-4 font-serif text-xl uppercase leading-snug tracking-wide text-bone transition-colors group-hover:text-herb sm:text-2xl">
                {guide.title}
              </h2>
              <p className="mt-2 line-clamp-3 text-sm leading-relaxed text-bone/55">
                {guide.description}
              </p>
            </article>
          </Link>
        ))}
      </div>
    </div>
  );
}
