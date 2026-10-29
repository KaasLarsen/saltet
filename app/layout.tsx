import type { Metadata } from "next";
import { Suspense } from "react";
import { Archivo_Black, Barlow } from "next/font/google";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { JsonLd } from "@/components/JsonLd";
import { buildWebsiteJsonLd, siteConfig } from "@/lib/seo";
import "./globals.css";

const archivo = Archivo_Black({
  variable: "--font-archivo",
  subsets: ["latin"],
  weight: "400",
  display: "swap",
});

const barlow = Barlow({
  variable: "--font-barlow",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
  display: "swap",
});

export const metadata: Metadata = {
  metadataBase: new URL(siteConfig.url),
  title: {
    default: "Saltet — Enkle opskrifter til hverdagen",
    template: "%s | Saltet",
  },
  description: siteConfig.description,
  openGraph: {
    title: "Saltet — Enkle opskrifter til hverdagen",
    description: siteConfig.description,
    url: siteConfig.url,
    siteName: siteConfig.name,
    locale: siteConfig.locale,
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Saltet",
    description: siteConfig.description,
  },
  alternates: {
    canonical: siteConfig.url,
  },
  other: {
    "google-adsense-account": "ca-pub-7373148222153531",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="da"
      className={`${archivo.variable} ${barlow.variable} h-full`}
    >
      <body className="flex min-h-full flex-col bg-stone font-sans text-bone antialiased">
        <JsonLd data={buildWebsiteJsonLd()} />
        <Suspense
          fallback={
            <header className="sticky top-0 z-50 border-b-2 border-bone/15 bg-iron/95">
              <div className="mx-auto flex h-[3.75rem] max-w-5xl items-center px-5 md:px-8">
                <span className="font-serif text-2xl uppercase tracking-wide text-bone md:text-3xl">
                  Saltet
                </span>
              </div>
            </header>
          }
        >
          <Header />
        </Suspense>
        <main className="flex-1">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
