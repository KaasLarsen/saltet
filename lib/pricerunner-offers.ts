import { unstable_cache } from "next/cache";
import { pricerunnerProductUrl } from "@/lib/pricerunner";

export interface PriceRunnerOffer {
  merchant: string;
  price: string;
  shipping: string | null;
  inStock: boolean;
}

export interface PriceRunnerComparison {
  name: string;
  image: string | null;
  href: string;
  offers: PriceRunnerOffer[];
}

interface PayloadQuery {
  queryKey?: unknown;
  state?: { data?: unknown };
}

interface OffersPayload {
  images?: Array<{ path?: string }>;
  offers?: Array<{
    merchantId?: string;
    stockStatus?: string;
    price?: { amount?: string };
    shippingCost?: { amount?: string } | null;
  }>;
  merchants?: Record<string, { name?: string }>;
}

interface ProductPayload {
  product?: { name?: string };
}

function productImageUrl(path: string | undefined): string | null {
  if (!path) return null;
  const parts = path.split("/").filter(Boolean);
  if (parts.length < 3) return null;
  const id = parts[1];
  const file = parts[2];
  return `https://owp.klarna.com/product/252x252/${id}/${file}?ph=true`;
}

function parseAmount(amount: string | undefined): number | null {
  if (!amount) return null;
  const n = Number(amount);
  return Number.isFinite(n) ? n : null;
}

export function formatDkk(amount: string | number): string {
  const n = typeof amount === "number" ? amount : Number(amount);
  if (!Number.isFinite(n)) return "";
  return new Intl.NumberFormat("da-DK", {
    style: "currency",
    currency: "DKK",
    maximumFractionDigits: n % 1 === 0 ? 0 : 2,
  }).format(n);
}

function asRecord(value: unknown): Record<string, unknown> | null {
  return value && typeof value === "object" && !Array.isArray(value)
    ? (value as Record<string, unknown>)
    : null;
}

function extractComparison(
  html: string,
  href: string
): PriceRunnerComparison | null {
  const match = html.match(
    /<script[^>]*id="initial_payload"[^>]*>([\s\S]*?)<\/script>/
  );
  if (!match?.[1]) return null;

  const payload = JSON.parse(match[1]) as {
    __DEHYDRATED_QUERY_STATE__?: { queries?: PayloadQuery[] };
  };
  const queries = payload.__DEHYDRATED_QUERY_STATE__?.queries ?? [];

  let product: ProductPayload | null = null;
  let offersData: OffersPayload | null = null;

  for (const query of queries) {
    const key = JSON.stringify(query.queryKey ?? "");
    const data = query.state?.data;
    if (key.includes("product-detail-initial")) {
      product = asRecord(data) as ProductPayload | null;
    }
    if (key.includes("product-detail-offers")) {
      offersData = asRecord(data) as OffersPayload | null;
    }
  }

  const merchants = offersData?.merchants ?? {};
  const image = productImageUrl(offersData?.images?.[0]?.path);
  const offers = (offersData?.offers ?? [])
    .map((offer) => {
      const price = offer.price?.amount;
      if (!price) return null;
      const merchant = merchants[offer.merchantId ?? ""]?.name;
      if (!merchant) return null;
      const shippingAmount = parseAmount(offer.shippingCost?.amount);
      return {
        merchant,
        price,
        shipping:
          shippingAmount === null
            ? null
            : shippingAmount === 0
              ? "Fri fragt"
              : `+ ${formatDkk(shippingAmount)} fragt`,
        inStock: offer.stockStatus === "IN_STOCK",
      } satisfies PriceRunnerOffer;
    })
    .filter((offer): offer is PriceRunnerOffer => Boolean(offer))
    .sort((a, b) => Number(a.price) - Number(b.price))
    .slice(0, 5);

  const name = product?.product?.name;
  if (!name || offers.length === 0) return null;

  return {
    name,
    image,
    href,
    offers,
  };
}

async function loadComparison(
  categoryId: string,
  productId: string
): Promise<PriceRunnerComparison | null> {
  const href = pricerunnerProductUrl(categoryId, productId);
  try {
    const response = await fetch(href, {
      headers: {
        "User-Agent":
          "Mozilla/5.0 (compatible; Saltet/1.0; +https://www.saltet.dk)",
        Accept: "text/html",
      },
      next: { revalidate: 21600 },
      signal: AbortSignal.timeout(8000),
    });
    if (!response.ok) return null;
    const html = await response.text();
    return extractComparison(html, href);
  } catch {
    return null;
  }
}

export function getPriceRunnerComparison(
  categoryId: string,
  productId: string
): Promise<PriceRunnerComparison | null> {
  return unstable_cache(
    () => loadComparison(categoryId, productId),
    ["pricerunner-offers", categoryId, productId],
    { revalidate: 21600 }
  )();
}
