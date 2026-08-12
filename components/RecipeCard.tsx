import Image from "next/image";
import Link from "next/link";
import type { RecipeFrontmatter } from "@/lib/types";
import { formatDuration, difficultyLabel } from "@/lib/format";

interface RecipeCardProps {
  recipe: RecipeFrontmatter;
  priority?: boolean;
}

export function RecipeCard({ recipe, priority = false }: RecipeCardProps) {
  const href = `/opskrifter/${recipe.category}/${recipe.slug}`;

  return (
    <Link href={href} className="group block text-center sm:text-left">
      <article>
        <div className="relative aspect-[4/3] overflow-hidden rounded-2xl border-2 border-bone/20 bg-ash shadow-[4px_4px_0_0_rgba(212,255,0,0.35)] transition-[transform,box-shadow,border-color] duration-300 group-hover:-translate-y-1 group-hover:border-herb group-hover:shadow-[6px_6px_0_0_rgba(212,255,0,0.7)]">
          <Image
            src={recipe.image}
            alt={recipe.imageAlt}
            fill
            className="object-cover transition-transform duration-500 ease-out group-hover:scale-[1.05]"
            sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
            priority={priority}
          />
          <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-iron/50 via-transparent to-transparent" />
          <span className="absolute left-3 top-3 rounded-lg border-2 border-iron bg-herb px-2 py-0.5 text-[10px] font-bold uppercase tracking-[0.12em] text-iron">
            {formatDuration(recipe.totalTime)}
          </span>
        </div>
        <div className="pt-4">
          <div className="mb-2 flex items-center justify-center gap-3 text-[11px] font-semibold uppercase tracking-[0.14em] text-smoke sm:justify-start">
            <span>{difficultyLabel(recipe.difficulty)}</span>
            <span className="text-wood">·</span>
            <span className="text-bone/40">{recipe.category}</span>
          </div>
          <h2 className="font-serif text-xl uppercase leading-snug tracking-wide text-bone transition-colors group-hover:text-herb sm:text-2xl">
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
