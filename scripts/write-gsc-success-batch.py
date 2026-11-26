#!/usr/bin/env python3
"""GSC success batch — 12 teknik-kloner ud fra 7-dages Search Console (nov 2026)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"
PUBLISHED = "2026-11-26"

RECIPES = r'''
=====
title: Griseskank i trykkoger
slug: griseskank-trykkoger
category: trykkoger
description: Griseskank / svineskank i trykkoger — mør skank på ca. 1 time med kraftig sauce, klar til rodfrugter eller kartoffelmos.
prepTime: PT20M
cookTime: PT1H
totalTime: PT1H20M
servings: 4
difficulty: mellem
tags:
  - griseskank
  - svineskank
  - griseskank i trykkoger
  - svineskank i trykkoger
  - skank af gris
  - trykkoger
  - svinekød
  - vinter
imageAlt: Mør griseskank fra trykkogeren i kraftig sauce
featured: true
ingredients:
  - 2–3 griseskanke (ca. 1,2–1,5 kg i alt)
  - 2 tsk salt
  - Peber
  - 1 spsk olie
  - 1 stort løg, 1 gulerod, 1 stilk bladselleri — hakket
  - 2 fed hvidløg
  - 1 spsk tomatpuré
  - 2 dl æblemost eller mørkt øl
  - 3 dl honse- eller grisebouillon
  - 2 laurbærblade, 4 kviste timian
  - 1 spsk smør til at montere saucen (valgfrit)
steps:
  - Dup skankene tørre. Salt og peber. Brun hårdt i olie på sautér-funktionen. Tag op.
  - Svits løg, gulerod og selleri 5 minutter. Hvidløg og tomatpuré 1 minut. Hæld most/øl i, skrab bunden.
  - Bouillon, laurbær og timian i. Læg skankene tilbage — væsken skal næsten dække.
  - Højt tryk 45 minutter. Naturlig udligning 15 minutter.
  - Tag skankene forsigtigt op. Si og reducér saucen på sautér til den napper. Montér med smør. Læg skankene tilbage, eller træk kødet fra benet.
  - Server med kartoffelmos, rodfrugter eller bløde boller.
faq:
  - question: Er skanken færdig, når den er brun?
    answer: Nej. Den skal være mør — collagenet skal smelte. Test med gaffel; kødet skal næsten slippe benet.
  - question: Airfryer i stedet?
    answer: Ja — se [griseskank i airfryer](/opskrifter/airfryer/griseskank-airfryer). Trykkoger er hurtigere til mørt; airfryer giver mere skorpe.
  - question: Ovn-version?
    answer: Se [griseskank i ovn](/opskrifter/ovn/griseskank-ovn) til langtidsstegning uden tryk.
  - question: For fed sauce?
    answer: Køl 10 minutter, skim fedtet af, og varm op. Eller reducér længere — fedtet samler sig i overfladen.
body: |
  Griseskank i trykkoger er #1-airfryer-vinderen på turbo: samme collagen, halv tid.

  Brun. Tryk 45 minutter. Reducér sauce.

  Du jagter mørt kød, der slipper benet — ikke en kotelet-skorpe.
tip: Put ikke for lidt væske i. Under tryk fordamper der næsten intet, men skanken skal bade, ellers bliver kanten tør.
=====
title: Langtidsstegt griseskank i ovn
slug: griseskank-ovn
category: ovn
description: Langtidsstegt griseskank / svineskank i ovn — lav temperatur, mør skank og stegt overflade uden trykkoger.
prepTime: PT20M
cookTime: PT3H
totalTime: PT3H20M
servings: 4
difficulty: mellem
tags:
  - griseskank
  - svineskank
  - griseskank i ovn
  - langtidsstegt griseskank
  - skank af gris
  - ovn
  - svinekød
  - søndagsmad
imageAlt: Langtidsstegt griseskank fra ovnen med stegt skorpe
featured: true
ingredients:
  - 2–3 griseskanke (ca. 1,2–1,5 kg)
  - 2 tsk salt
  - 1 tsk peber
  - 1 tsk paprika
  - 1 tsk tørret timian
  - 1 spsk olie
  - 1 løg i både, 2 gulerødder i stykker
  - 2 dl æblejuice eller fond
  - 2 laurbærblade
steps:
  - Tag skankene ud 30 minutter før. Tænd ovnen på 150 °C. Dup tørre. Vend med olie, salt, peber, paprika og timian.
  - Læg løg og gulerod i et fad. Skanke ovenpå. Hæld æblejuice/fond i bunden — ikke over kødet. Laurbær i.
  - Steg 2½–3 timer, til kødet næsten slipper benet. Vend én gang halvvejs.
  - Sidste 15 minutter ved 210 °C for ekstra skorpe, hvis overfladen er bleg.
  - Hvile 10 minutter. Server med saften fra fadet, rodfrugterne og sennep.
faq:
  - question: Hvilken kernetemperatur?
    answer: Til skank er mørt vigtigere end grader. Collagen skal smelte — typisk når kødet slipper benet. Ca. 90–95 °C i den tykkeste del er normalt for braiseret skank.
  - question: Airfryer eller trykkoger?
    answer: [Airfryer](/opskrifter/airfryer/griseskank-airfryer) er hurtigere med mere skorpe. [Trykkoger](/opskrifter/trykkoger/griseskank-trykkoger) er hurtigst til mørt. Ovn er klassisk søndagssteg.
  - question: Svær på skanken?
    answer: Score sværen, hold den over væsken, og finish højt (220 °C) de sidste 20 minutter — samme trick som schweinshaxe.
  - question: Tilbehør?
    answer: Kartoffelmos, brunkål, syltede rødløg eller bløde boller.
body: |
  Langtidsstegt griseskank i ovn er vinter uden hastværk: lav varme, tid, så en kort finish.

  Fond i bunden. Ikke over kødet. Vend én gang.

  Det er ikke en culotte. Det er collagen-arbejde i et fad.
tip: Ens størrelse på skankene. Bed slagteren save dem, så de bliver færdige samtidig.
=====
title: Schweinshaxe i airfryer
slug: schweinshaxe-airfryer
category: airfryer
description: Schweinshaxe / svineskank i airfryer — mør skank med sprød svær uden Dutch Oven, klar på ca. 90 minutter.
prepTime: PT15M
cookTime: PT1H30M
totalTime: PT1H45M
servings: 2
difficulty: mellem
tags:
  - schweinshaxe
  - schweinshaxe airfryer
  - svineskank
  - griseskank
  - airfryer
  - sprød svær
  - tysk
  - vinter
imageAlt: Schweinshaxe fra airfryeren med sprød svær
featured: true
ingredients:
  - 2 svineskanke med svær (à 400–500 g)
  - 2 tsk groft salt
  - 1 tsk spidskommen
  - 1 tsk peber
  - 1 spsk olie
  - 1 dl æblemost eller fond i en lav form (valgfrit)
  - 1 tsk sennep til pensling (valgfrit)
steps:
  - Score sværen tæt uden at skære i kødet. Dup knastørt. Gnid salt, spidskommen, peber og olie ind — også i snittene.
  - Forvarm airfryeren til 160 °C. Læg skankene med svær opad. Evt. form med lidt væske under (må ikke dække sværen).
  - Steg 60 minutter. Vend ikke sværen ned. Pensl evt. med sennep.
  - Skru op til 200 °C i 15–25 minutter, til sværen bobler og knaser, og kødet er mørt.
  - Hvile 8 minutter. Server med sauerkraut, sennep eller kartoffelsalat.
faq:
  - question: Sværen bliver gummi?
    answer: Den var våd, eller væsken nåede op. Salt godt, hold sværen tør og opad, finish højt.
  - question: Støbejern-version?
    answer: Se [rustik schweinshaxe](/opskrifter/stobejern/schweinshaxe) til ølbraise i Dutch Oven — mere gæstemad, længere tid.
  - question: Én stor skank?
    answer: Ja, ca. 1 kg. Giv 15–20 minutter ekstra ved 160 °C, før finish.
  - question: Griseskank uden svær?
    answer: Samme metode, skip den høje finish — se også [griseskank i airfryer](/opskrifter/airfryer/griseskank-airfryer).
body: |
  Schweinshaxe i airfryer er tysk gæstemad i en kurv: mør skank, svær der knækker.

  Score. Salt. Lav varme. Høj finish.

  Sværen skal boble. Kødet skal slippe benet.
tip: Stil skankene åbent i køleskab 2–4 timer efter saltning, hvis du har tid — tør svær = knas.
=====
title: Skinkeculotte i ovn
slug: skinkeculotte-ovn
category: ovn
description: Skinkeculotte i ovn — saftig søndagssteg med sprød fedtkappe, kernetemperatur og hvile.
prepTime: PT15M
cookTime: PT1H10M
totalTime: PT1H35M
servings: 6
difficulty: mellem
tags:
  - skinkeculotte
  - skinkeculotte i ovn
  - culotte
  - ovn
  - svinekød
  - søndagsmad
  - kernetemperatur
imageAlt: Skinkeculotte fra ovnen skåret i skiver med sprød fedtkappe
featured: true
ingredients:
  - 1–1,2 kg skinkeculotte med fedtkappe
  - 2 tsk salt
  - 1 tsk peber
  - 1 tsk paprika
  - 1 tsk hvidløgspulver
  - 1 spsk olivenolie
  - 2 kviste rosmarin
  - 1 dl fond eller vand i fadet (valgfrit)
steps:
  - Tag kødet ud 30 minutter før. Tænd ovnen på 180 °C. Score fedtkappen i ruder uden at skære i kødet.
  - Gnid med olie, salt, peber, paprika og hvidløgspulver. Rosmarin under snor eller løst ovenpå.
  - Læg culotten i et fad med fedtsiden op. Evt. lidt fond i bunden.
  - Steg 50–70 minutter. Træk ved kernetemperatur 62–64 °C for saftig, 66–68 °C for mere gennemstegt.
  - Vil du have ekstra knas: 5 minutter ved 220 °C til sidst.
  - Hvile 10–12 minutter under løst folie. Skær i skiver på tværs af fibrene.
faq:
  - question: Hvilken kernetemperatur?
    answer: Saftig classic — træk 62–64 °C, slut ca. 65–67 °C efter hvile. Magert svin tåler ikke okse-temperaturer.
  - question: Airfryer i stedet?
    answer: Ja — se [skinkeculotte i airfryer](/opskrifter/airfryer/skinkeculotte-airfryer). Sous vide: [skinkeculotte sous vide](/opskrifter/sous-vide/skinkeculotte-sous-vide).
  - question: For stor til fadet?
    answer: Bind strammere, eller skær i to stege. Overfyldt fad giver damp, ikke skorpe.
  - question: Restemad?
    answer: Tynde skiver på rugbrød, i wraps, eller tern i pastasauce.
body: |
  Skinkeculotte i ovn er søndagssteg uden airfryer-kurv: score fedtet, salt, termometer, hvile.

  Fedtkappen skal knase. Kødet skal være rosa-beige, ikke gråt.

  Ovn er den klassiske vej — samme mål som airfryer-versionen.
tip: Stik termometret midt i den tykkeste del, væk fra fedt. Fedt lyver varmt.
=====
title: Nakkefilet i airfryer
slug: nakkefilet-airfryer
category: airfryer
description: Nakkefilet i airfryer — saftig svinenakke med stegt overflade, kernetemperatur og søndagsmad uden ovn.
prepTime: PT10M
cookTime: PT40M
totalTime: PT50M
servings: 4
difficulty: mellem
tags:
  - nakkefilet
  - nakkefilet i airfryer
  - svinenakke
  - airfryer
  - svinekød
  - søndagsmad
imageAlt: Stegt nakkefilet fra airfryeren skåret i skiver
featured: true
ingredients:
  - 800 g–1 kg nakkefilet i ét stykke
  - 2 tsk salt
  - 1 tsk peber
  - 1 tsk røget paprika
  - 1 tsk tørret oregano
  - 1 spsk olie
steps:
  - Tag kødet ud 20 minutter før. Dup tørt. Vend med olie, salt, peber, paprika og oregano.
  - Forvarm til 180 °C. Læg nakkefilétten i kurven.
  - Steg 30–40 minutter. Vend halvvejs. Træk ved kernetemperatur 65–68 °C.
  - Sidste 3–4 minutter ved 200 °C, hvis overfladen er bleg.
  - Hvile 8 minutter. Skær i skiver på tværs af fibrene.
faq:
  - question: Hvilken kernetemperatur?
    answer: Saftig nakkefilet — træk 65–68 °C. Den har mere fedt end culotte og tåler lidt højere.
  - question: Ovn-version?
    answer: Se [nakkefilet i ovn](/opskrifter/ovn/nakkefilet-ovn). Sous vide findes som [sprængt nakkefilet sous vide](/opskrifter/sous-vide/spraengt-nakkefilet-sous-vide).
  - question: Til pulled pork?
    answer: Brug lavere varme længere, eller trykkoger — nakkefilet til pulled skal være over 90 °C og trækbar.
  - question: Tilbehør?
    answer: Kartoffelsalat, grillede grøntsager, BBQ-sauce eller flødekartofler.
body: |
  Nakkefilet i airfryer er hverdagssteg med fedtmarmorering: salt, 180 °C, termometer.

  Vend halvvejs. Hvile. Skær på tværs.

  Nakkefilet tilgiver mere end mager culotte — men gætter du på tid, bliver den grå midt i.
tip: Vælg en filet der passer i kurven. For lang — fold den, eller skær i to.
=====
title: Nakkefilet i ovn
slug: nakkefilet-ovn
category: ovn
description: Nakkefilet i ovn — saftig søndagssteg af svinenakke med urter, kernetemperatur og stegesaft.
prepTime: PT15M
cookTime: PT1H
totalTime: PT1H15M
servings: 6
difficulty: mellem
tags:
  - nakkefilet
  - nakkefilet i ovn
  - svinenakke
  - ovn
  - svinekød
  - søndagsmad
  - kernetemperatur
imageAlt: Nakkefilet fra ovnen med urter og stegesaft
featured: true
ingredients:
  - 1–1,2 kg nakkefilet i ét stykke
  - 2 tsk salt
  - 1 tsk peber
  - 1 tsk paprika
  - 1 spsk olie
  - 4 kviste timian
  - 1 helt hvidløg, flækket
  - 1,5 dl fond eller æblejuice
steps:
  - Tag kødet ud 30 minutter før. Tænd ovnen på 175 °C. Dup tørt. Gnid med olie, salt, peber og paprika.
  - Læg nakkefilétten i et fad med timian og hvidløg. Hæld fond i bunden.
  - Steg 50–70 minutter, til kernen er 65–68 °C. Vend ikke.
  - Hvile 10 minutter under løst folie. Si saften, kog evt. ind, og server til.
  - Skær i skiver på tværs af fibrene.
faq:
  - question: For tør?
    answer: For høj varme eller for længe. Hold 175 °C, og brug termometer. Nakkefilet har fedt — den skal ikke til 80 °C.
  - question: Airfryer i stedet?
    answer: Se [nakkefilet i airfryer](/opskrifter/airfryer/nakkefilet-airfryer) — samme mål, kortere tid.
  - question: Med svær?
    answer: Sjældent på nakkefilet. Har den fedtkappe, score den og finish 5 minutter ved 220 °C.
  - question: Meal prep?
    answer: Ja. Skiver i boks med saft — holder 3–4 dage i køleskab.
body: |
  Nakkefilet i ovn er søndagssteg uden drama: ét stykke kød, fond i bunden, termometer.

  175 °C. Hvile. Skær på tværs.

  Det er pulled porks venligere fætter — saftig, ikke trækbar.
tip: Gem stegesaften. Den er næsten færdig sauce — bare kog ind og smag til med sennep.
=====
title: Oksehaler i trykkoger
slug: oksehaler-trykkoger
category: trykkoger
description: Oksehaler i trykkoger — geléagtigt mørt kød i mørk sky på ca. 90 minutter i stedet for 4–5 timer.
prepTime: PT25M
cookTime: PT1H30M
totalTime: PT1H55M
servings: 4
difficulty: mellem
tags:
  - oksehaler
  - oksehale
  - oksehaler i trykkoger
  - trykkoger
  - mørk sky
  - vinter
  - oksekød
imageAlt: Møre oksehaler fra trykkogeren i mørk sky
featured: true
ingredients:
  - 1,5–1,8 kg oksehale, skåret ved leddene
  - 2 spsk olie
  - 2 tsk salt, peber
  - 2 løg, 2 gulerødder, 2 stilke bladselleri — hakket
  - 2 spsk tomatpuré
  - 1 spsk hvedemel
  - 2,5 dl tør rødvin
  - 6 dl kraftig oksebouillon
  - 2 laurbærblade, 6 peberkorn, 3 kviste timian, 2 fed hvidløg
  - 1 spsk mørk soya (valgfrit)
steps:
  - Dup oksehalerne tørre. Salt og peber. Brun hårdt i olie på sautér i portioner. Tag op.
  - Svits grøntsager 8 minutter. Tomatpuré 1 minut. Drys mel over, rør 30 sekunder.
  - Vin i, skrab bunden. Bouillon, krydderier og soya i. Kød tilbage.
  - Højt tryk 55 minutter. Naturlig udligning 15 minutter.
  - Tag kødet op. Si skysovsen, reducér på sautér til den er blank og napper. Smag til. Læg kød tilbage, eller pluk af benene.
  - Server med kartoffelmos eller polenta.
faq:
  - question: Stadig sejt?
    answer: Giv 10–15 minutter mere under tryk. Oksehale skal falde fra benet — brun er ikke nok.
  - question: Støbejern-version?
    answer: Se [oksehaler i mørk sky](/opskrifter/stobejern/oksehaler-moerk-sky) til 4–5 timers ovnbraise.
  - question: For fed?
    answer: Køl, skim fedtet af, varm op. Oksehale er fed — det er pointen.
  - question: Kan den fryses?
    answer: Ja, i sauce i portioner. Smager ofte bedre dagen efter.
body: |
  Oksehaler i trykkoger er langtidssimring på turbo: gelé, mørk sky, kartoffelmos.

  Brun hårdt. Tryk 55 minutter. Reducér.

  Samme logik som svinekæber og osso buco — sejt kød elsker tryk.
tip: Brun i små portioner. Overfyldt gryde damper i stedet for at brune, og skysovsen bliver grå.
=====
title: Fasan i ovn
slug: fasan-ovn
category: ovn
description: Fasan i ovn — hel eller i stykker med bacon, æble og timian. Saftig vildtfugl til efterår og jagtbord.
prepTime: PT25M
cookTime: PT1H15M
totalTime: PT1H40M
servings: 4
difficulty: mellem
tags:
  - fasan
  - fasan opskrift
  - fasan i ovn
  - vildt
  - ovn
  - efterår
  - jagt
imageAlt: Stegt fasan fra ovnen med bacon og æble
featured: true
ingredients:
  - 1 hel fasan (ca. 1–1,2 kg), eller 4 fasanlår/-bryster
  - 8 skiver bacon
  - 2 tsk salt
  - Peber
  - 2 æbler i både
  - 1 løg i både
  - 4 kviste timian
  - 2 dl æblemost eller honsebouillon
  - 1 spsk smør
steps:
  - Tænd ovnen på 170 °C. Dup fasanen tør. Salt og peber indvendigt og udvendigt.
  - Læg æble, løg og timian i et fad. Fasán ovenpå. Svøb brystet med bacon (eller læg bacon over lår/bryst).
  - Hæld most/bouillon i bunden. Smørklat ovenpå.
  - Steg 60–75 minutter for hel fugl (lår/bryst ca. 35–45 minutter), til brystet er ca. 70–72 °C og lårene er møre.
  - Tag bacon af de sidste 5–8 minutter, hvis du vil have mere farve på skindet. Hvile 10 minutter.
  - Si saften, kog ind, server til.
faq:
  - question: Tør bryst?
    answer: Fasan er magert. Bacon på brystet og væske i fadet redder det. Overkog ikke — træk ved 70–72 °C i brystet.
  - question: Støbejern-version?
    answer: Se [grydestegt fasan](/opskrifter/stobejern/grydestegt-fasan) til braise i jernfad.
  - question: Kun lår?
    answer: Ja. Samme fad, kortere tid. Lår tåler mere end bryst.
  - question: Tilbehør?
    answer: Rodfrugtmos, rødkål, syltede bær eller cremede kartofler.
body: |
  Fasan i ovn er jagtbord uden støbejern: bacon på brystet, æble i fadet, lav-mellem varme.

  Magert kød. Beskyt brystet. Termometer.

  Det smager af efterår — ikke af tør kylling, hvis du holder igen med tiden.
tip: Bind benene løst, så fuglen steger jævnt. Løse vinger brænder før brystet er færdigt.
=====
title: Hjerter i airfryer
slug: hjerter-airfryer
category: airfryer
description: Hjerter i airfryer — møre kalve- eller grisehjerter med stegeskorpe, klar til flødesovs eller kartoffelmos.
prepTime: PT20M
cookTime: PT25M
totalTime: PT45M
servings: 4
difficulty: mellem
tags:
  - hjerter
  - hjerter i airfryer
  - kalvehjerter
  - grisehjerter
  - indmad
  - airfryer
  - mormormad
imageAlt: Stegte hjerter fra airfryeren med stegeskorpe
featured: true
ingredients:
  - 800 g kalve- eller grisehjerter, renset og i 2 cm skiver eller tern
  - 2 tsk salt
  - Peber
  - 1 tsk paprika
  - 1 tsk tørret timian
  - 1 spsk olie
  - Valgfrit til servering: flødesovs, bacon, champignon
steps:
  - Rens hjerterne: skær sener, blodpropper og hårde rør væk. Skyl, dup knastørre.
  - Vend med olie, salt, peber, paprika og timian.
  - Forvarm til 180 °C. Læg hjertestykkerne i ét lag.
  - Steg 18–25 minutter. Vend halvvejs. De skal være møre, ikke tørre — kalv er hurtigere end gris.
  - Server som de er med sennep, eller vend i varm flødesovs (se [hjerter i flødesovs](/opskrifter/gryde/hjerter-i-floedesovs)).
faq:
  - question: Hvordan renses hjerter?
    answer: Skær sener, blodpropper og hårde rør væk. Skyl i koldt vand, og dup tørre — vådt kød damper.
  - question: Sejt kød?
    answer: For kort tid, eller for store stykker. Skær ens. Grisehjerter skal have den fulde tid.
  - question: Gryde-version?
    answer: Den klassiske er [hjerter i flødesovs](/opskrifter/gryde/hjerter-i-floedesovs). Airfryer giver skorpe; gryden giver sauce.
  - question: Kyllingehjerter?
    answer: Ja — 10–12 minutter ved 180 °C. De er små og bliver hurtigt tørre.
body: |
  Hjerter i airfryer er indmad uden sprøjt: rens, krydr, 180 °C, vend.

  Skorpe først. Sauce bagefter, hvis du vil.

  Det er mormormad i en kurv — ikke en bøf, men tæt på i tekstur når det er mørt.
tip: Overfyld ikke kurven. Ét lag. To hold slår ét proppet, der damper.
=====
title: Oksehøjreb i trykkoger
slug: oksehoejreb-trykkoger
category: trykkoger
description: Oksehøjreb i trykkoger — mørt højreb i kraftig sauce på ca. 90 minutter, alternativ til langtidsstegning i ovn.
prepTime: PT20M
cookTime: PT1H25M
totalTime: PT1H45M
servings: 6
difficulty: mellem
tags:
  - oksehøjreb
  - oksehøjreb i trykkoger
  - langtidsstegt oksehøjreb
  - trykkoger
  - oksekød
  - søndagsmad
imageAlt: Mørt oksehøjreb fra trykkogeren i kraftig sauce
featured: true
ingredients:
  - 1,5–1,8 kg oksehøjreb, i 4–5 cm tern (eller ét stykke der passer)
  - 2 tsk salt
  - Peber
  - 2 spsk olie
  - 2 løg, 2 gulerødder — hakket
  - 2 fed hvidløg
  - 1 spsk tomatpuré
  - 2 dl rødvin
  - 4 dl oksebouillon
  - 1 bundt timian, 2 laurbærblade
  - 1 spsk smør til montering (valgfrit)
steps:
  - Dup kødet tørt. Salt og peber. Brun hårdt i olie på sautér i portioner. Tag op.
  - Svits løg og gulerod 6 minutter. Hvidløg og tomatpuré 1 minut. Vin i, skrab bunden.
  - Bouillon, timian og laurbær i. Kød tilbage.
  - Højt tryk 60 minutter for tern (70 minutter for ét stort stykke). Naturlig udligning 15 minutter.
  - Tag kødet op. Si og reducér saucen. Montér med smør. Læg kød tilbage.
  - Server med kartoffelmos, rodfrugter eller bløde polenta.
faq:
  - question: Ovn-version i stedet?
    answer: Se [langtidsstegt oksehøjreb med hvidløg og timian](/opskrifter/ovn/langtidsstegt-oksehoejreb-hvidloeg-timian) til rosa reverse sear. Trykkoger giver braiseret, mørt kød — ikke rosa stege-kerne.
  - question: Vil jeg have rosa midte?
    answer: Brug ovn-metoden. Tryk + højreb = gryderet-tekstur, ikke roastbeef.
  - question: For lidt sauce?
    answer: Tilsæt fond før reducering. Reducér til den napper — ikke til den er sirup.
  - question: Kan det fryses?
    answer: Ja, i sauce. Tø i køleskab, varm forsigtigt.
body: |
  Oksehøjreb i trykkoger er den braiserede fætter til ovn-vinderen: samme kød, anden tekstur.

  Brun. Tryk. Reducér.

  Du får ikke rosa stege — du får mørt søndagskød i kraftig sauce.
tip: Skær i tern, hvis du vil have jævn tilberedning. Ét stort stykke kræver mere tid og er sværere at brune.
=====
title: Brunkål i ovn
slug: brunkaal-ovn
category: ovn
description: Brunkål i ovn med flæsk og brunt sukker — mør julekål uden trykkoger, klar til flæskesteg og medister.
prepTime: PT20M
cookTime: PT1H30M
totalTime: PT1H50M
servings: 6
difficulty: mellem
tags:
  - brunkål
  - brunkål i ovn
  - julemad
  - flæsk
  - ovn
  - dansk klassiker
  - dansk-klassiker
  - vinter
imageAlt: Mør brunkål med flæsk fra ovnen
featured: true
ingredients:
  - 1 kg hvidkål, i grove både
  - 400 g flæsk i tern, eller røget bacon
  - 2 spsk smør
  - 3 spsk sukker
  - 1 tsk salt
  - 2 dl vand eller æblemost
  - 1 spsk eddike
  - Friskkværnet peber
steps:
  - Tænd ovnen på 180 °C. Brun sukkeret i en stor ovnfast gryde eller fad på komfuret, til det er gyldent. Rør smør i.
  - Vend kål og flæsk i det brune sukker, til kålen tager farve. Tilsæt vand/most, salt og peber.
  - Låg på (eller dæk med folie). I ovnen 60 minutter.
  - Tag låg af. Rør rundt. 20–30 minutter mere, til kålen er mør, og væden er indkogt.
  - Smag med eddike og mere salt. Server til flæskesteg, medister eller frikadeller.
faq:
  - question: Hvorfor eddike til sidst?
    answer: Syren skærer igennem sukker og flæsk. Uden den smager kålen kun sødt og fedt.
  - question: Trykkoger i stedet?
    answer: Se [brunkål i trykkoger](/opskrifter/trykkoger/brunkaal) — under en time. Ovn er mere hands-off til juleaften.
  - question: Kan man bruge grønkål?
    answer: Nej. Brunkål er hvidkål, der brunes. Grønkål bliver bitter her.
  - question: Dagen før?
    answer: Ja. Brunkål smager bedre genopvarmet. Køl, og varm forsigtigt med en skvæt vand.
body: |
  Brunkål i ovn er julekål uden tryk: brun sukker, flæsk, låg på, vent.

  Farve først. Mørt bagefter. Eddike til sidst.

  Det er ikke stuvet hvidkål — det er karameliseret vinter.
tip: Røget flæsk salter mere end fersk. Vent med ekstra salt, til du har smagt efter ovntiden.
=====
title: Fløjlsgrød i trykkoger
slug: floejsgoed-trykkoger
category: trykkoger
description: Fløjlsgrød i trykkoger — gammeldags melgrød med smørklat, næsten uden klumper og uden konstant omrøring.
prepTime: PT5M
cookTime: PT20M
totalTime: PT25M
servings: 4
difficulty: nem
tags:
  - fløjlsgrød
  - fløjlsgrød trykkoger
  - gammeldags fløjlsgrød
  - melgrød
  - trykkoger
  - mormormad
  - hvidtølssukker
imageAlt: Fløjlsgrød fra trykkogeren med smørklat og hvidtølssukker
featured: true
ingredients:
  - 50 g smør
  - 1 dl hvedemel
  - 1 liter sødmælk
  - ½ tsk salt
  - Smørklat til servering
  - Hvidtølssukker eller kanelsukker
steps:
  - Smelt smør på sautér. Rør melet i, og lad det lyse stege 1–2 minutter under omrøring — det må ikke blive mørkt.
  - Pisk 2 dl af mælken i, til det er en glat pasta. Tilsæt resten af mælken under omrøring. Salt i.
  - Luk. Højt tryk 8 minutter. Hurtig udligning.
  - Åbn, pisk kraftigt (eller brug stavblender 5 sekunder), hvis der er hinde eller små klumper. Simre 2–3 minutter på sautér, til den er blank.
  - Server rygende varm med smørklat og hvidtølssukker.
faq:
  - question: Hvad er hvidtølssukker?
    answer: Sukker med stødt kanel og ofte lidt stødt nellike — klassisk til melgrød og øllebrød.
  - question: Klumper?
    answer: Pisk melet godt ind i smørret først, og pisk efter tryk. Stavblender redder næsten alt.
  - question: Gryde-version?
    answer: Se [gammeldags fløjlsgrød](/opskrifter/gryde/gammeldags-floejsgoed) — samme resultat, mere omrøring.
  - question: For tyk?
    answer: Rør mere mælk i på sautér. Den tykner mere ved henstand.
body: |
  Fløjlsgrød i trykkoger er mormors genvej uden piskearm: smør, mel, mælk — tryk, pisk, smørklat.

  Lys roux. Kort tryk. Blank finish.

  Det er ikke risengrød. Det er fløjl i en skål.
tip: Fyld ikke trykkogeren mere end halvvejs med mælkegrød — den kan skumme op under tryk.
'''


def parse_block(block: str) -> dict:
    lines = block.strip().split("\n")
    data: dict = {
        "tags": [],
        "ingredients": [],
        "steps": [],
        "faq": [],
    }
    mode = None
    body_lines: list[str] = []
    current_q = None
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
        elif line.startswith("tip: "):
            data["tip"] = line[5:]
            mode = None
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
'''


blocks = [b for b in RECIPES.split("=====") if b.strip()]
print(f"blocks: {len(blocks)}")
for b in blocks:
    d = parse_block(b)
    assert d.get("faq") and len(d["faq"]) >= 3, (d.get("slug"), len(d.get("faq", [])))
    assert d.get("tip"), d.get("slug")
    assert d.get("body"), d.get("slug")
    out = ROOT / d["category"]
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{d['slug']}.mdx"
    if path.exists():
        raise SystemExit(f"slug collision: {path}")
    path.write_text(to_mdx(d), encoding="utf-8")
    print("wrote", d["category"] + "/" + path.name)
