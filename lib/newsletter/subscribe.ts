import { createSupabaseAnonClient } from "@/lib/supabase/anon";
import { isSupabaseConfigured } from "@/lib/supabase/env";

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export function normalizeNewsletterEmail(value: unknown): string | null {
  if (typeof value !== "string") return null;
  const email = value.trim().toLowerCase();
  if (email.length < 3 || email.length > 254) return null;
  if (!EMAIL_RE.test(email)) return null;
  return email;
}

export function normalizeNewsletterSource(value: unknown): string {
  if (typeof value !== "string") return "footer";
  const source = value.trim().toLowerCase();
  if (!source || source.length > 40) return "footer";
  if (!/^[a-z0-9_-]+$/.test(source)) return "footer";
  return source;
}

export type NewsletterSubscribeResult =
  | { ok: true }
  | { ok: false; status: number; message: string };

export async function subscribeNewsletter(
  email: string,
  source: string
): Promise<NewsletterSubscribeResult> {
  if (!isSupabaseConfigured()) {
    return {
      ok: false,
      status: 503,
      message: "Nyhedsbrevet er ikke tilgængeligt lige nu.",
    };
  }

  try {
    const supabase = createSupabaseAnonClient();
    const { error } = await supabase.rpc("newsletter_subscribe", {
      p_email: email,
      p_source: source,
    });

    if (error) {
      if (error.message?.includes("invalid_email")) {
        return { ok: false, status: 400, message: "Ugyldig e-mailadresse." };
      }
      return {
        ok: false,
        status: 503,
        message: "Nyhedsbrevet er ikke tilgængeligt lige nu.",
      };
    }

    return { ok: true };
  } catch {
    return {
      ok: false,
      status: 503,
      message: "Nyhedsbrevet er ikke tilgængeligt lige nu.",
    };
  }
}
