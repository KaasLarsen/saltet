import type { RecipeEquipmentItem, RecipeFrontmatter } from "./types";

export type EquipmentId =
  | "airfryer"
  | "baal"
  | "dehydrator"
  | "fermentering"
  | "grill"
  | "gryde"
  | "meater"
  | "ovn"
  | "palaeg"
  | "pande"
  | "pizzaovn"
  | "plancha"
  | "roeg"
  | "roeremaskine"
  | "sous-vide"
  | "stobejern"
  | "sylte"
  | "trykkoger";

export interface ResolvedEquipment {
  id: EquipmentId | string;
  label: string;
}

const DEFAULT_LABELS: Record<string, string> = {
  airfryer: "Airfryer",
  baal: "Bål",
  dehydrator: "Dehydrator",
  fermentering: "Fermentering",
  grill: "Grill",
  gryde: "Gryde",
  meater: "MEATER",
  ovn: "Ovn",
  palaeg: "Pålæg",
  pande: "Pande",
  pizzaovn: "Pizzaovn",
  plancha: "Plancha",
  roeg: "Røg",
  roeremaskine: "Røremaskine",
  "sous-vide": "Sous vide",
  stobejern: "Støbejern",
  sylte: "Sylte",
  trykkoger: "Trykkoger",
};

/** Opskriftskategori → default grej-ikon. */
const CATEGORY_EQUIPMENT: Record<string, EquipmentId> = {
  airfryer: "airfryer",
  antipasti: "pande",
  baalmad: "baal",
  dehydrator: "dehydrator",
  dips: "gryde",
  fermentering: "fermentering",
  grill: "grill",
  gryde: "gryde",
  ovn: "ovn",
  palaeg: "palaeg",
  pande: "pande",
  pizzaovn: "pizzaovn",
  plancha: "plancha",
  roeg: "roeg",
  roeremaskine: "roeremaskine",
  "sous-vide": "sous-vide",
  stobejern: "stobejern",
  sylte: "sylte",
  trykkoger: "trykkoger",
};

export function equipmentLabel(id: string, override?: string): string {
  if (override?.trim()) return override.trim();
  return DEFAULT_LABELS[id] ?? id;
}

function normalizeItem(item: RecipeEquipmentItem): ResolvedEquipment | null {
  const id = item.id?.trim();
  if (!id) return null;
  return { id, label: equipmentLabel(id, item.label) };
}

/**
 * Eksplicit `equipment` hvis sat og ikke-tom; ellers ét ikon fra kategori.
 */
export function resolveEquipment(
  recipe: Pick<RecipeFrontmatter, "category" | "equipment">,
): ResolvedEquipment[] {
  const explicit = (recipe.equipment ?? [])
    .map(normalizeItem)
    .filter((item): item is ResolvedEquipment => item !== null);

  if (explicit.length > 0) return explicit;

  const fromCategory = CATEGORY_EQUIPMENT[recipe.category];
  if (fromCategory) {
    return [{ id: fromCategory, label: equipmentLabel(fromCategory) }];
  }

  return [];
}
