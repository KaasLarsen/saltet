#!/usr/bin/env python3
"""Vinter-comfort batch 2 — flere gryder, hverdagsretter, supper og sødt (okt 2026)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"
PUBLISHED = "2026-10-29"

RECIPES = r'''
=====
title: Braiserede svinekæber i mørkt øl
slug: braiserede-svinekaeber-moerkt-oel
category: gryde
description: Ultramøre svinekæber braiseret i porter eller julebryg — dyb, reduceret sauce serveret med grov kartoffelmos.
prepTime: PT30M
cookTime: PT2H30M
totalTime: PT3H
servings: 4
difficulty: mellem
tags:
  - svinekæber
  - mørkt øl
  - porter
  - braisering
  - gryderet
  - vinter
  - kartoffelmos
  - gryde
imageAlt: Møre svinekæber i mørk ølsauce med grov kartoffelmos
featured: true
ingredients:
  - 1 kg svinekæber, putset for hinder
  - 2 spsk smør + 1 spsk olie
  - 2 løg, hakket
  - 2 gulerødder, i skiver
  - 2 stilke bladselleri, hakket
  - 2 fed hvidløg
  - 2 spsk tomatpuré
  - 1 spsk hvedemel
  - 33 cl porter, stout eller julebryg
  - 4 dl oksebouillon
  - 2 laurbærblade, 4 kviste timian
  - 1 spsk mørk sirup eller brunt sukker
  - Salt, peber
  - Grov mos: 800 g kartofler, 50 g smør, ½ dl mælk, salt
steps:
  - Dup kæberne tørre. Salt og peber. Brun hårdt i smør og olie i en tung gryde. Tag op.
  - Svits løg, gulerod og selleri 8–10 minutter. Hvidløg og tomatpuré 1 minut. Drys mel over.
  - Hæld øl i, skrab bunden. Bouillon, laurbær, timian og sirup i. Læg kæberne tilbage.
  - Simre med låg 2–2½ time, til kødet er ultramørt. Tag kødet op. Reducer saucen hvis den er tynd.
  - Kog kartofler, mos groft med smør og mælk. Server kæberne i saucen over mosen.
faq:
  - question: Hvilket øl?
    answer: Porter, stout eller julebryg med malt. Undgå bitter IPA — den bliver for skarp efter reduktion.
  - question: Kan de laves dagen før?
    answer: Ja. Smagen bliver dybere. Varm forsigtigt op i saucen.
  - question: Ovnen i stedet?
    answer: Efter bruning — 160 °C med låg i 2½ time.
  - question: Erstatning for kæber?
    answer: Svinekam i store tern eller oksehaler. Tilpas tiden til kødet er mørt.
body: |
  Braiserede svinekæber i mørkt øl er vinterluksus: kollagen, malt og tålmodighed.

  Brun hårdt. Øl ind. Simre længe.

  Den grove mos er den rigtige makker — ikke finpuré.
tip: Putse hinderne væk før bruning — ellers bliver kødet sejt uanset hvor længe det simrer.
=====
title: Kylling Stroganoff
slug: kylling-stroganoff
category: gryde
description: Hurtig, cremet kylling Stroganoff med svampe, paprika og cremefraiche — hverdagsudgaven af klassikeren.
prepTime: PT15M
cookTime: PT25M
totalTime: PT40M
servings: 4
difficulty: nem
tags:
  - kylling stroganoff
  - stroganoff
  - kylling
  - svampe
  - cremefraiche
  - paprika
  - vinter
  - gryde
imageAlt: Cremet kylling Stroganoff med svampe i paprika-sauce
featured: true
ingredients:
  - 600 g kyllingebryst eller lårfilet, i strimler
  - 250 g champignon, skivede
  - 1 stort løg, hakket
  - 2 fed hvidløg
  - 1 spsk smør + 1 spsk olie
  - 1 spsk paprika
  - 1 tsk røget paprika
  - 1 spsk tomatpuré
  - 2 dl hønsebouillon
  - 2 dl cremefraiche 18 %
  - 1 tsk dijonsennep
  - Salt, peber, persille
  - Ris eller pasta til servering
steps:
  - Brun kyllingestrimler i olie og smør i portioner. Tag op.
  - Svits løg 5 minutter. Svampe i, til væsken er væk. Hvidløg, paprika og tomatpuré 1 minut.
  - Bouillon i, skrab bunden. Læg kylling tilbage. Simre 8–10 minutter.
  - Tag gryden af varmen. Rør cremefraiche og sennep i. Varm igennem uden at koge.
  - Smag til. Persille. Server med ris eller pasta.
faq:
  - question: Hvorfor ikke koge cremefraichen?
    answer: Den kan skille. Rør den i af varmen, og varm kun forsigtigt.
  - question: Oksekød i stedet?
    answer: Ja — klassisk bøf Stroganoff. Brun kødet meget kort, så det ikke bliver sejt.
  - question: Lettere version?
    answer: Brug 9 % cremefraiche eller skyr blandet med lidt fløde.
  - question: Svampetype?
    answer: Champignon er klassisk. Bland gerne med østershatte for mere dybde.
body: |
  Kylling Stroganoff er hverdagsstroganoff: hurtig, cremet, fyldt med svampe.

  Paprikaen giver farve. Cremefraichen lukker.

  Ris under — sauce ovenpå.
tip: Brun kyllingen i portioner, ellers damper den og bliver grå i stedet for gylden.
=====
title: Gammeldags oksehaleragout
slug: gammeldags-oksehaleragout
category: gryde
description: Langtidssimrede oksehaler i rødvin og urter — luksusmad, hvor kødet falder fuldstændig fra benene.
prepTime: PT30M
cookTime: PT3H30M
totalTime: PT4H
servings: 6
difficulty: mellem
tags:
  - oksehaler
  - oksehaleragout
  - rødvin
  - gryderet
  - braisering
  - vinter
  - luksus
  - gryde
imageAlt: Mør oksehaleragout i dyb rødvinssauce med gulerødder og urter
featured: true
ingredients:
  - 2 kg oksehaler, skåret i led
  - 3 spsk hvedemel
  - 2 spsk smør + 2 spsk olie
  - 2 løg, 2 gulerødder, 2 stilke bladselleri — hakket
  - 3 fed hvidløg
  - 2 spsk tomatpuré
  - 5 dl tør rødvin
  - 5 dl oksebouillon
  - 2 laurbærblade, 4 kviste timian, 2 kviste rosmarin
  - Salt, peber, persille
steps:
  - Vend oksehaler i mel, salt og peber. Brun grundigt i smør og olie. Tag op.
  - Svits løg, gulerod og selleri 10 minutter. Hvidløg og tomatpuré 1 minut.
  - Hæld vin i, skrab bunden, kog 3 minutter. Bouillon og urter i. Læg halerne tilbage.
  - Simre med låg 3–3½ time (eller 160 °C i ovnen), til kødet glider af benet.
  - Tag benene fra. Skum fedt af saucen. Smag til. Persille. Server med mos eller polenta.
faq:
  - question: Kan den laves i trykkoger?
    answer: Ja — ca. 45–55 minutter under tryk efter bruning. Slip trykket naturligt.
  - question: For fed sauce?
    answer: Køl gryden, og løft fedlaget af. Eller brug en fedtudskiller.
  - question: Dagen før?
    answer: Ideelt. Smagen sætter sig, og fedtet er nemmere at fjerne koldt.
  - question: Hvilken vin?
    answer: Tør, fyldig rødvin. Billig bordeaux eller syrah — ikke dessertvin.
body: |
  Gammeldags oksehaleragout er tålmodighed belønnet med kød, der falder fra benene.

  Brun. Vin. Lang simre.

  Det er søndagsmad til frostvejr.
tip: Brug en gryde, der netop kan rumme benene i ét lag — for meget plads giver tynd sauce.
=====
title: Svensk pølseret til vinteren
slug: svensk-poelseret-vinter
category: gryde
description: Børnevenlig vinter-comfortfood — kartofler, pølser og cremet tomat-paprikasovs i én gryde.
prepTime: PT15M
cookTime: PT30M
totalTime: PT45M
servings: 4
difficulty: nem
tags:
  - svensk pølseret
  - pølseret
  - pølser
  - kartofler
  - paprika
  - børnevenlig
  - vinter
  - gryde
imageAlt: Svensk pølseret med kartofler i cremet tomat-paprikasovs
featured: true
ingredients:
  - 600 g kartofler, skrællet og i tern
  - 400 g wienerpølser eller grillpølser, i skrå skiver
  - 1 stort løg, hakket
  - 1 rød peberfrugt, i tern
  - 1 spsk smør + 1 spsk olie
  - 1 spsk paprika
  - 1 spsk tomatpuré
  - 2 dl hønsebouillon
  - 2 dl piskefløde
  - 1 tsk sukker
  - Salt, peber, persille
steps:
  - Brun pølseskiverne i olie. Tag op. Svits løg og peberfrugt 5–7 minutter.
  - Paprika og tomatpuré 30 sekunder. Kartofler, bouillon og sukker i. Simre med låg 15–20 minutter, til kartoflerne er møre.
  - Rør fløde i. Læg pølser tilbage. Simre 5 minutter uden låg, til saucen er cremet.
  - Smag til. Persille. Server med rugbrød eller bare som den er.
faq:
  - question: Hvilke pølser?
    answer: Wiener, frankfurter eller milde grillpølser. Stærk chorizo ændrer retten.
  - question: Kan den laves uden fløde?
    answer: Ja — brug mælk og en teskefuld mel, eller cremefraiche til sidst.
  - question: Mere grønt?
    answer: Ærter eller majs de sidste 5 minutter er klassisk børnevenligt tilskud.
  - question: Dagen efter?
    answer: Den smager fint opvarmet. Tilsæt lidt bouillon, så den ikke bliver for tyk.
body: |
  Svensk pølseret er vinterens fredagsgryde: pølser, kartofler, paprika, fløde.

  Én gryde. Kort tid. Alle spiser.

  Det er comfortfood uden undskyldning.
tip: Brun pølserne først — den skorpe giver mere smag end at koge dem direkte i saucen.
=====
title: Boller i selleri
slug: boller-i-selleri
category: gryde
description: Den oversete fætter til boller i karry — kødboller i cremet opbagt sauce med masser af knoldselleritern.
prepTime: PT25M
cookTime: PT35M
totalTime: PT1H
servings: 4
difficulty: nem
tags:
  - boller i selleri
  - kødboller
  - knoldselleri
  - opbagt sauce
  - dansk
  - mormormad
  - vinter
  - gryde
imageAlt: Kødboller i cremet sellerisauce med knoldselleritern
featured: true
ingredients:
  - Kødboller: 500 g hakket kalv/svin, 1 æg, 1 dl mælk, 3 spsk rasp, 1 løg finthakket, salt, peber
  - 500 g knoldselleri, i 1 cm tern
  - 40 g smør
  - 3 spsk hvedemel
  - 6 dl mælk (eller 5 dl mælk + 1 dl hønsebouillon)
  - 1 knivspids muskatnød
  - Salt, peber, persille
  - Ris eller kartofler til servering
steps:
  - Bland farsen, og form 16–20 boller. Brun dem let i lidt smør. Tag op.
  - Kog selleritern 8–10 minutter i let saltet vand, til de er møre men stadig har bid. Hæld fra.
  - Smelt smør, rør mel i. Pisk mælk i til en glat sauce. Muskat, salt, peber.
  - Læg boller og selleri i saucen. Simre under låg 15–20 minutter, til bollerne er gennemstegte.
  - Persille. Server med ris eller kogte kartofler.
faq:
  - question: Smager det meget af selleri?
    answer: Det er mildt og nøddeagtigt, ikke skarpt. Muskat og mælk runder det af.
  - question: Kan man bruge bladselleri?
    answer: Nej — det er knoldselleri, der giver fylde. Bladselleri bliver for træagtig her.
  - question: Færdigkøbte kødboller?
    answer: Ja i nød. Brun dem, og lad dem få 10 minutter i saucen.
  - question: Forskel på boller i karry?
    answer: Samme bolle-idé, men selleri og hvid sauce i stedet for karry og æble.
body: |
  Boller i selleri er mormorkøkkenets skjulte hit: kødboller i cremet sellerisauce.

  Opbagningen skal være glat. Sellerien skal have bid.

  Det er ikke karry — og det skal det heller ikke være.
tip: Skær sellerien i ens tern, så de bliver møre samtidig. For store stykker er stadig rå midt i saucen.
=====
title: Kåldolmere
slug: kaaldolmere
category: ovn
description: Klassisk mormormad — krydret fars pakket i blancherede hvidkålsblade, bagt i ovnen med skysovs.
prepTime: PT40M
cookTime: PT1H
totalTime: PT1H40M
servings: 4
difficulty: mellem
tags:
  - kåldolmere
  - hvidkål
  - fars
  - skysovs
  - mormormad
  - dansk
  - vinter
  - ovn
imageAlt: Bagt kåldolmere i fad med skysovs
featured: true
ingredients:
  - 1 stor hvidkål
  - 500 g hakket kalv/svin
  - 1 dl kogte ris
  - 1 løg, finthakket
  - 1 æg
  - 1 tsk salt, peber, ½ tsk allehånde
  - 2 dl hønse- eller oksebouillon
  - 2 spsk smør
  - 1 spsk hvedemel
  - 1 dl fløde (valgfrit)
steps:
  - Kog hele kålhovedet 5–8 minutter, eller blanchér bladene enkeltvis, til de er bøjelige. Skær den tykke midterribbe flad.
  - Bland fars, ris, løg, æg og krydderi. Læg 1–2 spsk fars på hvert blad, fold ind, og rul tæt.
  - Læg dolmerne tæt i et smurt ovnfast fad. Fordel smørklatter og bouillon over.
  - Bag ved 180 °C i 50–60 minutter, til farsen er gennemstegt.
  - Hæld skyen fra i en gryde. Jævn med smør og mel (evt. fløde). Smag til. Server over dolmerne.
faq:
  - question: Bladene flækker?
    answer: Blanchér dem lidt længere, og skær midterribben tyndere. Brug de yderste store blade.
  - question: Kan de fryses?
    answer: Ja — helst før bagning. Tø i køleskab, og bag som anvist.
  - question: Surkål i stedet?
    answer: Det er en anden ret. Her er det mild hvidkål, der bærer farsen.
  - question: Tilbehør?
    answer: Kartofler, tyttebær eller syltede rødbeder. Klassisk dansk tallerken.
body: |
  Kåldolmere er fars i kålblad — bagt, saftig og mormor-korrekt.

  Blanchér bladene. Rul tæt. Bag i sky.

  Saucen fra fadet er pointen.
tip: Læg dolmerne med samlingen nedad i fadet, så de ikke folder sig ud under bagningen.
=====
title: Chili sin Carne med chokolade
slug: chili-sin-carne-chokolade
category: gryde
description: Vegetarisk chili med bønner, linser og dybde fra mørk kakao — varmende vintergryde uden kød.
prepTime: PT20M
cookTime: PT45M
totalTime: PT1H5M
servings: 6
difficulty: nem
tags:
  - chili sin carne
  - vegetar
  - bønner
  - linser
  - chokolade
  - kakao
  - vinter
  - gryde
imageAlt: Mørk vegetarisk chili med bønner og et skær af kakao
featured: true
ingredients:
  - 1 løg, hakket
  - 2 røde peberfrugter, i tern
  - 3 fed hvidløg
  - 2 spsk olivenolie
  - 2 spsk chilipulver eller mild chili
  - 1 spsk spidskommen
  - 1 tsk røget paprika
  - 2 spsk tomatpuré
  - 2 dåser hakkede tomater (à 400 g)
  - 1 dåse kidneybønner, skyllede
  - 1 dåse sorte bønner, skyllede
  - 150 g røde linser, skyllede
  - 5 dl grøntsagsbouillon
  - 20 g mørk chokolade (70 %) eller 1 spsk usødet kakao
  - Salt, peber, lime, koriander
steps:
  - Svits løg og peberfrugt i olie 8 minutter. Hvidløg, chili, spidskommen, paprika og tomatpuré 1 minut.
  - Tomater, bønner, linser og bouillon i. Bring i kog, simre 30–35 minutter under omrøring.
  - Rør chokolade eller kakao i. Smag til med salt, peber og lime.
  - Server med ris, tortillachips, skyr eller avocado. Koriander ovenpå.
faq:
  - question: Hvorfor chokolade?
    answer: Den giver dybde og afrunder chilien — ikke sød dessert-smag. Brug mørk, ikke mælkechokolade.
  - question: For stærk?
    answer: Start med mild chili, og tilsæt mere til sidst. Kakao og lime dæmper også.
  - question: Kan den fryses?
    answer: Ja i portioner. Den smager ofte bedre dagen efter.
  - question: Uden linser?
    answer: Brug ekstra bønner eller hakkede champignon for fylde.
body: |
  Chili sin Carne med chokolade er vegetarisk vintergryde med kant.

  Bønner og linser mætter. Kakaoen giver dybde.

  Lime til sidst — det løfter det hele.
tip: Tilsæt chokoladen først til sidst, så den smelter ind uden at brænde.
=====
title: Ristaffel med kylling i karry
slug: ristaffel-kylling-karry
category: gryde
description: Varm kylling i karry til ristaffel — med kokos, peanuts, rosiner, bananer og de klassiske vintertilbehør.
prepTime: PT25M
cookTime: PT35M
totalTime: PT1H
servings: 6
difficulty: nem
tags:
  - ristaffel
  - kylling i karry
  - karry
  - kokos
  - festmad
  - vinter
  - gryde
imageAlt: Kylling i karry på ris med ristaffel-tilbehør omkring
featured: true
ingredients:
  - 800 g kyllingelårfilet, i tern
  - 2 løg, hakket
  - 2 æbler, i tern
  - 2 spsk smør
  - 2–3 spsk karry
  - 1 spsk hvedemel
  - 4 dl hønsebouillon
  - 2 dl piskefløde eller kokosmælk
  - Salt, peber
  - Ris til 6 personer
  - Tilbehør: bananskiver, rosiner, peanuts, kokosmel, chutney, agurkesalat, hakkede tomater
steps:
  - Brun kylling i smør. Tag op. Svits løg og æble 5 minutter. Rør karry og mel i.
  - Bouillon i under omrøring. Læg kylling tilbage. Simre 20 minutter.
  - Rør fløde eller kokosmælk i. Smag til.
  - Kog ris. Arranger tilbehør i små skåle.
  - Server karryen over ris med frit valg af tilbehør — det er ristaffel.
faq:
  - question: Hvad skal der på bordet?
    answer: Mindst banan, peanuts, rosiner, kokos og chutney. Jo flere små skåle, jo mere fest.
  - question: Stærk karry?
    answer: Brug mild karry til klassisk dansk ristaffel. Gæsterne kan selv tilføje chili.
  - question: Kan saucen laves dagen før?
    answer: Ja. Varm op forsigtigt, og kog friske ris til servering.
  - question: Vegetarisk?
    answer: Brug kikærter eller blomkål i stedet for kylling. Samme sauce og tilbehør.
body: |
  Ristaffel er ikke bare kylling i karry — det er bordet fuldt af små skåle.

  Karryen er basen. Tilbehøret er legen.

  Det er vinterfest uden at være højtidsmiddag.
tip: Rist peanuts og kokos let på en tør pande — de smager mere, og bordet dufter færdigt.
=====
title: Shepherd's Pie til vinteren
slug: shepherds-pie-vinter
category: ovn
description: Krydret hakket lam (eller okse) med ærter og gulerødder under et gyldent låg af gratineret kartoffelmos.
prepTime: PT30M
cookTime: PT45M
totalTime: PT1H15M
servings: 6
difficulty: nem
tags:
  - shepherd's pie
  - shepherds pie
  - lam
  - kartoffelmos
  - ovnret
  - comfort food
  - vinter
  - ovn
imageAlt: Shepherd's pie med gyldent kartoffelmos-låg i ovnfast fad
featured: true
ingredients:
  - 700 g hakket lam (eller okse til cottage pie)
  - 1 løg, 2 gulerødder, 2 stilke bladselleri — hakket
  - 2 fed hvidløg
  - 1 spsk tomatpuré
  - 1 spsk hvedemel
  - 2 dl okse- eller lammebouillon
  - 1 spsk Worcestershire sauce
  - 1 tsk timian
  - 150 g frostærter
  - 1 kg kartofler
  - 50 g smør + 1 dl mælk
  - 50 g revet ost (valgfrit)
  - Salt, peber
steps:
  - Brun kødet. Svits løg, gulerod og selleri 8 minutter. Hvidløg, tomatpuré og mel 1 minut.
  - Bouillon, Worcestershire og timian i. Simre 15 minutter. Rør ærter i. Smag til.
  - Kog kartofler, mos med smør og mælk. Salt.
  - Læg kødfyld i ovnfast fad. Fordel mos over, ru overfladen med en gaffel. Ost ovenpå hvis du vil.
  - Bag ved 200 °C i 25–30 minutter, til låget er gyldent. Hvile 5 minutter før servering.
faq:
  - question: Lam eller okse?
    answer: Klassisk shepherd's pie er lam. Med okse hedder det cottage pie — samme metode.
  - question: Mosen synker i?
    answer: Lad fyldet køle lidt, før mosen lægges på. Eller pipér mosen i et tykkere lag.
  - question: Kan den fryses?
    answer: Ja før den sidste bagning. Bag fra frossen ved 180 °C ca. 45–50 minutter.
  - question: Uden Worcestershire?
    answer: Brug soja og en skvæt eddike til umami og syre.
body: |
  Shepherd's Pie er vinter under kartoffelmos: krydret fars, ærter, gulerødder, gyldent låg.

  Fyldet skal være saftigt. Mosen skal være ru på toppen.

  Ovnen klarer gratineringen.
tip: Ru mosen med en gaffel — toppene bliver sprøde og gyldne i ovnen.
=====
title: Svampelasagne
slug: svampelasagne
category: ovn
description: Fyldig vegetarlasagne med masser af svampe, timian og cremet béchamel — intens vinterrodsret.
prepTime: PT35M
cookTime: PT45M
totalTime: PT1H20M
servings: 6
difficulty: mellem
tags:
  - svampelasagne
  - lasagne
  - svampe
  - vegetar
  - béchamel
  - timian
  - vinter
  - ovn
imageAlt: Oppsnittet svampelasagne med cremet béchamel og gylden ostetop
featured: true
ingredients:
  - 600 g blandede svampe, hakket
  - 1 løg, 2 fed hvidløg
  - 2 spsk olivenolie + 1 spsk smør
  - 1 spsk tomatpuré
  - 1 dl hvidvin (valgfrit)
  - 1 dåse hakkede tomater (400 g)
  - 2 tsk frisk timian (eller 1 tsk tørret)
  - Béchamel: 50 g smør, 50 g hvedemel, 7 dl mælk, muskat, salt, peber
  - 12 lasagneplader
  - 150 g revet mozzarella eller blandet ost
  - 50 g parmesan
steps:
  - Svits løg i olie og smør. Svampe i ved høj varme, til væsken er væk. Hvidløg, tomatpuré, vin, tomater og timian. Simre 15 minutter.
  - Béchamel: smelt smør, rør mel i, pisk mælk i til tyk sauce. Muskat, salt, peber.
  - Lag i fad: béchamel, plader, svampefyld, ost — gentag. Afslut med béchamel og ost.
  - Bag ved 180 °C i 40–45 minutter, til toppen er gylden. Hvile 10 minutter før udskæring.
faq:
  - question: Hvilke svampe?
    answer: Champignon som base, plus portobello eller østershatte. Jo mere sort, jo mere umami.
  - question: Uden vin?
    answer: Drop den, og tilsæt 1 tsk soja til dybde.
  - question: Friske eller tørre lasagneplader?
    answer: Tørre virker, hvis saucerne er lidt mere flydende. Friske giver mere kontrol.
  - question: Kan den laves dagen før?
    answer: Ja. Bag den, køl, og varm op ved 160 °C i 25 minutter.
body: |
  Svampelasagne er vegetarisk vinter uden at mangle fylde.

  Svampene skal miste væske. Béchamelen skal være cremet.

  Ti minutters hvile — så skærer den rent.
tip: Brun svampene hårdt i portioner. Overfyldt pande damper, og lasagnen bliver vandig.
=====
title: Dahl med skyr og koriander
slug: dahl-skyr-koriander
category: gryde
description: Indisk linsedahl med varme krydderier — serveret med kold skyr og frisk koriander til kontrasten.
prepTime: PT15M
cookTime: PT35M
totalTime: PT50M
servings: 4
difficulty: nem
tags:
  - dahl
  - dal
  - linser
  - skyr
  - koriander
  - indisk
  - vinter
  - gryde
imageAlt: Gul dahl i skål toppet med skyr og frisk koriander
featured: true
ingredients:
  - 300 g røde linser, skyllede
  - 1 løg, hakket
  - 3 fed hvidløg, 1 spsk frisk ingefær
  - 1 spsk ghee eller olie
  - 1 tsk spidskommenfrø
  - 1 tsk gurkemeje
  - 1 tsk garam masala
  - ½–1 tsk chiliflager
  - 1 dåse hakkede tomater (400 g)
  - 8 dl vand eller grøntsagsbouillon
  - Salt, citronsaft
  - 2 dl skyr til servering
  - Frisk koriander, evt. naan eller ris
steps:
  - Varm ghee. Svits spidskommenfrø 30 sekunder. Løg 5 minutter. Hvidløg og ingefær 1 minut.
  - Gurkemeje, garam masala og chili i. Tomater og linser i. Vand i.
  - Simre 25–30 minutter under omrøring, til dahl er cremet. Tilsæt vand hvis den tykner for meget.
  - Smag til med salt og citron. Server med en klat skyr og masser af koriander.
faq:
  - question: Røde eller grønne linser?
    answer: Røde bliver cremede og passer til dahl. Grønne holder formen mere.
  - question: For stærk?
    answer: Drop chiliflager, og lad skyren køle munden.
  - question: Kan den fryses?
    answer: Ja. Den tykner — fortynd med vand ved opvarmning.
  - question: Uden koriander?
    answer: Brug persille. Det er anderledes, men friskheden mangler stadig uden noget grønt.
body: |
  Dahl med skyr og koriander er varme krydderier mødt af kold syre.

  Linserne skal nærmest smelte. Skyren skal være kold.

  Det er vintermad, der varmer indefra.
tip: Rør tit de sidste 10 minutter — røde linser sætter sig let i bunden.
=====
title: Hokkaido-græskarsuppe med ingefær
slug: hokkaido-graeskarsuppe-ingefaer
category: gryde
description: Fløjlsblød Hokkaido-græskarsuppe med ingefær, chili og lime — serveret med ristede græskarkerner.
prepTime: PT20M
cookTime: PT35M
totalTime: PT55M
servings: 4
difficulty: nem
tags:
  - græskarsuppe
  - hokkaido
  - ingefær
  - chili
  - lime
  - vinter
  - suppe
  - gryde
imageAlt: Cremet orange Hokkaido-suppe med ristede græskarkerner og lime
featured: true
ingredients:
  - 1 Hokkaido (ca. 1,2 kg), udkernet og i tern (skal kan blive på)
  - 1 løg, hakket
  - 2 fed hvidløg
  - 1 spsk frisk ingefær, reven
  - 1 spsk smør + 1 spsk olie
  - ½–1 tsk chiliflager
  - 1 liter grøntsagsbouillon
  - 1 dl piskefløde eller kokosmælk
  - Saft af ½ lime
  - Salt, peber
  - 3 spsk græskarkerner, ristede
steps:
  - Svits løg i smør og olie 5 minutter. Hvidløg, ingefær og chili 1 minut.
  - Græskar og bouillon i. Simre 25 minutter, til græskaret er mørt.
  - Blend glat. Rør fløde i. Smag til med salt, peber og lime.
  - Rist kerner på en tør pande. Server suppen med kerner og evt. ekstra lime.
faq:
  - question: Skal Hokkaido skrælles?
    answer: Nej — skallen bliver blød og kan blendes med. Spar tid.
  - question: Uden fløde?
    answer: Kokosmælk eller bare bouillon. En kogt kartoffel giver også cremethed.
  - question: Kan den fryses?
    answer: Ja før fløden. Tilsæt fløde ved opvarmning.
  - question: Butternut i stedet?
    answer: Ja — skræl den. Smagen er lidt sødere.
body: |
  Hokkaido-græskarsuppe er orange vinter i skålform.

  Ingefær og chili varmer. Lime klipper.

  De ristede kerner er den sprøde finale.
tip: Rist kernerne med en knivspids salt — de smager af mere end rå kerner ovenpå.
=====
title: Vinter-minestrone
slug: vinter-minestrone
category: gryde
description: Italiensk minestrone med tomat, bønner, små pastaer og vinterens grove grøntsager — mættende og klar på under en time.
prepTime: PT20M
cookTime: PT40M
totalTime: PT1H
servings: 6
difficulty: nem
tags:
  - minestrone
  - italiensk
  - bønner
  - pasta
  - grøntsagssuppe
  - vinter
  - suppe
  - gryde
imageAlt: Fyldig minestrone med pasta, bønner og vintergrøntsager
featured: true
ingredients:
  - 1 løg, 2 gulerødder, 2 stilke bladselleri, 1 porre — hakket
  - 2 fed hvidløg
  - 2 spsk olivenolie
  - 1 spsk tomatpuré
  - 1 dåse hakkede tomater (400 g)
  - 1,5 liter grøntsagsbouillon
  - 1 dåse cannellini- eller borlottibønner, skyllede
  - 150 g små pasta (ditalini eller macaroni)
  - 200 g savoykål eller grønkål, snittet
  - 1 parmesanskorpe (valgfrit)
  - Salt, peber, basilikum eller persille, olivenolie til dryp
steps:
  - Svits løg, gulerod, selleri og porre i olie 10 minutter. Hvidløg og tomatpuré 1 minut.
  - Tomater, bouillon og parmesanskorpe i. Simre 15 minutter.
  - Bønner, pasta og kål i. Kog til pastaen er al dente, 8–10 minutter.
  - Fjern skorpen. Smag til. Server med frisk urt og et skvæt olivenolie.
faq:
  - question: Pastaen suger al væske?
    answer: Kog pastaen separat, hvis du laver en stor portion til flere dage. Ellers tilsæt bouillon ved opvarmning.
  - question: Uden pasta?
    answer: Brug ekstra bønner eller en håndfuld ris.
  - question: Kød i?
    answer: Lidt pancetta svitset med løgene giver dybde uden at stjæle retten.
  - question: Kan den fryses?
    answer: Bedst uden pasta. Frys grundsuppen, og kog pasta i ved servering.
body: |
  Vinter-minestrone er italiensk hverdagssuppe med grove grøntsager og pasta.

  Svitset bund. Tomat. Bønner.

  Parmesanskorpen er det lille snydetrick.
tip: Tilsæt pastaen til sidst, så den ikke bliver udkogt, mens resten simrer.
=====
title: Klassisk hønsekødssuppe fra bunden
slug: klassisk-hoensekoedssuppe-fra-bunden
category: gryde
description: Hønsekødssuppe kogt fra bunden på suppehøne — med gulerødder, porrer, kødboller og melboller.
prepTime: PT40M
cookTime: PT2H30M
totalTime: PT3H10M
servings: 8
difficulty: mellem
tags:
  - hønsekødssuppe
  - suppehøne
  - kødboller
  - melboller
  - dansk
  - vinter
  - suppe
  - gryde
imageAlt: Klar hønsekødssuppe med gulerødder, porrer, kød- og melboller
featured: true
ingredients:
  - 1 suppehøne (ca. 1,5–2 kg)
  - 3 liter vand
  - 2 løg, 3 gulerødder, 2 porrer, ¼ knoldselleri
  - 2 laurbærblade, 8 peberkorn, 1 bundt urter (persille, timian)
  - Salt
  - Kødboller: 300 g hakket kalv/svin, 1 æg, 2 spsk rasp, salt, peber
  - Melboller: 50 g smør, 1 dl vand, 1 dl hvedemel, 2 æg, salt
steps:
  - Læg hønen i koldt vand med løg, selleri, laurbær, peberkorn og urter. Bring langsomt i kog, skum af. Simre 2 timer.
  - Tag hønen op. Si bouillonen. Tilsæt gulerødder og porrer i skiver. Simre 15 minutter.
  - Form kødboller. Kog dem i bouillonen 8–10 minutter.
  - Melboller: kog vand og smør op, rør mel i til en bold. Køl lidt, rør æg i. Form små boller, kog 3–5 minutter til de letter.
  - Pille kød af hønen, læg tilbage. Smag til. Server med masser af fyld.
faq:
  - question: Almindelig kylling i stedet?
    answer: Ja, men suppehøne giver dybere smag. Forlæng kogetiden på en almindelig kylling mindre.
  - question: Klar bouillon?
    answer: Start i koldt vand, skum af, og lad den ikke koge voldsomt.
  - question: Kan bouillonen fryses?
    answer: Ja. Frys uden boller, og lav friske boller ved servering.
  - question: Melboller falder fra hinanden?
    answer: Dejen skal være fast, og vandet skal simre — ikke rulle i kog.
body: |
  Klassisk hønsekødssuppe fra bunden er en hel eftermiddag — og det er meningen.

  Skum af. Si. Fyld i.

  Kød- og melboller gør den til middag, ikke bare forret.
tip: Lav ekstra bouillon, og frys den i bakker — næste vintersuppe er halvvejs færdig.
=====
title: Porretærte med bacon
slug: porretaerte-bacon
category: ovn
description: Sprød tærtebund med æggemasse, milde porrer og saltet bacon — perfekt til en kold vinteraften.
prepTime: PT25M
cookTime: PT40M
totalTime: PT1H5M
servings: 6
difficulty: nem
tags:
  - porretærte
  - bacon
  - tærte
  - æg
  - porrer
  - vinter
  - ovn
imageAlt: Gylden porretærte med bacon i skiver på tallerken
featured: true
ingredients:
  - 1 rullet tærtedej (eller hjemmelavet mørdej til 28 cm form)
  - 3 porrer (hvidt og lysegrønt), i skiver
  - 150 g bacon i tern
  - 1 spsk smør
  - 3 æg
  - 2 dl piskefløde
  - 1 dl mælk
  - 100 g revet ost (fx cheddar eller væsterhav)
  - Salt, peber, muskatnød
steps:
  - Forbag dejen i en tærteform ved 200 °C i 10 minutter med bagevægt eller prikket bund.
  - Steg bacon sprødt. Tag op. Svits porrer i smør og lidt baconfedt 8–10 minutter uden farve.
  - Pisk æg, fløde, mælk, salt, peber og muskat.
  - Fordel porrer, bacon og ost i bunden. Hæld æggemassen over.
  - Bag ved 180 °C i 30–35 minutter, til midten er sat og toppen gylden. Hvile 5 minutter.
faq:
  - question: Blød bund?
    answer: Forbag altid. Prikkes bunden, og brug bønner eller tærtevægt.
  - question: Uden bacon?
    answer: Brug feta eller soltørrede tomater. Eller røget ost for saltet dybde.
  - question: Kan den spises kold?
    answer: Ja — fin til frokost dagen efter.
  - question: Madlavningsfløde?
    answer: Den sætter sig mindre elegant. Piskefløde giver den klassiske custard.
body: |
  Porretærte med bacon er vinteraften i en form: mild porre, salt bacon, æggemasse.

  Forbag bunden. Svits porrerne bløde.

  Den er god varm — og næsten bedre kold næste dag.
tip: Lad tærten hvile før udskæring, ellers løber midten ud på første stykke.
=====
title: Flødekartofler med muskatnød
slug: floedekartofler-muskatnoed
category: ovn
description: Tunge, cremede flødekartofler med muskatnød — vinter- og festklassikeren til frikadeller, steg og søndagsmad.
prepTime: PT20M
cookTime: PT1H
totalTime: PT1H20M
servings: 6
difficulty: nem
tags:
  - flødekartofler
  - muskatnød
  - tilbehør
  - festmad
  - kartofler
  - vinter
  - ovn
imageAlt: Gratinerede flødekartofler med gylden top og muskatnød
featured: true
ingredients:
  - 1,2 kg kartofler, skrællet og tyndt skivede
  - 4 dl piskefløde
  - 1 dl mælk
  - 2 fed hvidløg, knuste
  - 1 tsk friskrevet muskatnød
  - 1 tsk salt
  - Friskkværnet peber
  - 1 spsk smør til formen
  - 50 g revet ost (valgfrit)
steps:
  - Varm ovnen til 180 °C. Smør et ovnfast fad.
  - Bland fløde, mælk, hvidløg, muskat, salt og peber.
  - Læg kartoffelskiverne i lag, og hæld flødeblandingen over, så den næsten dækker.
  - Fordel ost ovenpå hvis du vil. Bag 55–65 minutter, til kartoflerne er møre og toppen gylden.
  - Hvile 10 minutter før servering, så saucen sætter sig.
faq:
  - question: Rå midte?
    answer: Skær kartoflerne tynde (mandolin hjælper), og giv dem ekstra 10 minutter under folie hvis toppen er færdig før midten.
  - question: Kan de laves i forvejen?
    answer: Ja. Bag næsten færdigt, køl, og gratinér 15 minutter før servering.
  - question: Uden ost?
    answer: Klassisk. Osten er ekstra — muskat og fløde bærer smagen.
  - question: Madlavningsfløde?
    answer: Den spalter lettere. Piskefløde er mere stabil her.
body: |
  Flødekartofler med muskatnød er det tunge tilbehør, der stjæler tallerkenen.

  Tynde skiver. Fløde til randen. Muskat.

  Ti minutters hvile — så skærer de rent.
tip: Gnid fadet med hvidløg, før du smører det — ekstra duft uden stykker i saucen.
=====
title: Grønlangkål
slug: groenlangkaal
category: gryde
description: Stuvet grønkål på fløde — vendsysselsk/sønderjysk klassiker til hamburgerryg, medister eller kålpølser.
prepTime: PT20M
cookTime: PT30M
totalTime: PT50M
servings: 4
difficulty: nem
tags:
  - grønlangkål
  - grønkål
  - stuvning
  - fløde
  - sønderjysk
  - vendsyssel
  - vinter
  - gryde
imageAlt: Cremet stuvet grønlangkål i gryde klar til servering
featured: true
ingredients:
  - 500 g grønkål, stilke fjernet, finthakket
  - 1 lille løg, hakket
  - 30 g smør
  - 2 spsk hvedemel
  - 3 dl hønsebouillon eller mælk
  - 2 dl piskefløde
  - 1 tsk sukker
  - Salt, peber, muskatnød
steps:
  - Blanchér grønkålen 3–5 minutter i saltet vand. Hæld fra, og pres overskydende væske ud.
  - Svits løg i smør 3 minutter. Rør mel i. Tilsæt bouillon under piskning.
  - Rør fløde, sukker, salt, peber og muskat i. Læg grønkålen i.
  - Simre 15–20 minutter under omrøring, til den er cremet og dufter færdig.
  - Server til hamburgerryg, medister, kålpølser eller kogte kartofler.
faq:
  - question: Vendsyssel eller Sønderjylland?
    answer: Begge traditioner findes. Nogle bruger mere fløde, andre mere bouillon — justér til den konsistens, du kan lide.
  - question: Frossen grønkål?
    answer: Ja. Tø, og pres væsken godt ud før den kommer i saucen.
  - question: For bitter?
    answer: Blanchér lidt længere, og tilsæt en knivspids sukker. Unge blade er mildere.
  - question: Dagen før?
    answer: Ja. Den tykner — fortynd med fløde eller bouillon ved opvarmning.
body: |
  Grønlangkål er stuvet grønkål — tæt på mormor, tæt på julefrokostbordet.

  Blanchér. Opbag. Simre.

  Den hører til ved siden af saltet kød.
tip: Pres grønkålen tør efter blanchering — ellers bliver stuvningen vandig.
=====
title: Bagt Mont d'Or
slug: bagt-mont-d-or
category: ovn
description: Hel fransk Mont d'Or bagt i trææsken med hvidløg og hvidvin — klar til at dyppe sprødt brød i.
prepTime: PT10M
cookTime: PT25M
totalTime: PT35M
servings: 4
difficulty: nem
tags:
  - mont d'or
  - bagt ost
  - ost
  - hvidvin
  - aperitif
  - vinter
  - ovn
imageAlt: Bagt Mont d'Or i trææske med hvidløg og brød til at dyppe
featured: true
ingredients:
  - 1 Mont d'Or (ca. 500–750 g) i trææske
  - 1–2 fed hvidløg, i tynde skiver
  - ½ dl tør hvidvin
  - Friskkværnet peber
  - Frisk rosmarin eller timian (valgfrit)
  - Sprødt brød, kartofler eller spegeskinke til servering
steps:
  - Varm ovnen til 180 °C. Tag låget af æsken, og stil osten på en bradepande (gerne på et stykke folie).
  - Riv et kryds i skorpen. Stik hvidløgsskiver ned. Hæld vin over. Peber og evt. urter.
  - Bag 20–25 minutter, til osten er boblende midt i.
  - Server straks med brød, ovnkartofler eller spegepålæg til at dyppe.
faq:
  - question: Kan jeg bruge Vacherin eller Camembert?
    answer: Camembert virker som erstatning. Ægte Mont d'Or har sæson og trææske — det er halvdelen af oplevelsen.
  - question: Æsken brænder?
    answer: Den er lavet til ovnen, men sæt den på folie eller et fad. Fjern plastik hvis der er nogen under osten.
  - question: Uden vin?
    answer: Brug en skvæt mælk eller bare hvidløg og peber.
  - question: Til hvor mange?
    answer: En 500 g ost er forret eller aperitif til 3–4, eller hovedret til 2 sultne.
body: |
  Bagt Mont d'Or er vinterens mest direkte ostelykke: varm, flydende, klar til brød.

  Hvidløg i. Vin over. Ovnen på.

  Der er ingen opskrift, der er mere sig selv.
tip: Tag osten ud, når midten blødt bugter — overbagt Mont d'Or bliver fedtet og skiller.
=====
title: Luftig citronfromage
slug: luftig-citronfromage
category: pande
description: Frisk, syrlig og luftig mormor-citronfromage — det lette punktum efter vinterens tunge mad.
prepTime: PT25M
cookTime: PT10M
totalTime: PT4H35M
servings: 6
difficulty: mellem
tags:
  - citronfromage
  - fromage
  - citron
  - dessert
  - mormormad
  - vinter
  - pande
imageAlt: Portioner af luftig citronfromage med citronskal ovenpå
featured: true
ingredients:
  - 4 æg, adskilt
  - 100 g sukker
  - Saft og skal af 2 citroner
  - 4 ark husblas
  - 3 dl piskefløde
  - Evt. bær eller ekstra citronskal til pynt
steps:
  - Læg husblas i koldt vand 5–10 minutter.
  - Pisk æggeblommer og sukker lyse. Rør citronsaft og skal i.
  - Smelt den opvredne husblas i et lille bad eller meget lav varme. Rør den i æggeblandingen.
  - Pisk fløde til blødt skum. Pisk æggehvider stive. Fold fløde og hvider forsigtigt i citronmassen.
  - Hæld i glas eller form. Køl mindst 4 timer. Pynt før servering.
faq:
  - question: Grumset fromage?
    answer: Husblasen må ikke koges, og den skal røres godt ud, før fløden foldes i.
  - question: Uden husblas?
    answer: Den sætter sig ikke på klassisk vis. Brug et vegetabilsk alternativ efter pakkens anvisning.
  - question: For syrlig?
    answer: Mere sukker, eller kun saft fra 1½ citron. Skallen giver også skarphed.
  - question: Kan den laves dagen før?
    answer: Ja — den er bedst efter en nat i køleskabet.
body: |
  Luftig citronfromage er syre og fløde i balance.

  Den er ikke tung. Den er punktummet.

  Efter flæskesteg og flødekartofler er den den rigtige dessert.
tip: Fold æggehviderne i til sidst med en dejskraber — piskning flader luften ud af fromagen.
=====
title: Varme vafler med syltetøj og flødeskum
slug: varme-vafler-syltetoej
category: pande
description: Hyggelige varme vafler med syltetøj og flødeskum — den klassiske eftermiddagsspise, når mørket falder på.
prepTime: PT15M
cookTime: PT25M
totalTime: PT40M
servings: 4
difficulty: nem
tags:
  - vafler
  - syltetøj
  - flødeskum
  - eftermiddag
  - hygge
  - dessert
  - vinter
  - pande
imageAlt: Stabel varme vafler med jordbærsyltetøj og flødeskum
featured: true
ingredients:
  - 3 æg
  - 3 spsk sukker
  - 4 dl kærnemælk eller sødmælk
  - 75 g smeltet smør
  - 3 dl hvedemel
  - 1 tsk bagepulver
  - 1 knivspids salt
  - 1 tsk vaniljesukker
  - Smør til vaffeljernet
  - Syltetøj og 2 dl piskefløde til servering
steps:
  - Pisk æg og sukker let. Rør mælk og smeltet smør i.
  - Sigt mel, bagepulver, salt og vanilje i. Rør til en glat dej. Hvil 10 minutter.
  - Varm vaffeljernet. Pensl med smør. Bag vaflerne gyldne.
  - Pisk fløde til blødt skum.
  - Server vaflerne varme med syltetøj og flødeskum.
faq:
  - question: Uden vaffeljern?
    answer: Bag dem som tykke pandekager på panden — ikke samme rudemønster, men samme hygge.
  - question: Dejen for tyk?
    answer: Tilsæt en skvæt mælk. Den skal kunne hældes, men ikke være vandtynd.
  - question: Kan dejen stå?
    answer: Ja en time i køleskab. Rør igennem før bagning.
  - question: Saltede vafler?
    answer: Drop sukker og vanilje, tilsæt ost eller krydderurter — anden ret, samme jern.
body: |
  Varme vafler med syltetøj og flødeskum er klokken-fire-mad i vintermørket.

  Dej. Jern. Damp.

  Der er ingen grund til at komplicere det.
tip: Hold færdige vafler varme i ovnen ved 80 °C på en rist — så bliver de ikke bløde i stakken.
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
