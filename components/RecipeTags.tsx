import Link from "next/link";
import {
  getTagBySlug,
  isIndexableBrowseTag,
  slugifyTag,
  tagHref,
} from "@/lib/tags";
import { holidayForTagSlug } from "@/lib/holiday-nav";
import { seasonForTagSlug } from "@/lib/season-nav";
import { topicForTagSlug } from "@/lib/topic-nav";

interface RecipeTagsProps {
  tags: string[];
  className?: string;
}

function isLinkableTag(tag: string): boolean {
  const slug = slugifyTag(tag);
  if (holidayForTagSlug(slug) || seasonForTagSlug(slug) || topicForTagSlug(slug)) {
    return true;
  }
  const info = getTagBySlug(slug);
  return info != null && isIndexableBrowseTag(info);
}

export function RecipeTags({ tags, className = "" }: RecipeTagsProps) {
  if (!tags.length) return null;

  return (
    <div className={`flex flex-wrap justify-center gap-2 ${className}`}>
      {tags.map((tag) => {
        const classNameChip =
          "rounded-lg border-2 border-bone/20 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.12em] text-bone/55 transition-colors hover:border-pool hover:text-pool";

        if (!isLinkableTag(tag)) {
          return (
            <span key={tag} className={classNameChip}>
              {tag}
            </span>
          );
        }

        return (
          <Link key={tag} href={tagHref(tag)} className={classNameChip}>
            {tag}
          </Link>
        );
      })}
    </div>
  );
}
