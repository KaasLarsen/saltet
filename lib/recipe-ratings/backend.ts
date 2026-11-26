import { isMantleRatingsConfigured } from "@/lib/recipe-ratings/mantle";
import { isSupabaseConfigured } from "@/lib/supabase/env";

/**
 * Supabase env is shared with newsletter. Ratings stay on Mantle unless
 * RECIPE_RATINGS_BACKEND=supabase is set (and recipe-ratings.sql is applied).
 */
export function isSupabaseRatingsBackend(): boolean {
  return (
    isSupabaseConfigured() &&
    process.env.RECIPE_RATINGS_BACKEND?.trim().toLowerCase() === "supabase"
  );
}

export function isRecipeRatingsStoreConfigured(): boolean {
  return isSupabaseRatingsBackend() || isMantleRatingsConfigured();
}
