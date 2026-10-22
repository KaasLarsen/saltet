"use client";

import { useId, useState } from "react";

const PRESETS = [
  { label: "3 %", value: 3, hint: "Ferment / let sprængning" },
  { label: "5 %", value: 5, hint: "Mild kødsprængning" },
  { label: "8 %", value: 8, hint: "Klassisk sprænglage" },
  { label: "10 %", value: 10, hint: "Hård lage / sild" },
] as const;

function formatGrams(grams: number): string {
  if (!Number.isFinite(grams) || grams < 0) return "—";
  if (grams < 10) return grams.toFixed(1).replace(".", ",");
  return String(Math.round(grams));
}

interface SaltlageBeregnerProps {
  /** Drop default vertical margin when wrapped in a homepage section. */
  className?: string;
}

export function SaltlageBeregner({ className }: SaltlageBeregnerProps) {
  const litersId = useId();
  const percentId = useId();
  const [liters, setLiters] = useState(1);
  const [percent, setPercent] = useState(5);

  const grams = liters * 1000 * (percent / 100);
  const gramsPerDl = percent; // 1 dl = 100 g vand → percent g salt

  return (
    <aside
      className={`overflow-hidden rounded-2xl border-2 border-bone/20 bg-ash/40 ${className ?? "my-10"}`}
      aria-label="Saltlage-beregner"
    >
      <div className="border-b border-bone/10 bg-ash/80 px-5 py-3">
        <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-herb">
          Saltlage-beregner
        </p>
        <p className="mt-1 text-sm text-bone/60">
          Liter vand × procent = gram fint salt. Ikke flager.
        </p>
      </div>

      <div className="grid gap-6 p-5 sm:grid-cols-2">
        <div>
          <label
            htmlFor={litersId}
            className="mb-2 block text-[11px] font-bold uppercase tracking-[0.12em] text-bone/50"
          >
            Liter vand
          </label>
          <input
            id={litersId}
            type="number"
            inputMode="decimal"
            min={0.1}
            max={50}
            step={0.1}
            value={liters}
            onChange={(e) => setLiters(Number(e.target.value) || 0)}
            className="w-full rounded-xl border-2 border-bone/20 bg-iron px-4 py-3 font-serif text-2xl text-bone outline-none focus:border-herb"
          />
        </div>

        <div>
          <label
            htmlFor={percentId}
            className="mb-2 block text-[11px] font-bold uppercase tracking-[0.12em] text-bone/50"
          >
            Saltprocent
          </label>
          <div className="relative">
            <input
              id={percentId}
              type="number"
              inputMode="decimal"
              min={0.5}
              max={36}
              step={0.5}
              value={percent}
              onChange={(e) => setPercent(Number(e.target.value) || 0)}
              className="w-full rounded-xl border-2 border-bone/20 bg-iron px-4 py-3 pr-12 font-serif text-2xl text-bone outline-none focus:border-herb"
            />
            <span className="pointer-events-none absolute right-4 top-1/2 -translate-y-1/2 font-serif text-xl text-bone/40">
              %
            </span>
          </div>
        </div>
      </div>

      <div className="flex flex-wrap gap-2 px-5 pb-5">
        {PRESETS.map((preset) => {
          const active = percent === preset.value;
          return (
            <button
              key={preset.value}
              type="button"
              title={preset.hint}
              onClick={() => setPercent(preset.value)}
              className={`rounded-xl border-2 px-3 py-2 text-[12px] font-bold uppercase tracking-[0.1em] transition-colors ${
                active
                  ? "border-herb bg-herb text-iron"
                  : "border-bone/20 bg-iron text-bone/70 hover:border-herb hover:text-herb"
              }`}
            >
              {preset.label}
            </button>
          );
        })}
      </div>

      <div className="border-t border-bone/10 bg-iron/60 px-5 py-6 text-center">
        <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-pool">
          Du skal bruge
        </p>
        <p className="mt-2 font-serif text-4xl text-bone md:text-5xl">
          {formatGrams(grams)}{" "}
          <span className="text-2xl text-bone/50 md:text-3xl">g fint salt</span>
        </p>
        <p className="mt-3 text-sm text-bone/55">
          Ca. {formatGrams(gramsPerDl)} g pr. dl vand · formel: liter × 1000 ×{" "}
          {String(percent).replace(".", ",")}% / 100
        </p>
      </div>
    </aside>
  );
}
