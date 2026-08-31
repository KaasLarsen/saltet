"use client";

import { useEffect, useId, useState } from "react";
import { pricerunnerProductWidgetSrc } from "@/lib/pricerunner";

interface PriceRunnerOfficialWidgetProps {
  productId: string;
  fallbackHref: string;
  offerLimit?: number;
}

export function PriceRunnerOfficialWidget({
  productId,
  fallbackHref,
  offerLimit = 5,
}: PriceRunnerOfficialWidgetProps) {
  const widgetId = `pr-product-widget-${useId().replace(/[^a-zA-Z0-9_-]/g, "").toLowerCase()}`;
  const [failed, setFailed] = useState(false);

  useEffect(() => {
    const script = document.createElement("script");
    script.src = `${pricerunnerProductWidgetSrc(productId, widgetId, offerLimit)}&_=${Date.now()}`;
    script.async = true;
    script.onload = () => {
      const mount = document.getElementById(widgetId);
      if (!mount || mount.innerHTML.trim().length < 80) setFailed(true);
    };
    script.onerror = () => setFailed(true);
    document.body.appendChild(script);
    return () => {
      script.remove();
      const mount = document.getElementById(widgetId);
      if (mount) mount.innerHTML = "";
    };
  }, [productId, widgetId, offerLimit]);

  if (failed) {
    return (
      <a
        href={fallbackHref}
        target="_blank"
        rel="noopener noreferrer sponsored"
        className="block bg-bone px-5 py-4 text-sm font-semibold text-iron hover:bg-herb/15"
      >
        Sammenlign priser på PriceRunner
      </a>
    );
  }

  return (
    <div
      id={widgetId}
      className="w-full overflow-hidden rounded-xl bg-white"
      style={{ display: "block", width: "100%" }}
    />
  );
}
