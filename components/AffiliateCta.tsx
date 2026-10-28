import Image from "next/image";
import {
  affiliateVariantLabel,
  getAffiliateOffer,
  type AffiliateOffer,
  type AffiliateVariant,
} from "@/lib/affiliate";
import {
  outboundLinkAttrs,
  withOutboundSurface,
  type OutboundSurface,
} from "@/lib/outbound";

interface AffiliateCtaProps {
  /** Lookup i det centrale affiliate-register. */
  id?: string;
  /** Eller send et færdigt offer (fx fra getAffiliateOfferForRecipe). */
  offer?: AffiliateOffer;
  /** Overskriv variant-eyebrow (fx “Annonce”). */
  eyebrow?: string;
  /** Page type for click attribution. */
  surface?: OutboundSurface;
  className?: string;
}

const variantShadow: Record<AffiliateVariant, string> = {
  grej: "shadow-[4px_4px_0_0_rgba(212,255,0,0.35)]",
  grocery: "shadow-[4px_4px_0_0_rgba(212,255,0,0.35)]",
  meal_kit: "shadow-[4px_4px_0_0_rgba(255,92,57,0.35)]",
  wine: "shadow-[4px_4px_0_0_rgba(255,92,57,0.35)]",
};

/**
 * Native produkt-/CPA-anbefaling i Saltet-designsprog.
 * Understøtter grej nu; grocery / meal_kit / wine når partnere lander.
 * Produktbillede kommer fra Partner-ads feed (`billedurl`) når sat.
 */
function sharpenCtaLabel(offer: AffiliateOffer): string {
  if (offer.ctaLabel === "Sammenlign priser") return "Se laveste pris";
  if (offer.ctaLabel === "Se aktuel pris") return "Se laveste pris";
  return offer.ctaLabel;
}

export function AffiliateCta({
  id,
  offer: offerProp,
  eyebrow,
  surface = "other",
  className = "",
}: AffiliateCtaProps) {
  const offer = offerProp ?? (id ? getAffiliateOffer(id) : undefined);
  if (!offer) return null;

  const label = eyebrow ?? affiliateVariantLabel(offer.variant);
  const imageAlt = offer.imageAlt ?? offer.label;
  const href = withOutboundSurface(offer.href, surface);
  const linkAttrs = outboundLinkAttrs(surface, {
    offerId: offer.id,
    merchant: offer.merchant,
  });
  const ctaLabel = sharpenCtaLabel(offer);

  return (
    <aside
      className={`my-8 overflow-hidden rounded-2xl border-2 border-bone/20 bg-ash/40 text-left ${variantShadow[offer.variant]} ${className}`}
    >
      <div className="flex items-center justify-between gap-3 border-b border-bone/10 px-4 py-3">
        <p className="text-[11px] font-bold uppercase tracking-[0.14em] text-herb">
          {label}
        </p>
        <p className="text-[10px] font-bold uppercase tracking-[0.14em] text-bone/35">
          Annonce
        </p>
      </div>
      <div
        className={
          offer.image
            ? "grid gap-0 sm:grid-cols-[minmax(0,11rem)_1fr]"
            : undefined
        }
      >
        {offer.image ? (
          <a
            href={href}
            target="_blank"
            rel="nofollow noopener sponsored"
            className="relative block aspect-square h-full min-h-[11rem] bg-iron/80 sm:aspect-auto"
            {...linkAttrs}
          >
            <Image
              src={offer.image}
              alt={imageAlt}
              fill
              className="object-contain p-4"
              sizes="(max-width: 640px) 100vw, 11rem"
            />
          </a>
        ) : null}
        <div className="px-5 py-5">
          <p className="font-serif text-xl uppercase tracking-wide text-bone">
            {offer.label}
          </p>
          <p className="mt-2 text-sm leading-relaxed text-bone/65">
            {offer.description}
          </p>
          <a
            href={href}
            target="_blank"
            rel="nofollow noopener sponsored"
            className="mt-4 inline-flex items-center gap-2 rounded-xl border-2 border-herb bg-herb px-4 py-2.5 text-sm font-semibold text-iron transition-colors hover:bg-herb/85"
            {...linkAttrs}
          >
            {ctaLabel}
            <span className="text-xs text-iron/70" aria-hidden>
              · {offer.merchant}
            </span>
          </a>
        </div>
      </div>
    </aside>
  );
}
