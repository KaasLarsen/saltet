import Image from "next/image";
import Link from "next/link";
import { RecipeCard } from "@/components/RecipeCard";
import { formatDuration, difficultyLabel } from "@/lib/format";
import type { RecipeFrontmatter } from "@/lib/types";

interface FeaturedRecipeSpotlightProps {
  recipes: RecipeFrontmatter[];
}

function CompactRecipeRow({ recipe }: { recipe: RecipeFrontmatter }) {
  const href = `/opskrifter/${recipe.category}/${recipe.slug}`;

  return (
    <Link href={href} className="group block">
      <article className="grid grid-cols-[7.5rem_1fr] gap-3 sm:grid-cols-[9rem_1fr] sm:gap-4">
        <div className="relative aspect-square overflow-hidden rounded-xl border-2 border-bone/20 bg-ash shadow-[3px_3px_0_0_rgba(212,255,0,0.3)] transition-[transform,border-color,box-shadow] duration-300 group-hover:-translate-y-0.5 group-hover:border-herb group-hover:shadow-[4px_4px_0_0_rgba(212,255,0,0.65)]">
          <Image
            src={recipe.image}
            alt={recipe.imageAlt}
            fill
            className="object-cover transition-transform duration-500 group-hover:scale-[1.05]"
            sizes="144px"
          />
        </div>
        <div className="flex min-w-0 flex-col justify-center py-0.5">
          <div className="mb-1 flex flex-wrap items-center gap-2 text-[10px] font-semibold uppercase tracking-[0.12em] text-smoke">
            <span>{formatDuration(recipe.totalTime)}</span>
            <span className="text-wood">·</span>
            <span>{difficultyLabel(recipe.difficulty)}</span>
          </div>
          <h3 className="font-serif text-lg uppercase leading-snug tracking-wide text-bone transition-colors group-hover:text-herb sm:text-xl">
            {recipe.title}
          </h3>
          <p className="mt-1 line-clamp-2 text-sm leading-relaxed text-bone/50">
            {recipe.description}
          </p>
        </div>
      </article>
    </Link>
  );
}

export function FeaturedRecipeSpotlight({
  recipes,
}: FeaturedRecipeSpotlightProps) {
  if (recipes.length === 0) return null;

  const [hero, ...rest] = recipes;
  const side = rest.slice(0, 3);
  const more = rest.slice(3, 7);

  return (
    <div className="space-y-10">
      <div className="grid items-start gap-8 lg:grid-cols-12 lg:gap-10">
        <Link
          href={`/opskrifter/${hero.category}/${hero.slug}`}
          className="group block lg:col-span-7"
        >
          <article>
            <div className="relative aspect-[4/3] overflow-hidden rounded-2xl border-2 border-bone/20 bg-ash shadow-[6px_6px_0_0_rgba(212,255,0,0.4)] transition-[transform,box-shadow,border-color] duration-300 group-hover:-translate-y-1 group-hover:border-herb group-hover:shadow-[8px_8px_0_0_rgba(212,255,0,0.7)] sm:aspect-[16/10] lg:min-h-[28rem] lg:aspect-auto">
              <Image
                src={hero.image}
                alt={hero.imageAlt}
                fill
                className="object-cover transition-transform duration-500 ease-out group-hover:scale-[1.04]"
                sizes="(max-width: 1024px) 100vw, 58vw"
                priority
              />
              <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-iron via-iron/40 to-transparent" />
              <span className="absolute left-4 top-4 rounded-lg border-2 border-iron bg-herb px-2.5 py-1 text-[11px] font-bold uppercase tracking-[0.14em] text-iron shadow-[3px_3px_0_0_rgba(255,92,57,0.85)]">
                Ugens ret
              </span>
              <div className="absolute inset-x-0 bottom-0 p-5 md:p-7">
                <div className="mb-2 flex flex-wrap items-center gap-3 text-[11px] font-semibold uppercase tracking-[0.14em] text-bone/70">
                  <span>{formatDuration(hero.totalTime)}</span>
                  <span className="text-wood">·</span>
                  <span>{difficultyLabel(hero.difficulty)}</span>
                  <span className="text-wood">·</span>
                  <span className="text-bone/45">{hero.category}</span>
                </div>
                <h3 className="font-serif text-3xl uppercase leading-[0.95] tracking-wide text-bone transition-colors group-hover:text-herb md:text-4xl lg:text-5xl">
                  {hero.title}
                </h3>
                <p className="mt-3 max-w-xl text-sm leading-relaxed text-bone/65 md:text-base">
                  {hero.description}
                </p>
              </div>
            </div>
          </article>
        </Link>

        {side.length > 0 ? (
          <div className="flex flex-col justify-center gap-5 lg:col-span-5 lg:min-h-[28rem]">
            {side.map((recipe) => (
              <CompactRecipeRow
                key={`${recipe.category}/${recipe.slug}`}
                recipe={recipe}
              />
            ))}
          </div>
        ) : null}
      </div>

      {more.length > 0 ? (
        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          {more.map((recipe) => (
            <RecipeCard
              key={`${recipe.category}/${recipe.slug}`}
              recipe={recipe}
            />
          ))}
        </div>
      ) : null}
    </div>
  );
}
