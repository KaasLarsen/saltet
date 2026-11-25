"use client";

import Link from "next/link";
import { useState, type FormEvent } from "react";

type Status = "idle" | "pending" | "success" | "error";

export function NewsletterSignup() {
  const [email, setEmail] = useState("");
  const [website, setWebsite] = useState("");
  const [status, setStatus] = useState<Status>("idle");
  const [message, setMessage] = useState<string | null>(null);

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    if (status === "pending") return;

    setStatus("pending");
    setMessage(null);

    try {
      const res = await fetch("/api/newsletter", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          email,
          source: "footer",
          website,
        }),
      });
      const data = (await res.json().catch(() => null)) as {
        ok?: boolean;
        message?: string;
        error?: string;
      } | null;

      if (!res.ok) {
        setStatus("error");
        setMessage(data?.error ?? "Noget gik galt. Prøv igen.");
        return;
      }

      setStatus("success");
      setMessage(data?.message ?? "Tak — du er på listen.");
      setEmail("");
    } catch {
      setStatus("error");
      setMessage("Noget gik galt. Prøv igen.");
    }
  }

  return (
    <div className="mx-auto max-w-md">
      <p className="font-serif text-lg uppercase tracking-wide text-herb">
        Nyhedsbrev
      </p>
      <p className="mt-2 text-sm leading-relaxed text-bone/55">
        Få nye opskrifter og tips — ingen spam, kun salt.
      </p>
      <form onSubmit={onSubmit} className="mt-4 space-y-3" noValidate>
        <label className="sr-only" htmlFor="newsletter-email">
          E-mail
        </label>
        <div className="flex flex-col gap-2 sm:flex-row">
          <input
            id="newsletter-email"
            type="email"
            name="email"
            autoComplete="email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="din@email.dk"
            disabled={status === "pending" || status === "success"}
            className="min-w-0 flex-1 rounded-lg border-2 border-bone/20 bg-iron px-3 py-2.5 text-sm text-bone placeholder:text-bone/30 outline-none transition-colors focus:border-herb disabled:opacity-60"
          />
          <button
            type="submit"
            disabled={status === "pending" || status === "success"}
            className="rounded-lg border-2 border-herb bg-herb px-4 py-2.5 text-[11px] font-bold uppercase tracking-[0.14em] text-iron transition-opacity hover:opacity-90 disabled:opacity-60"
          >
            {status === "pending" ? "Sender…" : "Tilmeld"}
          </button>
        </div>
        {/* Honeypot — leave empty */}
        <div
          className="absolute -left-[9999px] h-0 w-0 overflow-hidden"
          aria-hidden="true"
        >
          <label htmlFor="newsletter-website">Website</label>
          <input
            id="newsletter-website"
            type="text"
            name="website"
            tabIndex={-1}
            autoComplete="off"
            value={website}
            onChange={(e) => setWebsite(e.target.value)}
          />
        </div>
        <p className="text-[11px] leading-relaxed text-bone/40">
          Ved tilmelding accepterer du, at vi gemmer din e-mail til nyhedsbrev.
          Se{" "}
          <Link
            href="/privatliv"
            className="font-semibold text-bone/55 underline decoration-bone/25 underline-offset-2 transition-colors hover:text-herb hover:decoration-herb"
          >
            privatlivspolitikken
          </Link>
          .
        </p>
        {message ? (
          <p
            role="status"
            className={`text-sm ${
              status === "error" ? "text-wood" : "text-herb"
            }`}
          >
            {message}
          </p>
        ) : null}
      </form>
    </div>
  );
}
