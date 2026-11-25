import Link from "next/link";
import type { IngredientIdeasEntry } from "@/lib/ingredient-ideas";

interface IngredientIdeasProps {
  entry: IngredientIdeasEntry;
}

export function IngredientIdeas({ entry }: IngredientIdeasProps) {
  return (
    <div className="mx-auto mt-10 max-w-2xl text-left">
      <p className="text-center text-sm leading-relaxed text-bone/60">
        {entry.blurb}
      </p>
      <h2 className="mt-8 text-center font-serif text-xl uppercase tracking-wide text-bone md:text-2xl">
        Opskriftsidéer
      </h2>
      <ul className="mt-6 space-y-5">
        {entry.ideas.map((idea) => (
          <li key={idea.title} className="border-l-2 border-wood/50 pl-4">
            {idea.recipeHref ? (
              <Link
                href={idea.recipeHref}
                className="font-serif text-lg text-bone transition-colors hover:text-herb"
              >
                {idea.title}
              </Link>
            ) : (
              <p className="font-serif text-lg text-bone">{idea.title}</p>
            )}
            <p className="mt-1 text-sm leading-relaxed text-bone/50">
              {idea.description}
            </p>
          </li>
        ))}
      </ul>
    </div>
  );
}
