#!/usr/bin/env python3
"""Write 20 additional protein-focused recipes (MDX only)."""
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
    {
        "title": "Airfryer kyllingewings med protein-BBQ",
        "slug": "airfryer-kyllingewings-protein-bbq",
        "category": "airfryer",
        "description": "Sprøde airfryer-kyllingewings med hjemmelavet protein-BBQ — mindre sukker, mere kød, klar på 30 minutter.",
        "prepTime": "PT10M",
        "cookTime": "PT22M",
        "totalTime": "PT32M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "airfryer", "BBQ", "wings", "snack"],
        "imageAlt": "Sprøde airfryer-kyllingewings med BBQ-glasur på tallerken",
        "ingredients": [
            "1 kg kyllingewings",
            "1 spsk olie",
            "1½ tsk salt",
            "1 tsk røget paprika",
            "1 tsk hvidløgspulver",
            "Peber",
            "1½ dl BBQ-sauce (gerne sukkerfattig)",
            "2 spsk tomatpuré",
            "1 spsk æblecidereddike",
            "1 tsk røget paprika ekstra til sauce",
        ],
        "steps": [
            "Tør wings. Vend med olie, salt, paprika, hvidløg og peber.",
            "Airfryer 190 °C i 18–20 minutter. Vend halvvejs.",
            "Rør BBQ, tomatpuré, eddike og paprika. Vend wings i saucen. Airfryer 3–4 minutter mere til klistret.",
            "Server med selleristænger og yoghurt-dip.",
        ],
        "faq": [
            {
                "question": "For fede wings?",
                "answer": "Tør dem godt og brug kurven — fedtet drypper af. Du kan også klippe vingetipperne af.",
            },
            {
                "question": "Uden færdig BBQ?",
                "answer": "Tomatpuré, eddike, røget paprika, lidt honning eller sukkerfri sirup og salt. Det er nok.",
            },
            {
                "question": "Meal prep?",
                "answer": "Spis dem friske. Genopvarm 160 °C i 6–8 minutter — de mister lidt knas.",
            },
        ],
        "body": """Wings er protein med knas. Airfryeren giver skorpe uden friture. BBQ’en skal være tyk — ikke en dunk sauce der gør dem våde.

Salt før sauce. Sauce til sidst.""",
        "tip": "Læg wings i ét lag. Stablede wings damper og bliver gummi i stedet for sprøde.",
    },
    {
        "title": "Airfryer laks med pesto og parmesan",
        "slug": "airfryer-laks-pesto-parmesan",
        "category": "airfryer",
        "description": "Airfryer-laks med pesto og parmesan-skorpe — hurtigt protein med grøn smag på 15 minutter.",
        "prepTime": "PT5M",
        "cookTime": "PT12M",
        "totalTime": "PT17M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "laks", "fisk", "airfryer", "pesto", "parmesan"],
        "imageAlt": "Airfryer-laks med grøn pesto og parmesan på toppen",
        "ingredients": [
            "4 lakseskiver (ca. 150 g)",
            "3 spsk grøn pesto",
            "40 g parmesan, finrevet",
            "Salt",
            "Peber",
            "1 spsk olie til pensling",
            "Citron til servering",
        ],
        "steps": [
            "Tør laksen. Salt og peber let. Pensel overfladen med pesto. Drys parmesan.",
            "Airfryer 180 °C i 10–12 minutter, til fisken er mat og osten er let gylden.",
            "Dryp citron over. Server med salat eller asparges.",
        ],
        "faq": [
            {
                "question": "Hjemmelavet pesto?",
                "answer": "Gerne. Hold den tyk — våd pesto drypper af i kurven.",
            },
            {
                "question": "Uden skind?",
                "answer": "Ja. Tiden er den samme. Pensel lidt olie under fisken, så den ikke klæber.",
            },
            {
                "question": "Rosa midt?",
                "answer": "Ja — tag den ud når midten stadig er lidt translucid. Den fortsætter lidt.",
            },
        ],
        "body": """Pesto og parmesan giver laksen skorpe og umami uden panering. Airfryeren er hurtigere end ovnen — og mindre opvask.

Salt forsigtigt. Parmesan og pesto er allerede saltede.""",
        "tip": "Riv parmesanen fint. Grove flager brænder før fisken er færdig.",
    },
    {
        "title": "Airfryer tofu med teriyaki og sesam",
        "slug": "airfryer-tofu-teriyaki-sesam",
        "category": "airfryer",
        "description": "Sprød airfryer-tofu med teriyaki og sesam — planteprotein med knas og glasur på 25 minutter.",
        "prepTime": "PT15M",
        "cookTime": "PT15M",
        "totalTime": "PT30M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "tofu", "airfryer", "teriyaki", "sesam", "vegetar"],
        "imageAlt": "Sprød airfryer-tofu med teriyakiglasur og sesamfrø",
        "ingredients": [
            "400 g fast tofu",
            "1 spsk olie",
            "1 spsk majsstivelse eller majsena",
            "½ tsk salt",
            "3 spsk teriyakisauce (eller soja + 1 tsk honning)",
            "1 tsk sesamolie",
            "1 spsk sesamfrø",
            "Forårsløg",
        ],
        "steps": [
            "Pres tofu 10 minutter mellem køkkenrulle og en vægt. Skær i tern.",
            "Vend med olie, majsstivelse og salt. Airfryer 190 °C i 12–14 minutter. Vend halvvejs.",
            "Vend i teriyaki og sesamolie. Airfryer 2 minutter mere. Sesam og forårsløg.",
        ],
        "faq": [
            {
                "question": "Blød tofu?",
                "answer": "Nej — brug fast eller ekstra fast. Blød tofu falder fra hinanden.",
            },
            {
                "question": "Uden majsstivelse?",
                "answer": "Den bliver mindre sprød. Lidt majsstivelse er knas-tricket.",
            },
            {
                "question": "Meal prep?",
                "answer": "Ja. Genopvarm 160 °C i 5 minutter. Sauce frisk hvis du vil have den blank.",
            },
        ],
        "body": """Tofu er protein der mangler knas — indtil airfryeren. Pres den. Stivelse den. Glasér til sidst.

Våd tofu = damp. Tør tofu = skorpe.""",
        "tip": "Pres længere end du tror — 10–15 minutter. Jo tørrere, jo sprødere.",
    },
    {
        "title": "Pandestegte rejer med hvidløg og spinat",
        "slug": "pande-rejer-hvidloeg-spinat",
        "category": "pande",
        "description": "Lynstegte rejer med hvidløg og babyspinat — højprotein pandemad klar på 12 minutter.",
        "prepTime": "PT5M",
        "cookTime": "PT7M",
        "totalTime": "PT12M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "rejer", "pande", "hvidløg", "spinat", "fisk"],
        "imageAlt": "Pandestegte rejer med hvidløg og wiltet spinat",
        "ingredients": [
            "700 g store rejer, pillede",
            "2 spsk olivenolie",
            "4 fed hvidløg, skivet",
            "200 g babyspinat",
            "1 tsk salt",
            "Peber",
            "½ tsk chiliflager",
            "½ citron",
        ],
        "steps": [
            "Tør rejerne. Salt let. Varm olie på høj varme.",
            "Steg rejer 1–2 minutter pr. side til lyserøde. Tilsæt hvidløg og chili sidste minut.",
            "Spinat i panden. Vend til den falder sammen (30–60 sekunder). Citronsaft, peber.",
            "Server med brød, ris eller bare som den er.",
        ],
        "faq": [
            {
                "question": "Frosne rejer?",
                "answer": "Tø helt op og tør ekstra godt. Ellers bliver panden våd.",
            },
            {
                "question": "For gummiagtige?",
                "answer": "Du steg for længe. Rejer er færdige når de er lige lyserøde — stop der.",
            },
            {
                "question": "Uden spinat?",
                "answer": "Rucola eller chard. Eller skip grønt og server med salat ved siden.",
            },
        ],
        "body": """Rejer og spinat er protein på autopilot. Hvidløg er hele smagen. Høj varme, kort tid.

Tag dem af panden før du tror — de fortsætter lidt.""",
        "tip": "Steg rejerne i ét lag. To lag = dampede rejer uden skorpe.",
    },
    {
        "title": "Bøf stroganoff light med skyr",
        "slug": "bof-stroganoff-light-skyr",
        "category": "pande",
        "description": "Klassisk bøf stroganoff med skyr i stedet for fløde — stadig cremet, markant mere protein-venlig.",
        "prepTime": "PT15M",
        "cookTime": "PT20M",
        "totalTime": "PT35M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": ["protein", "oksekød", "pande", "stroganoff", "skyr", "svampe"],
        "imageAlt": "Cremet bøf stroganoff med skyr og svampe i pande",
        "ingredients": [
            "500 g oksekød i strimler (tyndsteg eller culotte)",
            "250 g champignon, skivet",
            "1 løg, hakket",
            "1 spsk smør eller olie",
            "1 tsk paprika",
            "1 dl bouillon",
            "2 dl skyr",
            "1 spsk dijonsennep",
            "Salt og peber",
            "Frisk dild eller persille",
        ],
        "steps": [
            "Salt kødet. Brun hurtigt på høj varme i hold. Tag af.",
            "Svits løg og svampe i samme pande. Paprika. Bouillon. Simre 5 minutter.",
            "Tag panden af varmen. Rør skyr og sennep i. Kød tilbage. Varm forsigtigt — ikke kog.",
            "Smag salt. Urter. Server med ris, pasta eller blomkålsris.",
        ],
        "faq": [
            {
                "question": "Skiller skyr?",
                "answer": "Hvis du koger den. Tag panden af blusset, rør skyr i, og varm kun til den er lun.",
            },
            {
                "question": "Fløde i stedet?",
                "answer": "Klassisk — men så er det ikke light. Skyr er protein-grebet.",
            },
            {
                "question": "Tørt kød?",
                "answer": "Brun kort og hejt. Lange strimler på lav varme bliver skosåler.",
            },
        ],
        "body": """Stroganoff behøver ikke en liter fløde. Skyr giver syre og protein. Svampene giver umami.

Brun kødet. Sauce uden for blusset. Det er forskellen.""",
        "tip": "Brug skyr 5–10%. 0% skiller lettere og smager fladt i den varme sauce.",
    },
    {
        "title": "Kylling med paprika og hytteostsauce",
        "slug": "kylling-paprika-hytteostsauce",
        "category": "pande",
        "description": "Pandestegt kylling i cremet paprika-hytteostsauce — ungarsk-inspireret protein på 25 minutter.",
        "prepTime": "PT10M",
        "cookTime": "PT15M",
        "totalTime": "PT25M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "hytteost", "pande", "paprika", "sauce"],
        "imageAlt": "Kyllingestykker i rød paprika-hytteostsauce på tallerken",
        "ingredients": [
            "600 g kyllingebryst i strimler",
            "1 spsk olie",
            "1 løg",
            "1 peberfrugt i strimler",
            "1½ spsk ægte paprika",
            "200 g hytteost",
            "1 dl bouillon eller vand",
            "1 tsk salt",
            "Peber",
            "Frisk persille",
        ],
        "steps": [
            "Steg kylling i olie til gylden. Tag af. Svits løg og peberfrugt.",
            "Paprika i panden 20 sekunder. Bouillon. Simre 3 minutter.",
            "Blend hytteost med lidt af saucen til cremet (eller mos med gaffel). Rør i panden. Kylling tilbage.",
            "Varm igennem uden at koge hårdt. Salt, peber, persille.",
        ],
        "faq": [
            {
                "question": "Kornede sauce?",
                "answer": "Blend hytteosten. Eller brug fin hytteost og rør energisk.",
            },
            {
                "question": "Røget paprika?",
                "answer": "Ja, halv/halv med sød paprika. Ren røget kan dominere.",
            },
            {
                "question": "Meal prep?",
                "answer": "Ja. Sauce tykner i køl — fortynd med lidt vand ved opvarmning.",
            },
        ],
        "body": """Paprika-kylling med hytteostsauce er comfort food uden flødebombe. Peberfrugt giver sødme. Hytteosten gør saucen til protein.

Pas på blusset når osten er i — den skal smelte sammen, ikke koge itu.""",
        "tip": "Tilsæt paprika på varm — ikke brændende — pande. Brændt paprika bliver bitter.",
    },
    {
        "title": "Grill-kalkunbøf med urter",
        "slug": "grill-kalkunboef-urter",
        "category": "grill",
        "description": "Grillet kalkunbøf med urtemarinade — magert grillprotein med citron, hvidløg og timian.",
        "prepTime": "PT10M",
        "cookTime": "PT12M",
        "totalTime": "PT22M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kalkun", "grill", "urter", "citron", "sund"],
        "imageAlt": "Grillet kalkunbøf med friske urter og citron",
        "ingredients": [
            "4 kalkunbøffer (ca. 150 g)",
            "2 spsk olivenolie",
            "2 fed hvidløg, presset",
            "1 citron (saft + skal)",
            "1 spsk frisk timian eller 1 tsk tørret",
            "1 tsk oregano",
            "1½ tsk salt",
            "Peber",
        ],
        "steps": [
            "Vend bøffer med olie, hvidløg, citron, urter, salt og peber. Mariner 10–30 minutter.",
            "Grill på medium-høj varme 5–6 minutter pr. side til kernetemperatur 74 °C.",
            "Hvile 5 minutter. Dryp ekstra citron. Server med grillet squash eller salat.",
        ],
        "faq": [
            {
                "question": "Tør kalkun på grill?",
                "answer": "Olien i marinaden og et termometer redder dig. Tag den af ved 74 °C — ikke 85.",
            },
            {
                "question": "Kyllingebryst i stedet?",
                "answer": "Ja, samme marinade. Ofte 1 minut kortere pr. side.",
            },
            {
                "question": "Inde?",
                "answer": "Grillpande eller støbejern på høj varme. Samme tider.",
            },
        ],
        "body": """Kalkun på grill er undervurderet. Urter og citron holder det let. Fedtet mangler — derfor olien i marinaden.

Vend én gang. Pres ikke. Hvile er lov.""",
        "tip": "Bank bøfferne til jævn tykkelse. Ujævne stykker bliver tørre i den tynde ende.",
    },
    {
        "title": "Grillede oksespid med protein-marinade",
        "slug": "grillede-oksespid-protein",
        "category": "grill",
        "description": "Grillede oksespid i yoghurt-marinade — møre, proteinrige spyd til weekendgrillen.",
        "prepTime": "PT20M",
        "cookTime": "PT12M",
        "totalTime": "PT32M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "oksekød", "grill", "spyd", "yoghurt", "marinade"],
        "imageAlt": "Grillede oksespid med yoghurt-marinade og grillstriber",
        "ingredients": [
            "700 g oksekød i tern (tyndsteg eller culotte)",
            "2 dl græsk yoghurt",
            "2 fed hvidløg",
            "1 spsk olivenolie",
            "1 tsk spidskommen",
            "1 tsk paprika",
            "1½ tsk salt",
            "Peber",
            "1 peberfrugt og 1 løg i stykker (valgfrit på spyddene)",
        ],
        "steps": [
            "Rør yoghurt, hvidløg, olie, krydderier, salt og peber. Vend kødet. Mariner mindst 30 minutter (gerne 2 timer).",
            "Træk på spyd, evt. med peberfrugt og løg.",
            "Grill på høj varme 3–4 minutter pr. side til ønsket stegning.",
            "Hvile 3 minutter. Server med salat og ekstra yoghurt.",
        ],
        "faq": [
            {
                "question": "Hvorfor yoghurt?",
                "answer": "Syren mørner. Fedtet holder saften. Og det er ekstra protein i marinaden.",
            },
            {
                "question": "Træspyd?",
                "answer": "Læg dem i vand 20 minutter, ellers brænder de.",
            },
            {
                "question": "Inde på plancha?",
                "answer": "Ja — høj varme, samme tider. Vend ofte.",
            },
        ],
        "body": """Yoghurt-marinade er kebab-logik til oksekød. Spyddene får skorpe ude og bliver møre indeni.

Salt i marinaden. Ikke kun på grillen.""",
        "tip": "Skær kødet ensartet — ca. 3 cm tern. Store stykker er rå midt i, når kanterne er færdige.",
    },
    {
        "title": "Protein-kyllingefad med sødkartoffel",
        "slug": "protein-kyllingefad-sodekartoffel",
        "category": "ovn",
        "description": "Ovnbagt kyllingefad med sødkartoffel og krydderier — ét-fads proteinmiddag til meal prep.",
        "prepTime": "PT15M",
        "cookTime": "PT35M",
        "totalTime": "PT50M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "ovn", "sødkartoffel", "meal prep", "fad"],
        "imageAlt": "Ovnbagt kyllingefad med sødkartoffeltern og paprika",
        "ingredients": [
            "600 g kyllingebryst i tern",
            "500 g sødkartoffel i tern",
            "1 rødløg i både",
            "2 spsk olivenolie",
            "1½ tsk salt",
            "1 tsk røget paprika",
            "1 tsk spidskommen",
            "Peber",
            "Frisk koriander eller persille",
            "½ citron",
        ],
        "steps": [
            "Varm ovn til 200 °C. Vend alt (undtagen urter og citron) på en plade eller i fad.",
            "Bag 30–35 minutter. Vend halvvejs. Kylling skal være gennemstegt, sødkartoffel mør.",
            "Citron og urter over. Server direkte eller fordel i madkasser.",
        ],
        "faq": [
            {
                "question": "Sødkartoffel rå midt i?",
                "answer": "Skær dem mindre end kyllingen — ca. 2 cm — eller giv dem 10 minutter forskud i ovnen.",
            },
            {
                "question": "Almindelig kartoffel?",
                "answer": "Ja. Samme metode. Sødkartoffel er bare sødere og hurtigere.",
            },
            {
                "question": "Meal prep?",
                "answer": "Perfekt. 4 bokse. Holder 3–4 dage i køl.",
            },
        ],
        "body": """Ét fad. Kylling. Sødkartoffel. Krydderier. Det er meal prep uden gryderet-stress.

Fordel i ét lag. Stablet mad steger ujævnt.""",
        "tip": "Tør kyllingeternene før olie og krydderi — ellers bliver de grå i stedet for gyldne.",
    },
    {
        "title": "Bagt laks med asparges og ost",
        "slug": "bagt-laks-asparges-ost",
        "category": "ovn",
        "description": "Ovnstegt laks med asparges og smeltet ost — protein og grønt på én plade på 20 minutter.",
        "prepTime": "PT8M",
        "cookTime": "PT15M",
        "totalTime": "PT23M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "laks", "fisk", "ovn", "asparges", "ost"],
        "imageAlt": "Bagt laks med grønne asparges og smeltet ost",
        "ingredients": [
            "4 lakseskiver",
            "400 g grønne asparges",
            "1 spsk olivenolie",
            "1½ tsk salt",
            "Peber",
            "80 g mozzarella eller cheddar, reven",
            "½ citron",
            "Frisk dild",
        ],
        "steps": [
            "Varm ovn til 200 °C. Læg asparges på plade med olie, salt og peber. Bag 5 minutter.",
            "Læg laks på pladen. Salt, peber. Ost på fisken. Bag 10–12 minutter mere.",
            "Citron og dild. Server fra pladen.",
        ],
        "faq": [
            {
                "question": "Tynde asparges?",
                "answer": "Skip forskuddet — læg dem samtidig med laksen, ellers bliver de for bløde.",
            },
            {
                "question": "Uden ost?",
                "answer": "Ja. Pesto eller bare citron og dild. Osten er ekstra protein og fedme.",
            },
            {
                "question": "Frossen laks?",
                "answer": "Tø op og tør godt. Ellers bliver pladen våd.",
            },
        ],
        "body": """Laks og asparges er ovnens hurtigste protein-par. Osten smelter henover — ikke under — så fisken stadig får varme.

Salt asparges og fisk hver for sig.""",
        "tip": "Knæk den træagtige ende af asparges af — den der knækker naturligt er grænsen.",
    },
    {
        "title": "Protein-cannelloni med hytteost og spinat",
        "slug": "protein-cannelloni-hytteost-spinat",
        "category": "ovn",
        "description": "Cannelloni fyldt med hytteost og spinat — ovnbagt protein-pasta med tomat og mozzarella.",
        "prepTime": "PT20M",
        "cookTime": "PT35M",
        "totalTime": "PT55M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": ["protein", "hytteost", "spinat", "ovn", "pasta", "cannelloni"],
        "imageAlt": "Bagt cannelloni med hytteost-spinatfyld og tomat sauce",
        "ingredients": [
            "12 cannelloni-rør (eller lasagneplader rullet)",
            "400 g hytteost",
            "200 g spinat, hakket (frisk eller tintet, presset)",
            "1 æg",
            "½ tsk salt",
            "Peber",
            "Muskatnød (knip)",
            "500 ml tomatsauce",
            "100 g mozzarella",
            "1 spsk olie til fadet",
        ],
        "steps": [
            "Varm ovn til 180 °C. Rør hytteost, spinat, æg, salt, peber og muskat.",
            "Fyld rørene (ske eller sprøjtepose). Læg i olieret fad ovenpå et tyndt lag tomatsauce.",
            "Hæld resten af saucen over. Mozzarella på toppen.",
            "Bag 30–35 minutter til bubblende. Hvile 5 minutter.",
        ],
        "faq": [
            {
                "question": "Rørene er hårde?",
                "answer": "Der skal være nok sauce omkring — pastaen koger i saucen. Dæk fadet med folie de første 20 minutter hvis din ovn er aggressiv.",
            },
            {
                "question": "Lasagneplader i stedet?",
                "answer": "Kog dem kort, fyld, rul. Samme fyld og sauce.",
            },
            {
                "question": "Kan den fryses?",
                "answer": "Ja, bagt. Optø i køl, genopvarm 160 °C i 25 minutter.",
            },
        ],
        "body": """Cannelloni er ricotta-territorium — hytteost er den danske protein-erstatning. Spinat fylder. Tomatsauce binder.

Fyld rørene tæt, men ikke så de sprækker.""",
        "tip": "Press spinaten virkelig tør. Våd spinat gør fyldet til suppe.",
    },
    {
        "title": "Protein-kylling i kokoskarry",
        "slug": "protein-kylling-kokoskarry",
        "category": "gryde",
        "description": "Cremet kyllingekarry med kokosmælk og masser af kød — thailandsk-inspireret protein-gryde på 30 minutter.",
        "prepTime": "PT10M",
        "cookTime": "PT20M",
        "totalTime": "PT30M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "gryde", "karry", "kokos", "asiatisk"],
        "imageAlt": "Kyllingestykker i gul kokoskarry med koriander",
        "ingredients": [
            "650 g kyllingebryst i tern",
            "1 spsk olie",
            "1 løg",
            "2 fed hvidløg",
            "1 spsk ingefær",
            "2 spsk rød eller gul karrypasta",
            "1 dåse kokosmælk (400 ml)",
            "1 dl bouillon",
            "1 tsk salt",
            "1 peberfrugt eller håndfuld spinat",
            "Lime og koriander",
        ],
        "steps": [
            "Brun kylling i olie. Tag af. Svits løg, hvidløg og ingefær. Karrypasta 30 sekunder.",
            "Kokosmælk og bouillon. Simre 5 minutter. Kylling tilbage 8–10 minutter.",
            "Peberfrugt/spinat sidste 2 minutter. Salt. Lime og koriander.",
            "Server med ris eller blomkålsris.",
        ],
        "faq": [
            {
                "question": "Light kokosmælk?",
                "answer": "Virker, men saucen bliver tyndere. Evt. reducér længere.",
            },
            {
                "question": "For stærk?",
                "answer": "Start med 1 spsk pasta. Smag. Tilføj mere.",
            },
            {
                "question": "Meal prep?",
                "answer": "Ja. Smager ofte bedre dagen efter.",
            },
        ],
        "body": """Kokoskarry er fedme der bærer krydderi. Her er kyllingen hovedpersonen — ikke risbjerget.

Brun kødet først. Pastaen i olien. Så våder du.""",
        "tip": "Rør karrypastaen ud i den varme olie før væske — smagen åbner sig.",
    },
    {
        "title": "Fyldig oksekødssuppe med protein",
        "slug": "oksekodssuppe-protein",
        "category": "gryde",
        "description": "Fyldig oksekødssuppe med masser af kød og grønt — langsimret protein til kolde dage og meal prep.",
        "prepTime": "PT15M",
        "cookTime": "PT75M",
        "totalTime": "PT90M",
        "servings": 6,
        "difficulty": "nem",
        "tags": ["protein", "oksekød", "gryde", "suppe", "meal prep", "comfort"],
        "imageAlt": "Fyldig oksekødssuppe med gulerødder og urter i skål",
        "ingredients": [
            "700 g oksekød i tern (grydekød)",
            "1 spsk olie",
            "1 løg",
            "2 gulerødder",
            "2 stilke bladselleri",
            "2 fed hvidløg",
            "2 spsk tomatpuré",
            "1½ liter oksebouillon",
            "1 laurbærblad",
            "1 tsk timian",
            "Salt og peber",
            "Persille",
        ],
        "steps": [
            "Brun kødet i olie i hold. Tag af. Svits løg, gulerod og selleri.",
            "Tomatpuré 1 minut. Bouillon, laurbær, timian, kød tilbage.",
            "Simre med låg 60–75 minutter til kødet er mørt. Smag salt.",
            "Persille over. Server med rugbrød eller alene.",
        ],
        "faq": [
            {
                "question": "Hurtigere?",
                "answer": "Trykkoger: 25–30 minutter under tryk efter bruningen.",
            },
            {
                "question": "Mere protein?",
                "answer": "Flere kødtern — eller top med en klat hytteost lige før servering.",
            },
            {
                "question": "Fryses?",
                "answer": "Ja. Portionér. Optø i køl overnight.",
            },
        ],
        "body": """Oksekødssuppe er protein i skålform. Langsimring mørner. Grøntsagerne er til, men kødet er stjernen.

Brun i hold. Ellers koger kødet gråt.""",
        "tip": "Smag salt til sidst — bouillon er forskellig, og væsken reducerer undervejs.",
    },
    {
        "title": "Støbejerns-kylling med chorizo",
        "slug": "stobejern-kylling-chorizo",
        "category": "stobejern",
        "description": "Kylling og chorizo i støbejern — spansk-inspireret proteinpande med paprika og tomat.",
        "prepTime": "PT10M",
        "cookTime": "PT30M",
        "totalTime": "PT40M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "chorizo", "støbejern", "paprika", "spansk"],
        "imageAlt": "Støbejernspande med kylling, chorizo og cherrytomater",
        "ingredients": [
            "600 g kyllingelår eller bryst i stykker",
            "150 g chorizo i skiver",
            "1 spsk olie (hvis chorizo er magert)",
            "1 løg",
            "2 fed hvidløg",
            "200 g cherrytomater",
            "1 tsk røget paprika",
            "1 tsk salt",
            "Peber",
            "Frisk persille",
        ],
        "steps": [
            "Varm støbejern. Steg chorizo til fedtet smelter. Tag af.",
            "Brun kylling i chorizo-fedtet. Salt. Løg og hvidløg i. Paprika.",
            "Tomater og chorizo tilbage. Sæt i ovn 200 °C i 15–20 minutter (eller simre med låg).",
            "Persille. Server med salat eller brød til at samle saften.",
        ],
        "faq": [
            {
                "question": "For salt?",
                "answer": "Chorizo er salt. Salt kyllingen mildt først — smag til til sidst.",
            },
            {
                "question": "Uden ovn?",
                "answer": "Simre med låg på medium 15–20 minutter. Tjek at kyllingen er gennemstegt.",
            },
            {
                "question": "Kyllingebryst?",
                "answer": "Kortere tid — 12–15 minutter i ovnen, ellers tørrer det.",
            },
        ],
        "body": """Chorizo er smagsbombe og fedtstof i ét. Kyllingen steger i det. Tomaterne giver syre.

Én pande. Minimal opvask. Maks protein.""",
        "tip": "Brug spansk chorizo til stegning — den bløde tapas-type smelter for meget.",
    },
    {
        "title": "Plancha-laks med agurk og dild",
        "slug": "plancha-laks-agurk-dild",
        "category": "plancha",
        "description": "Lynstegt plancha-laks med kølig agurk-dildsalat — sommerprotein med kontrast mellem varmt og koldt.",
        "prepTime": "PT10M",
        "cookTime": "PT8M",
        "totalTime": "PT18M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "laks", "plancha", "agurk", "dild", "fisk"],
        "imageAlt": "Plancha-stegt laks med agurk-dildsalat ved siden",
        "ingredients": [
            "4 lakseskiver",
            "1 spsk olie",
            "1½ tsk salt",
            "Peber",
            "1 agurk i tynde skiver",
            "2 dl skyr eller yoghurt",
            "1 bundt dild, hakket",
            "1 tsk dijonsennep",
            "½ citron",
        ],
        "steps": [
            "Rør skyr, dild, sennep, lidt salt og citron. Fold agurk i. Køl.",
            "Olie og salt laksen. Varm plancha til høj. Steg skindsiden 4–5 minutter, vend 2–3 minutter.",
            "Server laks med agurk-dild ved siden.",
        ],
        "faq": [
            {
                "question": "Uden plancha?",
                "answer": "Støbejern eller grillpande. Samme metode.",
            },
            {
                "question": "Agurk for vandig?",
                "answer": "Salt agurken 5 minutter, pres væsken ud, fold i dressingen.",
            },
            {
                "question": "Hel side?",
                "answer": "Ja — lidt længere tid. Brug termometer til 50–52 °C midt i.",
            },
        ],
        "body": """Varm laks. Kold agurk-dild. Kontrasten er pointen. Skyr i salaten skubber proteinet op.

Skindsiden først. Altid.""",
        "tip": "Pres ikke fisken flat på planchaen efter første kontakt — lad skindet sætte sig.",
    },
    {
        "title": "Sous vide kyllingebryst med citron og hvidløg",
        "slug": "sous-vide-kyllingebryst-citron-hvidloeg",
        "category": "sous-vide",
        "description": "Saftigt sous vide-kyllingebryst med citron og hvidløg — præcist protein uden tørt midtpunkt.",
        "prepTime": "PT10M",
        "cookTime": "PT75M",
        "totalTime": "PT85M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": ["protein", "kylling", "sous-vide", "citron", "hvidløg", "meal prep"],
        "imageAlt": "Sous vide kyllingebryst skåret i skiver med citron og hvidløg",
        "ingredients": [
            "4 kyllingebryster",
            "1 tsk salt",
            "Peber",
            "2 fed hvidløg, knuste",
            "4 skiver citron",
            "1 spsk olivenolie",
            "Frisk timian",
            "1 spsk smør eller olie til finish",
        ],
        "steps": [
            "Sæt sous vide til 65 °C.",
            "Salt og peber kylling. Pose med hvidløg, citron, olie og timian. Fjern luft.",
            "Sous vide 1–1½ time.",
            "Tag op. Tør godt. Lynsteg 45–60 sekunder pr. side i varm pande med smør. Skær i skiver.",
        ],
        "faq": [
            {
                "question": "Hvorfor 65 °C?",
                "answer": "Saftigt men gennemstegt. 60 °C er pinkere (nogle foretrækker det). 70 °C er firmer.",
            },
            {
                "question": "Kan den stå længere?",
                "answer": "Op til 2–3 timer er fint. Meget længere bliver teksturen grødet.",
            },
            {
                "question": "Meal prep?",
                "answer": "Ja — køl i posen. Finish på panden lige før servering.",
            },
        ],
        "body": """Sous vide fjerner kyllingebryst-angsten. 65 °C er saft. Citron og hvidløg er smagen i posen.

Tør før panden. Ellers ingen skorpe.""",
        "tip": "Bank brysterne til jævn tykkelse før posen — så er alle fire færdige samtidig.",
    },
    {
        "title": "Trykkoger kylling-linse-gryde",
        "slug": "trykkoger-kylling-linse-gryde",
        "category": "trykkoger",
        "description": "Kylling og linser i trykkoger — dobbelt protein, én gryde, færdig på under 30 minutter under tryk.",
        "prepTime": "PT10M",
        "cookTime": "PT25M",
        "totalTime": "PT35M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "linser", "trykkoger", "gryde", "meal prep"],
        "imageAlt": "Kylling-linse-gryde fra trykkoger i skål med urter",
        "ingredients": [
            "500 g kyllingebryst i tern",
            "200 g grønne eller brune linser",
            "1 løg",
            "2 gulerødder",
            "2 fed hvidløg",
            "1 spsk olie",
            "1 tsk spidskommen",
            "1 tsk paprika",
            "8 dl kyllingebouillon",
            "1 tsk salt",
            "Peber",
            "Frisk persille",
        ],
        "steps": [
            "Svits løg, gulerod og hvidløg i trykkogerens sautér-funktion. Krydderier 20 sekunder.",
            "Kylling, skyllede linser, bouillon, salt. Luk låget.",
            "Højt tryk 12–15 minutter. Naturlig trykaflastning 10 minutter, resten manuel.",
            "Smag salt. Persille. Server.",
        ],
        "faq": [
            {
                "question": "Røde linser?",
                "answer": "De bliver til mos — brug 8 minutter under tryk hvis du vil have dem. Grønne/brune holder formen.",
            },
            {
                "question": "Uden trykkoger?",
                "answer": "Almindelig gryde: 35–45 minutter simre, til linser er møre.",
            },
            {
                "question": "For tyk?",
                "answer": "Mere bouillon efter åbning. Linser suger stadig mens det står.",
            },
        ],
        "body": """Kylling + linser er protein-stabling. Trykkogeren gør det hverdagsmuligt.

Skyl linserne. Salt til sidst hvis din bouillon er aggressiv.""",
        "tip": "Fyld aldrig trykkogeren over max-linjen — linser skummer.",
    },
    {
        "title": "Protein-tzatziki med hytteost",
        "slug": "protein-tzatziki-hytteost",
        "category": "dips",
        "description": "Tzatziki boostet med hytteost — mere protein end klassisk yoghurtversion, stadig kølig og frisk.",
        "prepTime": "PT15M",
        "cookTime": "PT0M",
        "totalTime": "PT15M",
        "servings": 6,
        "difficulty": "nem",
        "tags": ["protein", "tzatziki", "hytteost", "dips", "agurk", "græsk"],
        "imageAlt": "Protein-tzatziki med hytteost, agurk og dild i skål",
        "ingredients": [
            "200 g hytteost",
            "150 g græsk yoghurt",
            "1 agurk",
            "2 fed hvidløg",
            "1 bundt dild",
            "1 spsk olivenolie",
            "1 tsk salt",
            "1 spsk citronsaft",
            "Peber",
        ],
        "steps": [
            "Riv agurk. Salt. Lad stå 5–10 minutter. Pres væsken ud i et dørslag.",
            "Blend eller mos hytteost til cremet. Rør yoghurt, hvidløg, dild, olie, citron, salt og peber i.",
            "Fold agurk i. Smag til. Køl 15 minutter hvis du kan.",
            "Server til grill, kylling, spyd eller som dip.",
        ],
        "faq": [
            {
                "question": "For kornede?",
                "answer": "Blend hytteosten først. Eller brug fin hytteost.",
            },
            {
                "question": "Kun yoghurt?",
                "answer": "Klassisk — men så mister du protein-boostet fra hytteosten.",
            },
            {
                "question": "Holdbarhed?",
                "answer": "2–3 dage i køl. Rør op før servering — den kan skille lidt.",
            },
        ],
        "body": """Tzatziki er allerede protein — hytteost skubber den op uden at ødelægge den græske følelse.

Pres agurken. Ellers er det agurkesuppe.""",
        "tip": "Pres agurken i et rent viskestykke — mere effektivt end hænderne alene.",
    },
    {
        "title": "Protein-tunsalat med æg",
        "slug": "protein-tunsalat-aeg",
        "category": "palaeg",
        "description": "Tunsalat med æg og skyr — klassisk protein-pålæg til madpakke, toast og knækbrød.",
        "prepTime": "PT10M",
        "cookTime": "PT8M",
        "totalTime": "PT18M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "tun", "æg", "pålæg", "skyr", "madpakke"],
        "imageAlt": "Tunsalat med æg på rugbrød med purløg",
        "ingredients": [
            "2 dåser tun i vand (ca. 200 g dryppet)",
            "2 æg, hårdkogte",
            "150 g skyr",
            "1 spsk mayonnaise (valgfrit)",
            "1 tsk dijonsennep",
            "½ rødløg, finthakket",
            "1 stang bladselleri, hakket",
            "½ tsk salt",
            "Peber",
            "Purløg",
        ],
        "steps": [
            "Kog æggene 8–9 minutter. Køl. Hak groft.",
            "Dræn tun. Mos let med skyr, mayo, sennep, salt og peber.",
            "Fold æg, løg og selleri i. Purløg over.",
            "Smør på rugbrød eller spis med ske.",
        ],
        "faq": [
            {
                "question": "Tun i olie?",
                "answer": "Dræn godt. Smagen er federe — skip eventuelt mayo.",
            },
            {
                "question": "Uden æg?",
                "answer": "Ja. Tilføj ekstra skyr eller agurk for fylde.",
            },
            {
                "question": "Holdbarhed?",
                "answer": "2 dage i køl. Æg og fisk = frisk er bedst.",
            },
        ],
        "body": """Tun + æg er protein-stabling til pålæg. Skyr holder det cremet uden mayo-bjerg.

Dræn tunen hårdt. Våd tunsalat gør brødet slattent.""",
        "tip": "Hak æggene groft — for fine stykker forsvinder, for store falder af brødet.",
    },
    {
        "title": "Protein-pandekagebatter med hytteost",
        "slug": "protein-pandekagebatter-hytteost",
        "category": "roeremaskine",
        "description": "Luftigt protein-pandekagebatter med hytteost — blendet i røremaskine, klar til panden på 5 minutter.",
        "prepTime": "PT5M",
        "cookTime": "PT15M",
        "totalTime": "PT20M",
        "servings": 2,
        "difficulty": "nem",
        "tags": ["protein", "hytteost", "pandekager", "roeremaskine", "morgenmad", "æg"],
        "imageAlt": "Stabel proteinpandekager med hytteostbatter og bær",
        "ingredients": [
            "200 g hytteost",
            "3 æg",
            "60 g havregryn",
            "1 tsk bagepulver",
            "1 tsk vanilje",
            "Pinch salt",
            "Smør eller olie til panden",
            "Bær eller skyr til topping",
        ],
        "steps": [
            "Blend hytteost, æg, havre, bagepulver, vanilje og salt i røremaskine/blender til glat.",
            "Hvile 2 minutter (havren suger).",
            "Steg små pandekager på medium varme 2–3 minutter pr. side til gyldne.",
            "Server med bær og en klat skyr.",
        ],
        "faq": [
            {
                "question": "Batter for tyndt?",
                "answer": "1 spsk ekstra havre. For tykt: 1 spsk mælk.",
            },
            {
                "question": "Uden blender?",
                "answer": "Mos hytteost fint med gaffel — der kan være lidt struktur. Det er fint.",
            },
            {
                "question": "Salte version?",
                "answer": "Skip vanilje. Tilsæt purløg og ost. Steg som proteinvafler/pandekager til laks.",
            },
        ],
        "body": """Hytteost i batteret er proteinpandekagens hemmelighed. Røremaskinen gør det glat på sekunder.

Medium varme. For høj, og midten er rå mens kanten brænder.""",
        "tip": "Lav dem mindre end du tror — de er nemmere at vende, og midten sætter sig.",
    },
]


def main() -> None:
    for r in RECIPES:
        write_recipe(r)
    print(f"Wrote {len(RECIPES)} recipes")


if __name__ == "__main__":
    main()
