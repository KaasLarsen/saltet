import type { FejlMatrixRow } from "@/lib/types";

interface FejlMatrixProps {
  rows: FejlMatrixRow[];
}

export function FejlMatrix({ rows }: FejlMatrixProps) {
  if (!rows.length) return null;

  return (
    <div className="space-y-8">
      {rows.map((row, index) => (
        <article
          key={`${row.symptom}-${index}`}
          className="overflow-hidden rounded-2xl border-2 border-bone/20 bg-ash/40"
        >
          <div className="border-b-2 border-wood/40 bg-wood/15 px-5 py-4">
            <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-wood">
              Symptom {index + 1}
            </p>
            <h3 className="mt-1 font-serif text-2xl uppercase tracking-wide text-bone">
              {row.symptom}
            </h3>
          </div>

          <div className="grid gap-0 md:grid-cols-2">
            <section className="border-b-2 border-bone/10 px-5 py-5 md:border-b-0 md:border-r-2">
              <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-herb">
                Fysikken bag
              </p>
              <p className="mt-2 leading-relaxed text-bone/70">{row.physics}</p>
            </section>

            <section className="px-5 py-5">
              <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-pool">
                Action-planen
              </p>
              <div className="mt-3 space-y-4">
                <div>
                  <p className="text-[11px] font-bold uppercase tracking-[0.14em] text-bone/45">
                    Nu
                  </p>
                  <p className="mt-1 leading-relaxed text-bone/80">{row.now}</p>
                </div>
                <div>
                  <p className="text-[11px] font-bold uppercase tracking-[0.14em] text-bone/45">
                    Næste gang
                  </p>
                  <p className="mt-1 leading-relaxed text-bone/80">
                    {row.nextTime}
                  </p>
                </div>
              </div>
            </section>
          </div>
        </article>
      ))}
    </div>
  );
}
