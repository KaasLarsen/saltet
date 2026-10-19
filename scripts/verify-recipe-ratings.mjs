#!/usr/bin/env node
/**
 * Smoke-test Supabase recipe-rating RPCs.
 * Usage: node --env-file=.env.local scripts/verify-recipe-ratings.mjs
 *    or: NEXT_PUBLIC_SUPABASE_URL=... NEXT_PUBLIC_SUPABASE_ANON_KEY=... node scripts/verify-recipe-ratings.mjs
 */
import { createClient } from "@supabase/supabase-js";
import { createHash, randomUUID } from "node:crypto";

const url = process.env.NEXT_PUBLIC_SUPABASE_URL?.trim();
const key =
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY?.trim() ||
  process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY?.trim();

if (!url || !key) {
  console.error(
    "Mangler NEXT_PUBLIC_SUPABASE_URL og NEXT_PUBLIC_SUPABASE_ANON_KEY"
  );
  process.exit(1);
}

const supabase = createClient(url, key, {
  auth: { persistSession: false, autoRefreshToken: false },
});

const kind = "recipe";
const slug = "airfryer/bacon";
const voterHash = createHash("sha256")
  .update(`verify:${randomUUID()}`)
  .digest("hex");
const ipHash = createHash("sha256").update(`verify-ip:${randomUUID()}`).digest("hex");

const { data: cast, error: castError } = await supabase.rpc("recipe_rating_cast", {
  p_kind: kind,
  p_slug: slug,
  p_voter_hash: voterHash,
  p_ip_hash: ipHash,
  p_rating: 5,
});

if (castError) {
  console.error("recipe_rating_cast fejlede:", castError.message);
  console.error(
    "Har du kørt supabase/recipe-ratings.sql i SQL Editor?"
  );
  process.exit(1);
}

const { data: summary, error: summaryError } = await supabase.rpc(
  "recipe_rating_summary",
  { p_kind: kind, p_slug: slug }
);
if (summaryError) {
  console.error("recipe_rating_summary fejlede:", summaryError.message);
  process.exit(1);
}

const { data: mine, error: mineError } = await supabase.rpc("recipe_rating_mine", {
  p_kind: kind,
  p_slug: slug,
  p_voter_hash: voterHash,
});
if (mineError) {
  console.error("recipe_rating_mine fejlede:", mineError.message);
  process.exit(1);
}

console.log("OK cast:", cast);
console.log("OK summary:", summary);
console.log("OK mine:", mine);
if (Number(mine) !== 5) {
  console.error("Forventede myRating=5");
  process.exit(1);
}
console.log("Supabase recipe ratings virker.");
