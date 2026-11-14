"use client";

import { useId, useState } from "react";
import {
  OVEN_TEMP_MAX,
  OVEN_TEMP_MIN,
  OVEN_TIME_MAX,
  OVEN_TIME_MIN,
  clamp,
  convertOvenToAirfryer,
  type OvenMode,
} from "@/lib/airfryer-omregning";

interface AirfryerOmregnerProps {
  className?: string;
}

export function AirfryerOmregner({ className }: AirfryerOmregnerProps) {
  const tempId = useId();
  const timeId = useId();
  const modeId = useId();
  const [ovenTemp, setOvenTemp] = useState(200);
  const [ovenMinutes, setOvenMinutes] = useState(30);
  const [mode, setMode] = useState<OvenMode>("varmluft");

  const result = convertOvenToAirfryer(ovenTemp, ovenMinutes, mode);
  const percentLess = Math.round((1 - result.timeFactor) * 100);

  return (
    <aside
      className={`overflow-hidden rounded-2xl border-2 border-bone/20 bg-ash/40 ${className ?? "my-10"}`}
      aria-label="Airfryer-omregner"
    >
      <div className="border-b border-bone/10 bg-ash/80 px-5 py-3">
        <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-herb">
          Airfryer-omregner
        </p>
        <p className="mt-1 text-sm text-bone/60">
          Ovn-tal ind → airfryer-start ud. Typisk −20 °C og −{percentLess} % tid.
        </p>
      </div>

      <div className="grid gap-6 p-5 sm:grid-cols-3">
        <div>
          <label
            htmlFor={tempId}
            className="mb-2 block text-[11px] font-bold uppercase tracking-[0.12em] text-bone/50"
          >
            Ovn °C
          </label>
          <div className="relative">
            <input
              id={tempId}
              type="number"
              inputMode="numeric"
              min={OVEN_TEMP_MIN}
              max={OVEN_TEMP_MAX}
              step={5}
              value={ovenTemp}
              onChange={(e) =>
                setOvenTemp(
                  clamp(Number(e.target.value) || 0, OVEN_TEMP_MIN, OVEN_TEMP_MAX),
                )
              }
              className="w-full rounded-xl border-2 border-bone/20 bg-iron px-4 py-3 pr-12 font-serif text-2xl text-bone outline-none focus:border-herb"
            />
            <span className="pointer-events-none absolute right-4 top-1/2 -translate-y-1/2 font-serif text-xl text-bone/40">
              °C
            </span>
          </div>
        </div>

        <div>
          <label
            htmlFor={timeId}
            className="mb-2 block text-[11px] font-bold uppercase tracking-[0.12em] text-bone/50"
          >
            Ovn-tid
          </label>
          <div className="relative">
            <input
              id={timeId}
              type="number"
              inputMode="numeric"
              min={OVEN_TIME_MIN}
              max={OVEN_TIME_MAX}
              step={1}
              value={ovenMinutes}
              onChange={(e) =>
                setOvenMinutes(
                  clamp(Number(e.target.value) || 0, OVEN_TIME_MIN, OVEN_TIME_MAX),
                )
              }
              className="w-full rounded-xl border-2 border-bone/20 bg-iron px-4 py-3 pr-14 font-serif text-2xl text-bone outline-none focus:border-herb"
            />
            <span className="pointer-events-none absolute right-4 top-1/2 -translate-y-1/2 font-serif text-xl text-bone/40">
              min
            </span>
          </div>
        </div>

        <div>
          <label
            htmlFor={modeId}
            className="mb-2 block text-[11px] font-bold uppercase tracking-[0.12em] text-bone/50"
          >
            Ovn-mode
          </label>
          <select
            id={modeId}
            value={mode}
            onChange={(e) => setMode(e.target.value as OvenMode)}
            className="w-full appearance-none rounded-xl border-2 border-bone/20 bg-iron px-4 py-3 font-serif text-lg text-bone outline-none focus:border-herb"
          >
            <option value="varmluft">Varmluft</option>
            <option value="over-undervarme">Over/undervarme</option>
          </select>
        </div>
      </div>

      <div className="border-t border-bone/10 bg-iron/60 px-5 py-6 text-center">
        <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-pool">
          Airfryer-start
        </p>
        <p className="mt-2 font-serif text-4xl text-bone md:text-5xl">
          {result.temp}{" "}
          <span className="text-2xl text-bone/50 md:text-3xl">°C</span>
          <span className="mx-3 text-2xl text-bone/30 md:text-3xl">·</span>
          tjek ved {result.checkAt}{" "}
          <span className="text-2xl text-bone/50 md:text-3xl">min</span>
        </p>
        <p className="mt-3 text-sm text-bone/55">
          Startpunkt — tjek tidligt. Store stege følger kerne, ikke procent.
          Fyld ikke kurven som et ovnfad.
        </p>
      </div>
    </aside>
  );
}
