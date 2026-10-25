#!/usr/bin/env python3
"""Write 20 additional protein-focused recipes (batch 3)."""
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
        "title": "Airfryer kyllingespyd med pesto",
        "slug": "airfryer-kyllingespyd-pesto",
        "category": "airfryer",
        "description": "Saftige kyllingespyd i airfryer med grøn pesto — hurtigt protein til madpakke eller aftensmad på 20 minutter.",
        "prepTime": "PT10M",
        "cookTime": "PT12M",
        "totalTime": "PT22M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "airfryer", "pesto", "spyd", "meal prep"],
        "imageAlt": "Airfryer-kyllingespyd med grøn pesto og citron",
        "ingredients": [
            "600 g kyllingebryst i tern",
            "3 spsk grøn pesto",
            "1 spsk olivenolie",
            "1 tsk salt",
            "Peber",
            "1 citron",
            "Træ- eller metalspyd",
        ],
        "steps": [
            "Vend kylling med pesto, olie, salt og peber. Træk på spyd.",
            "Airfryer 180 °C i 10–12 minutter. Vend halvvejs. Kernetemperatur ca. 74 °C.",
            "Dryp citron over. Server med salat eller couscous.",
        ],
        "faq": [
            {
                "question": "Træspyd i airfryer?",
                "answer": "Ja — klip dem til, så de passer i kurven. Læg dem i vand 10 minutter hvis de er tynde.",
            },
            {
                "question": "Uden spyd?",
                "answer": "Steg ternene løst i kurven 10–12 minutter. Vend midtvejs.",
            },
            {
                "question": "Meal prep?",
                "answer": "Ja. Køl. Spis kolde eller varm 160 °C i 5 minutter.",
            },
        ],
        "body": """Pesto er marinade og sauce i ét. Airfryeren giver kyllingen kanter uden grill.

Salt let — pesto er allerede saltet.""",
        "tip": "Lad lidt pesto være til at pensle på efter stegning — frisk grøn smag ovenpå den bagte.",
    },
    {
        "title": "Airfryer torsk med citron og kapers",
        "slug": "airfryer-torsk-citron-kapers",
        "category": "airfryer",
        "description": "Saftig airfryer-torsk med citron, kapers og smør — let proteinmiddag klar på 15 minutter.",
        "prepTime": "PT5M",
        "cookTime": "PT12M",
        "totalTime": "PT17M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "torsk", "fisk", "airfryer", "citron", "kapers"],
        "imageAlt": "Airfryer-torsk med citronskiver og kapers",
        "ingredients": [
            "4 torskefileter (ca. 150 g)",
            "1 spsk olivenolie",
            "1½ tsk salt",
            "Peber",
            "1 citron i skiver",
            "2 spsk kapers",
            "1 spsk smør",
            "Frisk dild eller persille",
        ],
        "steps": [
            "Tør fisken. Olie, salt og peber. Læg citronskiver ovenpå.",
            "Airfryer 180 °C i 10–12 minutter til fisken er mat og flager.",
            "Smelt smør kort. Hæld over med kapers. Urter på toppen.",
        ],
        "faq": [
            {
                "question": "Frossen torsk?",
                "answer": "Tø helt op og tør godt. Ellers bliver den vandig.",
            },
            {
                "question": "Uden kapers?",
                "answer": "Oliven hakket fint eller ekstra citron. Kapers er syren.",
            },
            {
                "question": "Anden fisk?",
                "answer": "Sei eller kulmule. Samme tid.",
            },
        ],
        "body": """Torsk i airfryer er hverdagsprotein. Citron og kapers gør den skarp uden panering.

Tør fisken. Våd overflade = damp.""",
        "tip": "Kapers lige før servering — de bliver kedelige hvis de bager med hele vejen.",
    },
    {
        "title": "Airfryer æggebagt hytteost-fad",
        "slug": "airfryer-aeggebagt-hytteost",
        "category": "airfryer",
        "description": "Æggebagt hytteost-fad i airfryer — fluffy protein-morgenmad eller frokost på 15 minutter.",
        "prepTime": "PT5M",
        "cookTime": "PT12M",
        "totalTime": "PT17M",
        "servings": 2,
        "difficulty": "nem",
        "tags": ["protein", "hytteost", "æg", "airfryer", "morgenmad", "meal prep"],
        "imageAlt": "Luftigt æggebagt hytteost-fad fra airfryer med urter",
        "ingredients": [
            "250 g hytteost",
            "3 æg",
            "40 g reven ost",
            "½ tsk salt",
            "Peber",
            "½ tsk oregano eller chili",
            "Håndfuld spinat eller purløg",
            "Olie til formen",
        ],
        "steps": [
            "Rør hytteost, æg, ost, salt, peber og krydderi. Fold spinat/purløg i.",
            "Hæld i en olieret ovnfast form der passer i airfryeren.",
            "Airfryer 160 °C i 10–12 minutter til midten er sat.",
            "Hvile 2 minutter. Skær ud.",
        ],
        "faq": [
            {
                "question": "Metal- eller silikoneform?",
                "answer": "Begge. Silikone slipper lettere. Metal giver mere skorpe i kanterne.",
            },
            {
                "question": "For våd?",
                "answer": "Dræn hytteosten 5 minutter først, eller bag 2 minutter mere.",
            },
            {
                "question": "Meal prep?",
                "answer": "Ja. Køl i portioner. Varm 150 °C i 4 minutter.",
            },
        ],
        "body": """Hytteost + æg i airfryer er protein-soufflé uden besvær. Osten giver skorpe. Midten bliver fluffy.

Lav den i en form — ikke direkte i kurven.""",
        "tip": "Fyld kun til ¾. Æggene hæver, og overfyld drypper.",
    },
    {
        "title": "Pandestegt kyllingelever med løg",
        "slug": "pande-kyllingelever-loeg",
        "category": "pande",
        "description": "Klassisk pandestegt kyllingelever med bløde løg — jern- og proteinrig midtugeklassiker på 20 minutter.",
        "prepTime": "PT10M",
        "cookTime": "PT12M",
        "totalTime": "PT22M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "lever", "pande", "løg", "dansk-klassiker"],
        "imageAlt": "Pandestegt kyllingelever med karamelliserede løg",
        "ingredients": [
            "500 g kyllingelever",
            "2 store løg i både",
            "2 spsk smør",
            "1 spsk olie",
            "1½ tsk salt",
            "Peber",
            "1 tsk timian",
            "1 spsk balsamico eller æblecidereddike (valgfrit)",
        ],
        "steps": [
            "Rens lever for hinder. Tør af. Salt og peber.",
            "Svits løg i smør/olie på medium til bløde og gyldne (8 minutter). Tag af.",
            "Høj varme. Steg lever 2–3 minutter pr. side — stadig lidt rosa midt i. Løg tilbage. Timian. Evt. balsamico.",
            "Server med kartoffelmos eller rugbrød.",
        ],
        "faq": [
            {
                "question": "Bitter lever?",
                "answer": "Overstegning. Kort stegning på høj varme. Rosa midt er korrekt.",
            },
            {
                "question": "Udblødning i mælk?",
                "answer": "Valgfrit 20 minutter. Tør godt bagefter.",
            },
            {
                "question": "Okselever?",
                "answer": "Skær tyndere og steg endnu kortere.",
            },
        ],
        "body": """Kyllingelever er protein og jern til en slik. Løgene er søde. Leveren må ikke gennemsteges til skosål.

Høj varme. Kort tid. Færdig.""",
        "tip": "Steg lever i ét lag. Stablede stykker koger i stedet for at brune.",
    },
    {
        "title": "Pandestegt sej med sennep og spinat",
        "slug": "pande-sej-sennep-spinat",
        "category": "pande",
        "description": "Pandestegt sej med sennepsglasur og spinat — billigt hvidtfisk-protein på 15 minutter.",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "sej", "fisk", "pande", "sennep", "spinat"],
        "imageAlt": "Pandestegt sejfilet med sennep og wiltet spinat",
        "ingredients": [
            "4 sejfileter",
            "1 spsk olie",
            "1 spsk smør",
            "1½ tsk salt",
            "Peber",
            "2 spsk dijonsennep",
            "200 g babyspinat",
            "½ citron",
        ],
        "steps": [
            "Tør fisken. Salt og peber. Steg i olie/smør 3–4 minutter pr. side.",
            "Pensel sennep på sidste minut. Tag fisk af.",
            "Spinat i panden 30–60 sekunder. Citronsaft. Server under eller ved siden af fisken.",
        ],
        "faq": [
            {
                "question": "Sej vs. torsk?",
                "answer": "Sej er billigere og lidt fastere. Samme metode.",
            },
            {
                "question": "Falder fisken fra hinanden?",
                "answer": "Vend kun én gang med bred spatel. Tør fisken først.",
            },
            {
                "question": "Uden sennep?",
                "answer": "Smør og citron er nok. Sennep er ekstra bid.",
            },
        ],
        "body": """Sej er hverdagsfisk. Sennep giver den kant. Spinat er grønt uden ekstra gryde.

Tør. Steg. Pensel. Færdig.""",
        "tip": "Tag fisken af når den lige er mat midt i — den fortsætter på tallerkenen.",
    },
    {
        "title": "Protein-frittata med skinke",
        "slug": "protein-frittata-skinke",
        "category": "pande",
        "description": "Luftig protein-frittata med skinke og ost — panne-til-ovn på 25 minutter til brunch eller madpakke.",
        "prepTime": "PT10M",
        "cookTime": "PT18M",
        "totalTime": "PT28M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "æg", "skinke", "pande", "frittata", "morgenmad"],
        "imageAlt": "Gylden protein-frittata med skinke skåret i trekanter",
        "ingredients": [
            "8 æg",
            "100 g skinke i tern",
            "80 g reven ost",
            "1 dl mælk eller skyr",
            "1 spsk olie eller smør",
            "1 tsk salt",
            "Peber",
            "Frisk purløg",
            "Håndfuld spinat (valgfrit)",
        ],
        "steps": [
            "Varm ovn til 180 °C. Pisk æg med mælk/skyr, salt og peber.",
            "Svits skinke (og spinat) i ovnfast pande. Hæld æg over. Ost på toppen.",
            "Sæt panden i ovnen 12–15 minutter til midten er sat.",
            "Purløg. Skær i både. Spis varm eller kold.",
        ],
        "faq": [
            {
                "question": "Uden ovn?",
                "answer": "Låg på panden på medium-lav varme 10–12 minutter. Undersiden bliver mørkere.",
            },
            {
                "question": "Mere protein?",
                "answer": "Tilsæt 50 g hytteost i æggeblandingen.",
            },
            {
                "question": "Holdbarhed?",
                "answer": "3 dage i køl. God madpakke.",
            },
        ],
        "body": """Frittata er omelet der tåler at blive kold. Skinke og ost gør den til måltid.

Brug ovnfast pande — eller hæld over i et fad.""",
        "tip": "Ryst panden let efter 8 minutter. Hvis midten bølger meget, giv den 2–3 minutter mere.",
    },
    {
        "title": "Grill-kylling med mango-salsa",
        "slug": "grill-kylling-mango-salsa",
        "category": "grill",
        "description": "Grillet kyllingebryst med frisk mango-salsa — sommerprotein med sødme, syre og chili.",
        "prepTime": "PT15M",
        "cookTime": "PT14M",
        "totalTime": "PT29M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "grill", "mango", "salsa", "sommer"],
        "imageAlt": "Grillet kyllingebryst med farverig mango-salsa",
        "ingredients": [
            "4 kyllingebryster",
            "2 spsk olie",
            "1½ tsk salt",
            "1 tsk spidskommen",
            "1 tsk paprika",
            "1 moden mango i tern",
            "½ rødløg, finthakket",
            "1 lime (saft)",
            "Frisk koriander",
            "½ frisk chili (valgfrit)",
        ],
        "steps": [
            "Gnid kylling med olie, salt, spidskommen og paprika.",
            "Grill 6–7 minutter pr. side til 74 °C. Hvile 5 minutter.",
            "Rør mango, løg, lime, koriander, chili og pinch salt.",
            "Server kylling med salsa ovenpå.",
        ],
        "faq": [
            {
                "question": "Umoden mango?",
                "answer": "Vælg en der giver efter for tryk. Umoden salsa bliver sur og træagtig.",
            },
            {
                "question": "Uden grill?",
                "answer": "Grillpande eller ovn 200 °C i 18–20 minutter.",
            },
            {
                "question": "Meal prep?",
                "answer": "Kylling ja. Salsa frisk samme dag — mangoen bliver grødet overnight.",
            },
        ],
        "body": """Mango-salsa er dessert der tror den er salat. Kyllingen er proteinet. Sammen er det grill uden ketchup.

Salt kyllingen ordentligt. Salsaen er sød.""",
        "tip": "Bank brysterne til jævn tykkelse, så de ikke brænder i den tynde ende.",
    },
    {
        "title": "Grillede laksespyd med ingefær",
        "slug": "grillede-laksespyd-ingefaer",
        "category": "grill",
        "description": "Grillede laksespyd med ingefær og soja — lynhurtigt fisk-protein med asiatisk kant.",
        "prepTime": "PT15M",
        "cookTime": "PT8M",
        "totalTime": "PT23M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "laks", "grill", "spyd", "ingefær", "soja"],
        "imageAlt": "Grillede laksespyd med sesam og forårsløg",
        "ingredients": [
            "700 g laks i tern",
            "2 spsk sojasauce",
            "1 spsk olie",
            "1 spsk frisk ingefær, reven",
            "1 fed hvidløg",
            "1 tsk honning (valgfrit)",
            "Sesamfrø og forårsløg",
            "Spyd",
        ],
        "steps": [
            "Vend laks med soja, olie, ingefær, hvidløg og honning. Mariner 10–20 minutter.",
            "Træk på spyd. Grill på medium-høj 3–4 minutter pr. side.",
            "Sesam og forårsløg. Server med agurkesalat.",
        ],
        "faq": [
            {
                "question": "Falder fisken af?",
                "answer": "Brug faste tern (3 cm) og dobbeltspyd. Olie risten.",
            },
            {
                "question": "For salt soja?",
                "answer": "Mild soja, eller 1 spsk vand i marinaden.",
            },
            {
                "question": "Plancha?",
                "answer": "Ja — høj varme, samme tid. Vend forsigtigt.",
            },
        ],
        "body": """Laksespyd er grillens hurtigste fisk. Ingefær og soja er marinaden — ikke en dunk sauce.

Kort marinade. Kort grill. Ellers tørrer den.""",
        "tip": "Lad skindet sidde på nogle tern hvis du vil — det holder dem bedre sammen på risten.",
    },
    {
        "title": "Protein-kyllingepai med hytteost",
        "slug": "protein-kyllingepai-hytteost",
        "category": "ovn",
        "description": "Fyldig kyllingepai med hytteost — mere protein, mindre fløde, stadig boblende ovncomfort.",
        "prepTime": "PT20M",
        "cookTime": "PT30M",
        "totalTime": "PT50M",
        "servings": 6,
        "difficulty": "mellem",
        "tags": ["protein", "kylling", "hytteost", "ovn", "pai", "meal prep"],
        "imageAlt": "Bagt protein-kyllingepai med gylden skorpe",
        "ingredients": [
            "400 g kogt/stegt kylling, hakket",
            "250 g hytteost",
            "1 dl creme fraiche eller skyr",
            "1 æg",
            "1 porre eller 1 løg",
            "100 g ærter (frosne)",
            "1 tsk salt",
            "Peber",
            "1 tsk estragon eller timian",
            "1 rullet butterdej eller tærtedej",
            "1 æg til pensling",
        ],
        "steps": [
            "Varm ovn til 190 °C. Svits porre/løg. Rør med kylling, hytteost, creme fraiche, æg, ærter, salt, peber og urter.",
            "Læg dej i form. Fyld. Låg af dej eller gitter. Pensel æg.",
            "Bag 25–30 minutter til gylden. Hvile 10 minutter før skæring.",
        ],
        "faq": [
            {
                "question": "Uden butterdej?",
                "answer": "Bag fyldet i et fad med ost ovenpå — mere protein, mindre krumme.",
            },
            {
                "question": "For våd fyld?",
                "answer": "Dræn hytteost. Brug stegt kylling, ikke kogt i meget væske.",
            },
            {
                "question": "Fryses?",
                "answer": "Ja, bagt. Optø og varm 160 °C i 20 minutter.",
            },
        ],
        "body": """Kyllingepai er comfort. Hytteost erstatter en del af fløden og skubber proteintallet.

Hvile før skæring — ellers løber den.""",
        "tip": "Stik et par huller i låget, så dampen slipper ud og skorpen bliver sprød.",
    },
    {
        "title": "Bagt kyllingelår med rodfrugter",
        "slug": "bagt-kyllingelaar-rodfrugter",
        "category": "ovn",
        "description": "Ovnstegte kyllingelår med rodfrugter på én plade — saftigt protein og grønt uden ekstra opvask.",
        "prepTime": "PT15M",
        "cookTime": "PT40M",
        "totalTime": "PT55M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "ovn", "rodfrugter", "meal prep", "fad"],
        "imageAlt": "Ovnstegte kyllingelår med gulerødder og pastinak",
        "ingredients": [
            "8 kyllingelår med skind",
            "400 g gulerødder",
            "300 g pastinak eller kartofler",
            "1 rødløg",
            "2 spsk olivenolie",
            "2 tsk salt",
            "1 tsk rosmarin eller timian",
            "Peber",
            "1 citron",
        ],
        "steps": [
            "Varm ovn til 200 °C. Skær rodfrugter i grove stykker. Vend med olie, salt, urter og peber på plade.",
            "Læg lår ovenpå. Salt skindet. Bag 35–40 minutter til skindet er sprødt og kødet 75 °C.",
            "Dryp citron over. Server fra pladen.",
        ],
        "faq": [
            {
                "question": "Bløde rodfrugter?",
                "answer": "Skær dem ikke for små, og giv dem evt. 10 minutter forskud før kyllingen.",
            },
            {
                "question": "Bryst i stedet?",
                "answer": "Kortere tid — 25–30 minutter. Skindet på lår er mere tilgivende.",
            },
            {
                "question": "Meal prep?",
                "answer": "Ja. 4 bokse. Holder 3–4 dage.",
            },
        ],
        "body": """Én plade. Kyllingelår. Rodfrugter. Fedtet fra skindet smager grøntsagerne til.

Salt skindet ekstra. Det er skorpen.""",
        "tip": "Plads mellem lårene. Pressede lår damper i stedet for at sprøde.",
    },
    {
        "title": "Protein-quiche med spinat og laks",
        "slug": "protein-quiche-spinat-laks",
        "category": "ovn",
        "description": "Quiche med spinat, røget laks og æg — proteinrig tærte til brunch, picnic og madpakke.",
        "prepTime": "PT15M",
        "cookTime": "PT35M",
        "totalTime": "PT50M",
        "servings": 6,
        "difficulty": "mellem",
        "tags": ["protein", "æg", "laks", "spinat", "ovn", "quiche", "brunch"],
        "imageAlt": "Bagt protein-quiche med spinat og røget laks",
        "ingredients": [
            "1 tærtedej (eller butterdej)",
            "5 æg",
            "150 g hytteost eller 1½ dl creme fraiche",
            "100 g røget laks i strimler",
            "150 g spinat",
            "50 g reven ost",
            "½ tsk salt",
            "Peber",
            "Dild",
        ],
        "steps": [
            "Varm ovn til 180 °C. Læg dej i form. Forbag 8 minutter hvis den er tyk.",
            "Svits spinat til den falder sammen. Pres væske ud.",
            "Pisk æg med hytteost/creme fraiche, salt og peber. Fordel spinat, laks og ost i formen. Hæld æg over. Dild.",
            "Bag 25–30 minutter til midten er sat. Køl 10 minutter.",
        ],
        "faq": [
            {
                "question": "Uden dej?",
                "answer": "Bag i olieret form — crustless quiche. Mere protein pr. skive.",
            },
            {
                "question": "Frisk laks?",
                "answer": "Steg den kort først, eller brug rester. Røget er nemmest.",
            },
            {
                "question": "Holdbarhed?",
                "answer": "3 dage i køl. God kold.",
            },
        ],
        "body": """Quiche er æg i festtøj. Spinat og laks gør den til protein — ikke bare tærte.

Pres spinaten. Ellers bliver midten vandet.""",
        "tip": "Stik en kniv i midten — den skal komme op næsten ren. Lidt fugt er ok; den sætter sig under hvilen.",
    },
    {
        "title": "Protein-chili med kylling og bønner",
        "slug": "protein-chili-kylling-boenner",
        "category": "gryde",
        "description": "Chili med hakket kylling og bønner — højprotein gryderet til meal prep uden oksekød.",
        "prepTime": "PT10M",
        "cookTime": "PT25M",
        "totalTime": "PT35M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "bønner", "gryde", "chili", "meal prep"],
        "imageAlt": "Chili med kylling og bønner i skål med yoghurt",
        "ingredients": [
            "500 g hakket kylling",
            "1 dåse kidneybønner eller sorte bønner",
            "1 løg",
            "2 fed hvidløg",
            "1 peberfrugt",
            "1 dåse hakkede tomater",
            "1 spsk olie",
            "1 spsk chilipulver eller taco-krydderi",
            "1 tsk spidskommen",
            "1 tsk salt",
            "Skyr eller hytteost til topping",
        ],
        "steps": [
            "Brun kylling og løg i olie. Hvidløg og peberfrugt i.",
            "Krydderier 30 sekunder. Tomater og drænede bønner. Simre 15–20 minutter.",
            "Smag salt. Server med skyr/hytteost og evt. ris.",
        ],
        "faq": [
            {
                "question": "For mild?",
                "answer": "Ekstra chili, frisk jalapeño eller røget paprika.",
            },
            {
                "question": "Uden bønner?",
                "answer": "Mere kylling — eller linser. Bønnerne er ekstra planteprotein.",
            },
            {
                "question": "Fryses?",
                "answer": "Ja. Perfekt meal prep.",
            },
        ],
        "body": """Chili behøver ikke oksekød. Hakket kylling + bønner er protein-stabling med mindre fedt.

Krydderierne skal møde olien før tomaterne.""",
        "tip": "Top med hytteost i stedet for creme fraiche — endnu et proteinlag.",
    },
    {
        "title": "Kylling-gulasch med paprika",
        "slug": "kylling-gulasch-paprika",
        "category": "gryde",
        "description": "Ungarsk-inspireret kylling-gulasch med ægte paprika — cremet protein-gryde uden tung fløde.",
        "prepTime": "PT15M",
        "cookTime": "PT30M",
        "totalTime": "PT45M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "gryde", "gulasch", "paprika", "ungarsk"],
        "imageAlt": "Rød kylling-gulasch med paprika i gryde",
        "ingredients": [
            "700 g kyllingelår uden ben i stykker (eller bryst)",
            "2 løg",
            "2 spsk olie",
            "2 spsk ægte paprika",
            "1 peberfrugt",
            "1 dåse hakkede tomater",
            "3 dl bouillon",
            "1½ tsk salt",
            "Peber",
            "1 dl skyr til sidst (valgfrit)",
            "Persille",
        ],
        "steps": [
            "Brun kylling i olie. Tag af. Svits løg og peberfrugt.",
            "Paprika 20 sekunder. Tomater og bouillon. Kylling tilbage. Salt.",
            "Simre 25–30 minutter til kødet er mørt. Evt. skyr af blusset.",
            "Persille. Server med ris eller kartoffel.",
        ],
        "faq": [
            {
                "question": "Brændt paprika?",
                "answer": "For høj varme. Paprika skal dufte — ikke ryge.",
            },
            {
                "question": "Oksekød?",
                "answer": "Klassisk — men så 1½ time simre. Kylling er hverdagsversionen.",
            },
            {
                "question": "Meal prep?",
                "answer": "Ja. Smager bedre dagen efter.",
            },
        ],
        "body": """Gulasch er paprika i dybden. Kylling gør den hurtigere end okse. Skyr til sidst er protein-finish.

Løg først. Paprika midt i. Væske til sidst.""",
        "tip": "Brug sød ungarsk paprika — ikke kun røget. Røget alene bliver bitter i store mængder.",
    },
    {
        "title": "Støbejerns-laks med hvidløgssmør",
        "slug": "stobejern-laks-hvidloegssmoer",
        "category": "stobejern",
        "description": "Sprødskindet laks i støbejern med hvidløgssmør — restaurant-protein på 12 minutter.",
        "prepTime": "PT5M",
        "cookTime": "PT8M",
        "totalTime": "PT13M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "laks", "støbejern", "hvidløg", "smør", "fisk"],
        "imageAlt": "Støbejerns-laks med hvidløgssmør og citron",
        "ingredients": [
            "4 lakseskiver med skind",
            "1 spsk olie",
            "1½ tsk salt",
            "Peber",
            "2 spsk smør",
            "2 fed hvidløg, knuste",
            "½ citron",
            "Frisk dild eller persille",
        ],
        "steps": [
            "Tør laksen. Salt skindsiden. Varm støbejern til meget varmt med olie.",
            "Læg skindsiden ned. Pres let 20 sekunder. Steg 4–5 minutter uden at vippe.",
            "Vend. Smør og hvidløg i panden. Øs over fisken 1–2 minutter.",
            "Citron og urter. Server.",
        ],
        "faq": [
            {
                "question": "Klæber skindet?",
                "answer": "Panden var ikke hot nok, eller fisken var våd. Vent til den slipper selv.",
            },
            {
                "question": "Uden smør?",
                "answer": "Olivenolie og hvidløg. Smør er bare ekstra smag.",
            },
            {
                "question": "Rosa midt?",
                "answer": "Ja. Mat helt igennem = tør laks.",
            },
        ],
        "body": """Støbejern + laks = sprødt skind. Hvidløgssmør er saucen der laver sig selv i panden.

Pres kort. Vip sent.""",
        "tip": "Tag hvidløget ud hvis det bruner for hurtigt — brændt hvidløg ødelægger smørret.",
    },
    {
        "title": "Plancha-kalkun med peberfrugt",
        "slug": "plancha-kalkun-peberfrugt",
        "category": "plancha",
        "description": "Lynstegt plancha-kalkun med peberfrugt — magert fajita-protein med svedne grøntsager.",
        "prepTime": "PT12M",
        "cookTime": "PT10M",
        "totalTime": "PT22M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "kalkun", "plancha", "peberfrugt", "fajita", "sund"],
        "imageAlt": "Plancha med kalkunstrimler og farverig peberfrugt",
        "ingredients": [
            "600 g kalkunfilet i strimler",
            "2 peberfrugter",
            "1 rødløg",
            "2 spsk olie",
            "1½ tsk salt",
            "1 tsk røget paprika",
            "1 tsk oregano",
            "Peber",
            "1 lime",
            "Koriander",
        ],
        "steps": [
            "Vend kalkun med 1 spsk olie, salt, paprika, oregano og peber.",
            "Varm plancha høj. Steg kalkun 4–5 minutter. Skub til siden.",
            "Peberfrugt og løg 3–4 minutter. Bland. Lime og koriander.",
            "Server i tortillas, på salat eller med ris.",
        ],
        "faq": [
            {
                "question": "Tør kalkun?",
                "answer": "Høj varme, kort tid, og olie i marinaden. Oversteg ikke.",
            },
            {
                "question": "Kylling i stedet?",
                "answer": "Ja, 1:1.",
            },
            {
                "question": "Uden plancha?",
                "answer": "Stor pande eller wok. Samme metode.",
            },
        ],
        "body": """Kalkun på plancha er fajita uden kyllinge-autopilot. Peberfrugt skal svedes.

Høj varme. Tynde strimler. Færdig før du tror.""",
        "tip": "Tør kalkunen før krydderi — ellers får du damp i stedet for stegeskorpe.",
    },
    {
        "title": "Sous vide culotte til protein-skiver",
        "slug": "sous-vide-culotte-protein",
        "category": "sous-vide",
        "description": "Sous vide-culotte skåret til protein-skiver — meal prep-oksekød der er rosa og saftigt hele ugen.",
        "prepTime": "PT10M",
        "cookTime": "PT150M",
        "totalTime": "PT160M",
        "servings": 6,
        "difficulty": "mellem",
        "tags": ["protein", "oksekød", "culotte", "sous-vide", "meal prep"],
        "imageAlt": "Skåret sous vide-culotte i tynde protein-skiver",
        "ingredients": [
            "1 culotte (ca. 1–1,2 kg)",
            "2 tsk salt",
            "Peber",
            "2 fed hvidløg",
            "Frisk rosmarin eller timian",
            "1 spsk olie til finish",
        ],
        "steps": [
            "Sæt sous vide til 55 °C (rosa) eller 58 °C (medium).",
            "Salt culotten. Pose med peber, hvidløg og urter. Sous vide 2½–3 timer.",
            "Tag op. Tør godt. Lynsteg fedtsiden i varm pande med olie til skorpe.",
            "Hvile 5 minutter. Skær tynde skiver på tværs af fibrene. Køl til madpakke eller spis varm.",
        ],
        "faq": [
            {
                "question": "Kan den genopvarmes?",
                "answer": "Ja — kort i pande eller spis kold. Undgå micro på fuld effekt; den bliver grå.",
            },
            {
                "question": "Uden sous vide?",
                "answer": "Ovnsteg lavt (120 °C) til samme kernetemperatur, hvil, steg skorpe.",
            },
            {
                "question": "Holdbarhed?",
                "answer": "3–4 dage i køl, skåret i portioner.",
            },
        ],
        "body": """Culotte sous vide er meal prep-bøf. Skær tyndt. Brug på salat, i wraps eller med æg.

Tør før panden. Skorpen er det hele.""",
        "tip": "Skær først når den har hvilet — saften skal sætte sig i kødet.",
    },
    {
        "title": "Trykkoger kylling taco-fyld",
        "slug": "trykkoger-kylling-taco-fyld",
        "category": "trykkoger",
        "description": "Shredded kylling taco-fyld i trykkoger — saftigt protein til tacos, bowls og madpakke på 25 minutter.",
        "prepTime": "PT10M",
        "cookTime": "PT20M",
        "totalTime": "PT30M",
        "servings": 6,
        "difficulty": "nem",
        "tags": ["protein", "kylling", "trykkoger", "taco", "meal prep", "mexicansk"],
        "imageAlt": "Shredded kylling taco-fyld med lime og koriander",
        "ingredients": [
            "800 g kyllingebryst",
            "1 dl salsa eller hakkede tomater",
            "1 dl bouillon",
            "1 spsk taco-krydderi",
            "1 tsk salt",
            "1 tsk spidskommen",
            "1 fed hvidløg",
            "Lime og koriander til servering",
        ],
        "steps": [
            "Læg kylling i trykkoger med salsa, bouillon, krydderier, salt og hvidløg.",
            "Højt tryk 10–12 minutter. Hurtig aflastning.",
            "Tag kylling op. Træk fra hinanden med to gafler. Rør tilbage i saucen.",
            "Lime og koriander. Server i tortillas, på ris eller i bowl.",
        ],
        "faq": [
            {
                "question": "For tørt?",
                "answer": "Mere sauce i gryden, eller bland et skvæt af kogevæsken i det pullede kød.",
            },
            {
                "question": "Uden trykkoger?",
                "answer": "Ovnen 160 °C i 45–60 minutter tildækket, eller gryde 30–40 minutter.",
            },
            {
                "question": "Fryses?",
                "answer": "Ja — ideelt meal prep. Portionér med sauce.",
            },
        ],
        "body": """Taco-fyld er protein til hele ugen. Trykkogeren gør brystet shreddable uden at det bliver tørt.

Træk kødet. Rør det i saucen. Ikke omvendt.""",
        "tip": "Gem ½ dl kogevæske inden du reducerer — den redder fyldet hvis det tørrer i køleskabet.",
    },
    {
        "title": "Protein-guacamole med hytteost",
        "slug": "protein-guacamole-hytteost",
        "category": "dips",
        "description": "Guacamole boostet med hytteost — cremet avocado-dip med ekstra protein til chips og kylling.",
        "prepTime": "PT10M",
        "cookTime": "PT0M",
        "totalTime": "PT10M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "guacamole", "hytteost", "dips", "avocado", "snack"],
        "imageAlt": "Protein-guacamole med hytteost, lime og koriander",
        "ingredients": [
            "2 modne avocadoer",
            "100 g hytteost",
            "1 lime (saft)",
            "½ rødløg, finthakket",
            "1 tomat, hakket (valgfrit)",
            "Frisk koriander",
            "½ tsk salt",
            "Peber",
            "Chiliflager (valgfrit)",
        ],
        "steps": [
            "Mos avocado. Rør hytteost i (moset eller blendet).",
            "Lime, salt, peber, løg, tomat og koriander. Smag til.",
            "Server med grøntsagsstænger, tortillachips eller som topping på kylling.",
        ],
        "faq": [
            {
                "question": "Smager man hytteosten?",
                "answer": "Lidt — lime og løg dækker. Blend hytteosten først for mildere resultat.",
            },
            {
                "question": "Bruner den?",
                "answer": "Pres film direkte på overfladen. Lime hjælper. Spis samme dag.",
            },
            {
                "question": "Uden tomat?",
                "answer": "Ja. Ren avocado-hytteost er fin.",
            },
        ],
        "body": """Guacamole er fedt. Hytteost er protein. Sammen er det dip der faktisk mætter.

Mos — blend ikke avocadoen til smoothie.""",
        "tip": "Gem avocado-stenen i skålen under film — det forsinker bruningen en smule.",
    },
    {
        "title": "Protein-røget laks med hytteostcreme",
        "slug": "protein-roegtlaks-hytteostcreme",
        "category": "palaeg",
        "description": "Røget laks på hytteostcreme — hurtigt protein-pålæg til rugbrød, toast og knækbrød.",
        "prepTime": "PT8M",
        "cookTime": "PT0M",
        "totalTime": "PT8M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["protein", "laks", "hytteost", "pålæg", "røget laks", "madpakke"],
        "imageAlt": "Rugbrød med hytteostcreme og røget laks med dild",
        "ingredients": [
            "200 g røget laks",
            "200 g hytteost",
            "1 spsk skyr eller yoghurt",
            "1 tsk dijonsennep",
            "½ citron (saft)",
            "Frisk dild",
            "Peber",
            "Kapers (valgfrit)",
            "Rugbrød til servering",
        ],
        "steps": [
            "Mos eller blend hytteost med skyr, sennep, citron, peber og halvdelen af dilden.",
            "Smør cremen på brød. Læg laks ovenpå.",
            "Dild og kapers. Server med det samme.",
        ],
        "faq": [
            {
                "question": "Kornede creme?",
                "answer": "Blend hytteosten 20 sekunder. Den bliver silk.",
            },
            {
                "question": "Madpakke?",
                "answer": "Creme og laks separat. Saml ved frokost — ellers bliver brødet vådt.",
            },
            {
                "question": "Uden røget laks?",
                "answer": "Rejer eller kogt kylling på samme creme.",
            },
        ],
        "body": """Røget laks er protein. Hytteostcreme er mere protein. Rugbrød er bare køretøjet.

Citron i cremen — ikke kun ovenpå.""",
        "tip": "Dræn hytteosten kort hvis den er meget våd, så cremen ikke løber af brødet.",
    },
    {
        "title": "Protein-smoothie med spinat og skyr",
        "slug": "protein-smoothie-spinat-skyr",
        "category": "roeremaskine",
        "description": "Grøn protein-smoothie med spinat, skyr og bær — morgenmad eller post-workout på 5 minutter.",
        "prepTime": "PT5M",
        "cookTime": "PT0M",
        "totalTime": "PT5M",
        "servings": 1,
        "difficulty": "nem",
        "tags": ["protein", "smoothie", "skyr", "spinat", "morgenmad", "roeremaskine"],
        "imageAlt": "Grøn protein-smoothie med skyr og spinat i glas",
        "ingredients": [
            "200 g skyr",
            "1 håndfuld babyspinat",
            "100 g frosne bær",
            "1 scoop proteinpulver (valgfrit)",
            "1–1½ dl mælk eller plantedrik",
            "½ banan (valgfrit)",
            "Pinch salt",
        ],
        "steps": [
            "Kom alt i blender eller røremaskine.",
            "Blend til helt glat og grøn.",
            "Smag. Tilsæt væske hvis den er for tyk. Hæld i glas.",
        ],
        "faq": [
            {
                "question": "Smager man spinat?",
                "answer": "Næsten ikke når bærrene er med. Start med en lille håndfuld.",
            },
            {
                "question": "Uden pulver?",
                "answer": "Skyr alene er stadig proteinrigt.",
            },
            {
                "question": "For tyk?",
                "answer": "Mere mælk. Frosne bær gør den milkshake-agtig.",
            },
        ],
        "body": """Spinat i smoothien er grønt uden salatskål. Skyr er proteinbasen. Bær er smagen.

Blend længe — ellers får du bladstykker.""",
        "tip": "Pinch salt løfter bærrene. Det smager ikke salt — det smager mere af frugt.",
    },
]


def main() -> None:
    for r in RECIPES:
        write_recipe(r)
    print(f"Wrote {len(RECIPES)} recipes")


if __name__ == "__main__":
    main()
