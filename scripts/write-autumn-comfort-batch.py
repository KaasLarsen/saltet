#!/usr/bin/env python3
"""Efterårs-comfort batch — dybe gryder, supper og salte grødklassikere (aug 2026)."""
from pathlib import Path

ROOT = Path("/Users/dklarsen/Desktop/saltet/content/recipes")
PUBLISHED = "2026-08-27"

RECIPES = r'''
=====
title: Gammeldags jægergryde
slug: gammeldags-jaegergryde
category: gryde
description: Gammeldags jægergryde med svinemørbrad, svampe, pølsestykker og rødvin — efterårsklassikeren fra støbejernsgryden.
prepTime: PT25M
cookTime: PT45M
totalTime: PT1H10M
servings: 4
difficulty: mellem
tags:
  - jægergryde
  - gammeldags jægergryde
  - svinemørbrad
  - svampe
  - rødvin
  - gryderet
  - efterår
  - gryde
imageAlt: Gammeldags jægergryde med svinemørbrad, svampe og pølsestykker
featured: true
ingredients:
  - 700 g svinemørbrad, skåret i skrå skiver
  - 150 g bacon i tern
  - 300 g blandede svampe (champignon, østershatte, evt. kantareller)
  - 3–4 pølser (fx medister eller wiener), skåret i skrå skiver
  - 2 løg, hakket
  - 2 fed hvidløg
  - 2 spsk smør + 1 spsk olie
  - 2 spsk hvedemel
  - 2 dl tør rødvin
  - 3 dl okse- eller honsebouillon
  - 2 dl piskefløde
  - 1 spsk tomatpuré
  - 1 tsk timian, 1 laurbærblad
  - Salt, peber, persille
steps:
  - Brun bacon i en tung gryde, til det er sprødt. Tag op. Brun pølsestykkerne i fedtet, og tag dem op.
  - Vend mørbrad i salt og peber. Brun hurtigt i smør og olie i portioner — farve, ikke gennemstegning. Tag op.
  - Svits løg 5 minutter. Svampe i, til væsken er kogt væk. Hvidløg og tomatpuré 1 minut.
  - Drys mel over, rør 30 sekunder. Hæld rødvin i, skrab bunden, og lad koge 2 minutter. Bouillon, timian og laurbær i.
  - Læg kød, bacon og pølser tilbage. Simre 15–20 minutter under låg, til mørbraden er netop færdig.
  - Rør fløde i. Smag til. Persille. Server med kartoffelmos eller kogte kartofler.
faq:
  - question: Forskel på mørbradgryde?
    answer: Mørbradgryde er cremet og mild. Jægergryde har rødvin, mere svampe og den klassiske jagt-smag.
  - question: Kan jeg bruge vildt?
    answer: Ja — rådyr eller krondyr i tern. Forlæng simretiden, til kødet er mørt. Se også efterårs-vildtgryde.
  - question: Hvilken vin?
    answer: Tør, mellemfyldig rødvin — pinot noir eller en billig bordeaux. Undgå sød vin.
  - question: Bliver mørbraden tør?
    answer: Brun kort, og simre kun til den er gennemstegt. Overkogt mørbrad er tyggegummi.
body: |
  Gammeldags jægergryde er efterår i grydeform: mørbrad, masser af svampe, pølsestykker og et skud rødvin.

  Baconfedtet er smagen. Vinen koger ind. Fløden lukker.

  Det er ikke fin dining. Det er mormor med jagtstøvler.
tip: Svampene skal miste væske, før melet kommer i — ellers bliver saucen vandig og grå.
=====
title: Efterårs-vildtgryde
slug: efteraars-vildtgryde
category: stobejern
description: Efterårs-vildtgryde med krondyr eller rådyr i tung flødesovs — enebær, kantareller og Dutch Oven-simremad.
prepTime: PT30M
cookTime: PT2H30M
totalTime: PT3H
servings: 6
difficulty: mellem
tags:
  - vildtgryde
  - efterårs-vildtgryde
  - rådyr
  - krondyr
  - kantareller
  - enebær
  - flødesovs
  - efterår
  - støbejern
imageAlt: Vildtgryde med rådyr, kantareller og flødesovs i støbejernsgryde
featured: true
ingredients:
  - 1,2 kg rådyr- eller krondyrkød til gryderet, i 3 cm tern
  - 100 g bacon i tern
  - 2 spsk smør + 1 spsk olie
  - 2 løg, 2 gulerødder, 2 stilke bladselleri — hakket
  - 300 g kantareller (eller blandede vilde svampe)
  - 2 spsk tomatpuré
  - 3 dl tør rødvin
  - 4 dl vildt- eller oksebouillon
  - 8 knuste enebær
  - 2 laurbærblade, 4 kviste timian
  - 2 dl piskefløde
  - 1 spsk ribsgele eller tyttebærgele
  - Salt og peber
steps:
  - Tænd ovnen på 160 °C. Brun bacon i Dutch Oven. Tag op. Brun vildtkødet hårdt i portioner i smør og olie. Tag op.
  - Svits løg, gulerod og selleri 8 minutter. Kantareller i, til de mister væske. Tomatpuré 1 minut.
  - Vin i. Skrab bunden. Kog 3 minutter. Bouillon, enebær, laurbær, timian. Kød og bacon tilbage.
  - Låg på. I ovnen 2–2½ time, til kødet er smørmørt.
  - Tag op på komfur. Fløde og gele i. Simre 5 minutter uden låg. Smag til. Server med kartoffelmos eller rodfrugtmos.
faq:
  - question: Kan jeg bruge oksekød?
    answer: Ja — højreb eller grydestykker. Det er ikke vildt mere, men teknikken er den samme.
  - question: For meget enebær?
    answer: Otte knuste er nok. Flere gør det medicinsk. Start mildt.
  - question: Frosne kantareller?
    answer: Ja. Svits dem tørre, til vandet er væk, før resten kommer i.
  - question: Bål-versionen?
    answer: Se vildtgryde over bål — samme stemning, åben ild.
body: |
  Efterårs-vildtgryde er skoven på tallerkenen: mørkt kød, enebær, kantareller og en flødesovs, der bærer.

  Brun hårdt. Simre lavt. Gele til sidst — ikke før.

  Det er den ret, man laver, når jagtsæsonen åbner, og køleskabet lugter af skov.
tip: Kernetemperatur er irrelevant her. Stik en gaffel i — når kødet falder fra hinanden, er det færdigt.
=====
title: Klassiske gule ærter
slug: gule-aerter
category: gryde
description: Klassiske gule ærter med sprængt flæsk, pølser og sennep — den ultimative mormor-efterårsret fra gryden.
prepTime: PT20M
cookTime: PT2H
totalTime: PT2H20M
servings: 6
difficulty: mellem
tags:
  - gule ærter
  - gule ærter opskrift
  - flækærter
  - sprængt flæsk
  - mormormad
  - efterår
  - gryde
imageAlt: Gule ærter med sprængt flæsk, pølser og sennep
featured: true
ingredients:
  - 500 g gule flækærter, skyllede
  - 800 g sprængt flæsk eller saltet svinekød
  - 2–3 røgede pølser eller medister
  - 2 løg, 2 gulerødder, 1 porre — i grove stykker
  - ½ knoldselleri i tern
  - 2 laurbærblade, 8 peberkorn
  - Ca. 2 l vand
  - Salt (forsigtigt — flæsket er salt)
  - Stærk sennep og rugbrød til servering
steps:
  - Læg ærterne i en stor gryde med vand, så de er dækket med 5 cm. Bring i kog, skum, og skru ned.
  - Læg sprængt flæsk i. Tilsæt løg, gulerod, porre, selleri, laurbær og peberkorn. Simre 1½–2 timer under låg.
  - Rør jævnligt i bunden, så ærterne ikke brænder på. De skal koge ud til en tyk, cremet masse.
  - Tilsæt pølserne de sidste 20–30 minutter, så de varmer igennem uden at sprække.
  - Tag flæsk og pølser op. Smag ærterne til — ofte behøver de ikke mere salt. Server med skåret flæsk, pølseskiver, sennep og rugbrød.
faq:
  - question: Skal ærterne udblødes?
    answer: Flækærter behøver det ikke. Hele gule ærter skal gerne ligge i blød natten over.
  - question: For salt?
    answer: Brug mindre saltet kød, eller kog flæsket 20 minutter for sig, og skift vandet, før ærterne kommer i.
  - question: Trykkoger?
    answer: Se gule ærter i trykkoger — samme smag, kortere tid.
  - question: Tilbehør?
    answer: Sennep er ikke valgfrit. Syltede rødbeder og rugbrød hører til.
body: |
  Gule ærter er dansk efterår uden filter: flækærter, saltkød, pølser og så meget sennep, at næsen løber.

  Ærterne skal koge ud. Ikke al dente. Ikke fine. Ud.

  Det er den ret, man spiser, når kulden sætter ind, og man ikke gider pynte tallerkenen.
tip: Rør i bunden hvert kvarter. Brændte ærter smager af røg — og ikke på den gode måde.
=====
title: Klassisk fransk løgsuppe
slug: fransk-loegsuppe
category: gryde
description: Klassisk fransk løgsuppe med ostegratineret brød — karamelliserede løg, kraftig bouillon og tykt lag smeltet gruyère.
prepTime: PT25M
cookTime: PT1H30M
totalTime: PT1H55M
servings: 4
difficulty: mellem
tags:
  - fransk løgsuppe
  - løgsuppe
  - gruyère
  - ostegratineret
  - suppe
  - efterår
  - gryde
imageAlt: Fransk løgsuppe med ostegratineret brød og smeltet gruyère
featured: true
ingredients:
  - 1,2 kg gule løg, tyndt skåret
  - 50 g smør
  - 1 spsk olie
  - 2 fed hvidløg, finthakket
  - 2 dl tør hvidvin (eller tør sherry)
  - 1,5 l kraftig oksebouillon
  - 2 kviste timian, 1 laurbærblad
  - Salt og peber
  - 4 skiver daggammelt brød (fx baguette)
  - 200 g gruyère, groft revet
steps:
  - Smelt smør og olie i en tung gryde. Løg i. Karamelliser 40–50 minutter på middel-lav varme under hyppig omrøring, til de er dybt gyldenbrune.
  - Hvidløg 1 minut. Vin i. Skrab bunden, og lad koge ind 3–4 minutter.
  - Bouillon, timian og laurbær i. Simre 30–40 minutter. Smag til med salt og peber.
  - Rist brødet. Fordel suppe i ovnfaste skåle. Læg brød ovenpå, og dæk med et tykt lag gruyère.
  - Grill i ovnen 3–5 minutter, til osten bobler og får brune pletter. Server straks.
faq:
  - question: Kan jeg bruge cheddar?
    answer: Nej. Gruyère eller emmental. Cheddar giver forkert smag og fedtfilm.
  - question: Blonde løg?
    answer: Så får du løgvand. Farven skal være dyb brun — det er hele pointen.
  - question: Version med øl og marv?
    answer: Se fransk løgsuppe på mørkt øl og oksemarv — tungere og mere nørdet.
  - question: Vegetarisk?
    answer: Brug kraftig grøntsagsbouillon og mere smør. Ost og karamellisering bærer stadig.
body: |
  Klassisk fransk løgsuppe er tålmodighed: løgene skal brunes, til de næsten tager skade, før bouillonen kommer i.

  Osten er ikke pynt. Den er et låg.

  Det er den salte, boblende skål, man bestiller på bistro — og laver bedre derhjemme.
tip: Salt løgene sent. Tidligt salt trækker vand og bremser karamelliseringen.
=====
title: Cremet græskarsuppe med bacon
slug: cremet-graeskarsuppe-bacon
category: gryde
description: Cremet græskarsuppe med sprød bacon — efterårets mest søgte suppe, piftet op med chili og saltet baconknas.
prepTime: PT20M
cookTime: PT35M
totalTime: PT55M
servings: 4
difficulty: nem
tags:
  - græskarsuppe
  - cremet græskarsuppe
  - græskar
  - bacon
  - efterårssuppe
  - efterår
  - gryde
imageAlt: Cremet græskarsuppe med sprøde bacontern og chiliolie
featured: true
ingredients:
  - 1 kg hokkaido eller butternut, skrællet og i tern (hokkaido kan beholde skræl)
  - 150 g bacon i tern
  - 1 stort løg, hakket
  - 2 fed hvidløg
  - 1 tsk friskrevet ingefær (valgfrit)
  - ½–1 tsk chiliflager eller en knivspids cayenne
  - 8 dl grøntsags- eller honsebouillon
  - 1 dl piskefløde
  - 1 spsk smør (hvis baconet er magert)
  - Salt, peber, evt. lidt citronsaft
  - Græskarkerner til top (valgfrit)
steps:
  - Steg bacon i gryden, til det er knasende. Tag op på køkkenrulle. Gem 1–2 spsk baconfedt.
  - Svits løg i fedtet 5–7 minutter. Hvidløg, ingefær og chili 1 minut.
  - Græskar og bouillon i. Bring i kog, skru ned, og simre 20–25 minutter, til græskaret er blødt.
  - Blend glat. Rør fløde i. Smag til med salt, peber og en dråbe citron, hvis den er for sød.
  - Server med bacontern, evt. græskarkerner og et drys chili.
faq:
  - question: Hvilket græskar?
    answer: Hokkaido er sød og behøver ikke skræl. Butternut er cremet. Græskar til lanterner er ofte vandede.
  - question: Uden fløde?
    answer: Ja — blend med en klat creme fraiche eller kokosmælk. Eller bare bouillon.
  - question: Trykkoger?
    answer: Se græskarsuppe i trykkoger — hurtigere, uden bacon-fokus.
  - question: Kan den fryses?
    answer: Ja uden fløde og bacon. Tilsæt dem efter optøning.
body: |
  Cremet græskarsuppe med bacon er efterårets google-hit: sød græskar, chili og saltet knas ovenpå.

  Baconfedtet steger løgene. Fløden lukker. Chilien skærer det søde.

  Det er den suppe, der får folk til at tro, du har brugt timer — du har brugt en gryde.
tip: Gem baconternene til toppen. Blandes de i, mister du kontrasten mellem cremet og knasende.
=====
title: Byggrød med vesterhavsost og svampe
slug: byggoed-vesterhavsost-svampe
category: gryde
description: Gammeldags byggrød — nordisk efterårs-risotto på perlebyg, vendt med vesterhavsost og svampe.
prepTime: PT15M
cookTime: PT45M
totalTime: PT1H
servings: 4
difficulty: nem
tags:
  - byggrød
  - byg-otto
  - perlebyg
  - vesterhavsost
  - svampe
  - grød
  - efterår
  - gryde
imageAlt: Cremét byggrød med svampe og revet vesterhavsost
featured: true
ingredients:
  - 3 dl perlebyg, skyllet
  - 1 liter honse- eller grøntsagsbouillon, lun
  - 200 g blandede svampe, skåret
  - 1 skalotteløg eller 1 lille løg, finthakket
  - 1 fed hvidløg
  - 2 spsk smør + 1 spsk olie
  - 1 dl tør hvidvin (valgfrit)
  - 80 g vesterhavsost eller anden fast, saltet ost, revet
  - 2 spsk creme fraiche eller fløde
  - Salt, peber, persille eller timian
steps:
  - Svits svampe i 1 spsk smør og olie, til de er gyldne og væsken er væk. Krydr, og tag op.
  - Svits løg i resten af smørret 3 minutter. Perlebyg i, og rist 2 minutter under omrøring.
  - Vin i (hvis du bruger det), og lad suge. Tilsæt bouillon en øse ad gangen under omrøring, som risotto — ca. 35–40 minutter, til byggen er mør men stadig har bid.
  - Rør ost, creme fraiche og de fleste svampe i. Smag til. Den skal være cremet, ikke stiv.
  - Server med resten af svampene ovenpå og friske urter.
faq:
  - question: Kan jeg bruge perlebyg fra dagen før?
    answer: Ja — varm med ekstra bouillon, og rør ost i til sidst. Den suger mere overnight.
  - question: Anden ost?
    answer: Parmesan, væsterhavsost, dansk grydeost eller en saltet gedeost. Den skal smelte og smage.
  - question: Hurtigere?
    answer: Udblød byggen 1 time. Eller brug trykkoger til byggen, og finish på komfur med ost.
  - question: Til hvad?
    answer: Hovedret med salat, eller tilbehør til stegt kylling og vildt.
body: |
  Byggrød er den nordiske risotto, ingen snakker nok om: perlebyg, svampe og en saltet ost, der smelter ind.

  Byggen skal have bid. Osten skal gøre den blank. Svampene skal have stegeskorpe.

  Det er grød til dem, der synes risengrød er for sødt til aftensmad.
tip: Brug lun bouillon. Kold væske stopper kogningen og giver klæbrig, ujævn grød.
=====
title: Klassisk risengrød
slug: klassisk-risengrod
category: gryde
description: Klassisk risengrød med smørklat — guiden til cremet grød uden at brænde bunden. Søges massivt fra oktober.
prepTime: PT5M
cookTime: PT50M
totalTime: PT55M
servings: 4
difficulty: nem
tags:
  - risengrød
  - klassisk risengrød
  - grød
  - smørklat
  - jul
  - efterår
  - gryde
imageAlt: Klassisk risengrød med smørklat og kanelsukker
featured: true
ingredients:
  - 2 dl grødris (rundkornet)
  - 2 dl vand
  - 1 liter sødmælk (eller 8 dl mælk + 2 dl fløde)
  - 1 tsk salt
  - 1 vaniljestang eller 1 tsk vaniljesukker
  - Smørklat, kanelsukker og evt. saft til servering
steps:
  - Bring ris og vand i kog i en tung gryde under omrøring. Lad koge, til vandet er suget op — ca. 2–3 minutter.
  - Hæld mælken i lidt ad gangen under omrøring. Tilsæt salt og vanilje.
  - Skru helt ned. Simre 40–50 minutter under låg, og rør grundigt i bunden hvert 5.–7. minut.
  - Grøden er færdig, når risene er møre, og den er cremet — ikke stiv. Den tykner mere ved henstand.
  - Server med en stor smørklat og kanelsukker. Saft ved siden af.
faq:
  - question: Hvordan undgår jeg brændt bund?
    answer: Tung gryde, lav varme, og rør i bunden ofte. Bruger du induktion, er en diffusor eller støbejern din ven.
  - question: Kan den laves i trykkoger?
    answer: Ja — se risengrød i trykkoger. Mindre risiko for brændt bund.
  - question: For tyk?
    answer: Rør mere mælk i. For tynd: simre uden låg 5 minutter mere.
  - question: Dagen efter?
    answer: Den stivner. Varm med mælk under omrøring, eller lav risengrødsklatten.
body: |
  Klassisk risengrød er oktober-søgningerne i en gryde: ris, mælk, salt — og tålmodighed, så bunden ikke bliver sort.

  Start med vand. Så mælk. Rør i bunden, som om din ære afhænger af det.

  Smørklatten er ikke valgfri. Den er kontrakten.
tip: En knivspids salt i mælkegrød er forskellen på «sød grød» og «rigtig risengrød».
=====
title: Saltet havregrød med spejlæg og bacon
slug: saltet-havregroed-spejlaeg-bacon
category: gryde
description: Saltet havregrød med spejlæg og bacon — moderne, umami-morgenmad eller frokostgrød til kolde dage.
prepTime: PT10M
cookTime: PT20M
totalTime: PT30M
servings: 2
difficulty: nem
tags:
  - saltet havregrød
  - havregrød
  - spejlæg
  - bacon
  - morgenmad
  - umami
  - efterår
  - gryde
imageAlt: Saltet havregrød toppet med spejlæg og sprød bacon
featured: true
ingredients:
  - 2 dl havregryn (grove eller fine)
  - 4 dl vand eller en blanding af vand og mælk
  - 1 dl honsebouillon eller ½ bouillonterning
  - 1 spsk smør
  - Salt og peber
  - 100 g bacon i skiver eller tern
  - 2 æg
  - Evt. forårsløg, chiliolie eller parmesan
steps:
  - Steg bacon sprødt. Tag op. Gem 1 tsk baconfedt.
  - Bring vand/mælk og bouillon i kog. Rør gryn i. Simre 8–12 minutter under omrøring, til grøden er cremet.
  - Rør smør og lidt baconfedt i. Smag til med salt og peber — den skal være tydeligt salt, ikke dessert.
  - Spejlæg i resten af baconfedtet: hviden stiv, blommen blød.
  - Fordel grød i skåle. Top med spejlæg, bacon og evt. forårsløg eller chiliolie.
faq:
  - question: Er det ikke bare grød med topping?
    answer: Bouillon og baconfedt i selve grøden gør den til en salt ret — ikke sød morgengrød med æg ovenpå.
  - question: Protein?
    answer: Æg + bacon + havre. Vil du have mere: rør hytteost eller skyr i af varmen.
  - question: Fine eller grove gryn?
    answer: Grove giver mere bid. Fine bliver cremede hurtigere.
  - question: Kan den laves dagen før?
    answer: Ja. Varm med ekstra væske. Spejlæg og bacon frisk.
body: |
  Saltet havregrød er det modsatte af kanelsukker: bouillon, baconfedt, spejlæg og umami.

  Grøden skal smage af noget i sig selv. Toppingen er belønningen.

  Det er frokostgrød til folk, der er færdige med sød morgenmad i november.
tip: En skvis soyasauce eller lidt parmesan i grøden forstærker saltet uden at gøre den «asiatisk», hvis du holder dig til en teskefuld.
=====
title: Gammeldags svineben i skysovs
slug: svineben-skysovs
category: gryde
description: Gammeldags svineben i skysovs — billig efterårsmad, hvor kødet falder af benene, serveret med masser af brun sovs.
prepTime: PT20M
cookTime: PT2H30M
totalTime: PT2H50M
servings: 4
difficulty: mellem
tags:
  - svineben
  - gammeldags ben
  - skysovs
  - brun sovs
  - mormormad
  - efterår
  - gryde
imageAlt: Møre svineben i brun skysovs med kartofler
featured: true
ingredients:
  - 1,5–2 kg svineben (fx nakkeben eller ribben med kød)
  - 2 spsk olie eller svinefedt
  - 2 løg i både
  - 2 gulerødder i grove stykker
  - 2 spsk tomatpuré
  - 2 spsk hvedemel
  - 8–10 dl honse- eller grøntsagsbouillon
  - 2 laurbærblade, 8 peberkorn, 3 kviste timian
  - Salt og peber
  - Evt. 1 spsk mørk soya eller 1 tsk sukker til farve
steps:
  - Tænd ovnen på 160 °C. Dup benene tørre. Brun dem hårdt i olie i en ovnfast gryde i portioner. Tag op.
  - Svits løg og gulerødder 5 minutter. Tomatpuré 1 minut. Drys mel over, rør 1 minut.
  - Bouillon i under omrøring. Krydderier i. Ben tilbage — væsken skal næsten dække.
  - Låg på. I ovnen 2–2½ time, til kødet slipper benet.
  - Tag benene op. Si saucen, kog den ind, og smag til — det er skysovsen. Server med kogte kartofler og evt. rødkål.
faq:
  - question: Hvilke ben?
    answer: Nakkeben og ribben med kød på. Rene knogler uden kød giver kun bouillon.
  - question: Kan de koges på komfur?
    answer: Ja — svag simre 2–2½ time. Ovnen er mere tilgivende, så bunden ikke brænder.
  - question: For fed sovs?
    answer: Køl saucen, og skim fedtet af. Eller brug en fedtudskiller.
  - question: Tilbehør?
    answer: Kartofler, rødkål, agurkesalat. Sennep på siden.
body: |
  Gammeldags svineben er billig luksus: lang tid, lav varme, og en skysovs, der smager af mere end den kostede.

  Brun først. Simre længe. Si sovsen.

  Når kødet falder af benene, er aftenen i hus.
tip: Brun benene i portioner. Fylder du gryden, damper de i stedet for at få skorpe — og skorpen er smagen i sovsen.
=====
title: Sprængt andebryst med rødkål
slug: spraengt-andebryst-roedkaal
category: ovn
description: Sprængt andebryst med rødkål — saltet, mørt andebryst og tyvstart på julesmagene allerede i november.
prepTime: PT20M
cookTime: PT25M
totalTime: PT24H45M
servings: 4
difficulty: mellem
tags:
  - sprængt andebryst
  - andebryst
  - rødkål
  - saltet and
  - jul
  - november
  - efterår
  - ovn
imageAlt: Lyserødt sprængt andebryst skåret i skiver med rødkål
featured: true
ingredients:
  - 2 andebryster med skind (ca. 250–300 g stykket)
  - 40 g groft salt
  - 1 spsk sukker
  - 1 tsk knust peber
  - 1 tsk eneær, knust (valgfrit)
  - 1 laurbærblad, smuldret
  - 500 g rødkål (færdigsyltet eller hjemmelavet)
  - Evt. ribsgele og brune kartofler til servering
steps:
  - Bland salt, sukker, peber, eneær og laurbær. Gnid ind i andebrysterne. Læg i pose eller skål, og køl 12–24 timer.
  - Skyl overfladen let, og dup knastørt. Score skindet i tæt rudemønster uden at skære i kødet.
  - Læg brysterne skind-ned i kold panden. Tænd middel varme, og steg 8–12 minutter, til skindet er knasende og fedtet er stegt ud. Hæld fedt fra undervejs.
  - Vend brysterne, og steg 2–3 minutter på kødsiden. Afslut i ovn ved 180 °C til kernetemperatur 54–56 °C for rosa.
  - Hvil 8–10 minutter under folie. Skær i skiver på skrå. Server med lun rødkål og evt. ribsgele.
faq:
  - question: Hvorfor sprænge andebryst?
    answer: Saltet gør kødet saftigere og mere mørt — en mild forsmag på juleand uden hele fuglen.
  - question: For salt?
    answer: Skyl godt, og salt maks. 24 timer. Tynde bryster tåler kortere tid.
  - question: Sous vide?
    answer: Ja — se andebryst sous vide til præcis kernetemperatur, og finish skindet på panden.
  - question: Rødkål?
    answer: Færdigsyltet virker. Hjemmelavet med æble og eddike er bedre.
body: |
  Sprængt andebryst er november-snyd: julesmag uden at stege en hel and.

  Salt natten over. Skind i kold pande. Rosa midte.

  Rødkålen er ikke tilbehør — den er kontrakten med sæsonen.
tip: Start skindet i kold pande. Fedtet smelter langsomt ud, og skindet bliver knasende i stedet for svedent.
=====
title: Koteletter i fad med bacon og champignon
slug: koteletter-i-fad-bacon-champignon
category: ovn
description: Koteletter i fad med bacon og svitsede champignon — mormor-klassikeren i cremet paprikasovs fra ovnen.
prepTime: PT20M
cookTime: PT45M
totalTime: PT1H5M
servings: 4
difficulty: nem
tags:
  - koteletter i fad
  - svinekoteletter
  - bacon
  - champignon
  - paprikasovs
  - mormormad
  - efterår
  - ovn
imageAlt: Ovnstegte koteletter i fad med bacon, champignon og paprikasovs
featured: true
ingredients:
  - 4 svinekoteletter (gerne med ben)
  - 120 g bacon i tern
  - 250 g champignoner, skåret
  - 1 løg, hakket
  - 1 rød peberfrugt i strimler (valgfrit)
  - 2 spsk smør
  - 1 spsk paprika
  - 1 spsk hvedemel
  - 2 dl piskefløde
  - 2 dl mælk eller bouillon
  - 1 spsk tomatpuré
  - Salt, peber, persille
steps:
  - Tænd ovnen på 180 °C. Brun bacon i en pande. Tag op. Brun koteletterne 2–3 minutter på hver side i baconfedtet. Læg i et ovnfast fad.
  - Svits løg og champignon i smør 5–7 minutter. Peberfrugt i. Tomatpuré og paprika 30 sekunder på lav varme.
  - Drys mel over, rør. Hæld fløde og mælk i. Kog op til en cremet sauce. Smag til. Rør bacon i.
  - Hæld saucen over koteletterne, så de næsten svømmer.
  - Bag 30–35 minutter, til koteletterne er gennemstegte (ca. 70 °C). Persille. Server med kartoffelmos eller ris.
faq:
  - question: Forskel på versionen med cocktailpølser?
    answer: Den har tomat og cocktailpølser. Her er det bacon, champignon og paprika — den cremede mormor-sovs.
  - question: Tørre koteletter?
    answer: Brun kort, og lad dem færdiggøre i saucen. Magre koteletter uden fedtkant tørrer lettere.
  - question: Kan saucen laves dagen før?
    answer: Ja. Brun koteletterne friske, og hæld lun sauce over før bagning.
  - question: Tilbehør?
    answer: Kartoffelmos, ris eller bagekartofler. Agurkesalat skærer det fede.
body: |
  Koteletter i fad er mormor-logik: brun, overhæld med sauce, ovn — og kødet bliver mørt i stedet for tørt.

  Paprikaen skal kun have sekunder på varmen. Baconet skal knase i saucen.

  Det er den ret, der lugter af søndag, selv om det er tirsdag.
tip: Brug sødmefuld paprika. Røget paprika er en knivspids — ellers smager det af grillpølse, ikke mormor.
=====
title: Braiseret svineskank i mørkt øl
slug: braiseret-svineskank-moerkt-oel
category: gryde
description: Braiseret svineskank i mørkt øl — langtidssimret kød, der bliver smørmørt, mens øllen koger ind til en genial sovs.
prepTime: PT25M
cookTime: PT3H
totalTime: PT3H25M
servings: 4
difficulty: mellem
tags:
  - svineskank
  - braiseret svineskank
  - mørkt øl
  - skysovs
  - gryderet
  - efterår
  - gryde
imageAlt: Braiseret svineskank i mørkt øl med indkogt sovs
featured: true
ingredients:
  - 4 svineskanker (à 400–500 g), gerne med svær
  - 2 spsk olie
  - 2 løg, 2 gulerødder, 2 stilke bladselleri — i grove stykker
  - 2 spsk tomatpuré
  - 1 flaske mørkt øl (33–44 cl stout, porter eller dansk mørkt)
  - 4 dl honse- eller oksebouillon
  - 2 laurbærblade, 6 peberkorn, 3 kviste timian
  - 1 spsk dijonsennep
  - Salt og peber
steps:
  - Tænd ovnen på 160 °C. Score sværen. Salt og peber. Brun skankerne på alle sider i olie i en ovnfast gryde. Tag op.
  - Svits grøntsager 8 minutter. Tomatpuré 1 minut. Øl i, skrab bunden, kog 3 minutter.
  - Bouillon og krydderier i. Skanker tilbage — væsken må ikke dække sværen helt, hvis du vil have den sprødere til sidst.
  - Låg på. Braiser 2½–3 timer, til kødet er smørmørt.
  - Tag skanker op. Si saucen, kog ind, rør sennep i. Evt. 10 minutter ved 220 °C med skankerne svær-opad for knas. Server med kartoffelmos eller sauerkraut.
faq:
  - question: Forskel på Schweinshaxe?
    answer: Schweinshaxe er den tyske, knasende-svær-version. Her er fokus på ølsovsen og det smørmøre kød.
  - question: Hvilket øl?
    answer: Porter eller stout. Undgå bitter IPA — den bliver medicinsk i saucen.
  - question: Kan den laves dagen før?
    answer: Ja. Den smager bedre. Skim fedt af, når den er kold, og varm forsigtigt op.
  - question: Trykkoger?
    answer: Muligt på 45–50 minutter under tryk, men reducér saucen efterfølgende på komfur.
body: |
  Braiseret svineskank i mørkt øl er tålmodighed, der betaler sig: kødet slipper benet, øllen bliver til sovs.

  Brun. Øl. Lav ovn. Si.

  Det er den ret, man sætter over, før man tænder pejsen.
tip: Hold sværen over væskelinjen under brasereringen, hvis du vil finish’e den sprød — ellers bliver den læderagtig.
=====
title: Langtidsstegte oksehaler i mørk sky
slug: oksehaler-moerk-sky
category: stobejern
description: Langtidsstegte oksehaler i mørk sky — intens efterårsret, der skal simre 4–5 timer, til kødet er geléagtigt.
prepTime: PT30M
cookTime: PT4H30M
totalTime: PT5H
servings: 4
difficulty: svær
tags:
  - oksehaler
  - oksehale
  - mørk sky
  - langtidsstegt
  - gryderet
  - efterår
  - støbejern
imageAlt: Langtidsstegte oksehaler i mørk sky i støbejernsgryde
featured: true
ingredients:
  - 1,8–2 kg oksehale, skåret ved leddene
  - 2 spsk olie
  - 2 løg, 2 gulerødder, 2 stilke bladselleri, ¼ knoldselleri — hakket
  - 2 spsk tomatpuré
  - 2 spsk hvedemel
  - 3 dl tør rødvin
  - 1 liter kraftig oksebouillon
  - 2 laurbærblade, 8 peberkorn, 4 kviste timian, 2 fed hvidløg
  - 1 spsk mørk soya (valgfrit, til farve)
  - Salt og peber
steps:
  - Tænd ovnen på 140 °C. Dup oksehalerne tørre. Brun hårdt i olie i Dutch Oven i portioner. Tag op.
  - Svits grøntsager 10 minutter, til de tager farve. Tomatpuré 2 minutter. Drys mel over, rør 1 minut.
  - Vin i. Skrab bunden. Kog ind 5 minutter. Bouillon, krydderier og soya i. Kød tilbage — næsten dækket.
  - Låg på. I ovnen 4–5 timer, til kødet falder fra benet, og saucen er dyb og blank.
  - Tag kødet op. Si skysovsen, kog evt. ind. Smag til. Læg kød tilbage, eller pluk det af benene. Server med kartoffelmos eller polenta.
faq:
  - question: Forskel på versionen med mørkt øl?
    answer: Oksehale i mørkt øl er mere bitter-sød. Her er det klassisk mørk sky på vin og bouillon — ren kødsauce.
  - question: Kan tiden kortes?
    answer: Ved 160 °C ca. 3–3½ time. Lavere varme giver mere gelé og renere smag.
  - question: For fed?
    answer: Køl, skim fedtet af, og varm op. Oksehale er fed — det er pointen, men du kan styre overfladen.
  - question: Til hvad?
    answer: Kartoffelmos, cremet polenta eller bløde gnocchi. Noget, der kan bære skysovsen.
body: |
  Langtidsstegte oksehaler er nørdet efterårsmad: 4–5 timer, lav varme, og en mørk sky, der smager af ben og tålmodighed.

  Brun hårdt. Vin ind. Ovnen lav.

  Når kødet glider af, har du den mest intense sauce, en gryde kan lave.
tip: 140 °C og tålmodighed slår 180 °C og hastværk. Kollagenet skal smelte — ikke koge i stykker.
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
