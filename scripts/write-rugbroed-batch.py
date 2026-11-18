#!/usr/bin/env python3
"""Rugbrød-batch: 12 huller + billedkopi (nov 2026)."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RECIPES_DIR = ROOT / "content" / "recipes"
PUBLIC = ROOT / "public" / "recipes"
PUBLISHED = "2026-11-18"

IMG_MAP = {
    "malt-oel-rugbroed": PUBLIC / "ovn" / "klassisk-surdejsrugbroed.jpg",
    "skagensrugbroed": PUBLIC / "ovn" / "solsikke-hoerfroe-rugbroed.jpg",
    "hasselnod-tranebaer-rugbroed": PUBLIC / "ovn" / "graeskarkerne-rugbroed.jpg",
    "valnoedde-rugbroed": PUBLIC / "ovn" / "limfjords-porter-valnoedder.jpg",
    "stenalderbroed": PUBLIC / "airfryer" / "keto-madbrod.jpg",
    "kaernemaelk-rugbroed": PUBLIC / "ovn" / "skyr-rugbroed.jpg",
    "hurtigt-rugbroed-airfryer": PUBLIC / "airfryer" / "soenderjyske-rugbroedsboller.jpg",
    "gulerods-rugbroed": PUBLIC / "ovn" / "knuste-gulerodder-parmesan.jpg",
    "kartoffel-rugbroed": PUBLIC / "ovn" / "fyldt-bagekartoffel.jpg",
    "rugbroedschips-airfryer": PUBLIC / "ovn" / "rugbroedschips.jpg",
    "rugbroedsdrys": PUBLIC / "ovn" / "maillard-rodfrugter-hytteost-crumble.jpg",
    "oellebroed": PUBLIC / "gryde" / "gammeldags-floejsgoed.jpg",
}

RECIPES = r'''
=====
title: Malt- og ølrugbrød
slug: malt-oel-rugbroed
category: ovn
description: Malt- og ølrugbrød bagt med mørk hvidtøl eller porter og maltsirup — dyb farve, fyldig smag og saftig krumme.
prepTime: PT30M
cookTime: PT1H20M
totalTime: PT5H
servings: 12
difficulty: mellem
tags:
  - rugbrød
  - øl
  - malt
  - porter
  - brød
  - ovn
imageAlt: Mørkt malt- og ølrugbrød skåret på bræt
featured: false
ingredients:
  - 400 g rugmel
  - 100 g hvedemel
  - 25 g frisk gær eller 8 g tørgær
  - 2½ dl mørk hvidtøl eller porter (lunkent)
  - 1½ dl lunkent vand
  - 2 spsk maltsirup eller mørk sirup
  - 1½ tsk salt
  - 80 g solsikkekerner, udblødte
steps:
  - Rør gær ud i øl og vand med maltsirup. Tilsæt salt, mel og kerner. Ælt 8–10 minutter til en klæbrig, trådet dej.
  - Hæv tildækket 2–3 timer ved stuetemperatur, til dejen er boblet og syrlig-sød i duften.
  - Fyld i smurt 2-liters form. Glat toppen med våd ske. Efterhæv 45–60 minutter.
  - Bag ved 180 °C i 70–80 minutter. Dæk med folie de sidste 15 minutter, hvis skorpen bliver for mørk.
  - Tip ud, køl på rist mindst 4 timer — gerne til næste dag — før du skærer.
faq:
  - question: Hvilken øl?
    answer: Porter, stout eller mørk hvidtøl. Undgå bitter IPA — humlen bliver skarp i brødet.
  - question: Uden maltsirup?
    answer: Mørk sirup eller 1 spsk melasse. Smagen bliver mildere, farven lysere.
  - question: Surdej i stedet for gær?
    answer: 150 g aktiv rug-surdej, skip gæren, hæv længere. Se også klassisk surdejsrugbrød.
  - question: Hvorfor vente med at skære?
    answer: Rug sætter sig. Varmt brød klæber og smuldrer.
body: |
  Malt- og ølrugbrød er den mørke fætter: porter i dejen, maltsirup i skorpen, dybde uden surdejspasning.

  Øllen er væske og smag. Ikke en excuse for at drikke resten af flasken — det er også okay.
tip: Varm øllen til lunkent, ikke kogende. Kogende dræber gæren.
=====
title: Skagensrugbrød
slug: skagensrugbroed
category: ovn
description: Skagensrugbrød — lyst rugbrød vendt i solsikkekerner og blå birkes for masser af knas og en sprød skorpe.
prepTime: PT25M
cookTime: PT1H10M
totalTime: PT4H
servings: 12
difficulty: mellem
tags:
  - rugbrød
  - skagen
  - solsikkekerner
  - birkes
  - brød
  - ovn
imageAlt: Lyst Skagensrugbrød dækket af solsikkekerner og blå birkes
featured: false
ingredients:
  - 300 g sigtet rugmel
  - 200 g hvedemel
  - 25 g frisk gær eller 8 g tørgær
  - 3½ dl lunkent vand
  - 1 dl kærnemælk
  - 1½ tsk salt
  - 1 spsk lys sirup
  - 80 g solsikkekerner + 2 spsk blå birkes til rulle
steps:
  - Rør gær ud i vand og kærnemælk med sirup. Tilsæt salt og mel. Ælt 8 minutter til en blød, lidt klæbrig dej.
  - Hæv 1½–2 timer, til den er fordoblet.
  - Tip ud på melet bord. Form til et aflangt brød. Pensl med vand, rul i solsikkekerner og birkes.
  - Læg på bagepapir. Efterhæv 40–50 minutter.
  - Bag ved 200 °C i 55–65 minutter, til skorpen er gylden og brødet lyder hult. Køl på rist mindst 2 timer.
faq:
  - question: Hvorfor sigtet rugmel?
    answer: Det giver den lysere Skagen-krumme. Fuldkornsrug gør det mørkere og tættere.
  - question: Kun solsikke?
    answer: Ja. Birkes er finish. Uden dem er det stadig knas — bare mindre nordjysk look.
  - question: Form i stedet for frit?
    answer: Kan godt. Skip rulle-trinnet, og drys kerner ovenpå i formen.
  - question: Holdbarhed?
    answer: 4–5 dage indpakket. Frys skiver.
body: |
  Skagensrugbrød er det lyse knas-brød: mere hvede end klassisk rug, skorpe pakket i solsikke og blå birkes.

  Det er smørrebrød med attitude — ikke det tunge surdejsloft.
tip: Pensl med vand lige før kernerne, ellers falder de af i ovnen.
=====
title: Rugbrød med ristede hasselnødder og tranebær
slug: hasselnod-tranebaer-rugbroed
category: ovn
description: Rugbrød med ristede hasselnødder og tørrede tranebær — nøddeagtigt, syrligt og perfekt til ostebordet.
prepTime: PT30M
cookTime: PT1H15M
totalTime: PT5H
servings: 12
difficulty: mellem
tags:
  - rugbrød
  - hasselnødder
  - tranebær
  - ost
  - brød
  - ovn
imageAlt: Rugbrød med synlige hasselnødder og tranebær skåret på bræt
featured: false
ingredients:
  - 350 g rugmel
  - 150 g hvedemel
  - 25 g frisk gær eller 8 g tørgær
  - 4 dl lunkent vand
  - 1½ tsk salt
  - 2 spsk mørk sirup
  - 100 g hasselnødder, groft hakkede og ristede
  - 80 g tørrede tranebær
steps:
  - Riv hasselnødderne groft. Rist på tør pande 3–4 minutter, til de dufter. Køl.
  - Rør gær, vand og sirup. Tilsæt salt og mel. Ælt 8 minutter. Fold nødder og tranebær i til sidst.
  - Hæv 2–3 timer tildækket.
  - Fyld i smurt form. Glat toppen. Efterhæv 45–60 minutter.
  - Bag ved 180 °C i 70–75 minutter. Køl på rist mindst 4 timer før skæring.
faq:
  - question: Friske tranebær?
    answer: Nej — for våde. Tørrede. Hak store, hvis de er hele.
  - question: Valnødder i stedet?
    answer: Ja. Se også valnødderugbrød. Hasselnød er sødere.
  - question: Til hvad?
    answer: Blåskimmel, brie, leverpostej eller bare smør. Efterår på et bræt.
  - question: Bliver det sødt?
    answer: Let. Sirup og bær. Saltet holder det i skak.
body: |
  Hasselnød og tranebær i rug er ostebords-brødet: ristet nød, syrlig bær, mørk krumme.

  Rist nødderne. Rå hasselnød smager træ.
tip: Fold bærrene i til sidst — lang æltning knuser dem til røde striber.
=====
title: Valnødderugbrød
slug: valnoedde-rugbroed
category: ovn
description: Valnødderugbrød — kraftigt kernebrød med grofthakkede valnødder og en anelse honning til dybde og knas.
prepTime: PT25M
cookTime: PT1H15M
totalTime: PT5H
servings: 12
difficulty: mellem
tags:
  - rugbrød
  - valnødder
  - kerner
  - honning
  - brød
  - ovn
imageAlt: Kraftigt valnødderugbrød med synlige nødder i krummen
featured: false
ingredients:
  - 400 g rugmel
  - 100 g hvedemel
  - 25 g frisk gær eller 8 g tørgær
  - 4 dl lunkent vand
  - 1½ tsk salt
  - 1 spsk honning
  - 1 spsk mørk sirup
  - 120 g valnødder, groft hakkede
  - 40 g solsikkekerner (valgfrit)
steps:
  - Hak valnødder groft. Rist let på tør pande 2–3 minutter. Køl.
  - Rør gær ud i vand med honning og sirup. Tilsæt salt og mel. Ælt 8 minutter. Rør nødder og kerner i.
  - Hæv 2–3 timer.
  - Fyld i smurt form. Efterhæv 45–60 minutter.
  - Bag ved 180 °C i 70–80 minutter. Køl på rist mindst 4 timer.
faq:
  - question: Hvorfor honning?
    answer: En spiseske. Den binder bitterheden i valnødderne uden at gøre brødet sødt.
  - question: Surdej?
    answer: 150 g aktiv surdej, skip gær, længere hæv. Smagen bliver dybere.
  - question: Bittre nødder?
    answer: Rist dem. Gamle valnødder smager harsk — smag én før dejen.
  - question: Til ost?
    answer: Ja. Blåskimmel og æble. Eller bare smør.
body: |
  Valnødderugbrød er det kraftige madbrød: groft hak, lidt honning, mørk rug.

  Ikke dessert. Nødderne er protein og knas.
tip: Hak groft — for fint bliver det pasta i krummen.
=====
title: Stenalderbrød (keto)
slug: stenalderbroed
category: ovn
description: Stenalderbrød uden mel — æg, hørfrø, sesam, mandler og græskarkerner. Keto-agtigt madbrød med knas og mæthed.
prepTime: PT15M
cookTime: PT50M
totalTime: PT1H15M
servings: 10
difficulty: nem
tags:
  - stenalderbrød
  - keto
  - low-carb
  - brød
  - hørfrø
  - ovn
imageAlt: Skivet stenalderbrød med synlige kerner og frø
featured: true
ingredients:
  - 5 æg
  - 100 g mandelmel
  - 50 g hørfrø, knuste
  - 50 g sesamfrø
  - 50 g græskarkerner
  - 50 g solsikkekerner
  - 2 spsk olivenolie eller smeltet smør
  - 1 tsk bagepulver
  - 1 tsk salt
  - 1 dl vand eller usødet mandelmælk
steps:
  - Tænd ovnen på 175 °C. Beklæd en lille brødform (ca. 1 liter) med bagepapir.
  - Bland alle tørre ingredienser. Pisk æg, olie og væske. Rør det våde i det tørre til en tyk dej.
  - Fyld i formen. Glat toppen. Drys evt. ekstra sesam.
  - Bag 45–55 minutter, til toppen er gylden og en tandstikker kommer ud ren. Dæk med folie, hvis det bruner for hurtigt.
  - Køl i formen 15 minutter, derefter på rist. Skær først når det er køligt — det sætter sig.
faq:
  - question: Er det rugbrød?
    answer: Nej. Det er stenalder-/keto-madbrød uden mel. Det står her, fordi det erstatter rug til smørrebrød på low-carb.
  - question: Hele hørfrø?
    answer: Knus dem. Hele frø giver mindre bind. Stavblender eller morter.
  - question: Holder det?
    answer: Køleskab 4–5 dage. Frys skiver. Rist før brug.
  - question: Mere brød-agtigt?
    answer: Se også keto-madbrød med parmesan i airfryer — anden tekstur, mere ost.
body: |
  Stenalderbrød er ikke rug. Det er æg, frø og nødder i en form — mæthed uden mel.

  Det smager nøddeagtigt. Rist skiven. Smør. Pålæg. Færdig.
tip: Vej mandelmelet. For meget, og det bliver tørt som kiks.
=====
title: Rugbrød uden surdej med kærnemælk
slug: kaernemaelk-rugbroed
category: ovn
description: Rugbrød uden surdej — kærnemælk og gær til hverdagen. Saftig krumme uden surdejspasning.
prepTime: PT25M
cookTime: PT1H15M
totalTime: PT4H
servings: 12
difficulty: nem
tags:
  - rugbrød
  - kærnemælk
  - gær
  - uden surdej
  - brød
  - ovn
imageAlt: Saftigt kærnemælksrugbrød skåret på bræt
featured: true
ingredients:
  - 400 g rugmel
  - 100 g hvedemel
  - 25 g frisk gær eller 8 g tørgær
  - 3 dl kærnemælk, lunkent
  - 1½ dl lunkent vand
  - 1½ tsk salt
  - 2 spsk mørk sirup
  - 80 g blandede kerner (solsikke, græskar), udblødte
steps:
  - Rør gær ud i kærnemælk og vand med sirup. Tilsæt salt, mel og kerner. Ælt 8–10 minutter til klæbrig dej.
  - Hæv tildækket 2 timer, til den er boblet.
  - Fyld i smurt 2-liters form. Glat toppen. Efterhæv 45–60 minutter.
  - Bag ved 180 °C i 70–75 minutter.
  - Køl på rist mindst 4 timer før skæring.
faq:
  - question: Uden kærnemælk?
    answer: Tynd yoghurt naturel 1:1 med vand, eller mælk med 1 spsk eddike. Smagen bliver mildere.
  - question: Hvorfor ikke surdej?
    answer: Fordi det er tirsdag. Gær og kærnemælk giver syre-agtig dybde uden fodring.
  - question: For tæt?
    answer: For lidt væske eller for kort hæv. Dejen skal klistre.
  - question: Surdejsversion?
    answer: Se klassisk surdejsrugbrød.
body: |
  Rugbrød uden surdej er hverdagsbrødet: kærnemælk, gær, form, ovn.

  Ingen fodring. Ingen nattevagt. Stadig rug.
tip: Kærnemælken skal være lunkent — kold bremser gæren.
=====
title: Hurtigt rugbrød i airfryer
slug: hurtigt-rugbroed-airfryer
category: airfryer
description: Hurtigt rugbrød i airfryer — lille hverdagsbrød bagt uden at tænde den store ovn.
prepTime: PT15M
cookTime: PT35M
totalTime: PT2H
servings: 6
difficulty: nem
tags:
  - rugbrød
  - airfryer
  - hurtig
  - brød
  - gær
imageAlt: Lille rugbrød bagt i airfryer skåret i skiver
featured: true
ingredients:
  - 200 g rugmel
  - 50 g hvedemel
  - 12 g frisk gær eller 4 g tørgær
  - 2 dl lunkent vand
  - ½ dl kærnemælk
  - 1 tsk salt
  - 1 spsk mørk sirup
  - 40 g solsikkekerner
steps:
  - Rør gær ud i vand og kærnemælk med sirup. Tilsæt salt, mel og kerner. Ælt 5 minutter til klæbrig dej.
  - Hæv 60–75 minutter i skålen.
  - Smør en lille form der passer i kurven (ca. 15 cm), eller brug en silikoneform. Fyld dejen i. Efterhæv 20–30 minutter.
  - Forvarm airfryeren til 160 °C. Bag 30–35 minutter, til toppen er mørk og midten er ca. 96 °C. Dæk med folie, hvis det bruner for hurtigt.
  - Køl på rist mindst 1 time før skæring.
faq:
  - question: Hvor stort et brød?
    answer: Lille. Airfryeren er ikke en ovn. Halv portion. Til to–tre dages smørrebrød.
  - question: Uden form?
    answer: Dejen løber. Brug form. Eller lav sønderjyske rugbrødsboller i stedet.
  - question: Kan man bruge bagepulver?
    answer: Ja — skip gær og hæv, brug 2 tsk bagepulver, bag med det samme. Mere som skyr-rugbrød.
  - question: Ovn i stedet?
    answer: Ja. 180 °C i 50–60 minutter for denne portion.
body: |
  Hurtigt rugbrød i airfryer er det lille brød, når ovnen er for meget.

  Mindre form. Lavere varme. Stadig rug.
tip: Tjek midten med termometer. Airfryere bruner toppen før kernen er færdig.
=====
title: Saftigt gulerodsrugbrød
slug: gulerods-rugbroed
category: ovn
description: Saftigt gulerodsrugbrød med revet gulerod — sødme, fugt og en krumme der holder sig blød i dagevis.
prepTime: PT25M
cookTime: PT1H15M
totalTime: PT4H30M
servings: 12
difficulty: nem
tags:
  - rugbrød
  - gulerod
  - saftigt
  - brød
  - ovn
imageAlt: Saftigt gulerodsrugbrød med orange skær i krummen
featured: false
ingredients:
  - 350 g rugmel
  - 150 g hvedemel
  - 25 g frisk gær eller 8 g tørgær
  - 200 g revet gulerod (ca. 2 store)
  - 3 dl lunkent vand
  - 1 dl kærnemælk
  - 1½ tsk salt
  - 2 spsk mørk sirup
  - 50 g solsikkekerner
steps:
  - Riv gulerødderne fint. Pres ikke saften fra — den er hydrering.
  - Rør gær ud i vand og kærnemælk med sirup. Tilsæt salt, mel, gulerod og kerner. Ælt 8 minutter.
  - Hæv 2 timer.
  - Fyld i smurt form. Efterhæv 45–60 minutter.
  - Bag ved 180 °C i 70–75 minutter. Køl på rist mindst 4 timer.
faq:
  - question: Bliver det sødt?
    answer: Let. Gulerod og sirup. Det er stadig madbrød, ikke kage.
  - question: For våd dej?
    answer: Gulerødder varierer. Tilføj 1–2 spsk mel, hvis den ikke kan formes i formen.
  - question: Kan man bruge pastinak?
    answer: Ja. Samme vægt. Lidt mere jordagtig smag.
  - question: Holdbarhed?
    answer: Ofte 5–6 dage — guleroden holder krummen blød.
body: |
  Gulerodsrugbrød er fugt-hacket: revet rod i dejen, sødme uden sukkerbombe.

  Pres ikke guleroden. Saften er pointen.
tip: Riv fint. Grove strimler giver huller og ujævn bagning.
=====
title: Rugbrød med kartoffel
slug: kartoffel-rugbroed
category: ovn
description: Rugbrød med kogte, mosede kartofler i dejen — ekstra blød krumme og en helt særlig saftighed.
prepTime: PT40M
cookTime: PT1H15M
totalTime: PT5H
servings: 12
difficulty: mellem
tags:
  - rugbrød
  - kartoffel
  - blød
  - brød
  - ovn
imageAlt: Blødt kartoffel-rugbrød skåret på bræt
featured: false
ingredients:
  - 200 g kogte mealy kartofler, mosede (afkølede)
  - 350 g rugmel
  - 150 g hvedemel
  - 25 g frisk gær eller 8 g tørgær
  - 2½ dl lunkent vand (start — justér)
  - 1½ tsk salt
  - 1 spsk mørk sirup
  - 50 g hørfrø eller solsikkekerner
steps:
  - Kog kartofler uden salt. Mos fint uden mælk eller smør. Køl til lunkent.
  - Rør gær ud i vand med sirup. Tilsæt kartoffelmos, salt, mel og kerner. Ælt 8–10 minutter. Dejen er blød — tilsæt mel eller vand efter behov.
  - Hæv 2–2½ time.
  - Fyld i smurt form. Efterhæv 45–60 minutter.
  - Bag ved 180 °C i 70–75 minutter. Køl på rist mindst 4 timer.
faq:
  - question: Hvilke kartofler?
    answer: Mealy (bage-/moskartoffel). Faste kartofler giver gummi.
  - question: Rå kartoffel?
    answer: Nej. Kogt og moset. Rå giver hårde klumper.
  - question: Hvorfor blødere?
    answer: Stivelse og fugt fra kartoffel. Krummen holder længere.
  - question: Salt i kogevandet?
    answer: Skip. Du salter dejen. Dobbelt salt bliver skarpt.
body: |
  Kartoffel i rug er den bløde krumme: kogt mos, ikke rå riv.

  Det føles næsten som toast-brød — men det er stadig rug.
tip: Vej kartoffelmosen. For meget, og dejen aldrig sætter sig.
=====
title: Rugbrødschips med flagesalt i airfryer
slug: rugbroedschips-airfryer
category: airfryer
description: Rugbrødschips i airfryer — tynde skiver penslet med olie og flagesalt, sprøde på få minutter.
prepTime: PT8M
cookTime: PT8M
totalTime: PT20M
servings: 4
difficulty: nem
tags:
  - rugbrødschips
  - rugbrød
  - airfryer
  - snack
  - rester
  - flagesalt
imageAlt: Sprøde rugbrødschips med flagesalt fra airfryeren
featured: false
ingredients:
  - 8 tynde skiver gammelt rugbrød
  - 2 spsk olivenolie
  - 1 tsk flagesalt
  - Valgfrit: karve, hvidløgspulver, porreaske-salt
steps:
  - Skær rugbrødet 2–3 mm tykt. Pensl begge sider let med olie.
  - Læg i ét lag i airfryer-kurven. Drys flagesalt.
  - Steg ved 160 °C i 6–8 minutter. Ryst eller vend halvvejs.
  - De skal være tørre og knasende. Køl på rist — de sprøder videre.
  - Server til ost, dip eller øl.
faq:
  - question: Frisk brød?
    answer: Det damper. Brug 1–2 dage gammelt, eller tør skiverne 2 minutter først.
  - question: Ovn i stedet?
    answer: Ja — se hjemmelavede rugbrødschips i ovn. 170 °C i 12–18 minutter.
  - question: Seje chips?
    answer: For tykke skiver eller for kort tid. Ét lag. Køl åbent.
  - question: Mere smag?
    answer: Karve, røget paprika eller porreaske-salt. Salt først — krydderi bagefter, hvis det brænder.
body: |
  Rugbrødschips i airfryer er resten på turbo: tynde skiver, olie, flagesalt, få minutter.

  Ikke ovn. Ikke ventetid. Bare knas.
tip: Overfyld ikke kurven. To hold er bedre end dampende stak.
=====
title: Ristet rugbrødsdrys
slug: rugbroedsdrys
category: pande
description: Ristet rugbrødsdrys — smørstegt, sprødt crumble af gammelt rugbrød til ymer, supper og æblekage.
prepTime: PT5M
cookTime: PT8M
totalTime: PT15M
servings: 6
difficulty: nem
tags:
  - rugbrød
  - drys
  - crumble
  - rester
  - pande
  - øllebrød
imageAlt: Gyldent ristet rugbrødsdrys i skål
featured: false
ingredients:
  - 4 skiver gammelt rugbrød
  - 2 spsk smør
  - 1 knivspids flagesalt
  - Valgfrit: ½ tsk sukker, stødt kanel
steps:
  - Smuldr rugbrødet groft mellem hænderne — ikke pulver, ikke hele skiver.
  - Smelt smør på middel-lav varme i pande. Kom brødet i.
  - Rør jævnligt 5–8 minutter, til det er gyldent og knasende. Salt til sidst.
  - Til sødt: sukker og kanel det sidste minut.
  - Køl på bakke. Opbevar lufttæt op til en uge.
faq:
  - question: Til hvad?
    answer: Ymer, øllebrød, græskarsuppe, æblekage, bagte æbler. Eller bare i hånden.
  - question: Olie i stedet for smør?
    answer: Ja. Smør smager bedre. Olie er neutral.
  - question: Airfryer?
    answer: 160 °C i 4–6 minutter, ryst ofte. Mindre smørsmag.
  - question: Brændt?
    answer: Lav varme. Rug går fra gylden til bitter hurtigt.
body: |
  Rugbrødsdrys er øllebrøds-crumble uden grøden: smør, pande, knas.

  Det er resten, der redder morgenmaden.
tip: Grov smuld. Fint pulver bliver til mudder i smørret.
=====
title: Klassisk øllebrød med flødeskum
slug: oellebroed
category: gryde
description: Klassisk øllebrød med flødeskum — tørt rugbrød kogt op med hvidtøl, sukker og citronskal. Den ultimative restemad i kolde måneder.
prepTime: PT10M
cookTime: PT25M
totalTime: PT40M
servings: 4
difficulty: nem
tags:
  - øllebrød
  - rugbrød
  - hvidtøl
  - dansk klassiker
  - dessert
  - gryde
imageAlt: Klassisk øllebrød i skål med flødeskum
featured: true
ingredients:
  - 300 g tørt rugbrød, brudt i stykker
  - 75 cl hvidtøl (eller ½ hvidtøl og ½ vand)
  - 2–3 spsk sukker
  - Skal af ½ citron (uden hvidt)
  - 1 kanelstang eller ½ tsk stødt kanel
  - 1–2 dl piskefløde til piskning
  - Valgfrit: appelsinskal, rosiner, rugbrødsdrys
steps:
  - Læg rugbrød i gryde. Hæld hvidtøl over, så det dækker. Låd trække 10 minutter.
  - Tilsæt sukker, citronskal og kanel. Bring langsomt i kog under omrøring.
  - Simre 15–20 minutter på lav varme, til det er en tyk, glat grød. Rør ofte, så det ikke brænder.
  - Smag til — mere sukker hvis det er surt, mere væske hvis det er for tykt. Fjern kanelstang.
  - Pisk fløden til blødt skum. Server øllebrødet lunkent eller køligt med flødeskum og evt. rugbrødsdrys.
faq:
  - question: Hvilken øl?
    answer: Hvidtøl. Mørk porter bliver for bitter. Uden hvidtøl: æblejuice + vand 1:1 og ekstra citron.
  - question: Frisk rugbrød?
    answer: Det bliver slatten. Tørt er pointen. Tør skiver i ovnen 10 minutter ved 150 °C, hvis brødet er friskt.
  - question: Blender?
    answer: Ja, til sidst for ekstra glat. Klassisk er rustik med ske.
  - question: Kan det laves dagen før?
    answer: Ja. Køl. Varm forsigtigt op med lidt væske. Flødeskum først ved servering.
body: |
  Øllebrød er resternes hævn: tørt rug, hvidtøl, sukker, flødeskum.

  Det er ikke fancy. Det er november i en skål.
tip: For tykt? Mere hvidtøl. For tyndt? Simre videre uden låg.
=====
'''


def parse_block(block: str) -> dict:
    data: dict = {"tags": [], "ingredients": [], "steps": [], "faq": []}
    mode = None
    body_lines: list[str] = []
    current_q = ""
    i = 0
    lines = block.strip().splitlines()
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
        elif line.startswith("imageAlt: "):
            data["imageAlt"] = line[10:]
        elif line.startswith("featured: "):
            data["featured"] = line[10:]
        elif line == "tags:":
            mode = "tags"
        elif line == "ingredients:":
            mode = "ingredients"
        elif line == "steps:":
            mode = "steps"
        elif line == "faq:":
            mode = "faq"
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
    featured = "featured: true\n" if d.get("featured") == "true" else "featured: false\n"
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


def main() -> None:
    blocks = [b for b in RECIPES.split("=====") if b.strip()]
    written: list[tuple[str, str]] = []
    for b in blocks:
        d = parse_block(b)
        if not d.get("ingredients"):
            continue
        assert d.get("faq") and len(d["faq"]) >= 3, d.get("slug")
        assert d.get("tip"), d.get("slug")
        out = RECIPES_DIR / d["category"]
        out.mkdir(parents=True, exist_ok=True)
        path = out / f"{d['slug']}.mdx"
        if path.exists():
            raise SystemExit(f"slug collision: {path}")
        path.write_text(to_mdx(d), encoding="utf-8")
        written.append((d["category"], d["slug"]))
        print("wrote", f"{d['category']}/{path.name}")

    for cat, slug in written:
        dest = PUBLIC / cat / f"{slug}.jpg"
        dest.parent.mkdir(parents=True, exist_ok=True)
        src = IMG_MAP.get(slug)
        if src is None or not src.exists():
            raise SystemExit(f"missing image source for {slug}: {src}")
        shutil.copyfile(src, dest)
        print("img", dest.relative_to(ROOT))

    print(f"done: {len(written)} recipes")


if __name__ == "__main__":
    main()
