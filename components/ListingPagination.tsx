import Link from "next/link";

interface ListingPaginationProps {
  currentPage: number;
  totalPages: number;
  /** Bygger href for en given side (1-indexeret). */
  hrefForPage: (page: number) => string;
}

export function ListingPagination({
  currentPage,
  totalPages,
  hrefForPage,
}: ListingPaginationProps) {
  if (totalPages <= 1) return null;

  const prev = currentPage > 1 ? currentPage - 1 : null;
  const next = currentPage < totalPages ? currentPage + 1 : null;

  return (
    <nav
      className="mt-12 flex flex-col items-center gap-4"
      aria-label="Sideinddeling"
    >
      <p className="text-[12px] uppercase tracking-[0.14em] text-bone/40">
        Side {currentPage} af {totalPages}
      </p>
      <div className="flex items-center gap-3">
        {prev ? (
          <Link
            href={hrefForPage(prev)}
            className="rounded-lg border-2 border-bone/25 px-4 py-2 text-[11px] font-bold uppercase tracking-[0.14em] text-bone/70 transition-colors hover:border-herb hover:text-herb"
            rel={prev === 1 ? undefined : "prev"}
          >
            Forrige
          </Link>
        ) : (
          <span className="rounded-lg border-2 border-bone/10 px-4 py-2 text-[11px] font-bold uppercase tracking-[0.14em] text-bone/25">
            Forrige
          </span>
        )}
        {next ? (
          <Link
            href={hrefForPage(next)}
            className="rounded-lg border-2 border-bone/25 px-4 py-2 text-[11px] font-bold uppercase tracking-[0.14em] text-bone/70 transition-colors hover:border-herb hover:text-herb"
            rel="next"
          >
            Næste
          </Link>
        ) : (
          <span className="rounded-lg border-2 border-bone/10 px-4 py-2 text-[11px] font-bold uppercase tracking-[0.14em] text-bone/25">
            Næste
          </span>
        )}
      </div>
    </nav>
  );
}
