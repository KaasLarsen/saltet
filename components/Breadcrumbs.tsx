import Link from "next/link";

interface BreadcrumbItem {
  label: string;
  href?: string;
}

interface BreadcrumbsProps {
  items: BreadcrumbItem[];
}

export function Breadcrumbs({ items }: BreadcrumbsProps) {
  return (
    <nav aria-label="Brødkrumme" className="mb-6">
      <ol className="flex flex-wrap items-center justify-center gap-2 text-[11px] font-bold uppercase tracking-[0.12em] text-smoke">
        {items.map((item, index) => (
          <li key={item.label} className="flex items-center gap-2">
            {index > 0 && (
              <span aria-hidden="true" className="text-wood">
                /
              </span>
            )}
            {item.href ? (
              <Link
                href={item.href}
                className="transition-colors hover:text-herb"
              >
                {item.label}
              </Link>
            ) : (
              <span className="text-bone/70">{item.label}</span>
            )}
          </li>
        ))}
      </ol>
    </nav>
  );
}
