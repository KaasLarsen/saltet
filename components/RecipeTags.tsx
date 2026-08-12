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
          className="rounded-lg border-2 border-bone/20 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.12em] text-bone/55 transition-colors hover:border-pool hover:text-pool"
        >
          {tag}
        </Link>
      ))}
    </div>
  );
}
