import assert from "node:assert/strict";
import test from "node:test";

import {
  __resetMantleCacheForTests,
  __setMantleFetchForTests,
  MantleRateLimitError,
  mantleCastRating,
  mantleReadSummary,
  mantleReadVoterRating,
} from "./mantle.ts";

const DOC = {
  v: 1 as const,
  recipes: {
    "recipe:airfryer/bacon": {
      voters: {
        voter_a: 5,
        voter_b: 3,
      },
    },
  },
};

function jsonResponse(body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}

test.beforeEach(() => {
  __resetMantleCacheForTests();
  __setMantleFetchForTests(null);
});

test.afterEach(() => {
  __resetMantleCacheForTests();
  __setMantleFetchForTests(null);
});

test("læsninger deler Mantle-doc cache (én fetch)", async () => {
  let fetches = 0;
  __setMantleFetchForTests(async () => {
    fetches += 1;
    return jsonResponse(DOC);
  });

  const summary = await mantleReadSummary("recipe", "airfryer/bacon");
  const mine = await mantleReadVoterRating(
    "recipe",
    "airfryer/bacon",
    "voter_a"
  );
  const again = await mantleReadSummary("recipe", "airfryer/bacon");

  assert.equal(fetches, 1);
  assert.deepEqual(summary, { average: 4, count: 2 });
  assert.equal(mine, 5);
  assert.deepEqual(again, { average: 4, count: 2 });
});

test("429 på læsning caches og undgår ekstra fetches", async () => {
  let fetches = 0;
  __setMantleFetchForTests(async () => {
    fetches += 1;
    return new Response("rate limited", { status: 429 });
  });

  const first = await mantleReadSummary("recipe", "airfryer/bacon");
  const second = await mantleReadSummary("recipe", "airfryer/bacon");
  const mine = await mantleReadVoterRating(
    "recipe",
    "airfryer/bacon",
    "voter_a"
  );

  assert.equal(fetches, 1);
  assert.deepEqual(first, { average: null, count: 0 });
  assert.deepEqual(second, { average: null, count: 0 });
  assert.equal(mine, null);
});

test("cast stopper med det samme ved 429 (ingen retries)", async () => {
  let fetches = 0;
  __setMantleFetchForTests(async (_url, init) => {
    fetches += 1;
    if (init?.method === "POST") {
      return new Response("rate limited", { status: 429 });
    }
    return jsonResponse(DOC);
  });

  await assert.rejects(
    () =>
      mantleCastRating({
        kind: "recipe",
        slug: "airfryer/bacon",
        rating: 4,
        voterHash: "voter_c",
      }),
    (err: unknown) => err instanceof MantleRateLimitError
  );

  // 1 GET + 1 POST — no retry storm
  assert.equal(fetches, 2);
});

test("succesfuld cast opdaterer cache uden ekstra GET", async () => {
  let fetches = 0;
  __setMantleFetchForTests(async (_url, init) => {
    fetches += 1;
    if (init?.method === "POST") {
      return new Response(null, { status: 200 });
    }
    return jsonResponse(DOC);
  });

  const summary = await mantleCastRating({
    kind: "recipe",
    slug: "airfryer/bacon",
    rating: 4,
    voterHash: "voter_c",
  });
  const mine = await mantleReadVoterRating(
    "recipe",
    "airfryer/bacon",
    "voter_c"
  );

  assert.equal(fetches, 2); // GET + POST only
  assert.equal(summary.count, 3);
  assert.equal(mine, 4);
});
