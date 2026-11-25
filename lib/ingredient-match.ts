import type { IngredientNavItem } from "@/lib/ingredient-nav";
import type { Recipe } from "@/lib/types";

const aliasPatternCache = new Map<string, RegExp>();

function escapeRegex(value: string): string {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

/** Alias som selvstændigt token (ikke del af længere ord). */
export function aliasPattern(alias: string): RegExp {
  const key = alias.toLowerCase();
  const cached = aliasPatternCache.get(key);
  if (cached) return cached;

  const pattern = new RegExp(
    `(^|[^\\p{L}\\p{N}])${escapeRegex(key)}(?=[^\\p{L}\\p{N}]|$)`,
    "iu"
  );
  aliasPatternCache.set(key, pattern);
  return pattern;
}

/**
 * Strip mængder, markdown-links og parenteser, så aliases kan matches.
 * Eksempel: «8 mellemstore kartofler» → «mellemstore kartofler»
 *           «[Bøgerøget flagesalt](/opskrifter/…)» → «Bøgerøget flagesalt»
 */
export function normalizeIngredientLine(line: string): string {
  return line
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/\([^)]*\)/g, " ")
    .replace(
      /^[\d½¼¾⅓⅔.,\/\-–—\s]+(?:g|kg|mg|ml|cl|dl|l|tsk|spsk|stk|fed|bundt|pk|dåse|dasse|skive|skiver|nip|dråbe|draabe)?\.?\s*/iu,
      ""
    )
    .replace(/\s+/g, " ")
    .trim()
    .toLowerCase();
}

export function lineMatchesAlias(line: string, alias: string): boolean {
  const normalized = normalizeIngredientLine(line);
  if (!normalized || !alias.trim()) return false;
  return aliasPattern(alias.trim().toLowerCase()).test(normalized);
}

export function recipeMatchesIngredient(
  recipe: Pick<Recipe, "ingredients">,
  item: Pick<IngredientNavItem, "match">
): boolean {
  for (const line of recipe.ingredients) {
    for (const alias of item.match) {
      if (lineMatchesAlias(line, alias)) return true;
    }
  }
  return false;
}
