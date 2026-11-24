#!/usr/bin/env python3
"""5 julebag-/konfekt-huller (nov 2026).

Springer jødekager (ovn) og havregrynskugler (pande) over — de findes.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"
PUBLIC = Path(__file__).resolve().parent.parent / "public/recipes"
PUBLISHED = "2026-11-24"

RECIPES = [
    {
        "cat": "airfryer",
        "title": "Pebernødder i airfryer",
        "slug": "pebernoedder-airfryer",
        "description": "Pebernødder i airfryer — hurtig portion krydrede julesmåkager på ca. 8 minutter uden at tænde den store ovn.",
        "prepTime": "PT25M",
        "cookTime": "PT8M",
        "totalTime": "PT1H35M",
        "servings": 40,
        "difficulty": "nem",
        "tags": [
            "pebernødder",
            "småkager",
            "jul",
            "airfryer",
            "dessert",
            "bagværk",
            "festmad",
        ],
        "relatedGrej": ["airfryer-tilbehoer"],
        "imageAlt": "Små brune pebernødder fra airfryeren i en juleskål",
        "ingredients": [
            "250 g hvedemel",
            "125 g smør, blødt",
            "125 g farin",
            "1 æg",
            "1 tsk stødt peber",
            "1 tsk kanel",
            "½ tsk stødt ingefær",
            "½ tsk stødt nellike",
            "½ tsk bagepulver",
            "1 knivspids salt",
        ],
        "steps": [
            "Rør smør og farin luftigt. Tilsæt æg. Bland mel, krydderier, bagepulver og salt i. Ælt kort til en blød dej.",
            "Form to pølser (ca. 2–3 cm tykke). Pak ind, og køl mindst 1 time — gerne længere.",
            "Skær i små nødder (ca. 1 cm). Læg i ét lag på bagepapir i airfryer-kurven.",
            "Airfry 160 °C i 7–9 minutter, til de er dybt gyldne. Køl på rist — de sprøder op. Flere hold efter behov.",
        ],
        "faq": [
            {
                "question": "Forskel på [pebernødder i ovn](/opskrifter/ovn/pebernoedder)?",
                "answer": "Samme dej. Airfryer er hurtigere til små portioner — ovn vinder, hvis du bager hele dåsen på én gang.",
            },
            {
                "question": "De bliver for mørke?",
                "answer": "For høj varme eller for længe. 160 °C. Første hold er din kalibrering — pebernødder bruner hurtigt.",
            },
            {
                "question": "Kan dejen fryses?",
                "answer": "Ja. Frys pølserne. Tø 10 minutter i køleskab, skær, bag direkte.",
            },
            {
                "question": "Hvor længe holder de?",
                "answer": "2–3 uger i tæt dåse. Smagen bliver mere peber efter et par dage.",
            },
        ],
        "body": "Pebernødder i airfryer er december-turbo: samme krydderdej, små hold, 8 minutter.\n\nIkke hele ovnen. Bare knas i skålen.",
        "tip": "Skær dem ens. Ujævne nødder = nogle brændte, nogle dejede i samme hold.",
    },
    {
        "cat": "ovn",
        "title": "Specier",
        "slug": "specier",
        "description": "Specier — bløde, peberkrydrede julesmåkager med sprød kant. Den klassiker, der mangler i småkagedåsen ved siden af pebernødder og brunkager.",
        "prepTime": "PT30M",
        "cookTime": "PT12M",
        "totalTime": "PT2H",
        "servings": 40,
        "difficulty": "nem",
        "tags": [
            "specier",
            "småkager",
            "jul",
            "dessert",
            "ovn",
            "peber",
            "festmad",
        ],
        "relatedGrej": [],
        "imageAlt": "Runde gyldne specier med peber og kanel på julefad",
        "ingredients": [
            "250 g hvedemel",
            "125 g smør, blødt",
            "125 g farin",
            "1 æg",
            "1 tsk stødt hvid peber (eller sort)",
            "1 tsk kanel",
            "½ tsk stødt nellike",
            "½ tsk bagepulver",
            "1 knivspids salt",
            "Evt. perlesukker til pynt",
        ],
        "steps": [
            "Rør smør og farin luftigt. Tilsæt æg. Bland mel, peber, kanel, nellike, bagepulver og salt i. Ælt til en blød, smidig dej.",
            "Form en pølse (ca. 4 cm tyk). Pak ind, og køl mindst 1 time.",
            "Skær i 1 cm skiver, eller rul kugler og tryk dem flade. Læg på bagepapir. Evt. drys perlesukker.",
            "Bag ved 175 °C varmluft 10–12 minutter, til kanterne er gyldne, men midten stadig ser blød ud. Køl på rist — midten sætter sig.",
        ],
        "faq": [
            {
                "question": "Forskel på [pebernødder](/opskrifter/ovn/pebernoedder)?",
                "answer": "Pebernødder er små og knasende hele vejen. Specier er større, blødere i midten, med peber i fokus.",
            },
            {
                "question": "Forskel på [brunkager](/opskrifter/ovn/brunkager)?",
                "answer": "Brunkager er tynde, sirupssprøde skiver. Specier er tykkere og peber-runde.",
            },
            {
                "question": "Hvid eller sort peber?",
                "answer": "Hvid er klassisk til specier — ren varme uden mørke prikker. Sort virker også.",
            },
            {
                "question": "De er for hårde?",
                "answer": "Bagt for længe. Tag dem ud, mens midten stadig giver efter. De stivner under afkøling.",
            },
        ],
        "body": "Specier er peberens småkage: blød midte, gylden kant, plads i dåsen ved siden af pebernødder og [jødekager](/opskrifter/ovn/joedekager).\n\nIkke brunkage. Ikke pebernød. Sin egen.",
        "tip": "Køl dejen ordentligt. Varm dej spreder sig til pandekager i ovnen.",
    },
    {
        "cat": "pande",
        "title": "Marcipanbrød",
        "slug": "marcipanbroed",
        "description": "Marcipanbrød — klassisk julekonfekt af marcipan formet som brød, dyppet i chokolade. Nul ovntid.",
        "prepTime": "PT25M",
        "cookTime": "PT0M",
        "totalTime": "PT50M",
        "servings": 16,
        "difficulty": "nem",
        "tags": [
            "marcipanbrød",
            "marcipan",
            "julekonfekt",
            "jul",
            "dessert",
            "konfekt",
            "chokolade",
        ],
        "relatedGrej": [],
        "imageAlt": "Marcipanbrød dyppet i mørk chokolade skåret i skiver",
        "ingredients": [
            "400 g marcipan (min. 50–60 % mandel)",
            "Flormelis til bordet",
            "200 g mørk chokolade",
            "Valgfrit: 50 g blød nougat til midten, eller hakkede mandler til pynt",
        ],
        "steps": [
            "Ælt marcipanen kort på flormelis, til den er smidig. Form 2–3 små brød (pølser med let afrundede ender), ca. 3 cm tykke.",
            "Valgfrit: lav en rende, læg en tynd nougatpølse i, luk sammen. Køl 15 minutter.",
            "Smelt chokoladen over vandbad. Dyp brødene helt eller pensl tykt. Læg på bagepapir. Pynt, før chokoladen stivner.",
            "Lad stivne. Skær i skiver med skarp kniv lige før servering — eller server hele.",
        ],
        "faq": [
            {
                "question": "Forskel på [marcipankonfekt](/opskrifter/ovn/marcipankonfekt)?",
                "answer": "Konfekt er små bidder. Marcipanbrød er ét stykke, der skæres — mere gave, mere fad.",
            },
            {
                "question": "Med nougat i midten?",
                "answer": "Ja. Blød [nougat](/opskrifter/pande/nougat-konfekt) eller købt pladenougat. Ikke for meget — ellers skrider formen.",
            },
            {
                "question": "Skal det bages?",
                "answer": "Nej. Rå marcipan + chokolade. Vil du have bagt skorpe, se [kransekagekonfekt](/opskrifter/ovn/kransekagekonfekt).",
            },
            {
                "question": "Holdbarhed?",
                "answer": "Lufttæt 1–2 uger køligt. Skær først ved servering, så snitfladen ikke tørrer.",
            },
        ],
        "body": "Marcipanbrød er julekonfekt uden ovn: god marcipan, chokolade, skåret til kaffen.\n\nForm. Dyp. Skær.",
        "tip": "Vej brødene ens (ca. 120–150 g), så chokoladen rækker, og de ser ud som et sæt.",
    },
    {
        "cat": "pande",
        "title": "Nougat-konfekt",
        "slug": "nougat-konfekt",
        "description": "Blød nougat-konfekt til julehyggen — chokolade, nødder og nul ovntid. Til dåsen eller midten af marcipanbrød.",
        "prepTime": "PT20M",
        "cookTime": "PT5M",
        "totalTime": "PT2H25M",
        "servings": 24,
        "difficulty": "nem",
        "tags": [
            "nougat",
            "julekonfekt",
            "jul",
            "dessert",
            "konfekt",
            "chokolade",
            "hasselnødder",
        ],
        "relatedGrej": [],
        "imageAlt": "Blød nougat-konfekt i firkanter med hasselnødder",
        "ingredients": [
            "200 g mørk chokolade",
            "100 g mælkechokolade",
            "100 g blød smør",
            "3 spsk flormelis",
            "100 g ristede hasselnødder, grofthakkede (eller mandler)",
            "1 knivspids flagesalt",
            "Evt. 1 spsk kakao til rulning",
        ],
        "steps": [
            "Smelt chokolade og smør over vandbad under omrøring, til det er blankt. Tag af varmen.",
            "Rør flormelis, nødder og salt i. Smagen skal være nøddeagtig og ikke for sød.",
            "Hæld i en lille form med bagepapir (ca. 15×15 cm). Glat overfladen. Køl mindst 2 timer, til den er fast nok at skære.",
            "Skær i firkanter. Evt. rul let i kakao. Opbevar køligt i dåse.",
        ],
        "faq": [
            {
                "question": "Er det fransk hård nougat?",
                "answer": "Nej. Det her er blød dansk jule-nougat — chokolade og nødder. Ikke æggehvide-honning-nougat.",
            },
            {
                "question": "Til [marcipanbrød](/opskrifter/pande/marcipanbroed)?",
                "answer": "Ja. Brug en strimmel som fyld, før du dypper brødet i chokolade.",
            },
            {
                "question": "Uden mælkechokolade?",
                "answer": "Kun mørk virker — tilsæt 1 ekstra spsk flormelis, ellers bliver den bitter.",
            },
            {
                "question": "Holdbarhed?",
                "answer": "1–2 uger køligt i tæt dåse. Frys gerne.",
            },
        ],
        "body": "Nougat-konfekt er julehygge uden ovn: chokolade, smør, ristede nødder, salt.\n\nKøl. Skær. Dåse.",
        "tip": "Rist nødderne først. Rå nødder smager af træ — ristede smager af jul.",
    },
    {
        "cat": "airfryer",
        "title": "Danske klejner i airfryer",
        "slug": "klejner-airfryer",
        "description": "Klassiske danske snoede klejner i airfryer — alternativ til friture og stor ovn, med flormelis og juleknas.",
        "prepTime": "PT35M",
        "cookTime": "PT8M",
        "totalTime": "PT1H15M",
        "servings": 20,
        "difficulty": "mellem",
        "tags": [
            "klejner",
            "jul",
            "airfryer",
            "bagværk",
            "dessert",
            "dansk",
            "festmad",
        ],
        "relatedGrej": ["airfryer-tilbehoer", "oliesprayflasker-airfryer"],
        "imageAlt": "Gyldne danske klejner fra airfryeren med flormelis",
        "ingredients": [
            "250 g hvedemel",
            "50 g sukker",
            "1 tsk kardemomme",
            "1 tsk bagepulver",
            "75 g smør, koldt",
            "1 æg",
            "2 spsk fløde",
            "1 spsk hvidt rum eller vand",
            "1 spsk olie til pensling",
            "Flormelis til pynt",
        ],
        "steps": [
            "Bland mel, sukker, kardemomme og bagepulver. Smuldr smør i. Æg, fløde og rum — ælt kort til dej. Køl 30 minutter.",
            "Rul tyndt (2–3 mm). Skær romber. Skær midtersnit, træk den ene ende igennem — klassisk dansk klejneform.",
            "Pensl eller spray let med olie. Forvarm airfryer til 170 °C.",
            "Bag 6–8 ad gangen i 6–8 minutter, vend halvvejs, til gyldne. Drys flormelis, mens de er lune.",
        ],
        "faq": [
            {
                "question": "Forskel på [norske klejner](/opskrifter/airfryer/norske-klejner)?",
                "answer": "Norske er mere donut-agtige og ofte tykkere. Denne følger den danske ovn-/frituredej — tyndere, mere småkage.",
            },
            {
                "question": "Forskel på [klejner i ovn](/opskrifter/ovn/klejner-ovn) og [friture](/opskrifter/pande/klejner-friture)?",
                "answer": "Samme form. Friture er ægte knas. Ovn er plade. Airfryer er hurtig mellemting uden oliebad.",
            },
            {
                "question": "Dejen er for blød?",
                "answer": "Køl længere. Lidt ekstra mel. Den skal kunne rulles tyndt uden at klæbe.",
            },
            {
                "question": "Hvor længe holder de?",
                "answer": "Lufttæt 4–5 dage. Flormelis lige før servering, hvis du gemmer dem.",
            },
        ],
        "body": "Danske klejner i airfryer er snoet jul uden frituregryde: tynd dej, slynge, oliepensling, flormelis.\n\nIkke norske donuts. Dansk småkage-klejne.",
        "tip": "Snittet i midten skal være stort nok. Små huller lukker sig, og slyngen forsvinder.",
    },
]


def yaml_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def to_mdx(d: dict) -> str:
    cat = d["cat"]
    tags = "\n".join(f"  - {yaml_str(t)}" for t in d["tags"])
    ings = "\n".join(f"  - {yaml_str(x)}" for x in d["ingredients"])
    steps = "\n".join(f"  - {yaml_str(x)}" for x in d["steps"])
    faqs = "\n".join(
        f'  - question: {yaml_str(f["question"])}\n    answer: {yaml_str(f["answer"])}'
        for f in d["faq"]
    )
    grej = ""
    if d.get("relatedGrej"):
        grej_lines = "\n".join(f"  - {yaml_str(g)}" for g in d["relatedGrej"])
        grej = f"relatedGrej:\n{grej_lines}\n"
    slug = d["slug"]
    return f"""---
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
{grej}image: /recipes/{cat}/{slug}.jpg
imageAlt: {yaml_str(d["imageAlt"])}
publishedAt: {PUBLISHED}
ingredients:
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


def main() -> None:
    assert len(RECIPES) == 5, f"expected 5 recipes, got {len(RECIPES)}"
    slugs = [r["slug"] for r in RECIPES]
    assert len(slugs) == len(set(slugs)), "duplicate slugs"

    written = []
    for d in RECIPES:
        assert len(d["faq"]) >= 3, d["slug"]
        assert d.get("tip")
        cat = d["cat"]
        out = ROOT / cat
        out.mkdir(parents=True, exist_ok=True)
        (PUBLIC / cat).mkdir(parents=True, exist_ok=True)
        path = out / f"{d['slug']}.mdx"
        if path.exists():
            raise SystemExit(f"slug collision: {path}")
        path.write_text(to_mdx(d), encoding="utf-8")
        written.append(f"{cat}/{d['slug']}")
        print("wrote", f"{cat}/{path.name}")

    print(f"done: {len(written)} recipes")


if __name__ == "__main__":
    main()
