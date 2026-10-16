#!/usr/bin/env python3
"""Jul batch — flæskesteg, grød, klejner og juleklassikere (aug 2026)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"
PUBLIC = Path(__file__).resolve().parent.parent / "public/recipes"
PUBLISHED = "2026-08-31"
IMG_FLAEsk = PUBLIC / "airfryer" / "flaeskesteg.jpg"
IMG_RIS = PUBLIC / "gryde" / "klassisk-risengrod.jpg"

RECIPES = r'''
=====
title: Flæskesteg i trykkoger
slug: flaeskesteg-trykkoger
category: trykkoger
description: Flæskesteg i trykkoger — mørt kød på kort tid, sprød svær i ovn eller airfryer bagefter til jul.
prepTime: PT20M
cookTime: PT40M
totalTime: PT1H30M
servings: 6
difficulty: mellem
tags:
  - flæskesteg
  - flæskesteg trykkoger
  - jul
  - svinekød
  - trykkoger
  - festmad
imageAlt: Flæskesteg fra trykkoger med sprød svær efter finish
featured: true
ingredients:
  - 1 kamsteg med svær (1–1,5 kg)
  - 2 tsk salt
  - 1 tsk peber
  - 1 dl vand eller bouillon
  - 1 løg, kvart
steps:
  - Rid svær i riller. Salt i riller og på kød. Dup tør.
  - Læg steg i trykkoger med vand og løg. Høj tryk 25–30 minutter.
  - Tag steg ud. Dup tør. Svær opad — finish 220 °C ovn 15–20 min eller airfryer 200 °C 8–12 min.
  - Hvil 10 min. Skær langs rillerne. Brug sky til brun sovs.
faq:
  - question: Sprød svær fra trykkoger?
    answer: Nej alene — trykkogeren gør kødet mørt. Svær skal tørres og finishe ved høj varme bagefter.
  - question: Hvilken steg?
    answer: Kam med jævn svær. Nakke er bedre til pulled — kam vinder til flæskesteg.
  - question: Kerne-temperatur?
    answer: Træk ved 65–68 °C før finish. Over 72 °C bliver kødet tørt.
  - question: Jul eller hverdag?
    answer: Samme teknik — jul er bare dagen du serverer persillesovs til.
body: |
  Flæskesteg i trykkoger er tids-hack til juleaften.

  Tryk gør kødet mørt. Ovnen gør sværen ærefuld.

  To trin — spring ikke finish. Våd svær er juletraume, ikke tradition.
tip: Dup stegen knastørt og salt sværen igen før finish — salt suger restvæske og giver knas.
=====
title: Risengrod i airfryer
slug: risengrod-airfryer
category: airfryer
description: Risengrod i airfryer — cremet julegrød i ildfast form uden gryde på komfuret.
prepTime: PT5M
cookTime: PT45M
totalTime: PT50M
servings: 4
difficulty: nem
tags:
  - risengrod
  - risengroed
  - jul
  - morgenmad
  - airfryer
  - dessert
imageAlt: Cremet risengrod i skål med kanel og smør
featured: true
ingredients:
  - 1 dl grødris
  - 5 dl mælk
  - 1 dl vand
  - ½ tsk salt
  - 1 spsk smør
  - Sukker og kanel til servering
steps:
  - Bland ris, mælk, vand og salt i ildfast form der passer i airfryer.
  - Læg folie eller låg løst over. Airfry 160 °C i 35–45 min, rør hver 15 min.
  - Rør smør i. Smag til — tykere konsistens ved 5 min ekstra uden låg.
  - Server med smør, sukker og kanel — eller gem til risengrød dagen efter.
faq:
  - question: Brænder risene?
    answer: Rør ofte. Låg/folie holder på dampen. For høj varme = brune bund — hold 160 °C.
  - question: Samme som gryde?
    answer: Ja, men hænderne fri. Formen skal passe — for fuld = kog-over.
  - question: Til risengrød?
    answer: Lav grød d. 23. december. Gem halvdelen kold til risengrød d. 24 med fløde og mandler.
  - question: Mandel i grøden?
    answer: Det er risengrød-traditionen d. 24 — ikke risengroden d. 23.
body: |
  Risengrod i airfryer er julegrød uden gryde der koger over.

  Lav varme. Rør. Smør til sidst.

  Det er grøden d. 23 — risengrød er d. 24. Begge dele starter her.
tip: Brug bred lav form — tynd lag koger jævnere end høj skål i lille kurv.
=====
title: Æbleskiver i airfryer
slug: aebleskiver-airfryer
category: airfryer
description: Æbleskiver i airfryer — frosne eller hjemmelavede æbleskiver sprøde uden pande og stik.
prepTime: PT5M
cookTime: PT10M
totalTime: PT15M
servings: 4
difficulty: nem
tags:
  - æbleskiver
  - jul
  - airfryer
  - dessert
  - morgenmad
imageAlt: Gyldne æbleskiver med flormelis
featured: true
ingredients:
  - 16 frosne æbleskiver (eller færdig dej i forme)
  - Valgfrit: flormelis, syltetøj
steps:
  - Læg æbleskiver i kurv med plads — ikke stablet.
  - Airfry 180 °C i 8–10 minutter for frosne. Vend halvvejs hvis de er blege under.
  - Drys flormelis. Server med syltetøj mens de er lune.
faq:
  - question: Hjemmelavet dej?
    answer: Fyld æbleskivejern-forme eller små muffinforme — 160 °C længere tid, til gyldne og gennembagte.
  - question: Tørre?
    answer: For høj varme. 180 °C og vend. En skvæt smør i kurv hjælper.
  - question: Juleaften eller advent?
    answer: Begge. Frosne æbleskiver i airfryer er advents-hack når gæsterne ankommer.
  - question: Pandekager i stedet?
    answer: Se varme æbleskiver på pande — airfryer er til kugler, ikke flade.
body: |
  Æbleskiver i airfryer er jul uden fedtet pande på komfuret.

  Plads i kurven. Medium varme. Vend én gang.

  Frosne æbleskiver er ikke snyd — de er smart, når adventskaffen har ti gæster.
tip: Læg bagepapir i bunden af kurven — dejrester slipper lettere end direkte på rist.
=====
title: Klejner i ovn
slug: klejner-ovn
category: ovn
description: Klejner i ovn — sprøde juleklejner bagt på plade uden friture til jul og advent.
prepTime: PT30M
cookTime: PT15M
totalTime: PT1H
servings: 20
difficulty: mellem
tags:
  - klejner
  - jul
  - ovn
  - bagværk
  - dessert
imageAlt: Gyldne klejner på bageplade
featured: true
ingredients:
  - 250 g hvedemel
  - 50 g sukker
  - 1 tsk kardemomme
  - 1 tsk bagepulver
  - 75 g smør, koldt
  - 1 æg
  - 2 spsk fløde
  - 1 spsk hvidt rum eller vand
  - Flormelis til pynt
steps:
  - Bland mel, sukker, kardemomme og bagepulver. Smuldr smør i. Æg, fløde og rum — ælt kort til dej.
  - rul tyndt. Skær i rombeformer med lille snit i midten. Træk enden igennem hullet — klassisk klejneform.
  - Læg på bagepapir. Pensl let med æg. Bag 200 °C i 10–14 min til gyldne — ikke mørkebrune.
  - Afkøl. Drys flormelis. Opbevar lufttæt — de bliver sprødere næste dag.
faq:
  - question: Sprøde uden friture?
    answer: Tynd dej + høj varme kort tid. Ovn-klejner er lettere end friture — ikke helt samme crunch, men tæt på.
  - question: Dejen er for blød?
    answer: Køl 20 minutter før udrolling. For meget fløde = fed — tilføj lidt mel.
  - question: Hvor længe holder de?
    answer: Uge i tætte box. Julens klejner laves ofte uge 48–49 og spises hele december.
  - question: Norske klejner i airfryer?
    answer: Se norske klejner airfryer — denne opskrift er klassisk dansk ovn-version.
body: |
  Klejner i ovn er julebag uden friture-gymnastik.

  Tynd dej. Høj varme. Flormelis mens gæsterne kigger.

  De er ikke mormors friture — men de er sprøde nok til at ingen spørger, hvis der er gløgg nok.
tip: Skær snittet i midten stort nok — små huller lukker sig under bagning og klejneren mister formen.
=====
title: Julefrokost-tallerken
slug: julefrokost-tallerken
category: palaeg
description: Julefrokost-tallerken — sammensætning af pålæg, sild og sylte til det klassiske julebord.
prepTime: PT30M
cookTime: PT0M
totalTime: PT30M
servings: 6
difficulty: nem
tags:
  - julefrokost
  - jul
  - pålæg
  - smørrebrød
  - sild
  - frokost
imageAlt: Julefrokost-tallerken med sild, pålæg og rødbeder
featured: true
ingredients:
  - Rugbrød og franskbrød
  - 2 typer sild (fx kryddersild og rødvins-sild)
  - Leverpostej, rullepølse eller julesylte
  - Sennep, rødbeder, cornichons
  - Æggehalv, agurk, tomater
  - Smør til brød
steps:
  - Skær pålæg i passende skiver og anret på fade — sild, postej, sylte hver for sig.
  - Skær brød i skiver. Smør lige før servering så det ikke tørrer.
  - Anret tilbehør i små skåle: sennep, rødbeder, cornichons, kapers.
  - Lad gæsterne bygge selv — klassisk julefrokost uden stress ved tallerkenen.
faq:
  - question: Hvad skal der minimum være?
    answer: Sild, brød, sennep, rødbeder og ét fedt pålæg (postej eller flæsk). Resten er bonus.
  - question: Hvor meget per person?
    answer: 150–200 g pålæg + brød til 3–4 smørrebrød som starter før varm julemad.
  - question: Dagen før?
    answer: Skær pålæg og læg fade. Brød skæres samme dag. Sild smager bedre efter nat i lage.
  - question: Hjemmelavet vs købt?
    answer: Bland — hjemmelavet sennep og sylte imponerer. God købt sild er ikke snyd.
body: |
  Julefrokost-tallerken er pausen før flæskesteg.

  Sild. Brød. Sennep der stikker i næsen.

  Det er ikke en opskrift — det er en sammensætning. Se links til sild, julesylte og postej på Saltet.
tip: Server sild og fedt adskilt — rødvinsmarinade og leverpostej på samme kniv er julefrokost-uheld.
=====
title: Medister i fad til jul
slug: medister-i-fad-jul
category: ovn
description: Medister i fad til jul — hel medisterpølse bagt med løg, æbler og svesker til julebordet.
prepTime: PT15M
cookTime: PT45M
totalTime: PT1H
servings: 4
difficulty: nem
tags:
  - medister
  - medisterpølse
  - jul
  - ovn
  - dansk klassiker
imageAlt: Medister i fad med løg og æbler
featured: true
ingredients:
  - 1 stor medisterpølse (600–800 g)
  - 2 løg, i ringe
  - 2 æbler, i både
  - 100 g svesker
  - 1 dl æblemost eller vand
  - Salt, peber
steps:
  - Tænd ovn 180 °C. Læg medister i ovnfast fad med løg, æbler og svesker omkring.
  - Hæld most i bunden. Låg med folie de første 25 minutter.
  - Tag folie af. Bag 20 min mere, til medister er 75 °C og overfladen gylden.
  - Skær i skiver. Server sky og frugt som tilbehør til julemaden.
faq:
  - question: Revner pølsen?
    answer: Stik få huller med gaffel — damp undslipper. Folie tidligt holder den saftig.
  - question: Med rødkål?
    answer: Klassisk julekombination — medister som supplement til flæskesteg og and.
  - question: Pande i stedet?
    answer: Pande giver skorpe. Fad giver saft og frugt — bedre til julebord med mange retter.
  - question: For salt?
    answer: Medister er saltet — smag skyen før ekstra salt.
body: |
  Medister i fad er julebordet der husker 1987.

  Æbler. Svesker. Saft i bunden.

  Det er ikke gourmet — det er den pølse der altid var der, og som alle tager en skive af alligevel.
tip: Brug syrlige æbler — sødme mod medisterfedtet uden at blive dessert.
=====
title: Æbleflæsk til jul
slug: aebleflaesk-jul
category: gryde
description: Æbleflæsk til jul — klassisk dansk ret med saltet flæsk, æbler og løg til julebordet.
prepTime: PT15M
cookTime: PT40M
totalTime: PT55M
servings: 4
difficulty: nem
tags:
  - æbleflæsk
  - jul
  - flæsk
  - dansk klassiker
  - gryde
imageAlt: Æbleflæsk i gryde med løg og æbler
featured: true
ingredients:
  - 400 g saltet flæsk i tern
  - 3 syrlige æbler, i både
  - 2 løg, i ringe
  - 1 spsk sukker
  - ½ tsk peber
  - Valgfrit: 1 spsk eddike
steps:
  - Blanchér flæsket kort i kogende vand 2 min. Hæld af.
  - Steg flæsk sprødt i gryde på medium. Tag halvdelen ud til sprød topping.
  - Løg i fedtet til bløde. Æbler, sukker og peber i. Simre 10–15 min under låg.
  - Vend sprødt flæsk tilbage. Smag til — eddike hvis det mangler syre.
faq:
  - question: For salt?
    answer: Blanchér og brug letsaltet flæsk. Smag før mere salt — æblerne giver sødme.
  - question: Til julebord?
    answer: Ja — æbleflæsk er gammel jule- og vintermad ved siden af flæskesteg.
  - question: Vegetar-version?
    answer: Skip — det er flæsk og æbler. Se grøntsagsretter til julebord ellers.
  - question: Dagen efter?
    answer: Endnu bedre. Varm langsomt — sprødt flæsk taber crunch, men smagen sidder.
body: |
  Æbleflæsk er jul før flæskesteg tog over.

  Salt flæsk. Syrlige æbler. Løg der smelter.

  Det er rustikt julebord — server som side til kød, ikke som main event.
tip: Gem det sprøde flæsk til sidst — hvis det simrer for længe med æblerne, bliver det gummi.
=====
title: Gløgg-krydret svinemørbrad
slug: gloegg-svinemoerbrad-jul
category: ovn
description: Gløgg-krydret svinemørbrad — julesteg med krydderier, appelsin og portvin til juleaften.
prepTime: PT20M
cookTime: PT35M
totalTime: PT1H
servings: 4
difficulty: mellem
tags:
  - svinemørbrad
  - jul
  - gløgg
  - festmad
  - ovn
imageAlt: Skiver af gløgg-krydret svinemørbrad med sauce
featured: true
ingredients:
  - 600 g svinemørbrad
  - 1 tsk salt, peber
  - 1 tsk stødt kanel, ½ tsk nelliker, 1 tsk timian
  - 1 appelsin, saft og skal
  - 1 dl portvin eller rødvin
  - 1 spsk honning
  - 1 spsk smør
steps:
  - Tænd ovn 200 °C. Gnid mørbrad med salt, peber og krydderier.
  - Brun i ovnfast fad på komfuret. Ovn 15 min. Vend. 10–15 min til 63–65 °C.
  - Tag ud. Hvil. Deglasér fad med portvin, appelsin og honning — kog til sauce.
  - Skær mørbrad. Sauce over. Server med brunede kartofler.
faq:
  - question: Tørt kød?
    answer: Mørbrad tåler ikke over 65 °C — termometer er juleaftenens bedste ven.
  - question: Børn og gløgg-krydderi?
    answer: Skru ned for nelliker. Appelsin og timian giver jul uden stærk gløgg.
  - question: I stedet for flæskesteg?
    answer: Alternativ julesteg når nogen ikke spiser svær — eller som anden varm ret på julebordet.
  - question: Sauce for sød?
    answer: Eddike eller fond — balance sød portvin med salt og syre.
body: |
  Gløgg-krydret mørbrad er juleaften uden svær-diskussionen.

  Krydderier. Portvin. Rosa kerne.

  Det er fest uden flæskesteg — eller ved siden af, hvis I er mange om bordet.
tip: Riv appelsinskal før saft — skal i saucen, saft i fadet. Bitter hvid bund smager ikke jul.
'''


def parse_block(text: str) -> dict:
    lines = text.strip().split("\n")
    data: dict = {}
    mode = None
    body_lines: list[str] = []
    current_q = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("title: "):
            data["title"] = line[7:]
        elif line.startswith("slug: "):
            data["slug"] = line[6:]
        elif line.startswith("category: "):
            data["category"] = line[10:]
        elif line.startswith("description: "):
            data["description"] = line[13:]
        elif line.startswith("prepTime: "):
            data["prepTime"] = line[10:]
        elif line.startswith("cookTime: "):
            data["cookTime"] = line[10:]
        elif line.startswith("totalTime: "):
            data["totalTime"] = line[11:]
        elif line.startswith("servings: "):
            data["servings"] = line[10:]
        elif line.startswith("difficulty: "):
            data["difficulty"] = line[12:]
        elif line.startswith("featured: "):
            data["featured"] = line[10:]
        elif line.startswith("imageAlt: "):
            data["imageAlt"] = line[10:]
        elif line == "tags:":
            mode = "tags"
            data["tags"] = []
        elif line == "ingredients:":
            mode = "ingredients"
            data["ingredients"] = []
        elif line == "steps:":
            mode = "steps"
            data["steps"] = []
        elif line == "faq:":
            mode = "faq"
            data["faq"] = []
        elif line == "body: |":
            mode = "body"
        elif mode == "tags" and line.startswith("  - "):
            data["tags"].append(line[4:])
        elif mode == "ingredients" and line.startswith("  - "):
            data["ingredients"].append(line[4:])
        elif mode == "steps" and line.startswith("  - "):
            data["steps"].append(line[4:])
        elif mode == "faq" and line.startswith("  - question: "):
            current_q = line[14:]
        elif mode == "faq" and line.startswith("    answer: "):
            data["faq"].append({"question": current_q, "answer": line[12:]})
        elif mode == "body":
            if line.startswith("tip: "):
                mode = None
                data["tip"] = line[5:]
            else:
                body_lines.append(line)
        i += 1
    data["body"] = "\n".join(body_lines).strip()
    return data


def yaml_str(s: str) -> str:
    return '"' + s.replace('"', '\\"') + '"'


def to_mdx(d: dict) -> str:
    tags = "\n".join(f"  - {yaml_str(t)}" for t in d["tags"])
    ings = "\n".join(f"  - {yaml_str(x)}" for x in d["ingredients"])
    steps = "\n".join(f"  - {yaml_str(x)}" for x in d["steps"])
    faqs = "\n".join(
        f'  - question: {yaml_str(f["question"])}\n    answer: {yaml_str(f["answer"])}'
        for f in d["faq"]
    )
    featured = "featured: true\n" if d.get("featured") == "true" else ""
    slug = d["slug"]
    cat = d["category"]
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


IMG_MAP = {
    "flaeskesteg-trykkoger": IMG_FLAEsk,
    "risengrod-airfryer": IMG_RIS,
    "aebleskiver-airfryer": PUBLIC / "pande" / "varme-aebleskiver-pande.jpg",
    "klejner-ovn": PUBLIC / "airfryer" / "norske-klejner.jpg",
    "julefrokost-tallerken": PUBLIC / "palaeg" / "julesylte.jpg",
    "medister-i-fad-jul": PUBLIC / "pande" / "medisterpoelse-pande.jpg",
    "aebleflaesk-jul": PUBLIC / "palaeg" / "letsaltet-flaesk.jpg",
    "gloegg-svinemoerbrad-jul": PUBLIC / "ovn" / "glaseret-skinke-groenlangkaal.jpg",
}

blocks = [b for b in RECIPES.split("=====") if b.strip()]
print(f"blocks: {len(blocks)}")
written = []
for b in blocks:
    d = parse_block(b)
    if not d.get("ingredients"):
        continue
    assert d.get("faq") and len(d["faq"]) >= 3, d.get("slug")
    assert d.get("tip")
    out = ROOT / d["category"]
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{d['slug']}.mdx"
    if path.exists():
        raise SystemExit(f"slug collision: {path}")
    path.write_text(to_mdx(d), encoding="utf-8")
    written.append((d["category"], d["slug"]))
    print("wrote", d["category"] + "/" + path.name)

for cat, slug in written:
    dest = PUBLIC / cat / f"{slug}.jpg"
    dest.parent.mkdir(parents=True, exist_ok=True)
    src = IMG_MAP.get(slug, IMG_FLAEsk)
    if not dest.exists() and src.exists():
        print("warn: mangler unikt billede — tilføj foto i stedet for kopi:", dest.relative_to(PUBLIC.parent))

print(f"done: {len(written)} recipes")
