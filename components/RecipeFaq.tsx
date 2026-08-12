import type { RecipeFaq } from "@/lib/types";

interface RecipeFaqProps {
  items: RecipeFaq[];
}

export function RecipeFaqSection({ items }: RecipeFaqProps) {
  if (!items?.length) return null;

  return (
    <section className="mt-14 text-left" aria-labelledby="faq-heading">
      <h2
        id="faq-heading"
        className="mb-6 text-center font-serif text-2xl uppercase tracking-wide text-bone"
      >
        Ofte stillede spørgsmål
      </h2>
      <div className="overflow-hidden rounded-2xl border-2 border-bone/20 divide-y divide-bone/10">
        {items.map((item) => (
          <details key={item.question} className="group bg-ash/30 px-4 py-4">
            <summary className="cursor-pointer list-none font-semibold text-bone marker:content-none [&::-webkit-details-marker]:hidden">
              <span className="flex items-start justify-between gap-4">
                <span>{item.question}</span>
                <span
                  aria-hidden="true"
                  className="mt-0.5 shrink-0 font-bold text-herb transition-transform group-open:rotate-45"
                >
                  +
                </span>
              </span>
            </summary>
            <p className="mt-3 leading-relaxed text-bone/65">{item.answer}</p>
          </details>
        ))}
      </div>
    </section>
  );
}
