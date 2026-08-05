import Image from "next/image";
import Link from "next/link";
import type { Recipe } from "@/lib/types";
import { formatDuration, difficultyLabel } from "@/lib/format";

interface RecipeCardProps {
  recipe: Recipe;
  priority?: boolean;
}

export function RecipeCard({ recipe, priority = false }: RecipeCardProps) {
  const href = `/opskrifter/${recipe.category}/${recipe.slug}`;

  return (
    <Link href={href} className="group block text-center sm:text-left">
      <article>
        <div className="relative aspect-[4/3] overflow-hidden border border-bone/15 bg-ash">
          <Image
            src={recipe.image}
            alt={recipe.imageAlt}
            fill
            className="object-cover transition-transform duration-700 ease-out group-hover:scale-[1.03]"
            sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
            priority={priority}
          />
          <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-iron/40 to-transparent" />
        </div>
        <div className="pt-4">
          <div className="mb-2 flex items-center justify-center gap-3 text-[11px] uppercase tracking-[0.14em] text-smoke sm:justify-start">
            <span>{formatDuration(recipe.totalTime)}</span>
            <span className="text-bone/20">·</span>
            <span>{difficultyLabel(recipe.difficulty)}</span>
          </div>
          <h2 className="font-serif text-2xl leading-snug text-bone transition-colors group-hover:text-wood">
            {recipe.title}
          </h2>
          <p className="mt-2 line-clamp-2 text-sm leading-relaxed text-bone/55">
            {recipe.description}
          </p>
        </div>
      </article>
    </Link>
  );
}
