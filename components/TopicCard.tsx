import Image from "next/image";
import Link from "next/link";
import type { Topic } from "@/lib/types";

interface TopicCardProps {
  topic: Topic;
  count: number;
  image: string;
  imageAlt: string;
  priority?: boolean;
}

export function TopicCard({
  topic,
  count,
  image,
  imageAlt,
  priority = false,
}: TopicCardProps) {
  return (
    <Link
      href={`/emner/${topic.slug}`}
      className="group block text-center sm:text-left"
    >
      <article>
        <div className="relative aspect-[4/3] overflow-hidden rounded-2xl border-2 border-bone/20 bg-ash shadow-[4px_4px_0_0_rgba(212,255,0,0.35)] transition-[transform,box-shadow,border-color] duration-300 group-hover:-translate-y-1 group-hover:border-herb group-hover:shadow-[6px_6px_0_0_rgba(212,255,0,0.7)]">
          {image ? (
            <Image
              src={image}
              alt={imageAlt}
              fill
              className="object-cover transition-transform duration-500 ease-out group-hover:scale-[1.05]"
              sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
              priority={priority}
            />
          ) : null}
          <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-iron/50 via-transparent to-transparent" />
          <span className="absolute left-3 top-3 rounded-lg border-2 border-iron bg-herb px-2 py-0.5 text-[10px] font-bold uppercase tracking-[0.12em] text-iron">
            {count} opskrift{count === 1 ? "" : "er"}
          </span>
        </div>
        <div className="pt-4">
          <h2 className="font-serif text-xl uppercase leading-snug tracking-wide text-bone transition-colors group-hover:text-herb sm:text-2xl">
            {topic.name}
          </h2>
          <p className="mt-2 line-clamp-2 text-sm leading-relaxed text-bone/55">
            {topic.description}
          </p>
        </div>
      </article>
    </Link>
  );
}
