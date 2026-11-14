import type { ResolvedEquipment } from "@/lib/recipe-equipment";

function EquipmentSvg({ id }: { id: string }) {
  const common = {
    viewBox: "0 0 24 24",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: 1.75,
    strokeLinecap: "round" as const,
    strokeLinejoin: "round" as const,
    "aria-hidden": true as const,
    className: "h-5 w-5 shrink-0",
  };

  switch (id) {
    case "airfryer":
      return (
        <svg {...common}>
          <rect x="5" y="3" width="14" height="16" rx="2" />
          <path d="M8 19v2M16 19v2" />
          <circle cx="12" cy="11" r="3.5" />
          <path d="M12 9.5v3M10.5 11h3" />
        </svg>
      );
    case "plancha":
      return (
        <svg {...common}>
          <rect x="3" y="8" width="18" height="8" rx="1" />
          <path d="M6 16v2M18 16v2M8 8V6M16 8V6" />
        </svg>
      );
    case "meater":
      return (
        <svg {...common}>
          <path d="M4 12h11" />
          <path d="M15 12l4-2.5v5L15 12z" />
          <circle cx="7" cy="12" r="1.25" fill="currentColor" stroke="none" />
        </svg>
      );
    case "grill":
      return (
        <svg {...common}>
          <path d="M4 10h16" />
          <path d="M6 10v8M10 10v8M14 10v8M18 10v8" />
          <path d="M5 18h14" />
          <path d="M8 6c1 1.5 1 2.5 0 4M12 5c1 1.5 1 2.5 0 4M16 6c1 1.5 1 2.5 0 4" />
        </svg>
      );
    case "pizzaovn":
      return (
        <svg {...common}>
          <path d="M3 18h18" />
          <path d="M5 18V10a7 7 0 0 1 14 0v8" />
          <path d="M9 18v-3a3 3 0 0 1 6 0v3" />
        </svg>
      );
    case "stobejern":
      return (
        <svg {...common}>
          <path d="M5 10h11a3 3 0 0 1 3 3v3H5v-6z" />
          <path d="M5 16H3v-3a2 2 0 0 1 2-2" />
          <path d="M8 10V8M12 10V7" />
        </svg>
      );
    case "sous-vide":
      return (
        <svg {...common}>
          <rect x="7" y="3" width="10" height="18" rx="2" />
          <path d="M10 7h4M10 11h4M10 15h3" />
        </svg>
      );
    case "trykkoger":
      return (
        <svg {...common}>
          <path d="M6 9h12v10a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V9z" />
          <path d="M8 9V7a4 4 0 0 1 8 0v2" />
          <circle cx="12" cy="5" r="1" fill="currentColor" stroke="none" />
        </svg>
      );
    case "dehydrator":
      return (
        <svg {...common}>
          <rect x="4" y="3" width="16" height="18" rx="2" />
          <path d="M7 8h10M7 12h10M7 16h10" />
        </svg>
      );
    case "baal":
      return (
        <svg {...common}>
          <path d="M12 3c2 3 5 5 5 9a5 5 0 0 1-10 0c0-2 1.5-4 3-5 0 2 1 3 2 3 0-2 0-4 0-7z" />
          <path d="M5 21h14" />
        </svg>
      );
    case "ovn":
      return (
        <svg {...common}>
          <rect x="4" y="3" width="16" height="18" rx="2" />
          <path d="M4 8h16" />
          <circle cx="8" cy="5.5" r="0.75" fill="currentColor" stroke="none" />
          <circle cx="11" cy="5.5" r="0.75" fill="currentColor" stroke="none" />
          <rect x="7" y="11" width="10" height="7" rx="1" />
        </svg>
      );
    case "pande":
      return (
        <svg {...common}>
          <ellipse cx="10" cy="13" rx="7" ry="5" />
          <path d="M16.5 11.5L21 8" />
        </svg>
      );
    case "gryde":
      return (
        <svg {...common}>
          <path d="M6 10h12v8a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2v-8z" />
          <path d="M4 12h2M18 12h2" />
          <path d="M9 10V8a3 3 0 0 1 6 0v2" />
        </svg>
      );
    case "roeg":
      return (
        <svg {...common}>
          <path d="M8 20c0-4 2-5 2-8M12 20c0-5 3-6 3-10M16 20c0-3 1-4 1-7" />
          <path d="M5 20h14" />
        </svg>
      );
    case "roeremaskine":
      return (
        <svg {...common}>
          <path d="M8 4h8v4H8z" />
          <path d="M12 8v5" />
          <path d="M9 18c0-2.5 1.5-4 3-5 1.5 1 3 2.5 3 5H9z" />
        </svg>
      );
    case "fermentering":
      return (
        <svg {...common}>
          <path d="M8 4h8v3H8z" />
          <path d="M7 7h10v12a2 2 0 0 1-2 2H9a2 2 0 0 1-2-2V7z" />
          <path d="M10 12h4M10 15h4" />
        </svg>
      );
    case "palaeg":
      return (
        <svg {...common}>
          <rect x="3" y="6" width="14" height="12" rx="1" />
          <path d="M17 10h3v4h-3" />
          <path d="M6 10h8M6 13h6" />
        </svg>
      );
    case "sylte":
      return (
        <svg {...common}>
          <path d="M9 3h6v3H9z" />
          <path d="M8 6h8l1 14H7L8 6z" />
          <path d="M10 11h4" />
        </svg>
      );
    default:
      return (
        <svg {...common}>
          <circle cx="12" cy="12" r="7" />
          <path d="M12 9v3l2 2" />
        </svg>
      );
  }
}

interface RecipeEquipmentIconsProps {
  items: ResolvedEquipment[];
  className?: string;
}

export function RecipeEquipmentIcons({
  items,
  className,
}: RecipeEquipmentIconsProps) {
  if (items.length === 0) return null;

  return (
    <ul
      className={`mt-4 flex flex-wrap items-center justify-center gap-2 ${className ?? ""}`}
      aria-label="Nødvendigt grej"
    >
      {items.map((item) => (
        <li
          key={`${item.id}-${item.label}`}
          className="inline-flex items-center gap-2 rounded-xl border-2 border-bone/15 bg-ash/40 px-3 py-2 text-sm text-bone"
        >
          <span className="text-herb">
            <EquipmentSvg id={item.id} />
          </span>
          <span className="font-semibold tracking-wide">{item.label}</span>
        </li>
      ))}
    </ul>
  );
}
