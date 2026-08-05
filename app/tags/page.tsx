import type { Metadata } from "next";
import Link from "next/link";
import { getAllTags } from "@/lib/tags";
import { absoluteUrl, siteConfig } from "@/lib/seo";

export const metadata: Metadata = {
  title: "Tags",
  description: `Gennemse alle opskrifts-tags på ${siteConfig.name} — hurtig, vegetar, kylling og mere.`,
  alternates: { canonical: absoluteUrl("/tags") },
};

export default function TagsIndexPage() {
  const tags = getAllTags();

  return (
    <div className="mx-auto max-w-5xl px-5 py-12 text-center md:px-8 md:py-16">
      <h1 className="font-serif text-4xl text-bone md:text-5xl">Tags</h1>
      <p className="mx-auto mt-4 max-w-xl text-bone/55 leading-relaxed">
        Find opskrifter via emne — klik på et tag for at se alle matchende
        retter.
      </p>
      <div className="mx-auto mt-12 flex max-w-3xl flex-wrap justify-center gap-3">
        {tags.map((tag) => (
          <Link
            key={tag.slug}
            href={`/tags/${tag.slug}`}
            className="border border-bone/20 px-4 py-2 text-[12px] uppercase tracking-[0.14em] text-bone/65 transition-colors hover:border-bone/45 hover:text-bone"
          >
            {tag.label}
            <span className="ml-2 text-smoke">{tag.count}</span>
          </Link>
        ))}
      </div>
    </div>
  );
}
