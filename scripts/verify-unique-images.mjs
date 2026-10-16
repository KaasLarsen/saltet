#!/usr/bin/env node
/**
 * Fail if any duplicate image files exist under public/recipes/.
 * Usage: node scripts/verify-unique-images.mjs
 */
import { execSync } from "node:child_process";

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
  console.log(`OK: ${hashToFiles.size} unique images, 0 duplicates`);
  process.exit(0);
}

console.error(`FAIL: ${dupes.length} duplicate group(s)`);
for (const [hash, files] of dupes.sort((a, b) => b[1].length - a[1].length).slice(0, 20)) {
  console.error(`\n${files.length}x ${hash}`);
  for (const f of files) console.error(`  ${f}`);
}
process.exit(1);
