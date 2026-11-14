import Image from "next/image";

interface FailSuccessCompareProps {
  successImage: string;
  successAlt: string;
  failImage?: string;
  failImageAlt?: string;
  symptom: string;
}

export function FailSuccessCompare({
  successImage,
  successAlt,
  failImage,
  failImageAlt,
  symptom,
}: FailSuccessCompareProps) {
  if (failImage) {
    return (
      <div
        className="grid gap-3 sm:grid-cols-2"
        aria-label={`Sammenligning: fejl vs. fix for ${symptom}`}
      >
        <figure className="relative overflow-hidden rounded-2xl border-2 border-wood/50">
          <div className="relative aspect-[4/3]">
            <Image
              src={failImage}
              alt={failImageAlt ?? `Mislykket: ${symptom}`}
              fill
              className="object-cover"
              sizes="(max-width: 640px) 100vw, 50vw"
            />
          </div>
          <figcaption className="absolute left-3 top-3 rotate-[-2deg] rounded-lg border-2 border-iron bg-wood px-2.5 py-1 text-[11px] font-bold uppercase tracking-[0.14em] text-iron">
            Fejl
          </figcaption>
        </figure>

        <figure className="relative overflow-hidden rounded-2xl border-2 border-herb/50">
          <div className="relative aspect-[4/3]">
            <Image
              src={successImage}
              alt={successAlt}
              fill
              className="object-cover"
              sizes="(max-width: 640px) 100vw, 50vw"
            />
          </div>
          <figcaption className="absolute left-3 top-3 rotate-[-2deg] rounded-lg border-2 border-iron bg-herb px-2.5 py-1 text-[11px] font-bold uppercase tracking-[0.14em] text-iron">
            Fix
          </figcaption>
        </figure>
      </div>
    );
  }

  return (
    <figure className="relative overflow-hidden rounded-2xl border-2 border-bone/15">
      <div className="relative aspect-[16/10]">
        <Image
          src={successImage}
          alt={successAlt}
          fill
          className="object-cover"
          sizes="(max-width: 768px) 100vw, 42rem"
          priority
        />
        <div className="absolute inset-0 bg-gradient-to-t from-stone/80 via-transparent to-transparent" />
      </div>
      <figcaption className="absolute bottom-4 left-4 right-4 flex flex-wrap items-end justify-between gap-2">
        <span className="rotate-[-2deg] rounded-lg border-2 border-iron bg-wood px-2.5 py-1 text-[11px] font-bold uppercase tracking-[0.14em] text-iron">
          Mål: red det her
        </span>
        <span className="max-w-[14rem] text-right text-sm text-bone/80">
          {symptom}
        </span>
      </figcaption>
    </figure>
  );
}
