import assert from "node:assert/strict";
import test from "node:test";

import {
  isRecipeRatingsStoreConfigured,
  isSupabaseRatingsBackend,
} from "./backend.ts";

const KEYS = [
  "NEXT_PUBLIC_SUPABASE_URL",
  "NEXT_PUBLIC_SUPABASE_ANON_KEY",
  "NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY",
  "RECIPE_RATINGS_BACKEND",
] as const;

function withEnv(
  values: Partial<Record<(typeof KEYS)[number], string | undefined>>,
  fn: () => void
): void {
  const previous = new Map<string, string | undefined>();
  for (const key of KEYS) {
    previous.set(key, process.env[key]);
    const next = values[key];
    if (next === undefined) delete process.env[key];
    else process.env[key] = next;
  }
  try {
    fn();
  } finally {
    for (const key of KEYS) {
      const value = previous.get(key);
      if (value === undefined) delete process.env[key];
      else process.env[key] = value;
    }
  }
}

test("Supabase-env alene aktiverer ikke ratings-backend", () => {
  withEnv(
    {
      NEXT_PUBLIC_SUPABASE_URL: "https://example.supabase.co",
      NEXT_PUBLIC_SUPABASE_ANON_KEY: "anon-key",
      RECIPE_RATINGS_BACKEND: undefined,
    },
    () => {
      assert.equal(isSupabaseRatingsBackend(), false);
      assert.equal(isRecipeRatingsStoreConfigured(), true);
    }
  );
});

test("RECIPE_RATINGS_BACKEND=supabase kræver også Supabase-env", () => {
  withEnv(
    {
      NEXT_PUBLIC_SUPABASE_URL: undefined,
      NEXT_PUBLIC_SUPABASE_ANON_KEY: undefined,
      RECIPE_RATINGS_BACKEND: "supabase",
    },
    () => {
      assert.equal(isSupabaseRatingsBackend(), false);
    }
  );

  withEnv(
    {
      NEXT_PUBLIC_SUPABASE_URL: "https://example.supabase.co",
      NEXT_PUBLIC_SUPABASE_ANON_KEY: "anon-key",
      RECIPE_RATINGS_BACKEND: "supabase",
    },
    () => {
      assert.equal(isSupabaseRatingsBackend(), true);
      assert.equal(isRecipeRatingsStoreConfigured(), true);
    }
  );
});

test("RECIPE_RATINGS_BACKEND er case-insensitive", () => {
  withEnv(
    {
      NEXT_PUBLIC_SUPABASE_URL: "https://example.supabase.co",
      NEXT_PUBLIC_SUPABASE_ANON_KEY: "anon-key",
      RECIPE_RATINGS_BACKEND: " Supabase ",
    },
    () => {
      assert.equal(isSupabaseRatingsBackend(), true);
    }
  );
});
