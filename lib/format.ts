/** Konverter ISO 8601 varighed (PT25M, P14D, PT2D12H) til læsbar dansk tekst */
export function formatDuration(iso: string): string {
  const match = iso.match(
    /^P(?:(\d+)D)?(?:T(?:(\d+)D)?(?:(\d+)H)?(?:(\d+)M)?)?$/
  );
  if (!match) return iso;

  const days =
    (match[1] ? parseInt(match[1], 10) : 0) +
    (match[2] ? parseInt(match[2], 10) : 0);
  const hours = match[3] ? parseInt(match[3], 10) : 0;
  const minutes = match[4] ? parseInt(match[4], 10) : 0;

  const parts: string[] = [];
  if (days > 0) parts.push(`${days} dage`);
  if (hours > 0) parts.push(`${hours} t.`);
  if (minutes > 0) parts.push(`${minutes} min.`);

  return parts.join(" ") || "—";
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
    em: "Nem",
    mellem: "Mellem",
    ellem: "Mellem",
    svær: "Svær",
  };
  return labels[difficulty] ?? difficulty;
}
