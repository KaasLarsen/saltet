/**
 * Match søgestreng mod tekst: alle ord skal findes (AND), ikke hele frasen.
 * «syltede tomater» matcher «Syltede grønne tomater» og «syltede-cherrytomater».
 */
export function textMatchesQuery(haystack: string, query: string): boolean {
  const q = query.trim().toLowerCase();
  if (!q) return true;

  const hay = haystack.toLowerCase().replace(/[-_/]+/g, " ");
  const tokens = q.split(/\s+/).filter(Boolean);
  return tokens.every((token) => hay.includes(token));
}
