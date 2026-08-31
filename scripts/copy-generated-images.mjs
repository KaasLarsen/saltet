#!/usr/bin/env node
/**
 * Copy GenerateImage artifacts (category--slug.jpg) to public/recipes paths.
 * Usage: node scripts/copy-generated-images.mjs [artifactsDir]
 */
import fs from "node:fs";
import path from "node:path";

const artifactsDir =
  process.argv[2] ?? "/opt/cursor/artifacts/assets";
const publicRoot = new URL("../public/recipes/", import.meta.url);

let copied = 0;
for (const file of fs.readdirSync(artifactsDir)) {
  if (!file.endsWith(".jpg")) continue;
  const match = file.match(/^(.+)--(.+)\.jpg$/);
  if (!match) continue;
  const [, category, slug] = match;
  const destDir = path.join(publicRoot.pathname, category);
  const dest = path.join(destDir, `${slug}.jpg`);
  fs.mkdirSync(destDir, { recursive: true });
  fs.copyFileSync(path.join(artifactsDir, file), dest);
  copied++;
}

console.log(`Copied ${copied} generated images to public/recipes/`);
