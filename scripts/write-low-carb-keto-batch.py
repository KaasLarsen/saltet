#!/usr/bin/env python3
"""Write Low-Carb & Keto hub content: guides + recipes + copy images."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
PUBLIC = ROOT / "public"
PUBLISHED = "2026-10-16"


def yaml_str(s: str) -> str:
    if any(c in s for c in ':#{}[]&*!|>\'"%@`') or s.startswith(("-", "?", " ")):
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return '"' + s.replace('"', '\\"') + '"'


def write_recipe(d: dict) -> None:
    tags = "\n".join(f"  - {yaml_str(t)}" for t in d["tags"])
    ings = "\n".join(f"  - {yaml_str(x)}" for x in d["ingredients"])
    steps = "\n".join(f"  - {yaml_str(x)}" for x in d["steps"])
    faqs = "\n".join(
        f"  - question: {yaml_str(f['question'])}\n    answer: {yaml_str(f['answer'])}"
        for f in d["faq"]
    )
    featured = "featured: true\n" if d.get("featured") else ""
    slug = d["slug"]
    cat = d["category"]
    body = f"""---
title: {yaml_str(d["title"])}
slug: {slug}
category: {cat}
description: {yaml_str(d["description"])}
prepTime: "{d["prepTime"]}"
cookTime: "{d["cookTime"]}"
totalTime: "{d["totalTime"]}"
servings: {d["servings"]}
difficulty: {d["difficulty"]}
tags:
{tags}
image: /recipes/{cat}/{slug}.jpg
imageAlt: {yaml_str(d["imageAlt"])}
publishedAt: {PUBLISHED}
{featured}ingredients:
{ings}
steps:
{steps}
faq:
{faqs}
---

{d["body"]}

<Tip>
{d["tip"]}
</Tip>
"""
    out_dir = CONTENT / "recipes" / cat
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{slug}.mdx"
    if path.exists():
        raise SystemExit(f"slug collision: {path}")
    path.write_text(body, encoding="utf-8")
    print("recipe", cat + "/" + slug)


def write_guide(d: dict) -> None:
    tags = "\n".join(f"  - {yaml_str(t)}" for t in d["tags"])
    related = "\n".join(f"  - {r}" for r in d["relatedRecipes"])
    related_g = "\n".join(f"  - {r}" for r in d.get("relatedGuides", []))
    faqs = "\n".join(
        f"  - question: {yaml_str(f['question'])}\n    answer: {yaml_str(f['answer'])}"
        for f in d["faq"]
    )
    related_grej = ""
    if d.get("relatedGrej"):
        related_grej = "relatedGrej:\n" + "\n".join(
            f"  - {r}" for r in d["relatedGrej"]
        ) + "\n"
    body = f"""---
title: {yaml_str(d["title"])}
slug: {d["slug"]}
description: {yaml_str(d["description"])}
tags:
{tags}
image: /guides/{d["slug"]}.jpg
imageAlt: {yaml_str(d["imageAlt"])}
publishedAt: {PUBLISHED}
relatedRecipes:
{related}
relatedGuides:
{related_g}
{related_grej}faq:
{faqs}
---

{d["body"]}
"""
    path = CONTENT / "guides" / f"{d['slug']}.mdx"
    if path.exists():
        raise SystemExit(f"guide collision: {path}")
    path.write_text(body, encoding="utf-8")
    print("guide", d["slug"])


def copy_img(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not src.exists():
        raise SystemExit(f"missing image source: {src}")
    shutil.copyfile(src, dest)
    print("img", dest.relative_to(ROOT))


# --- Guides ---

GUIDES = [
    {
        "slug": "keto-flu-og-flagesalt",
        "title": "Keto-flu — hvorfor flagesalt er kuren",
        "description": "Keto-flu forklaret: når insulin falder, udskiller nyrerne salt. Sådan doserer du flagesalt og elektrolytter uden hovedpine.",
        "imageAlt": "Flagesalt i skål ved et glas elektrolyt-vand med lime",
        "tags": ["keto", "keto-flu", "elektrolyt", "flagesalt", "salt", "low-carb"],
        "relatedRecipes": [
            "gryde/sukkerfri-elektrolyt-shots",
            "trykkoger/gourmet-bone-broth-marvben",
            "stobejern/baconfedt-mandler",
            "airfryer/keto-madbrod",
            "airfryer/bacon",
        ],
        "relatedGuides": ["saltguide", "bedste-salte-elektrolyt-vand", "sunde-teknikker"],
        "faq": [
            {
                "question": "Hvad er keto-flu?",
                "answer": "Hovedpine, træthed, svimmelhed og kramper de første dage uden kulhydrat. Det er ofte salt- og væskemangel — ikke «gift» fra ketose.",
            },
            {
                "question": "Hvorfor mister man salt på low-carb?",
                "answer": "Lavt insulin får nyrerne til at udskille mere natrium. Glykogen binder vand; når det tømmes, følger salt med ud.",
            },
            {
                "question": "Hvor meget salt skal jeg spise?",
                "answer": "Mange lander på 5–7 g natrium dagligt i starten (ca. 12–18 g bordsalt fordelt) — justér efter sved, træning og blodtryk. Flagesalt på maden tæller med.",
            },
            {
                "question": "Er flagesalt bedre end bordsalt?",
                "answer": "Kemisk er det stadig NaCl. Flager er nemmere at dose visuelt og smager «renere» som finish. Til elektrolyt-vand: fint eller groft havsalt opløses lettere.",
            },
            {
                "question": "Skal jeg også have kalium og magnesium?",
                "answer": "Ja, hvis kramper og hjertebanken fortsætter. Kaliumsalt (KCl) i små mængder og magnesium om aftenen er klassiske næste skridt — ikke megadoser.",
            },
        ],
        "body": """Når kulhydraterne ryger, falder insulin. Nyrerne slipper natrium. Vandet følger med. Du kalder det keto-flu. Vi kalder det **saltunderskud**.

Denne guide er hub’en til [Low-Carb & Keto](/emner/keto). Praktisk saltvand: [sukkerfri elektrolyt-shots](/opskrifter/gryde/sukkerfri-elektrolyt-shots). Varm mineral-suppe: [gourmet bone broth](/opskrifter/trykkoger/gourmet-bone-broth-marvben). Salttyper til glasset: [testen af salte](/guides/bedste-salte-elektrolyt-vand). Den store salt-hub: [saltguiden](/guides/saltguide).

## Hvad sker der i kroppen

Insulin holder normalt på natrium i nyrerne. Skær kulhydrater væk → insulin falder → mere natrium i urinen. Samtidig tømmes glykogenlagre (hver gram glykogen binder ~3 g vand). Resultat: du tisser salt og væske væk i 48–96 timer.

Symptomerne — bankende hoved, tung krop, «hjernetåge», nattekramper — ligner dehydrering, fordi det *er* elektrolyt-tab.

## Flagesalt er ikke magi — det er dosering

Flagesalt vinder, fordi du **ser** mængden. En knivspids fint salt i panden er usynlig. En tydelig flage-finish på æg, bøf og bouillon gør det svært at underdose.

| Situation | Salt-greb |
| --- | --- |
| Morgen-keto-flu | ¼–½ tsk havsalt i varm bouillon eller shot |
| Efter træning | Shot + ekstra flager på maden |
| Aftenkramper | Magnesium + tjek at dagens salt ikke var «restaurant-lavt» |
| Kun kød (carnivore) | Salt hvert måltid — der er ingen brød der «gemmer» natrium |

## Sådan doserer du uden Excel

1. **Spis salt synligt.** Flager på alt kød, æg og bouillon.
2. **Drik ét elektrolyt-shot** de første 1–2 uger, hvis hovedet banker. Se [opskriften](/opskrifter/gryde/sukkerfri-elektrolyt-shots).
3. **Bone broth til aftensult.** Kollagen + natrium + varme. [Marvben i trykkoger](/opskrifter/trykkoger/gourmet-bone-broth-marvben).
4. **Stop med at «være flink».** Low-carb uden salt er en migræne-fabriksindstilling.

Har du forhøjet blodtryk, nyresygdom eller tager væske-/blodtryksmedicin: tal med læge før du skruer saltet i vejret. Resten af os underdoserer typisk i uge ét.

## Hvad keto-flu *ikke* er

Det er ikke bevis på, at ketose «virker». Det er ikke noget, du skal «ride af» i tre uger. Det er ikke sukkertrang forklædt som sygdom. Fix saltet først. Så smager [baconfedt-mandler](/opskrifter/stobejern/baconfedt-mandler) og [carnivore-tacoen](/opskrifter/ovn/carnivore-taco) af sejr igen.
""",
        "img_src": PUBLIC / "guides" / "saltguide.jpg",
    },
    {
        "slug": "bedste-salte-elektrolyt-vand",
        "title": "Testen: bedste salte til elektrolyt-vand",
        "description": "Maldon-flagesalt vs. keltisk havsalt vs. Himalayasalt — mineraler, smag og opløselighed i koldt vand til keto-elektrolytter.",
        "imageAlt": "Tre salttyper i skåle: flagesalt, gråt havsalt og lyserødt Himalayasalt",
        "tags": ["salt", "elektrolyt", "flagesalt", "havsalt", "keto", "test"],
        "relatedRecipes": [
            "gryde/sukkerfri-elektrolyt-shots",
            "trykkoger/gourmet-bone-broth-marvben",
            "roeg/roget-salt",
            "ovn/braendt-hvidloegssalt",
        ],
        "relatedGuides": ["keto-flu-og-flagesalt", "saltguide", "saltlage-til-mandler"],
        "faq": [
            {
                "question": "Hvilket salt er bedst i koldt vand?",
                "answer": "Fint eller groft havsalt (og fint Himalaya) opløses hurtigst. Maldon-flager er til finish — knus dem, eller vælg en anden type til shots.",
            },
            {
                "question": "Har Himalayasalt flere mineraler?",
                "answer": "Ja, sporstoffer i små mængder — men natrium er stadig hovedsagen. Farven er jernoxider, ikke en multivitamin.",
            },
            {
                "question": "Er keltisk salt «vådt»?",
                "answer": "Ofte ja — residual moisture. Det klumper og vejer tungere pr. ske. Vej det, eller smag dig frem.",
            },
            {
                "question": "Kan jeg bruge røget salt i shots?",
                "answer": "Du kan, men det smager af lejrbål i limevand. Gem røget salt til kød og æg.",
            },
        ],
        "body": """Elektrolyt-vand er kedeligt, indtil saltet er forkert. Så er det uudrikkeligt.

Vi tester tre klassikere til [sukkerfri elektrolyt-shots](/opskrifter/gryde/sukkerfri-elektrolyt-shots) og til at forstå [keto-flu](/guides/keto-flu-og-flagesalt). Baggrund: [saltguiden](/guides/saltguide).

## Feltet

| Salt | Form | Smag i koldt vand | Opløselighed | Bedst til |
| --- | --- | --- | --- | --- |
| **Maldon-flagesalt** | Pyramideflager | Rent, «hav», lidt metallisk hvis for meget | Langsom — knus først | Finish på mad; knust i shot |
| **Keltisk havsalt** | Groft, ofte fugtigt | Mineralt, let bittert | Middel | Shots hvis du vejer; bouillon |
| **Lyserødt Himalayasalt** | Fint/groft | Mildt, lidt «sten» | Godt (især fint) | Dagligt elektrolyt-vand |

## Hvad vi faktisk smagte

**Maldon.** Flot i skålen. I iskoldt vand svømmer flagerne som sne, indtil du rører hårdt. Smagen er ren — og det er let at overdosere, fordi volumen lyver (flager vejer lidt). Knus mellem fingrene, eller brug vægt: start med 1–1,5 g pr. glas.

**Keltisk.** Gråt, lidt klistret. Smager af tidevand og kælder på den fede måde. I shots giver det mere «body» end Maldon. Ulempen: ske-mål snyder pga. fugt. Vægt vinder.

**Himalaya.** Den nemme hverdagsvinder til koldt vand. Fint pulver forsvinder. Smagen er mild nok til lime. Mineral-historien er marketing med en kerne af sporstoffer — din keto-flu fixes af **natriummængden**, ikke den lyserøde aura.

## Dom

- **Shot i glas:** fint Himalaya eller vejet keltisk.
- **Finish på bøf og æg:** Maldon.
- **Bouillon:** keltisk eller groft havsalt — smag til, til det er tydeligt salt, ikke «suppe-light».

Ingen af dem erstatter kalium eller magnesium. Salt er base-laget. Resten er finjustering.
""",
        "img_src": PUBLIC / "guides" / "saltlage-til-mandler.jpg",
    },
    {
        "slug": "maillard-low-carb-groentsager",
        "title": "Maillard på low-carb grøntsager",
        "description": "Sådan karamelliserer du rosenkål og broccoli med plancha og salt — hård kontaktvarme, så low-carb grønt smager af kød.",
        "imageAlt": "Dybt brunede rosenkål og broccoli på plancha med flagesalt",
        "tags": ["maillard", "low-carb", "keto", "plancha", "rosenkål", "broccoli", "grøntsager"],
        "relatedRecipes": [
            "airfryer/rosenkaal-baconfedt-parmesan",
            "plancha/spidskaal-smoer-parmesan-plancha",
            "airfryer/spidskaal",
            "airfryer/bacon-twists",
            "fermentering/fermenteret-sennep-uden-sukker",
        ],
        "relatedGuides": [
            "groentsager-med-guldskorpe",
            "plancha-vs-stobejern-groentsager",
            "braendt-kaal",
            "stegeoverflader",
            "keto-flu-og-flagesalt",
        ],
        "faq": [
            {
                "question": "Hvorfor smager dampet broccoli kedeligt?",
                "answer": "Du får svovl og vand — ikke Maillard. Brun kræver tør overflade og kontakt over ca. 140 °C.",
            },
            {
                "question": "Skal grøntsagerne blancheres først?",
                "answer": "Nej til plancha-bark. Halvér, tør, salt, hård varme. Blanchering giver hospital-kål.",
            },
            {
                "question": "Hvilket fedt?",
                "answer": "Baconfedt, andefedt eller ghee. Højt røgpunkt, animalsk smag. Olivenolie til finish — ikke til max-varme.",
            },
            {
                "question": "Er det keto?",
                "answer": "Rosenkål og broccoli er low-carb nok til de fleste. Salt og fedt gør dem mættende. Se emnet Low-Carb & Keto.",
            },
        ],
        "body": """Low-carb savner ikke pasta. Den savner **skarpe kanter**. Maillard er kanterne.

Når der ikke er kartoffelstivelse til at brune, skal kål og broccoli opføre sig som kød: tørre, salte, presset ned på glødende metal. Hub: [Low-Carb & Keto](/emner/keto). Teknik-søskende: [grøntsager med guldskorpe](/guides/groentsager-med-guldskorpe), [plancha vs. støbejern](/guides/plancha-vs-stobejern-groentsager), [brændt kål](/guides/braendt-kaal).

## Reglen: vand er fjenden

Vask. Tør. Salt 10–20 minutter før (draw brine). Dup igen. Våd kål damper. Tør kål bruner.

## Plancha-metoden

1. Plancha eller støbejern **rygende** varm.
2. Tyndt lag baconfedt eller ghee.
3. Halve rosenkål cut-side ned. Broccoliflorets fladside ned.
4. **Tryk.** Lad dem sidde 2–4 minutter uden at pille.
5. Vend. Flagesalt. Evt. mere fedt.

Du er færdig, når snitfladen er mørkebrun — ikke olivengrøn. Den rå kålsmag er væk, fordi sukkerstofferne har reageret med aminosyrer. Det er Maillard, ikke «brændt».

## Saltets job

Salt trækker overfladevand væk *før* stegen og forstærker browning. Efter stegen: flager for knas. Underdosér ikke — low-carb grønt uden salt smager af dyd.

## Server med

[Rosenkål i baconfedt](/opskrifter/airfryer/rosenkaal-baconfedt-parmesan). [Airfryer bacon-twists](/opskrifter/airfryer/bacon-twists) som «fritter». [Fermenteret sennep uden sukker](/opskrifter/fermentering/fermenteret-sennep-uden-sukker) til det fede.
""",
        "img_src": PUBLIC / "recipes" / "airfryer" / "rosenkaal-baconfedt-parmesan.jpg"
        if (PUBLIC / "recipes" / "airfryer" / "rosenkaal-baconfedt-parmesan.jpg").exists()
        else PUBLIC / "guides" / "stegeoverflader.jpg",
    },
    {
        "slug": "carnivore-boeuf-stoebjern-vs-carbonstaal",
        "title": "Støbejern vs. carbonstål til carnivore-bøffen",
        "description": "Når der kun er kød og salt, skal panden være fejlfri. Støbejern vs. carbonstål til den ultimative carnivore-bøf — hvilken vinder?",
        "imageAlt": "Ribeye stegt i støbejernspande med flagesalt",
        "tags": ["carnivore", "keto", "støbejern", "carbonstål", "bøf", "stegeoverflader"],
        "relatedRecipes": [
            "stobejern/cast-iron-ribeye",
            "stobejern/carnivore-aeggekage-svinekaebe",
            "ovn/carnivore-taco",
            "pande/hakkeboef-loeg-spejlaeg",
            "stobejern/smash-burgers-stobejern",
        ],
        "relatedGuides": ["stegeoverflader", "stoebjern-seasoning", "stegning-olier-roegpunkt", "keto-flu-og-flagesalt"],
        "relatedGrej": ["stoebejern-vs-carbonstaal", "stoebjern-rene-skole", "plancha-vs-stobejern"],
        "faq": [
            {
                "question": "Hvilken pande vinder til carnivore-bøf?",
                "answer": "Støbejern til tykke steaks (varmereserve). Carbonstål til tynde stykker og smash, hvor du vil have lynhurtig respons.",
            },
            {
                "question": "Må man bruge olie, eller kun animalsk fedt?",
                "answer": "Talg, baconfedt eller fedtkanten fra stegen. Olie er valgfrit — ikke nødvendigt, hvis kødet er marbleret.",
            },
            {
                "question": "Salt før eller efter?",
                "answer": "Tørsalt mindst 40 minutter før (eller natten over) for tør skorpe. Flager efter udskæring.",
            },
            {
                "question": "Findes der en købsguide?",
                "answer": "Ja — støbejern vs. carbonstål som grej-artikel. Denne guide er stege-vinklen til kød-og-salt.",
            },
        ],
        "body": """To ingredienser. Kød. Salt. Panden er den tredje — den, der afgør skorpen.

Carnivore tåler ikke en halvbagt stegeoverflade. Ingen sauce redder dig. Enten Maillard — eller gråt kød. Grej-duellen ligger i [støbejern vs. carbonstål](/grej/stoebejern-vs-carbonstaal). Her er **carnivore-dommen**. Teknik: [stegeoverflader](/guides/stegeoverflader), [seasoning](/guides/stoebjern-seasoning).

## Støbejern — varmelagringens konge

Tung pande. Holder temperaturen, når en kold ribeye lander. Cut-side bark uden at panden kollapser i varme.

**Vind:** [cast iron ribeye](/opskrifter/stobejern/cast-iron-ribeye), tykke culotter, [carnivore-æggekage](/opskrifter/stobejern/carnivore-aeggekage-svinekaebe).

**Tab:** du løfter den som et bilbatteri. Den er langsom op. Syre og opvaskemaskine er fjender.

## Carbonstål — respons og kontrol

Halv vægt. Lynhurtig op og ned. Perfekt til smash og tynde skiver, hvor du vil vende ofte uden at brænde fedtet.

**Vind:** smash-bøf, minute steaks, æg på restfedt.

**Tab:** tyk steak køler panden. Du skal forvarme længere end egoet tillader, eller stegen bliver grå midt på.

## Dom til «kun kød og salt»

| Steg | Vinder | Hvorfor |
| --- | --- | --- |
| Tyk ribeye / tomahawk-agtig | **Støbejern** | Masse = stabil skorpe |
| Smash / tyndt hakket | **Carbonstål** | Hurtig, jævn kontakt |
| Æg i restfedt | Begge | Carbonstål hvis du vendte steak dér; støbejern hvis æggemasse |
| Bål | Støbejern | Tåler mishandling |

## Den fejlfri carnivore-sekvens

1. Kød ud af køleskab. Dup knastørt.
2. Salt (1 % af vægten) — vent.
3. Pande til den *næsten* ryger. Animalsk fedt til det glinser.
4. Læg i. **Rør ikke.** 2–4 minutter.
5. Vend én gang. Smør/talg-bast valgfrit.
6. Hvile. Flagesalt.

Når skorpen er på plads, smager saltet af mere. Når skorpen mangler, smager det hele af hospital. Det er derfor panden er religion, når kulhydraterne er væk.
""",
        "img_src": PUBLIC / "grej" / "stoebejern-vs-carbonstaal.jpg"
        if (PUBLIC / "grej" / "stoebejern-vs-carbonstaal.jpg").exists()
        else PUBLIC / "guides" / "stoebjern-seasoning.jpg",
    },
]

# --- Recipes ---

RECIPES = [
    {
        "title": "Sukkerfri elektrolyt-shots",
        "slug": "sukkerfri-elektrolyt-shots",
        "category": "gryde",
        "description": "Sukkerfri elektrolyt-shots med lime, havsalt og kaliumsalt — hjemmelavet keto-elektrolyt uden sødemidler.",
        "prepTime": "PT5M",
        "cookTime": "PT0M",
        "totalTime": "PT5M",
        "servings": 2,
        "difficulty": "nem",
        "tags": ["elektrolyt", "keto", "low-carb", "salt", "lime", "keto-flu"],
        "imageAlt": "To shots med lime, havsalt og klart elektrolyt-vand",
        "featured": True,
        "ingredients": [
            "4 dl filtreret vand (koldt eller lunkent)",
            "Saft af 1 lime (ca. 2 spsk)",
            "1,5–2 g fint havsalt eller knust flagesalt (ca. ¼–⅓ tsk)",
            "0,5–1 g kaliumsalt (KCl) — start lavt",
            "Valgfrit: 2–3 isterninger",
        ],
        "steps": [
            "Hæld vand i en kande eller to store shot-glas.",
            "Rør salt og kaliumsalt i, til det er opløst. Smag — det skal være tydeligt salt, ikke søvand.",
            "Pres lime i. Rør. Smag igen. For skarpt: mere vand. For fladt: en knivspids mere havsalt.",
            "Server koldt. Drik 1–2 shots om dagen i keto-flu-perioden, eller efter træning.",
        ],
        "faq": [
            {
                "question": "Hvorfor kaliumsalt?",
                "answer": "Natrium alene ordner meget. Kalium hjælper mod kramper. For meget KCl smager bittert og er unødvendigt — start med en knivspids.",
            },
            {
                "question": "Kan jeg bruge Maggi eller bouillonterning?",
                "answer": "Du kan, men så får du smagsforstærker og ofte stivelse/sukker. Denne shot er ren: vand, salt, lime.",
            },
            {
                "question": "Flagesalt i glasset?",
                "answer": "Knus det først, eller vælg fint salt. Se testen af salte til elektrolyt-vand.",
            },
            {
                "question": "Er det farligt med ekstra salt?",
                "answer": "Hvis du er rask og sveder/tisser salt ud på low-carb, er det typisk det, kroppen mangler. Ved blodtryk/nyrer: spørg læge.",
            },
        ],
        "body": """Glem poser med sødemiddel-støv. Elektrolyt-shots er vand, salt, lime — og en knivspids kalium.

Læs fysikken i [keto-flu-guiden](/guides/keto-flu-og-flagesalt). Vælg salt i [testen](/guides/bedste-salte-elektrolyt-vand). Til aftenhunger: [bone broth](/opskrifter/trykkoger/gourmet-bone-broth-marvben).

Det skal smage af hav med citrus — ikke af saft.""",
        "tip": "Lav en halv liter om morgenen. Ryst før hver shot — salt synker.",
        "img_src": PUBLIC / "recipes" / "ovn" / "bagte-padron-pebre-flagesalt.jpg"
        if (PUBLIC / "recipes" / "ovn" / "bagte-padron-pebre-flagesalt.jpg").exists()
        else PUBLIC / "guides" / "saltguide.jpg",
    },
    {
        "title": "Gourmet bone broth på marvben",
        "slug": "gourmet-bone-broth-marvben",
        "category": "trykkoger",
        "description": "Gourmet bone broth på marvben i trykkoger — kollagen og mineraler på 2 timer, afsluttet med groft havsalt.",
        "prepTime": "PT15M",
        "cookTime": "PT2H",
        "totalTime": "PT2H30M",
        "servings": 6,
        "difficulty": "nem",
        "tags": ["bone broth", "fond", "marvben", "keto", "elektrolyt", "carnivore", "trykkoger", "low-carb"],
        "imageAlt": "Gylden bone broth fra marvben i skål med groft havsalt",
        "featured": True,
        "ingredients": [
            "1,5–2 kg okse-marvben (gerne savet, med synlig marv)",
            "2 spsk æblecidereddike",
            "Valgfrit (ikke carnivore-purister): 1 løg, 1 gulerod, 1 selleristilk",
            "2 laurbærblade, 8 peberkorn",
            "Vand til under max-linjen",
            "1–2 tsk groft havsalt — eller mere — til sidst",
        ],
        "steps": [
            "Rist marvbenene 35–40 minutter ved 220 °C, til de er dybt brune. Hæld stegesky fra bakken over i trykkogeren.",
            "Læg ben, eddike, krydderier og evt. grønt i gryden. Dæk med vand under max.",
            "Højt tryk 120 minutter. Naturlig udligning 20–30 minutter.",
            "Si. Køl. Et gelé-lag er succes. Skum fedtet af til stegning — eller rør det i for ekstra kalorier.",
            "Varm en kop. Salt generøst med groft havsalt, til det smager af bouillon, ikke af varmt vand.",
        ],
        "faq": [
            {
                "question": "Hvorfor kun 2 timer?",
                "answer": "Tryk trækker kollagen ud langt hurtigere end en døgnsimring. 90–120 minutter på okseben er standard.",
            },
            {
                "question": "Carnivore — uden grønt?",
                "answer": "Ja. Ben, vand, eddike, salt. Grønt er dybde, ikke krav.",
            },
            {
                "question": "Forskel på jeres andre fond?",
                "answer": "Denne er marv-tung, saltet som elektrolyt-mad og tænkt som kop-mad — ikke kun base til sauce. Se også fond i trykkoger.",
            },
            {
                "question": "Holder den?",
                "answer": "Køleskab 4–5 dage. Frys i portioner. Salt først ved servering, hvis du vil reducere frit.",
            },
        ],
        "body": """Bone broth er elektrolyt-køkkenets varme håndtag: kollagen, natrium, fedt.

Trykkogeren gør på to timer, hvad gryden bruger et døgn på. Salt til sidst — masser. Relateret: [fond i trykkoger](/opskrifter/trykkoger/fond-trykkoger), [keto-flu](/guides/keto-flu-og-flagesalt).

En kop om morgenen slår ofte et cold shot, når hovedet banker.""",
        "tip": "Gem det hvide fedtlag. Det er stegefedt til æg og [carnivore-taco](/opskrifter/ovn/carnivore-taco).",
        "img_src": PUBLIC / "recipes" / "trykkoger" / "fond-trykkoger.jpg",
    },
    {
        "title": "The Carnivore Taco",
        "slug": "carnivore-taco",
        "category": "ovn",
        "description": "Carnivore taco med osteskaller, hårdtstegt tørsaltet hakket oksekød og rygende baconfedt — ingen majs.",
        "prepTime": "PT15M",
        "cookTime": "PT25M",
        "totalTime": "PT40M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": ["carnivore", "keto", "low-carb", "taco", "ost", "baconfedt", "oksekød"],
        "imageAlt": "Carnivore-tacos med sprøde osteskaller, stegt hakket oksekød og baconfedt",
        "featured": True,
        "ingredients": [
            "200 g cheddar eller mozzarella, groft reven (til 4–6 skaller)",
            "500 g hakket oksekød (15–20 % fedt)",
            "2 tsk fint salt til kødet (tørsalt)",
            "3 spsk baconfedt",
            "Friskkværnet peber",
            "Valgfrit: sprøde bacontern, æggeblomme",
        ],
        "steps": [
            "Tørsalt kødet: bland salt i det hakkede. Fordel på bakke. Køl 20–40 minutter (eller natten over).",
            "Osteskaller: fordel osten i 4–6 cirkler på bagepapir. Bag ved 200 °C i 6–8 minutter, til kanten er dybt gylden. Drapér over en ske-skaft eller dåse, til de stivner som taco-skaller.",
            "Varm en pande med 2 spsk baconfedt til det næsten ryger. Kom kødet i. Pres fladt. Steg hårdt uden at røre, til undersiden er mørk. Hak op, vend, stegte til tørt og sprødt i kanterne.",
            "Smag til med peber. Evt. mere salt.",
            "Fyld skallerne. Dryp det sidste rygende baconfedt over. Spis med det samme.",
        ],
        "faq": [
            {
                "question": "Forskel på keto smash burger taco?",
                "answer": "Den her er ovnskaller, tørsaltet kød og baconfedt som sauce — mere carnivore, færre toppings.",
            },
            {
                "question": "Airfryer til skallerne?",
                "answer": "Ja — 180 °C i 4–5 minutter som i keto smash burger taco. Ovnen er nemmere til flere ad gangen.",
            },
            {
                "question": "Majsskaller?",
                "answer": "Nej. Det er pointen.",
            },
            {
                "question": "Kødet er tørt?",
                "answer": "Det skal være hårdtstegt. Fedtet ovenpå giver saften tilbage. Brug kød med fedt — 5 % er støv.",
            },
        ],
        "body": """Glem majs. Skallen er ost. Fyldet er tørsaltet kød, stegt til det knaser. Finish er baconfedt, der stadig ryger.

Søsterret: [keto smash burger taco](/opskrifter/airfryer/keto-smash-burger-taco). Pande-teori: [støbejern vs. carbonstål](/guides/carnivore-boeuf-stoebjern-vs-carbonstaal).""",
        "tip": "Tørsalt kødet i forvejen. Vådt hakket koger. Saltet kød steger.",
        "img_src": PUBLIC / "recipes" / "airfryer" / "keto-smash-burger-taco.jpg",
    },
    {
        "title": "Hjemmelavet pemmican",
        "slug": "pemmican",
        "category": "dehydrator",
        "description": "Hjemmelavet pemmican — dehydreret pulveriseret oksekød blandet 1:1 med nyrefedt og flagesalt. Jægerens nødration.",
        "prepTime": "PT30M",
        "cookTime": "PT8H",
        "totalTime": "PT10H",
        "servings": 12,
        "difficulty": "mellem",
        "tags": ["pemmican", "carnivore", "keto", "dehydrator", "oksekød", "nyrefedt", "bålmad", "low-carb"],
        "imageAlt": "Pemmican-barer af tørret oksekød og nyrefedt med flagesalt",
        "featured": True,
        "ingredients": [
            "500 g magert oksekød (fx culotte uden fedtkant), skåret i 5 mm skiver",
            "250–300 g okse-nyrefedt (talg), smeltet og siet",
            "1–1½ tsk flagesalt, knust",
            "Valgfrit: ½ tsk tørret urter — ellers hold den ren",
        ],
        "steps": [
            "Dehydrer kødet ved 65–70 °C i 6–10 timer, til det knækker som chips — ingen sej midte.",
            "Blend eller mortér til fint pulver. Du skal have et tørt «kødmels». Vej det.",
            "Smelt nyrefedt lavt. Si. Lad det køle til flydende, men ikke stift.",
            "Bland kødmel og fedt ca. 1:1 efter vægt. Rør flagesalt i. Massen skal samle sig som en dej.",
            "Pres i en form eller rul til barer. Køl til det stivner. Opbevar lufttæt, køligt og mørkt.",
        ],
        "faq": [
            {
                "question": "Hvorfor magert kød?",
                "answer": "Fedt i kødet harskner hurtigere under tørring. Magert kød + frisk talg giver længere holdbarhed.",
            },
            {
                "question": "Kan man bruge baconfedt?",
                "answer": "Til smag ja, til klassisk pemmican nej — talg er mere stabilt. Baconfedt er til panden.",
            },
            {
                "question": "Holdbarhed?",
                "answer": "Uger til måneder køligt og tørt, hvis kødet er knastørt og fedtet rent. Ved tvivl: køleskab.",
            },
            {
                "question": "Uden dehydrator?",
                "answer": "Laveste ovn med dør på klem. Det tager længere, og du skal passe på ikke at stege kødet.",
            },
        ],
        "body": """Pemmican er dehydratorens ultimative carnivore-snack: kødmel + talg + salt. Ingen sukker. Ingen frugt. Bare kalorier der overlever bålturen.

Teknik-hub: [dehydrering for nørder](/guides/dehydrering-for-noerder). Relateret tørt kød: [beef jerky](/opskrifter/dehydrator/beef-jerky-dehydrator).""",
        "tip": "Vej 1:1. Gætning giver enten smuldrende støv eller fedtlommer.",
        "img_src": PUBLIC / "recipes" / "dehydrator" / "beef-jerky-dehydrator.jpg",
    },
    {
        "title": "Carnivore-æggekage med sprængt svinekæbe",
        "slug": "carnivore-aeggekage-svinekaebe",
        "category": "stobejern",
        "description": "Carnivore-æggekage i støbejern med sprængt svinekæbe — fedtet fra kæberne bærer en luftig æggemasse.",
        "prepTime": "PT20M",
        "cookTime": "PT35M",
        "totalTime": "PT55M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": ["carnivore", "keto", "æggekage", "svinekæbe", "støbejern", "low-carb", "æg"],
        "imageAlt": "Æggekage i støbejern med sprængt svinekæbe og flagesalt",
        "featured": True,
        "ingredients": [
            "400 g sprængt svinekæbe (guanciale-agtig eller hjemmesprængt), skåret i tern",
            "8 æg",
            "2 spsk creme fraiche eller ekstra æggeblomme (valgfrit, til luft)",
            "Flagesalt og peber",
            "Valgfrit: 30 g reven parmesan",
        ],
        "steps": [
            "Varm støbejernspanden på middel varme. Kom kæbeternene i uden ekstra fedt. Steg til de er letsprængte/sprøde, og fedtet er smeltet ud. Tag ca. halvdelen af ternene op til topping.",
            "Pisk æg med creme fraiche, peber og evt. parmesan. Salt forsigtigt — kæberne er salte.",
            "Hæld æggemassen i panden med resten af kæberne og fedtet. Rør én gang. Skru ned.",
            "Steg til bunden sætter sig (5–8 minutter). Afslut i ovn ved 180 °C i 8–12 minutter, til midten er sat, men stadig blank.",
            "Top med de gemte tern og flagesalt. Server direkte fra jernet.",
        ],
        "faq": [
            {
                "question": "Ingen sprængt kæbe?",
                "answer": "Brug guanciale, pancetta eller tykt bacon. Pointen er saltsvin + fedt i panden.",
            },
            {
                "question": "Bliver den gummiagtig?",
                "answer": "For høj varme eller for lang tid. Bund på blus, finish i ovn, træk ud mens midten stadig er blød.",
            },
            {
                "question": "Ren carnivore uden mælkeprodukt?",
                "answer": "Skip creme fraiche og parmesan. Ekstra blomme giver stadig fedme.",
            },
            {
                "question": "Hvilken pande?",
                "answer": "Støbejern. Se carnivore-pande-guiden.",
            },
        ],
        "body": """Fedtet fra de letsprængte kæber *er* panden. Æggene lander i det og bliver en luftig masse med sprød bund.

Klassisk søster: [flæskeæggekage](/opskrifter/pande/flaeskeaeggekage). Metal: [støbejern vs. carbonstål](/guides/carnivore-boeuf-stoebjern-vs-carbonstaal).""",
        "tip": "Salt æggene sent og lidt. Sprængt kæbe har allerede gjort arbejdet.",
        "img_src": PUBLIC / "recipes" / "pande" / "flaeskeaeggekage.jpg"
        if (PUBLIC / "recipes" / "pande" / "flaeskeaeggekage.jpg").exists()
        else PUBLIC / "recipes" / "ovn" / "aeggekage-ovn.jpg",
    },
    {
        "title": "Fermenteret sennep uden sukker",
        "slug": "fermenteret-sennep-uden-sukker",
        "category": "fermentering",
        "description": "Fermenteret sennep uden sukker — gule og brune sennepskorn i 3 % saltlage i 2 uger, blendet med eddike.",
        "prepTime": "PT15M",
        "cookTime": "PT0M",
        "totalTime": "P14D",
        "servings": 20,
        "difficulty": "mellem",
        "tags": ["sennep", "fermentering", "keto", "low-carb", "uden sukker", "umami", "charcuteri"],
        "imageAlt": "Sukkerfri fermenteret sennep i glas med hele sennepskorn",
        "featured": False,
        "ingredients": [
            "100 g gule sennepskorn",
            "50 g brune sennepskorn",
            "Lage: 3 dl vand + 9 g fint salt (3 %)",
            "3–4 spsk æbleeddike",
            "Valgfrit: 1 tsk peber, ½ tsk gurkemeje for farve — ingen honning",
        ],
        "steps": [
            "Læg kornene i et rent glas. Hæld 3 % saltlage over, så de er dækket. Luftsluse eller løst låg. 14 dage ved stuetemperatur — syrlig, ikke harsk.",
            "Hæld det meste lage fra. Gem 2–3 spsk.",
            "Blend kornene med eddike og restlage til ønsket grovhed. Smag til — mere eddike for syre, mere lage for salt.",
            "Køleskab 2 dage, så skarpen sætter sig. Holder 2–3 måneder koldt.",
        ],
        "faq": [
            {
                "question": "Forskel på jeres grove fermenterede sennep?",
                "answer": "Den anden har honning. Den her er 3 % lage og nul sukker — lavet til keto og charcuteri.",
            },
            {
                "question": "For skarp?",
                "answer": "Vent 48 timer i køleskab. Varme dræber sennep — blend koldt.",
            },
            {
                "question": "2 eller 3 % lage?",
                "answer": "3 % er mere robust til længere gæring og mildere risiko for slim. 2 % er også brugt — se den grove version.",
            },
            {
                "question": "Til hvad?",
                "answer": "Pålæg, [pemmican](/opskrifter/dehydrator/pemmican)-bræt, pølser, æg og cold cuts.",
            },
        ],
        "body": """Syrlig umami-bombe uden et gram sukker. Kornene gærer i 3 % saltlage, så eddiken bare syner af finish.

Søster med honning: [fermenteret grov sennep](/opskrifter/fermentering/fermenteret-grov-sennep). Metode: [fermentering for begyndere](/guides/fermentering-for-begyndere).""",
        "tip": "3 % er 9 g salt pr. 3 dl vand. Vej. Gæt ikke.",
        "img_src": PUBLIC / "recipes" / "fermentering" / "fermenteret-grov-sennep.jpg",
    },
    {
        "title": "Airfryer bacon-twists",
        "slug": "bacon-twists",
        "category": "airfryer",
        "description": "Airfryer bacon-twists — tykke bacon-skiver snoet, drysset med chiliflager og røgsalt, stegt sprøde som low-carb fritter.",
        "prepTime": "PT10M",
        "cookTime": "PT14M",
        "totalTime": "PT25M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["bacon", "airfryer", "keto", "low-carb", "snack", "chili", "røgsalt"],
        "imageAlt": "Sprøde snoede bacon-twists med chiliflager fra airfryer",
        "featured": True,
        "ingredients": [
            "300 g tykke baconskiver (ikke papirtynde)",
            "1 tsk chiliflager",
            "1 tsk røgsalt eller [bøgerøget flagesalt](/opskrifter/roeg/roget-salt)",
            "Friskkværnet peber",
        ],
        "steps": [
            "Sno hver baconskive stramt som et reb. Læg i airfryer-kurven med luft imellem.",
            "Drys chiliflager, røgsalt og peber over.",
            "Airfry 180 °C i 10–14 minutter. Vend halvvejs. De skal være dybt røde og sprøde i kanterne.",
            "Dræn kort på rist eller køkkenrulle. Spis varme — de er low-carb-svaret på franske kartofler.",
        ],
        "faq": [
            {
                "question": "Forskel på smoked candied bacon twist?",
                "answer": "Den er røget og sød. De her er airfryer, chili, røgsalt — ingen sukker.",
            },
            {
                "question": "Tyndt bacon?",
                "answer": "Det brænder før det snoede midtpunkt er færdigt. Køb tykt.",
            },
            {
                "question": "Fedt i bunden?",
                "answer": "Gem det. Det er guld til [carnivore-taco](/opskrifter/ovn/carnivore-taco) og [baconfedt-mandler](/opskrifter/stobejern/baconfedt-mandler).",
            },
            {
                "question": "Ovnen i stedet?",
                "answer": "200 °C på rist over bakke, 15–20 minutter. Vend én gang.",
            },
        ],
        "body": """Fredagsfilm uden pommes: snoet bacon, chili, røgsalt, airfryer. Sprødt, salt, nul stivelse.

Relateret: [airfryer-bacon](/opskrifter/airfryer/bacon), [røget salt](/opskrifter/roeg/roget-salt), [Maillard på low-carb grønt](/guides/maillard-low-carb-groentsager).""",
        "tip": "Ikke overlappe. Twists der rører hinanden damper i stedet for at knase.",
        "img_src": PUBLIC / "recipes" / "roeg" / "smoked-candied-bacon-twist.jpg"
        if (PUBLIC / "recipes" / "roeg" / "smoked-candied-bacon-twist.jpg").exists()
        else PUBLIC / "recipes" / "airfryer" / "bacon.jpg",
    },
    {
        "title": "Røget low-carb chilisauce",
        "slug": "roget-low-carb-chilisauce",
        "category": "roeg",
        "description": "Røget low-carb chilisauce med røgpistol — tomater og chili koldrøges, blendes med salt og æbleeddike. Ingen sukker.",
        "prepTime": "PT20M",
        "cookTime": "PT25M",
        "totalTime": "PT45M",
        "servings": 12,
        "difficulty": "mellem",
        "tags": ["chilisauce", "røg", "røgpistol", "keto", "low-carb", "uden sukker", "umami"],
        "imageAlt": "Low-carb røget chilisauce i flaske med røgpistol ved siden af",
        "featured": False,
        "ingredients": [
            "400 g ripe tomater, kvartede",
            "100–150 g røde chili (fx cayenne eller blandet — fjern frø for mildere)",
            "2 fed hvidløg",
            "1 tsk fint salt — eller mere",
            "3 spsk æbleeddike",
            "1 spsk olie eller baconfedt",
            "Rygesmuld til røgpistol (hickory eller æble)",
        ],
        "steps": [
            "Svits tomat, chili og hvidløg i olien 8–10 minutter, til det er blødt og lidt karamelliseret. Tag af varmen.",
            "Læg blandingen i en skål. Dæk med folie. Skyd 1–2 gange kold røg ind med røgpistolen. Lad stå 3–5 minutter under folien.",
            "Blend med salt og æbleeddike til en jævn sauce. Smag til — mere salt, mere eddike, mere røg.",
            "Køl. Flaske. Køleskab 1–2 uger, eller frys i isterninger.",
        ],
        "faq": [
            {
                "question": "Uden røgpistol?",
                "answer": "Brug [røget chili](/opskrifter/roeg/roget-chili-chipotle) eller en knivspids røgpulver. Eller koldrøg tomaterne kort i røgovn.",
            },
            {
                "question": "Hvor er sukkeret?",
                "answer": "Der er ikke noget. Sødmen kommer fra ripe tomater. Det er pointen til keto.",
            },
            {
                "question": "For tynd?",
                "answer": "Simre uden låg 5–10 minutter efter blend, eller brug færre tomater.",
            },
            {
                "question": "Hvilket grej?",
                "answer": "Se grej-artiklen om røgpistol / Smoking Gun.",
            },
        ],
        "body": """Kold røg, salt, æbleeddike. Ingen sirup. Saucen skal smage af bål og chili — ikke af ketchup.

Grej: [røgpistol](/grej/roegpistol-smoking-gun). Teknik: [røget smag uden rygeovn](/guides/roget-smag-uden-rygeovn). Server til [bacon-twists](/opskrifter/airfryer/bacon-twists) og æg.""",
        "tip": "Én røgskud ad gangen. To hårde skud smager af askebæger.",
        "img_src": PUBLIC / "recipes" / "roeg" / "rogede-tomater-sauce.jpg"
        if (PUBLIC / "recipes" / "roeg" / "rogede-tomater-sauce.jpg").exists()
        else PUBLIC / "recipes" / "roeg" / "roget-chili-chipotle.jpg",
    },
]


def main() -> None:
    for g in GUIDES:
        write_guide(g)
        copy_img(g["img_src"], PUBLIC / "guides" / f"{g['slug']}.jpg")

    for r in RECIPES:
        # fix body typo if any trailing quote issues
        write_recipe(r)
        copy_img(r["img_src"], PUBLIC / "recipes" / r["category"] / f"{r['slug']}.jpg")

    print("done")


if __name__ == "__main__":
    main()
