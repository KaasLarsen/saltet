import type { PartnerBannerConfig } from "@/lib/partners";

interface PartnerBannerProps {
  banner: PartnerBannerConfig;
}

export function PartnerBanner({ banner }: PartnerBannerProps) {
  return (
    <section className="mx-auto max-w-5xl px-5 py-10 md:px-8 md:py-12">
      <p className="mb-3 text-center text-[10px] font-bold uppercase tracking-[0.18em] text-bone/40">
        Annonce
      </p>
      <a
        href={banner.href}
        target="_blank"
        rel="nofollow noopener"
        className="block overflow-hidden rounded-2xl border-2 border-bone/20 bg-ash shadow-[4px_4px_0_0_rgba(212,255,0,0.35)] transition-[border-color,box-shadow] hover:border-herb hover:shadow-[6px_6px_0_0_rgba(212,255,0,0.7)]"
      >
        {/* Partner Ads tracking pixel — must stay a native img */}
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img
          src={banner.imgSrc}
          alt={banner.alt}
          className="mx-auto h-auto w-full max-w-full"
        />
      </a>
    </section>
  );
}
