#!/usr/bin/env python3
"""Rugbrødsrester-batch: 18 huller (nov 2026). Billeder genereres separat."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RECIPES_DIR = ROOT / "content" / "recipes"
PUBLISHED = "2026-11-18"

RECIPES = r'''
=====
title: Rugbrødscroutoner med hvidløg og brunet smør
slug: rugbroedscroutoner
category: pande
description: Rugbrødscroutoner med hvidløg og brunet smør — sprøde tern til salat, svampesuppe og cremet kartoffelsuppe.
prepTime: PT10M
cookTime: PT10M
totalTime: PT20M
servings: 4
difficulty: nem
tags:
  - rugbrød
  - rester
  - croutoner
  - hvidløg
  - snack
  - pande
imageAlt: Gyldne rugbrødscroutoner med hvidløg i skål
featured: false
ingredients:
  - 4 skiver tørt rugbrød, skåret i 1–1½ cm tern
  - 40 g smør
  - 1 fed hvidløg, knust
  - 1 knivspids flagesalt
  - Valgfrit: frisk timian eller persille
steps:
  - Skær rugbrødet i jævne tern. For vådt brød? Tør 5 minutter på panden uden fedt først.
  - Smelt smør på middel varme, til det bruner og dufter nøddeagtigt. Hvidløg i 20 sekunder.
  - Ternene i. Vend jævnligt 6–8 minutter, til de er knasende og gyldne.
  - Salt til sidst. Krydderurt over. Server straks til [svampesuppe](/opskrifter/gryde/svampesuppe) eller salat.
faq:
  - question: Olie i stedet for smør?
    answer: Ja. Brunet smør smager bedre. Olie er neutral.
  - question: Airfryer?
    answer: 160 °C i 6–8 minutter, ryst ofte. Pensl med smeltet smør og hvidløg først.
  - question: Til hvad?
    answer: Salat, cremet kartoffelsuppe, græskarsuppe — eller bare i hånden.
  - question: Bløde croutoner?
    answer: For vådt brød eller for lav varme. Tør først, steg færdigt.
body: |
  Rugbrødscroutoner er resten der redder suppen: brunet smør, hvidløg, knas.

  Ikke toast. Tern. Vend. Salt.
tip: Salt til sidst — ellers suger ternene væske og bliver sej.
=====
title: Sprød rugbrødspanko
slug: rugbroedspanko
category: pande
description: Sprød rugbrødspanko — blendet tørt rugbrød ristet på panden. Perfekt rasp til fiskefilet og koteletter.
prepTime: PT5M
cookTime: PT8M
totalTime: PT15M
servings: 8
difficulty: nem
tags:
  - rugbrød
  - rester
  - panko
  - rasp
  - panering
  - pande
imageAlt: Gylden rugbrødspanko i skål klar til panering
featured: false
ingredients:
  - 200 g tørt rugbrød (ca. 6–8 skiver)
  - 1 spsk olie eller smør (valgfrit, til ristning)
  - ½ tsk salt
steps:
  - Bræk brødet i stykker. Blend til grove rasp — ikke pulver. Nogle flager er okay.
  - Rist på tør pande ved middel-lav varme 5–8 minutter under omrøring, til det er tørt og gyldent. Lidt fedt giver mere farve.
  - Salt. Køl helt. Opbevar lufttæt op til 2 uger.
  - Brug til panering af fisk, koteletter eller blomkål — æg, mel, rugbrødspanko.
faq:
  - question: Fint eller groft?
    answer: Groft til knas. Fint til tynd skorpe. Stavblender i korte pulse.
  - question: Uden ristning?
    answer: Kan bruges råt, men smager fladt. Ristning er umami.
  - question: Fryser det?
    answer: Ja. Pose i fryseren. Brug direkte.
  - question: Er det panko?
    answer: Det er rugbrødspanko — mørkere, mere smag end hvidt panko.
body: |
  Rugbrødspanko er rasp med kant: blend, rist, panér.

  Fiskefilet. Koteletter. Færdig.
tip: For fint blend = mudder. Stop når det ligner flager.
=====
title: Rugbrøds-nachos med cheddar og jalapeños
slug: rugbroeds-nachos
category: ovn
description: Rugbrøds-nachos — trekanter af tørt rugbrød bagt sprøde og toppet med cheddar, jalapeños og syltede løg.
prepTime: PT15M
cookTime: PT15M
totalTime: PT30M
servings: 4
difficulty: nem
tags:
  - rugbrød
  - rester
  - nachos
  - cheddar
  - snack
  - ovn
imageAlt: Rugbrøds-nachos med smeltet cheddar og jalapeños
featured: true
ingredients:
  - 8 skiver tørt rugbrød, skåret i trekanter
  - 2 spsk olie
  - 150 g cheddar, groft reven
  - 1–2 spsk syltede jalapeños
  - 2 spsk syltede rødløg
  - Flagesalt
  - Valgfrit: creme fraiche, koriander, [aioli](/opskrifter/dips/aioli)
steps:
  - Tænd ovnen på 190 °C. Skær rugbrød i trekanter. Pensl let med olie, drys salt.
  - Fordel i ét lag på bageplade. Bag 8–10 minutter, til de er knasende. Vend halvvejs.
  - Tag ud. Fordel cheddar, jalapeños og løg over. Bag 3–5 minutter mere, til osten bobler.
  - Server straks med creme fraiche.
faq:
  - question: Frisk rugbrød?
    answer: Det damper. Brug gammelt, eller tør skiverne 5 minutter først.
  - question: Airfryer?
    answer: Sprød først ved 160 °C i 6 minutter. Ost under grill/ovn — airfryeren smelter ujævnt i stakke.
  - question: Mildere?
    answer: Skip jalapeños. Brug paprika og [syltede rødløg](/opskrifter/sylte/syltede-roedloeg-10-minutter).
  - question: Mere fyld?
    answer: Restekød, bønner eller chorizo under osten.
body: |
  Rugbrøds-nachos er fredags-resten: trekanter, cheddar, jalapeños.

  Ikke tortilla. Rug. Det holder.
tip: Ét lag når de sprødes. Stak først når osten kommer på.
=====
title: Smørstegte rugbrødsstænger med dip
slug: rugbroedsstaenger
category: pande
description: Smørstegte rugbrødsstænger — sprøde soldater vendt i salt, serveret med hytteost-creme eller aioli.
prepTime: PT10M
cookTime: PT8M
totalTime: PT20M
servings: 4
difficulty: nem
tags:
  - rugbrød
  - rester
  - snack
  - hytteost
  - aioli
  - pande
imageAlt: Smørstegte rugbrødsstænger med dip i skål
featured: false
ingredients:
  - 6 skiver tørt rugbrød, skåret i 1 cm stænger
  - 40 g smør
  - Flagesalt
  - Dip: 150 g hytteost blendet med 1 spsk olie, citronsaft, salt — eller [aioli](/opskrifter/dips/aioli)
steps:
  - Skær brødet i stænger. Smelt smør på middel varme.
  - Steg stængerne 3–4 minutter per side, til de er knasende og gyldne. Vend forsigtigt.
  - Drys flagesalt.
  - Blend hytteost-dip glat, eller stil aioli frem. Dip. Spis.
faq:
  - question: Til børn?
    answer: Ja. Mild dip. Mindre salt.
  - question: Uden smør?
    answer: Olie. Smør smager bedre.
  - question: Bløde midter?
    answer: Tyndere stænger, eller længere tid. Tørt brød hjælper.
  - question: Airfryer?
    answer: Pensl med smeltet smør. 160 °C i 6–8 minutter, ryst.
body: |
  Rugbrødsstænger er soldater med attitude: smør, salt, dip.

  Hytteost-creme eller aioli. Ikke ketchup — medmindre det er tirsdag.
tip: Skær jævnt. Tynde stænger brænder, tykke bliver bløde.
=====
title: Rugbrødslasagne
slug: rugbroedslasagne
category: ovn
description: Rugbrødslasagne — dansk bonde-lasagne med tynde skiver tørt rugbrød i stedet for pasta, kødsovs og ost.
prepTime: PT30M
cookTime: PT45M
totalTime: PT1H20M
servings: 6
difficulty: mellem
tags:
  - rugbrød
  - rester
  - lasagne
  - kødsovs
  - aftensmad
  - ovn
imageAlt: Rugbrødslasagne med osteskorpe i fad
featured: true
ingredients:
  - 10–12 tynde skiver tørt rugbrød
  - 600 g kødsovs (klar eller hjemmelavet)
  - 2 dl crème fraiche eller bechamel
  - 150 g mozzarella eller blandet ost, reven
  - 50 g parmesan
  - Salt og peber
  - Smør til fadet
steps:
  - Tænd ovnen på 180 °C. Smør et ovnfast fad.
  - Læg et lag rugbrød. Fordel kødsovs. Lidt crème fraiche. Gentag lag — slut med sovs og ost.
  - Drys parmesan. Bag 40–45 minutter, til det bobler og toppen er gylden.
  - Hvile 10 minutter før du skærer — ellers falder det sammen.
faq:
  - question: For tørt?
    answer: Mere sovs. Rug suger. Sovsen skal være lidt løsere end til pasta-lasagne.
  - question: Oksehale i stedet for kødsovs?
    answer: Ja. Braiseret kød med sauce. Endnu mere bonde.
  - question: Vegetar?
    answer: Svampesovs eller linse-ragù. Samme lag.
  - question: Frisk rugbrød?
    answer: Tør skiverne 10 minutter ved 150 °C først.
body: |
  Rugbrødslasagne er pasta-fri bonde-mad: skiver, kødsovs, ost, ovn.

  Rug suger mere end pasta. Sovsen skal være generøs.
tip: Tynde skiver. Tykke bliver til skosåler i midten.
=====
title: Rugbrødspizza på støbejern
slug: rugbroedspizza
category: stobejern
description: Rugbrødspizza på støbejern — sprød bund af rugbrødsskiver stegt i smør, toppet med tomatsovs, ost og kødrester.
prepTime: PT10M
cookTime: PT12M
totalTime: PT25M
servings: 2
difficulty: nem
tags:
  - rugbrød
  - rester
  - pizza
  - støbejern
  - aftensmad
imageAlt: Rugbrødspizza med ost og tomatsovs i støbejernspande
featured: false
ingredients:
  - 2–3 skiver tørt rugbrød (store, eller overlappende)
  - 20 g smør
  - 3–4 spsk tomatsovs
  - 80 g mozzarella, reven
  - Rester af kød, skinke eller grønt
  - Oregano, flagesalt
steps:
  - Varm støbejern på middel. Smør i. Læg rugbrødsskiverne i ét lag — overlap er okay.
  - Steg 2–3 minutter, til undersiden er knasende. Vend ikke endnu.
  - Smør tomatsovs på. Ost og topping. Låg på 3–5 minutter, til osten smelter.
  - Salt, oregano. Spis fra panden.
faq:
  - question: Uden låg?
    answer: Osten smelter langsommere. Brug låg eller skub panden under grill et minut.
  - question: Ovn i stedet?
    answer: Ja. Sprød brødet først på pande, top, bag ved 220 °C i 5–7 minutter.
  - question: Blød bund?
    answer: Mere varme, mindre sovs midt på, tørt brød.
  - question: Surdejspizza i stedet?
    answer: Se [overnight sourdough cast iron pizza](/opskrifter/stobejern/overnight-sourdough-cast-iron-pizza).
body: |
  Rugbrødspizza er restepizza uden dej: smør, jernpande, ost.

  Bund på 3 minutter. Topping efter hvad køleskabet siger.
tip: Mindre sovs midt på end kanterne — rug suger og bliver slatten.
=====
title: Ristet rugbrøds-pyttipanna
slug: rugbroeds-pyttipanna
category: pande
description: Ristet rugbrøds-pyttipanna — tern af rugbrød stegt sprøde med kartofler, løg, kødrester og spejlæg.
prepTime: PT15M
cookTime: PT20M
totalTime: PT35M
servings: 4
difficulty: nem
tags:
  - rugbrød
  - rester
  - pyttipanna
  - aftensmad
  - spejlæg
  - pande
imageAlt: Rugbrøds-pyttipanna med spejlæg på pande
featured: false
ingredients:
  - 3 skiver tørt rugbrød, i tern
  - 400 g kogte kartofler, i tern
  - 1 løg, hakket
  - 200 g kødrester (steg, pølse, bacon)
  - 2 spsk smør eller olie
  - 4 æg
  - Salt, peber, evt. rødbeder
steps:
  - Steg løg i fedt 3 minutter. Kartoffeltern i. Steg til de får skorpe.
  - Kød i. Rugbrødstern i til sidst — 4–5 minutter, til de er knasende.
  - Smag til med salt og peber.
  - Spejlæg i anden pande. Server pyttipanna med æg ovenpå — og gerne syltede rødbeder.
faq:
  - question: Uden kød?
    answer: Ja. Ekstra kartoffel, svampe eller bønner.
  - question: Friske kartofler?
    answer: Kog først. Rå kartoffel tager for lang tid.
  - question: Mere som biksemad?
    answer: Se [biksemad med spejlæg](/opskrifter/pande/biksemad-spejlaeg). Her er rugbrødet stjernen.
  - question: Brændt brød?
    answer: Kom ternene ind til sidst. De steger hurtigere end kartoffel.
body: |
  Rugbrøds-pyttipanna er svensk restemad med dansk knas: kartoffel, kød, rug, spejlæg.

  Brødet kommer sidst. Ellers brænder det.
tip: Store tern. Små bliver til sand i panden.
=====
title: Frikadeller strakt med rugbrød
slug: frikadeller-rugbroed
category: pande
description: Frikadeller strakt med opblødt rugbrød — saftig fars med umami, mæthed og mindre kødspild.
prepTime: PT20M
cookTime: PT15M
totalTime: PT40M
servings: 4
difficulty: nem
tags:
  - rugbrød
  - rester
  - frikadeller
  - fars
  - aftensmad
  - pande
imageAlt: Gyldne frikadeller med rugbrød i farsen
featured: true
ingredients:
  - 500 g hakket grise-/kalvefars
  - 2 skiver tørt rugbrød, udblødt i 1 dl mælk
  - 1 æg
  - 1 lille løg, fint hakket
  - 1 tsk salt
  - ½ tsk peber
  - Smør eller olie til stegning
steps:
  - Udblød rugbrød i mælk 5–10 minutter. Mos med gaffel — ingen store klumper.
  - Bland fars, æg, løg, salt, peber og det mosede brød. Rør til det hænger sammen. Hvile 10 minutter.
  - Form frikadeller. Steg i smør 4–5 minutter per side, til de er gennemstegte og gyldne.
  - Server med kartofler, sovs eller rugbrød — ironisk, men korrekt.
faq:
  - question: Hvor meget brød?
    answer: Ca. 10–15 % af farsvægten. Mere, og de smager af toast.
  - question: Airfryer?
    answer: Ja. 180 °C i 12–14 minutter. Vend halvvejs. Se også [airfryer-frikadeller](/opskrifter/airfryer/frikadeller).
  - question: Tørt i midten?
    answer: For lidt væske i brødet, eller for høj varme. Udblød ordenligt.
  - question: Farsbrød i ovn?
    answer: Samme fars i form. 180 °C i ca. 45 minutter.
body: |
  Opblødt rugbrød i farsen er gammeldags saft-hack: umami, volumen, mindre tørhed.

  Ikke snyd. Teknik.
tip: Mos brødet helt. Klumper giver huller i frikadellen.
=====
title: Rugbrødsgratin med porrer og bacon
slug: rugbroedsgratin-porrer-bacon
category: ovn
description: Rugbrødsgratin med porrer og bacon — lag af tørt rugbrød, stegte porrer og bacon bagt under æggemasse og ost.
prepTime: PT25M
cookTime: PT35M
totalTime: PT1H
servings: 4
difficulty: mellem
tags:
  - rugbrød
  - rester
  - gratin
  - porrer
  - bacon
  - ovn
imageAlt: Rugbrødsgratin med porrer, bacon og osteskorpe
featured: false
ingredients:
  - 6 skiver tørt rugbrød
  - 2 porrer, skåret i skiver
  - 150 g bacon, i tern
  - 4 æg
  - 2 dl mælk eller fløde
  - 100 g ost, reven
  - Salt, peber, muskatnød
steps:
  - Tænd ovnen på 180 °C. Steg bacon sprødt. Tag op. Steg porrer i baconfedtet 5–7 minutter.
  - Læg rugbrød i smurt fad. Fordel porrer og bacon.
  - Pisk æg, mælk, salt, peber og muskat. Hæld over. Drys ost.
  - Bag 30–35 minutter, til midten er sat og toppen gylden. Hvile 5 minutter.
faq:
  - question: For vådt?
    answer: Tørt brød. Eller bag 5 minutter ekstra. Fløde gør det rigere — mælk er lettere.
  - question: Uden bacon?
    answer: Ja. Svampe eller ekstra ost. Lidt olie til porrerne.
  - question: Kan det forberedes?
    answer: Saml fadet, køl, bag dagen efter. Plus 5–10 minutter.
  - question: Til hvad?
    answer: Aftensmad med salat. Eller brunch.
body: |
  Rugbrødsgratin er strata på dansk: brød, porre, bacon, æg, ost.

  Brødet drikker æggemassen. Det er pointen.
tip: Tryk brødet let ned i væsken, så toppen ikke bliver tør.
=====
title: Brændende kærlighed på rugbrødsbund
slug: braendende-kaerlighed-rugbroed
category: pande
description: Brændende kærlighed på ristet rugbrødsbund — smørstegt rugbrød under kartoffelmos og bacon.
prepTime: PT20M
cookTime: PT25M
totalTime: PT45M
servings: 4
difficulty: nem
tags:
  - rugbrød
  - rester
  - brændende kærlighed
  - bacon
  - aftensmad
  - pande
imageAlt: Brændende kærlighed med bacon på ristet rugbrødsbund
featured: false
ingredients:
  - 4 skiver tørt rugbrød
  - 800 g kartofler til mos
  - 200 g bacon, i tern
  - 2 dl mælk, 25 g smør til mos
  - Ekstra smør til brødet
  - Salt, peber
  - Valgfrit: stegte løg
steps:
  - Kog kartofler. Mos med mælk, smør, salt og peber.
  - Steg bacon sprødt. Gem lidt fedt.
  - Steg rugbrødsskiver i smør/baconfedt, til de er knasende på begge sider.
  - Læg brød på tallerken. Mos ovenpå. Bacon og evt. løg over. Server straks — se også klassisk [brændende kærlighed](/opskrifter/gryde/braendende-kaerlighed).
faq:
  - question: Hvorfor rugbrød under?
    answer: Sprød bund. Mosen bliver ikke kedelig tallerken-klat.
  - question: Blød bund?
    answer: Steg brødet længere. Mos lige før servering — ikke forud.
  - question: Uden bacon?
    answer: Svampe og løg. Eller chorizo.
  - question: Ovnmoss?
    answer: Ja. Samme servering.
body: |
  Brændende kærlighed på rugbrød er den tungere udgave: knas under, mos midt, bacon top.

  Tallerkenen skal bære. Brødet gør det.
tip: Mos først når brødet er stegt — ellers bliver skorpen våd.
=====
title: Arme riddere af rugbrød
slug: arme-riddere-rugbroed
category: pande
description: Arme riddere af rugbrød — savory french toast vendt i æg og mælk, stegt i smør, toppet med bacon eller hytteost.
prepTime: PT10M
cookTime: PT12M
totalTime: PT25M
servings: 2
difficulty: nem
tags:
  - rugbrød
  - rester
  - arme riddere
  - brunch
  - bacon
  - pande
imageAlt: Savory arme riddere af rugbrød med bacon
featured: false
ingredients:
  - 4 skiver tørt rugbrød
  - 2 æg
  - 1 dl mælk
  - Salt, peber
  - 25 g smør
  - Topping: sprød bacon eller 100 g hytteost med purløg
steps:
  - Pisk æg, mælk, salt og peber. Dyp rugbrødsskiverne — begge sider, men ikke til de falder fra hinanden.
  - Steg i smør på middel varme 3–4 minutter per side, til de er gyldne.
  - Top med bacon eller hytteost. Server straks.
faq:
  - question: Søde arme riddere?
    answer: Skip salt/peber. Brug kanel og sukker. Her er det savory.
  - question: For vådt?
    answer: Kort dyp. Rug suger hurtigt. Tørt brød er bedst.
  - question: Hvidt toastbrød?
    answer: Se [franske toast](/opskrifter/pande/franske-toast) eller [arme riddere på plancha](/opskrifter/plancha/arme-riddere-plancha).
  - question: Uden bacon?
    answer: Hytteost, røget laks eller stegte svampe.
body: |
  Arme riddere af rugbrød er brunch med kant: æg, smør, bacon — ikke bærkompot.

  Rug holder. Hvidt toast giver efter.
tip: Dyp hurtigt. Langt bad = grød på panden.
=====
title: Rugbrøds-æggekage i støbejern
slug: rugbroeds-aeggekage
category: stobejern
description: Rugbrøds-æggekage i støbejern — tern af rugbrød stegt sprøde i bunden, før æggemassen hældes over.
prepTime: PT10M
cookTime: PT15M
totalTime: PT25M
servings: 2
difficulty: nem
tags:
  - rugbrød
  - rester
  - æggekage
  - støbejern
  - brunch
imageAlt: Rugbrøds-æggekage med sprøde brødtern i støbejern
featured: false
ingredients:
  - 2 skiver tørt rugbrød, i tern
  - 4 æg
  - 2 spsk mælk
  - 50 g ost, reven (valgfrit)
  - 1 spsk smør
  - Salt, peber
  - Valgfrit: bacon, purløg, spinat
steps:
  - Varm støbejern på middel. Smør i. Steg rugbrødstern 3–4 minutter, til de er knasende.
  - Pisk æg, mælk, salt og peber. Hæld over ternene. Ost og topping over.
  - Steg til bunden sætter sig. Låg på 2–3 minutter, eller finish under grill.
  - Skær i både. Spis fra panden.
faq:
  - question: Uden støbejern?
    answer: Almindelig pande med låg. Samme metode.
  - question: Bliver brødet blødt?
    answer: Steg ternene sprøde først. Så holder de bid i æggemassen.
  - question: Flere æg?
    answer: Ja. Større pande. Flere tern.
  - question: Ovnen?
    answer: Hæld i ovnfast fad efter stegning af tern. 180 °C i 12–15 minutter.
body: |
  Rugbrød i æggekagen er knas i bunden: steg ternene først, så æg.

  Ellers bliver det vådt toast-æg.
tip: Middel varme. For høj, og undersiden brænder før æggene sætter sig.
=====
title: Ymerdrys med brun farin
slug: ymerdrys
category: pande
description: Klassisk ymerdrys — ristet rugbrød med brun farin og smør. Sprødt drys til ymer, skyr og græsk yoghurt.
prepTime: PT5M
cookTime: PT8M
totalTime: PT15M
servings: 6
difficulty: nem
tags:
  - rugbrød
  - rester
  - ymerdrys
  - ymer
  - morgenmad
  - pande
imageAlt: Gyldent ymerdrys med brun farin i skål
featured: true
ingredients:
  - 4 skiver tørt rugbrød, smuldret groft
  - 30 g smør
  - 2 spsk brun farin
  - 1 knivspids salt
  - Valgfrit: kanel
steps:
  - Smuld rugbrødet groft. Smelt smør på middel-lav varme.
  - Brød i. Rør 4–5 minutter. Farin og salt i. Rør til det karamelliserer let — 2–3 minutter.
  - Kanel evt. i til sidst. Tip ud på bakke. Køl. Det sprøder videre.
  - Drys over ymer, skyr eller yoghurt. Til saltet version uden sukker: se [rugbrødsdrys](/opskrifter/pande/rugbroedsdrys).
faq:
  - question: Hvidt sukker?
    answer: Kan bruges. Brun farin smager dybere.
  - question: Brænder hurtigt?
    answer: Lav varme. Farin går fra karamel til bitter på sekunder.
  - question: Holdbarhed?
    answer: Lufttæt 1 uge. Bliver det blødt? Kort rist igen.
  - question: Til øllebrød?
    answer: Ja. Eller [æblemos](/opskrifter/gryde/aeblemos).
body: |
  Ymerdrys er morgenmadens knas: smør, brun farin, rug.

  Ikke müsli. Resten af brødet i en skål.
tip: Grov smuld. Fint pulver bliver til slik-sand.
=====
title: Rugbrødsvafler
slug: rugbroedsvafler
category: pande
description: Rugbrødsvafler — blendet, opblødt rugbrød rørt med æg og bagepulver, bagt sprøde i vaffeljernet under pålæg.
prepTime: PT15M
cookTime: PT20M
totalTime: PT40M
servings: 4
difficulty: mellem
tags:
  - rugbrød
  - rester
  - vafler
  - frokost
  - pålæg
  - pande
imageAlt: Sprøde rugbrødsvafler med pålæg
featured: false
ingredients:
  - 150 g tørt rugbrød
  - 2 dl mælk
  - 2 æg
  - 1 tsk bagepulver
  - 1 spsk olie eller smeltet smør
  - ½ tsk salt
  - Olie til jernet
steps:
  - Udblød rugbrød i mælk 10 minutter. Blend glat (eller mos meget fint).
  - Rør æg, olie, salt og bagepulver i. Dejen er tyk som vaffeldej.
  - Varm vaffeljern. Pensl let. Bag til sprøde og mørke — lidt længere end søde vafler.
  - Server med smør og pålæg, eller som bund under æg.
faq:
  - question: For tæt?
    answer: Mere mælk, eller ekstra æg. Bagepulver skal være friskt.
  - question: Søde vafler?
    answer: 1 spsk sukker og kanel. Her er de salte.
  - question: Uden vaffeljern?
    answer: Tynde pandekager på pande. Anden tekstur, samme dej.
  - question: Salte hytteostvafler?
    answer: Se [salte hytteostvafler](/opskrifter/pande/salte-hytteostvafler) — anden base.
body: |
  Rugbrødsvafler er pålægs-vafler: blendet brød, æg, jern.

  Sprøde kanter. Blød midte. Leverpostej hører til.
tip: Pensl jernet hver gang. Rugdej klistre mere end hvededej.
=====
title: Bondepige med slør
slug: bondepige-med-sloer
category: gryde
description: Bondepige med slør — lagkage i glas med smørristet rugbrødsrasp, æblemos og flødeskum.
prepTime: PT20M
cookTime: PT10M
totalTime: PT40M
servings: 4
difficulty: nem
tags:
  - rugbrød
  - rester
  - bondepige
  - æblemos
  - dessert
  - gryde
imageAlt: Bondepige med slør i glas med æblemos og flødeskum
featured: true
ingredients:
  - 4 skiver tørt rugbrød, smuldret
  - 30 g smør
  - 1 spsk sukker
  - 4 dl [æblemos](/opskrifter/gryde/aeblemos)
  - 2½ dl piskefløde
  - Valgfrit: vaniljesukker, mandelsplitter
steps:
  - Rist rugbrødssmuld i smør med sukker på panden, til det er knasende. Køl.
  - Pisk fløden til blødt skum (evt. med vaniljesukker).
  - Lag i glas: rasp, æblemos, flødeskum. Gentag. Afslut med rasp.
  - Server straks, eller køl 30 minutter så lagene sætter sig.
faq:
  - question: Uden æblemos?
    answer: Anden kompot — rabarber, bær. Æble er klassisk.
  - question: Makroner i stedet for rug?
    answer: Det er gammeldags æblekage-spor. Her er rug pointen.
  - question: Kan det stå natten over?
    answer: Ja, men rasp bliver blødere. Gem lidt knas til top.
  - question: Flødeskum for blødt?
    answer: Pisk til bløde toppe — ikke smør.
body: |
  Bondepige med slør er lagkage uden bagning: rasp, æblemos, fløde.

  Brug den [æblemos](/opskrifter/gryde/aeblemos) I allerede har. Resten er 10 minutter.
tip: Køl raspene helt. Varme rasp smelter flødeskummet.
=====
title: Rugbrødslagkage
slug: rugbroedslagkage
category: ovn
description: Rugbrødslagkage til sønderjysk kaffebord — bunde af revet rugbrød og chokolade med solbærsyltetøj og flødeskum.
prepTime: PT30M
cookTime: PT25M
totalTime: PT2H
servings: 10
difficulty: mellem
tags:
  - rugbrød
  - rester
  - lagkage
  - kaffebord
  - dessert
  - ovn
imageAlt: Rugbrødslagkage med flødeskum og solbærsyltetøj
featured: true
ingredients:
  - 150 g tørt rugbrød, fint revet eller blendet
  - 100 g mørk chokolade, smeltet
  - 100 g smør, blødt
  - 100 g sukker
  - 3 æg
  - 1 tsk bagepulver
  - 1 dl solbærsyltetøj (eller ribs)
  - 3 dl piskefløde
steps:
  - Tænd ovnen på 175 °C. Beklæd to små springforme (ca. 18–20 cm) eller bag én bund og del.
  - Pisk smør og sukker. Æg i ét ad gangen. Rør chokolade, rugbrød og bagepulver i.
  - Fordel dejen. Bag 20–25 minutter. Køl helt på rist.
  - Pisk fløde. Læg bunde sammen med syltetøj og flødeskum. Køl 1 time før servering.
faq:
  - question: Én form?
    answer: Bag én tykkere bund. Del vandret med kniv når den er kold.
  - question: Anden syltetøj?
    answer: Solbær er klassisk. Hindbær eller ribs virker.
  - question: For tør bund?
    answer: Lidt mere smør eller 1 spsk mælk i dejen. Rug suger.
  - question: Dagen før?
    answer: Ja. Den bliver saftigere natten over.
body: |
  Rugbrødslagkage er kaffebord uden spild: revet rug, chokolade, solbær, fløde.

  Det smager af Sønderjylland. Ikke af restemad.
tip: Riv brødet fint. Grove stykker giver huller i bunden.
=====
title: Rugbrødstrøfler
slug: rugbroedstroefler
category: pande
description: Rugbrødstrøfler — tørt rugbrød blendet med kakao, romessens og hindbærmarmelade. Romkugler med kant.
prepTime: PT20M
cookTime: PT0M
totalTime: PT1H
servings: 20
difficulty: nem
tags:
  - rugbrød
  - rester
  - trøfler
  - romkugler
  - dessert
  - pande
imageAlt: Rugbrødstrøfler rullet i kakao
featured: false
ingredients:
  - 200 g tørt rugbrød
  - 2 spsk kakao
  - 2–3 spsk hindbærmarmelade
  - 1 tsk romessens (eller 1 spsk rom)
  - 50 g blødt smør
  - 1 spsk sukker
  - Kakao eller kokos til rulle
  - Valgfrit: lidt kagerester — se også [romkugler](/opskrifter/pande/romkugler)
steps:
  - Blend rugbrød til fine rasp. Bland med kakao, sukker, smør, marmelade og romessens. Dejen skal kunne formes — tilsæt marmelade eller smør efter behov.
  - Køl 20–30 minutter.
  - Rul til små kugler. Vend i kakao eller kokos.
  - Køl til de er faste. Holdes 4–5 dage i køl.
faq:
  - question: For tør masse?
    answer: Mere marmelade eller smør. Rug drikker.
  - question: Uden rom?
    answer: Vanilje eller appelsinskal. Så er det trøfler, ikke romkugler.
  - question: Kun kagerester?
    answer: Se [romkugler](/opskrifter/pande/romkugler). Her er rug stjernen.
  - question: Kan de fryses?
    answer: Ja. Tø op i køl.
body: |
  Rugbrødstrøfler er romkuglernes mørke fætter: rug, kakao, hindbær, rom.

  Ingen ovn. Bare hænder.
tip: Køl massen før du ruller — ellers klistre det til fingrene.
=====
title: Æblecrumble med rugbrøds-topping
slug: aeblecrumble-rugbroed
category: ovn
description: Æblecrumble med rugbrøds-topping — halvdelen af havregrynene skiftet ud med groft tørt rugbrød for nøddeagtig knas.
prepTime: PT20M
cookTime: PT35M
totalTime: PT55M
servings: 6
difficulty: nem
tags:
  - rugbrød
  - rester
  - æblecrumble
  - dessert
  - æble
  - ovn
imageAlt: Æblecrumble med rugbrøds-topping i fad
featured: false
ingredients:
  - 800 g æbler, i både
  - 1 spsk sukker
  - 1 tsk kanel
  - Topping: 50 g havregryn, 50 g groft smuldret tørt rugbrød, 75 g mel, 75 g smør, 50 g sukker, 1 knivspids salt
steps:
  - Tænd ovnen på 180 °C. Læg æbler i smurt fad med sukker og kanel.
  - Smuld rugbrød groft. Gnid smør i mel, havre, rug, sukker og salt til en knasende crumble.
  - Fordel topping over æblerne. Bag 30–35 minutter, til toppen er gylden og æblerne bobler.
  - Server med fløde eller vaniljeis. Klassisk uden rug: [æblecrumble](/opskrifter/ovn/aeblecrumble).
faq:
  - question: Kun rugbrød i topping?
    answer: Kan godt. Halv/halv giver bedre balance. Rent rug bliver tungt.
  - question: Hvilke æbler?
    answer: Syrlige. Ingrid Marie, Granny Smith, Belle de Boskoop.
  - question: For våd topping?
    answer: Mere mel, eller tørrere brød. Smørret skal være koldt.
  - question: Dutch Oven?
    answer: Se [æblecrumble i Dutch Oven](/opskrifter/baalmad/aeblecrumble-i-dutch-oven) — samme rug-trick virker.
body: |
  Æblecrumble med rug er nøddeagtig restemad: halv havre, halv rugbrød, koldt smør.

  Samme fad. Mere kant.
tip: Grov smuld. Fint rugbrødspulver klumper i toppingen.
=====
'''


def parse_block(block: str) -> dict:
    data: dict = {"tags": [], "ingredients": [], "steps": [], "faq": []}
    mode = None
    body_lines: list[str] = []
    current_q = ""
    lines = block.strip().splitlines()
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
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


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
    written = []
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
        written.append(f"{d['category']}/{d['slug']}")
        print("wrote", written[-1])
    print(f"done: {len(written)} recipes")
    for w in written:
        print(w)


if __name__ == "__main__":
    main()
