import { NextRequest, NextResponse } from "next/server";

import {
  normalizeNewsletterEmail,
  normalizeNewsletterSource,
  subscribeNewsletter,
} from "@/lib/newsletter/subscribe";
import { isSupabaseConfigured } from "@/lib/supabase/env";

export const dynamic = "force-dynamic";

const RATE_WINDOW_MS = 60_000;
const RATE_MAX = 5;
const rateBuckets = new Map<string, { count: number; resetAt: number }>();

const SUCCESS_MESSAGE = "Tak — du er på listen.";

function clientIp(req: NextRequest): string {
  return (
    req.headers.get("x-forwarded-for")?.split(",")[0]?.trim() ||
    req.headers.get("x-real-ip")?.trim() ||
    "unknown"
  );
}

function rateLimit(ip: string): boolean {
  const now = Date.now();
  const cur = rateBuckets.get(ip);
  if (!cur || now > cur.resetAt) {
    rateBuckets.set(ip, { count: 1, resetAt: now + RATE_WINDOW_MS });
    return true;
  }
  if (cur.count >= RATE_MAX) return false;
  cur.count += 1;
  return true;
}

export async function POST(req: NextRequest) {
  if (!rateLimit(clientIp(req))) {
    return NextResponse.json(
      { error: "For mange forsøg. Prøv igen om et øjeblik." },
      { status: 429 }
    );
  }

  let raw: unknown;
  try {
    raw = await req.json();
  } catch {
    return NextResponse.json({ error: "Ugyldigt JSON." }, { status: 400 });
  }

  if (!raw || typeof raw !== "object") {
    return NextResponse.json({ error: "Ugyldig tilmelding." }, { status: 400 });
  }

  const body = raw as {
    email?: unknown;
    source?: unknown;
    website?: unknown;
  };

  // Honeypot: bots fill hidden fields; real users leave it empty.
  if (typeof body.website === "string" && body.website.trim() !== "") {
    return NextResponse.json({ ok: true, message: SUCCESS_MESSAGE });
  }

  const email = normalizeNewsletterEmail(body.email);
  if (!email) {
    return NextResponse.json(
      { error: "Ugyldig e-mailadresse." },
      { status: 400 }
    );
  }

  if (!isSupabaseConfigured()) {
    return NextResponse.json(
      { error: "Nyhedsbrevet er ikke tilgængeligt lige nu." },
      { status: 503 }
    );
  }

  const source = normalizeNewsletterSource(body.source);
  const result = await subscribeNewsletter(email, source);

  if (!result.ok) {
    return NextResponse.json(
      { error: result.message },
      { status: result.status }
    );
  }

  return NextResponse.json({ ok: true, message: SUCCESS_MESSAGE });
}
