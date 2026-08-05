/** Konverter ISO 8601 varighed (PT25M) til læsbar dansk tekst */
export function formatDuration(iso: string): string {
  const match = iso.match(/PT(?:(\d+)H)?(?:(\d+)M)?/);
  if (!match) return iso;

  const hours = match[1] ? parseInt(match[1], 10) : 0;
  const minutes = match[2] ? parseInt(match[2], 10) : 0;

  const parts: string[] = [];
  if (hours > 0) parts.push(`${hours} t.`);
  if (minutes > 0) parts.push(`${minutes} min.`);

  return parts.join(" ") || iso;
}

export function formatDate(dateStr: string): string {
  return new Intl.DateTimeFormat("da-DK", {
    day: "numeric",
    month: "long",
    year: "numeric",
  }).format(new Date(dateStr));
}

export function difficultyLabel(difficulty: string): string {
  const labels: Record<string, string> = {
    nem: "Nem",
    mellem: "Mellem",
    svær: "Svær",
  };
  return labels[difficulty] ?? difficulty;
}
