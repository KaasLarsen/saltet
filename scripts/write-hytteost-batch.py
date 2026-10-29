#!/usr/bin/env python3
"""20 proteinrige hytteost-opskrifter — maskiner, grill, røg, tryk (okt 2026)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"
PUBLISHED = "2026-10-29"

RECIPES = r'''
=====
title: Airfryer hytteost-chips med paprika og hvidløg
slug: airfryer-hytteost-chips-paprika
category: airfryer
description: Blendet hytteost smurt ultratyndt ud og airfryet til sprøde, boblende proteinchips med paprika og hvidløg.
prepTime: PT10M
cookTime: PT25M
totalTime: PT35M
servings: 2
difficulty: mellem
tags:
  - hytteost
  - protein
  - chips
  - snack
  - airfryer
  - paprika
imageAlt: Sprøde hytteost-chips med paprika på mørk tallerken
featured: true
ingredients:
  - 250 g hytteost (4–5 %), godt dryppet
  - 1 tsk røget paprika
  - ½ tsk hvidløgspulver
  - ¼ tsk flagesalt
  - Friskkværnet peber
steps:
  - Blend hytteost helt glat. Rør paprika, hvidløgspulver, peber og en snert salt i.
  - Læg bagepapir i airfryer-kurven. Smør massen ultratyndt ud (1–2 mm) med en paletkniv.
  - Airfry ved 180 °C i 12–15 minutter. Vend papiret forsigtigt, når kanterne løsner sig.
  - Fortsæt 8–12 minutter, til chipsene bobler, bruner og knækker. Køl 5 minutter — de stivner.
faq:
  - question: Hvorfor blender man hytteosten?
    answer: Kornene brænder ujævnt. Glat masse giver ensartet, boblende skorpe.
  - question: Bliver de bløde igen?
    answer: Ja, hvis de ligger lukket. Opbevar åbent eller i lufttæt dåse med husholdningspapir.
  - question: Kan man bruge magrere hytteost?
    answer: 1–2 % virker, men 4–5 % giver mere farve og mindre risiko for papirtynde flager.
  - question: Paprika uden røg?
    answer: Sød paprika går. Røget giver dybden, der matcher Saltets grill-umami.
body: |
  Hytteost-chips er snack uden chips-pose. Blend, smør tyndt, airfry højt.

  Tyndt er loven. Tykt bliver gummi.

  Når det bobler og knækker, er proteinet blevet knas.
tip: Smør tyndere end du tror. 1 mm er chips. 3 mm er omelet-låg.
=====
title: Sprøde hytteost-nuggets med panko
slug: airfryer-hytteost-nuggets-panko
category: airfryer
description: Små faste hytteost-kugler vendt i krydret panko og airfryet til guldskorpe — protein-nuggets uden kød.
prepTime: PT15M
cookTime: PT12M
totalTime: PT27M
servings: 3
difficulty: nem
tags:
  - hytteost
  - protein
  - nuggets
  - snack
  - airfryer
  - panko
imageAlt: Gyldne hytteost-nuggets med panko-skorpe
featured: true
ingredients:
  - 300 g hytteost, godt dryppet
  - 1 æg
  - 3 spsk mandelmel eller havregryn
  - ½ tsk salt, peber, ½ tsk røget paprika
  - 1 æg til panering
  - 80 g panko
  - 1 spsk olie til at vende panko
steps:
  - Dryp hytteost i si. Mos med æg, mandelmel, salt, peber og paprika til en fast masse. Køl 10 minutter.
  - Form små kugler (ca. 20 g). Vend i pisket æg, derefter i panko blandet med olie.
  - Airfry ved 190 °C i 10–12 minutter. Vend halvvejs, til skorpen er gylden.
  - Server med dip — fx hytteost-aioli eller BBQ.
faq:
  - question: Hvorfor køle massen?
    answer: Den sætter sig. Varm masse falder fra hinanden i paneringen.
  - question: Glutenfri?
    answer: Brug glutenfri panko eller knuste majschips. Mandelmel i massen allerede.
  - question: Kan de fryses?
    answer: Ja, rå panerede. Airfry fra frost +3–4 minutter.
  - question: For bløde indeni?
    answer: Dryp hårdere, og tilsæt 1 spsk ekstra mel. Væske er fjenden.
body: |
  Hytteost-nuggets er børnemad for voksne med proteinmål. Fast kerne, panko-knas.

  Dryp. Form. Vend. Airfry.

  Guldskorpe uden friturekar.
tip: Olie i pankoen giver farve. Tør panko bliver bleg og støvet.
=====
title: Hytteost-fyldte jalapeño poppers
slug: airfryer-hytteost-jalapeno-poppers
category: airfryer
description: Jalapeños fyldt med hytteost, cheddar og røget paprika, pakket i bacon og airfryet til sprød, cremet snack.
prepTime: PT15M
cookTime: PT14M
totalTime: PT29M
servings: 4
difficulty: nem
tags:
  - hytteost
  - protein
  - jalapeño
  - poppers
  - snack
  - airfryer
  - bacon
imageAlt: Bacon-svøbte jalapeño poppers med hytteostfyld
featured: true
ingredients:
  - 10–12 jalapeños, halveret, kerner og hinder skrabet ud
  - 200 g hytteost, dryppet
  - 80 g revet cheddar
  - 1 tsk røget paprika
  - 1 fed hvidløg, presset
  - Salt og peber
  - 10–12 skiver bacon
steps:
  - Rør hytteost, cheddar, paprika, hvidløg, salt og peber.
  - Fyld hver jalapeño-halvdel. Svøb med en halv eller hel baconskive, så åbningen er lukket.
  - Airfry ved 180 °C i 12–14 minutter, til baconet er sprødt og fyldet bobler.
  - Lad hvile 2 minutter — osten er lava.
faq:
  - question: For stærke?
    answer: Skrab alle hvide hinder. Brug mildere grøn chili, eller bland med friske peberfrugter.
  - question: Uden bacon?
    answer: Drys panko ovenpå og spray olie. Eller brug kalkunbacon.
  - question: Hytteost eller flødeost?
    answer: Hytteost giver mere protein og mindre fedt. Blend den glat, hvis du vil have klassisk creme.
  - question: Handsker?
    answer: Ja. Capsaicin i øjnene er en dårlig forret.
body: |
  Klassiske poppers, men fyldet er hytteost og cheddar. Protein møder chili.

  Bacon lukker. Airfryeren sprøder.

  Party-snack med grill-energi — uden grill.
tip: Læg poppers med sømmen nedad først 2 minutter, så baconet griber, før du vender.
=====
title: Hytteost-fritter i stave
slug: airfryer-hytteost-fritter-stave
category: airfryer
description: Fast dej af hytteost, æg og mandelmel skåret i stave og airfryet til sprøde pomfrit-alternativer med højt protein.
prepTime: PT15M
cookTime: PT18M
totalTime: PT33M
servings: 3
difficulty: mellem
tags:
  - hytteost
  - protein
  - fritter
  - snack
  - airfryer
  - low carb
imageAlt: Sprøde hytteost-fritter i stave som pommes-alternativ
featured: true
ingredients:
  - 300 g hytteost, godt dryppet
  - 2 æg
  - 80 g mandelmel
  - 1 spsk psyllium eller 2 spsk havregryn
  - ½ tsk bagepulver
  - 1 tsk salt, peber, ½ tsk hvidløgspulver
  - 1 spsk olie
steps:
  - Blend eller mos hytteost med æg. Rør mandelmel, psyllium, bagepulver og krydderier i til en fast dej.
  - Læg dejen mellem bagepapir. Rul til ca. 1 cm tyk plade. Køl 10 minutter.
  - Skær i stave. Pensl eller vend let i olie.
  - Airfry ved 190 °C i 15–18 minutter. Vend halvvejs, til de er gyldne og knasende udenpå.
faq:
  - question: Hvorfor køle?
    answer: Dejen skærer renere. Varm dej smører sig ud.
  - question: Havregryn i stedet for mandelmel?
    answer: Ja, 100 g finthakkede havregryn. Mere fiber, mindre low carb.
  - question: Dip?
    answer: Hytteost-aioli, remoulade eller røget hytteost-dip.
  - question: Bløde midt i?
    answer: Normal. Skorpen er pointen. Ekstra 3 minutter ved 200 °C, hvis du vil have dem tørrere.
body: |
  Hytteost-fritter er pommes uden kartoffel. Fast dej, stave, høj varme.

  Mandelmel binder. Airfryeren giver skorpe.

  Server ved siden af bøf eller som snack med dip.
tip: Dryp hytteosten i et viskestykke og vrid — våd dej giver slappe stave.
=====
title: Koldrøget hytteost med flagesalt og purløg
slug: koldroeger-hytteost-flagesalt
category: roeg
description: Hytteost på finmasket bakke koldrøget med bøgesmuld — dyb nordisk barbecuesmag med flagesalt og purløg.
prepTime: PT10M
cookTime: PT45M
totalTime: PT55M
servings: 4
difficulty: mellem
tags:
  - hytteost
  - protein
  - koldrøg
  - røg
  - BBQ
  - purløg
imageAlt: Koldrøget hytteost med flagesalt og purløg
featured: true
ingredients:
  - 400 g hytteost (gerne i en fast klump eller godt dryppet i form)
  - Bøgesmuld til koldrøg
  - Flagesalt
  - Frisk purløg, hakket
  - Friskkværnet peber
  - Evt. lidt olivenolie
steps:
  - Læg hytteost på en finmasket rist eller perforeret bakke, så røgen kan gå rundt. Dryp overfladen let.
  - Tænd koldrøg-generator med bøgesmuld. Hold grill/kammer under 30 °C.
  - Røg 30–45 minutter, til osten har tydelig røgaroma og let gylden overflade.
  - Drys flagesalt, peber og purløg. En snert olie. Server kold til knækbrød eller som BBQ-side.
faq:
  - question: Koldrøg eller varmrøg?
    answer: Koldrøg bevarer strukturen. Over 30 °C begynder hytteost at blive grødet.
  - question: Andet træ?
    answer: Æble eller kirsebær er mildere. Bøg er klassisk nordisk BBQ.
  - question: Holdbarhed?
    answer: 3–4 dage i køleskab, tæt lukket. Smagen bliver skarpere dag 2.
  - question: For våd ost?
    answer: Dryp 30 minutter i si først. Væske fortynder røgen.
body: |
  Koldrøget hytteost er BBQ uden kød. Bøgesmuld, lav temperatur, tålmodighed.

  Osten suger røg. Flagesalt lukker.

  Nordisk barbecuesmag i en skål.
tip: Hold låget på — træk ikke i røgen hvert andet minut. Stabil kold røg slår nysgerrighed.
=====
title: Plancha-stegte hytteost-bøffer
slug: plancha-hytteost-boeffer
category: plancha
description: Faste vegetariske koteletter af hytteost, revne rodfrugter og havregryn — presset hårdt på 250 °C plancha for Maillard-skorpe.
prepTime: PT20M
cookTime: PT12M
totalTime: PT32M
servings: 4
difficulty: mellem
tags:
  - hytteost
  - protein
  - plancha
  - vegetar
  - rodfrugter
  - Maillard
imageAlt: Plancha-stegte hytteost-bøffer med mørk skorpe
featured: true
ingredients:
  - 400 g hytteost, godt dryppet
  - 150 g revne gulerødder
  - 100 g revne rødbeder eller pastinak
  - 80 g havregryn (fin)
  - 1 æg
  - 1 tsk salt, peber, 1 tsk røget paprika
  - Olie til plancha
steps:
  - Mos hytteost med æg. Rør rodfrugter, havregryn og krydderier i. Massen skal kunne formes.
  - Form 4 flade bøffer. Køl 15 minutter.
  - Varm plancha til ca. 250 °C. Olie let. Læg bøfferne på, og pres hårdt med smash-jern eller spartel.
  - Steg 4–5 minutter pr. side uden at pille — skorpen skal sætte sig. Server med dip eller salat.
faq:
  - question: Hvorfor presse?
    answer: Mere kontakt = mere Maillard. Løse bøffer bruner ikke.
  - question: Binder ikke?
    answer: Mere havregryn eller 1 spsk mandelmel. Dryp osten hårdere.
  - question: Stegepande i stedet?
    answer: Ja, støbejern på høj varme. Samme pres, samme tålmodighed.
  - question: Kan de grilles?
    answer: Direkte grill er risikabelt — de falder igennem. Plancha eller pande.
body: |
  Hytteost-bøffer er vegetariske koteletter med grillattitude. Rodfrugt, havre, hård varme.

  Pres. Vent. Vend.

  Skorpen er retten. Midten er saftig protein.
tip: Vend først, når bøffen slipper af sig selv. Hvis den hænger, er skorpen ikke klar.
=====
title: Grillede hytteost-pakker
slug: grillede-hytteost-pakker
category: grill
description: Hytteost vendt med hvidløg, chili og friske krydderurter, grillet i bananblad eller folie til osten er varm og fast.
prepTime: PT10M
cookTime: PT15M
totalTime: PT25M
servings: 4
difficulty: nem
tags:
  - hytteost
  - protein
  - grill
  - chili
  - urter
  - side
imageAlt: Grillede hytteost-pakker åbnet med urter og chili
featured: true
ingredients:
  - 400 g hytteost
  - 2 fed hvidløg, finthakket
  - 1 frisk chili, finthakket
  - 2 spsk olivenolie
  - 1 håndfuld friske krydderurter (persille, koriander eller oregano)
  - Salt, peber, saft af ½ citron
  - Bananblade eller kraftigt sølvpapir
steps:
  - Rør hytteost med hvidløg, chili, olie, urter, salt, peber og citron.
  - Fordel på 4 bananblade eller dobbelt folie. Luk tæt til pakker.
  - Grill ved direkte middel varme 12–15 minutter. Vend én gang.
  - Åbn forsigtigt — dampen er hed. Server som side til kød eller med brød.
faq:
  - question: Bananblad eller folie?
    answer: Bananblad giver aroma. Folie er praktisk. Begge virker, hvis pakken er tæt.
  - question: Smelter osten væk?
    answer: Nej — hytteost bliver varm og fastere. Undgå at åbne for tidligt og miste damp.
  - question: Indirekte varme?
    answer: Kan. Tag +5 minutter. Direkte giver mere sveden kant på folien.
  - question: Flødeost i?
    answer: 50/50 med hytteost bliver cremet. Ren hytteost holder proteinet højest.
body: |
  Hytteost-pakker er grillens stille side. Hvidløg, chili, urter, lukket varme.

  Pakken damper. Osten sætter sig.

  Åbn ved bordet — dampen er showet.
tip: Dobbelt folie, hvis du griller hårdt. Én lag river, og osten lander i kullet.
=====
title: Røget hytteost-dip til BBQ
slug: roeger-hytteost-dip-bbq
category: dips
description: Varmrøget hytteost blendet med grillet hvidløg og chili — koldt, proteinrigt modspil til fedt svinebryst og ribs.
prepTime: PT15M
cookTime: PT40M
totalTime: PT55M
servings: 6
difficulty: mellem
tags:
  - hytteost
  - protein
  - dip
  - røg
  - BBQ
  - chili
imageAlt: Skål med røget hytteost-dip til BBQ
featured: true
ingredients:
  - 400 g hytteost
  - 1 hel hvidløg
  - 1–2 friske chilier
  - 1 spsk olivenolie
  - 1 tsk røget paprika
  - Saft af ½ citron, salt, peber
  - Træsmuld til varmrøg (bøg eller æble)
steps:
  - Læg hytteost i et lille fad. Røg ved 110–120 °C i 25–35 minutter, til overfladen er gylden og dufter.
  - Grill eller rist hele hvidløg og chili, til de er bløde og svedne. Press hvidløg ud af skallen.
  - Blend røget hytteost med hvidløg, chili, olie, paprika, citron, salt og peber til ønsket konsistens.
  - Køl. Server kold ved siden af brisket, ribs eller chips.
faq:
  - question: Uden rygeovn?
    answer: Brug røget paprika og en snert flydende røg sparsomt — eller røg kun hvidløg/chili.
  - question: For tyk?
    answer: 1–2 spsk creme fraiche eller lidt af hytteost-vallen. Eller mere olie.
  - question: Holdbarhed?
    answer: 3 dage i køleskab. Rør op før servering.
  - question: Hvor stærk chili?
    answer: Én mild chili til gæster. To med kerner til dig selv.
body: |
  Fedt kød skal have koldt, røget modspil. Hytteost suger røg og bliver dip.

  Grillet hvidløg er sødmen. Chili er kanten.

  BBQ-bordets protein-anker.
tip: Røg osten i fad, ikke direkte på risten — ellers drypper den ned i smuldet.
=====
title: Skillet hytteost-gnocchi i tomatsauce
slug: skillet-hytteost-gnocchi-tomat
category: pizzaovn
description: Hurtige gnocchi på hytteost og mel, brændt af i støbejern under pizzaovnens overvarme med intens tomatsauce.
prepTime: PT20M
cookTime: PT15M
totalTime: PT35M
servings: 3
difficulty: mellem
tags:
  - hytteost
  - protein
  - gnocchi
  - pizzaovn
  - støbejern
  - tomat
imageAlt: Skillet med hytteost-gnocchi i boblende tomatsauce
featured: true
ingredients:
  - 250 g hytteost, dryppet
  - 120–150 g hvedemel (eller 00-mel)
  - 1 æggeblomme
  - ½ tsk salt
  - 2 spsk olivenolie
  - 400 g hakkede tomater
  - 2 fed hvidløg, 1 tsk oregano, chiliflager
  - Revt parmesan og basilikum til servering
steps:
  - Mos hytteost med blomme og salt. Rør mel i til en blød, men formbar dej. Rul pølser, skær gnocchi.
  - Varm pizzaovn til 400 °C (eller ovn med max overvarme). Varm skillet med olie.
  - Svits hvidløg, hæld tomater, oregano og chili i. Læg gnocchi direkte i saucen.
  - Sæt skillet i ovnen 6–8 minutter under overvarme, til gnocchi er oppustede og toppen er sveden. Parmesan og basilikum.
faq:
  - question: Koge gnocchi først?
    answer: Nej her — de bages i saucen. Hurtigere, mere skorpe.
  - question: For klistret dej?
    answer: Mere mel, og dryp osten bedre. Dejen skal slippe fingrene.
  - question: Uden pizzaovn?
    answer: Almindelig ovn 250 °C med grill-element. Hold øje — det går stærkt.
  - question: Glutenfri?
    answer: Prøv 00-erstatning eller en blanding af rismel og kartoffelstivelse. Teksturen bliver anderledes.
body: |
  Hytteost-gnocchi er gnocchi uden kartoffelkog. Ost, mel, blomme — skillet under ild.

  Saucen bobler. Overvarmen brænder toppen.

  Italiensk street-energi i støbejern.
tip: Små gnocchi. Store klumper forbliver dejede i midten under den korte ovntid.
=====
title: Hytteost-hvidløgsbrød Pull-Apart
slug: hytteost-hvidloegsbroed-pull-apart
category: stobejern
description: Rustikt pull-apart brød i støbejernsgryde med lag af hytteost, hvidløgssmør og mozzarella.
prepTime: PT25M
cookTime: PT35M
totalTime: PT2H
servings: 6
difficulty: mellem
tags:
  - hytteost
  - protein
  - brød
  - hvidløg
  - støbejern
  - mozzarella
imageAlt: Pull-apart hvidløgsbrød med hytteost i støbejern
featured: true
ingredients:
  - 500 g hvedemel
  - 25 g frisk gær (eller 7 g tørgær)
  - 3 dl lunkent vand
  - 1 tsk salt, 1 tsk sukker
  - 250 g hytteost
  - 100 g mozzarella, revet
  - 75 g smør, blødt
  - 4 fed hvidløg, presset
  - Frisk persille, hakket
steps:
  - Rør gær op i vand med sukker. Tilsæt mel og salt. Ælt 8–10 minutter. Hæv 45–60 minutter.
  - Rør smør, hvidløg og persille. Mos hytteost let (ikke helt glat).
  - Del dejen i bolle-stykker. Smør hvert stykke med hvidløgssmør, top med hytteost og mozzarella. Stabl i smurt støbejernsgryde.
  - Efterhæv 20 minutter. Bag ved 200 °C i 30–35 minutter, til toppen er dybt gylden. Træk fra hinanden ved bordet.
faq:
  - question: Pizzaovn?
    answer: Ja, lavere varme end pizza — ca. 250 °C med sten eller i gryde, hold øje efter 20 minutter.
  - question: Kan man bruge færdig bolledeje?
    answer: Ja. Spring hævningen over, og gå direkte til lag og bagning.
  - question: For vådt midt i?
    answer: Dryp hytteosten. For meget valle giver soggy lag.
  - question: Dagen efter?
    answer: Varm i ovn 160 °C 10 minutter. Mikrobølgeovn gør skorpen trist.
body: |
  Pull-apart er brød, der bliver til leg. Hytteost mellem lagene løfter proteinet.

  Hvidløgssmør. Mozzarella. Støbejern.

  Riv, dip, gentag.
tip: Smør gryden godt, og lad brødet hvile 5 minutter før du river — oste-lagene sætter sig.
=====
title: Hytteost-tarte flambée
slug: hytteost-tarte-flambee
category: pizzaovn
description: Ultratynd Flammkuchen-bund smurt med blendet hytteost i stedet for crème fraîche, toppet med røget bacon og løg ved 400 °C.
prepTime: PT20M
cookTime: PT6M
totalTime: PT1H26M
servings: 2
difficulty: mellem
tags:
  - hytteost
  - protein
  - flammkuchen
  - pizzaovn
  - bacon
  - løg
imageAlt: Tynd hytteost-tarte flambée med bacon og løg
featured: true
ingredients:
  - 200 g hvedemel
  - 1 dl vand, 1 spsk olie, ½ tsk salt
  - 200 g hytteost, blendet glat
  - 1 stor løg, tynde skiver
  - 100 g røget bacon i strimler
  - Peber, evt. muskatnød
steps:
  - Ælt mel, vand, olie og salt til en stram dej. Hvil 30–60 minutter.
  - Blend hytteost glat. Smag til med peber og en snert muskat.
  - Rul dejen ultratynd. Smør hytteost ud. Fordel løg og bacon.
  - Bag på sten eller stål ved 400 °C i 3–6 minutter, til kanterne er svedne og toppingen bobler.
faq:
  - question: Crème fraîche i stedet?
    answer: Klassisk Flammkuchen bruger crème fraîche. Hytteost er magrere og mere protein — blend den helt glat.
  - question: Almindelig ovn?
    answer: Max varme med bagestål. Forvarm længe. Bliver lidt blødere end pizzaovn.
  - question: Vegetar?
    answer: Skip bacon. Brug røget paprika og tynde champignon-skiver.
  - question: Dejen river?
    answer: Mere hviletid. Kold dej ruller bedre.
body: |
  Tarte flambée er Alsace på sten. Her er cremen blendet hytteost.

  Tyndt. Hurtigt. 400 °C.

  Bacon og løg gør resten.
tip: Mindre topping end pizza. For meget væske slår den tynde bund ihjel.
=====
title: Bagt hytteost-omelet med sprød ostekant
slug: bagt-hytteost-omelet-ostekant
category: stobejern
description: Hytteost og æg pisket hårdt, hældt i rygende varm støbejernspande og bagt til den puster op med sprød ostekant.
prepTime: PT10M
cookTime: PT12M
totalTime: PT22M
servings: 2
difficulty: nem
tags:
  - hytteost
  - protein
  - omelet
  - støbejern
  - æg
  - morgenmad
imageAlt: Bagt hytteost-omelet i støbejern med sprød ostekant
featured: true
ingredients:
  - 200 g hytteost
  - 4 æg
  - 50 g revet ost (cheddar eller væster)
  - 1 spsk smør eller olie
  - Salt, peber, purløg
  - Valgfrit: spinat eller skinketern
steps:
  - Forvarm ovn eller pizzaovn til 220–250 °C. Varm skillet til den er rygende.
  - Pisk æg og hytteost hårdt. Salt, peber. Rør evt. fyld i.
  - Smør i panden. Hæld massen i. Drys ost ud til kanterne.
  - Bag 8–12 minutter, til omeletten puster og ostekanten er mørkegylden. Purløg. Skær i panden.
faq:
  - question: Hvorfor støbejern?
    answer: Varmen holder. Kanterne bruner, midten sætter sig. Nonstick giver ikke samme skorpe.
  - question: Bliver den våd?
    answer: Dryp hytteosten, og bag til midten ikke dirrer. Den sætter sig 1 minut efter ovnen.
  - question: Meal prep?
    answer: Ja. Køleskab 2 dage. Genopvarm kort i ovn eller airfryer.
  - question: Flere portioner?
    answer: Større pande, flere æg. Hold forholdet ca. 50 g hytteost pr. æg.
body: |
  Hytteost-omelet er æg, der fik protein-upgrade. Pisk hårdt, hæld i hed pande.

  Osten til kanten er skorpen.

  Morgenmad eller aftensmad — samme pande.
tip: Panden skal være hed, før massen lander. Kold pande = ingen ostekant.
=====
title: Trykkogt hytteost-curry
slug: trykkogt-hytteost-curry
category: trykkoger
description: Faste hytteost-tern trykkogt i intens indisk tomatsauce — paneer-style, hvor osten suger krydderierne uden at smelte væk.
prepTime: PT15M
cookTime: PT20M
totalTime: PT35M
servings: 4
difficulty: mellem
tags:
  - hytteost
  - protein
  - curry
  - trykkoger
  - indisk
  - tomat
imageAlt: Trykkogt hytteost-curry i tomatsauce
featured: true
ingredients:
  - 400 g hytteost, skåret i store tern (gerne tørret 20 min)
  - 1 løg, hakket
  - 3 fed hvidløg, 1 spsk reven ingefær
  - 2 spsk olie eller ghee
  - 1 spsk garam masala, 1 tsk spidskommen, 1 tsk gurkemeje, ½ tsk chili
  - 400 g hakkede tomater
  - 1 dl vand eller bouillon
  - ½ dl piskefløde eller kokosmælk (valgfrit)
  - Salt, koriander, citron
steps:
  - Brun løg i trykkogeren (sauté). Hvidløg, ingefær og krydderier 1 minut.
  - Tomater og vand i. Smag til med salt. Læg hytteost-tern ovenpå — rør ikke for hårdt.
  - Trykkog 5–6 minutter ved høj tryk. Naturlig aflastning 5 minutter, derefter ventil.
  - Rør forsigtigt. Evt. fløde. Koriander og citron. Server med ris eller blomkålsris.
faq:
  - question: Smelter hytteosten?
    answer: Store, tørrede tern holder. Mini-tern bliver til sauce. Tør 20 minutter på viskestykke først.
  - question: Paneer i stedet?
    answer: Klassisk. Samme metode. Hytteost er mere tilgængelig i DK og mere protein pr. krone.
  - question: Uden trykkoger?
    answer: Simre sauce 20 minutter i gryde, læg ost i de sidste 5.
  - question: Mildere?
    answer: Skip chilien, og brug mere fløde.
body: |
  Paneer-vibes med hytteost. Krydderier i tomat, kort tryk, ost der suger.

  Brun løgene. Respektér ternene.

  Intens curry uden timevis på komfuret.
tip: Rør først efter trykket er væk. Aggressiv omrøring før gør osten til grød.
=====
title: Cremet trykkogt kartoffelsuppe med hytteost-swirl
slug: trykkogt-kartoffelsuppe-hytteost
category: trykkoger
description: Klassisk efterårssuppe trykkogt på ca. 10 minutter, blendet cremet og toppet med kold, fed hytteost-creme.
prepTime: PT10M
cookTime: PT15M
totalTime: PT25M
servings: 4
difficulty: nem
tags:
  - hytteost
  - protein
  - kartoffelsuppe
  - trykkoger
  - efterår
  - suppe
imageAlt: Kartoffelsuppe med kold hytteost-swirl
featured: true
ingredients:
  - 800 g kartofler, skrællet, i tern
  - 1 løg, 2 fed hvidløg
  - 1 spsk smør
  - 8 dl hønse- eller grøntsagsbouillon
  - 1 laurbærblad, salt, peber
  - 200 g hytteost
  - 1 spsk citronsaft, purløg
  - Evt. 1 dl mælk til at tynde
steps:
  - Svits løg i smør i trykkogeren. Hvidløg 30 sekunder. Kartofler, bouillon, laurbær, salt.
  - Trykkog 8–10 minutter ved høj tryk. Aflast. Fjern laurbær.
  - Blend suppen cremet. Evt. mælk. Smag til.
  - Blend eller mos 150 g hytteost med citron til swirl. Top hver skål med kold creme, resten hytteost-korn og purløg.
faq:
  - question: Hvorfor kold swirl?
    answer: Kontrast. Varm suppe, kold protein-creme. Samme trick som crème fraîche — mere protein.
  - question: Med skræl?
    answer: Ja, hvis de er tyndskrællede. Blend længere.
  - question: Bacon på toppen?
    answer: Klassisk. Sprødt bacon og purløg er tilladt umami.
  - question: For tyk?
    answer: Mere bouillon. For tynd: kog uden låg 5 minutter efter blend.
body: |
  Kartoffelsuppe på tryk er hverdags-luksus på et kvarter. Blend, top, spis.

  Hytteost-swirlen er den kolde fedme.

  Efterår i skål — med protein.
tip: Gem en håndfuld kogte kartoffeltern før blend, hvis du vil have bid i bunden.
=====
title: Hytteost-dumplings i dampende fond
slug: hytteost-dumplings-fond
category: gryde
description: Små, intense protein-dumplings af hytteost kogt direkte i fyldig oksehale- eller hønsekødssuppe.
prepTime: PT20M
cookTime: PT25M
totalTime: PT45M
servings: 4
difficulty: mellem
tags:
  - hytteost
  - protein
  - dumplings
  - suppe
  - gryde
  - fond
imageAlt: Hytteost-dumplings i dampende kødsuppe
featured: true
ingredients:
  - 250 g hytteost, dryppet
  - 1 æg
  - 6 spsk hvedemel (eller semulje)
  - ½ tsk salt, peber, muskatnød
  - 2 spsk hakket persille
  - 1,5 l god oksehale- eller hønsefond/suppe
  - Evt. gulerod og porre i skiver til suppen
steps:
  - Mos hytteost med æg, mel, salt, peber, muskat og persille til en klæbrig dej. Køl 10 minutter.
  - Bring fonden i kog. Evt. grøntsager i, til de er møre.
  - Form små dumplings med to skeer. Læg dem i den let simrende fond.
  - Kog 8–10 minutter, til de flyder og er faste. Server dampende med masser af fond.
faq:
  - question: Falder de fra hinanden?
    answer: For lidt mel, eller for hård kogning. Simre, ikke rulle-kog. Køl dejen.
  - question: Semulje?
    answer: Ja — mere bid, mere nordisk. Lad dejen hvile 15 minutter, så semuljen svulmer.
  - question: Vegetarisk fond?
    answer: Fungerer. Vælg en kraftig grøntsagsfond med svampe til umami.
  - question: Kan de laves før?
    answer: Form og frys på bakke. Kog fra frost +2 minutter.
body: |
  Dumplings i fond er trøst med teknik. Hytteost gør dem protein-tunge.

  Simrende væske. Små klumper. Tålmodighed.

  Suppe, der mætter som hovedret.
tip: Test én dumpling først. Falder den fra, mere mel. For hård, mere hytteost.
=====
title: Hytteost-aioli med bagt hvidløg
slug: hytteost-aioli-bagt-hvidloeg
category: dips
description: Hytteost blendet glat med confiteret eller bagt hvidløg, olivenolie og citron — magert protein-alternativ til klassisk aioli.
prepTime: PT10M
cookTime: PT35M
totalTime: PT45M
servings: 6
difficulty: nem
tags:
  - hytteost
  - protein
  - aioli
  - hvidløg
  - dip
  - citron
imageAlt: Skål med cremet hytteost-aioli og bagt hvidløg
featured: true
ingredients:
  - 300 g hytteost
  - 1 hel hvidløg
  - 3 spsk olivenolie
  - Saft af ½–1 citron
  - Salt, peber
  - Evt. ½ tsk dijon
steps:
  - Bag hvidløg ved 180 °C i 30–35 minutter (skær top af, olie, folie), til feddene er bløde. Press ud.
  - Blend hytteost, hvidløg, olie, citron, salt, peber og evt. dijon helt glat.
  - Smag til. Køl 20 minutter, så smagen sætter sig.
  - Server til fritter, grillgrønt, fisk eller som burger-sauce.
faq:
  - question: Smager det af mayo?
    answer: Nej — det er lysere og syrligere. Samme rolle, mere protein, mindre fedt.
  - question: Råt hvidløg?
    answer: Kan, men skarpere. Bagte fed bliver søde og runde.
  - question: Holdbarhed?
    answer: 3–4 dage i køleskab. Rør op, hvis den skiller lidt.
  - question: For tyk?
    answer: Mere olie eller en skvæt koldt vand under blend.
body: |
  Aioli uden æggeblomme-stress. Hytteost, bagt hvidløg, olie, citron.

  Blend til den er blank.

  Magert greb, fuld hvidløgs-punch.
tip: Blend længere end du tror. Kornede aioli er bare dårligt blendet hytteost.
=====
title: Krydret hytteost-obatzda
slug: hytteost-obatzda
category: dips
description: Hytteost rørt med moden brie, smør, paprika og en tår mørk øl — tysk øl-dip til saltkringler efter grillsessionen.
prepTime: PT15M
cookTime: PT0M
totalTime: PT15M
servings: 6
difficulty: nem
tags:
  - hytteost
  - protein
  - obatzda
  - dip
  - paprika
  - øl
imageAlt: Hytteost-obatzda med paprika og forårsløg
featured: true
ingredients:
  - 250 g hytteost
  - 150 g moden brie eller camembert, skorpe fjernet
  - 40 g blødt smør
  - 1–2 tsk sød paprika
  - 2–3 spsk mørk øl
  - 1 lille løg eller forårsløg, finthakket
  - Salt, peber, merian (valgfrit)
steps:
  - Mos brie og smør sammen. Rør hytteost i — beholde lidt struktur eller blend halvdelen.
  - Paprika, øl, løg, salt, peber. Smag til. Mere paprika for farve.
  - Køl mindst 30 minutter.
  - Server med saltkringler, radiser eller knækbrød.
faq:
  - question: Klassisk obatzda?
    answer: Bruger camembert/brie og smør. Hytteost skærer fedmen og løfter proteinet.
  - question: Uden øl?
    answer: Lidt mælk eller æblemost. Øllen er tradition, ikke lov.
  - question: For skarp løg?
    answer: Skold hakket løg 10 sekunder i kogende vand, eller brug kun forårsløg.
  - question: Til grill?
    answer: Perfekt efter ribs — kold, fed, paprika-rød.
body: |
  Obatzda er Bayern i en skål. Her får den hytteost-boost.

  Brie for dybde. Paprika for farve. Øl for tradition.

  Saltkringler er ikke valgfrie.
tip: Køl ordenligt. Varm obatzda smager af løg og forvirring.
=====
title: Hytteost-remoulade med groft bid
slug: hytteost-remoulade
category: dips
description: Protein-twist på klassisk remoulade — hytteost blendet med kapers, hakkede syltede agurker og karry.
prepTime: PT15M
cookTime: PT0M
totalTime: PT15M
servings: 6
difficulty: nem
tags:
  - hytteost
  - protein
  - remoulade
  - dip
  - karry
  - fisk
imageAlt: Groft hytteost-remoulade med kapers og agurk
featured: true
ingredients:
  - 250 g hytteost
  - 2 spsk kapers, hakket
  - 4 spsk hakkede syltede agurker
  - 1 tsk karry
  - 1 spsk dijon
  - 1 spsk agurkelage eller citronsaft
  - 1 spsk olie
  - Salt, peber, dild eller purløg
steps:
  - Blend 200 g hytteost glat med olie, dijon, karry og lage.
  - Fold resten af hytteosten, kapers og agurk i med gaffel — groft bid.
  - Smag til med salt, peber og urter.
  - Køl 20 minutter. Server til fiskefilet, fritter eller roastbeef-mad.
faq:
  - question: Smager det af rigtig remoulade?
    answer: Tæt på — mere frisk, mindre mayo-tung. Karry og agurk er DNA’et.
  - question: Sukker?
    answer: Klassisk remoulade er lidt sød. ½ tsk sukker, hvis du vil have kantinen tilbage.
  - question: Holdbarhed?
    answer: 3 dage. Bliver skarpere af lagen.
  - question: Til hotdogs?
    answer: Ja. Protein-hotdog er pludselig en ting.
body: |
  Remoulade er dansk helligdom. Hytteost er indbruddet, der virker.

  Blend basen. Fold biddet i.

  Fisk, fritter, madder — samme skål.
tip: Gem noget hakket agurk til toppen. Det ser ud som om du har gjort dig umage.
=====
title: Protein-skinkesalat med hytteost
slug: protein-skinkesalat-hytteost
category: palaeg
description: Trevlet koldrøget skinke vendt i grov hytteostcreme med dijon og purløg — smørrebrødspålæg med højt protein.
prepTime: PT15M
cookTime: PT0M
totalTime: PT15M
servings: 4
difficulty: nem
tags:
  - hytteost
  - protein
  - skinke
  - pålæg
  - smørrebrød
  - dijon
imageAlt: Skinkesalat med hytteost på rugbrød
featured: true
ingredients:
  - 200 g koldrøget skinke, trevlet eller i strimler
  - 250 g hytteost
  - 1 spsk dijon
  - 1 spsk kapers (valgfrit)
  - 1 håndfuld purløg, hakket
  - Peber, evt. lidt citronsaft
  - Rugbrød og smør til servering
steps:
  - Mos eller blend halvdelen af hytteosten med dijon til creme. Fold resten i, så der er korn.
  - Vend skinke, kapers og purløg i. Peber. Evt. citron.
  - Smag til. Køl 10 minutter.
  - Server tykt på rugbrød — evt. med agurkskiver.
faq:
  - question: Hvilken skinke?
    answer: Koldrøget eller god pålægsskinke. Skip den vandede turkey-skinke.
  - question: Mayo?
    answer: Ikke nødvendigt. Hytteost + dijon er basen. 1 spsk mayo, hvis du vil have klassisk fedme.
  - question: Holdbarhed?
    answer: 2 dage. Skinke og mælkeprodukt — hold det koldt.
  - question: Kyllingesalat?
    answer: Samme metode med trevlet kyllingebryst.
body: |
  Skinkesalat behøver ikke et bjerg mayo. Hytteost, dijon, purløg.

  Trevl skinken. Vend groft.

  Smørrebrød, der faktisk mætter.
tip: Trevl skinken med hænderne, ikke tern — det føles mere delikatesse, mindre kantinekøkken.
=====
title: Røget laksesalat med pisket hytteost
slug: roeger-laksesalat-pisket-hytteost
category: palaeg
description: Koldrøget laks rørt op med pisket, luftig hytteost, dild og masser af citronskal — let pålæg med dyb røgsmag.
prepTime: PT15M
cookTime: PT0M
totalTime: PT15M
servings: 4
difficulty: nem
tags:
  - hytteost
  - protein
  - laks
  - pålæg
  - dild
  - røget
imageAlt: Røget laksesalat med pisket hytteost og dild
featured: true
ingredients:
  - 150 g koldrøget laks, hakket
  - 250 g hytteost
  - Saft og skal af 1 citron
  - 1 stor håndfuld dild, hakket
  - Friskkværnet peber
  - Evt. 1 spsk creme fraiche for ekstra luft
steps:
  - Blend eller pisk hytteost med citronsaft, til den er luftig og næsten mousse-agtig.
  - Fold hakket laks, citronskal og dild i med spatel. Peber. Evt. creme fraiche.
  - Smag til — mere skal, hvis det mangler aroma.
  - Server på knækbrød, bagel eller rugbrød.
faq:
  - question: Varmrøget laks?
    answer: Kan. Mere kraftig, mere tør. Hak finere, og tilsæt lidt ekstra citron.
  - question: Salt?
    answer: Røget laks er salt. Smag før du salter.
  - question: Forskel på laksecreme?
    answer: Denne er grovere salat med bid. Cremen er mere blendet og glat.
  - question: Holdbarhed?
    answer: 1–2 dage. Fisk og frisk citron — spis friskt.
body: |
  Laks, hytteost, dild, citronskal. Fire ting, klar pålæg.

  Pisk osten luftig. Fold fisken i.

  Røg og syre — ikke tung mayo-salat.
tip: Riv citronskallen før du presser saften. Omvendt rækkefølge er klodset og våd.
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
