#!/usr/bin/env python3
"""Grovfritter content-gap batch — 17 manglende vinkler (springer 3 eksisterende over)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"

RECIPES = r'''
=====
title: Rustikke grovfritter i ovn med bagepulver
slug: rustikke-grovfritter-bagepulver
category: ovn
description: Rustikke grovfritter i ovn med bagepulver — tykke kartofler med glass-like skorpe uden friture.
prepTime: PT25M
cookTime: PT40M
totalTime: PT1H5M
servings: 4
difficulty: mellem
tags:
  - grovfritter
  - kartofler
  - bagepulver
  - ovn
  - tilbehør
  - fritter
imageAlt: Tykke rustikke grovfritter fra ovnen med knasende guldsorpe
featured: true
ingredients:
  - 1 kg bagekartofler (melede), med skræl
  - 1 spsk bagepulver
  - 2 spsk olivenolie eller andefedt
  - 1 tsk flagesalt
  - Friskkværnet peber
steps:
  - Skær kartoflerne i tykke stave (ca. 1,5–2 cm). Skyl under koldt vand, til vandet er klart.
  - Kog i en stor gryde med saltet vand og 1 spsk bagepulver i 6–8 minutter — kanterne skal være matte og let flossede, midten stadig fast.
  - Dræn, ryst gryden hårdt 10 sekunder, så overfladen bliver ru. Læg på et rent viskestykke og lufttør 5–10 minutter.
  - Tænd ovnen på 220 °C (varmluft). Vend stavene med olie/fedt og peber. Fordel i ét lag på en rist over en bakke — eller på en meget varm bageplade.
  - Bag 20 minutter. Vend. Bag yderligere 15–20 minutter, til skorpen er dybt gylden og knaser.
  - Flagesalt lige før servering.
faq:
  - question: Hvorfor bagepulver?
    answer: Det hæver pH i vandet, så overfladen brydes og tørrer hurtigere. Resultatet er en tynd, glasagtig skorpe på tykke stave.
  - question: Kan man springe kogningen over?
    answer: Du kan — men så mister du den "glass-like" kant. Blanchering + rystning er tricket.
  - question: Andefedt eller olie?
    answer: Andefedt smager dybere. Olivenolie er hverdag. Begge virker — bare en tynd film, ikke en sø.
  - question: Airfryer i stedet?
    answer: Ja. 200 °C i 18–22 minutter efter blanchering. Ryst undervejs. Se også vores klassiske airfryer-grovfritter.
body: |
  Rustikke grovfritter i ovn med bagepulver er opskriften på friture-knas uden frituregryde.

  Kog kort. Ryst. Høj varme. Tykkelsen beholder den bløde midte — skorpen kommer fra den ru, tørre overflade.

  Det er gastropub-fritter til en almindelig hverdagsovn.
tip: Ryst gryden, til stavene ser ud som de har fået en tynd frakke af kartoffelmos. Den ru overflade er skorpen.
=====
title: Grovfritter på grillens plancha
slug: grovfritter-plancha
category: plancha
description: Grovfritter på plancha — tykke kartofler vendt i andefedt eller olivenolie direkte på den brandvarme støbejernsplade.
prepTime: PT20M
cookTime: PT25M
totalTime: PT45M
servings: 4
difficulty: mellem
tags:
  - grovfritter
  - kartofler
  - plancha
  - grill
  - andefedt
  - fritter
imageAlt: Grovfritter stegt på brandvarm plancha med gyldne kanter
featured: true
ingredients:
  - 900 g fastkogende kartofler, med skræl
  - 2–3 spsk andefedt eller olivenolie
  - 1 tsk groft havsalt
  - Friskkværnet peber
  - Valgfrit: 1 fed hvidløg, knust, til sidste minut
steps:
  - Skær kartoflerne i tykke stave (ca. 1,5 cm). Skyl, tør knastørt. Blanchér 5 minutter i saltet vand, dræn og tør igen.
  - Varm planchaen op, til en dråbe vand danser — brandvarm støbejernsplade.
  - Smelt andefedt (eller fordel olie) på pladen. Læg stavene i ét lag med plads imellem.
  - Steg 4–5 minutter uden at røre, til undersiden er dybt brun. Vend med en bred palet.
  - Fortsæt 12–15 minutter i alt, vend 2–3 gange, til alle sider har skorpe og midten er mør.
  - Salt, peber og evt. hvidløg det sidste minut. Server direkte fra pladen.
faq:
  - question: Andefedt eller olivenolie?
    answer: Andefedt giver dyb, grillbar smag. Olivenolie er lettere. Begge skal være varme, før kartoflerne rammer pladen.
  - question: Kan man springe blanchering over?
    answer: På plancha tager rå stave længere og brænder oftere. Kort kog gør midten færdig, før kanterne bliver sorte.
  - question: Almindelig grillrist i stedet?
    answer: Stavene falder igennem. Brug plancha, støbejernsplade eller en perforeret grillbakke.
  - question: For mange på pladen?
    answer: De damper. Arbejd i to hold — planchaen skal blive ved med at brune, ikke koge.
body: |
  Grovfritter på grillens plancha er kartoffel med røg-kant og støbejernsbrand.

  Pladen skal være brandvarm. Fedtet skal synge. Stavene skal have plads.

  Vend dem som smash burgers — tålmodigt, med paletten fladt under.
tip: Tør stavene to gange — efter skyl og efter blanchering. Vand på plancha er damp, ikke skorpe.
=====
title: Hvidløg- og parmesan-grovfritter
slug: hvidloeg-parmesan-grovfritter
category: airfryer
description: Hvidløg- og parmesan-grovfritter — tykke rustikke fritter vendt i friskrevet parmesan, hvidløgsolie og persille.
prepTime: PT15M
cookTime: PT22M
totalTime: PT37M
servings: 4
difficulty: nem
tags:
  - grovfritter
  - kartofler
  - parmesan
  - hvidløg
  - airfryer
  - fritter
imageAlt: Grovfritter vendt i parmesan, hvidløgsolie og frisk persille
featured: true
ingredients:
  - 800 g fastkogende kartofler, med skræl
  - 1½ spsk olivenolie
  - 2 fed hvidløg, finthakkede
  - 40 g parmesan, friskrevet
  - 2 spsk finthakket persille
  - Flagesalt og peber
steps:
  - Skær kartoflerne i tykke stave. Skyl 10 minutter i koldt vand. Tør grundigt.
  - Vend med 1 spsk olie og peber. Forvarm airfryeren til 200 °C.
  - Steg 12 minutter. Ryst. Steg yderligere 8–10 minutter, til kanterne er dybt gyldne.
  - Varm ½ spsk olie med hvidløg i 20–30 sekunder i en lille pande (eller 1 minut i airfryeren i et lille fad) — hvidløget skal dufte, ikke brune.
  - Hæld de varme fritter i en skål. Vend hurtigt med hvidløgsolie, parmesan og persille.
  - Flagesalt. Server med det samme, mens osten stadig klæber.
faq:
  - question: Hvorfor parmesan efter stegning?
    answer: Parmesan i kurven fra start brænder. Friskrevet ost smelter let på varme fritter og giver skorpe uden bitterhed.
  - question: Kan man bruge ovn?
    answer: Ja. 220 °C i 35–40 minutter, vend halvvejs. Samme topping bagefter.
  - question: Hvidløgspulver i stedet?
    answer: Det kan komme på før stegning. Frisk hvidløgsolie efter er den luksuriøse version.
  - question: Hvilken ost?
    answer: Parmigiano Reggiano eller Grana Padano. Forrevet fra pose smager fladere og smelter dårligere.
body: |
  Hvidløg- og parmesan-grovfritter er den version, der forsvinder fra skålen først.

  Steg fritterne færdige. Vend dem varme i hvidløgsolie, friskrevet parmesan og persille.

  Osten skal klæbe — ikke ligge som et tørt lag i bunden.
tip: Riv parmesanen fint på den fine side af rivejernet. Jo finere, jo bedre klæber den til de varme stave.
=====
title: Rosmarin- og havsalt-grovfritter
slug: rosmarin-havsalt-grovfritter
category: ovn
description: Rosmarin- og havsalt-grovfritter — gastropub-klassikeren med knust salt og friske krydderurter.
prepTime: PT20M
cookTime: PT40M
totalTime: PT1H
servings: 4
difficulty: nem
tags:
  - grovfritter
  - kartofler
  - rosmarin
  - havsalt
  - ovn
  - fritter
imageAlt: Ovnstegte grovfritter med frisk rosmarin og knust havsalt
featured: true
ingredients:
  - 1 kg bagekartofler, med skræl
  - 3 spsk olivenolie
  - 2–3 kviste frisk rosmarin
  - 1 tsk knust havsalt (eller flagesalt)
  - Friskkværnet peber
  - Valgfrit: 1 fed hvidløg, smadret
steps:
  - Tænd ovnen på 220 °C. Skær kartoflerne i tykke stave. Skyl, tør knastørt.
  - Vend med olie, peber og halvdelen af rosmarinen (bladene pillet af). Fordel i ét lag på to plader.
  - Bag 20 minutter. Vend. Læg evt. smadret hvidløg og resten af rosmarinen på pladen.
  - Bag yderligere 15–20 minutter, til kanterne er knasende og midten fluffy.
  - Knus havsalt let i morter eller mellem fingrene. Drys over lige før servering.
faq:
  - question: Frisk eller tørret rosmarin?
    answer: Frisk er gastropub-versionen. Tørret: brug halv dosis, og kom den på efter 25 minutter, så den ikke brænder.
  - question: Hvorfor knust salt til sidst?
    answer: Salt på rå stave trækker vand ud. Knust havsalt til sidst giver crunch og smag uden at gøre dem slatne.
  - question: Melede eller fastkogende?
    answer: Melede/bagekartofler giver fluffy midte. Fastkogende bliver mere voksagtige — stadig gode, bare anden tekstur.
  - question: Airfryer?
    answer: 200 °C i 20–24 minutter. Rosmarin til sidste 5 minutter.
body: |
  Rosmarin- og havsalt-grovfritter er den klassiske pub-side: tykke stave, urteduft, knust salt.

  Høj varme. Én etage. Salt til sidst.

  De skal dufte af rosmarin, når du åbner ovnen — ikke af brændt kvist.
tip: Læg hele rosmarinkviste under stavene de sidste 10 minutter, hvis du vil have aroma uden brændte nåle på fritterne.
=====
title: Grovfritter i støbejernsgryde
slug: grovfritter-stoebejaernsgryde
category: stobejern
description: Grovfritter af bagekartofler i støbejernsgryde — dobbeltstegte i Dutch oven med olie eller oksefedt.
prepTime: PT25M
cookTime: PT35M
totalTime: PT1H
servings: 4
difficulty: mellem
tags:
  - grovfritter
  - kartofler
  - støbejern
  - dutch oven
  - fritter
  - oksefedt
imageAlt: Dobbeltstegte grovfritter i støbejernsgryde med gylden skorpe
featured: true
ingredients:
  - 1 kg bagekartofler
  - 6–8 dl neutral olie eller 400 g oksefedt (nok til at dække stavene)
  - 1 tsk flagesalt
steps:
  - Skær kartoflerne i tykke stave (ca. 1,5 cm). Skyl til vandet er klart. Tør helt.
  - Varm olien/fedtet i støbejernsgryden til ca. 150–160 °C (en stav skal boble roligt).
  - Steg første omgang 6–8 minutter i hold — midten skal være mør, skorpen stadig bleg. Løft op på rist.
  - Hæv temperaturen til 180–190 °C. Steg anden omgang 3–5 minutter, til de er dybt gyldne og knaser.
  - Dræn på rist eller køkkenrulle. Flagesalt med det samme.
faq:
  - question: Hvorfor to omgange?
    answer: Første lave varme koger midten. Anden høje varme laver skorpe. Én omgang giver enten rå midte eller brændt skal.
  - question: Olie eller oksefedt?
    answer: Oksefedt smager dybere og knaser klassisk. Neutral olie er billigere og mere hverdagsagtig. Bland gerne.
  - question: Kan man genbruge fedtet?
    answer: Ja, når det er afkølet og siet. Opbevar køligt. Smid det ud, hvis det lugter harsk eller er meget mørkt.
  - question: Uden friture i gryden?
    answer: Du kan ovnstege på støbejernsplade med lidt fedt — men denne opskrift er den ægte dobbeltstegte version.
body: |
  Grovfritter i støbejernsgryde er den gamle skole: to temperaturer, én gryde, rigtig skorpe.

  Dutch oven holder varmen stabil. Det er derfor fritterne bliver jævnt gyldne.

  Salt dem, mens de stadig damper.
tip: Brug et slikketermometer. Gæt ikke på 160 versus 190 — forskellen er fluffy midte versus rå stav.
=====
title: Røgede grovfritter på grillen
slug: rogede-grovfritter-grill
category: roeg
description: Røgede grovfritter på grillen — indirekte varme med æble- eller hickory-rygesmuld og knasende kant.
prepTime: PT20M
cookTime: PT50M
totalTime: PT1H10M
servings: 4
difficulty: mellem
tags:
  - grovfritter
  - kartofler
  - røg
  - grill
  - fritter
  - rygesmuld
imageAlt: Røgede grovfritter fra grillen med gylden skorpe og røgaroma
featured: true
ingredients:
  - 1 kg bagekartofler, med skræl
  - 2 spsk olivenolie eller andefedt
  - 1 håndfuld æble- eller hickory-rygesmuld (gennemblødt 20 min)
  - 1 tsk flagesalt
  - Peber
  - Valgfrit: ½ tsk røget paprika
steps:
  - Skær kartoflerne i tykke stave. Skyl, tør. Vend med olie, peber og evt. røget paprika.
  - Forbered grillen til indirekte varme ca. 180–190 °C. Læg rygesmuld på gløderne eller i en røgboks.
  - Læg stavene på rist over den indirekte zone (eller på en plancha væk fra direkte ild). Luk låget.
  - Røg/steg 35–40 minutter. Vend halvvejs. Til sidst kan du flytte dem kort over direkte varme for ekstra skorpe (2–3 minutter pr. side).
  - Flagesalt. Server med det samme.
faq:
  - question: Æble eller hickory?
    answer: Æble er mildt og sødt — godt til kartofler. Hickory er kraftigere og mere BBQ. Start med æble, hvis du er i tvivl.
  - question: Bliver de sprøde nok kun med røg?
    answer: Indirekte varme giver aroma. Den sidste direkte finish giver knas. Uden finish bliver de mere som røgede kartoffelstave.
  - question: Gasgrill?
    answer: Ja — brug røgboks eller rygechips i en foliebakke over en brænder. Hold 180–190 °C med låget lukket.
  - question: For meget røg?
    answer: En håndfuld smuld er nok. Konstant tyk hvid røg gør dem bitre.
body: |
  Røgede grovfritter på grillen er kartoffel med lejrbål — uden at de smager af askebæger.

  Indirekte varme til midten. Lidt rygesmuld til aroma. Kort direkte varme til knas.

  De hører til ved burgersessionen, ikke i mikroovnen dagen efter.
tip: Læg stavene på en kold rist først, så de ikke klæber, når du flytter dem til grillen.
=====
title: Chili- og spidskommen-grovfritter
slug: chili-spidskommen-grovfritter
category: airfryer
description: Chili- og spidskommen-grovfritter — spicy, grove fritter med masser af kant til burgersessionen.
prepTime: PT15M
cookTime: PT22M
totalTime: PT37M
servings: 4
difficulty: nem
tags:
  - grovfritter
  - kartofler
  - chili
  - spidskommen
  - airfryer
  - fritter
imageAlt: Spicy grovfritter med chili og spidskommen fra airfryeren
featured: true
ingredients:
  - 800 g fastkogende kartofler, med skræl
  - 1½ spsk olivenolie
  - 1 tsk stødt spidskommen
  - ½–1 tsk chiliflager (eller ½ tsk cayenne)
  - ½ tsk røget paprika
  - ½ tsk salt
  - ¼ tsk hvidløgspulver
steps:
  - Skær kartoflerne i tykke stave. Skyl 10 minutter. Tør grundigt.
  - Bland olie med spidskommen, chili, paprika, salt og hvidløgspulver. Vend stavene, til de er jævnt dækket.
  - Forvarm airfryeren til 200 °C. Steg 12 minutter. Ryst.
  - Steg yderligere 8–10 minutter, til kanterne er knasende og krydderierne dufter ristede — ikke brændte.
  - Smag til med ekstra flagesalt eller chiliflager.
faq:
  - question: For stærke?
    answer: Start med ½ tsk chiliflager. Du kan altid drysse mere på efter stegning.
  - question: Hele spidskommenfrø?
    answer: Ja — rist dem let i en tør pande først, knus dem, og vend med olien. Mere aroma end pulver.
  - question: Til hvad?
    answer: Smash burgers, pulled pork, grillkylling eller bare med yoghurt-dip.
  - question: Ovn?
    answer: 220 °C i 35–40 minutter på to plader. Vend halvvejs.
body: |
  Chili- og spidskommen-grovfritter er burgersessionens spicy side.

  Krydderierne skal ristes af varmen — ikke brænde. Derfor olie som lim, og høj varme i kort tid.

  De skal have kant, både i smag og tekstur.
tip: Har du sukker i chili-blandingen (fx færdig taco-mix), kom det først på de sidste 5 minutter — ellers brænder det.
=====
title: Polenta-fritter med rosmarin
slug: polenta-fritter-rosmarin
category: airfryer
description: Polenta-fritter med rosmarin — sprøde majsfritter bagt eller airfryet som tilbehør eller snack.
prepTime: PT20M
cookTime: PT25M
totalTime: PT2H45M
servings: 4
difficulty: mellem
tags:
  - polenta
  - fritter
  - rosmarin
  - airfryer
  - snack
  - vegetar
imageAlt: Sprøde polenta-fritter med rosmarin og flagesalt
featured: true
ingredients:
  - 2 dl polenta (majsgryn til grød)
  - 8 dl vand eller let bouillon
  - 1 tsk salt
  - 1 spsk smør eller olivenolie
  - 1 spsk finthakket frisk rosmarin
  - 2 spsk olivenolie til pensling
  - 30 g parmesan, reven (valgfrit)
  - Flagesalt
steps:
  - Kog vand/bouillon med salt op. Drys polenta i under piskning. Kog under omrøring 8–10 minutter til en tyk grød. Rør smør, rosmarin og evt. parmesan i.
  - Fordel i et tyndt lag (ca. 1,5 cm) på et bakkeånd papirbelagt fad. Køl mindst 2 timer (eller natten over), til den er fast.
  - Skær i stave som fritter. Pensl let med olie.
  - Forvarm airfryeren til 200 °C. Steg 12 minutter. Vend forsigtigt. Steg 8–10 minutter mere, til kanterne er knasende.
  - Flagesalt. Server varme med aioli eller marinara.
faq:
  - question: Instant eller traditionel polenta?
    answer: Begge virker. Instant er hurtigere. Traditionel smager lidt dybere — følg pakkens kogetid.
  - question: Hvorfor køle dem?
    answer: Varm polenta falder fra hinanden. Den skal være køleskabsfast, før du skærer stave.
  - question: Ovn i stedet?
    answer: 220 °C i 25–30 minutter, vend halvvejs. Pensl med olie, så de bruner.
  - question: Kan man fryse dem?
    answer: Ja — skær stave, frys på bakke, pose dem. Airfry direkte fra frost + 3–4 minutter.
body: |
  Polenta-fritter med rosmarin er majs med knas — uden kartoffel.

  Kog grøden. Køl den hård. Skær stave. Høj varme.

  Ideelle som snack med dip eller som tilbehør til grillmad.
tip: Skær stavene med en våd kniv. Polentaen klæber mindre, og kanterne bliver renere.
=====
title: Pastinak- og persillerodsfritter
slug: pastinak-persillerod-fritter
category: airfryer
description: Pastinak- og persillerodsfritter — grove, sødmefulde rødder med højt smæk på guldskorpen i airfryer.
prepTime: PT15M
cookTime: PT20M
totalTime: PT35M
servings: 4
difficulty: nem
tags:
  - pastinak
  - persillerod
  - fritter
  - rodfrugter
  - airfryer
  - tilbehør
imageAlt: Pastinak- og persillerodsfritter med gylden skorpe fra airfryeren
featured: true
ingredients:
  - 400 g pastinak
  - 400 g persillerod
  - 1½ spsk olivenolie
  - 1 tsk flagesalt
  - Friskkværnet peber
  - Valgfrit: ½ tsk tørret timian
steps:
  - Skræl rødderne. Skær i ens fritter à ca. 1–1,5 cm. Tør overfladen — skyl kun hvis de er jordede, og tør bagefter.
  - Vend med olie, peber og evt. timian.
  - Forvarm airfryeren til 190 °C. Steg 10 minutter. Ryst forsigtigt.
  - Steg yderligere 8–10 minutter, til kanterne er karamelliserede og midten mør.
  - Flagesalt. Server med det samme.
faq:
  - question: Hvorfor 190 °C og ikke 200?
    answer: Pastinak og persillerod har mere sukker end kartoffel. Lidt lavere varme giver guldskorpe uden brændte spidser.
  - question: Kun den ene rod?
    answer: Ja. Blandingen giver både sødme (pastinak) og jordnær dybde (persillerod).
  - question: Med kartoffel?
    answer: Du kan blande 200 g kartoffel i for ekstra stivelse og knas — se også vores rodfrugtsfritter i ovn.
  - question: Slatne fritter?
    answer: For fuld kurv, eller for våde stave. Tør dem, og arbejd i to hold.
body: |
  Pastinak- og persillerodsfritter er efterårets søde, grove fritter.

  Sukkeret i rødderne laver guldskorpe af sig selv — du skal bare holde dem tørre og give dem plads.

  Salt til sidst. De er færdige, når spidserne er mørke og midten giver efter.
tip: Skær dem ens. Pastinak er ofte tykkere i den ene ende — del de tykke stykker på langs, så alt er færdigt samtidigt.
=====
title: Gulerodsfritter med timian
slug: gulerodsfritter-timian
category: airfryer
description: Gulerodsfritter med timian — hurtigt tilbehør, der karamelliserer perfekt under høj varme i airfryer.
prepTime: PT10M
cookTime: PT18M
totalTime: PT28M
servings: 3
difficulty: nem
tags:
  - gulerod
  - fritter
  - timian
  - airfryer
  - tilbehør
  - vegetar
imageAlt: Gulerodsfritter med timian og flagesalt fra airfryeren
featured: true
ingredients:
  - 700 g gulerødder
  - 1½ spsk olivenolie
  - 1 tsk frisk timian (eller ½ tsk tørret)
  - ½ tsk flagesalt
  - Peber
  - Valgfrit: ½ tsk honning de sidste 3 minutter
steps:
  - Skræl gulerødderne. Skær i fritter à ca. 1 cm. Tør dem.
  - Vend med olie, timian og peber.
  - Forvarm airfryeren til 195 °C. Steg 10 minutter. Ryst.
  - Steg yderligere 6–8 minutter, til kanterne er karamelliserede. Evt. pensl med honning de sidste 3 minutter.
  - Flagesalt. Server varme.
faq:
  - question: Bliver gulerodsfritter sprøde?
    answer: Kanterne knaser, midten bliver mør og sød — ikke som kartoffel-knas. Det er meningen.
  - question: Baby-gulerødder?
    answer: De er fine halveret på langs. Hold øje med tiden — de er færdige hurtigere.
  - question: Ovn?
    answer: 210 °C i 25–30 minutter på én etage. Vend halvvejs.
  - question: Til hvad?
    answer: Stegt kylling, lam, falafel eller som snack med yoghurt.
body: |
  Gulerodsfritter med timian er det hurtige tilbehør, der ser ud af mere end det er.

  Høj varme karamelliserer sukkeret. Timian holder dem salte i næsen.

  Honning er valgfrit — og kun til sidst.
tip: Undgå for tynde stave. Under 8 mm brænder de, før midten er mør.
=====
title: Loaded grovfritter med pulled pork og BBQ
slug: loaded-grovfritter-pulled-pork
category: airfryer
description: Loaded grovfritter med pulled pork og BBQ — restemad gratineret i airfryer eller ovn.
prepTime: PT15M
cookTime: PT25M
totalTime: PT40M
servings: 4
difficulty: nem
tags:
  - grovfritter
  - kartofler
  - pulled pork
  - BBQ
  - loaded
  - airfryer
  - festmad
imageAlt: Loaded grovfritter med pulled pork, BBQ-sauce og smeltet ost
featured: true
ingredients:
  - 800 g grovfritter (hjemmelavede eller frosne)
  - 300–400 g pulled pork (rester eller færdiglavet)
  - 1 dl BBQ-sauce
  - 100 g cheddar eller mozzarella, reven
  - 2 forårsløg, skåret tyndt
  - Valgfrit: syltede jalapeños og creme fraiche
steps:
  - Steg grovfritterne i airfryeren ved 200 °C i 15–20 minutter (ryst halvvejs), til de er sprøde.
  - Varm pulled pork med ½ dl BBQ-sauce i en gryde eller 2–3 minutter i airfryeren i et fad.
  - Fordel fritterne i et ovnfast fad eller airfryer-bakke. Top med pulled pork, resten af BBQ-saucen og osten.
  - Gratinér 3–5 minutter ved 180 °C, til osten bobler.
  - Drys forårsløg (og jalapeños). Server med creme fraiche.
faq:
  - question: Kun rester?
    answer: Rester er pointen — men færdig pulled pork fra køledisken virker også midt i ugen.
  - question: Ovn i stedet for airfryer?
    answer: Ja. Fritterne 220 °C i 35–40 minutter. Gratinér med topping 5–7 minutter ved 200 °C.
  - question: Hvilken ost?
    answer: Cheddar til BBQ-smag. Mozzarella til mere tråd. Bland gerne.
  - question: Kan man bruge kylling?
    answer: Ja — pulled chicken eller strimlet grillkylling med samme sauce.
body: |
  Loaded grovfritter med pulled pork og BBQ er restemad på sit højeste.

  Først fritterne sprøde. Så kød og ost. Kort gratinering.

  Det er en session — ikke et pænt anrettet tilbehør.
tip: Varm kødet separat, før det lander på fritterne. Koldt kød køler skorpen ned, før osten er smeltet.
=====
title: Grovfritter med bacon-cheese sauce
slug: grovfritter-bacon-cheese-sauce
category: airfryer
description: Grovfritter med bacon-cheese sauce — hjemmelavet ostesovs hældt over rygende varme, rustikke fritter.
prepTime: PT20M
cookTime: PT25M
totalTime: PT45M
servings: 4
difficulty: mellem
tags:
  - grovfritter
  - kartofler
  - bacon
  - ostesovs
  - cheese sauce
  - airfryer
  - snack
imageAlt: Rustikke grovfritter overhældt med bacon-cheese sauce
featured: true
ingredients:
  - 800 g grovfritter (hjemmelavede eller frosne)
  - 100 g bacon, i tern
  - 1 spsk smør
  - 1 spsk hvedemel
  - 2 dl sødmælk
  - 80 g cheddar, reven
  - 40 g mozzarella eller ekstra cheddar
  - Peber og en snert salt
  - Valgfrit: ½ tsk dijonsennep
steps:
  - Steg grovfritterne sprøde i airfryeren ved 200 °C (ca. 18–22 minutter). Hold dem varme.
  - Steg bacontern sprøde på panden. Løft op. Gem 1 spsk baconfedt i panden.
  - Smelt smør med baconfedtet. Rør mel i, og lad det boble 1 minut. Tilsæt mælk under piskning. Kog til en tyk sauce.
  - Tag panden af varmen. Rør ostene i (og evt. dijon), til saucen er blank. Smag til med peber.
  - Hæld saucen over de varme fritter. Drys bacon over. Server med det samme.
faq:
  - question: Saucen bliver klumpet?
    answer: Pisk konstant, når mælken kommer i, og hold varmen middel. Si den om nødvendigt — den er reddet.
  - question: Kan man lave saucen før?
    answer: Ja, op til en dag. Genopvarm forsigtigt med en skvæt mælk. Fritterne skal være ny-stegte.
  - question: Uden bacon?
    answer: Ja — ren cheese sauce. Eller brug røget paprika for dybde.
  - question: Forskel på chili-cheese pommes?
    answer: Chili-cheese smelter ost direkte på fritterne. Her er det en rigtig bechamel-ostesovs med bacon.
body: |
  Grovfritter med bacon-cheese sauce er den tunge snack-bakke: rustikke fritter, varm ostesovs, sprødt bacon.

  Saucen skal være blank og hældbar — ikke en osteklump.

  Hæld den over lige før servering, ellers æder den knasen.
tip: Riv osten selv. Forrevet ost med anti-klump midler gør saucen kornet.
=====
title: Trøffel- og parmesanfritter
slug: troeffel-parmesan-fritter
category: airfryer
description: Trøffel- og parmesanfritter — den luksuriøse variant med god trøffelolie og flagesalt.
prepTime: PT15M
cookTime: PT22M
totalTime: PT37M
servings: 4
difficulty: nem
tags:
  - grovfritter
  - kartofler
  - trøffel
  - parmesan
  - airfryer
  - festmad
  - fritter
imageAlt: Grovfritter med trøffelolie, parmesan og flagesalt
featured: true
ingredients:
  - 800 g fastkogende kartofler, med skræl
  - 1½ spsk olivenolie
  - 1–1½ tsk god trøffelolie
  - 40 g parmesan, friskrevet
  - Flagesalt
  - Friskkværnet peber
  - Valgfrit: 1 spsk finthakket persille
steps:
  - Skær kartoflerne i tykke stave. Skyl, tør. Vend med olivenolie og peber.
  - Forvarm airfryeren til 200 °C. Steg 12 minutter. Ryst. Steg 8–10 minutter mere, til de er knasende.
  - Hæld fritterne i en skål. Dryp trøffelolie over — start med 1 tsk, smag, tilføj mere.
  - Vend med parmesan og evt. persille. Flagesalt. Server med det samme.
faq:
  - question: Hvilken trøffelolie?
    answer: En du faktisk kan lide duften af. Billig trøffelolie kan smage kemisk — mindre er mere.
  - question: Trøffelmayo i stedet?
    answer: God idé til dip. Oliven på fritterne + mayo ved siden giver dobbelt trøffel uden at overdøve.
  - question: Kan man bruge ægte trøffel?
    answer: Ja — høvl sort trøffel over til sidst, hvis budgettet er til det. Oliven er hverdags-luksus.
  - question: Ovn?
    answer: 220 °C i 35–40 minutter. Samme topping efter stegning.
body: |
  Trøffel- og parmesanfritter er den luksuriøse bakke til vin og weekend.

  Steg fritterne færdige. Trøffelolie og parmesan kommer efter — varmen åbner aromaen.

  Flagesalt lukker det af.
tip: Dryp olien på skålen først, så vend fritterne i den. Du fordeler aromaen bedre end med dryp ovenpå.
=====
title: Poutine med grovfritter og brun sovs
slug: poutine-grovfritter
category: ovn
description: Poutine med grovfritter — den canadiske klassiker med cheese curds (eller mozzarella) og masser af skysovs.
prepTime: PT25M
cookTime: PT45M
totalTime: PT1H10M
servings: 4
difficulty: mellem
tags:
  - poutine
  - grovfritter
  - kartofler
  - brun sovs
  - cheese curds
  - ovn
  - festmad
imageAlt: Poutine med grovfritter, cheese curds og brun sovs
featured: true
ingredients:
  - 1 kg bagekartofler til grovfritter
  - 3 spsk olivenolie
  - 150–200 g cheese curds (eller mozzarella i tern, tempereret)
  - 4 dl god brun sovs / skysovs (gerne lidt tykkere end til frikadeller)
  - Flagesalt og peber
steps:
  - Lav rustikke grovfritter: skær stave, skyl, tør, vend med olie. Bag ved 220 °C i 35–40 minutter, vend halvvejs, til de er knasende.
  - Varm den brune sovs op, til den er dampende — ikke kogende vildt.
  - Læg fritterne i en dyb skål eller bakke. Fordel cheese curds (de skal være tempererede, ikke lige fra køl).
  - Hæld den varme sovs over, så osten begynder at blødgøre uden at smelte helt væk.
  - Peber og evt. flagesalt. Spis med det samme.
faq:
  - question: Hvad hvis jeg ikke kan få cheese curds?
    answer: Mozzarella i tern (ikke forrevet) er den bedste danske stand-in. Temperér dem 20 minutter uden for køl.
  - question: Hvilken sovs?
    answer: En kraftig skysovs eller gravy. Den skal kunne bære fritterne uden at være tynd som bouillon.
  - question: Airfryer-fritter?
    answer: Ja — steg grovfritterne færdige i airfryeren, og saml poutinen i skålen bagefter.
  - question: Kan man lave det på forhånd?
    answer: Nej. Poutine dør, når den venter. Fritterne, osten og sovsen skal mødes varme.
body: |
  Poutine med grovfritter er den canadiske klassiker: sprøde stave, squeaky ost, brun sovs.

  Rækkefølgen er hellig. Fritter. Ost. Varm sovs.

  Osteternene skal blødgøre — ikke forsvinde i en ostesuppe.
tip: Sovsen skal være varmere end fritterne. Det er varmen fra sovsen, der vækker cheese curds.
=====
title: Asiatiske sticky fritter
slug: sticky-fritter-soja-honning
category: airfryer
description: Asiatiske sticky fritter — grovfritter vendt i en hurtig glaze af soja, honning, sesam og chili.
prepTime: PT15M
cookTime: PT22M
totalTime: PT37M
servings: 4
difficulty: nem
tags:
  - grovfritter
  - kartofler
  - soja
  - sticky
  - chili
  - airfryer
  - fritter
imageAlt: Sticky fritter vendt i soja-honning-glaze med sesam og chili
featured: true
ingredients:
  - 800 g grovfritter (kartofler, med skræl)
  - 1½ spsk olivenolie
  - 2 spsk sojasauce
  - 1½ spsk honning
  - 1 tsk sesamolie
  - 1 tsk ristet sesam
  - ½–1 tsk chiliflager
  - 1 fed hvidløg, finthakket
  - 2 forårsløg, skåret tyndt
steps:
  - Skær og steg grovfritterne sprøde i airfryeren ved 200 °C i 18–22 minutter (olie på før stegning).
  - Mens de steger: bland soja, honning, sesamolie, chili og hvidløg i en lille gryde. Kog op 1–2 minutter til en tyk glaze.
  - Hæld de færdige fritter i en skål. Vend hurtigt med glazen.
  - Drys sesam og forårsløg over. Server med det samme.
faq:
  - question: Bliver de ikke slatne af glazen?
    answer: Jo, hvis de venter. Vend og spis. Glazen skal være tyk, ikke en sø af sauce.
  - question: Sød eller stærk?
    answer: Honning giver sticky-sødme. Chiliflager styrer heden — start lavt.
  - question: Kan man bruge frosne fritter?
    answer: Ja. Steg dem ekstra sprøde først — glazen blødgør dem en smule.
  - question: Teriyaki i stedet?
    answer: En tyk teriyaki virker. Undgå tynde stir-fry-saucer, der drukner fritterne.
body: |
  Asiatiske sticky fritter er snack med glaze: soja, honning, sesam, chili.

  Fritterne skal være færdige og knasende, før saucen rammer.

  Vend. Drys. Spis. Punktum.
tip: Reducér glazen, til den coat'er bagsiden af en ske. For tynd sauce = våde fritter.
=====
title: Grovfritter med hvidløgsmayo og sprøde løg
slug: grovfritter-hvidloegsmayo-sproede-loeg
category: airfryer
description: Grovfritter med hvidløgsmayo og sprøde løg — nem snack-bakke med masser af crunch.
prepTime: PT15M
cookTime: PT22M
totalTime: PT37M
servings: 4
difficulty: nem
tags:
  - grovfritter
  - kartofler
  - hvidløgsmayo
  - sprøde løg
  - airfryer
  - snack
  - fritter
imageAlt: Grovfritter med hvidløgsmayo og sprøde løg på toppen
featured: true
ingredients:
  - 800 g fastkogende kartofler, med skræl
  - 1½ spsk olivenolie
  - 1 dl mayonnaise
  - 1–2 fed hvidløg, presset
  - 1 tsk citronsaft
  - 4–5 spsk sprøde stegte løg (købte eller hjemmelavede)
  - Flagesalt og peber
  - Valgfrit: finthakket persille
steps:
  - Skær kartoflerne i tykke stave. Skyl, tør. Vend med olie og peber.
  - Steg i airfryeren ved 200 °C i 12 + 8–10 minutter, til de er knasende.
  - Rør mayo med hvidløg og citronsaft. Smag til med salt.
  - Læg fritterne på en bakke. Dryp eller dollop hvidløgsmayo over. Drys generøst med sprøde løg og evt. persille.
  - Server med det samme, så løgene forbliver knasende.
faq:
  - question: Hjemmelavede sprøde løg?
    answer: Ja — tynde skalotteløg vendt i mælk og mel, stegt gyldne. Købte fra posen er den hurtige hverdagsversion.
  - question: Aioli i stedet for mayo?
    answer: Endnu bedre, hvis du har den. Ellers er presset hvidløg i mayo fine på 30 sekunder.
  - question: Mayo under eller ved siden af?
    answer: Begge dele. Lidt på toppen til crunch-kontrast, resten som dip, så ikke alle fritter bliver våde.
  - question: Ovn?
    answer: 220 °C i 35–40 minutter. Samme topping.
body: |
  Grovfritter med hvidløgsmayo og sprøde løg er snack-bakken med dobbelt crunch.

  Varme fritter. Kold, skarp mayo. Løg der knaser mellem tænderne.

  Den er færdig på den tid, det tager at røre mayo.
tip: Drys løgene på lige før servering — selv 5 minutter på mayo blødgør dem.
=====
title: Gyros-style loaded frites
slug: gyros-style-loaded-frites
category: airfryer
description: Gyros-style loaded frites — grovfritter toppet med stegt kylling eller svinekød, rødløg og masser af tzatziki.
prepTime: PT20M
cookTime: PT25M
totalTime: PT45M
servings: 4
difficulty: nem
tags:
  - grovfritter
  - kartofler
  - gyros
  - tzatziki
  - loaded
  - airfryer
  - festmad
imageAlt: Gyros-style loaded frites med kød, rødløg og tzatziki
featured: true
ingredients:
  - 800 g grovfritter
  - 400 g kyllingebryst eller svinekam, i tynde strimler
  - 1 spsk olivenolie
  - 1 tsk oregano
  - 1 tsk paprika
  - ½ tsk hvidløgspulver
  - ½ tsk salt
  - 1 lille rødløg, tyndt skåret
  - 2 dl tzatziki
  - Valgfrit: cherrytomater, persille, chili
steps:
  - Steg grovfritterne sprøde i airfryeren ved 200 °C (18–22 minutter).
  - Vend kødet med olie, oregano, paprika, hvidløgspulver og salt. Steg på panden eller i airfryeren ved 200 °C i 8–10 minutter, til det er gennemstegt og får kant.
  - Fordel fritterne på en bakke. Top med kødet, rødløg og generøse klattezatziki.
  - Drys persille og evt. chili. Server med det samme.
faq:
  - question: Kylling eller svin?
    answer: Begge er klassisk gyros-agtige. Svin er mere street food. Kylling er lettere midt i ugen.
  - question: Købt eller hjemmelavet tzatziki?
    answer: Begge. Hjemmelavet medpresset agurk smager skarpere og holder fritterne bedre selskab.
  - question: Kan man bruge gyroskød fra grillen?
    answer: Ja — det er den bedste version. Varm det og saml bakken.
  - question: Vegetarisk?
    answer: Stegte halloumi-strimler eller kikærter med samme krydderi fungerer som topping.
body: |
  Gyros-style loaded frites er street food på bakke: grovfritter i bunden, krydret kød, rødløg, tzatziki.

  Fritterne skal være sprøde nok til at holde til toppingen.

  Det er ikke pænt. Det er mættende.
tip: Læg tzatziki i klattez i stedet for at smøre hele bakken — så bevarer du knas i midten.
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
publishedAt: 2026-10-15
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
for b in blocks:
    d = parse_block(b)
    assert d.get("slug"), "missing slug"
    assert d.get("faq") and len(d["faq"]) >= 3, d.get("slug")
    assert d.get("tip"), d.get("slug")
    assert d.get("body"), d.get("slug")
    out = ROOT / d["category"]
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{d['slug']}.mdx"
    if path.exists():
        raise SystemExit(f"slug collision: {path}")
    path.write_text(to_mdx(d), encoding="utf-8")
    print("wrote", d["category"] + "/" + path.name)
