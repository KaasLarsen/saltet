#!/usr/bin/env python3
"""25 manglende airfryer-opskrifter (content gaps, okt 2026)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"

RECIPES = r'''
=====
title: Hakkebøffer med bløde løg i airfryer
slug: hakkeboeffer-bloede-loeg
category: airfryer
description: Saftige hakkebøffer i airfryer med bløde, karamelliserede løg — klassisk pande-ret uden pande.
prepTime: PT20M
cookTime: PT25M
totalTime: PT45M
servings: 4
difficulty: nem
tags:
  - hakkebøffer
  - bløde løg
  - hakket kød
  - oksekød
  - hverdag
  - klassisk
  - airfryer
imageAlt: Hakkebøffer med bløde karamelliserede løg på mørk tallerken
featured: true
ingredients:
  - 500 g hakket oksekød (10–12 % fedt)
  - 1 æg
  - 1 spsk hvedemel eller rasp
  - 1 tsk salt + ½ tsk peber
  - ½ tsk paprika
  - 3 store gule løg, i tynde skiver
  - 1 spsk smør + 1 spsk olie til løgene
  - 1 tsk sukker (valgfrit, til karamelisering)
  - Olie-spray til bøfferne
steps:
  - Bland hakket kød, æg, mel, salt, peber og paprika let. Form 4 tykke bøffer med en fordybning i midten.
  - Læg løgskiver i et ovnfast fad eller airfryer-bakke med smør, olie, sukker og en knivspids salt. Airfry 180 °C i 12–14 minutter. Rør halvvejs, til løgene er bløde og gyldne.
  - Flyt løgene til siden. Spray bøfferne med olie. Forvarm til 190 °C.
  - Steg bøfferne 7 minutter. Vend. Steg 5–7 minutter mere til 70–72 °C (eller ca. 65 °C for mere rosa).
  - Læg bløde løg ovenpå eller ved siden af. Hvile 3 minutter. Server med kartoffelmos eller [pommes frites](/opskrifter/airfryer/sproede-pomfritter).
faq:
  - question: Forskel på almindelige hakkebøffer?
    answer: Her er løgene hovedrollen — bløde og søde, ikke bare et valgfrit tilbehør. Se også [klassiske hakkebøffer](/opskrifter/airfryer/hakkeboeffer).
  - question: Kan løgene laves på pande?
    answer: Ja, men airfryeren klarer dem uden at du står over panden. Rør bare halvvejs.
  - question: Hvorfor er bøfferne tørre?
    answer: For magert kød eller for lang tid. Brug 10–12 % fedt og mål med termometer.
  - question: Brun sovs?
    answer: Klassisk. Lav den på pande mens kødet hviler — eller server med sennep og de bløde løg alene.
body: |
  Hakkebøffer med bløde løg er den danske klassiker, der normalt kræver to pander. Airfryeren klarer begge dele.

  Først løgene, til de er bløde og søde. Så bøfferne oveni — eller i næste runde, hvis kurven er lille.

  Det er hverdagsmad med stegeskorpe og uden sprøjtende fedt over komfuret.
tip: Læg løgene i bunden af et lille fad under bøfferne de sidste 5 minutter — saften drypper ned og smager endnu mere af bøf.
=====
title: Ribbenssteg-slider i airfryer
slug: ribbenssteg-slider
category: airfryer
description: Ribbenssteg-slider i airfryer — saftig ribbenssteg med sprød skorpe i mini-boller, lavet fra bunden.
prepTime: PT25M
cookTime: PT55M
totalTime: PT1H20M
servings: 6
difficulty: mellem
tags:
  - ribbenssteg
  - slider
  - sandwich
  - svinekød
  - festmad
  - airfryer
  - street food
imageAlt: Mini-sliders med ribbenssteg, remoulade og syltede agurker
featured: true
ingredients:
  - 1–1,2 kg ribbenssteg (uden svær, eller med hvis du vil have knas)
  - 2 tsk salt + 1 tsk peber
  - 1 tsk paprika + 1 tsk hvidløgspulver
  - 8–10 mini-boller eller slider-boller
  - 4 spsk remoulade eller sennep
  - 1 glas [syltede agurker](/opskrifter/sylte/syltede-agurker)
  - Valgfrit: rødkål, brun sovs til dyp
steps:
  - Dup stegen tør. Gnid med salt, peber, paprika og hvidløgspulver. Lad stå 15 minutter ved stuetemperatur.
  - Forvarm airfryeren til 180 °C. Læg stegen i kurven. Steg 25 minutter.
  - Skru op til 200 °C i 15–20 minutter, til kernen er 65–68 °C. Hvile 10 minutter under folie.
  - Skær tynde skiver på tværs af fibrene. Rist bollerne 2 minutter i den varme kurv.
  - Smør remoulade. Læg kød, agurk og evt. rødkål. Spis varme — det er pointen med en slider.
faq:
  - question: Ribbenssteg eller flæskesteg?
    answer: Ribbenssteg er mere marmorering og mindre «søndagssteg-svær». Vil du have klassisk flæskestegssandwich, se [flæskestegssandwich](/opskrifter/airfryer/flaeskestegssandwich).
  - question: Kan jeg bruge rester?
    answer: Ja. Varm skiver 4–5 minutter ved 180 °C og saml sliderne med det samme.
  - question: Hvilke boller?
    answer: Bløde mini-burgerboller eller brioche-sliders. For hårde boller knækker oplevelsen.
  - question: Med svær?
    answer: Muligt, men sværen skal riddes og tørres som på [flæskesteg](/opskrifter/airfryer/flaeskesteg). Ellers skip sværen og gå efter saftigt kød.
body: |
  Ribbenssteg-slider er street food fra airfryeren: stegen steges hele, skæres tyndt, stables i mini-boller.

  Ingen ovn. Ingen buffet-bakke. Bare kerntemperatur og bløde boller.

  Remoulade og syltede agurker er ikke valgfrit — de skærer fedtet.
tip: Skær stegen lidt på skrå, så skiverne fylder bollerne uden at falde ud. Tynde skiver > tykke klumper.
=====
title: Kyllingenuggets med cornflakes-panering
slug: kyllingenuggets-cornflakes
category: airfryer
description: Hjemmelavede kyllingenuggets med cornflakes-panering i airfryer — ekstra grov sprødhed uden friture.
prepTime: PT25M
cookTime: PT14M
totalTime: PT40M
servings: 4
difficulty: nem
tags:
  - nuggets
  - kylling
  - cornflakes
  - panering
  - børn
  - protein
  - airfryer
imageAlt: Sprøde kyllingenuggets med cornflakes-panering og dip
featured: true
ingredients:
  - 500 g kyllingebryst, i 3 cm stykker
  - 1 dl hvedemel
  - 2 æg, pisket
  - 100 g cornflakes, knust groft (ikke til pulver)
  - 1 tsk paprika + 1 tsk hvidløgspulver + salt + peber
  - Olie-spray
  - Dip: ketchup, mayo eller BBQ
steps:
  - Krydr kyllingen med salt, peber, paprika og hvidløgspulver.
  - Knus cornflakes i en pose — grove stykker giver den rigtige knas. Bland evt. 2 spsk rasp i, hvis de er for store.
  - Vend stykkerne i mel, æg og cornflakes. Tryk paneringen fast. Hvile 5 minutter.
  - Forvarm til 200 °C. Spray nuggets let med olie. Ét lag i kurven.
  - Steg 6 minutter. Vend. 5–7 minutter mere, til gyldne og 74 °C i midten. Server med det samme.
faq:
  - question: Panko eller cornflakes?
    answer: Cornflakes er grovere og sødere. Til klassisk panko-nuggets se [hjemmelavede kyllingenuggets](/opskrifter/airfryer/hjemmelavede-kyllingenuggets). Frosne? Se [kyllingenuggets](/opskrifter/airfryer/kyllingenuggets).
  - question: Cornflakes bliver brændte?
    answer: For høj varme eller for fin knusning. Hold 200 °C, grove stykker, og spray olie — det beskytter.
  - question: Kan man bruge lår?
    answer: Ja. Skær af benet, samme panering. Giv 1–2 minutter ekstra.
  - question: Glutenfri?
    answer: Brug glutenfri cornflakes og majsstivelse i stedet for hvedemel.
body: |
  Cornflakes-nuggets er den grove, knasende version — ikke den fine panko-skorpe.

  Knus ikke til mel. Du vil have flager, der knækker mellem tænderne.

  Airfryeren giver farve uden oliebad. Dip er obligatorisk.
tip: Spray olien efter første vend — paneringen sætter sig bedre, og cornflakesene bliver dybere gyldne.
=====
title: Pulled pork i airfryer
slug: pulled-pork
category: airfryer
description: Pulled pork i airfryer — saftig nakkefilet med BBQ-rub, tilpasset den hurtigere tilberedningstid.
prepTime: PT20M
cookTime: PT1H30M
totalTime: PT1H50M
servings: 6
difficulty: mellem
tags:
  - pulled pork
  - svinekød
  - BBQ
  - festmad
  - airfryer
  - sandwich
imageAlt: Pulled pork trukket i tråde med BBQ-sauce i skål
featured: true
ingredients:
  - 1–1,2 kg svinenakkefilet eller skulder uden ben
  - Rub: 2 spsk brunt sukker, 1 spsk paprika, 1 tsk røget paprika, 1 tsk salt, 1 tsk peber, 1 tsk hvidløgspulver, ½ tsk spidskommen
  - 1 dl æblecidereddike eller æblejuice
  - 2 dl BBQ-sauce
  - Valgfrit: burgerboller, coleslaw
steps:
  - Dup kødet tørt. Gnid rub ind overalt. Lad stå 20 minutter (eller natten over i køleskab).
  - Forvarm til 160 °C. Læg kødet i kurven. Steg 45 minutter.
  - Pensl med eddike/juice. Vend. Steg yderligere 35–45 minutter, til kernen er 90–93 °C og kødet giver efter for en gaffel.
  - Hvile 10 minutter. Træk i tråde med to gafler. Bland med BBQ-sauce — start med 1½ dl, smag til.
  - Server i boller eller ovenpå [loaded grovfritter](/opskrifter/airfryer/loaded-grovfritter-pulled-pork).
faq:
  - question: Er airfryer hurtigere end ovn?
    answer: Ja — mindre kabine, mere cirkulation. Du sparer typisk 30–60 minutter vs. lav ovnstegning, men det er stadig en langsommerekodning.
  - question: Skulder eller nakke?
    answer: Begge virker. Nakke er ofte mere marmorering i danske udskæringer. Undgå magert mørbrad — det bliver tørt.
  - question: Kan det laves dagen før?
    answer: Ja. Køl i saucen. Varm 8–10 minutter ved 160 °C med lidt ekstra BBQ.
  - question: For tørt?
    answer: For lav sluttemperatur eller for magert stykke. Gå efter 90 °C+, og gem saucen til sidst — ikke undervejs i store mængder.
body: |
  Pulled pork i airfryer er ikke 12-timers røg. Det er den hurtige, hjemlige version med rub, tålmodighed og BBQ.

  Lav temperatur først. Høj kerne til sidst. Træk, sauce, spis.

  Resten er boller, coleslaw og eventuelle [loaded fritter](/opskrifter/airfryer/loaded-grovfritter-pulled-pork).
tip: Pak kødet løst i folie de sidste 20 minutter, hvis det begynder at tørre på overfladen — saften bliver indenfor, skorpen kan stadig sætte sig.
=====
title: Fyldte kyllingebryster med spinat og feta
slug: fyldte-kyllingebryster-spinat-feta
category: airfryer
description: Hele fyldte kyllingebryster med spinat og feta i airfryer — saftig midte og gylden overflade.
prepTime: PT20M
cookTime: PT22M
totalTime: PT42M
servings: 4
difficulty: mellem
tags:
  - kylling
  - kyllingebryst
  - spinat
  - feta
  - fyldt
  - protein
  - airfryer
imageAlt: Fyldte kyllingebryster med spinat og feta skåret op
featured: true
ingredients:
  - 4 hele kyllingebryster (ca. 150–180 g hver)
  - 150 g frisk spinat, hakket
  - 100 g feta, smuldret
  - 1 fed hvidløg, presset
  - 1 spsk olivenolie + salt + peber
  - 1 tsk oregano eller basilikum
  - Tandstikker eller kødsnor
  - Olie-spray
steps:
  - Svits spinat 1–2 minutter på pande eller 2 minutter i airfryer ved 180 °C i et fad, til den synker. Køl. Bland med feta, hvidløg, olie, oregano, salt og peber.
  - Skær en lomme i siden af hvert bryst. Fyld med spinat-feta. Luk med tandstikker. Krydr ydersiden med salt og peber. Spray olie.
  - Forvarm til 180 °C. Læg brysterne i ét lag.
  - Steg 18–22 minutter, vend halvvejs, til kernen er 74 °C. Hvile 5 minutter. Fjern tandstikker før servering.
faq:
  - question: Kan man bruge frossen spinat?
    answer: Ja — tø op og pres al væske ud. Våd fyld gør brystet vandigt.
  - question: Ost i stedet for feta?
    answer: Creme fraiche-ost eller mozzarella virker. Feta giver den salte kant.
  - question: For tørt kyllingebryst?
    answer: Overstegning. Mål 74 °C og træk dem ud. Tynde bryster er færdige før tykke.
  - question: Kan de forberedes?
    answer: Fyld og luk om morgenen. Steg lige før servering.
body: |
  Fyldte kyllingebryster lyder fancy. Det er en lomme, spinat, feta og termometer.

  Airfryeren giver farve uden tør ovnlugt. Midten skal være saftig — ikke grå og kedelig.

  Server med salat, ris eller [bagekartofler](/opskrifter/airfryer/bagekartofler).
tip: Bind ikke for stramt. Fyldet skal kunne udvide sig lidt — ellers presses det ud i kurven.
=====
title: Indbagt laks i butterdej
slug: indbagt-laks-butterdej
category: airfryer
description: Indbagt laks i butterdej (salmon en croûte) i airfryer — sprød dej og saftig laks uden stor ovn.
prepTime: PT25M
cookTime: PT22M
totalTime: PT47M
servings: 4
difficulty: mellem
tags:
  - laks
  - fisk
  - butterdej
  - festmad
  - airfryer
  - indbagt
imageAlt: Indbagt laks i gylden butterdej skåret så den rosa midte ses
featured: true
ingredients:
  - 500–600 g laksefilet uden skind, i ét stykke eller 4 portioner
  - 1 rulle butterdej (ca. 250 g)
  - 100 g frisk spinat eller 2 spsk pesto
  - 1 spsk dijonsennep
  - Salt, peber, citronsaft
  - 1 æg til pensling
steps:
  - Dup laksen tør. Krydr med salt, peber og citron. Pensl med sennep. Læg spinat eller pesto ovenpå.
  - Rul butterdej ud. Læg laks midt på. Fold dejen tæt omkring — samling nedad. Skær væk overflødig dej. Ridsk forsigtigt et mønster ovenpå. Pensl med æg.
  - Forvarm til 180 °C. Læg pakkerne på bagepapir i kurven med plads imellem.
  - Steg 18–22 minutter, til dejen er dybt gylden og laksen er ca. 50–52 °C i midten (stadig saftig). Hvile 3 minutter.
faq:
  - question: Bliver bunden soggy?
    answer: For våd fyld eller for lav varme. Dup laksen knastør, og brug ikke for meget pesto. Evt. forbag dejen 3 minutter.
  - question: Hel filet eller portioner?
    answer: Portioner er nemmere i airfryer. Hel filet kræver stor kurv og jævn tykkelse.
  - question: Kan man bruge torsk?
    answer: Ja, men torsk er magrere — pensl med lidt olie indeni, og mål 55–58 °C.
  - question: Færdigdej eller hjemmelavet?
    answer: Købe-butterdej er pointen her. Den bliver sprød nok i airfryeren.
body: |
  Salmon en croûte i airfryer er festmad uden ovn-opvarmning i 20 minutter.

  Tør laks. Tæt fold. Æggeglasur. Gylden skorpe.

  Skær ved bordet, så dampen og den rosa midte gør arbejdet.
tip: Læg et stykke bagepapir under — butterdej drypper smør, og du vil ikke have røg i lejligheden.
=====
title: Airfryer-skaldyr med hvidløgssmør
slug: skaldyr-hvidloegssmoer
category: airfryer
description: Blandede skaldyr i airfryer med hvidløgssmør — rejer, blæksprutteringe og muslinger på få minutter.
prepTime: PT15M
cookTime: PT10M
totalTime: PT25M
servings: 4
difficulty: nem
tags:
  - skaldyr
  - rejer
  - blæksprutte
  - muslinger
  - hvidløg
  - airfryer
  - hurtig
imageAlt: Blandede skaldyr vendt i hvidløgssmør i skål
featured: true
ingredients:
  - 200 g store rejer, pillede (gerne med hale)
  - 200 g blæksprutteringe (friske eller tøede)
  - 200 g muslinger, rensede (eller 150 g uden skal)
  - 50 g smør, smeltet
  - 3 fed hvidløg, presset
  - 1 spsk citronsaft + 1 spsk hakkede persille
  - Salt, peber, chili (valgfrit)
  - Brød til at dyppe
steps:
  - Dup alle skaldyr godt tørre — væske damper i stedet for at stege.
  - Bland smør, hvidløg, citron, salt, peber og chili. Vend skaldyrene i halvdelen af smørret.
  - Forvarm til 200 °C. Læg i ét lag (gerne i et lavt fad). Steg 4 minutter.
  - Ryst/rør. Tilsæt resten af smørret. Steg 3–5 minutter mere, til rejerne er lyserøde og blæksprutten er mør. Muslinger skal være åbne — smid lukkede ud.
  - Drys persille på. Server med det samme med brød.
faq:
  - question: Frosne skaldyr?
    answer: Tø helt op i køleskab og dup knastørre. Ellers bliver det en dampgryde.
  - question: Kun rejer?
    answer: Ja — se også [hvidløgsmarinerede kæmperejer](/opskrifter/airfryer/hvidloegsmarinerede-kaemperejer). Blandingen er bare mere fest.
  - question: Blæksprutten bliver gummi?
    answer: For lang tid. Hold den under 8–9 minutter total, eller meget længere (20+ min) til den bliver mør igen — midterzonen er fjenden.
  - question: Muslinger i airfryer — sikkert?
    answer: Kun friske, levende muslinger. De skal åbne sig. Lugter de af ammoniak, smid dem.
body: |
  Blandede skaldyr med hvidløgssmør er tapas-tempo: varm kurv, kort tid, masser af smør.

  Tørhed er hemmeligheden. Våde skaldyr damper. Tørre skaldyr steger.

  Brød er ikke tilbehør — det er redskab.
tip: Brug et lille ovnfast fad i kurven, så smørret samles i bunden i stedet for at dryppe gennem hullerne.
=====
title: Fiskefrikadeller i airfryer
slug: fiskefrikadeller
category: airfryer
description: Fiskefrikadeller i airfryer — saftige, sprøde uden fedtstegning, klassisk dansk fiskefars.
prepTime: PT20M
cookTime: PT14M
totalTime: PT34M
servings: 4
difficulty: nem
tags:
  - fiskefrikadeller
  - fisk
  - frikadeller
  - hverdag
  - børn
  - airfryer
imageAlt: Gyldne fiskefrikadeller fra airfryer med remoulade
featured: true
ingredients:
  - 500 g hvid fiskefars (torsk, sej eller købt fiskefars)
  - 1 æg
  - 1 dl havregryn eller rasp
  - 1 lille løg, meget fint hakket
  - 1 spsk hakket dild
  - 1 tsk salt + peber
  - 1 spsk creme fraiche eller mælk
  - Olie-spray
  - Remoulade og citron til servering
steps:
  - Bland fars, æg, havregryn, løg, dild, salt, peber og creme fraiche. Lad hvile 10 minutter.
  - Form 8–10 flade frikadeller med våde hænder. Spray begge sider med olie.
  - Forvarm til 190 °C. Læg i ét lag med plads imellem.
  - Steg 7 minutter. Vend. Steg 5–7 minutter mere, til de er gyldne og faste (ca. 70 °C i midten).
  - Server med remoulade, citron og rugbrød eller kartofler.
faq:
  - question: Købt fars eller hakket fisk?
    answer: Begge. Købt er nemmest. Hakket torsk skal være kold og gerne kørt to gange for binding.
  - question: Hvorfor falder de fra hinanden?
    answer: For våd fars eller for lidt binding. Tilføj en spsk rasp, og køl farsen 15 minutter.
  - question: Samme tid som kødfrikadeller?
    answer: Lidt kortere — fisk er færdig før oksekød. Se også [frikadeller](/opskrifter/airfryer/frikadeller).
  - question: Kan de fryses?
    answer: Ja, rå eller stegte. Steg fra fryser ved 180 °C i 12–14 minutter.
body: |
  Fiskefrikadeller i airfryer er den fedtfrie genvej til klassisk dansk fiskemiddag.

  Kold fars. Våde hænder. Olie-spray. Vend halvvejs.

  Remoulade er ikke til forhandling.
tip: Gør dem fladere end kødfrikadeller — fiskefars er mørere og gennemsteger mere jævnt, når de ikke er kuglerunde.
=====
title: Tunmelt-sandwich i airfryer
slug: tunmelt-sandwich
category: airfryer
description: Tunmelt-sandwich i airfryer — luksusudgaven med masser af smeltet ost og cremet tunsalat.
prepTime: PT10M
cookTime: PT8M
totalTime: PT18M
servings: 2
difficulty: nem
tags:
  - tun
  - sandwich
  - ost
  - fisk
  - frokost
  - hurtig
  - airfryer
imageAlt: Tunmelt-sandwich med smeltet ost og gylden skorpe
featured: true
ingredients:
  - 1 dåse tun i vand eller olie (ca. 140 g drænet)
  - 2 spsk mayonnaise
  - 1 tsk dijonsennep
  - 1 spsk finthakket rødløg eller forårsløg
  - Salt, peber, citronsaft
  - 4 skiver godt brød
  - 4 skiver cheddar eller mozzarella
  - Smør til ydersiden
steps:
  - Bland tun, mayo, sennep, løg, salt, peber og citron.
  - Smør ydersiden af brødskiverne. Læg ost, tunfyld, mere ost, luk sandwich.
  - Forvarm til 180 °C. Læg sandwichene i kurven. Evt. vægt med en rist eller let folie, så de ikke folder op.
  - Steg 4 minutter. Vend. Steg 3–4 minutter mere, til osten er smeltet og brødet gyldent.
  - Skær diagonalt. Spis med det samme — smeltet ost venter ikke.
faq:
  - question: Hvilken ost?
    answer: Cheddar smelter og smager. Mozzarella er mildere. Emmentaler virker også. Brug hellere for meget end for lidt — det er luksusudgaven.
  - question: Tun i olie eller vand?
    answer: Begge. Olie giver mere smag; vand er lettere. Dup godt drænet uanset.
  - question: Kan man bruge tortilla?
    answer: Ja — fold som quesadilla, samme temperatur, 5–6 minutter.
  - question: Bliver brødet tørt?
    answer: Smør ydersiden. Uden fedt bliver det knastørt i stedet for toastet.
body: |
  Tunmelt er den amerikanske diner-sandwich på dansk frokosttid.

  Dobbelt ost. Cremet tun. Airfryer i stedet for grilljern.

  Det skal dryppe. Ellers har du sparet forkert.
tip: Læg et stykke bagepapir under — ost der flyder er godt i sandwich, mindre godt i bunden af kurven.
=====
title: Fyldte portobellosvampe med gedeost og valnødder
slug: fyldte-portobello-gedeost-valnoedder
category: airfryer
description: Fyldte portobellosvampe med gratineret gedeost og valnødder i airfryer — vegetarisk festmad på 15 minutter.
prepTime: PT10M
cookTime: PT12M
totalTime: PT22M
servings: 4
difficulty: nem
tags:
  - portobello
  - gedeost
  - valnødder
  - vegetar
  - svampe
  - festmad
  - airfryer
imageAlt: Portobellosvampe fyldt med gratineret gedeost og valnødder
featured: true
ingredients:
  - 4 store portobellosvampe
  - 120 g gedeost (chevre), i skiver eller smuldret
  - 40 g valnødder, groft hakket
  - 1 spsk honning
  - 1 spsk olivenolie
  - Frisk timian eller rosmarin
  - Salt, peber
  - Valgfrit: rucola til servering
steps:
  - Skrab lamellerne forsigtigt ud. Dup hattene tørre. Pensl med olie, salt og peber.
  - Forsteg tomme hatte 3 minutter ved 180 °C (underside op). Hæld eventuelt væske fra.
  - Fyld med gedeost, valnødder og timian. Dryp honning over.
  - Airfry 8–10 minutter ved 180 °C, til osten er blød og gylden og nødderne dufter.
  - Server med rucola. Spis varme.
faq:
  - question: Forskel på pesto-portobello?
    answer: Den her er gedeost, honning og valnød — mere ostetapås. Til pesto og mozzarella se [pesto-portobello](/opskrifter/airfryer/pesto-portobello).
  - question: Hvorfor er de våde?
    answer: Svampe afgiver væske. Forstegning og tørring er ikke valgfrit.
  - question: Anden ost?
    answer: Blåskimmel eller brie virker. Gedeost er den klassiske sødt-saltede kombi med honning.
  - question: Kan nødderne brændes?
    answer: Læg dem under osten, eller tilsæt dem de sidste 3 minutter.
body: |
  Portobello, gedeost og valnødder er vegetarisk gratineringsmad med kant.

  Store hatte. Lidt forstegning. Ost og nødder ovenpå.

  Honning binder det hele sammen — bare en tynd tråd.
tip: Vælg hatte der er flade nok til at ligge stabilt. Dybe «skåle» holder mere ost, men drypper også mere.
=====
title: Helbagt blomkål med kryddersmør og parmesan
slug: helbagt-blomkaal-kryddersmoer
category: airfryer
description: Helbagt blomkål i airfryer med kryddersmør og parmesan — sprød skorpe og mør midte uden ovn.
prepTime: PT15M
cookTime: PT35M
totalTime: PT50M
servings: 4
difficulty: nem
tags:
  - blomkål
  - vegetar
  - parmesan
  - kryddersmør
  - tilbehør
  - airfryer
imageAlt: Helbagt blomkål med parmesanskorpe og kryddersmør
featured: true
ingredients:
  - 1 hel blomkål (ca. 800 g–1 kg), blade fjernet, stok kortet
  - 50 g smør, blødt
  - 2 fed hvidløg, presset
  - 1 tsk paprika + ½ tsk spidskommen + salt + peber
  - 40 g parmesan, revet
  - 1 spsk olivenolie
  - Citron og persille til servering
steps:
  - Bland smør, hvidløg, paprika, spidskommen, salt og peber. Pensl blomkålen grundigt — også ind mellem buketterne.
  - Forvarm til 170 °C. Læg blomkålen i kurven (skær i halve hvis den ikke kan være). Pensl med olie.
  - Steg 25 minutter. Pensl igen. Drys parmesan på.
  - Steg 8–12 minutter mere ved 190 °C, til den er mør indeni (kniv skal glide let) og skorpen er gylden.
  - Hvile 5 minutter. Skær i kiler. Dryp citron og persille over.
faq:
  - question: For stor til kurven?
    answer: Skær i to halvdele eller fire «steaks». Se også [blomkåls-steaks](/opskrifter/airfryer/blomkaals-steaks) til den flade version.
  - question: Skal den forkoges?
    answer: Nej. Airfryeren klarer den hele — bare giv tid nok ved 170 °C først.
  - question: Kan man skippe parmesan?
    answer: Ja. Kryddersmør alene er nok. Parmesan giver knas.
  - question: Rå midte?
    answer: For kort tid eller for høj varme for tidligt. Start lavt, finish højt.
body: |
  Helbagt blomkål er midtpunktet, ikke tilbehøret i baggrunden.

  Kryddersmør ind mellem buketterne. Parmesan til sidst. Knivtest.

  Det ser ud af mere, end det er — og det er præcis pointen.
tip: Prik stokken med en kniv før stegning, så varmen når midten hurtigere uden at ydersiden brænder.
=====
title: Sprøde løgringe i airfryer
slug: sproede-logrige
category: airfryer
description: Hjemmelavede sprøde løgringe i airfryer med panko — knasende uden frituregryde.
prepTime: PT20M
cookTime: PT12M
totalTime: PT32M
servings: 4
difficulty: nem
tags:
  - løgringe
  - snack
  - panko
  - vegetar
  - tilbehør
  - airfryer
  - festmad
imageAlt: Sprøde panerede løgringe fra airfryer med dip
featured: true
ingredients:
  - 2 store gule løg
  - 1 dl hvedemel
  - 2 æg, pisket
  - 1½ dl panko
  - 1 tsk paprika + ½ tsk salt + peber
  - Olie-spray
  - Dip: mayo, ketchup eller ranch
steps:
  - Skær løg i 1 cm skiver. Adskil til ringe. Smid de mindste kerner til anden brug.
  - Bland paprika i melet. Vend ringene i mel, æg og panko. Tryk paneringen fast.
  - Forvarm til 200 °C. Spray ringene med olie. Ét lag i kurven — gerne på en rist.
  - Steg 6 minutter. Vend forsigtigt. Spray igen. Steg 4–6 minutter mere, til dybt gyldne.
  - Salt let lige efter. Server med det samme.
faq:
  - question: Panko eller dejbatter?
    answer: Panko er nemmest i airfryer. Vil du have dej: bland 1 dl mel + 1 dl danskvand + salt, dyp, og spray ekstra olie.
  - question: Er porre-ringe det samme?
    answer: Nej — [porre-ringe](/opskrifter/airfryer/porre-ringe) er low-carb uden mel. De her er klassiske snack-løgringe.
  - question: Hvorfor falder paneringen af?
    answer: For våde løg eller for lidt tryk. Dup ringene, og lad dem hvile 5 minutter efter panering.
  - question: Kan de laves i forvejen?
    answer: Panér og køl. Steg lige før servering — de bliver slappe hvis de venter.
body: |
  Sprøde løgringe er pub-mad derhjemme — uden liter olie.

  Tykkelse betyder noget. For tynde brænder. For tykke bliver bløde i midten.

  Én centimeter. Panko. Olie-spray. Dip.
tip: Brug en airfryer-rist hvis du har — luften under ringene gør undersiden lige så sprød som toppen.
=====
title: Majsribs (corn ribs) i airfryer
slug: majsribs
category: airfryer
description: Virale majsribs (corn ribs) i airfryer — buede majsstænger med BBQ-krydderi og smør.
prepTime: PT15M
cookTime: PT15M
totalTime: PT30M
servings: 4
difficulty: mellem
tags:
  - majsribs
  - corn ribs
  - majs
  - BBQ
  - vegetar
  - snack
  - airfryer
  - viral
imageAlt: Buede majsribs med BBQ-krydderi på mørkt fad
featured: true
ingredients:
  - 2 hele majskolber
  - 2 spsk smeltet smør eller olie
  - 1 tsk røget paprika + 1 tsk paprika
  - ½ tsk hvidløgspulver + ½ tsk spidskommen
  - ½ tsk salt + peber
  - 1 tsk brunt sukker (valgfrit)
  - Lime og koriander til servering
steps:
  - Skær hver majskolbe på langs i 4 «ribs» — stil kolben oprejst og skær forsigtigt gennem kernen. Brug skarp kniv.
  - Bland smør og krydderier. Pensl majsen grundigt på alle sider.
  - Forvarm til 200 °C. Læg ribs i kurven med plads. Steg 12–15 minutter, vend halvvejs, til kanterne er gyldne og de buer.
  - Dryp lime over. Drys koriander. Spis med hænderne.
faq:
  - question: Hvorfor skære i fire?
    answer: Kernen trækker sig, så stykkerne buer som ribs. Halve kolber buer ikke på samme måde — se [majskolber med urtesmør](/opskrifter/airfryer/majskolber-urtesmoer).
  - question: Svært at skære?
    answer: Meget. Skær ikke mod dig selv. En tung kokkekniv og stabil kolbe. Alternativt: skær i trekanter fra siden.
  - question: Frossen majs?
    answer: Hellere frisk. Frosne kerner falder af. Hele frosne kolber skal tø først.
  - question: For tørre?
    answer: Mere smør før og efter. De skal glinse.
body: |
  Majsribs er den virale snack, der faktisk smager af noget — BBQ, smør, lime.

  Skæringen er det svære. Stegningen er det nemme.

  De skal bue. Ellers er det bare majsstænger.
tip: Pensl ekstra smør efter stegning — den varme majs suger det ind, og krydderierne klistrer bedre.
=====
title: Vegetariske falafel i airfryer
slug: falafel
category: airfryer
description: Sprøde vegetariske falafel i airfryer — knasende skal uden at blive tørre indeni.
prepTime: PT30M
cookTime: PT14M
totalTime: PT44M
servings: 4
difficulty: mellem
tags:
  - falafel
  - vegetar
  - kikærter
  - middle eastern
  - protein
  - airfryer
  - snack
imageAlt: Sprøde falafel fra airfryer med yoghurt-dip
featured: true
ingredients:
  - 250 g tørrede kikærter, udblødt natten over (ikke kogte)
  - 1 lille løg, groft hakket
  - 2 fed hvidløg
  - 1 dl frisk persille + ½ dl koriander
  - 1 tsk spidskommen + 1 tsk koriander + ½ tsk bagepulver
  - 1 tsk salt + peber + chili
  - 1–2 spsk mel hvis farsen er for våd
  - Olie-spray
  - Pitabrød, yoghurt og salat til servering
steps:
  - Dræn kikærterne. Kør dem med løg, hvidløg, urter og krydderier til en grov fars — ikke puré. Rør bagepulver i. Køl 20 minutter.
  - Form 16 små bollerne. Spray med olie.
  - Forvarm til 190 °C. Ét lag i kurven.
  - Steg 7 minutter. Vend. Spray igen. Steg 5–7 minutter mere, til dybt gyldne. De skal give efter let i midten — ikke knastørre.
  - Server i [pitabrød](/opskrifter/airfryer/pitabroed) med yoghurt og salat.
faq:
  - question: Hvorfor ikke kogte kikærter?
    answer: Kogte giver våd, melet falafel. Udblødte rå kikærter er klassikeren og holder formen.
  - question: Dåsekikærter?
    answer: Nødløsning. Dræn, tør grundigt, tilsæt ekstra mel — resultatet bliver blødere.
  - question: For tørre?
    answer: For høj varme eller for små. Hold 190 °C og lav dem på størrelse med en valnød.
  - question: Kan de fryses?
    answer: Ja, rå. Steg fra fryser ved 180 °C i 14–16 minutter.
body: |
  Falafel i airfryer skal knase udenpå og være urte-grøn indeni — ikke kugler af sand.

  Rå udblødte kikærter. Grov fars. Olie-spray.

  Pitabrød og yoghurt gør resten.
tip: Tilsæt bagepulver lige før formning — det giver let hævning og luftigere midte.
=====
title: Fyldte peberfrugter med mexicansk ris- og bønnefyld
slug: fyldte-peberfrugter-mexicansk
category: airfryer
description: Fyldte peberfrugter i airfryer med mexicansk ris, bønner og ost — vegetarisk aftensmad i én kurv.
prepTime: PT20M
cookTime: PT18M
totalTime: PT38M
servings: 4
difficulty: nem
tags:
  - peberfrugt
  - vegetar
  - mexicansk
  - bønner
  - ris
  - airfryer
  - hverdag
imageAlt: Fyldte peberfrugter med ris, bønner og smeltet ost
featured: true
ingredients:
  - 4 store peberfrugter (rød/gul), halveret på langs, kerner fjernet
  - 3 dl kogte ris (restemad er perfekt)
  - 1 dåse sorte bønner eller kidneybønner, drænet
  - 1 dl majs
  - 1 tsk spidskommen + 1 tsk paprika + ½ tsk chili
  - 100 g revet ost (cheddar eller mozzarella)
  - 2 spsk salsa eller hakket tomat
  - Salt, koriander, lime
steps:
  - Bland ris, bønner, majs, krydderier, salsa, halvdelen af osten, salt og koriander.
  - Pensl peberfrugterne let med olie. Fyld dem generøst.
  - Forvarm til 180 °C. Læg fyldte halvdele i kurven. Steg 12 minutter.
  - Drys resten af osten på. Steg 4–6 minutter mere, til osten er smeltet og peberfrugten er mør men holder formen.
  - Dryp lime over. Server med yoghurt eller ekstra salsa.
faq:
  - question: Skal peberfrugten forbages?
    answer: Ikke nødvendigt i airfryer — 180 °C giver blød væg uden at den kollapser.
  - question: Uden ris?
    answer: Brug quinoa, couscous eller ekstra bønner. Fyldet skal bare være forholdsvis tørt.
  - question: Med kød?
    answer: Tilsæt stegt hakket oksekød eller kylling i fyldet. Krydderierne er de samme.
  - question: For væltende?
    answer: Skær en tynd skive af undersiden, så de står plant — eller brug et fad i kurven.
body: |
  Fyldte peberfrugter er aftensmad der ser ud som om du har planlagt den.

  Rest-ris. Dåsebønner. Ost på toppen.

  Airfryeren smelter og blødgør uden at køkkenet bliver til sauna.
tip: Oversalt ikke fyldet — osten og salsaen bringer salt nok. Smag til før du fylder.
=====
title: Grydebrød / franskbrød i airfryer
slug: grydebrod
category: airfryer
description: Grydebrød og franskbrød i airfryer fra bunden — hel/stor form til 5–7 L kurv, sprød skorpe uden mini-version.
prepTime: PT2H
cookTime: PT35M
totalTime: PT2H35M
servings: 6
difficulty: mellem
tags:
  - grydebrød
  - franskbrød
  - brød
  - bagværk
  - hjemmebag
  - airfryer
imageAlt: Hel grydebrød med sprød skorpe bagt i airfryer
featured: true
ingredients:
  - 400 ml lunkent vand
  - 1 pose tørgær (12 g) eller 25 g frisk gær
  - 1 tsk sukker
  - 2 tsk salt
  - 550–600 g hvedemel
  - 1 spsk olivenolie
  - Ekstra mel til bordet
steps:
  - Rør gær ud i vandet med sukker. Tilsæt salt, olie og mel. Ælt 8–10 minutter til en blød, elastisk dej. Hæv tildækket 60–75 minutter.
  - Fold dejen sammen. Læg i en smurt form eller lille støbejernsgryde der passer i din 5–7 L airfryer. Efterhæv 25–30 minutter.
  - Ridsk toppen. Forvarm til 180 °C. Bag 25 minutter.
  - Skru op til 200 °C i 8–10 minutter for ekstra skorpe. Brødet er færdigt når det lyder hult, eller kernen er ca. 96–98 °C.
  - Vend ud. Køl mindst 30 minutter på rist før udskæring.
faq:
  - question: Forskel på mini-franskbrød?
    answer: Det her er den fulde dej og større form — ikke snack-størrelse. Til den lille version se [mini-franskbrød](/opskrifter/airfryer/mini-franskbrod).
  - question: Min kurv er under 5 L?
    answer: Del dejen i to. Bag ét brød ad gangen, eller brug to mindre forme.
  - question: Bund bleg?
    answer: Vend brødet forsigtigt ud af formen de sidste 5 minutter, eller bag direkte på en rist-indsats.
  - question: Kan jeg bruge surdej?
    answer: Ja — erstat gæren med 100 g aktiv starter og forlæng hævningen. Bagetiden er den samme.
body: |
  Grydebrød i airfryer er rigtigt brød — ikke en mini-kopi til én sandwich.

  Stor form. Fuld hævning. Høj finish-temperatur til skorpen.

  Du skal høre det hule dunk, før du skærer.
tip: Stil en lille skål med vand i kurven de første 10 minutter, hvis din model tillader det — damp giver mere sprød skorpe.
=====
title: Pølsehorn af hjemmelavet gærdej
slug: poelsehorn-gaerdej
category: airfryer
description: Pølsehorn med hjemmelavet gærdej i airfryer — bløde, gyldne horn uden færdigdej.
prepTime: PT1H30M
cookTime: PT14M
totalTime: PT1H44M
servings: 8
difficulty: mellem
tags:
  - pølsehorn
  - gærdej
  - bagværk
  - børn
  - party
  - airfryer
imageAlt: Gyldne pølsehorn af hjemmelavet gærdej fra airfryer
featured: true
ingredients:
  - 2½ dl lunkent mælk
  - 25 g frisk gær eller 1 pose tørgær
  - 1 tsk sukker
  - 1 tsk salt
  - 1 æg
  - 50 g smør, smeltet
  - 450 g hvedemel
  - 8 pølser (hotdogs eller snackpølser)
  - 1 æg til pensling + sesam (valgfrit)
steps:
  - Rør gær ud i mælken med sukker. Tilsæt salt, æg, smør og mel. Ælt til en blød dej. Hæv 45–60 minutter.
  - Del i 8. Rul hver til en trekant eller lang strimmel. Rul pølsen ind. Efterhæv 15 minutter.
  - Pensl med æg. Drys sesam. Forvarm til 170 °C.
  - Læg hornene med plads. Steg 12–14 minutter, til dybt gyldne. Vend ikke — dej hæver bedst i ro.
  - Køl 3 minutter. Server med ketchup og sennep.
faq:
  - question: Hvorfor ikke bare færdigdej?
    answer: Fordi gærdej smager af brød, ikke af butterdej. Til den lynhurtige version se [pølsehorn](/opskrifter/airfryer/poelsehorn).
  - question: Kan dejen laves dagen før?
    answer: Ja — køl efter første hævning. Form og efterhæv fra kolde.
  - question: Rå pølser?
    answer: Brug færdigkogte. Rå pølser kræver længere tid og kan efterlade dejen bleg.
  - question: Frysning?
    answer: Frys efter formning. Bag fra fryser ved 170 °C i 16–18 minutter.
body: |
  Pølsehorn med gærdej er den langsomme, bedre version.

  Dejen hæver. Pølsen pakkes ind. Airfryeren giver farve uden ovn.

  Børnefødselsdag-godkendt. Voksen-snack også.
tip: Lav dem lidt mindre end du tror — gærdej hæver i kurven, og plads mellem hornene er vigtigere end størrelse.
=====
title: Søde vafler og pandekager i silikoneforme
slug: vafler-pandekager-silikone
category: airfryer
description: Søde vafler eller pandekager bagt i silikoneforme i airfryer — morgenmad uden vaffeljern.
prepTime: PT15M
cookTime: PT12M
totalTime: PT27M
servings: 4
difficulty: nem
tags:
  - vafler
  - pandekager
  - morgenmad
  - silikoneforme
  - sødt
  - airfryer
  - børn
imageAlt: Gyldne mini-vafler og pandekager fra airfryer-silikoneforme
featured: true
ingredients:
  - 2 æg
  - 2½ dl mælk
  - 200 g hvedemel
  - 2 spsk sukker
  - 1 tsk bagepulver
  - 1 knivspids salt
  - 50 g smeltet smør
  - 1 tsk vaniljesukker
  - Silikone-vaffelform eller muffin/pandekage-forme til airfryer
  - Sirup, bær eller flormelis til servering
steps:
  - Pisk æg, mælk, sukker og vanilje. Sigt mel, bagepulver og salt i. Rør smør i. Dejen skal være lidt tykkere end pandekagedej.
  - Smør/spray silikoneformene. Fyld ⅔ op — de hæver.
  - Forvarm til 160 °C. Sæt formene i kurven. Bag 10–12 minutter, til de er faste og let gyldne. Vend ikke.
  - Køl 2 minutter i formen. Vip ud. Server med bær og sirup.
faq:
  - question: Vafler eller pandekager?
    answer: Samme dej. Vaffelform giver riller; runde silikoneforme giver tykke pandekage-puder.
  - question: Bliver de tørre?
    answer: For høj varme. Hold 160 °C. De skal være lysegyldne, ikke brune som toast.
  - question: Kan man bruge færdig vaffeldej?
    answer: Ja. Fyld formene og bag samme tid.
  - question: Uden silikoneform?
    answer: Så er airfryer ikke det rigtige værktøj — brug pandekagepande eller vaffeljern i stedet.
body: |
  Vafler og pandekager i airfryer kræver én ting: silikoneforme der passer i kurven.

  Samme dej. Forskellig form. Lav temperatur.

  Det er weekendmorgen uden at finde vaffeljernet frem fra skabet.
tip: Fyld ikke formene helt — bagepulveret hæver, og overløb klistrer til kurven.
=====
title: Hjemmelavet granola i airfryer
slug: granola
category: airfryer
description: Hjemmelavet granola og mysli i airfryer — ristet sprødt på få minutter med nødder og honning.
prepTime: PT10M
cookTime: PT12M
totalTime: PT22M
servings: 8
difficulty: nem
tags:
  - granola
  - mysli
  - morgenmad
  - havregryn
  - snack
  - airfryer
imageAlt: Sprød hjemmelavet granola med nødder på bakke
featured: true
ingredients:
  - 4 dl havregryn (grove)
  - 1 dl hakkede mandler eller valnødder
  - ½ dl græskarkerner eller solsikkekerner
  - 3 spsk honning eller sirup
  - 2 spsk olie eller smeltet kokosolie
  - 1 tsk kanel
  - ½ tsk salt
  - ½ dl rosiner eller tørrede bær (tilsættes efter ristning)
steps:
  - Bland havre, nødder, kerner, kanel og salt. Rør honning og olie i, til alt er dækket.
  - Fordel i et tyndt lag i et fad eller på bagepapir i kurven.
  - Airfry 150 °C i 10–12 minutter. Rør hver 3.–4. minut, så kanterne ikke brænder.
  - Køl helt — den bliver sprødere når den køler. Rør rosiner i.
  - Opbevar lufttæt op til 2 uger.
faq:
  - question: Hvorfor lav temperatur?
    answer: Honning brænder let. 150 °C rister uden at svi. Rør ofte.
  - question: Klumper eller løs mysli?
    answer: Press blandingen let sammen før stegning for clusters. Rør mere undervejs for løs mysli.
  - question: Sukkerfri?
    answer: Brug sukkerfri sirup eller skip sødemiddel — så er det mere ristede havregryn end klassisk granola.
  - question: Kan man lave stor portion?
    answer: Hellere to hold end ét tykt lag. Tykt lag damper.
body: |
  Granola i airfryer er sprød morgenmad på under et kvarter.

  Lav varme. Hyppig røring. Køling er en del af opskriften.

  Rosinerne kommer i bagefter — ellers bliver de til kul.
tip: Smag på en nød halvvejs. Når den dufter ristet og smager nøddeagtigt, er du tæt på færdig.
=====
title: Fyldte croissanter med chokolade eller skinke/ost
slug: fyldte-croissanter
category: airfryer
description: Fyldte croissanter i airfryer på købe-wienerdej — chokolade eller skinke/ost, sprøde på 15 minutter.
prepTime: PT15M
cookTime: PT14M
totalTime: PT29M
servings: 6
difficulty: nem
tags:
  - croissant
  - wienerdej
  - chokolade
  - skinke
  - ost
  - bagværk
  - airfryer
  - brunch
imageAlt: Fyldte croissanter med chokolade og med skinke-ost fra airfryer
featured: true
ingredients:
  - 1 rulle croissantdej eller wienerdej
  - Sød: 50 g mørk chokolade i stænger eller 6 tsk nutella
  - Salt: 6 skiver skinke + 6 skiver ost
  - 1 æg til pensling
  - Valgfrit: sesam eller flormelis
steps:
  - Rul dejen ud. Del i trekanter efter pakkens anvisning.
  - Læg chokolade eller skinke+ost i den brede ende. Rul til croissanter. Bøj let til måneform.
  - Pensl med æg. Forvarm til 160 °C.
  - Læg med plads på bagepapir i kurven. Steg 12–14 minutter, til dybt gyldne. Vend ikke.
  - Køl 3 minutter — fyldet er lavaspringende.
faq:
  - question: Croissantdej eller butterdej?
    answer: Croissantdej hæver mere og bliver luftig. Butterdej er fladere og sprødere — begge virker.
  - question: Frosne færdig-croissanter?
    answer: Også fint — fyld dem forsigtigt, eller bag dem ufyldte og skær dem op efter.
  - question: Chokolade løber ud?
    answer: Brug chokoladestænger, ikke chips. Rul tæt, og læg samlingen nedad.
  - question: Kan man fryse?
    answer: Frys rå rullede. Bag fra fryser ved 160 °C i 16–18 minutter.
body: |
  Fyldte croissanter er brunch-snyd med købe-dej — og det er helt legitimt.

  Én rulle. To fyld. Airfryer ved lav varme.

  Chokolade til den søde. Skinke og ost til den saltede. Gerne begge dele på samme bakke.
tip: 160 °C er vigtigt — højere brænder ydersiden før midten er bagt færdig.
=====
title: Churros fra bunden i airfryer
slug: churros-fra-bunden
category: airfryer
description: Churros fra bunden i airfryer — udvidet guide til vandbakkelsesdej, stjerne-tylle og klassisk kanelsukker.
prepTime: PT30M
cookTime: PT16M
totalTime: PT46M
servings: 4
difficulty: mellem
tags:
  - churros
  - vandbakkelsesdej
  - dessert
  - kanel
  - airfryer
  - fra bunden
imageAlt: Hjemmelavede churros vendt i kanelsukker
featured: true
ingredients:
  - 2½ dl vand
  - 50 g smør
  - 1 spsk sukker
  - ½ tsk salt
  - 150 g hvedemel (sigtet)
  - 2–3 æg (rumtempererede)
  - Olie-spray
  - Kanelsukker: 80 g sukker + 2 tsk kanel + knivspids flagesalt
  - Valgfrit: chokoladesauce til dyp
steps:
  - Kog vand, smør, sukker og salt op. Tag af varmen. Hæld al melet i på én gang. Rør energisk til en glat bold der slipper siden. Sæt tilbage på lav varme 1 minut for at tørre dejen.
  - Køl 5–8 minutter (varm, ikke skoldende). Pisk æg i ét ad gangen. Dejen er klar når den er blank og falder i et V fra skeen — tilsæt ikke nødvendigvis hele æg nr. 3.
  - Kom dej i sprøjtepose med stor stjerne-tylle. Sprøjt 10–12 cm stænger på bagepapir. Spray olie.
  - Airfry 190 °C i 12–16 minutter, til de er hule, faste og gyldne. Vend ikke undervejs.
  - Vend straks i kanelsukker. Server varme. Vil du have saltkaramel, se [churros med saltkaramel](/opskrifter/airfryer/churros-saltkaramel).
faq:
  - question: Hvorfor udvidet guide?
    answer: Fordi vandbakkelsesdej er det der går galt — for varmt til æg, for tynd dej, for blege stænger. Denne opskrift er teknikken. Saltkaramel-versionen er den færdige dessert-tallerken.
  - question: Dejen er for tynd?
    answer: For meget æg eller for lidt tørring. Den skal holde rillerne fra tyllen. Vent, eller rør en spsk mel i.
  - question: Bløde indeni?
    answer: For korte. De skal være tørre i midten. Giv 2 minutter mere.
  - question: Uden sprøjtepose?
    answer: Brug en frysepose med hjørnet klippet — men stjerne-tylle giver den klassiske overflade der knaser.
body: |
  Churros fra bunden starter med vandbakkelsesdej — ikke færdigblanding.

  Kog. Mel. Tør. Æg. Piping. Olie-spray.

  Kanelsukker lige når de kommer ud, mens overfladen stadig er klistret nok til at sukkeret sidder.
tip: Test én churro først. Hvis den ikke hæver og bliver hul, mangler dejen æg eller var for kold da æggene gik i.
=====
title: Varme hveder i airfryer
slug: varme-hveder
category: airfryer
description: Varme hveder i airfryer — bløde, klassiske hveder perfekte op til Store Bededag, bagt uden stor ovn.
prepTime: PT2H
cookTime: PT14M
totalTime: PT2H14M
servings: 8
difficulty: mellem
tags:
  - hveder
  - Store Bededag
  - bagværk
  - gærdej
  - brunsviger
  - airfryer
  - tradition
imageAlt: Varme hveder skåret og ristet i airfryer
featured: true
ingredients:
  - 2½ dl lunkent mælk
  - 25 g frisk gær eller 1 pose tørgær
  - 1 spsk sukker
  - 1 tsk salt
  - 1 æg
  - 50 g smør, blødt
  - 450 g hvedemel
  - 1 æg til pensling
  - Til servering: smør, kanelsukker eller brunsviger-agtig remonce
steps:
  - Rør gær ud i mælken med sukker. Tilsæt salt, æg, smør og mel. Ælt til blød dej. Hæv 60 minutter.
  - Del i 8–10 boller. Læg tæt i en smurt form der passer i kurven (de skal bage sammen som hveder). Efterhæv 30 minutter.
  - Pensl med æg. Forvarm til 160 °C. Bag 12–14 minutter, til lysegyldne.
  - Køl kort. Skær hver hvede over. Smør og drys kanelsukker — eller pensl remonce.
  - Rist de smurte halvdele 2–3 minutter ved 180 °C til kanelsukkeret smelter. Server varme — Store Bededag eller ej.
faq:
  - question: Hvorfor Store Bededag?
    answer: Traditionen med varme hveder hører til dagen, også efter den faldt bort som helligdag. Opskriften smager godt alle andre dage også.
  - question: Skal de ristes efter?
    answer: Ja — det er «varme» hveder. Første bagning gør dem færdige; ristningen med smør/kanel er ritualet.
  - question: Kan man bruge færdigboller?
    answer: Ja. Køb hveder eller boller, skær, smør, rist 2–3 minutter ved 180 °C.
  - question: For mørke?
    answer: 160 °C. Hveder skal være lyse, ikke landbrød-brune.
body: |
  Varme hveder er bløde boller, skåret, smurt og ristet — ikke bare «boller med kanel».

  Bag dem tæt, så siderne bliver bløde. Rist dem åbne.

  Store Bededag eller en tilfældig søndag: samme opskrift.
tip: Læg dem tæt i formen — ægte hveder har bløde «kyssesider». Hvis de bager frit, bliver det bare almindelige boller.
=====
title: Sprøde tortillachips med hjemmelavet krydderiblanding
slug: tortillachips
category: airfryer
description: Sprøde tortillachips i airfryer med hjemmelavet krydderiblanding — bedre end posechips på 8 minutter.
prepTime: PT10M
cookTime: PT8M
totalTime: PT18M
servings: 4
difficulty: nem
tags:
  - tortillachips
  - snack
  - nachos
  - majstortilla
  - airfryer
  - festmad
imageAlt: Sprøde hjemmelavede tortillachips med krydderier
featured: true
ingredients:
  - 6 majstortillas (eller hvedetortillas)
  - 1 spsk olie
  - Krydderi: 1 tsk salt, 1 tsk paprika, ½ tsk spidskommen, ½ tsk hvidløgspulver, ¼ tsk chili, knivspids oregano
  - Dip: salsa, guacamole eller creme fraiche
steps:
  - Skær tortillas i 6–8 trekanter. Pensl eller vend let i olie.
  - Bland krydderierne. Drys over chipsene og vend, så alle får smag.
  - Forvarm til 180 °C. Læg i ét lag (to hold). Steg 5 minutter. Ryst. Steg 2–3 minutter mere, til knasende.
  - Køl 2 minutter — de sprøder færdigt udenfor kurven. Server med dip.
faq:
  - question: Majs eller hvede?
    answer: Majs bliver mere «posechips». Hvede bliver lidt blødere men stadig sprød.
  - question: For brændte kanter?
    answer: For høj varme eller for tynde tortillas. Hold 180 °C og kig de sidste minutter.
  - question: Kan man lave nachos?
    answer: Ja — top med ost og jalapeños, 2–3 minutter ekstra ved 180 °C.
  - question: Holdbarhed?
    answer: Lufttæt dåse 2–3 dage. De er bedst samme dag.
body: |
  Tortillachips i airfryer er snack-matematik: tortillas + olie + salt = bedre end posen.

  Krydderiblandingen er det der gør dem til «nogen har gjort sig umage».

  Ét lag. Ryst. Køl. Dip.
tip: Salt mens de er varme — det klistrer bedre end på kolde chips.
=====
title: Airfryer-cookies med marcipan- eller nougatmidte
slug: cookies-marcipan-nougat
category: airfryer
description: Airfryer-cookies med flydende marcipan- eller nougatmidte — bløde kanter og smeltet kerne.
prepTime: PT20M
cookTime: PT10M
totalTime: PT30M
servings: 8
difficulty: nem
tags:
  - cookies
  - marcipan
  - nougat
  - dessert
  - bagværk
  - airfryer
  - sødt
imageAlt: Cookies med flydende marcipanmidte brudt over så fyldet ses
featured: true
ingredients:
  - 125 g smør, blødt
  - 100 g brun farin
  - 50 g sukker
  - 1 æg
  - 1 tsk vaniljesukker
  - 200 g hvedemel
  - ½ tsk bagepulver
  - ½ tsk salt
  - 80 g marcipan eller blød nougat, i 8 små bolde
  - Valgfrit: 50 g chokoladechips i dejen
steps:
  - Pisk smør og sukker luftigt. Rør æg og vanilje i. Sigt mel, bagepulver og salt i. Rør chokoladechips i hvis du bruger dem.
  - Del dejen i 8. Flad hver portion, læg en marcipan/nougat-bold i midten, luk dejen omkring og form en cookie. Tryk let fladt.
  - Forvarm til 160 °C. Læg 3–4 cookies på bagepapir i kurven med god plads.
  - Bag 8–10 minutter, til kantene er sat og midten stadig ser blød ud. De stivner når de køler.
  - Køl 5 minutter på papiret. Flyt til rist. Midten skal være blød og fyldet smeltet.
faq:
  - question: Forskel på hurtige bager-cookies?
    answer: De her har fyld. Til den simple version se [hurtige bager-cookies](/opskrifter/airfryer/hurtige-bager-cookies).
  - question: Marcipan eller nougat?
    answer: Begge. Marcipan er mandlet. Nougat er chokolade-nøddeagtig. Brug blød nougat — ikke hårde barer.
  - question: Cookies flyder ud?
    answer: For blød dej eller for varmt. Køl dejen 15 minutter, og hold 160 °C.
  - question: Kan de fryses?
    answer: Frys formede, ufyldte eller fyldte. Bag fra fryser +1–2 minutter.
body: |
  Cookies med marcipan- eller nougatmidte er den lille luksus oven på en almindelig cookie.

  Luk fyldet tæt. Bag dem lyse. Lad midten være blød.

  Airfryeren bager få ad gangen — det er en feature, ikke en bug.
tip: Markér toppen med et lille kryds, så du husker hvor fyldet er, hvis dejen er tyk — så undgår du at trykke fyldet ud.
=====
title: Indbagte Oreo-kager i pandekagedej
slug: indbagte-oreos
category: airfryer
description: Indbagte Oreo-kager i pandekagedej i airfryer — deep-fried Oreos uden friture, knasende og varme.
prepTime: PT15M
cookTime: PT8M
totalTime: PT23M
servings: 4
difficulty: nem
tags:
  - oreo
  - dessert
  - snack
  - pandekagedej
  - airfryer
  - festmad
  - børn
imageAlt: Indbagte Oreos i gylden pandekagedej med flormelis
featured: true
ingredients:
  - 12 Oreo-kager (eller lignende cremekager)
  - 1 dl hvedemel
  - 1 dl mælk
  - 1 æg
  - 1 spsk sukker
  - ½ tsk bagepulver
  - Knivspids salt
  - Olie-spray
  - Flormelis til drys
steps:
  - Pisk mel, mælk, æg, sukker, bagepulver og salt til en tyk pandekagedej — den skal dække kagen uden at løbe af.
  - Dup hver Oreo i dejen, så den er helt dækket. Læg på bagepapir. Spray olie.
  - Forvarm til 180 °C. Læg 4–6 ad gangen med plads.
  - Steg 4 minutter. Vend forsigtigt. Spray igen. Steg 3–4 minutter mere, til gyldne.
  - Drys flormelis på. Vent 1 minut — midten er vulkan-varm.
faq:
  - question: Er det ikke bare fedt?
    answer: Jo. Det er pointen. Airfryeren gør det uden oliebad — stadig dessert, bare mindre rod.
  - question: Dejen drypper af?
    answer: For tynd. Tilsæt 1 spsk mel. Dejen skal være som tyk yoghurt.
  - question: Andre kager?
    answer: Ja — andre cremekager virker. Hold dem kølige så cremen ikke smelter før dejen sætter sig.
  - question: Kan man forberede?
    answer: Dyp lige før stegning. Dejen bliver soggy hvis de venter.
body: |
  Indbagte Oreos er carnival-mad i airfryeren.

  Tyk pandekagedej. Olie-spray. Kort tid.

  Flormelis skjuler ingen synder — og det er heller ikke meningen.
tip: Frys Oreos 20 minutter først — så smelter cremen ikke før dejen er stivnet.
=====
'''


def parse_block(text: str) -> dict:
    data: dict = {}
    mode = None
    body_lines: list[str] = []
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
    tags = "\n".join(f'  - {yaml_str(t)}' for t in d["tags"])
    ings = "\n".join(f'  - {yaml_str(x)}' for x in d["ingredients"])
    steps = "\n".join(f'  - {yaml_str(x)}' for x in d["steps"])
    faqs = "\n".join(
        f'  - question: {yaml_str(f["question"])}\n    answer: {yaml_str(f["answer"])}'
        for f in d["faq"]
    )
    featured = "featured: true\n" if d.get("featured") == "true" else ""
    slug = d["slug"]
    cat = d["category"]
    return f'''---
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
publishedAt: 2026-10-23
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
'''


blocks = [b for b in RECIPES.split("=====") if b.strip()]
print(f"blocks: {len(blocks)}")
assert len(blocks) == 25, len(blocks)
for b in blocks:
    d = parse_block(b)
    assert d.get("faq") and len(d["faq"]) >= 3, d.get("slug")
    assert d.get("tip"), d.get("slug")
    out = ROOT / d["category"]
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{d['slug']}.mdx"
    if path.exists():
        raise SystemExit(f"slug collision: {path}")
    path.write_text(to_mdx(d), encoding="utf-8")
    print("wrote", d["category"] + "/" + path.name)
