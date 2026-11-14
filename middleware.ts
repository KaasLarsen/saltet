import type { NextRequest } from "next/server";
import { NextResponse } from "next/server";

/**
 * Aggressive scrapers der typisk banker /_next/image og blæser CDN-requests op.
 * Googlebot / Bingbot røres ikke — kun image-optimizer-stien short-circuits.
 */
const AGGRESSIVE_IMAGE_BOTS =
  /bytespider|gptbot|ccbot|petalbot|semrushbot|ahrefsbot|dotbot|mj12bot|dataforseobot|amazonbot|claudebot|meta-externalagent/i;

export function middleware(request: NextRequest) {
  if (!request.nextUrl.pathname.startsWith("/_next/image")) {
    return NextResponse.next();
  }

  const ua = request.headers.get("user-agent") ?? "";
  if (AGGRESSIVE_IMAGE_BOTS.test(ua)) {
    return new NextResponse(null, { status: 403 });
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/_next/image"],
};
