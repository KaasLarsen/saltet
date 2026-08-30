# Saltet — saltet.dk

Dansk opskriftsside med skate 80s/90s vibe — bygget med Next.js, MDX og Tailwind CSS. Hostet på Vercel.

## Kom i gang lokalt

```bash
npm install
npm run dev
```

Åbn [http://localhost:3000](http://localhost:3000).

Kopiér `.env.example` til `.env.local` og sæt:

```
NEXT_PUBLIC_SITE_URL=https://saltet.dk
```

## Tilføj en ny opskrift

1. Opret en `.mdx`-fil i `content/recipes/[kategori]/`, fx `content/recipes/airfryer/min-opskrift.mdx`
2. Tilføj et billede i `public/recipes/[kategori]/min-opskrift.jpg`
3. Commit og push til `main` — Vercel deployer automatisk

### MDX-format

```yaml
---
title: "Din opskriftstitel"
slug: min-opskrift
category: airfryer
description: "Kort beskrivelse til Google og sociale medier (max ~155 tegn)."
prepTime: "PT10M"
cookTime: "PT20M"
totalTime: "PT30M"
servings: 4
difficulty: nem          # nem | mellem | svær
tags: [tag1, tag2]
image: /recipes/airfryer/min-opskrift.jpg
imageAlt: "Beskrivende alt-tekst til billedet"
publishedAt: 2026-08-17   # brug udgivelsesdato — nyeste vises på forsiden
featured: false          # valgfri; forsiden bruger de 3 seneste opskrifter per kategori
ingredients:
  - "500 g ingrediens"
  - "1 spsk olie"
steps:
  - "Første trin i fremgangsmåden."
  - "Andet trin."
---

Brødtekst med intro og tips. Brug `<Tip>` komponenten:

<Tip>
Dit tip til læseren.
</Tip>
```

### Ny kategori

1. Opret mappe: `content/recipes/ovn/`
2. Tilføj kategorien i `lib/categories.ts`
3. Opskrifter i den nye mappe vises automatisk i navigation og sitemap

### Højtider

Højtider er **ikke** kategorier. Kategorier er tilberedningsmetode (airfryer, grill …). Højtider er en tværgående facet:

- Sider: `/hoejtider` og `/hoejtider/jul` (nytår, påske, Mortensaften)
- Opskrifter vises på en højtid, når de har matchende tags (`jul`, `nytår`, `påske`, `Mortensaften`)
- Tagget `jul` på en opskrift linker til `/hoejtider/jul` (gamle `/tags/jul` omdirigeres)
- Årstider (forår, sommer …) er ikke med endnu

Tilføj `jul` / `nytår` / `påske` / `Mortensaften` i opskriftens `tags` for at få den med. Listen står i [`lib/holiday-nav.ts`](lib/holiday-nav.ts) og [`lib/holidays.ts`](lib/holidays.ts).

### Emner

Emner er **ikke** tilberedningsmetoder. De er madtyper på tværs af metoder:

- Sider: `/emner` og `/emner/sovs` (kylling, fisk, bacon, pizza, festmad m.fl. — se [`lib/topic-nav.ts`](lib/topic-nav.ts))
- `/emner` har filtre for emne, metode, tid, sværhed og søgning — som kategori-sider
- Opskrifter vises på et emne, når de har matchende tags (`sauce`, `kage`, `dessert` osv.)
- Tagget `sauce` på en opskrift linker til `/emner/sovs` (gamle `/tags/sauce` omdirigeres)
- Tilføj emne-tags i opskriftens `tags` for at få den med. Listen står i [`lib/topic-nav.ts`](lib/topic-nav.ts) og [`lib/topics.ts`](lib/topics.ts).

## SEO

Sitet genererer automatisk:

- `sitemap.xml` — **alle** offentlige sider: forside, om, opskrifter, kategorier, højtider, emner, tags og enkeltopskrifter
- `robots.txt`
- JSON-LD Recipe + FAQ schema på hver opskriftsside
- BreadcrumbList schema
- Open Graph og Twitter cards
- Canonical URLs

Når du tilføjer en **ny fast side** (fx `/kontakt`), skal stien også tilføjes i `STATIC_ROUTES` i [`app/sitemap.ts`](app/sitemap.ts). Opskrifter, tags, højtider, emner og kategorier opdateres automatisk.

Test rich results: [Google Rich Results Test](https://search.google.com/test/rich-results)

Tilføj sitet i [Google Search Console](https://search.google.com/search-console) og indsend sitemap: `https://saltet.dk/sitemap.xml`

## Deploy (Vercel + GitHub)

### GitHub

Repoet pushes til GitHub. Ved push til `main` deployer Vercel automatisk.

### Vercel

1. Gå til [vercel.com/new](https://vercel.com/new) og importér GitHub-repoet
2. Framework: **Next.js** (auto-detekteret)
3. Environment variable: `NEXT_PUBLIC_SITE_URL` = `https://saltet.dk`
4. Deploy

### DNS (saltet.dk)

Hos din domæne-registrar, sæt:

| Type  | Navn | Værdi                |
|-------|------|----------------------|
| A     | @    | `76.76.21.21`        |
| CNAME | www  | `cname.vercel-dns.com` |

I Vercel → Project → Settings → Domains, tilføj:

- `saltet.dk`
- `www.saltet.dk`

Vercel udsteder SSL automatisk.

## Projektstruktur

```
app/                    # Next.js sider
components/             # UI-komponenter
content/recipes/        # MDX opskrifter
lib/                    # Parser, SEO, kategorier
public/recipes/         # Opskriftsbilleder
```

## Hvad du skal levere

| Punkt            | Status   | Handling                                      |
|------------------|----------|-----------------------------------------------|
| Domæne DNS       | Fra dig  | Peg A/CNAME records som beskrevet ovenfor     |
| Opskrift-tekster | Løbende  | Erstat AI-udkast med dine egne opskrifter     |
| Billeder         | Løbende  | Erstat med egne fotos for bedst SEO           |
| Logo/brand       | Valgfrit | Tekst-logo "Saltet" bruges indtil videre      |
| Search Console   | Fra dig  | Verificér domæne og indsend sitemap           |

## Scripts

```bash
npm run dev      # Udvikling
npm run build    # Production build
npm run start    # Kør production lokalt
npm run lint     # ESLint
```
