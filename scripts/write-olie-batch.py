#!/usr/bin/env python3
"""30 smagsolier — chiliolie, urteolier og fedt-olier (okt 2026)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"
PUBLISHED = "2026-10-18"

RECIPES = r'''
=====
title: Klassisk chiliolie
slug: chiliolie
category: dips
description: Klassisk chiliolie med chiliflager — varm, rød og klar til pizza, pasta og æg.
prepTime: PT5M
cookTime: PT10M
totalTime: PT15M
servings: 12
difficulty: nem
tags:
  - chiliolie
  - chili
  - olie
  - smagsolie
  - pizza
  - pasta
imageAlt: Klar rød chiliolie i glas med chiliflager
featured: true
ingredients:
  - 2 dl neutral olie (solsikke eller rapsolie)
  - 3 spsk tørrede chiliflager
  - 1 tsk salt
  - Evt. 1 knust fed hvidløg
  - Evt. ½ tsk røget paprika
steps:
  - Kom chiliflager, salt og evt. hvidløg/paprika i et rent, varmeresistent glas.
  - Varm olien i en lille gryde til ca. 120–130 °C — den skal dirre, ikke røge.
  - Hæld olien over flagerne. Det skal bruse let. Rør rundt.
  - Lad køle til stuetemperatur. Si hvidløg fra hvis du brugte det. Opbevar køligt.
faq:
  - question: Hvor stærk bliver den?
    answer: Det afhænger af flagerne. Start med 2 spsk, smag efter en time, og tilsæt mere hvis du vil.
  - question: Kan jeg bruge olivenolie?
    answer: Ekstra jomfru olivenolie bliver bitter ved høj varme. Brug neutral olie til infusionen, eller bland senere.
  - question: Holdbarhed?
    answer: Uden frisk hvidløg 2–3 uger i køleskab. Med frisk hvidløg max 1 uge, og altid køligt.
body: |
  Klassisk chiliolie er varm olie over tørrede flager — simpel, hurtig og mere kontrolleret end frisk chili i olie.

  Temperaturen er vigtig. For kold olie giver flad smag. For varm olie brænder flagerne bittert.
tip: Dryp over pizza, ramen, scrambled eggs eller grillede grøntsager lige før servering.
=====
title: Chili crisp
slug: chili-crisp
category: dips
description: Chili crisp — knasende chiliolie med hvidløg, skalotteløg og sesam til ris, nudler og dumplings.
prepTime: PT15M
cookTime: PT20M
totalTime: PT35M
servings: 16
difficulty: mellem
tags:
  - chili-crisp
  - chiliolie
  - olie
  - asiatisk
  - dumpling
  - smagsolie
imageAlt: Skål med knasende rød chili crisp og sesam
featured: true
ingredients:
  - 2½ dl neutral olie
  - 4 fed hvidløg, tyndt skåret
  - 2 skalotteløg, tyndt skåret
  - 4 spsk tørrede chiliflager
  - 1 spsk gochugaru eller ekstra chiliflager
  - 1 spsk sesamfrø
  - 1 tsk salt
  - ½ tsk sukker
  - Evt. 1 tsk sojasauce
steps:
  - Varm olien på middel lav varme. Steg hvidløg og skalotteløg, til de er gyldne og knasende (8–12 min). Tag dem op med hulske.
  - Kom chiliflager, gochugaru, sesam, salt og sukker i en varmeresistent skål.
  - Hæld den varme olie over. Rør. Læg det stegte hvidløg og løg tilbage i.
  - Smag til med sojasauce hvis du vil. Lad køle. Opbevar i køleskab.
faq:
  - question: Hvidløg bliver sort?
    answer: Varmen er for høj. Hold under 150 °C og rør ofte. Sort = bitter.
  - question: Er det det samme som chiliolie?
    answer: Nej — chili crisp har knas. Chiliolie er mere flydende. Begge er gode; crisp er topping.
  - question: Holdbarhed?
    answer: 2–3 uger i køleskab. Brug ren ske, så den ikke surer.
body: |
  Chili crisp er knas i olie — hvidløg og løg steges først, flagerne vækkes bagefter.

  Sukkeret er ikke til sødme. Det balancerer bitterheden fra de brasede flager.
tip: Server over dampede dumplings, ris med æg eller stegte nudler. En skefuld er nok.
=====
title: Hvidløgs-chiliolie
slug: hvidloegs-chiliolie
category: dips
description: Hvidløgs-chiliolie — dobbelt smag til pasta, pizza og grillkød.
prepTime: PT10M
cookTime: PT15M
totalTime: PT25M
servings: 12
difficulty: nem
tags:
  - hvidloegs-chiliolie
  - chiliolie
  - hvidloeg
  - olie
  - pasta
  - smagsolie
imageAlt: Gyldenrød hvidløgs-chiliolie i glas med fed
featured: false
ingredients:
  - 2 dl neutral olie
  - 6 fed hvidløg, tyndt skåret
  - 2 spsk chiliflager
  - 1 tsk salt
  - Evt. 1 tsk chilipasta
steps:
  - Steg hvidløg i olien på lav varme, til det er lysgyldent (6–8 min). Tag af varmen.
  - Rør chiliflager, salt og evt. pasta i. Lad trække 10 minutter.
  - Si eller lad stykkerne blive i. Hæld på rent glas. Køl.
faq:
  - question: Er hvidløg i olie farligt?
    answer: Frisk hvidløg i olie skal altid på køl og bruges inden 1 uge. Frys portioner hvis du laver meget.
  - question: Kan jeg bruge hele fed?
    answer: Ja, men skiver giver mere smag hurtigere. Hele fed confiteres blødere.
  - question: Til hvad?
    answer: Spaghetti aglio e olio, pizza, brød, grillkylling og stegte grøntsager.
body: |
  Hvidløgs-chiliolie er to aromaer i én flaske — hvidløget steges blidt, chili får varmen bagefter.

  Hold varmen lav. Brændt hvidløg smager af aske, ikke fest.
tip: Dryp over mozzarella på toast med flagesalt — instant forret.
=====
title: Sichuan-peberolie
slug: sichuan-peberolie
category: dips
description: Sichuan-peberolie — nummen, citrusagtig peberolie til mapo, nudler og agurkesalat.
prepTime: PT5M
cookTime: PT10M
totalTime: PT15M
servings: 10
difficulty: nem
tags:
  - sichuan-peberolie
  - sichuan
  - olie
  - asiatisk
  - smagsolie
  - chiliolie
imageAlt: Gylden sichuan-peberolie med hele peberkorn
featured: false
ingredients:
  - 2 dl neutral olie
  - 3 spsk sichuan-peberkorn
  - 1 spsk chiliflager (valgfrit)
  - ½ tsk salt
steps:
  - Rist peberkornene tørt på panden 1–2 minutter, til de dufter. Knus let i morter.
  - Varm olien til ca. 120 °C. Tag af varmen. Kom peber og evt. chili i.
  - Lad trække 15–30 minutter. Si. Salt. Hæld på glas.
faq:
  - question: Hvad er «nummen»?
    answer: Sichuan-peber giver prikkende følelse (ma), ikke kun styrke (la). Det er meningen.
  - question: Kan jeg bruge almindelig peber?
    answer: Nej — smagen er helt anden. Find sichuan-peber i asiatiske butikker.
  - question: Holdbarhed?
    answer: 3–4 uger køligt, når den er siftet.
body: |
  Sichuan-peberolie er aroma uden brænd — peberkornene ristes først, så olien tager den citrusagtige duft.

  Si kornene fra. De smager bittert hvis de ligger for længe i olien.
tip: Dryp over agurkesalat med salt, eller over mapo tofu lige før servering.
=====
title: Gochugaru-olie
slug: gochugaru-olie
category: dips
description: Gochugaru-olie — koreansk chiliflageolie med sød varme til bibimbap, æg og stegte grøntsager.
prepTime: PT5M
cookTime: PT8M
totalTime: PT13M
servings: 12
difficulty: nem
tags:
  - gochugaru-olie
  - gochugaru
  - chiliolie
  - olie
  - koreansk
  - smagsolie
imageAlt: Rød gochugaru-olie i skål med chiliflager
featured: false
ingredients:
  - 2 dl neutral olie
  - 4 spsk gochugaru (koreanske chiliflager)
  - 1 tsk salt
  - ½ tsk sukker
  - Evt. 1 fed hvidløg, knust
steps:
  - Kom gochugaru, salt, sukker og evt. hvidløg i en varmeresistent skål.
  - Varm olien til ca. 120 °C. Hæld over flagerne under omrøring.
  - Lad køle. Si hvidløg fra. Opbevar køligt.
faq:
  - question: Gochugaru vs. almindelige flager?
    answer: Gochugaru er frugtigt og mildere. Almindelige flager er skarpere. Brug det du har — justér mængden.
  - question: Kan jeg bruge gochujang?
    answer: Nej til denne olie — pastaen brænder og klumper. Brug gochujang i saucer i stedet.
  - question: Holdbarhed?
    answer: 2–3 uger i køleskab uden frisk hvidløg.
body: |
  Gochugaru-olie er den koreanske genvej til rød farve og mild varme — flagerne skal bare møde varm olie.

  Sukkeret løfter den frugtige note. Spring det over hvis du vil have den mere rå.
tip: Dryp over bibimbap, soft scramble eller ristede broccoli.
=====
title: Harissaolie
slug: harissaolie
category: dips
description: Harissaolie — nordafrikansk chiliolie med spidskommen og koriander til kylling, æg og couscous.
prepTime: PT5M
cookTime: PT10M
totalTime: PT15M
servings: 12
difficulty: nem
tags:
  - harissaolie
  - harissa
  - chiliolie
  - olie
  - nordafrikansk
  - smagsolie
imageAlt: Dybrød harissaolie i glas med krydderier
featured: false
ingredients:
  - 2 dl neutral olie eller mild olivenolie
  - 2 spsk harissapaste
  - 1 tsk stødt spidskommen
  - ½ tsk stødt koriander
  - ½ tsk salt
  - Evt. 1 knust fed hvidløg
steps:
  - Rør harissa, krydderier, salt og evt. hvidløg sammen i en skål.
  - Varm olien til ca. 100–110 °C. Hæld over under omrøring, til pasten løser sig.
  - Lad trække 20 minutter. Si hvis du vil have klar olie, eller lad pasten blive i.
faq:
  - question: Hvilken harissa?
    answer: En paste du kan lide at spise med ske. Mild eller stærk — justér mængden.
  - question: Bliver den bitter?
    answer: Hvis olien er for varm. Hold under røgepunktet, især med olivenolie.
  - question: Holdbarhed?
    answer: 1–2 uger i køleskab. Rør før brug.
body: |
  Harissaolie er paste møder varme — spidskommen og koriander giver den nordafrikanske profil.

  Si eller lad være. Klar olie er elegant til bordet; med paste er den mere intens.
tip: Pensl kyllingelår før grill, eller dryp over hummus og blødkogt æg.
=====
title: Røgfyldt paprikaolie
slug: roegfyldt-paprikaolie
category: dips
description: Røgfyldt paprikaolie — dyb rød olie med røget paprika til æg, kartofler og grill.
prepTime: PT5M
cookTime: PT8M
totalTime: PT13M
servings: 12
difficulty: nem
tags:
  - roegfyldt-paprikaolie
  - paprika
  - røget
  - olie
  - smagsolie
  - grill
imageAlt: Dybrød røget paprikaolie i flaske
featured: false
ingredients:
  - 2 dl neutral olie
  - 2 spsk røget paprika (pimentón)
  - ½ tsk salt
  - Evt. ½ tsk chiliflager
steps:
  - Kom paprika, salt og evt. chili i en varmeresistent skål.
  - Varm olien til ca. 100 °C — paprika brænder let. Hæld over under omrøring.
  - Lad trække 15 minutter. Si gennem fin si eller kaffefilter for klar olie.
faq:
  - question: Sød eller stærk paprika?
    answer: Røget sød er klassisk. Røget stærk giver mere bid. Bland gerne.
  - question: Olien bliver bitter?
    answer: Paprika må ikke steges hårdt. For lav varme er bedre end for høj.
  - question: Holdbarhed?
    answer: 3–4 uger køligt i mørke.
body: |
  Røgfyldt paprikaolie giver grillsmag uden grill — paprikaen skal vækkes, ikke brændes.

  Si olien. Pulverrester synker og bliver mudrede i flasken.
tip: Dryp over pommes, scrambled eggs eller grillede peberfrugter.
=====
title: Chipotleolie
slug: chipotleolie
category: dips
description: Chipotleolie — røget jalapeño-olie til tacos, mayo og grillede grøntsager.
prepTime: PT5M
cookTime: PT10M
totalTime: PT15M
servings: 10
difficulty: nem
tags:
  - chipotleolie
  - chipotle
  - chiliolie
  - olie
  - mexicansk
  - smagsolie
imageAlt: Mørkerød chipotleolie med tørrede chilier
featured: false
ingredients:
  - 2 dl neutral olie
  - 3–4 tørrede chipotle-chilier (eller 2 spsk chipotle i adobo, afdryppet)
  - 1 tsk salt
  - Evt. 1 knust fed hvidløg
steps:
  - Knus eller hak chilierne groft. Kom dem i en skål med salt og evt. hvidløg.
  - Varm olien til ca. 120 °C. Hæld over. Lad trække 20–30 minutter.
  - Si. Smag — den skal være røget og varm, ikke askeagtig.
faq:
  - question: Friske jalapeños i stedet?
    answer: De giver frisk chili, ikke røg. Brug tørrede chipotle eller adobo.
  - question: For stærk?
    answer: Fortynd med mere olie, eller start med 2 chilier.
  - question: Holdbarhed?
    answer: Siftet uden frisk hvidløg 2–3 uger i køleskab.
body: |
  Chipotleolie er røg på flaske — tørrede jalapeños i olie, ikke frisk grøn chili.

  Adobo-varianten er mere saftig. Tørrede chilier giver renere olie.
tip: Rør en teskefuld i mayo til burger, eller dryp over street corn.
=====
title: Rosmarinolie
slug: rosmarinolie
category: dips
description: Rosmarinolie — aromatisk urteolie til brød, kartofler, lam og grill.
prepTime: PT5M
cookTime: PT10M
totalTime: PT15M
servings: 12
difficulty: nem
tags:
  - rosmarinolie
  - rosmarin
  - urtesolie
  - olie
  - smagsolie
  - grill
imageAlt: Grønlig rosmarinolie med friske kviste
featured: false
ingredients:
  - 2 dl mild olivenolie eller neutral olie
  - 3–4 kviste frisk rosmarin
  - 1 tsk salt
  - Evt. 1 fed hvidløg, knust
steps:
  - Skyl rosmarin, tør den godt. Pluk bladene af stilken.
  - Varm olien til ca. 90–100 °C. Tag af. Kom rosmarin, salt og evt. hvidløg i.
  - Lad trække 30–60 minutter. Si. Hæld på flaske.
faq:
  - question: Tørret rosmarin?
    answer: Ja — brug 2 tsk. Frisk er mere floral. Tørret er mere harpiksagtig.
  - question: Holdbarhed?
    answer: Siftet 2–3 uger køligt. Friske blade må ikke ligge i olien for længe.
  - question: Til hvad?
    answer: Focaccia, bagte kartofler, lam, grillkylling og hvid bønnesalat.
body: |
  Rosmarinolie er varme der vækker nålene — for høj temperatur gør den bitter og medicinsk.

  Tør urterne først. Vand i olien giver spil og dårlig holdbarhed.
tip: Pensl brød før ristning, eller dryp over ovnkartofler med flagesalt.
=====
title: Timianolie
slug: timianolie
category: dips
description: Timianolie — blid urteolie til kylling, svampe, æg og rodfrugter.
prepTime: PT5M
cookTime: PT10M
totalTime: PT15M
servings: 12
difficulty: nem
tags:
  - timianolie
  - timian
  - urtesolie
  - olie
  - smagsolie
  - kylling
imageAlt: Gylden timianolie med friske kvist
featured: false
ingredients:
  - 2 dl mild olivenolie
  - 6–8 kviste frisk timian
  - ½ tsk salt
  - Evt. 1 strimmel citronskal (uden hvid)
steps:
  - Tør timian grundigt. Varm olien til ca. 90 °C. Tag af.
  - Kom timian, salt og evt. citronskal i. Træk 30–45 minutter.
  - Si. Flask. Køl.
faq:
  - question: Citron-timian?
    answer: Ja — citronskal giver friskhed. Tag skallen ud efter 30 minutter, ellers bliver den bitter.
  - question: Holdbarhed?
    answer: 2–3 uger i køleskab, siftet.
  - question: Til hvad?
    answer: Stegte svampe, kyllingebryst, blødkogte æg og rodfrugtmos.
body: |
  Timianolie er diskret — den skal støtte retten, ikke dominere som rosmarin.

  Lav varme. Timian brænder lettere end man tror.
tip: Dryp over svampetoast med ricotta, eller over grillede asparges.
=====
title: Basilikumolie
slug: basilikumolie
category: dips
description: Basilikumolie — grøn, frisk olie til tomat, mozzarella, pasta og carpaccio.
prepTime: PT10M
cookTime: PT5M
totalTime: PT15M
servings: 10
difficulty: nem
tags:
  - basilikumolie
  - basilikum
  - urtesolie
  - olie
  - smagsolie
  - pasta
imageAlt: Klar grøn basilikumolie i glas
featured: true
ingredients:
  - 2 dl mild olivenolie
  - 2 store håndfulde frisk basilikum
  - ½ tsk salt
  - Evt. 1 knivspids sukker
steps:
  - Blanchér basilikum 5–10 sekunder i kogende vand. Kom i isvand. Dup knastør.
  - Blend basilikum med olie og salt til en glat, grøn olie. Si gennem fin si eller klud.
  - Smag til. Opbevar køligt i tæt flaske.
faq:
  - question: Hvorfor blanchere?
    answer: Farven holder grøn. Uden blanchering bliver olien hurtigt mat og brunlig.
  - question: Holdbarhed?
    answer: 5–7 dage i køleskab. Frys i isterningebakker til længere hold.
  - question: Kan jeg bruge pesto-teknik?
    answer: Ja, men uden ost og pinjekerner — det er olie, ikke pesto.
body: |
  Basilikumolie er farve og aroma — blanchering låser det grønne, si gør den elegant.

  Den er kortlivet. Lav små portioner og brug dem.
tip: Dryp over caprese, tomatpasta eller rå oksecapaccio.
=====
title: Oreganoolie
slug: oreganoolie
category: dips
description: Oreganoolie — kraftig middelhavsolie til pizza, tomat, feta og grillgrønt.
prepTime: PT5M
cookTime: PT10M
totalTime: PT15M
servings: 12
difficulty: nem
tags:
  - oreganoolie
  - oregano
  - urtesolie
  - olie
  - smagsolie
  - pizza
imageAlt: Grønlig oreganoolie med tørrede blade
featured: false
ingredients:
  - 2 dl mild olivenolie
  - 2 spsk tørret oregano (eller 1 stor håndfuld frisk)
  - ½ tsk salt
  - Evt. ½ tsk chiliflager
steps:
  - Varm olien til ca. 90–100 °C. Tag af. Rør oregano, salt og evt. chili i.
  - Træk 30–45 minutter. Si. Flask.
faq:
  - question: Tørret eller frisk?
    answer: Tørret oregano er mere koncentreret og klassisk til pizza. Frisk er grønnere.
  - question: Holdbarhed?
    answer: 2–3 uger køligt, siftet.
  - question: Til hvad?
    answer: Pizza efter bagning, græsk salat, feta, grillede peberfrugter.
body: |
  Oreganoolie er pizzaens bedste ven — tørret oregano i mild varme giver den rigtige middelhavsduft.

  Dryp efter bagning. Varme i ovnen slår aromaen ihjel.
tip: En skefuld over varm pizza lige ud af ovnen slår de fleste toppings.
=====
title: Dildolie
slug: dildolie
category: dips
description: Dildolie — nordisk grøn olie til laks, kartofler, æg og smørrebrød.
prepTime: PT10M
cookTime: PT5M
totalTime: PT15M
servings: 10
difficulty: nem
tags:
  - dildolie
  - dild
  - urtesolie
  - olie
  - smagsolie
  - laks
imageAlt: Grøn dildolie i skål ved siden af frisk dild
featured: false
ingredients:
  - 2 dl neutral olie eller mild olivenolie
  - 2 store håndfulde frisk dild
  - ½ tsk salt
  - Evt. 1 tsk citronsaft
steps:
  - Blanchér dild 5 sekunder. Isvand. Dup tør.
  - Blend med olie og salt. Si. Smag med citron hvis du vil.
  - Flask. Køl.
faq:
  - question: Stilkene med?
    answer: De nederste tykke stilke smager skarpt. Brug blade og tynde stilke.
  - question: Holdbarhed?
    answer: 5–7 dage i køleskab. Frys i portioner.
  - question: Til hvad?
    answer: Røget laks, nye kartofler, blødkogte æg, gravad laks og kold kartoffelsalat.
body: |
  Dildolie er nordisk grøn — blanchering holder farven, si giver en blank dressing-olie.

  Citron er valgfri. Den gør olien mere vinaigrette-agtig.
tip: Dryp over røget laks på rugbrød i stedet for remoulade, når du vil have det lettere.
=====
title: Estragonolie
slug: estragonolie
category: dips
description: Estragonolie — anislignende urteolie til kylling, fisk, æg og bearnaise-agtige retter.
prepTime: PT5M
cookTime: PT10M
totalTime: PT15M
servings: 10
difficulty: nem
tags:
  - estragonolie
  - estragon
  - urtesolie
  - olie
  - smagsolie
  - kylling
imageAlt: Lys grøn estragonolie med friske blade
featured: false
ingredients:
  - 2 dl mild olivenolie
  - 1 stor håndfuld frisk estragon
  - ½ tsk salt
  - Evt. 1 spsk hvidvinseddike (til servering)
steps:
  - Tør estragon. Varm olien til ca. 80–90 °C. Tag af.
  - Kom estragon og salt i. Træk 20–40 minutter. Si.
  - Flask. Brug gerne samme dag eller inden for en uge.
faq:
  - question: Tørret estragon?
    answer: Det mister meget aroma. Frisk er næsten et krav her.
  - question: Holdbarhed?
    answer: Max 1 uge i køleskab. Aromaen falder hurtigt.
  - question: Til hvad?
    answer: Kyllingebryst, pocheret æg, hvid fisk, asparges og som finish på bearnaise.
body: |
  Estragonolie er fin og flygtig — lav varme, kort trækketid, brug den frisk.

  Den erstatter ikke bearnaise, men den giver den samme anis-note uden æg.
tip: Dryp over grillede asparges med flagesalt og citron.
=====
title: Persilleolie
slug: persilleolie
category: dips
description: Persilleolie — grøn blendet urteolie til fisk, kartofler, supper og grill.
prepTime: PT10M
cookTime: PT5M
totalTime: PT15M
servings: 10
difficulty: nem
tags:
  - persilleolie
  - persille
  - urtesolie
  - olie
  - smagsolie
  - fisk
imageAlt: Klar grøn persilleolie i flaske
featured: false
ingredients:
  - 2 dl neutral olie
  - 2 store bundter bredbladet persille
  - ½ tsk salt
  - Evt. 1 fed hvidløg
steps:
  - Blanchér persille 10 sekunder. Isvand. Dup knastør.
  - Blend med olie, salt og evt. hvidløg. Si gennem fin si.
  - Flask. Køl. Ryst før brug.
faq:
  - question: Kruset eller bredbladet?
    answer: Bredbladet er milde og grønne. Kruset kan smage skarpere.
  - question: Holdbarhed?
    answer: 5–7 dage i køleskab. Frys i portioner.
  - question: Til hvad?
    answer: Finish på supper, fisk, kartoffelmos, grillgrønt og carpaccio.
body: |
  Persilleolie er den grønne finish — blanchér, blend, si. Den løfter retter uden at være tung.

  Neutral olie holder farven renere end kraftig olivenolie.
tip: En ring af persilleolie rundt om en skål tomatsuppe ser ud og smager som restaurant.
=====
title: Koriander-limetteolie
slug: koriander-limetteolie
category: dips
description: Koriander-limetteolie — frisk, syrlig urteolie til tacos, fisk, rejer og salat.
prepTime: PT10M
cookTime: PT5M
totalTime: PT15M
servings: 10
difficulty: nem
tags:
  - koriander-limetteolie
  - koriander
  - limette
  - urtesolie
  - olie
  - smagsolie
imageAlt: Grøn korianderolie med limetteskal
featured: false
ingredients:
  - 2 dl neutral olie
  - 1 stor bundt koriander
  - Skal af 1 limette (uden hvid)
  - ½ tsk salt
  - Evt. 1 tsk limettesaft til servering
steps:
  - Blanchér koriander 5 sekunder. Isvand. Dup tør.
  - Blend med olie, limetteskal og salt. Si.
  - Smag. Tilsæt limettesaft først ved servering, hvis du vil have mere syre.
faq:
  - question: Kan jeg bruge citron?
    answer: Ja. Limette er skarpere; citron er rundere.
  - question: Holdbarhed?
    answer: 4–6 dage i køleskab. Saften forkorter holdbarheden — tilsæt den sent.
  - question: Til hvad?
    answer: Tacos, ceviche, grillede rejer, avocado-toast og fisketacos.
body: |
  Koriander-limetteolie er friskhed på flaske — skal i olien, saft ved bordet.

  Blanchering dæmper den rå koriander-note uden at fjerne den.
tip: Dryp over street tacos med stegt kål og creme fraiche.
=====
title: Hvidløgsolie
slug: hvidloegsolie
category: dips
description: Hvidløgsolie — blidt varmetilført olie til brød, pasta, pizza og grill.
prepTime: PT5M
cookTime: PT20M
totalTime: PT25M
servings: 12
difficulty: nem
tags:
  - hvidloegsolie
  - hvidloeg
  - olie
  - smagsolie
  - pasta
  - pizza
imageAlt: Gylden hvidløgsolie med hele fed i glas
featured: true
ingredients:
  - 2 dl neutral olie eller mild olivenolie
  - 8–10 fed hvidløg, skrællet
  - ½ tsk salt
  - Evt. 1 kvist timian
steps:
  - Læg hvidløg i kold olie i en lille gryde. Varm langsomt til ca. 90–95 °C.
  - Hold temperaturen lav 15–20 minutter, til feddene er bløde og lysgyldne — ikke brune.
  - Tag af. Salt. Si eller lad feddene blive i. Køl straks. Opbevar i køleskab.
faq:
  - question: Botulisme?
    answer: Frisk hvidløg i olie skal altid på køl og bruges inden 1 uge. Frys resten. Opbevar aldrig ved stuetemperatur.
  - question: Kan feddene spises?
    answer: Ja — de er milde og smørbare. Smør dem på brød.
  - question: Til hvad?
    answer: Pasta, pizza, focaccia, grillgrønt og som base til vinaigrette.
body: |
  Hvidløgsolie er lav og langsom — feddene confiteres blidt, så smagen bliver sød, ikke skarp.

  Køl med det samme. Sikkerhed først, smag bagefter.
tip: Brug olien til at stege rejer, og mos de bløde fed ovenpå til sidst.
=====
title: Sort hvidløgsolie
slug: sort-hvidloegsolie
category: dips
description: Sort hvidløgsolie — sød, balsamicoagtig umami-olie til steak, æg og ost.
prepTime: PT5M
cookTime: PT10M
totalTime: PT15M
servings: 10
difficulty: nem
tags:
  - sort-hvidloegsolie
  - sort-hvidloeg
  - hvidloeg
  - olie
  - smagsolie
  - umami
imageAlt: Mørk sort hvidløgsolie i skål
featured: false
ingredients:
  - 2 dl mild olivenolie
  - 6–8 fed sort hvidløg
  - ½ tsk salt
  - Evt. 1 tsk sojasauce
steps:
  - Mos sort hvidløg til en pasta. Rør med lidt olie, til det er glat.
  - Varm resten af olien til ca. 80 °C. Rør pastæn i. Salt. Evt. sojasauce.
  - Lad trække 20 minutter. Si eller blend glat. Køl.
faq:
  - question: Hvad er sort hvidløg?
    answer: Fermenteret/aged hvidløg — sødt, blødt, uden skarphed. Købes færdigt.
  - question: Holdbarhed?
    answer: 1–2 uger i køleskab. Rør før brug.
  - question: Til hvad?
    answer: Steak finish, blødkogte æg, gedeost, svampe og majs.
body: |
  Sort hvidløgsolie er umami uden brænd — pastæn opløses i mild varme og giver dyb, sød aroma.

  Den er dyr i indkøb. Lav små portioner og brug dem som finish.
tip: En teskefuld over culotte lige før servering slår de fleste steaksaucer.
=====
title: Citronolie
slug: citronolie
category: dips
description: Citronolie — lys citrusolie til fisk, salat, kylling og sommerbordet.
prepTime: PT10M
cookTime: PT5M
totalTime: PT15M
servings: 12
difficulty: nem
tags:
  - citronolie
  - citron
  - olie
  - smagsolie
  - fisk
  - salat
imageAlt: Lys gul citronolie med citronskal
featured: false
ingredients:
  - 2 dl mild olivenolie
  - Skal af 2 citroner (kun det gule)
  - ½ tsk salt
  - Evt. 1 kvist timian
steps:
  - Skræl citronerne tyndt uden hvid pith. Kom skal i en skål med salt.
  - Varm olien til ca. 80–90 °C. Hæld over skallen. Evt. timian.
  - Træk 30–60 minutter. Si. Flask. Køl.
faq:
  - question: Hvorfor uden hvid?
    answer: Den hvide pith er bitter. Kun det gule skal i olien.
  - question: Holdbarhed?
    answer: 1–2 uger i køleskab. Aromaen er bedst den første uge.
  - question: Til hvad?
    answer: Fisk, kylling, grøn salat, asparges, ricotta-toast.
body: |
  Citronolie er skal, ikke saft — olien tager de æteriske olier uden at blive sur.

  Lav varme. For varmt brænder skallen og smager af møbelpolish.
tip: Dryp over grillede zucchiniskiver med flagesalt og parmesan.
=====
title: Appelsinolie
slug: appelsinolie
category: dips
description: Appelsinolie — sødlig citrusolie til vildt, and, salat og efterårsgrønt.
prepTime: PT10M
cookTime: PT5M
totalTime: PT15M
servings: 12
difficulty: nem
tags:
  - appelsinolie
  - appelsin
  - olie
  - smagsolie
  - vildt
  - salat
imageAlt: Gylden appelsinolie med appelsinskal
featured: false
ingredients:
  - 2 dl mild olivenolie
  - Skal af 2 appelsiner (kun det orange)
  - ½ tsk salt
  - Evt. 1 knivspids stødt nellike eller kanel
steps:
  - Skræl appelsinerne tyndt uden hvid. Kom skal og salt i en skål.
  - Varm olien til ca. 80–90 °C. Hæld over. Evt. en knivspids krydderi.
  - Træk 45–60 minutter. Si. Flask. Køl.
faq:
  - question: Blodappelsin?
    answer: Ja — skallen giver stadig aroma. Frugtkødet er til saften, ikke olien.
  - question: Holdbarhed?
    answer: 1–2 uger i køleskab.
  - question: Til hvad?
    answer: Andebryst, vildt, rødbedesalat, fennikel, gulerødder og chokolade-dessert finish.
body: |
  Appelsinolie er efterår på flaske — skal i mild olie, gerne med en anelse varmt krydderi.

  Nellike er valgfri og stærk. Start med en knivspids.
tip: Dryp over rødbedesalat med gedeost og valnødder.
=====
title: Ingefærolie
slug: ingefaerolie
category: dips
description: Ingefærolie — skarp, varm olie til asiatiske retter, rejer, ris og wok.
prepTime: PT10M
cookTime: PT10M
totalTime: PT20M
servings: 12
difficulty: nem
tags:
  - ingefaerolie
  - ingefær
  - olie
  - smagsolie
  - asiatisk
  - wok
imageAlt: Gylden ingefærolie med friske skiver
featured: false
ingredients:
  - 2 dl neutral olie
  - 80 g frisk ingefær, tyndt skåret
  - ½ tsk salt
  - Evt. 1 spsk chiliflager
steps:
  - Steg ingefær i olien på middel lav varme 8–10 minutter, til skiverne er lysgyldne og knasende.
  - Tag af. Salt. Evt. chili. Lad køle 10 minutter.
  - Si. Gem gerne de knasende skiver som topping. Flask olien. Køl.
faq:
  - question: Er det det samme som forårsløgsolie?
    answer: Nej — denne er ren ingefær. Forårsløgsolien har løg og ofte hvidløg oveni.
  - question: Holdbarhed?
    answer: 1–2 uger i køleskab. Skiverne er bedst de første dage.
  - question: Til hvad?
    answer: Wok, dampede fisk, ris, nudler, stegte rejer og dumpling-dyp.
body: |
  Ingefærolie er skarp varme uden løg — skiverne steges til knas, olien tager aromaen.

  For høj varme brænder ingefæren bitter. Hold den gylden, ikke brun.
tip: Dryp over dampet fisk med sojasauce og forårsløg.
=====
title: Peberrodsolie
slug: peberrodsolie
category: dips
description: Peberrodsolie — skarp nordisk olie til laks, roastbeef, kartofler og smørrebrød.
prepTime: PT10M
cookTime: PT5M
totalTime: PT15M
servings: 10
difficulty: nem
tags:
  - peberrodsolie
  - peberrod
  - olie
  - smagsolie
  - laks
  - frokost
imageAlt: Lys peberrodsolie i skål med revet peberrod
featured: false
ingredients:
  - 2 dl neutral olie
  - 40 g frisk peberrod, fintrevet
  - ½ tsk salt
  - Evt. 1 tsk citronsaft
steps:
  - Riv peberrod. Kom det i en skål med salt.
  - Varm olien til ca. 80 °C. Hæld over. Rør. Træk 20–30 minutter.
  - Si hårdt. Smag. Evt. citron ved servering. Køl.
faq:
  - question: Fra glas?
    answer: Ja i nød — men frisk er skarpere og renere. Glas-peberrod er ofte med eddike.
  - question: Holdbarhed?
    answer: 5–7 dage i køleskab. Styrken falder hurtigt.
  - question: Til hvad?
    answer: Røget laks, roastbeef, kogte kartofler, æg og smørrebrød.
body: |
  Peberrodsolie er snudeklar skarphed — varmen vækker roden, si fjerner fibrene.

  Lav den samme dag du skal bruge den. Den mister bite hurtigt.
tip: Dryp over røget laks i stedet for peberrodssauce, når du vil have det lettere.
=====
title: Soltørret tomatolie
slug: soltoerret-tomatolie
category: dips
description: Soltørret tomatolie — sød umami-olie til pasta, brød, mozzarella og grill.
prepTime: PT5M
cookTime: PT10M
totalTime: PT15M
servings: 12
difficulty: nem
tags:
  - soltoerret-tomatolie
  - soltørret-tomat
  - olie
  - smagsolie
  - pasta
  - umami
imageAlt: Rød soltørret tomatolie med tomater i glas
featured: false
ingredients:
  - 2 dl mild olivenolie (gerne olien fra glasset + ekstra)
  - 100 g soltørrede tomater i olie, hakket
  - 1 tsk oregano eller basilikum
  - ½ tsk salt
  - Evt. 1 fed hvidløg
steps:
  - Hak tomaterne. Kom dem i en skål med urter, salt og evt. hvidløg.
  - Varm olien til ca. 90 °C. Hæld over. Træk 30 minutter.
  - Blend kort for mere intensitet, eller lad stykkerne være. Køl.
faq:
  - question: Tørrede uden olie?
    answer: Blød dem 10 minutter i varmt vand, dup tør, og brug frisk olie.
  - question: Holdbarhed?
    answer: 1–2 uger i køleskab. Med frisk hvidløg max 1 uge.
  - question: Til hvad?
    answer: Pasta, bruschetta, mozzarella, omelet, grillkylling.
body: |
  Soltørret tomatolie er sød umami — brug gerne olien fra glasset, den er allerede smagt til.

  Blend hvis du vil have den mere sauce-agtig. Lad stykkerne være til topping.
tip: Dryp over burrata med flagesalt og basilikum.
=====
title: Svampeolie
slug: svampeolie
category: dips
description: Svampeolie — dyb umami-olie af tørrede svampe til risotto, æg, steak og pasta.
prepTime: PT5M
cookTime: PT15M
totalTime: PT20M
servings: 12
difficulty: nem
tags:
  - svampeolie
  - svampe
  - olie
  - smagsolie
  - umami
  - pasta
imageAlt: Mørk svampeolie med tørrede svampe
featured: false
ingredients:
  - 2 dl neutral olie
  - 20 g tørrede porcini eller blandede skovsvampe
  - ½ tsk salt
  - Evt. 1 fed hvidløg
steps:
  - Knus de tørrede svampe groft. Kom dem i en lille gryde med olie og evt. hvidløg.
  - Varm langsomt til ca. 90–95 °C. Hold 12–15 minutter uden at det braser hårdt.
  - Si. Salt. Flask. Køl. Gem svampepulveret til risotto eller omelet.
faq:
  - question: Friske svampe?
    answer: De indeholder vand og giver svagere olie. Tørrede er koncentreret umami.
  - question: Holdbarhed?
    answer: 2–3 uger i køleskab, siftet.
  - question: Til hvad?
    answer: Risotto-finish, scrambled eggs, steak, pasta, kartoffelmos.
body: |
  Svampeolie er skov på flaske — tørrede porcini i mild varme giver dyb umami uden fløde.

  Si godt. Små partikler synker og bliver mudrede.
tip: En skefuld over blødkogte æg med flagesalt er instant brunch.
=====
title: Ansjosolie
slug: ansjosolie
category: dips
description: Ansjosolie — salt umami-olie til pasta, grønt, caesar-agtige dressinger og grill.
prepTime: PT5M
cookTime: PT10M
totalTime: PT15M
servings: 10
difficulty: nem
tags:
  - ansjosolie
  - ansjos
  - olie
  - smagsolie
  - umami
  - pasta
imageAlt: Gylden ansjosolie i skål med ansjosfileter
featured: false
ingredients:
  - 1½ dl mild olivenolie
  - 6–8 ansjosfileter i olie
  - 1 fed hvidløg, knust
  - Evt. ½ tsk chiliflager
  - Friskkværnet peber
steps:
  - Hak ansjoserne. Svits dem med hvidløg i olien på lav varme 5–8 minutter, til de nærmest smelter.
  - Tag af. Chiliflager og peber. Lad køle lidt.
  - Blend glat eller brug som den er. Køl.
faq:
  - question: Smager det fisket?
    answer: Det skal smage umami og salt — ikke fiskebutik. Start med færre fileter hvis du er nervøs.
  - question: Holdbarhed?
    answer: 5–7 dage i køleskab. Brug det som finish, ikke som lagerolie.
  - question: Til hvad?
    answer: Pasta cacio e pepe-finish, grillede broccoli, caesar-salat, brød.
body: |
  Ansjosolie er salt umami — fileterne smelter i mild olie og forsvinder som smag, ikke som stykker.

  Salt først til sidst. Ansjoserne er allerede salte.
tip: Vend grillede broccoli i en skefuld ansjosolie og citron — klassisk romana-stil.
=====
title: Baconolie
slug: baconolie
category: dips
description: Baconolie — knasende baconfedt blandet med olie til æg, kartofler, salat og grillgrønt.
prepTime: PT5M
cookTime: PT15M
totalTime: PT20M
servings: 12
difficulty: nem
tags:
  - baconolie
  - bacon
  - olie
  - smagsolie
  - æg
  - kartofler
imageAlt: Gylden baconolie med crispy baconbits
featured: true
ingredients:
  - 150 g bacon i tern
  - 1 dl neutral olie
  - Friskkværnet peber
  - Evt. ½ tsk røget paprika
steps:
  - Steg bacon på middel varme, til det er knasende og fedtet er smeltet. Tag bacon op.
  - Hæld baconfedt gennem si. Bland med neutral olie, peber og evt. paprika.
  - Kom baconbits tilbage hvis du vil have knas, eller gem dem separat. Køl.
faq:
  - question: Størkner den?
    answer: Ja i køleskab. Tag den ud 10 minutter før brug, eller varm forsigtigt.
  - question: Holdbarhed?
    answer: 1 uge i køleskab. Bacon er kød — hold det koldt og brug det op.
  - question: Til hvad?
    answer: Æg, ovnkartofler, spinatsalat, grillede asparges, majs.
body: |
  Baconolie er fedt plus aroma — bacon steges knasende, fedtet blandes med olie så det bliver hældbart.

  Peber og paprika løfter uden at skjule baconen.
tip: Dryp over blødkogte æg med crispy bits ovenpå — breakfast på to minutter.
=====
title: Chorizoolie
slug: chorizoolie
category: dips
description: Chorizoolie — krydret pølseolie til æg, kartofler, rejer, pizza og tapas.
prepTime: PT5M
cookTime: PT12M
totalTime: PT17M
servings: 10
difficulty: nem
tags:
  - chorizoolie
  - chorizo
  - olie
  - smagsolie
  - paprika
  - æg
imageAlt: Rød chorizoolie med pølsestykker
featured: false
ingredients:
  - 150 g chorizo, skåret i små tern
  - 1 dl mild olivenolie
  - Evt. ½ tsk røget paprika
  - Friskkværnet peber
steps:
  - Steg chorizo på middel varme, til fedtet løber og kanterne er knasende.
  - Tag pølsen op. Bland det røde fedt med olivenolie og evt. ekstra paprika.
  - Si hvis du vil have klar olie, eller lad små stykker blive i. Køl.
faq:
  - question: Hvilken chorizo?
    answer: Spansk, kraftigt krydret. Mild dansk «chorizo» giver mindre farve og smag.
  - question: Holdbarhed?
    answer: 5–7 dage i køleskab.
  - question: Til hvad?
    answer: Æg, patatas bravas, rejer, pizza, nachos, grillede peberfrugter.
body: |
  Chorizoolie er paprika og fedt — pølsen steges, det røde spejl blandes med olie.

  Den er stærk. En skefuld er finish, ikke stegefedt til hele retten.
tip: Steg rejer i en skefuld chorizoolie med hvidløg — tapas på fem minutter.
=====
title: Sesam-chiliolie
slug: sesam-chiliolie
category: dips
description: Sesam-chiliolie — ristet sesam møder chili til nudler, dumplings, ris og wok.
prepTime: PT5M
cookTime: PT10M
totalTime: PT15M
servings: 12
difficulty: nem
tags:
  - sesam-chiliolie
  - sesam
  - chiliolie
  - olie
  - smagsolie
  - asiatisk
imageAlt: Mørk sesam-chiliolie med sesamfrø
featured: false
ingredients:
  - 1½ dl neutral olie
  - ½ dl ristet sesamolie
  - 3 spsk chiliflager
  - 2 spsk sesamfrø
  - 1 tsk salt
  - Evt. 1 fed hvidløg, finthakket
steps:
  - Rist sesamfrø tørt på panden, til de dufter. Kom dem i en skål med chili, salt og evt. hvidløg.
  - Varm den neutrale olie til ca. 120 °C. Hæld over. Rør den ristede sesamolie i til sidst.
  - Lad køle. Flask. Køl.
faq:
  - question: Kun sesamolie?
    answer: Nej — ren sesamolie er for kraftig og ryger let. Bland med neutral olie.
  - question: Holdbarhed?
    answer: 1–2 uger i køleskab. Med frisk hvidløg max 1 uge.
  - question: Til hvad?
    answer: Nudler, dumplings, ris, wokgrønt, tofu og æg.
body: |
  Sesam-chiliolie er nøddeagtig varme — flagerne vækkes i neutral olie, sesamolien tilsættes til sidst.

  Tilsæt sesamolien af varmen. Den må ikke koge.
tip: Dryp over kold nudelsalat med agurk og forårsløg.
=====
title: Fennikelolie
slug: fennikelolie
category: dips
description: Fennikelolie — anislignende olie til fisk, pølse, tomat og efterårssalat.
prepTime: PT5M
cookTime: PT10M
totalTime: PT15M
servings: 10
difficulty: nem
tags:
  - fennikelolie
  - fennikel
  - urtesolie
  - olie
  - smagsolie
  - fisk
imageAlt: Lys fennikelolie med frø og fennikeltop
featured: false
ingredients:
  - 2 dl mild olivenolie
  - 2 tsk fennikelfrø
  - 1 håndfuld fennikeltop (hvis du har)
  - ½ tsk salt
steps:
  - Rist fennikelfrø tørt 1 minut, til de dufter. Knus let.
  - Varm olien til ca. 90 °C. Tag af. Kom frø, salt og evt. fennikeltop i.
  - Træk 30–45 minutter. Si. Flask. Køl.
faq:
  - question: Kun frø?
    answer: Frø giver den klassiske anis-note. Toppen giver grøn friskhed. Gerne begge.
  - question: Holdbarhed?
    answer: 2 uger i køleskab, siftet.
  - question: Til hvad?
    answer: Grillet fisk, italiensk pølse, tomatsalat, appelsin-fennikelsalat.
body: |
  Fennikelolie er blød anis — ristede frø i mild olie, gerne med grøn top.

  Den passer til både fisk og svin. En skefuld over grillede pølser er undervurderet.
tip: Dryp over blodappelsin- og fennikelsalat med oliven.
=====
title: Lautrec-hvidløgsolie
slug: lautrec-hvidloeg-olie
category: dips
description: Lautrec-hvidløgsolie — mild, sød konfiteret hvidløgsolie til brød, ost og fine retter.
prepTime: PT10M
cookTime: PT40M
totalTime: PT50M
servings: 12
difficulty: mellem
tags:
  - lautrec-hvidloeg-olie
  - hvidloeg
  - olie
  - smagsolie
  - confit
  - festmad
imageAlt: Gyldne konfiterede hvidløgsfed i olie
featured: false
ingredients:
  - 2 dl mild olivenolie
  - 2 hele hvidløgshoveder, fed skrællet (gerne pink Lautrec-type hvis du finder dem)
  - 2 kviste timian
  - 1 laurbærblad
  - ½ tsk salt
steps:
  - Læg fed, timian og laurbær i en lille ovnfast skål. Dæk med olie. Salt.
  - Bag ved 120 °C i 35–40 minutter, til feddene er bløde og lysgyldne.
  - Lad køle i olien. Tag urter fra. Opbevar fed og olie i køleskab — brug inden 1 uge.
faq:
  - question: Er det det samme som hvidløgsconfit fra Sylte?
    answer: Samme teknik, anden brug — her er olien hovedrollen til dryp og finish, feddene er bonus.
  - question: Botulisme?
    answer: Altid køl. Max 1 uge. Frys portioner. Aldrig stuetemperatur.
  - question: Til hvad?
    answer: Brød, ostebræt, fin pasta, kylling, grillede grøntsager.
body: |
  Lautrec-hvidløgsolie er den milde konfitering — lav ovnvarme, hele fed, olie der bliver sød.

  Den er festmad-finish. En skefuld olie og to bløde fed på brød er nok.
tip: Mos et fed på toast med flagesalt, og dryp olien over — enkleste forret.
=====
'''


def parse_block(text: str) -> dict:
    lines = text.strip().splitlines()
    data: dict = {
        "tags": [],
        "ingredients": [],
        "steps": [],
        "faq": [],
        "featured": "false",
    }
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
        elif line.startswith("body: |"):
            mode = "body"
            body_lines = []
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
    assert "olie" in d["tags"] or "chiliolie" in d["tags"] or "urtesolie" in d["tags"] or "smagsolie" in d["tags"], d.get("slug")
    out = ROOT / d["category"]
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{d['slug']}.mdx"
    if path.exists():
        raise SystemExit(f"slug collision: {path}")
    path.write_text(to_mdx(d), encoding="utf-8")
    print("wrote", d["category"] + "/" + path.name)
