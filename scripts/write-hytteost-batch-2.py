#!/usr/bin/env python3
"""10 ekstra proteinrige hytteost-opskrifter — grill, røg, støbejern (okt 2026)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"
PUBLISHED = "2026-10-29"

RECIPES = r'''
=====
title: Plancha-smashed hytteost-tacos
slug: plancha-smashed-hytteost-tacos
category: plancha
description: Små tortillas på rygende plancha med hytteost-krydderikugle smash'et flad — sprød, karamelliseret osteskorpe under fyld.
prepTime: PT15M
cookTime: PT10M
totalTime: PT25M
servings: 4
difficulty: mellem
tags:
  - hytteost
  - protein
  - plancha
  - taco
  - smash
  - snack
imageAlt: Plancha-smashed tacos med karamelliseret hytteost-skorpe
featured: true
ingredients:
  - 8 små majs- eller hvedetortillas
  - 300 g hytteost, godt dryppet
  - 1 tsk røget paprika, ½ tsk spidskommen, ½ tsk chili, ½ tsk salt
  - Olie til plancha
  - Fyld: grillede grøntsager, kødstrimler eller bønner
  - Koriander, lime, løg til servering
steps:
  - Mos hytteost med paprika, spidskumen, chili og salt til en fast masse. Form 8 kugler.
  - Varm plancha til ca. 250 °C. Olie let. Læg tortilla på, hytteost-kugle i midten.
  - Smash hårdt med jern eller spartel, til osten spredes tyndt under/ved tortillaen. Pres 45–60 sekunder.
  - Vend forsigtigt, når skorpen slipper. Fyld, fold, server med lime og koriander.
faq:
  - question: Majs eller hvede?
    answer: Majs giver mere knas og autentisk taco. Hvede er mere bøjelig til fold.
  - question: Osten brænder?
    answer: Smash tyndere og flyt til lidt køligere zone. Maillard, ikke kul.
  - question: Uden smash-jern?
    answer: Tung spartel eller bunden af en lille gryde med bagepapir imellem.
  - question: Meal prep?
    answer: Krydderimassen ja. Smash først lige før servering — skorpen dør i kassen.
body: |
  Smash er ikke kun burger. Hytteost under tortillaen bliver karamel og skorpe.

  Hed plancha. Hårdt pres. Kort tid.

  Taco med osteskorpe i stedet for bare ost på toppen.
tip: Dryp hytteosten i viskestykke først. Våd ost damper i stedet for at brune.
=====
title: Grillet flanksteak-salat med røget hytteost-dressing
slug: grill-flanksteak-roeger-hytteost-dressing
category: grill
description: Saftig grillet flanksteak over grillet spidskål med koldrøget, cremet hytteost-dressing og groft flagesalt.
prepTime: PT20M
cookTime: PT45M
totalTime: PT1H5M
servings: 4
difficulty: mellem
tags:
  - hytteost
  - protein
  - flanksteak
  - grill
  - røg
  - salat
imageAlt: Flanksteak-salat med røget hytteost-dressing og spidskål
featured: true
ingredients:
  - 600–700 g flanksteak
  - 1 spidskål, skåret i både
  - 250 g hytteost
  - Bøgesmuld til koldrøg (til dressingen)
  - 2 spsk olivenolie, saft af 1 citron
  - 1 fed hvidløg, flagesalt, peber
  - Evt. grillede forårsløg
steps:
  - Læg hytteost i fad. Koldrøg under 30 °C i 25–35 minutter. Blend glat med olie, citron, hvidløg, peber.
  - Salt flanksteak generøst. Grill direkte høj varme 3–5 minutter pr. side til medium-rare. Hvile 10 minutter.
  - Grill spidskål-både med olie, til de har svedne kanter men stadig bid.
  - Skær kødet tyndt på tværs af fibrene. Anret over kål, dress med røget hytteost, flagesalt.
faq:
  - question: Uden koldrøg?
    answer: Røget paprika + en snert flydende røg, eller varmrøg osten 20 minutter ved 110 °C.
  - question: Andet kød?
    answer: Skirt, culotte eller kyllingebryst. Samme dressing.
  - question: For tyk dressing?
    answer: Mere citron eller en skvæt koldt vand under blend.
  - question: Hvilekød?
    answer: Ja — ellers løber saften ud på kålen i stedet for at blive i kødet.
body: |
  Flanksteak vil have direkte varme. Dressingen vil have røg og kulde.

  Grill kål. Skær tyndt. Dress tungt.

  Salat, der mætter som hovedret.
tip: Skær flanksteak altid på tværs af fibrene. Med fibrene er det skosåler.
=====
title: Støbejerns-shakshuka med pisket hytteost-skum
slug: stobejern-shakshuka-hytteost-skum
category: stobejern
description: Stærk tomatsauce med pocherede æg i støbejern — toppet med iskold, luftig hytteost-creme fra sifon lige før servering.
prepTime: PT15M
cookTime: PT25M
totalTime: PT40M
servings: 3
difficulty: mellem
tags:
  - hytteost
  - protein
  - shakshuka
  - støbejern
  - æg
  - brunch
imageAlt: Støbejerns-shakshuka med hytteost-skum på toppen
featured: true
ingredients:
  - 1 løg, 1 rød peberfrugt, 3 fed hvidløg
  - 2 spsk olie
  - 1 spsk tomatpuré, 1 tsk spidskommen, 1 tsk paprika, chiliflager
  - 400 g hakkede tomater
  - 4–5 æg
  - 250 g hytteost, godt dryppet
  - 1–2 spsk citronsaft, salt
  - Evt. sifonflaske + 1 N2O-patron (eller pisk hårdt i stedet)
  - Koriander eller persille
steps:
  - Svits løg og peber i støbejern. Hvidløg, tomatpuré og krydderier 1 minut. Tomater i, simre 10–12 minutter til saucen er tyk.
  - Lav fordybninger, knæk æg i. Låg på — eller ovn 200 °C — til hviderne er stive (5–8 minutter).
  - Blend hytteost med citron og salt helt glat. Fyld sifon, lad køle, eller pisk med elpisker til skum.
  - Sprøjt eller ske iskold hytteost-skum over den hede shakshuka lige før servering. Urter.
faq:
  - question: Uden sifon?
    answer: Pisk blendet hytteost 2–3 minutter med elpisker. Mindre luft, samme kontrast.
  - question: Forskel på shakshuka med hytteost-creme?
    answer: Her er cremen iskold skum ovenpå — ikke rørt i saucen. Temperaturkontrast er pointen.
  - question: For stærk?
    answer: Skip chiliflager. Mere peberfrugt.
  - question: Brød til?
    answer: Ja. Surdeig eller pitabrød til at skovle med.
body: |
  Shakshuka er varme og syre. Hytteost-skummet er det kolde chok ovenpå.

  Støbejern holder saucen. Sifonen holder luften.

  Brunch med attitude.
tip: Skummet skal være koldt. Varm hytteost-creme smelter ind og forsvinder i tomaten.
=====
title: Hytteost-cornbread i Dutch Oven
slug: hytteost-cornbread-dutch-oven
category: stobejern
description: Rustikt majsbrød i støbejernsgryde med hytteost i dejen — ekstremt svampet krumme under sprød skorpe, også over kul.
prepTime: PT15M
cookTime: PT35M
totalTime: PT50M
servings: 8
difficulty: nem
tags:
  - hytteost
  - protein
  - cornbread
  - støbejern
  - majs
  - Dutch Oven
imageAlt: Gyldent hytteost-cornbread i Dutch Oven
featured: true
ingredients:
  - 200 g majsmel
  - 100 g hvedemel
  - 2 tsk bagepulver, 1 tsk salt, 1 spsk sukker (valgfrit)
  - 250 g hytteost
  - 2 æg
  - 2 dl kærnemælk eller mælk
  - 50 g smeltet smør eller baconfedt + ekstra til gryden
steps:
  - Forvarm ovn til 200 °C (eller forbered kul til Dutch Oven). Smør gryden godt, og varm den.
  - Rør tørre ingredienser. Mos hytteost med æg, mælk og smeltet fedt. Fold vådt i tørt — klumper er ok.
  - Hæld i den hede gryde. Bag 30–35 minutter med låg (kul: gløder under og på låget), til spyd kommer rent ud.
  - Køl 10 minutter i gryden. Skær i både. Server med chili, smør eller BBQ.
faq:
  - question: Over kul?
    answer: Ja — ca. 8–10 briketter under, 12–14 på låget. Tjek efter 25 minutter.
  - question: Hvorfor hytteost?
    answer: Fugt og protein. Krummen bliver saftig uden at blive tung som ren flødeost.
  - question: Sød eller salt?
    answer: Skip sukker til BBQ-side. Behold det til brunch med honning.
  - question: Almindelig bradepande?
    answer: Fungerer, men skorpen bliver bedre i forvarmet støbejern.
body: |
  Cornbread uden tør midte. Hytteost er fugten. Dutch Oven er skorpen.

  Hed gryde. Hurtig dej. Ikke overælte.

  BBQ-bordets brød med protein.
tip: Varm gryden tom først. Dejen skal synge, når den lander — det er starten på skorpen.
=====
title: Maillard-ristede rodfrugter med bagt hytteost-crumble
slug: maillard-rodfrugter-hytteost-crumble
category: ovn
description: Efterårsrodfrugter sprødstegt til Maillard, vendt med krydret bagt hytteost-crumble for ekstra umami og protein.
prepTime: PT20M
cookTime: PT40M
totalTime: PT1H
servings: 4
difficulty: mellem
tags:
  - hytteost
  - protein
  - rodfrugter
  - ovn
  - crumble
  - efterår
  - umami
imageAlt: Ristede rodfrugter med gylden hytteost-crumble
featured: true
ingredients:
  - 1 kg blandede rodfrugter (gulerod, pastinak, rødbede, selleri), i stave
  - 2 spsk olie, salt, peber, 1 tsk røget paprika
  - 200 g hytteost, godt dryppet
  - 3 spsk mandelmel eller havregryn
  - 1 spsk olivenolie, ½ tsk hvidløgspulver, ½ tsk chili
  - Frisk timian
steps:
  - Forvarm ovn til 220 °C. Vend rodfrugter i olie, salt, peber og paprika. Fordel på bradepande.
  - Mos hytteost med mandelmel, olie, hvidløgspulver, chili og salt til en smuldrende masse. Fordel på bagepapir.
  - Bag rodfrugter 35–40 minutter, vend halvvejs. Bag crumble på anden plade 20–25 minutter, til den er dybt gylden og tør — smuldr undervejs.
  - Vend varme rodfrugter med crumble og timian. Evt. ekstra flagesalt.
faq:
  - question: Airfryer i stedet?
    answer: Rodfrugter 190 °C i portioner 18–22 minutter. Crumble i tyndt lag 12–15 minutter — ryst ofte.
  - question: Dehydrator?
    answer: Crumble kan tørres færdig ved 60 °C efter bagning for ekstra knas. Valgfrit nørderi.
  - question: For våd crumble?
    answer: Dryp osten hårdere, og bag længere. Den skal knase mellem fingrene.
  - question: Til kød?
    answer: Perfekt side til culotte, lam eller grillede pølser.
body: |
  Rodfrugter vil have høj varme. Crumble vil have tørhed og brunhed.

  Maillard på grønt. Umami fra ostestøv.

  Efterårsside med protein-knas.
tip: Bag crumble og rodfrugter samtidigt, men på separate plader — ellers damper crumble’n.
=====
title: Airfryer hytteost-onion rings
slug: airfryer-hytteost-onion-rings
category: airfryer
description: Store løgringe i tyk blendet hytteost-dej, vendt i knuste flæskesvær og airfryet til maksimal sprødhed.
prepTime: PT20M
cookTime: PT12M
totalTime: PT32M
servings: 3
difficulty: mellem
tags:
  - hytteost
  - protein
  - onion rings
  - airfryer
  - flæskesvær
  - snack
imageAlt: Sprøde hytteost-onion rings med flæskesvær-coating
featured: true
ingredients:
  - 2 store gule løg, skåret i 1,5 cm ringe
  - 250 g hytteost
  - 1 æg
  - 3 spsk mandelmel eller hvedemel
  - ½ tsk salt, ½ tsk røget paprika, peber
  - 80–100 g flæskesvær, knust fint
  - Olie-spray
steps:
  - Blend hytteost, æg, mel, salt, paprika og peber til en tyk dej.
  - Adskil løgringe. Dyp i dejen, lad overskud dryppe af. Vend i knuste flæskesvær.
  - Airfry ved 190 °C i 10–12 minutter. Vend forsigtigt halvvejs. Spray let med olie hvis de ser tørre ud.
  - Server straks med hytteost-tartarsauce eller aioli.
faq:
  - question: Uden flæskesvær?
    answer: Panko + parmesan. Mindre carnivore, stadig knas.
  - question: Dejen drypper af?
    answer: Tykkere dej (mere mel), og køl panerede ringe 10 minutter før airfry.
  - question: Vegetarisk?
    answer: Skip flæskesvær — brug panko eller knuste tortillachips.
  - question: Genopvarm?
    answer: Airfryer 180 °C i 3 minutter. Mikrobølgeovn ødelægger skorpen.
body: |
  Onion rings uden våd panering. Hytteost er limen. Flæskesvær er knaset.

  Tykk dej. Fin knus. Høj varme.

  Snack med protein og attitude.
tip: Knus flæskesvær fint — store stykker falder af i kurven.
=====
title: Sprøde hytteost-ravioli i airfryer
slug: airfryer-hytteost-ravioli
category: airfryer
description: Wonton-papir eller pastaplader fyldt med krydret hytteost og hvidløg, penslet med olie og airfryet til sprøde, boblende snacks.
prepTime: PT20M
cookTime: PT10M
totalTime: PT30M
servings: 4
difficulty: nem
tags:
  - hytteost
  - protein
  - ravioli
  - airfryer
  - snack
  - hvidløg
imageAlt: Sprøde airfryer-ravioli fyldt med hytteost
featured: true
ingredients:
  - 24 wonton-ark (eller friske pastaplader)
  - 250 g hytteost, dryppet
  - 1 fed hvidløg, presset
  - 30 g revet parmesan
  - ½ tsk salt, peber, chiliflager
  - 1 æg til at forsegle
  - Olie til pensling
steps:
  - Rør hytteost, hvidløg, parmesan, salt, peber og chili.
  - Læg 1 tsk fyld på hvert ark. Pensl kanter med æg. Læg ark ovenpå, pres luften ud, forsegle.
  - Pensl begge sider med olie. Airfry ved 180 °C i 8–10 minutter, vend halvvejs, til de er gyldne og bobler.
  - Server med tomatsauce eller hytteost-aioli.
faq:
  - question: Pastaplader i stedet for wonton?
    answer: Ja — rul tyndt, eller brug færdige lasagneplader blødgjort 1 minut i vand.
  - question: Åbner de sig?
    answer: For lidt æg på kanten, eller for meget fyld. Pres hårdt, og undgå luftbobler.
  - question: Kan de fryses?
    answer: Ja, rå. Airfry fra frost +2–3 minutter.
  - question: Til dip?
    answer: Marinara, pesto eller røget hytteost-dip.
body: |
  Ravioli uden kogevand. Fyld, forsegle, airfry.

  Wonton er genvejen. Hytteost er fyldet.

  Boblende snack på ti minutter.
tip: Overfyld ikke. 1 tsk er nok — mere sprænger sømmen i varmen.
=====
title: Tyk hytteost-tartarsauce
slug: hytteost-tartarsauce
category: dips
description: Proteinrigt alternativ til fish and chips-sauce — pisket hytteost med cornichoner, kapers, dild og masser af citron.
prepTime: PT10M
cookTime: PT0M
totalTime: PT10M
servings: 6
difficulty: nem
tags:
  - hytteost
  - protein
  - tartarsauce
  - dip
  - fisk
  - dild
imageAlt: Tyk hytteost-tartarsauce med cornichoner og dild
featured: true
ingredients:
  - 250 g hytteost
  - 4 spsk finthakkede cornichoner
  - 2 spsk kapers, hakket
  - 2 spsk frisk dild, hakket
  - Saft af 1 citron
  - 1 tsk dijon
  - 1 spsk olie
  - Salt, peber, evt. ½ tsk sukker
steps:
  - Blend 200 g hytteost med olie, dijon og citron til den er glat.
  - Fold resten af hytteosten, cornichoner, kapers og dild i med gaffel.
  - Smag til med salt, peber og evt. sukker.
  - Køl 15 minutter. Server til stegt fisk, fritter eller fish cakes.
faq:
  - question: Smager det af rigtig tartar?
    answer: Ja i DNA’et — syre, agurk, kapers, dild. Mindre mayo-tung, mere protein.
  - question: Holdbarhed?
    answer: 3 dage i køleskab. Bliver skarpere af lagen.
  - question: Til shrimp?
    answer: Perfekt. Også til grillede rejer og fish tacos.
  - question: For tynd?
    answer: Dryp hytteosten først, og brug mindre citron.
body: |
  Tartarsauce uden mayo-bjerget. Hytteost, cornichoner, kapers, dild, citron.

  Blend basen. Fold biddet i.

  Fish and chips med renere samvittighed.
tip: Hak cornichoner fint. Store tern stjæler showet fra fisken.
=====
title: Carnivore hytteost-spread med sprødt bacon
slug: carnivore-hytteost-spread-bacon
category: dips
description: Hytteost blendet glat med confiteret fedt og røget flagesalt, vendt med fintknust sprødstegt bacon — low-carb protein-spread.
prepTime: PT15M
cookTime: PT15M
totalTime: PT30M
servings: 6
difficulty: nem
tags:
  - hytteost
  - protein
  - carnivore
  - bacon
  - dip
  - low carb
  - keto
imageAlt: Carnivore hytteost-spread med knust bacon
featured: true
ingredients:
  - 300 g hytteost
  - 2–3 spsk confiteret ande- eller baconfedt (blødt)
  - 150 g bacon, stegt sprødt
  - ½–1 tsk røget flagesalt
  - Friskkværnet peber
steps:
  - Steg bacon sprødt. Dræn på papir. Knus fint.
  - Blend hytteost med fedt, til den er helt blank og glat. Smag til med røget flagesalt og peber.
  - Fold det meste af det knuste bacon i. Gem lidt til topping.
  - Server med agurkestave, ostesnacks eller på pork rinds.
faq:
  - question: Hvilket fedt?
    answer: Baconfedt, andefedt eller ghee. Det skal være smagfuldt, ikke neutral olie.
  - question: Strengt carnivore?
    answer: Skip peber, hvis du er purist. Ellers er det kød, ost og fedt.
  - question: Holdbarhed?
    answer: 3 dage. Bacon-knas bliver blødere — top friskt.
  - question: Til æg?
    answer: Ja — smear på omelet eller egg muffins.
body: |
  Ingen agurk. Ingen urter. Ost, fedt, bacon.

  Blend blank. Fold knas.

  Carnivore-snack der faktisk smager af noget.
tip: Salt forsigtigt — bacon og røget flagesalt er allerede aggressive.
=====
title: Hytteost-tzatziki med grillet agurk
slug: hytteost-tzatziki-grillet-agurk
category: dips
description: Agurk grillet hårdt på plancha for røgsmag, drænet og vendt i fed, dryppet hytteost med masser af hvidløg.
prepTime: PT15M
cookTime: PT10M
totalTime: PT25M
servings: 4
difficulty: nem
tags:
  - hytteost
  - protein
  - tzatziki
  - agurk
  - plancha
  - grill
  - dip
imageAlt: Hytteost-tzatziki med grillet agurk og hvidløg
featured: true
ingredients:
  - 300 g hytteost, godt dryppet
  - 1 stor agurk
  - 2–3 fed hvidløg, presset
  - 1 spsk olivenolie + mere til grill
  - Saft af ½ citron
  - Salt, peber, frisk dild
steps:
  - Skær agurk i lange skiver. Pensl med olie. Grill eller plancha hårdt, til der er tydelige svedne striber.
  - Køl kort. Hak fint. Dryp i si eller viskestykke — pres væsken ud.
  - Mos eller blend hytteost med hvidløg, olie, citron, salt og peber. Fold agurk og dild i.
  - Køl 20 minutter. Server til grillkød, pitabrød eller grøntsager.
faq:
  - question: Hvorfor grille agurken?
    answer: Røg og sødme. Klassisk tzatziki er rå og vandig — her er dybde.
  - question: Yoghurt i stedet for noget af osten?
    answer: 50/50 hytteost og græsk yoghurt er cremet. Ren hytteost holder proteinet højest.
  - question: For skarp hvidløg?
    answer: Ét fed, eller rist hvidløg kort på plancha først.
  - question: Holdbarhed?
    answer: 2 dage. Agurk slipper væske — rør op før servering.
body: |
  Tzatziki med grill i blodet. Agurken får striber. Hytteosten får hvidløg.

  Dryp begge. Fold. Køl.

  Græsk dip til dansk BBQ.
tip: Pres agurken hårdt efter grill. Ellers bliver dippen til suppe i skålen.
'''


def parse_block(text: str) -> dict:
    data = {}
    mode = None
    body_lines = []
    current_q = None
    i = 0
    lines = text.splitlines()
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
            data["difficulty"] = line.split(": ", 1)[1]
        elif line.startswith("imageAlt: "):
            data["imageAlt"] = line.split(": ", 1)[1]
        elif line.startswith("featured: "):
            data["featured"] = line.split(": ", 1)[1]
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
        elif line.startswith("body: |"):
            mode = "body"
            body_lines = []
        elif line.startswith("tip: "):
            mode = None
            data["tip"] = line[5:]
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


blocks = [b for b in RECIPES.split("=====") if b.strip()]
print(f"blocks: {len(blocks)}")
for b in blocks:
    d = parse_block(b)
    assert d.get("faq") and len(d["faq"]) >= 3, (d.get("slug"), d.get("faq"))
    assert d.get("tip"), d.get("slug")
    out = ROOT / d["category"]
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{d['slug']}.mdx"
    if path.exists():
        raise SystemExit(f"slug collision: {path}")
    path.write_text(to_mdx(d), encoding="utf-8")
    print("wrote", d["category"] + "/" + path.name)
