# Opskriftsbilleder — Saltet-standard

Hero-fotos til `public/recipes/{category}/{slug}.jpg` skal ligne **hjemmekøkken / photojournalism**, ikke poleret stock eller «AI cookbook».

## Krav

- Unik binær pr. opskrift (kør `npm run verify:images`)
- Filnavn ved generering: `{category}--{slug}.jpg` → kopiér med `node scripts/copy-generated-images.mjs`
- Format: `.jpg` (eller PNG-bytes i `.jpg`, som resten af sitet), typisk 4:3
- Ingen tekst, logo, watermark eller UI i billedet
- Gerne ét eksisterende Saltet-madfoto som `reference_image_paths` (fx `flaeskesteg.jpg`, `frikadeller.jpg`, `kanelsnegle.jpg`)

## Stil (gør)

- Blødt vindueslys / sidelys — ikke beauty-lighting
- Ujævn plating, krummer, dryp, parchment med pletter
- Reel madtekstur (skorpe, saft, fiber, ostetråd)
- Hverdagstallerkener, mørkt træ, lidt rod i baggrunden (sløret)
- Varierende stegefarve; hjemmelavede former

## Undgå

- Spejlblank «plastik»-overflade og CGI-look
- Perfekt symmetrisk plating og spotfrit studio
- Oversatueret mad, glow, faux-bokeh-cirkler
- Generisk «dark plate + dramatic rim light» uden karakter

## Prompt-skabelon

Brug som udgangspunkt (udfyld retten):

```text
Photojournalism style: [retten konkret og synlig], on dark everyday plate or parchment,
soft window light from the side, real food texture, uneven homemade plating,
crumbs or sauce drips, shallow depth of field, home-kitchen realism,
not CGI, not stock photo, no plastic sheen, no text
```

Eksempel:

```text
Photojournalism style: sticky BBQ spareribs on dark tray, messy glaze, bone tips
visible, parchment stained, warm kitchen side light, real meat texture,
imperfect stack, not CGI, no text
```

## Workflow

1. Generér med skabelonen (+ referencefoto når muligt)
2. `node scripts/copy-generated-images.mjs`
3. `npm run verify:images`
4. Kasser og regenerér hvis billedet ser stock-/AI-blankt ud
