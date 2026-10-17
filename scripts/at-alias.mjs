import path from "node:path";
import { pathToFileURL } from "node:url";

const root = path.resolve(import.meta.dirname, "..");

export async function resolve(specifier, context, nextResolve) {
  if (!specifier.startsWith("@/")) {
    return nextResolve(specifier, context);
  }
  const abs = path.join(root, specifier.slice(2));
  const candidates = [abs, `${abs}.ts`, `${abs}.tsx`, `${abs}.js`];
  let lastError;
  for (const candidate of candidates) {
    try {
      return await nextResolve(pathToFileURL(candidate).href, context);
    } catch (err) {
      lastError = err;
    }
  }
  throw lastError;
}
