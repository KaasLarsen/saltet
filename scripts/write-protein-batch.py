#!/usr/bin/env python3
"""Write 30 protein-focused recipes (MDX only; images via GenerateImage + copy script)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
PUBLISHED = "2026-10-21"


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


RECIPES = [
    # --- Airfryer (5) ---
    {
        "title": "Airfryer kyllingelår med harissa-yoghurt",
        "slug": "airfryer-kyllingelaar-harissa-yoghurt",
        "category": "airfryer",
        "description": "Saftige kyllingelår i airfryer med sprød skind og kølig harissa-yoghurt — højprotein midtugemad på 30 minutter.",
        "prepTime": "PT10M",
        "cookTime": "PT22M",
        "totalTime": "PT32M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "airfryer", "harissa", "yoghurt", "meal prep"],
        "imageAlt": "Gyldne airfryer-kyllingelår med harissa-yoghurt og frisk koriander",
        "ingredients": [
            "8 kyllingelår med skind (ca. 1 kg)",
            "2 spsk olivenolie",
            "2 tsk salt",
            "1 tsk røget paprika",
            "1 tsk spidskommen",
            "2 dl græsk yoghurt 10%",
            "1–1½ spsk harissa",
            "1 citron (saft + lidt skal)",
            "Frisk koriander eller persille",
        ],
        "steps": [
            "Tør lårene af. Gnid med olie, salt, paprika og spidskommen.",
            "Airfryer 190 °C i 20–22 minutter. Vend halvvejs. Skindet skal være sprødt; kernetemperatur ca. 75 °C.",
            "Rør yoghurt, harissa, citronsaft og lidt skal. Smag salt.",
            "Server lårene med sauce og urter. Spoed eventuelt overskydende fedt fra kurven.",
        ],
        "faq": [
            {
                "question": "Kan jeg bruge filet i stedet?",
                "answer": "Ja, men skær tiden til 14–16 minutter og tjek midten. Filet tørrer hurtigere end lår.",
            },
            {
                "question": "For stærk harissa?",
                "answer": "Start med 1 tsk i yoghurten. Harissa varierer — smag før du serverer.",
            },
            {
                "question": "Meal prep?",
                "answer": "Køl lårene. Sauce separat. Opvarm 160 °C i 8 minutter. Yoghurt kold på toppen.",
            },
        ],
        "body": """Kyllingelår i airfryer er protein med skind-krokant. Harissa-yoghurten køler varmen ned uden at fortynde smagen.

Saltet skal ind i kødet — ikke kun på skindet. Yoghurten er dip, ikke marinade her.""",
        "tip": "Tør skindet ekstra med køkkenrulle før olie. Vådt skind damper — tørt skind sprøder.",
    },
    {
        "title": "Protein-kyllingekroketter i airfryer",
        "slug": "airfryer-protein-kyllingekroketter",
        "category": "airfryer",
        "description": "Sprøde protein-kyllingekroketter af hakket kylling og hytteost — airfryer i stedet for friture, klar på under 25 minutter.",
        "prepTime": "PT12M",
        "cookTime": "PT12M",
        "totalTime": "PT24M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "hytteost", "airfryer", "snack", "madpakke"],
        "imageAlt": "Sprøde gyldne kyllingekroketter i airfryer-kurv med dip ved siden",
        "ingredients": [
            "500 g hakket kyllingebryst",
            "150 g hytteost",
            "1 æg",
            "40 g havregryn eller panko",
            "1 tsk salt",
            "½ tsk peber",
            "1 tsk hvidløgspulver",
            "1 tsk tørret oregano",
            "Sprayolie eller 1 spsk olie til pensling",
        ],
        "steps": [
            "Bland kylling, hytteost, æg, gryn og krydderier. Massen skal hænge sammen — tilsæt lidt flere gryn hvis den er våd.",
            "Form 12–14 ovale kroketter. Pensel let med olie.",
            "Airfryer 180 °C i 10–12 minutter. Vend efter 6 minutter. De skal være gyldne og gennemstegte.",
            "Server med yoghurt-dip, chili eller sennep.",
        ],
        "faq": [
            {
                "question": "Hvorfor hytteost?",
                "answer": "Den binder og løfter proteinet uden brødkrummer i massevis. Tør hytteost (ikke den vådeste i bakken) giver bedst greb.",
            },
            {
                "question": "Kan de fryses?",
                "answer": "Ja — rå eller stegte. Steg fra frost: +3–4 minutter i airfryeren.",
            },
            {
                "question": "For bløde?",
                "answer": "For våd hytteost. Dræn den i et dørslag 10 minutter, eller tilsæt 1 spsk ekstra gryn.",
            },
        ],
        "body": """Hakket kylling alene bliver tørt. Hytteost holder saften og skubber proteintallet op.

Airfryeren giver skorpe uden oliebassin. De er snack, madpakke og aftensmad med salat.""",
        "tip": "Våd hænder når du former. Massen klæber mindre, og kroketterne bliver ens.",
    },
    {
        "title": "Hytteost-kyllingeboller i airfryer",
        "slug": "hytteost-kyllingeboller-airfryer",
        "category": "airfryer",
        "description": "Saftige kyllingeboller med hytteost i airfryer — højt protein, minimal rod, perfekte til meal prep og madpakke.",
        "prepTime": "PT10M",
        "cookTime": "PT14M",
        "totalTime": "PT24M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "hytteost", "airfryer", "meal prep", "frikadeller"],
        "imageAlt": "Luftige hytteost-kyllingeboller stablet på tallerken med citron",
        "ingredients": [
            "500 g hakket kylling",
            "200 g hytteost",
            "1 æg",
            "2 spsk havregryn",
            "1 tsk salt",
            "½ tsk peber",
            "1 tsk dijonsennep",
            "½ tsk løgpulver",
            "Frisk dild eller persille (valgfrit)",
        ],
        "steps": [
            "Rør alt sammen til en ensartet farce. Smag salt.",
            "Form 16 bolde med våde hænder.",
            "Airfryer 180 °C i 12–14 minutter. Vend halvvejs. Kernetemperatur ca. 74 °C.",
            "Server med salat, ris eller som protein-topping på bowl.",
        ],
        "faq": [
            {
                "question": "Forskel på kroketter og bolde?",
                "answer": "Samme base — bolde er rundere og lidt saftigere indeni. Kroketter har mere skorpe-overflade.",
            },
            {
                "question": "Kan jeg bruge kalkun?",
                "answer": "Ja, 1:1. Kalkun er magrere — tilsæt 1 spsk olie i farcen hvis den føles tør.",
            },
            {
                "question": "Ovnen i stedet?",
                "answer": "200 °C i 18–20 minutter på bagepapir. Vend ikke nødvendigt.",
            },
        ],
        "body": """Hytteost i farcen er genvejen til saftige kyllingeboller uden fløde. Airfryeren gør dem gyldne uden pandestænk.

De smager bedst varme — men er også gode kolde i madpakken.""",
        "tip": "Smag en lille testbåd først (30 sekunder i micro eller 2 min i airfryer). Justér salt før du former resten.",
    },
    {
        "title": "Protein-æggemuffins med spinat og feta",
        "slug": "protein-aeggemuffins-spinat-feta",
        "category": "airfryer",
        "description": "Æggemuffins med spinat og feta i airfryer — protein-morgenmad og meal prep, klar på 20 minutter.",
        "prepTime": "PT8M",
        "cookTime": "PT12M",
        "totalTime": "PT20M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "æg", "spinat", "feta", "airfryer", "morgenmad", "meal prep"],
        "imageAlt": "Gyldne æggemuffins med spinat og feta i muffinforme",
        "ingredients": [
            "8 æg",
            "100 g frisk spinat, hakket",
            "80 g feta, smuldret",
            "2 spsk mælk eller skyr",
            "½ tsk salt",
            "Peber",
            "Lite olie eller spray til forme",
        ],
        "steps": [
            "Pisk æg med mælk/skyr, salt og peber. Fold spinat og feta i.",
            "Smør 8–10 muffinforme (silikone eller metal). Fordel blandingen.",
            "Airfryer 160 °C i 10–12 minutter, til midten er sat.",
            "Køl 2 minutter i formen, tip ud. Spis varme eller køl til madpakke.",
        ],
        "faq": [
            {
                "question": "Klæber de?",
                "answer": "Smør formene godt — eller brug silikone. Lad dem sætte sig 1–2 minutter før du tipper.",
            },
            {
                "question": "Uden feta?",
                "answer": "Hytteost eller reven cheddar. Salt lidt mere uden fetaens salt.",
            },
            {
                "question": "Holdbarhed?",
                "answer": "3–4 dage i køleskab. Frys op til 1 måned. Optø i køl, varm 150 °C i 4–5 minutter.",
            },
        ],
        "body": """Æggemuffins er protein i portionsstørrelse. Spinat og feta giver smag uden at fylde med brød.

Lav en bakke søndag — spis dem hele ugen.""",
        "tip": "Fyld kun til ¾. Æggene hæver, og overfyldte forme drypper ned i kurven.",
    },
    {
        "title": "Airfryer kalkunfilet med citron og timian",
        "slug": "airfryer-kalkunfilet-citron-timian",
        "category": "airfryer",
        "description": "Mager kalkunfilet i airfryer med citron og timian — rent protein, sprød kant, klar på 20 minutter.",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kalkun", "airfryer", "citron", "timian", "sund"],
        "imageAlt": "Skåret kalkunfilet med citronskiver og frisk timian",
        "ingredients": [
            "600–700 g kalkunfilet",
            "1 spsk olivenolie",
            "1½ tsk salt",
            "Peber",
            "1 citron (skiver + saft)",
            "4 kvist timian (eller 1 tsk tørret)",
            "1 fed hvidløg, presset",
        ],
        "steps": [
            "Tør fileten. Gnid med olie, salt, peber, hvidløg og timian. Læg citronskiver ovenpå.",
            "Airfryer 180 °C i 14–16 minutter afhængigt af tykkelse. Kernetemperatur 74 °C.",
            "Hvile 5 minutter. Dryp med citronsaft. Skær i skiver.",
            "Server med grønt, quinoa eller som pålæg dagen efter.",
        ],
        "faq": [
            {
                "question": "Bliver kalkun tørt?",
                "answer": "Kun hvis du oversteger. Termometer er din ven. Tag den ud ved 74 °C — den stiger lidt under hvilen.",
            },
            {
                "question": "Kyllingebryst i stedet?",
                "answer": "Ja, samme metode. Tiden er typisk 12–15 minutter.",
            },
            {
                "question": "Marinade overnight?",
                "answer": "Olie, citron, timian og salt natten over giver mere smag. Tør overfladen før airfryer, så den bruner.",
            },
        ],
        "body": """Kalkun er magert protein der fortjener mere end jul. Citron og timian holder det let — airfryeren holder det saftigt hvis du ikke går for langt.""",
        "tip": "Skær fileten i to lige tykke stykker hvis den er meget ujævn. Ens tykkelse = ens stegning.",
    },
    # --- Pande (5) ---
    {
        "title": "Kyllingestirfry med cashew og broccoli",
        "slug": "kyllingestirfry-cashew-broccoli",
        "category": "pande",
        "description": "Lynstegt kyllingestirfry med broccoli og cashew — højprotein wok på 20 minutter med soya og ingefær.",
        "prepTime": "PT10M",
        "cookTime": "PT10M",
        "totalTime": "PT20M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "pande", "wok", "broccoli", "cashew"],
        "imageAlt": "Wok med kyllingestykker, broccoli og cashewnødder",
        "ingredients": [
            "600 g kyllingebryst i tern",
            "300 g broccoli i buketter",
            "80 g cashewnødder",
            "2 spsk olie",
            "2 fed hvidløg, hakket",
            "1 spsk frisk ingefær, reven",
            "3 spsk sojasauce",
            "1 spsk honning eller sukkerfri sirup",
            "1 tsk sesamolie (valgfrit)",
            "Salt og peber",
        ],
        "steps": [
            "Salt kyllingen let. Varm olie på høj varme. Steg kylling i 4–5 minutter til den er gylden. Tag af panden.",
            "Steg broccoli 2–3 minutter med lidt vand, til den er sprød-mør. Tilsæt hvidløg og ingefær 30 sekunder.",
            "Kylling tilbage. Soja, honning og cashew. Vend 1 minut. Sesamolie til sidst.",
            "Server med ris, blomkålsris eller bare som den er.",
        ],
        "faq": [
            {
                "question": "For våd wok?",
                "answer": "For lav varme eller for meget i panden. Steg kylling i to hold hvis nødvendigt.",
            },
            {
                "question": "Uden cashew?",
                "answer": "Mandler eller peanuts. Rist dem kort i panden først for mere smag.",
            },
            {
                "question": "Meal prep?",
                "answer": "Ja. Køl hurtigt. Opvarm på pande — ikke micro hvis du vil beholde sprødheden i broccoli.",
            },
        ],
        "body": """Stirfry er protein på høj varme. Kyllingen først, broccoli bagefter, sauce til sidst.

Cashew giver crunch og fedt, så det ikke smager af «diæt». """,
        "tip": "Skær kyllingen ensartet — 2 cm tern. Store stykker bliver rå midt i, små bliver tørre.",
    },
    {
        "title": "Græsk kylling med hytteost",
        "slug": "graesk-kylling-hytteost",
        "category": "pande",
        "description": "Pandestegt græsk kylling med oregano, citron og cremet hytteost — proteinrig midtugeklassiker på 25 minutter.",
        "prepTime": "PT10M",
        "cookTime": "PT15M",
        "totalTime": "PT25M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "hytteost", "pande", "græsk", "citron"],
        "imageAlt": "Græsk pandestegt kylling med hytteost, oliven og citron",
        "ingredients": [
            "600 g kyllingebryst i skiver",
            "2 spsk olivenolie",
            "2 tsk tørret oregano",
            "1½ tsk salt",
            "Peber",
            "1 citron (saft + skiver)",
            "2 fed hvidløg",
            "250 g hytteost",
            "100 g cherrytomater, halverede",
            "Håndfuld oliven (valgfrit)",
        ],
        "steps": [
            "Gnid kylling med olie, oregano, salt og peber.",
            "Steg på medium-høj varme 3–4 minutter pr. side til gylden og gennemstegt. Tilsæt hvidløg sidste minut.",
            "Tag panden af varmen. Dryp citronsaft over. Fordel hytteost, tomater og oliven ovenpå — lad varmen blødgøre ost en smule.",
            "Server med salat eller bagt kartoffel.",
        ],
        "faq": [
            {
                "question": "Kan hytteosten erstattes med feta?",
                "answer": "Ja — smuldret feta er mere «græsk», men lavere volumen. Hytteost vinder på protein pr. ske.",
            },
            {
                "question": "Tør kylling?",
                "answer": "Skær skiver jævnt og undgå at stege for længe. En klat hytteost ovenpå redder også mundfølelsen.",
            },
            {
                "question": "Meal prep?",
                "answer": "Kylling og hytteost separat. Saml varmt/koldt lige før servering.",
            },
        ],
        "body": """Græske smage — oregano, citron, oliven — og så hytteost i stedet for kun feta. Mere protein, stadig middelhavs.

Panden klarer kødet. Osten er finish.""",
        "tip": "Pres hytteosten let i et dørslag hvis den er meget våd — så fortynder den ikke citronsaften.",
    },
    {
        "title": "Protein-omelet med skinke og ost",
        "slug": "protein-omelet-skinke-ost",
        "category": "pande",
        "description": "Luftig protein-omelet med skinke og ost — hurtig morgenmad eller frokost med masser af æggeprotein.",
        "prepTime": "PT5M",
        "cookTime": "PT8M",
        "totalTime": "PT13M",
        "servings": 1,
        "difficulty": "nem",
        "tags": ["protein", "æg", "skinke", "ost", "pande", "morgenmad"],
        "imageAlt": "Foldet omelet med smeltet ost og skinke på tallerken",
        "ingredients": [
            "3 æg",
            "50 g skinke i tern",
            "40 g reven ost (cheddar eller mozzarella)",
            "1 spsk smør eller olie",
            "Salt og peber",
            "Frisk purløg (valgfrit)",
        ],
        "steps": [
            "Pisk æggene med salt og peber.",
            "Varm smør på medium varme. Hæld æg i. Træk kanterne ind mod midten, så flydende æg løber ud.",
            "Når overfladen næsten er sat: fordel skinke og ost på den ene halvdel. Fold.",
            "Steg 30–60 sekunder mere. Tip ud. Purløg på toppen.",
        ],
        "faq": [
            {
                "question": "Hvor mange æg?",
                "answer": "3 er standard til én person. Vil du mere protein: tilsæt 1 æggehvide ekstra.",
            },
            {
                "question": "Bliver den gummiagtig?",
                "answer": "For høj varme. Medium — tålmodighed. Tag den af lidt før den ser «færdig» ud.",
            },
            {
                "question": "Vegetar?",
                "answer": "Skip skinke, brug spinat, svampe og ekstra ost — eller hytteost i midten.",
            },
        ],
        "body": """Omelet er protein på autopilot. Skinke og ost gør den til et måltid — ikke bare «æg».

Hold fyldet simpelt. For meget i midten, og den brækker.""",
        "tip": "Ost der smelter godt (mozzarella, cheddar) binder folden. Hård parmesan alene smuldrer ud.",
    },
    {
        "title": "Kalkunbøf med sennep og asparges",
        "slug": "kalkunboef-sennep-asparges",
        "category": "pande",
        "description": "Pandestegt kalkunbøf med sennepsglasur og asparges — magert protein med skarp finish på 20 minutter.",
        "prepTime": "PT8M",
        "cookTime": "PT12M",
        "totalTime": "PT20M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kalkun", "pande", "sennep", "asparges", "sund"],
        "imageAlt": "Kalkunbøf med sennepsglasur og grønne asparges på tallerken",
        "ingredients": [
            "4 kalkunbøffer (ca. 150 g hver)",
            "1 spsk olie",
            "1½ tsk salt",
            "Peber",
            "2 spsk dijonsennep",
            "1 spsk honning (valgfrit)",
            "400 g grønne asparges",
            "1 spsk smør",
            "½ citron",
        ],
        "steps": [
            "Salt og peber bøfferne. Steg i olie 4–5 minutter pr. side på medium-høj varme. Sidste minut: pensel med sennep (og honning).",
            "Tag kødet af til hvile. Steg asparges i samme pande med smør 3–4 minutter. Salt, peber, citronsaft.",
            "Server bøf med asparges og resten af senneppen som dip.",
        ],
        "faq": [
            {
                "question": "Kalkunbøf vs. filet?",
                "answer": "Bøffen er skåret til panden — ens tykkelse. Filet skal ofte flækkes eller bankes let.",
            },
            {
                "question": "Uden honning?",
                "answer": "Ren dijon er fint. Honning balancerer bare skarpheden.",
            },
            {
                "question": "Ovnen?",
                "answer": "Sælg panden først, færdiggør 180 °C i 5–8 minutter hvis bøfferne er tykke.",
            },
        ],
        "body": """Kalkunbøf er undervurderet midtugekød. Sennep giver bid. Asparges giver grønt uden at stjæle showet.

Kort stegning. Lang hvile. Det er hele trikset.""",
        "tip": "Bank bøfferne let under plast hvis de er ujævne — ens tykkelse betyder ens saftighed.",
    },
    {
        "title": "Lynstegt laks med soja og sesam",
        "slug": "pande-laks-soya-sesam",
        "category": "pande",
        "description": "Lynstegt lakseside med soja-sesamglasur — omega-3 og protein på panden på under 15 minutter.",
        "prepTime": "PT5M",
        "cookTime": "PT8M",
        "totalTime": "PT13M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "laks", "fisk", "pande", "soja", "sesam"],
        "imageAlt": "Pandestegt laks med sesamfrø og sojaglasur",
        "ingredients": [
            "4 lakseskiver (ca. 150 g hver)",
            "1 spsk olie",
            "Salt",
            "3 spsk sojasauce",
            "1 spsk sesamolie",
            "1 tsk honning eller sirup",
            "1 fed hvidløg, presset",
            "1 spsk sesamfrø",
            "Forårsløg til pynt",
        ],
        "steps": [
            "Tør laksen. Salt skindsiden let. Varm olie. Steg skindsiden ned 4–5 minutter til sprød.",
            "Vend. Steg kødsiden 2–3 minutter. Tag af panden.",
            "I panden: soja, sesamolie, honning og hvidløg. Boble 20 sekunder. Hæld over fisken.",
            "Drys sesam og forårsløg. Server med broccoli eller ris.",
        ],
        "faq": [
            {
                "question": "Uden skind?",
                "answer": "Steg 3–4 minutter pr. side på medium. Pas på — den går hurtigere.",
            },
            {
                "question": "For salt soja?",
                "answer": "Brug mild soja eller fortynd med 1 spsk vand. Smag før du hælder det hele på.",
            },
            {
                "question": "Rosa midt?",
                "answer": "Ja, gerne. Laks må gerne være lidt translucid midt i — ellers tørrer den.",
            },
        ],
        "body": """Laks på panden er hurtigste vej til protein og fedtsyrer. Soja og sesam er glasuren — ikke en dunk sauce.

Skindsiden først. Altid.""",
        "tip": "Pres let på fisken de første 30 sekunder, så skindet ikke slår bobler og bliver ujævnt.",
    },
    # --- Grill (4) ---
    {
        "title": "Grill-laks med dild-skyr",
        "slug": "grill-laks-dild-skyr",
        "category": "grill",
        "description": "Grillet laks med kølig dild-skyr — sommerprotein på grillen med sprød skind og frisk sauce.",
        "prepTime": "PT10M",
        "cookTime": "PT12M",
        "totalTime": "PT22M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "laks", "grill", "skyr", "dild", "fisk"],
        "imageAlt": "Grillet lakseside med dild-skyr og citron",
        "ingredients": [
            "4 lakseskiver med skind",
            "1 spsk olie",
            "1½ tsk salt",
            "Peber",
            "2 dl skyr",
            "1 bundt dild, hakket",
            "½ citron (saft)",
            "1 tsk dijonsennep",
        ],
        "steps": [
            "Olie og salt laksen. Varm grillen til medium-høj. Rist skindsiden ned 6–8 minutter med låg.",
            "Vend forsigtigt. 3–4 minutter mere. Tag af når den næsten er sat midt i.",
            "Rør skyr, dild, citron, sennep, salt og peber.",
            "Server laks med en klat dild-skyr.",
        ],
        "faq": [
            {
                "question": "Klæber fisken?",
                "answer": "Rens riste, olie fisken, og lad skindet slippe selv — vip ikke for tidligt.",
            },
            {
                "question": "Skyr eller yoghurt?",
                "answer": "Begge virker. Skyr er tykkere og mere protein pr. dl.",
            },
            {
                "question": "Hel side i stedet?",
                "answer": "Ja — indirekte varme 12–18 minutter afhængigt af tykkelse. Termometer til 50–52 °C midt i.",
            },
        ],
        "body": """Grill-laks er sommer uden at være «let mad». Dild-skyr køler og skubber proteinet yderligere op.

Salt før grillen. Sauce efter.""",
        "tip": "Læg fisken på den varmeste zone først for skind — flyt til køligere zone hvis flammerne slikker.",
    },
    {
        "title": "Grillede rejer med chili og lime",
        "slug": "grillede-rejer-chili-lime",
        "category": "grill",
        "description": "Grillede kæmperejer med chili, hvidløg og lime — lynhurtigt protein til forret eller hovedret.",
        "prepTime": "PT10M",
        "cookTime": "PT6M",
        "totalTime": "PT16M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "rejer", "grill", "chili", "lime", "fisk"],
        "imageAlt": "Grillede rejer på spyd med chili og lime",
        "ingredients": [
            "800 g store rejer, pillede (hale på)",
            "2 spsk olivenolie",
            "3 fed hvidløg, hakket",
            "1 tsk chiliflager (eller frisk chili)",
            "1½ tsk salt",
            "2 lime (saft + både)",
            "Frisk koriander",
        ],
        "steps": [
            "Vend rejer med olie, hvidløg, chili, salt og lidt limesaft. Træk på spyd hvis du vil.",
            "Grill på høj varme 2–3 minutter pr. side til de er lyserøde og har grillstriber.",
            "Dryp mere lime over. Koriander på toppen. Server med det samme.",
        ],
        "faq": [
            {
                "question": "Med skal?",
                "answer": "Gerne — mere smag og beskyttelse. Gæsterne piller selv. Stegetiden er den samme.",
            },
            {
                "question": "For små rejer?",
                "answer": "Brug kurv eller plancha-plade, ellers falder de gennem risten. 1–2 minutter pr. side.",
            },
            {
                "question": "Kan de marinere længe?",
                "answer": "Max 20–30 minutter. Lime «koger» proteinerne og gør dem melede hvis de står for længe.",
            },
        ],
        "body": """Rejer på grill er protein der er færdigt før salaten er vendt. Chili og lime er alt — ikke en tung marinade.

Tag dem af når de er lige lyserøde. Et minut ekstra, og de bliver gummi.""",
        "tip": "Tør rejerne af før olie — ellers damper de i stedet for at få grillstriber.",
    },
    {
        "title": "Protein-burger 90/10 med grillet salat",
        "slug": "protein-burger-okse-90",
        "category": "grill",
        "description": "Saftig protein-burger af 90/10 hakket oksekød med grillet romaine — mere kød, mindre bolle-fokus.",
        "prepTime": "PT15M",
        "cookTime": "PT10M",
        "totalTime": "PT25M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "oksekød", "grill", "burger", "salat", "meal prep"],
        "imageAlt": "Grillet okseburger med grillet romainesalat og tomat",
        "ingredients": [
            "600 g hakket oksekød 90/10 (eller 10–12% fedt)",
            "1½ tsk salt",
            "Peber",
            "2 hjerter romainesalat, halveret på langs",
            "1 spsk olie",
            "4 skiver tomat",
            "4 skiver ost (valgfrit)",
            "Sennep eller yoghurt-dressing",
            "Bolle valgfri — eller skip den",
        ],
        "steps": [
            "Form 4 bøffer. Salt og peber lige før grill. Lav en lille fordybning midt i, så de ikke hvælver.",
            "Grill på høj varme 3–4 minutter pr. side til ønsket stegning. Ost på sidste minut.",
            "Olie romaine-snitflader. Grill 1–2 minutter til let svedne.",
            "Stable: salat, burger, tomat, dressing. Bolle kun hvis du vil.",
        ],
        "faq": [
            {
                "question": "Hvorfor 90/10?",
                "answer": "Højt protein, stadig nok fedt til saft. 95/5 bliver let tørt på grill.",
            },
            {
                "question": "Uden bolle?",
                "answer": "Grillet romaine er brødet. Eller portobello. Protein-first.",
            },
            {
                "question": "Inde i ovnen?",
                "answer": "Pande eller grillpande på høj varme. Samme tider.",
            },
        ],
        "body": """Protein-burger er ikke «uden smag» — det er mere kød, mindre fyld. Grillet salat giver crunch og røg uden at æde makroerne.

Salt bøffen sent. Tidligt salt trækker væske ud.""",
        "tip": "Pres ikke bøffen flat på risten. Du presser saften ud i flammerne.",
    },
    {
        "title": "Grillede kyllingelår med chimichurri",
        "slug": "grillede-kyllingelaar-chimichurri",
        "category": "grill",
        "description": "Grillede kyllingelår med frisk chimichurri — saftigt protein og urteolie til weekendgrillen.",
        "prepTime": "PT15M",
        "cookTime": "PT30M",
        "totalTime": "PT45M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": ["protein", "kylling", "grill", "chimichurri", "urter"],
        "imageAlt": "Grillede kyllingelår med grøn chimichurri ovenpå",
        "ingredients": [
            "8 kyllingelår med skind",
            "2 spsk olie",
            "2 tsk salt",
            "Peber",
            "1 bundt persille",
            "½ bundt koriander (valgfrit)",
            "2 fed hvidløg",
            "1 spsk rødvineddike",
            "1 dl olivenolie",
            "½ tsk chiliflager",
            "Salt til chimichurri",
        ],
        "steps": [
            "Gnid lår med olie, salt og peber.",
            "Grill indirekte (medium) 25–30 minutter med låg, vend undervejs. Afslut 2 minutter direkte varme for skind. Kernetemperatur 75 °C.",
            "Hak persille, koriander og hvidløg. Rør med eddike, olie, chili og salt.",
            "Server lår med chimichurri over eller ved siden.",
        ],
        "faq": [
            {
                "question": "Direkte varme hele vejen?",
                "answer": "Risikabelt — ydersiden brænder før midten er færdig. Indirekte først, direkte til sidst.",
            },
            {
                "question": "Chimichurri dagen før?",
                "answer": "Ja. Smagen bliver endnu bedre. Rør op før servering.",
            },
            {
                "question": "Bryst i stedet?",
                "answer": "Kortere tid, indirekte. Pensel chimichurri på efter stegning, ellers brænder urterne.",
            },
        ],
        "body": """Chimichurri er normalt til bøf — men kyllingelår elsker den også. Fedtet fra skindet møder syren fra eddiken.

Grill lavt og langsomt. Så er kødet saftigt.""",
        "tip": "Lav chimichurri i foodprocessor, men pulse — den skal være grov, ikke pesto-smooth.",
    },
    # --- Ovn (5) ---
    {
        "title": "Protein-lasagne med hytteost",
        "slug": "protein-lasagne-hytteost",
        "category": "ovn",
        "description": "Lasagne med hytteost i stedet for tung béchamel — mere protein, stadig boblende osteskorpe.",
        "prepTime": "PT20M",
        "cookTime": "PT40M",
        "totalTime": "PT60M",
        "servings": 6,
        "difficulty": "mellem",
        "tags": ["protein", "hytteost", "ovn", "lasagne", "oksekød", "meal prep"],
        "imageAlt": "Bagt protein-lasagne med gylden osteskorpe i ildfast fad",
        "ingredients": [
            "500 g hakket oksekød eller kalkun",
            "1 løg, hakket",
            "2 fed hvidløg",
            "1 dåse hakkede tomater (400 g)",
            "2 spsk tomatpuré",
            "1 tsk oregano",
            "Salt og peber",
            "500 g hytteost",
            "1 æg",
            "12 lasagneplader",
            "150 g mozzarella, reven",
        ],
        "steps": [
            "Brun kød og løg. Tilsæt hvidløg, tomatpuré, tomater, oregano, salt og peber. Simre 10 minutter.",
            "Rør hytteost med æg og lidt salt.",
            "Lag i fad: kød, plader, hytteost — gentag. Afslut med kød og mozzarella.",
            "Bag 180 °C i 35–40 minutter til boblende og gylden. Hvile 10 minutter før skæring.",
        ],
        "faq": [
            {
                "question": "Hvorfor æg i hytteosten?",
                "answer": "Det sætter laget, så lasagnen ikke løber ud når du skærer.",
            },
            {
                "question": "Fuldkornsplader?",
                "answer": "Ja. Tjek om de skal forkoges — nogle mærker kræver ekstra væske i saucen.",
            },
            {
                "question": "Kan den fryses?",
                "answer": "Ja, bagt og afkølet. Optø i køl, genopvarm 160 °C i 25 minutter.",
            },
        ],
        "body": """Klassisk lasagne er kulhydrat med kød. Her vender vi forholdet: hytteost erstatter meget af béchamelen, og proteintallet stiger.

Den smager stadig af søndag — bare mere tanket.""",
        "tip": "Dræn hytteosten 10 minutter hvis den er meget våd. Ellers bliver midten vandet.",
    },
    {
        "title": "Ovnstegt torsk med broccoli",
        "slug": "ovnstegt-torsk-broccoli",
        "category": "ovn",
        "description": "Ovnstegt torsk og broccoli på én plade — let proteinmiddag med citron og olivenolie på 25 minutter.",
        "prepTime": "PT8M",
        "cookTime": "PT18M",
        "totalTime": "PT26M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "torsk", "fisk", "ovn", "broccoli", "sund"],
        "imageAlt": "Ovnstegt torskefilet med broccoli og citron på bageplade",
        "ingredients": [
            "4 torskefileter (ca. 150 g hver)",
            "400 g broccoli i buketter",
            "2 spsk olivenolie",
            "1½ tsk salt",
            "Peber",
            "1 citron",
            "1 tsk tørret dill eller frisk dild",
            "1 spsk smør (valgfrit)",
        ],
        "steps": [
            "Varm ovn til 200 °C. Vend broccoli med 1 spsk olie, salt og peber. Fordel på plade. Bag 8 minutter.",
            "Læg torsk på pladen. Olie, salt, peber, dild, citronskiver. Evt. en klat smør på hver filet.",
            "Bag 10–12 minutter mere, til fisken er mat og flager let.",
            "Dryp citronsaft over. Server direkte fra pladen.",
        ],
        "faq": [
            {
                "question": "Frossen torsk?",
                "answer": "Tø helt op og tør godt af. Ellers bliver den vandig i ovnen.",
            },
            {
                "question": "Anden fisk?",
                "answer": "Sei, kulmule eller laks. Laks tåler 2–3 minutter mere.",
            },
            {
                "question": "Bliver broccoli grød?",
                "answer": "Store buketter og høj varme. Start broccoli før fisken, så den får forkørsel.",
            },
        ],
        "body": """Én plade. Torsk. Broccoli. Citron. Det er protein-hverdag uden opvaskbjerg.

Salt fisken lige før ovnen, så den ikke trækker væske for tidligt.""",
        "tip": "Tør fileterne med køkkenrulle. Overfladefugt = damp = kedelig fisk.",
    },
    {
        "title": "Kyllingeform med quinoa og ost",
        "slug": "kyllingeform-quinoa-ost",
        "category": "ovn",
        "description": "Ovnbagt kyllingeform med quinoa og ost — komplet protein-måltid i ét fad til meal prep.",
        "prepTime": "PT15M",
        "cookTime": "PT30M",
        "totalTime": "PT45M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "quinoa", "ovn", "ost", "meal prep"],
        "imageAlt": "Bagt kyllingeform med quinoa og smeltet ost i ildfast fad",
        "ingredients": [
            "500 g kyllingebryst i tern",
            "200 g kogt quinoa (ca. 70 g tør)",
            "1 peberfrugt i tern",
            "1 dl creme fraiche eller skyr",
            "100 g hytteost",
            "100 g reven ost",
            "1 tsk salt",
            "Peber",
            "1 tsk paprika",
            "1 spsk olie",
        ],
        "steps": [
            "Varm ovn til 190 °C. Vend kylling med olie, salt, peber og paprika. Fordel i fad med peberfrugt.",
            "Rør quinoa, creme fraiche/skyr og hytteost. Fordel over kyllingen. Ost på toppen.",
            "Bag 25–30 minutter til kyllingen er gennemstegt og osten er gylden.",
            "Hvile 5 minutter. Server med salat.",
        ],
        "faq": [
            {
                "question": "Quinoa ikke kogt?",
                "answer": "Kog den først (1:2 quinoa:vand, 12–15 min). Rå quinoa bliver ikke færdig i fadet.",
            },
            {
                "question": "Ris i stedet?",
                "answer": "Ja, kogt ris 1:1. Quinoa har bare mere protein.",
            },
            {
                "question": "Meal prep?",
                "answer": "Perfekt. 4 bokse. Opvarm 160 °C eller micro med lidt vand.",
            },
        ],
        "body": """Kyllingeform er comfort food der stadig tæller som protein. Quinoa og hytteost gør fadet til et komplet måltid.

Én gang i ovnen. Fire dage i køleskabet.""",
        "tip": "Fordel kyllingetermene i ét lag. Stablede klumper steger ujævnt.",
    },
    {
        "title": "Protein-meatloaf med kalkun",
        "slug": "protein-meatloaf-kalkun",
        "category": "ovn",
        "description": "Saftig meatloaf af hakket kalkun med havre og æg — højprotein ovnklassiker til aftensmad og madpakke.",
        "prepTime": "PT15M",
        "cookTime": "PT45M",
        "totalTime": "PT60M",
        "servings": 6,
        "difficulty": "nem",
        "tags": ["protein", "kalkun", "ovn", "meatloaf", "meal prep", "madpakke"],
        "imageAlt": "Skåret kalkun-meatloaf med glasur på skærebræt",
        "ingredients": [
            "700 g hakket kalkun",
            "1 æg",
            "80 g havregryn",
            "1 lille løg, fint hakket",
            "2 fed hvidløg",
            "2 spsk ketchup eller tomatpuré",
            "1 spsk dijonsennep",
            "1½ tsk salt",
            "Peber",
            "1 tsk tørret timian",
            "Ekstra ketchup til glasur (valgfrit)",
        ],
        "steps": [
            "Varm ovn til 180 °C. Bland alle ingredienser (undtagen glasur). Form et brød på bagepapir eller i form.",
            "Pensel med ketchup hvis du vil. Bag 40–45 minutter til kernetemperatur 74 °C.",
            "Hvile 10 minutter. Skær i skiver. Server med grønt eller som sandwich dagen efter.",
        ],
        "faq": [
            {
                "question": "Tør meatloaf?",
                "answer": "Kalkun er magert — tilsæt 2 spsk olie eller 50 g hytteost i farcen hvis den føles tør.",
            },
            {
                "question": "Oksekød i stedet?",
                "answer": "Ja, 1:1. Bagetiden er den samme.",
            },
            {
                "question": "Kan den fryses?",
                "answer": "Ja, i skiver. Optø og varm — eller spis kold i madpakken.",
            },
        ],
        "body": """Meatloaf er amerikansk — men med kalkun og havre bliver den til dansk meal prep-protein.

Skær den når den har hvilet. Ellers smuldrer den.""",
        "tip": "Form brødet aflangt og ikke for tykt — max 6–7 cm højt — så midten bliver færdig uden at kanterne tørrer.",
    },
    {
        "title": "Bagt kyllingebryst med mozzarella",
        "slug": "bagt-kyllingebryst-mozzarella",
        "category": "ovn",
        "description": "Ovnstegt kyllingebryst med tomat og mozzarella — caprese-inspireret protein der smelter i fadet.",
        "prepTime": "PT10M",
        "cookTime": "PT25M",
        "totalTime": "PT35M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "ovn", "mozzarella", "tomat", "italiensk"],
        "imageAlt": "Bagt kyllingebryst med smeltet mozzarella og cherrytomater",
        "ingredients": [
            "4 kyllingebryster",
            "1 spsk olivenolie",
            "1½ tsk salt",
            "Peber",
            "1 tsk oregano",
            "200 g cherrytomater, halverede",
            "125 g mozzarella, skivet",
            "Frisk basilikum",
            "1 fed hvidløg",
        ],
        "steps": [
            "Varm ovn til 200 °C. Gnid kylling med olie, salt, peber og oregano. Læg i fad med hvidløg og tomater.",
            "Bag 18–20 minutter. Læg mozzarella på. Bag 5 minutter mere til osten smelter.",
            "Basilikum over. Server med salat eller zucchini.",
        ],
        "faq": [
            {
                "question": "Tyndt bryst?",
                "answer": "Tjek efter 15 minutter. Tynde fileter er færdige hurtigere.",
            },
            {
                "question": "Buffalo mozzarella?",
                "answer": "Dræn den godt — den er vådere end pizza-mozzarella.",
            },
            {
                "question": "Airfryer?",
                "answer": "180 °C i 16–18 minutter, ost på sidste 3 minutter.",
            },
        ],
        "body": """Caprese møder kyllingebryst. Tomat og mozzarella holder magert kød interessant.

Salt kyllingen ordentligt — osten er mild.""",
        "tip": "Bank brysterne til jævn tykkelse under plast. Så bliver alle fire færdige samtidig.",
    },
    # --- Gryde (4) ---
    {
        "title": "Kylling tikka masala light",
        "slug": "kylling-tikka-masala-light",
        "category": "gryde",
        "description": "Cremet kylling tikka masala med yoghurt i stedet for fløde — stadig fyldig, markant mere protein-venlig.",
        "prepTime": "PT15M",
        "cookTime": "PT25M",
        "totalTime": "PT40M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": ["protein", "kylling", "gryde", "tikka masala", "indisk", "yoghurt"],
        "imageAlt": "Kylling tikka masala i gryde med yoghurtswirl og koriander",
        "ingredients": [
            "600 g kyllingebryst i tern",
            "2 dl græsk yoghurt",
            "2 spsk tikka- eller garam masala-krydderi",
            "1 tsk salt",
            "1 spsk olie",
            "1 løg, hakket",
            "2 fed hvidløg",
            "1 spsk ingefær, reven",
            "1 dåse hakkede tomater",
            "1 dl vand eller bouillon",
            "Frisk koriander",
        ],
        "steps": [
            "Vend kylling med 1 dl yoghurt, 1 spsk krydderi og salt. Mariner 10 minutter (eller længere).",
            "Brun kylling i olie i gryde. Tag af. Svits løg, hvidløg og ingefær.",
            "Tilsæt resten af krydderi, tomater og vand. Simre 10 minutter. Kylling tilbage 5–8 minutter.",
            "Tag af varmen. Rør resten af yoghurt i. Koriander. Server med ris eller blomkålsris.",
        ],
        "faq": [
            {
                "question": "Skiller yoghurten?",
                "answer": "Rør den i uden for blusset. Kogende gryde + yoghurt = ostemasse.",
            },
            {
                "question": "Garam masala i stedet?",
                "answer": "Ja. Smag til — tilsæt evt. lidt chili og paprika.",
            },
            {
                "question": "Meal prep?",
                "answer": "Ja. Yoghurt-swirl frisk når du genopvarmer, hvis du vil have den cremet.",
            },
        ],
        "body": """Tikka masala behøver ikke en liter fløde. Yoghurt giver syre og protein — krydderierne gør det tunge løft.

Mariner kort. Brun godt. Sauce til sidst.""",
        "tip": "Brug yoghurt 5–10%. 0% skiller lettere og smager fladt i den varme sauce.",
    },
    {
        "title": "Linse-kylling dahl",
        "slug": "linse-kylling-dahl",
        "category": "gryde",
        "description": "Cremet dahl med røde linser og kylling — dobbelt protein fra bælgfrugt og kød i én gryde.",
        "prepTime": "PT10M",
        "cookTime": "PT30M",
        "totalTime": "PT40M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "linser", "gryde", "dahl", "meal prep"],
        "imageAlt": "Gul linse-kylling dahl i skål med naan ved siden",
        "ingredients": [
            "400 g kyllingebryst i tern",
            "200 g røde linser",
            "1 løg",
            "2 fed hvidløg",
            "1 spsk ingefær",
            "1 spsk olie",
            "1 spsk karry eller garam masala",
            "1 tsk gurkemeje",
            "1 dåse hakkede tomater",
            "8 dl kyllingebouillon",
            "1 tsk salt",
            "Frisk koriander",
        ],
        "steps": [
            "Skyl linser. Svits løg, hvidløg og ingefær i olie. Tilsæt krydderier 30 sekunder.",
            "Tilsæt kylling. Brun let. Linser, tomater og bouillon i. Salt.",
            "Simre 25–30 minutter under omrøring, til linser er cremede og kylling er mør.",
            "Smag salt. Koriander. Server med ris eller bare en skål.",
        ],
        "faq": [
            {
                "question": "Uden kylling?",
                "answer": "Skip den — dahl er stadig proteinrig. Eventuelt ekstra linser eller kikærter.",
            },
            {
                "question": "For tyk?",
                "answer": "Mere bouillon. Røde linser suger meget vand.",
            },
            {
                "question": "Holdbarhed?",
                "answer": "3–4 dage i køl. Bliver tykkere overnight — fortynd ved opvarmning.",
            },
        ],
        "body": """Dahl er linse-protein. Kylling er kød-protein. Sammen er det en skål der mætter uden at fylde med pasta.

Rør undervejs — linser sætter sig i bunden.""",
        "tip": "Skyl linserne til vandet er klart. Det fjerner støv og mindsker skum i gryden.",
    },
    {
        "title": "Protein-tomatsuppe med kødboller",
        "slug": "protein-tomatsuppe-koedboller",
        "category": "gryde",
        "description": "Fyldig tomatsuppe med hjemmelavede protein-kødboller — varm comfort food med ordentligt proteinindhold.",
        "prepTime": "PT15M",
        "cookTime": "PT25M",
        "totalTime": "PT40M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "oksekød", "gryde", "suppe", "kødboller", "tomat"],
        "imageAlt": "Tomatsuppe med kødboller i skål med basilikum",
        "ingredients": [
            "400 g hakket oksekød eller kylling",
            "1 æg",
            "2 spsk havregryn",
            "1 tsk salt til boller",
            "1 spsk olie",
            "1 løg",
            "2 fed hvidløg",
            "2 dåser hakkede tomater",
            "5 dl bouillon",
            "1 tsk oregano",
            "Salt og peber",
            "Frisk basilikum",
        ],
        "steps": [
            "Bland kød, æg, gryn og salt. Form små bolde.",
            "Brun bollerne i olie i gryden. Tag af. Svits løg og hvidløg.",
            "Tomater, bouillon, oregano. Simre 10 minutter. Bollerne tilbage 8–10 minutter.",
            "Smag salt. Basilikum. Server med en klat yoghurt eller hytteost ovenpå for ekstra protein.",
        ],
        "faq": [
            {
                "question": "Blender du suppen?",
                "answer": "Valgfrit — blend før bollerne kommer i, hvis du vil have den helt glat.",
            },
            {
                "question": "Kyllingeboller?",
                "answer": "Ja. Tilsæt 50 g hytteost i farcen, så de ikke bliver tørre.",
            },
            {
                "question": "Kan den fryses?",
                "answer": "Ja. Frys i portioner. Optø og varm forsigtigt, så bollerne ikke falder fra hinanden.",
            },
        ],
        "body": """Tomatsuppe alene er væske. Kødboller gør den til aftensmad. Havre i farcen binder — og holder proteinet saftigt.

Top med hytteost hvis du vil have endnu et lag.""",
        "tip": "Små bolde (3 cm) bliver færdige i saucen uden at tørre ud. Store midt-i-rå-bolde er træls.",
    },
    {
        "title": "Protein-kyllingeboller i karry",
        "slug": "protein-kyllingebooller-karry",
        "category": "gryde",
        "description": "Saftige kyllingeboller med hytteost i mild karrysauce — dansk-inspireret protein-gryde på 35 minutter.",
        "prepTime": "PT15M",
        "cookTime": "PT20M",
        "totalTime": "PT35M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "hytteost", "gryde", "karry", "dansk-klassiker"],
        "imageAlt": "Kyllingeboller i gul karrysauce i gryde",
        "ingredients": [
            "500 g hakket kylling",
            "150 g hytteost",
            "1 æg",
            "2 spsk havregryn",
            "1 tsk salt",
            "1 spsk olie",
            "1 løg",
            "1 spsk karry",
            "1 spsk hvedemel eller majsstivelse",
            "4 dl mælk eller bouillon + mælk",
            "Salt og peber",
            "Æbletern eller ærter (valgfrit)",
        ],
        "steps": [
            "Bland kylling, hytteost, æg, gryn og salt. Form bolde. Brun i olie. Tag af.",
            "Svits løg. Tilsæt karry og mel. Rør mælk/bouillon i. Simre til saucen tykner.",
            "Boller tilbage. Simre 10–12 minutter. Smag salt. Evt. æble eller ærter sidste 3 minutter.",
            "Server med ris.",
        ],
        "faq": [
            {
                "question": "Mild eller stærk karry?",
                "answer": "Start med 1 spsk mild. Smag. Du kan altid lægge mere i.",
            },
            {
                "question": "Uden mel?",
                "answer": "Reducér saucen længere, eller brug 1 tsk majsstivelse udrørt i koldt vand.",
            },
            {
                "question": "Meal prep?",
                "answer": "Ja. Sauce og boller sammen. Ris separat.",
            },
        ],
        "body": """Kyllingeboller i karry er mormor-energi med protein-upgrade. Hytteost i bollerne holder dem saftige.

Saucen skal smage salt — ellers smager det af skolemad.""",
        "tip": "Brun bollerne godt først. Smagen sidder i skorpen, ikke kun i saucen.",
    },
    # --- Plancha / støbejern (3) ---
    {
        "title": "Plancha-kylling med peberfrugt",
        "slug": "plancha-kylling-peberfrugt",
        "category": "plancha",
        "description": "Lynstegt plancha-kylling med peberfrugt og løg — fajita-energi med højt protein og sprøde grøntsager.",
        "prepTime": "PT12M",
        "cookTime": "PT10M",
        "totalTime": "PT22M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "plancha", "peberfrugt", "fajita"],
        "imageAlt": "Plancha med kyllingestrimler, peberfrugt og løg",
        "ingredients": [
            "600 g kyllingebryst i strimler",
            "2 peberfrugter i strimler",
            "1 rødløg i både",
            "2 spsk olie",
            "1½ tsk salt",
            "1 tsk røget paprika",
            "1 tsk spidskommen",
            "Peber",
            "1 lime",
            "Frisk koriander",
        ],
        "steps": [
            "Vend kylling med 1 spsk olie, salt, paprika, spidskommen og peber.",
            "Varm plancha til høj varme. Steg kylling 4–5 minutter. Skub til siden.",
            "Peberfrugt og løg med resten af olien 3–4 minutter til svedne kanter.",
            "Bland. Lime og koriander. Server i tortillas, på salat eller med ris.",
        ],
        "faq": [
            {
                "question": "Uden plancha?",
                "answer": "Stor støbejernspande eller wok. Samme metode — høj varme, ikke for meget ad gangen.",
            },
            {
                "question": "Meal prep?",
                "answer": "Ja. Genopvarm på pande. Lime frisk ved servering.",
            },
            {
                "question": "Stærkere?",
                "answer": "Chilipulver eller frisk jalapeño med grøntsagerne.",
            },
        ],
        "body": """Plancha er fajita uden restaurantpris. Kyllingestrimler får stegeskorpe. Peberfrugt skal svedes — ikke dampes.

Høj varme. Lidt ad gangen. Det er hele religionen.""",
        "tip": "Tør kyllingen før krydderi. Våd overflade = grå damp i stedet for brun skorpe.",
    },
    {
        "title": "Støbejerns-bøf med æg",
        "slug": "stobejern-bof-aeg",
        "category": "stobejern",
        "description": "Stegt bøf i støbejern med spejlæg ovenpå — klassisk protein-tallerken til brunch eller aftensmad.",
        "prepTime": "PT5M",
        "cookTime": "PT12M",
        "totalTime": "PT17M",
        "servings": 2,
        "difficulty": "nem",
        "tags": ["protein", "oksekød", "æg", "støbejern", "brunch", "bøf"],
        "imageAlt": "Støbejernspande med bøf og spejlæg",
        "ingredients": [
            "2 bøffer (entrecote, culotte eller hamburgersteak) ca. 200 g hver",
            "2–4 æg",
            "1 spsk olie eller smør",
            "Salt og peber",
            "Frisk timian eller purløg",
        ],
        "steps": [
            "Tag bøfferne ud 20 minutter før. Salt generøst. Varm støbejern til meget varmt.",
            "Olie i panden. Steg bøf 2–4 minutter pr. side efter tykkelse og ønsket stegning. Tag af til hvile. Peber.",
            "Sænk varmen. Spejlæg i samme pande. Salt.",
            "Læg æg på bøffen. Urter. Server med det samme.",
        ],
        "faq": [
            {
                "question": "Hvilken udskæring?",
                "answer": "Entrecote til fedme og smag. Culotte til magrere. Hakket bøf til budget.",
            },
            {
                "question": "Røg i køkkenet?",
                "answer": "Høj varme røger. Åbn vindue. Eller brug udendørs plancha til bøffen.",
            },
            {
                "question": "Kun æggehvider?",
                "answer": "Du kan — men blommen er smagen. Protein er i begge.",
            },
        ],
        "body": """Bøf og æg er protein uden undskyldning. Støbejernet giver skorpe. Ægget er sauce.

Salt tidligt. Hvile sent. Vend kun én gang.""",
        "tip": "Tør bøffen med køkkenrulle før den rammer panden. Vandt = grå kødsauce, ikke skorpe.",
    },
    {
        "title": "Støbejerns-kyllingelår med citron",
        "slug": "stobejern-kyllingelaar-citron",
        "category": "stobejern",
        "description": "Kyllingelår i støbejern med citron og hvidløg — sprødt skind, saftigt kød, én pande i ovnen.",
        "prepTime": "PT10M",
        "cookTime": "PT35M",
        "totalTime": "PT45M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "støbejern", "citron", "hvidløg", "ovn"],
        "imageAlt": "Støbejernspande med kyllingelår, citronskiver og hvidløg",
        "ingredients": [
            "8 kyllingelår med skind",
            "2 spsk olivenolie",
            "2 tsk salt",
            "Peber",
            "1 citron i skiver",
            "6 fed hvidløg, knuste",
            "4 kvist timian eller rosmarin",
        ],
        "steps": [
            "Varm ovn til 200 °C. Salt og peber lår. Varm olie i støbejern på komfur.",
            "Brun skindsiden 5–6 minutter uden at vippe. Vend. Læg citron, hvidløg og urter i panden.",
            "Sæt panden i ovnen 25–30 minutter til kernetemperatur 75 °C.",
            "Hvile 5 minutter. Dryp pandesaft over. Server.",
        ],
        "faq": [
            {
                "question": "Uden ovn?",
                "answer": "Fortsæt på komfur med låg på medium 20–25 minutter. Skindet bliver mindre sprødt.",
            },
            {
                "question": "Bryst i stedet?",
                "answer": "Kortere ovntid — 15–18 minutter. Tjek midten.",
            },
            {
                "question": "Kan panden i opvaskemaskinen?",
                "answer": "Nej. Vask støbejern i hånden, tør, og smør let med olie.",
            },
        ],
        "body": """Støbejern + ovn = kyllingelår med restaurant-skind. Citron og hvidløg steger med i fedtet.

Brun først. Ovnen færdiggør. Skip ikke hvil.""",
        "tip": "Brug ovnhandsker — håndtaget er lige så hot som panden når den kommer ud.",
    },
    # --- Snacks / meal prep (4) ---
    {
        "title": "Protein-hummus med hytteost",
        "slug": "protein-hummus-hytteost",
        "category": "dips",
        "description": "Cremet hummus boostet med hytteost — mere protein end klassisk version, stadig med tahin og citron.",
        "prepTime": "PT10M",
        "cookTime": "PT0M",
        "totalTime": "PT10M",
        "servings": 6,
        "difficulty": "nem",
        "tags": ["protein", "hummus", "hytteost", "dips", "kikærter", "snack"],
        "imageAlt": "Protein-hummus med hytteost i skål med olivenolie og paprika",
        "ingredients": [
            "1 dåse kikærter (240 g dryppet)",
            "150 g hytteost",
            "2 spsk tahin",
            "1 citron (saft)",
            "1 fed hvidløg",
            "½ tsk salt",
            "2 spsk olivenolie",
            "½ tsk spidskommen",
            "Vand efter behov",
            "Paprika til pynt",
        ],
        "steps": [
            "Blend kikærter, hytteost, tahin, citron, hvidløg, salt, spidskommen og 1 spsk olie.",
            "Tilsæt vand 1 spsk ad gangen til cremet konsistens.",
            "Smager salt og citron. Kom i skål. Olie og paprika på toppen.",
            "Server med grøntsagsstænger, knækbrød eller som dip til kylling.",
        ],
        "faq": [
            {
                "question": "Smager man hytteosten?",
                "answer": "Lidt — men citron, tahin og hvidløg dækker. Brug tør hytteost for mildere resultat.",
            },
            {
                "question": "Uden tahin?",
                "answer": "1 spsk peanutbutter eller ekstra olie. Tahin er dog smagen af hummus.",
            },
            {
                "question": "Holdbarhed?",
                "answer": "3–4 dage i køl i lukket bøtte.",
            },
        ],
        "body": """Hummus er allerede protein — hytteost skubber den yderligere op uden at ødelægge cremen.

Blend længe. Kornede kikærter er ikke en stil. Det er doven blending.""",
        "tip": "Gem lidt kikærtevand (aquafaba) fra dåsen. Det gør hummusen luftigere end almindeligt vand.",
    },
    {
        "title": "Protein-kyllingesalat til pålæg",
        "slug": "protein-kyllingesalat-palaeg",
        "category": "palaeg",
        "description": "Cremet kyllingesalat med skyr og sennep — protein-pålæg til madpakke, toast og knækbrød.",
        "prepTime": "PT10M",
        "cookTime": "PT0M",
        "totalTime": "PT10M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "pålæg", "skyr", "madpakke", "meal prep"],
        "imageAlt": "Kyllingesalat på rugbrød med purløg",
        "ingredients": [
            "400 g kogt eller stegt kyllingebryst, hakket",
            "150 g skyr eller græsk yoghurt",
            "1 spsk dijonsennep",
            "1 spsk mayonnaise (valgfrit)",
            "1 stang bladselleri, finthakket",
            "½ rødløg, finthakket",
            "1 tsk salt",
            "Peber",
            "Purløg",
            "1 tsk citronsaft",
        ],
        "steps": [
            "Hak kylling fint. Rør skyr, sennep, mayo, salt, peber og citron.",
            "Fold kylling, selleri og løg i. Smag til.",
            "Purløg over. Køl 15 minutter hvis du kan — smagen samler sig.",
            "Smør på rugbrød, i wrap eller spis med ske.",
        ],
        "faq": [
            {
                "question": "Hvilken kylling?",
                "answer": "Overskud fra aftensmad, rotisserie eller airfryer-bryst. Tørt bryst? Lidt ekstra skyr.",
            },
            {
                "question": "Uden mayo?",
                "answer": "Kun skyr er fint — mere protein, lidt syrligere.",
            },
            {
                "question": "Holdbarhed?",
                "answer": "2–3 dage i køl. Tag kun den portion ud, du skal bruge.",
            },
        ],
        "body": """Kyllingesalat er pålæg der faktisk mætter. Skyr erstatter det meste af mayoen — proteinet stiger, munden bliver stadig cremet.

Hak kødet fint. Store bidder falder af brødet.""",
        "tip": "Salt salaten efter du har smagt — købt rotisserie-kylling er ofte allerede saltet.",
    },
    {
        "title": "Proteinshake med skyr og bær",
        "slug": "proteinshake-skyr-baer",
        "category": "roeremaskine",
        "description": "Tykk proteinshake med skyr, bær og proteinpulver — morgenmad eller post-workout på 5 minutter.",
        "prepTime": "PT5M",
        "cookTime": "PT0M",
        "totalTime": "PT5M",
        "servings": 1,
        "difficulty": "nem",
        "tags": ["protein", "skyr", "shake", "bær", "morgenmad", "roeremaskine"],
        "imageAlt": "Lilla proteinshake med skyr og bær i glas",
        "ingredients": [
            "200 g skyr",
            "100 g frosne bær",
            "1 scoop proteinpulver (vanilje eller neutral)",
            "1–1½ dl mælk eller plantedrik",
            "1 tsk honning (valgfrit)",
            "Håndfuld spinat (valgfrit, smager ikke)",
        ],
        "steps": [
            "Kom alt i blender eller røremaskine med pisker/blendertilbehør.",
            "Blend til helt glat. Tilsæt mere væske hvis den er for tyk.",
            "Smag sødme. Hæld i glas. Evt. ekstra bær på toppen.",
        ],
        "faq": [
            {
                "question": "Uden pulver?",
                "answer": "Ja — skyr og bær er stadig proteinrige. Pulver er boost, ikke krav.",
            },
            {
                "question": "For tyk?",
                "answer": "Mere mælk. Frosne bær gør den milkshake-agtig.",
            },
            {
                "question": "Aften-snack?",
                "answer": "Brug usødet pulver og skip honning. Stadig dessert-fornemmelse.",
            },
        ],
        "body": """Proteinshake behøver ikke smage af kemi. Skyr er basen. Bær er smagen. Pulver er ekstra.

Blend til der ikke er isklumper tilbage.""",
        "tip": "Frosne bær > isterninger. De tykner og smager — is bare fortynder.",
    },
    {
        "title": "Sous vide laks med soja og ingefær",
        "slug": "sous-vide-laks-soja-ingefaer",
        "category": "sous-vide",
        "description": "Silkeblød sous vide-laks med soja og ingefær — præcist protein uden tør midte.",
        "prepTime": "PT10M",
        "cookTime": "PT45M",
        "totalTime": "PT55M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": ["protein", "laks", "sous-vide", "soja", "ingefær", "fisk"],
        "imageAlt": "Sous vide-laks med sesam og forårsløg på tallerken",
        "ingredients": [
            "4 lakseskiver (ca. 150 g)",
            "2 spsk sojasauce",
            "1 tsk sesamolie",
            "1 spsk frisk ingefær, skivet",
            "1 fed hvidløg, skivet",
            "Salt",
            "1 spsk olie til finish",
            "Sesamfrø og forårsløg",
        ],
        "steps": [
            "Sæt sous vide til 50 °C (silkeblød) eller 52 °C (lidt firmer).",
            "Salt laksen let. Pose med soja, sesamolie, ingefær og hvidløg. Fjern luft.",
            "Sous vide 40–45 minutter.",
            "Tag op. Tør overfladen. Lynsteg skindsiden 30–60 sekunder på varm pande med olie. Sesam og forårsløg.",
        ],
        "faq": [
            {
                "question": "Uden finish på pande?",
                "answer": "Du kan servere direkte — men skindet bliver ikke sprødt. En hurtig pande gør forskellen.",
            },
            {
                "question": "Kan den gå længere?",
                "answer": "Op til 1 time er fint. Meget længere bliver teksturen grødet.",
            },
            {
                "question": "Anden fisk?",
                "answer": "Torsk: 54 °C i 30–40 minutter. Tør godt før servering.",
            },
        ],
        "body": """Sous vide fjerner gætterne fra laks. 50 °C er silk. Soja og ingefær trænger ind i posen uden at koge fisken hård.

Tør før panden. Ellers får du damp, ikke skorpe.""",
        "tip": "Salt kun let før posen — sojaen bidrager allerede med natrium.",
    },
]


def main() -> None:
    for r in RECIPES:
        write_recipe(r)
    print(f"Wrote {len(RECIPES)} recipes")


if __name__ == "__main__":
    main()
