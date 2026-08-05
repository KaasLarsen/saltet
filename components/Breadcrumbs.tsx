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
      <ol className="flex flex-wrap items-center gap-2 text-sm text-charcoal/50">
        {items.map((item, index) => (
          <li key={item.label} className="flex items-center gap-2">
            {index > 0 && <span aria-hidden="true">/</span>}
            {item.href ? (
              <Link href={item.href} className="hover:text-charcoal">
                {item.label}
              </Link>
            ) : (
              <span className="text-charcoal/70">{item.label}</span>
            )}
          </li>
        ))}
      </ol>
    </nav>
  );
}
