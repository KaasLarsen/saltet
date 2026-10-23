interface AnmeldelseStarsProps {
  rating: number;
  count?: number;
  size?: "sm" | "md";
  align?: "center" | "start";
  className?: string;
}

function Star({ fill }: { fill: number }) {
  const clipped = Math.max(0, Math.min(1, fill));
  return (
    <span className="relative inline-block h-[1em] w-[1em]" aria-hidden>
      <svg viewBox="0 0 20 20" className="absolute inset-0 fill-bone/25">
        <path d="M10 1.6 12.4 6.5l5.4.8-3.9 3.8.9 5.4L10 14.1l-4.8 2.4.9-5.4L2.2 7.3l5.4-.8L10 1.6z" />
      </svg>
      {clipped > 0 ? (
        <span
          className="absolute inset-0 overflow-hidden"
          style={{ width: `${clipped * 100}%` }}
        >
          <svg viewBox="0 0 20 20" className="h-[1em] w-[1em] fill-herb">
            <path d="M10 1.6 12.4 6.5l5.4.8-3.9 3.8.9 5.4L10 14.1l-4.8 2.4.9-5.4L2.2 7.3l5.4-.8L10 1.6z" />
          </svg>
        </span>
      ) : null}
    </span>
  );
}

function formatDa(value: number): string {
  return value.toFixed(1).replace(".", ",");
}

/**
 * Read-only stjerner til produktanmeldelser (typisk PriceRunner-rating).
 */
export function AnmeldelseStars({
  rating,
  count,
  sourceLabel = "via PriceRunner",
  size = "md",
  align = "center",
  className = "",
}: AnmeldelseStarsProps) {
  if (!Number.isFinite(rating) || rating <= 0) return null;

  const sizeClass = size === "sm" ? "text-[14px]" : "text-[18px]";
  const alignClass = align === "start" ? "items-start" : "items-center";
  const votes =
    count != null && count > 0
      ? `${count.toLocaleString("da-DK")} ${count === 1 ? "bedømmelse" : "bedømmelser"}`
      : null;

  return (
    <div className={`flex flex-col gap-1 ${alignClass} ${className}`}>
      <div
        className={`flex items-center gap-2 ${sizeClass}`}
        title={`${formatDa(rating)} ud af 5`}
      >
        <span className="flex items-center gap-0.5" aria-hidden>
          {Array.from({ length: 5 }, (_, i) => (
            <Star key={i} fill={rating - i} />
          ))}
        </span>
        <span className="text-[13px] font-semibold tabular-nums text-bone">
          {formatDa(rating)}
        </span>
      </div>
      <p className="text-[10px] font-bold uppercase tracking-[0.14em] text-bone/40">
        {votes ? `${votes} · ${sourceLabel}` : sourceLabel}
      </p>
    </div>
  );
}
