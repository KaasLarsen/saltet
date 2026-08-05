import Link from "next/link";
import { tagHref } from "@/lib/tags";

interface RecipeTagsProps {
  tags: string[];
  className?: string;
}

export function RecipeTags({ tags, className = "" }: RecipeTagsProps) {
  if (!tags.length) return null;

  return (
    <div className={`flex flex-wrap justify-center gap-2 ${className}`}>
      {tags.map((tag) => (
        <Link
          key={tag}
          href={tagHref(tag)}
          className="border border-bone/20 px-3 py-1 text-[11px] uppercase tracking-[0.12em] text-bone/50 transition-colors hover:border-bone/45 hover:text-bone"
        >
          {tag}
        </Link>
      ))}
    </div>
  );
}
