#!/usr/bin/env python3
"""6 airfryer-opskrifter batch 41–50 (skip overlap 44, 46, 48, 50) — nov 2026."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes/airfryer"
PUBLISHED = "2026-11-19"

RECIPES = [
    {
        "title": "Crispy Rice Paper Dumplings i airfryer",
        "slug": "crispy-rispapir-dumplings",
        "description": "Crispy Rice Paper Dumplings i airfryer — kyllinge- eller svinefars med forårsløg og ingefær i dobbelt rispapir, sprøde som gyldne puder.",
        "prepTime": "PT20M",
        "cookTime": "PT12M",
        "totalTime": "PT32M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": ["rispapir", "dumplings", "kylling", "snack", "party", "viral", "airfryer"],
        "imageAlt": "Gyldne crispy rice paper dumplings fra airfryeren med dip",
        "ingredients": [
            "400 g kyllinge- eller svinefars",
            "3 forårsløg, fint hakket",
            "1 spsk frisk ingefær, revet",
            "2 fed hvidløg, presset",
            "1 spsk sojasauce",
            "1 tsk sesamolie",
            "12–16 ark rispapir (22 cm)",
            "Olie-spray",
            "Dip: sojasauce, riseddike, chiliolie",
        ],
        "steps": [
            "Rør fars, forårsløg, ingefær, hvidløg, soja og sesamolie. Del i 12–16 portioner.",
            "Dyp ét rispapir 2–3 sekunder i lunkent vand. Læg 1 spsk fyld midt i. Fold til en stram pude. Pak endnu et vådt ark udenom — dobbelt lag giver bobler og knas.",
            "Spray let med olie. Airfry 190 °C i 10–12 minutter. Vend halvvejs, til begge sider er gyldne og sprøde.",
            "Server straks med dip. De bliver blødere, hvis de står.",
        ],
        "faq": [
            {
                "question": "Forskel på sushi-ruller og gyoza?",
                "answer": "Her er foldede puder i dobbelt rispapir — ikke ruller og ikke dej-gyoza. Samme snack-energi, anden form.",
            },
            {
                "question": "Rispapiret klæber sammen?",
                "answer": "For vådt eller for tæt i kurven. Dup let, spray olie, giv luft mellem dumplings.",
            },
            {
                "question": "Vegetarisk fyld?",
                "answer": "Finthakket champignon, kål og tofu med samme krydderi. Pres væske ud først.",
            },
            {
                "question": "Kan de laves forud?",
                "answer": "Pak og stil køligt op til 2 timer. Airfry lige før servering — ikke genopvarm.",
            },
        ],
        "body": """Crispy rice paper dumplings er den virale pude: dobbelt rispapir, vådt nok til at folde, tørt nok til at boble i blæsten.

  Fars indenfor. Gylden skorpe udenpå. Dip ved siden af.""",
        "tip": "To lag er non-negotiable. Ét lag bliver sej; to lag giver de karakteristiske bobler.",
    },
    {
        "title": "Pistacie-paneret laks i airfryer",
        "slug": "pistacie-paneret-laks",
        "description": "Pistacie-paneret laks i airfryer — filet smurt med dijon og honning, toppet med knuste pistacier, panko og citronskal.",
        "prepTime": "PT10M",
        "cookTime": "PT12M",
        "totalTime": "PT22M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["laks", "pistacie", "fisk", "hurtig", "middag", "airfryer"],
        "imageAlt": "Laksefilet med pistacie- og panko-skorpe fra airfryeren",
        "ingredients": [
            "4 laksefileter (á ca. 150 g), skindfri",
            "1 spsk dijonsennep",
            "1 spsk honning",
            "60 g usaltede pistacienødder, groft knust",
            "40 g panko",
            "Skal af 1 citron",
            "1 spsk olivenolie",
            "Salt og peber",
            "Citronsaft og frisk dild til servering",
        ],
        "steps": [
            "Dup laksen tør. Salt og peber. Smør toppen med dijon blandet med honning.",
            "Bland pistacier, panko, citronskal og olie. Press skorpen fast på laksen.",
            "Airfry 180 °C i 10–12 minutter, til skorpen er gylden og kernen stadig saftig (ca. 50–52 °C for medium).",
            "Citronsaft og dild over. Server med det samme.",
        ],
        "faq": [
            {
                "question": "Med skind?",
                "answer": "Ja — læg skindsiden ned, skorpen op. Skindet bliver sprødt i bunden.",
            },
            {
                "question": "Nøddeallergi?",
                "answer": "Erstat pistacier med ekstra panko + sesamfrø. Samme teknik.",
            },
            {
                "question": "Forskel på miso-laks?",
                "answer": "Her er dijon-honning og nødde-panko. Miso-sesam er en anden glaze — begge er fine, men det er ikke samme opskrift.",
            },
            {
                "question": "For tør?",
                "answer": "For lang tid eller for tynde fileter. Tjek efter 9–10 minutter.",
            },
        ],
        "body": """Pistacie-paneret laks er restaurant-look på hverdagsminutter: dijon klæber skorpen, honning giver karamel, pistacier giver knas.

  Grøn skorpe. Rosa midte. Citron til sidst.""",
        "tip": "Knus pistacier groft — ikke mel. Store stykker holder knaset, når pankoen brunner.",
    },
    {
        "title": "Hot Honey Halloumi Fries i airfryer",
        "slug": "hot-honey-halloumi-fries",
        "description": "Hot Honey Halloumi Fries i airfryer — panerede halloumi-stave med chili-honning, granatæblekerner og mynteyoghurt.",
        "prepTime": "PT15M",
        "cookTime": "PT12M",
        "totalTime": "PT27M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["halloumi", "hot honey", "snack", "party", "vegetar", "airfryer"],
        "imageAlt": "Sprøde halloumi fries med hot honey, granatæble og mynteyoghurt",
        "ingredients": [
            "400 g halloumi",
            "3 spsk hvedemel (eller majsstivelse)",
            "1 tsk røget paprika",
            "½ tsk chilipulver",
            "Olie-spray",
            "Hot honey: 3 spsk honning + ½–1 tsk chiliflager",
            "150 g græsk yoghurt",
            "1 spsk hakket mynte",
            "Granatæblekerner til topping",
        ],
        "steps": [
            "Skær halloumi i stave á ca. 1×1×6 cm. Dup tør. Vend i mel blandet med paprika og chilipulver.",
            "Spray med olie. Airfry 200 °C i 10–12 minutter. Vend halvvejs, til alle sider er gyldne.",
            "Varm honning med chiliflager 20 sekunder. Rør yoghurt med mynte og lidt salt.",
            "Anret fries, dryp hot honey over, top med granatæble og mynteyoghurt ved siden af.",
        ],
        "faq": [
            {
                "question": "Panko i stedet for mel?",
                "answer": "Ja — dip i æg først, så panko. Mere knas, lidt mere arbejde.",
            },
            {
                "question": "Halloumi bliver gummiagtig?",
                "answer": "For lav varme eller for våd ost. Dup tør, 200 °C, spis med det samme.",
            },
            {
                "question": "Forskel på paneret feta?",
                "answer": "Halloumi er stave, der holder formen. Feta smuldrer — anden snack, samme hot honey-energi.",
            },
            {
                "question": "Uden granatæble?",
                "answer": "Brug syltede rødløg eller finthakket agurk. Syre er pointen.",
            },
        ],
        "body": """Hot Honey Halloumi Fries er party-stave: saltost, chili-honning, kølig yoghurt og knasende granatæble.

  Sprød yderside. Blød midte. Spis dem varme.""",
        "tip": "Sal ikke halloumien — den er allerede salt. Lad hot honey og yoghurt balancere.",
    },
    {
        "title": "Scotch eggs i airfryer",
        "slug": "scotch-eggs-airfryer",
        "description": "Scotch eggs i airfryer — blødkogte æg pakket i krydret salsiccia eller medister og panko, sprøde uden frituregryde.",
        "prepTime": "PT25M",
        "cookTime": "PT16M",
        "totalTime": "PT41M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": ["scotch eggs", "æg", "salsiccia", "medister", "brunch", "airfryer"],
        "imageAlt": "Gennemskåret scotch egg med smilende blomme og panko-skorpe",
        "ingredients": [
            "5 æg (4 til pakning + 1 til panering)",
            "400 g salsiccia eller medister (uden skind)",
            "1 tsk dijonsennep",
            "½ tsk sort peber",
            "50 g hvedemel",
            "80 g panko",
            "Olie-spray",
            "Flagesalt",
            "Sennep eller aioli til servering",
        ],
        "steps": [
            "Kog 4 æg 6½ minut i kogende vand. Iskold vand 5 minutter. Skræl forsigtigt.",
            "Rør fars med dijon og peber. Del i 4. Flad hver portion, pak omkring et æg, og luk tæt uden luftlommer.",
            "Vend i mel, pisket æg og panko. Spray med olie.",
            "Airfry 180 °C i 14–16 minutter. Vend halvvejs, til skorpen er dybt gylden og farsen er gennemstegt. Flagesalt. Server med det samme.",
        ],
        "faq": [
            {
                "question": "Hård blomme?",
                "answer": "For lang æggekogning. 6–6½ minut giver smil; 8+ er hårdkogt.",
            },
            {
                "question": "Medister vs salsiccia?",
                "answer": "Begge virker. Salsiccia er mere krydret; medister er mildere og mere dansk.",
            },
            {
                "question": "Farsen åbner sig?",
                "answer": "For tyndt lag eller luftlommer. Press godt sammen, og hold æggene kølige, mens du pakker.",
            },
            {
                "question": "Kan de laves dagen før?",
                "answer": "Kog og pak, stil køligt. Panér og airfry lige før servering.",
            },
        ],
        "body": """Scotch eggs i airfryer er pub-klassikeren uden friture: blød blomme, krydret fars, panko der knaser.

  Smilende midte. Gylden skorpe. Sennep ved siden af.""",
        "tip": "Våde hænder, når du pakker farsen — den klæber mindre, og laget bliver jævnere.",
    },
    {
        "title": "Brunede kartofler i airfryer",
        "slug": "brunede-kartofler-airfryer",
        "description": "Brunede kartofler i airfryer — små glaskartofler vendt i smør og sukker i en bageform i kurven, blanke uden konstant røring.",
        "prepTime": "PT10M",
        "cookTime": "PT25M",
        "totalTime": "PT35M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["brunede kartofler", "kartofler", "jul", "vinter", "tilbehør", "airfryer"],
        "imageAlt": "Blanke brunede kartofler fra airfryeren i smør-sukker-glaze",
        "ingredients": [
            "800 g små kartofler (glaskartofler), kogte og afkølede",
            "40 g smør",
            "50 g sukker",
            "1 knivspids salt",
            "Evt. 1 spsk andefedt eller lidt ekstra smør",
        ],
        "steps": [
            "Tør de kogte kartofler godt. Læg dem i en airfryer-egnet metal- eller ovnfast form, der passer i kurven.",
            "Fordel smør og sukker over. Airfry 180 °C i 12 minutter.",
            "Ryst eller vend kartoflerne. Fortsæt 10–12 minutter, til sukkeret er karamelliseret og kartoflerne blanke og gyldne.",
            "Salt let. Server varme — klassisk til flæskesteg, and eller julebordet.",
        ],
        "faq": [
            {
                "question": "Forskel på gryde-versionen?",
                "answer": "Samme smør-sukker-glaze. Airfryeren sparer dig for at stå og røre — formen i kurven gør arbejdet.",
            },
            {
                "question": "Sukkeret brænder?",
                "answer": "For høj varme eller for tynd form. Hold 180 °C, og vend midtvejs.",
            },
            {
                "question": "Rå kartofler?",
                "answer": "Nej. De skal være kogte og tørre først — ellers koger de i stedet for at glasere.",
            },
            {
                "question": "Andefedt?",
                "answer": "Ja. En spsk andefedt med smørret giver mere jule-dybde.",
            },
        ],
        "body": """Brunede kartofler i airfryer er julebordets slik uden gryde-vagt: smør, sukker, blæst — blanke kartofler klar til and og flæskesteg.

  Karamel uden konstant røring. Form i kurven. Vend én gang.""",
        "tip": "Kartoflerne skal være tørre. Våd overflade = sukkeret opløses i stedet for at karamellisere.",
    },
    {
        "title": "Fyldte æbler med marcipan i airfryer",
        "slug": "fyldte-aebler-marcipan",
        "description": "Fyldte æbler med marcipan i airfryer — hele æbler udhulet med rå marcipan, brunet smør og hasselnødder, bagt møre med karamelliseret top.",
        "prepTime": "PT15M",
        "cookTime": "PT18M",
        "totalTime": "PT33M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["æble", "marcipan", "dessert", "jul", "vinter", "hasselnødder", "airfryer"],
        "imageAlt": "Fyldte æbler med marcipan, brunet smør og hasselnødder fra airfryeren",
        "ingredients": [
            "4 faste æbler (Ingrid Marie, Cox eller Granny Smith)",
            "100 g rå marcipan",
            "40 g smør",
            "30 g hasselnødder, groft hakket",
            "1 spsk farin",
            "½ tsk kanel",
            "1 knivspids stødt nellike",
            "Vaniljeis eller creme fraiche til servering",
        ],
        "steps": [
            "Skær toppen af æblerne, og udhul kernehuset med en ske — lad bunden sidde, så de er skåle. Brun smørret i en lille gryde, til det dufter nøddeagtigt.",
            "Smuldr marcipan med farin, kanel, nellike, halvdelen af hasselnødderne og halvdelen af det brunede smør. Fyld æblerne.",
            "Drys resten af nødderne på, og pensl med rest-smør. Airfry 170 °C i 15–18 minutter, til æblerne er møre, og toppen er gylden.",
            "Server lune med is eller creme fraiche.",
        ],
        "faq": [
            {
                "question": "Forskel på bagte æbler med havre?",
                "answer": "Her er fyldet marcipan og brunet smør — juleagtigt og blødt. Havre-crumble er en anden dessert.",
            },
            {
                "question": "Marcipanen brænder?",
                "answer": "For høj varme. 170 °C og evt. et stykke folie over de sidste minutter, hvis din airfryer er aggressiv.",
            },
            {
                "question": "Mandelmasse i stedet?",
                "answer": "Ja. Lidt sødere — smag til med mindre farin.",
            },
            {
                "question": "Kan de laves forud?",
                "answer": "Udhul og fyld, stil køligt. Airfry lige før dessert.",
            },
        ],
        "body": """Fyldte æbler med marcipan er jule-dessert uden ovn-drama: rå marcipan smelter ind i æblet, brunet smør og hasselnødder giver knas på toppen.

  Blød midte. Karamelliseret kant. Is ved siden af.""",
        "tip": "Lad ½ cm æblebund sidde. Går du igennem, løber marcipanen ud i kurven.",
    },
]


def yaml_str(s: str) -> str:
    if any(c in s for c in ':#"\'\n') or s.startswith(("-", "?", "[", "{", "*", "&", "!", "|", ">", "%", "@", "`")):
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return '"' + s + '"'


def dump_list(items: list[str], indent: int = 2) -> str:
    pad = " " * indent
    return "\n".join(f"{pad}- {yaml_str(i)}" for i in items)


def dump_faq(faq: list[dict], indent: int = 2) -> str:
    pad = " " * indent
    blocks = []
    for f in faq:
        blocks.append(f"{pad}- question: {yaml_str(f['question'])}\n{pad}  answer: {yaml_str(f['answer'])}")
    return "\n".join(blocks)


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    for r in RECIPES:
        path = ROOT / f"{r['slug']}.mdx"
        content = f"""---
title: {yaml_str(r['title'])}
slug: {r['slug']}
category: airfryer
description: {yaml_str(r['description'])}
prepTime: "{r['prepTime']}"
cookTime: "{r['cookTime']}"
totalTime: "{r['totalTime']}"
servings: {r['servings']}
difficulty: {r['difficulty']}
tags:
{dump_list(r['tags'])}
image: /recipes/airfryer/{r['slug']}.jpg
imageAlt: {yaml_str(r['imageAlt'])}
publishedAt: {PUBLISHED}
featured: true
ingredients:
{dump_list(r['ingredients'])}
steps:
{dump_list(r['steps'])}
faq:
{dump_faq(r['faq'])}
---

{r['body']}

<Tip>
{r['tip']}
</Tip>
"""
        path.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"Wrote {path.relative_to(path.parents[2])}")


if __name__ == "__main__":
    main()
