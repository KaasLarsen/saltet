"use client";

import { useEffect } from "react";
import {
  OUTBOUND_ATTR,
  OUTBOUND_MERCHANT_ATTR,
  OUTBOUND_OFFER_ATTR,
  OUTBOUND_SURFACE_ATTR,
  type OutboundSurface,
} from "@/lib/outbound";

declare global {
  interface Window {
    gtag?: (...args: unknown[]) => void;
    plausible?: (
      event: string,
      options?: { props?: Record<string, string | undefined> }
    ) => void;
    dataLayer?: unknown[];
  }
}

/**
 * Captures clicks on `[data-outbound]` so grej/anmeldelse/opskrift
 * CTR can be split in GA / Plausible / GTM without changing partner URLs.
 */
export function OutboundClickTracker() {
  useEffect(() => {
    function onClick(event: MouseEvent) {
      const target = event.target;
      if (!(target instanceof Element)) return;
      const anchor = target.closest(`a[${OUTBOUND_ATTR}]`);
      if (!(anchor instanceof HTMLAnchorElement)) return;

      const surface = (anchor.getAttribute(OUTBOUND_SURFACE_ATTR) ??
        "other") as OutboundSurface;
      const offerId = anchor.getAttribute(OUTBOUND_OFFER_ATTR) ?? undefined;
      const merchant =
        anchor.getAttribute(OUTBOUND_MERCHANT_ATTR) ?? undefined;
      const href = anchor.href;
      const props = {
        surface,
        offer_id: offerId,
        merchant,
        url: href,
      };

      window.dispatchEvent(
        new CustomEvent("saltet:outbound", { detail: props })
      );

      window.gtag?.("event", "outbound_click", {
        event_category: "affiliate",
        event_label: `${surface}:${offerId ?? href}`,
        outbound_surface: surface,
        outbound_offer: offerId,
        outbound_merchant: merchant,
        transport_type: "beacon",
      });

      window.plausible?.("Outbound Click", { props });

      window.dataLayer?.push({
        event: "saltet_outbound_click",
        outbound_surface: surface,
        outbound_offer: offerId,
        outbound_merchant: merchant,
        outbound_url: href,
      });
    }

    document.addEventListener("click", onClick);
    return () => document.removeEventListener("click", onClick);
  }, []);

  return null;
}
