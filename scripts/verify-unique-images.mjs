#!/usr/bin/env node
/**
 * Fail if:
 * - duplicate binary image files exist under public/recipes/
 * - two recipes share the same frontmatter image path
 * - a recipe image path does not match /recipes/{category}/{slug}.jpg
 * - a referenced image file is missing under public/
 *
 * Usage: node scripts/verify-unique-images.mjs
 */
import { execSync } from "node:child_process";
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { join } from "node:path";

let failed = false;

function fail(message) {
  console.error(message);
  failed = true;
}

// --- Binary MD5 uniqueness ---
const out = execSync("find public/recipes -name '*.jpg' -exec md5sum {} +", {
  encoding: "utf8",
});
const hashToFiles = new Map();
for (const line of out.split("\n").filter(Boolean)) {
  const [hash, ...rest] = line.split(/\s+/);
  const file = rest.join(" ");
  if (!hashToFiles.has(hash)) hashToFiles.set(hash, []);
  hashToFiles.get(hash).push(file);
}

const dupes = [...hashToFiles.entries()].filter(([, files]) => files.length > 1);
if (dupes.length === 0) {
  console.log(`OK: ${hashToFiles.size} unique binary images, 0 duplicates`);
} else {
  fail(`FAIL: ${dupes.length} binary duplicate group(s)`);
  for (const [hash, files] of dupes
    .sort((a, b) => b[1].length - a[1].length)
    .slice(0, 20)) {
    console.error(`\n${files.length}x ${hash}`);
    for (const f of files) console.error(`  ${f}`);
  }
}

// --- Frontmatter path checks ---
function walkMdx(dir, acc = []) {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walkMdx(p, acc);
    else if (name.endsWith(".mdx")) acc.push(p);
  }
  return acc;
}

const recipes = walkMdx("content/recipes");
const imageToRecipes = new Map();
const pathMismatches = [];
const missingFiles = [];

for (const file of recipes) {
  const text = readFileSync(file, "utf8");
  const parts = text.split("---");
  if (parts.length < 3) continue;
  const front = parts[1];
  const slug = front.match(/^slug:\s*(.+)$/m)?.[1]?.trim().replace(/^["']|["']$/g, "");
  const category = front
    .match(/^category:\s*(.+)$/m)?.[1]
    ?.trim()
    .replace(/^["']|["']$/g, "");
  const image = front
    .match(/^image:\s*(.+)$/m)?.[1]
    ?.trim()
    .replace(/^["']|["']$/g, "");
  if (!slug || !category || !image) {
    fail(`FAIL: missing slug/category/image in ${file}`);
    continue;
  }

  const recipeId = `${category}/${slug}`;
  const expected = `/recipes/${category}/${slug}.jpg`;
  if (image !== expected) {
    pathMismatches.push({ recipeId, image, expected });
  }

  const publicPath = join("public", image.replace(/^\//, ""));
  if (!existsSync(publicPath)) {
    missingFiles.push({ recipeId, image });
  }

  if (!imageToRecipes.has(image)) imageToRecipes.set(image, []);
  imageToRecipes.get(image).push(recipeId);
}

const shared = [...imageToRecipes.entries()].filter(([, ids]) => ids.length > 1);

if (shared.length === 0) {
  console.log(
    `OK: ${imageToRecipes.size} unique frontmatter image paths across ${recipes.length} recipes`,
  );
} else {
  fail(`FAIL: ${shared.length} shared frontmatter image path(s)`);
  for (const [image, ids] of shared.sort((a, b) => a[0].localeCompare(b[0]))) {
    console.error(`\n${image}`);
    for (const id of ids) console.error(`  - ${id}`);
  }
}

if (pathMismatches.length === 0) {
  console.log("OK: all recipe image paths match /recipes/{category}/{slug}.jpg");
} else {
  fail(`FAIL: ${pathMismatches.length} image path(s) do not match slug convention`);
  for (const { recipeId, image, expected } of pathMismatches.slice(0, 30)) {
    console.error(`\n${recipeId}`);
    console.error(`  uses: ${image}`);
    console.error(`  expected: ${expected}`);
  }
}

if (missingFiles.length === 0) {
  console.log("OK: all referenced recipe image files exist under public/");
} else {
  fail(`FAIL: ${missingFiles.length} missing image file(s)`);
  for (const { recipeId, image } of missingFiles.slice(0, 30)) {
    console.error(`  ${recipeId} -> ${image}`);
  }
}

if (failed) process.exit(1);
process.exit(0);
