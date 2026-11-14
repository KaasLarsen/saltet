import Link from "next/link";
import { getFejlfindingGearName } from "@/lib/fejlfinding-nav";
import type { Fejlfinding } from "@/lib/types";

interface RecipeFejlfindingCtaProps {
  items: Fejlfinding[];
  recipeTitle?: string;
}

function ctaBlurb(item: Fejlfinding, recipeTitle?: string): string {
  const gear = getFejlfindingGearName(item.gear).toLowerCase();
  const title = recipeTitle?.toLowerCase() ?? "";
  const count = item.matrices.length;

  if (title.includes("onion")) {
    return `Blev de ikke sprøde? Se de ${count} hyppigste fejl med hytteost-dej i ${gear}en her.`;
  }
  if (title.includes("smash")) {
    return `Hænger den fast? Se de ${count} hyppigste fejl med smash-burgere på ${gear} her.`;
  }
  if (title.includes("oksehale") && title.includes("sovs")) {
    return `Skiller sovsen? Se de ${count} hyppigste fejl med oksehalesovs i trykkogeren her.`;
  }
  if (title.includes("oksehale") || title.includes("flæskesvær") || title.includes("flæskesteg")) {
    return `${item.symptom.replace(/\.$/, "")}? Se de ${count} hyppigste fejl i ${gear}en her.`;
  }

  const symptom = item.symptom.trim().replace(/\.$/, "");
  return `Gik det galt? ${symptom} — se fejlfinding til ${gear} her.`;
}

export function RecipeFejlfindingCta({
  items,
  recipeTitle,
}: RecipeFejlfindingCtaProps) {
  if (!items.length) return null;

  return (
    <section
      className="mt-14 text-left"
      aria-labelledby="fejlfinding-heading"
    >
      <h2
        id="fejlfinding-heading"
        className="mb-4 text-center font-serif text-2xl uppercase tracking-wide text-bone"
      >
        SOS: Red min mad
      </h2>
      <ul className="space-y-3">
        {items.map((item) => (
          <li key={item.slug}>
            <Link
              href={`/fejlfinding/${item.slug}`}
              className="block rounded-2xl border-2 border-wood/40 bg-wood/10 px-4 py-3 transition-colors hover:border-wood hover:bg-wood/20"
            >
              <span className="inline-flex rotate-[-1deg] rounded-md border-2 border-iron bg-wood px-2 py-0.5 text-[10px] font-bold uppercase tracking-[0.14em] text-iron">
                Fejlfinding
              </span>
              <span className="mt-2 block font-serif text-lg uppercase tracking-wide text-bone">
                {item.title}
              </span>
              <span className="mt-1 block text-sm text-bone/60">
                {ctaBlurb(item, recipeTitle)}
              </span>
            </Link>
          </li>
        ))}
      </ul>
    </section>
  );
}
