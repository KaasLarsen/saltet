import Image from "next/image";
import Link from "next/link";
import { AnmeldelseStars } from "@/components/AnmeldelseStars";
import type { GuideListItem } from "@/lib/guide-filters";

interface GuideCardProps {
  guide: GuideListItem;
  href?: string;
  /** PriceRunner-rating (kun anmeldelser). */
  rating?: number;
  ratingCount?: number;
}

export function GuideCard({ guide, href, rating, ratingCount }: GuideCardProps) {
  return (
    <Link href={href ?? `/guides/${guide.slug}`} className="group block text-left">
      <article>
        <div className="relative aspect-[16/10] overflow-hidden rounded-2xl border-2 border-bone/20 bg-ash shadow-[4px_4px_0_0_rgba(212,255,0,0.35)] transition-[transform,box-shadow,border-color] duration-300 group-hover:-translate-y-1 group-hover:border-herb group-hover:shadow-[6px_6px_0_0_rgba(212,255,0,0.7)]">
          <Image
            src={guide.image}
            alt={guide.imageAlt}
            fill
            quality={90}
            className="object-cover transition-transform duration-500 ease-out group-hover:scale-[1.05]"
            sizes="(max-width: 768px) 100vw, 50vw"
          />
          <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-iron/40 via-transparent to-transparent" />
        </div>
        <h2 className="mt-4 font-serif text-xl uppercase leading-snug tracking-wide text-bone transition-colors group-hover:text-herb sm:text-2xl">
          {guide.title}
        </h2>
        {rating != null && rating > 0 ? (
          <AnmeldelseStars
            rating={rating}
            count={ratingCount}
            size="sm"
            align="start"
            className="mt-2"
          />
        ) : null}
        <p className="mt-2 line-clamp-3 text-sm leading-relaxed text-bone/55">
          {guide.description}
        </p>
      </article>
    </Link>
  );
}
