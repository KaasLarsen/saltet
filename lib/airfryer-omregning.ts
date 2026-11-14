export type OvenMode = "varmluft" | "over-undervarme";

export const OVEN_TEMP_MIN = 120;
export const OVEN_TEMP_MAX = 250;
export const OVEN_TIME_MIN = 1;
export const OVEN_TIME_MAX = 180;

export function clamp(value: number, min: number, max: number): number {
  if (!Number.isFinite(value)) return min;
  return Math.min(max, Math.max(min, value));
}

function roundTemp(celsius: number): number {
  return Math.round(celsius / 5) * 5;
}

function roundMinutes(minutes: number): number {
  if (minutes < 10) return Math.max(1, Math.round(minutes));
  return Math.round(minutes);
}

/**
 * Ovn → airfryer startpunkt.
 * Varmluft: −20 °C, ×0,80 tid.
 * Over/undervarme: +10 °C først, derefter −20 °C / ×0,75 tid.
 */
export function convertOvenToAirfryer(
  ovenTemp: number,
  ovenMinutes: number,
  mode: OvenMode,
): { temp: number; checkAt: number; timeFactor: number } {
  const temp = clamp(ovenTemp, OVEN_TEMP_MIN, OVEN_TEMP_MAX);
  const minutes = clamp(ovenMinutes, OVEN_TIME_MIN, OVEN_TIME_MAX);

  const equivalent = mode === "over-undervarme" ? temp + 10 : temp;
  const airTemp = roundTemp(equivalent - 20);
  const timeFactor = mode === "over-undervarme" ? 0.75 : 0.8;
  const checkAt = roundMinutes(minutes * timeFactor);

  return {
    temp: clamp(airTemp, 100, 230),
    checkAt,
    timeFactor,
  };
}
