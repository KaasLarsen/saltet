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
    <Link href={href} className="group block">
      <article className="overflow-hidden rounded-2xl bg-white shadow-sm ring-1 ring-charcoal/5 transition-shadow hover:shadow-md">
        <div className="relative aspect-[4/3] overflow-hidden">
          <Image
            src={recipe.image}
            alt={recipe.imageAlt}
            fill
            className="object-cover transition-transform duration-500 group-hover:scale-105"
            sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
            priority={priority}
          />
        </div>
        <div className="p-5">
          <div className="mb-2 flex items-center gap-3 text-xs text-charcoal/50">
            <span>{formatDuration(recipe.totalTime)}</span>
            <span>·</span>
            <span>{difficultyLabel(recipe.difficulty)}</span>
          </div>
          <h2 className="font-serif text-xl font-medium text-charcoal group-hover:text-accent transition-colors">
            {recipe.title}
          </h2>
          <p className="mt-2 line-clamp-2 text-sm text-charcoal/65 leading-relaxed">
            {recipe.description}
          </p>
        </div>
      </article>
    </Link>
  );
}
