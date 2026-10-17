#!/usr/bin/env python3
"""One Pot batch — 20 opskrifter (okt 2026)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"
PUBLISHED = "2026-10-16"

RECIPES = r'''
=====
title: One pot cremet bacon- og svampepasta i støbejernsgryde
slug: one-pot-bacon-svampe-pasta
category: stobejern
description: One pot cremet bacon- og svampepasta i støbejernsgryde — pasta, bacon og champignon kogt færdige i samme gryde.
prepTime: PT10M
cookTime: PT20M
totalTime: PT30M
servings: 4
difficulty: nem
tags:
  - one pot
  - pasta
  - bacon
  - svampe
  - champignon
  - støbejern
  - hverdagsmad
imageAlt: Cremet bacon- og svampepasta i støbejernsgryde
ingredients:
  - 300 g pasta (penne eller fusilli)
  - 150 g bacon i tern
  - 250 g champignon, skivede
  - 1 løg, finthakket
  - 2 fed hvidløg, pressede
  - 7 dl grøntsags- eller kyllingebouillon
  - 1½ dl piskefløde
  - 50 g parmesan, revet
  - 1 spsk smør eller olie
  - Salt, peber, persille
steps:
  - Brun bacon i støbejernsgryden, til det er sprødt. Tag halvdelen op til topping.
  - Svits champignon og løg i fedtet 5–6 minutter, til væsken er væk. Hvidløg 30 sekunder.
  - Tilsæt pasta og bouillon. Bring i kog under omrøring. Kog 10–12 minutter, til pastaen er al dente, og væsken er cremet.
  - Tag af varmen. Rør fløde og det meste af parmesanen i. Smag til med salt og peber.
  - Server i gryden med bacon-topping, resten af parmesanen og persille.
faq:
  - question: Forskel på one pot pasta?
    answer: Klassisk one pot pasta er tomatbaseret. Her er det bacon, svampe og fløde i støbejern — mere umami, mindre syre.
  - question: Bliver pastaen klistrende?
    answer: Rør ofte, især de første minutter. Brug en bred gryde, så alt koger jævnt.
  - question: Uden fløde?
    answer: Brug ekstra bouillon og mere parmesan. Saucen bliver mindre blank, men stadig cremet af pastaens stivelse.
  - question: Hvilke svampe?
    answer: Champignon er nemmest. Bland med portobello eller østershatte for mere dybde.
body: |
  One pot bacon- og svampepasta er støbejernets hverdagsgenvej: bacon, champignon og pasta i samme gryde, én ske at vaske.

  Brun baconen først. Pastaen skal suge bouillonen, ikke svømme i den.

  Stivelsen fra pastaen gør saucen blank — fløden er bare den sidste blankhed.
tip: Tag gryden af varmen, før du rører fløden i. Så skiller den ikke, og parmesanen smelter jævnt.
=====
title: One pot krydret chili con carne med mørk øl og oksetyksteg
slug: one-pot-chili-con-carne-moerkt-oel
category: gryde
description: One pot chili con carne med mørk øl og oksetyksteg — dyb, maltet gryderet med skært kød i stedet for hakket.
prepTime: PT20M
cookTime: PT2H30M
totalTime: PT2H50M
servings: 6
difficulty: mellem
tags:
  - one pot
  - chili con carne
  - oksetyksteg
  - mørk øl
  - bønner
  - gryderet
  - gryde
imageAlt: Chili con carne med oksetyksteg og mørk øl i gryde
ingredients:
  - 1 kg oksetyksteg, skåret i 2–3 cm tern
  - 2 dåser (á 400 g) hakkede tomater
  - 1 dåse (400 g) kidneybønner, skyllede
  - 1 dåse (400 g) sorte bønner, skyllede (valgfrit)
  - 2 store løg, hakket
  - 3 fed hvidløg
  - 2 røde peberfrugter i tern
  - 1–2 friske chili efter smag
  - 3 spsk tomatpuré
  - 3 dl mørk øl (porter eller stout)
  - 2 dl oksebouillon
  - 2 spsk olie
  - 2 spsk chilipulver, 1 tsk spidskommen, 1 tsk røget paprika, 1 tsk oregano
  - Salt, peber, lime og koriander til servering
steps:
  - Brun kødet hårdt i portioner i olie i en tung gryde. Tag op.
  - Svits løg og peberfrugt 8–10 minutter. Hvidløg, chili og tomatpuré 1 minut. Krydderier 30 sekunder.
  - Øl i — skrab bunden. Tomater, bouillon og kød tilbage. Bring i kog, skru ned.
  - Simre under låg 2–2½ time, til kødet er mørt. Rør bønnerne i de sidste 15 minutter.
  - Smag til. Server med lime, koriander, ris eller nachos.
faq:
  - question: Forskel på klassisk chili con carne?
    answer: Den klassiske bruger ofte hakket kød. Her er det skært oksetyksteg og mørk øl — mere braisering, mere dybde.
  - question: Hvilken øl?
    answer: Porter eller stout. Undgå bitter IPA — bitterheden bliver for skarp efter lang simre.
  - question: Kan det laves dagen før?
    answer: Ja. Chili bliver bedre overnight. Varm forsigtigt, og tilsæt lidt bouillon hvis den er tyk.
  - question: Trykkoger?
    answer: Se chili con carne i trykkoger, hvis du vil have samme idé på under en time.
body: |
  One pot chili med mørk øl og oksetyksteg er chili, der tager sig tid: skært kød, malt fra øllen og bønner til sidst.

  Brun hårdt. Simre lavt. Smag til med lime.

  Det er ikke hverdags-hakkekødschili — det er weekendgryden.
tip: Tilsæt bønnerne sent, så de ikke bliver til mos. Kødet skal være smørmørt, før de kommer i.
=====
title: One pot lynhurtig pølseret med chorizo og røget paprika
slug: one-pot-poelseret-chorizo-paprika
category: gryde
description: One pot lynhurtig pølseret med chorizo og røget paprika — pasta, chorizo og tomat i samme gryde på under 30 minutter.
prepTime: PT10M
cookTime: PT18M
totalTime: PT28M
servings: 4
difficulty: nem
tags:
  - one pot
  - pølseret
  - chorizo
  - røget paprika
  - pasta
  - hverdagsmad
  - gryde
imageAlt: One pot pølseret med chorizo og røget paprika i gryde
ingredients:
  - 200 g chorizo, skåret i skiver
  - 200 g mild pølse (grill eller wiener), i skiver
  - 300 g pasta (penne eller fusilli)
  - 1 dåse (400 g) hakkede tomater
  - 1 spsk tomatpuré
  - 1 løg, 2 fed hvidløg
  - 7 dl vand eller bouillon
  - 1½ tsk røget paprika
  - 1 spsk olie
  - Salt, peber, persille
  - Valgfrit: 50 g revet ost
steps:
  - Brun chorizo og pølse i olie i en bred gryde. Tag halvdelen op til topping.
  - Svits løg og hvidløg 2 minutter. Tomatpuré og røget paprika i.
  - Tilsæt pasta, hakkede tomater og vand. Rør rundt. Salt.
  - Kog under låg 12–14 minutter, rør jævnligt, til pastaen er mør, og saucen er cremet.
  - Smag til. Ost og sparede pølseskiver over. Persille. Server i gryden.
faq:
  - question: Forskel på one-pot pølseret?
    answer: Den enkle one-pot pølseret bruger almindelige pølser. Her er chorizo og røget paprika pointen — mere røg, mere fedme.
  - question: Mild eller stærk chorizo?
    answer: Begge virker. Stærk chorizo giver varme; mild er mere børnevenlig — justér paprikaen.
  - question: Svensk pølseret?
    answer: Nej. Svensk er cremet sennepssauce til mos. Her er pasta og tomat i én gryde.
  - question: Uden pasta?
    answer: Så er det mere en chorizogryde — tilsæt kartofler eller server til brød.
body: |
  One pot pølseret med chorizo er hverdagens genvej med røg: chorizo, pasta og tomat i samme gryde.

  Brun pølserne først. Pastaen skal suge saucen.

  Røget paprika binder det hele sammen uden ekstra opvask.
tip: Hold et øje de sidste minutter. Når pastaen er al dente, sluk — restvarmen koger den færdig.
=====
title: One pot cremet dild- og hvidløgskylling med kartofler
slug: one-pot-dild-hvidloegskylling
category: gryde
description: One pot cremet dild- og hvidløgskylling med kartofler — blød kylling, kartofler og frisk dild i samme gryde.
prepTime: PT15M
cookTime: PT35M
totalTime: PT50M
servings: 4
difficulty: nem
tags:
  - one pot
  - kylling
  - dild
  - hvidløg
  - kartofler
  - fløde
  - gryde
imageAlt: Cremet dild- og hvidløgskylling med kartofler i gryde
ingredients:
  - 800 g kyllingelår uden ben (eller bryst i store stykker)
  - 800 g kartofler, i både
  - 1 løg, hakket
  - 4 fed hvidløg, skivede
  - 2 dl kyllingebouillon
  - 2 dl piskefløde
  - 1 bundt frisk dild, hakket
  - 1 spsk smør + 1 spsk olie
  - 1 tsk dijonsennep
  - Salt, peber, citronsaft
steps:
  - Salt og peber kyllingen. Brun i smør og olie i gryden 3–4 minutter pr. side. Tag op.
  - Svits løg 3 minutter. Hvidløg 30 sekunder. Kartofler i, rør rundt.
  - Bouillon i. Læg kyllingen ovenpå. Låg på. Simre 20–25 minutter, til kartofler og kød er møre.
  - Tag kyllingen op. Rør fløde og sennep i. Kog 2–3 minutter, til saucen tykner lidt.
  - Kylling tilbage. Dild og citronsaft i. Smag til. Server i gryden.
faq:
  - question: Bryst eller lår?
    answer: Lår er mere tilgivende. Bryst virker, hvis du skærer dem store og undgår at overkoge dem.
  - question: Kan dilden komme tidligere i?
    answer: Nej — frisk dild mister aroma ved lang kogning. Rør den i til allersidst.
  - question: Uden fløde?
    answer: Brug creme fraiche af varmen, eller ekstra bouillon og en knivspids majsstivelse.
  - question: Hvilke kartofler?
    answer: Fastkogende. Melede falder lettere fra hinanden i saucen.
body: |
  One pot dild- og hvidløgskylling er den lyse gryderet: kylling, kartofler og masser af dild i samme gryde.

  Brun kyllingen. Simre kartoflerne med. Dild til sidst.

  Det er hverdagsmad, der smager af sommer — også i oktober.
tip: En skvæt citronsaft lige før servering skærer fløden og får dilden til at springe frem.
=====
title: One pot bålmad — vildtgryde med enebær og fløde
slug: one-pot-vildtgryde-enebaer
category: baalmad
description: One pot bålmad — vildtgryde med enebær og fløde. Dutch oven over gløder med rådyr eller hjort.
prepTime: PT20M
cookTime: PT1H30M
totalTime: PT1H50M
servings: 4
difficulty: mellem
tags:
  - one pot
  - bålmad
  - vildtgryde
  - enebær
  - rådyr
  - fløde
  - dutch oven
imageAlt: Vildtgryde med enebær og fløde i dutch oven over bål
ingredients:
  - 800 g vildtkød (rådyr, hjort eller vildsvin) i 3 cm tern
  - 200 g bacon i tern
  - 2 løg, hakket
  - 2 gulerødder i skiver
  - 250 g champignon, halverede
  - 8–10 tørrede enebær, knuste
  - 2 dl rødvin
  - 3 dl vildt- eller oksebouillon
  - 1½ dl piskefløde
  - 2 spsk tomatpuré
  - 2 laurbærblade, 2 kviste timian
  - Salt, peber, smør/olie
steps:
  - Brun bacon i dutch oven over gløder. Tag op. Brun vildtkødet i fedtet i portioner. Tag op.
  - Svits løg, gulerod og champignon. Tomatpuré og enebær i.
  - Vin i — skrab bunden. Bouillon, laurbær, timian, bacon og kød tilbage. Låg på.
  - Simre 1–1½ time, flyt mellem gløder og låg-kul, til kødet er mørt.
  - Rør fløde i de sidste 5 minutter. Smag til. Server med brød eller kartoffelmos.
faq:
  - question: Hvilket vildt?
    answer: Rådyr og hjort er klassiske. Vildsvin virker også — giv det gerne lidt længere tid.
  - question: For bitter enebær?
    answer: Brug 8–10 bær, knust. Flere gør retten medicinsk. Start lavt.
  - question: Kan det laves hjemme på komfur?
    answer: Ja. Samme opskrift i støbejern på lav blus eller i ovn ved 160 °C.
  - question: Uden fløde?
    answer: Lad saucen reducere lidt længere, eller rør en knivspids smør i til blankhed.
body: |
  One pot vildtgryde over bål er dutch oven-mad: vildt, enebær, vin og fløde i samme gryde.

  Brun hårdt. Simre lavt. Fløde til sidst.

  Enebær giver den skovagtige note, der gør vildt til vildt.
tip: Knus enebærrene let i en morter, før de kommer i — ellers smager de næsten ikke.
=====
title: One pot sprængt oksebryst med rodfrugter og saltlage-bouillon
slug: one-pot-spraengt-oksebryst
category: gryde
description: One pot sprængt oksebryst med rodfrugter og saltlage-bouillon — klassisk saltet bryst kogt mørt med rodfrugter.
prepTime: PT20M
cookTime: PT2H30M
totalTime: PT2H50M
servings: 6
difficulty: mellem
tags:
  - one pot
  - sprængt oksebryst
  - oksebryst
  - rodfrugter
  - saltlage
  - gryderet
  - gryde
imageAlt: Sprængt oksebryst med rodfrugter i gryde
ingredients:
  - 1,2–1,5 kg sprængt oksebryst (saltet)
  - 4 gulerødder i store stykker
  - ½ selleri i store tern
  - 4 kartofler i både
  - 2 porrer i grove stykker
  - 1 løg, 2 laurbærblade
  - 8–10 peberkorn
  - 1 tsk sennepsfrø (valgfrit)
  - Vand til dækning
  - Sennep og persille til servering
steps:
  - Skyl oksebrystet under koldt vand. Læg i gryde, dæk med vand. Bring i kog, skum af.
  - Tilsæt løg, laurbær, peberkorn og sennepsfrø. Simre under låg ca. 1½–2 time.
  - Tilsæt gulerod, selleri og porre. Kog 20 minutter. Kartofler i — kog til alt er mørt (ca. 20 minutter mere).
  - Tag kødet op, skær i skiver på tværs af fibrene.
  - Server med rodfrugterne, lidt af bouillonen, sennep og persille.
faq:
  - question: Skal det udblødes først?
    answer: Mange moderne sprængte bryster er mildere. Smag på bouillonen efter 30 minutter — er den meget salt, skift vandet én gang.
  - question: Kan jeg bruge usaltet bryst?
    answer: Ja, men tilsæt salt i vandet, og forvent en mildere, mere oksekødssuppe-agtig smag.
  - question: Hvad med resten af bouillonen?
    answer: Den er guld til suppe dagen efter. Frys i portioner.
  - question: Sennep til?
    answer: Ja — grov sennep er klassisk til sprængt oksebryst.
body: |
  One pot sprængt oksebryst er den gamle saltede klassiker: kød og rodfrugter i samme gryde, bouillon som sauce.

  Skum af. Simre lavt. Skær på tværs af fibrene.

  Det er søndagsmad uden stegesky — saltlagen er smagen.
tip: Skær først, når kødet har hvil 10 minutter. Saften bliver i skiverne, ikke på skærebrættet.
=====
title: One pot trykkoger-gullasch med rygende varm paprika
slug: one-pot-gullasch-trykkoger-paprika
category: trykkoger
description: One pot trykkoger-gullasch med rygende varm paprika — ungarsk gryderet på under en time med skært kød og masser af paprika.
prepTime: PT20M
cookTime: PT45M
totalTime: PT1H5M
servings: 6
difficulty: mellem
tags:
  - one pot
  - gullasch
  - trykkoger
  - paprika
  - oksekød
  - gryderet
imageAlt: Trykkoger-gullasch med varm paprika og oksekød
ingredients:
  - 1 kg skært oksekød til gryderet i 3 cm tern
  - 3 store løg, finthakket
  - 2 røde peberfrugter i strimler
  - 400 g kartofler i tern
  - 3 spsk sødmefuld paprika + 1–2 tsk stærk paprika
  - 2 spsk tomatpuré
  - 2 fed hvidløg
  - 4 dl oksebouillon
  - 2 spsk svinefedt eller olie
  - 2 laurbærblade, 1 tsk spidskommen
  - Salt, peber
  - Valgfrit: creme fraiche til servering
steps:
  - Brun kødet i portioner i trykkogeren på sauteringsprogram. Tag op.
  - Svits løg 8–10 minutter. Peberfrugt 3 minutter. Tag af varmen.
  - Rør paprika og tomatpuré i — paprikaen må ikke brænde. Hvidløg 30 sekunder.
  - Bouillon, laurbær, spidskommen, kartofler og kød i. Lås låget. Tryk 30–35 minutter. Naturlig trykudligning 10 minutter.
  - Smag til. Server med creme fraiche og brød.
faq:
  - question: Forskel på gullasch i trykkoger?
    answer: Samme idé — her er den stærke paprika skruet op, så retten bliver «rygende varm» uden at miste den sødmefulde base.
  - question: Bitter paprika?
    answer: Den blev for varm. Rør altid paprika i af varmen eller på meget lav blus i sekunder.
  - question: For stærk?
    answer: Start med 1 tsk stærk paprika. Du kan altid røre mere i efter trykket er ude.
  - question: Uden trykkoger?
    answer: Se klassisk gullasch i gryde — samme paprika-logik, længere simretid.
body: |
  One pot trykkoger-gullasch er paprika under tryk: skært kød, kartofler og en sauce, der bliver dyb på under en time.

  Brun hårdt. Paprika af varmen. Tryk lavt og tålmodigt.

  Den stærke paprika er knivspidsen, der får retten til at vågne.
tip: Brug sødmefuld paprika som hovedmængde. Den stærke er varme — ikke hele smagen.
=====
title: One pot krydret hakket oksekød, ris og chili i jernpande
slug: one-pot-oksekoed-ris-chili
category: pande
description: One pot krydret hakket oksekød, ris og chili i jernpande — taco-agtig one-pan-mad på ca. 30 minutter.
prepTime: PT10M
cookTime: PT25M
totalTime: PT35M
servings: 4
difficulty: nem
tags:
  - one pot
  - hakket oksekød
  - ris
  - chili
  - jernpande
  - hverdagsmad
  - pande
imageAlt: Krydret hakket oksekød med ris og chili i jernpande
ingredients:
  - 500 g hakket oksekød
  - 250 g langkornet ris
  - 1 dåse (400 g) hakkede tomater
  - 1 dåse (400 g) kidneybønner, skyllede
  - 1 løg, 2 fed hvidløg
  - 1 rød peberfrugt i tern
  - 1 frisk chili eller 1 tsk chiliflager
  - 6 dl bouillon
  - 1 spsk olie
  - 2 tsk spidskommen, 1 tsk røget paprika, 1 tsk oregano
  - Salt, peber, lime, koriander
steps:
  - Brun kødet hårdt i olie i jernpanden. Løg, peberfrugt og chili i 3–4 minutter. Hvidløg og krydderier 30 sekunder.
  - Ris i — rør rundt, så den får fedt og smag.
  - Tomater, bønner og bouillon i. Bring i kog. Salt.
  - Skru ned. Låg på (eller folie). Simre 18–20 minutter, til risen er mør. Rør midtvejs.
  - Smag til. Lime og koriander over. Server direkte fra panden.
faq:
  - question: Bliver risen klistrende?
    answer: Brug langkornet ris, og rør kun midtvejs. For meget røring frigør stivelse.
  - question: Kan jeg bruge basmati?
    answer: Ja. Tjek væskemængden — basmati kan kræve lidt mindre bouillon.
  - question: Mere taco-agtigt?
    answer: Top med revet ost, creme fraiche og nachochips direkte i panden.
  - question: Uden bønner?
    answer: Drop dem, og tilsæt ekstra peberfrugt eller majs.
body: |
  One pot hakket oksekød med ris og chili er jernpandens midtugemad: kød, ris og tomat i samme pande.

  Brun kødet. Lad risen suge saucen.

  Det er taco uden tortilla — eller med, hvis du vil.
tip: Lad panden hvile 5 minutter af varmen med låg på. Risen sætter sig, og saucen tykner.
=====
title: One pot flødestuvet spidskål med sprøde bacondrys
slug: one-pot-floede-spidskaal-bacon
category: gryde
description: One pot flødestuvet spidskål med sprøde bacondrys — blød kål, fløde og knasende bacon i samme gryde.
prepTime: PT10M
cookTime: PT25M
totalTime: PT35M
servings: 4
difficulty: nem
tags:
  - one pot
  - spidskål
  - fløde
  - bacon
  - tilbehør
  - vegetarisk mulighed
  - gryde
imageAlt: Flødestuvet spidskål med sprøde bacondrys
ingredients:
  - 1 stort spidskålshoved (ca. 800 g), i strimler
  - 150 g bacon i tern
  - 1 løg, finthakket
  - 2 dl piskefløde
  - 1 dl bouillon eller vand
  - 1 tsk dijonsennep
  - 1 spsk smør
  - Salt, peber, muskatnød
  - Valgfrit: lidt citronsaft
steps:
  - Brun bacon i gryden, til det er sprødt. Tag op på køkkenrulle.
  - Svits løg i fedtet 2–3 minutter. Spidskål i portioner, til det synker og får lidt farve.
  - Bouillon i. Låg på. Simre 8–10 minutter, til kålen er blød men ikke grød.
  - Rør fløde og sennep i. Kog uden låg 3–5 minutter, til saucen tykner. Smag til med salt, peber og muskat.
  - Server med bacondrys og evt. citronsaft.
faq:
  - question: Forskel på braiseret spidskål med bacon?
    answer: Den braiserede har ofte mindre fløde og mere stegesky. Her er det bevidst stuvet og cremet med sprødt bacon ovenpå.
  - question: Kan det være vegetarisk?
    answer: Ja — skip bacon, brug smør og olie, og top med ristede nødder eller brødkrummer.
  - question: Hvidkål i stedet?
    answer: Ja, men giv den længere tid. Spidskål er sødere og blødere hurtigere.
  - question: Til hvad?
    answer: Til koteletter, medister, stegt flæsk — eller som hovedret med æg og brød.
body: |
  One pot flødestuvet spidskål er den bløde kålgryde: spidskål i fløde, bacon på toppen.

  Brun baconen først. Stuv kålen. Drys til sidst.

  Det er tilbehør, der stjæler billedet fra kødet.
tip: Tag baconen op, før kålen går i — ellers bliver den blød i fløden i stedet for sprød.
=====
title: One pot cajun-pasta med kylling, krydret pølse og flagesalt
slug: one-pot-cajun-pasta
category: gryde
description: One pot cajun-pasta med kylling, krydret pølse og flagesalt — cremet, røget og færdig i én gryde.
prepTime: PT15M
cookTime: PT25M
totalTime: PT40M
servings: 4
difficulty: nem
tags:
  - one pot
  - cajun
  - pasta
  - kylling
  - pølse
  - flagesalt
  - gryde
imageAlt: Cajun-pasta med kylling og krydret pølse i gryde
ingredients:
  - 400 g kyllingebryst i strimler
  - 200 g krydret pølse eller andouille-agtig pølse i skiver
  - 300 g pasta (penne)
  - 1 rød peberfrugt i strimler
  - 1 løg, 3 fed hvidløg
  - 1 dåse (400 g) hakkede tomater
  - 6 dl kyllingebouillon
  - 1½ dl piskefløde
  - 2 spsk cajun-krydderi
  - 1 spsk olie
  - Flagesalt, peber, forårsløg
steps:
  - Vend kylling i 1 spsk cajun. Brun kylling og pølse i olie. Tag op.
  - Svits løg og peberfrugt 3 minutter. Hvidløg og resten af cajun 30 sekunder.
  - Pasta, tomater og bouillon i. Bring i kog. Kog 10–12 minutter under omrøring.
  - Kød tilbage. Fløde i. Kog 2–3 minutter, til saucen klæber.
  - Smag til. Flagesalt og forårsløg over. Server i gryden.
faq:
  - question: Hvad er cajun-krydderi?
    answer: Blanding med paprika, hvidløg, oregano, timian og cayenne. Købt pose virker — smag til, for saltindholdet varierer.
  - question: For stærkt?
    answer: Brug mild pølse, og start med 1 spsk cajun. Flagesalt til sidst balancerer varmen.
  - question: Uden fløde?
    answer: Ekstra bouillon og lidt revet ost giver stadig cremethed via pastaens stivelse.
  - question: Andouille?
    answer: Klassisk i cajun — hvis du kan få det. Ellers chorizo eller stærk grillpølse.
body: |
  One pot cajun-pasta er den røgede hverdagsgryde: kylling, krydret pølse og pasta i samme gryde.

  Brun kødet. Lad pastaen suge tomaten. Flagesalt til sidst.

  Cajun er varme og røg — ikke bare chili.
tip: Smag bouillonen, før du salter hårdt. Cajun-krydderi og pølse kan allerede være salte — flagesalt er finish, ikke base.
=====
title: One pot asiatisk oksekød med nudler og masser af hvidløg
slug: one-pot-asiatisk-oksekoed-nudler
category: gryde
description: One pot asiatisk oksekød med nudler og masser af hvidløg — stir-fry-smag i én gryde på ca. 25 minutter.
prepTime: PT15M
cookTime: PT15M
totalTime: PT30M
servings: 4
difficulty: nem
tags:
  - one pot
  - asiatisk
  - oksekød
  - nudler
  - hvidløg
  - sojasauce
  - gryde
imageAlt: Asiatisk oksekød med nudler og hvidløg i gryde
ingredients:
  - 500 g oksekød i tynde strimler (tyndsteg eller roastbeef)
  - 250 g æggenudler eller wheat noodles
  - 6–8 fed hvidløg, skivede
  - 1 spsk frisk ingefær, reven
  - 1 rød peberfrugt i strimler
  - 150 g sukkerærter eller broccoli
  - 4 spsk sojasauce
  - 1 spsk østerssauce (valgfrit)
  - 1 tsk sesamolie
  - 1 spsk sukker eller honning
  - 6 dl bouillon eller vand
  - 2 spsk olie
  - Forårsløg, chili, sesamfrø
steps:
  - Brun kødet hårdt i olie i portioner. Tag op.
  - Svits hvidløg og ingefær 30–45 sekunder på middel varme — de må ikke brænde. Peberfrugt og grønt i 2 minutter.
  - Bouillon, soja, østerssauce og sukker i. Bring i kog. Nudler i.
  - Kog 4–6 minutter under omrøring, til nudlerne er møre, og saucen klæber.
  - Kød tilbage. Sesamolie i. Forårsløg, chili og sesam over. Server straks.
faq:
  - question: Hvilke nudler?
    answer: Tørre æggenudler eller wheat noodles. Risnudler kræver mindre væske og kortere tid — hold øje.
  - question: Brænder hvidløget?
    answer: Skru ned, og svits kun til det dufter. Brændt hvidløg smager bittert — start forfra hellere end at redde det.
  - question: Kan jeg bruge hakket kød?
    answer: Ja. Brun det godt, og følg resten. Strimler giver mere «wok-fornemmelse».
  - question: Mere sauce?
    answer: Tilsæt ½–1 dl ekstra bouillon til sidst. Nudlerne suger hurtigt.
body: |
  One pot asiatisk oksekød med nudler er wok i gryden: tynde kødstykker, masser af hvidløg og nudler i samme skål.

  Brun kødet. Pas på hvidløget. Lad nudlerne suge saucen.

  Det er takeaway-tempo uden plastikbakke.
tip: Skær kødet på tværs af fibrene i tynde strimler, og brun det i portioner — ellers koger det i stedet for at få stegeskorpe.
=====
title: One pot marokkansk lammebov med kikærter fra trykkogeren
slug: one-pot-marokkansk-lammebov
category: trykkoger
description: One pot marokkansk lammebov med kikærter fra trykkogeren — varm, krydret tagine-agtig gryde på under 90 minutter.
prepTime: PT20M
cookTime: PT55M
totalTime: PT1H15M
servings: 6
difficulty: mellem
tags:
  - one pot
  - marokkansk
  - lammebov
  - kikærter
  - trykkoger
  - tagine
imageAlt: Marokkansk lammebov med kikærter i trykkoger
ingredients:
  - 1,2 kg lammebov i 3–4 cm tern
  - 1 dåse (400 g) kikærter, skyllede
  - 1 dåse (400 g) hakkede tomater
  - 2 løg, hakket
  - 4 fed hvidløg
  - 2 gulerødder i skiver
  - 1 spsk ras el hanout eller 1 tsk hver: spidskommen, koriander, kanel
  - 1 tsk stødt ingefær, ½ tsk cayenne
  - 1 spsk tomatpuré
  - 4 dl lamme- eller oksebouillon
  - 2 spsk olie
  - Salt, peber, koriander, citron
  - Valgfrit: 50 g tørrede abrikoser
steps:
  - Brun lammet i olie i trykkogeren i portioner. Tag op.
  - Svits løg 5 minutter. Hvidløg, krydderier og tomatpuré 1 minut.
  - Tomater, bouillon, gulerødder, abrikoser og kød i. Lås låget. Tryk 40 minutter. Naturlig udligning 10 minutter.
  - Rør kikærter i. Sauter uden låg 5 minutter, hvis saucen skal tykne.
  - Smag til. Koriander og citronsaft over. Server med couscous eller brød.
faq:
  - question: Kan jeg bruge tørrede kikærter?
    answer: Ja — udblød natten over, og giv dem med under tryk. Dåsekikærter er nemmere til sidst.
  - question: For sødt med abrikoser?
    answer: Drop dem, eller brug kun en håndfuld. De er klassiske i marokkansk gryde, men ikke lovpligtige.
  - question: Uden trykkoger?
    answer: Samme opskrift i støbejern 2–2½ time ved 160 °C, til kødet er mørt.
  - question: Hvilket udskær?
    answer: Bov er bedst til langsimre. Kølle virker også. Filet er for mager.
body: |
  One pot marokkansk lammebov er trykkogerens tagine: lam, krydderier og kikærter i samme gryde.

  Brun kødet. Krydder af varmen. Tryk til det er smørmørt.

  Ras el hanout gør det marokkansk uden 12 separate poser.
tip: Smag til med citron til sidst — syren løfter kanel og spidskommen, så retten ikke bliver tung.
=====
title: One pot cremet ostesovs-pasta med hårdtstegt bacon
slug: one-pot-ostesovs-pasta-bacon
category: gryde
description: One pot cremet ostesovs-pasta med hårdtstegt bacon — mac & cheese-energi i én gryde med sprødt bacon.
prepTime: PT10M
cookTime: PT20M
totalTime: PT30M
servings: 4
difficulty: nem
tags:
  - one pot
  - pasta
  - ostesovs
  - bacon
  - mac and cheese
  - hverdagsmad
  - gryde
imageAlt: Cremet ostesovs-pasta med hårdtstegt bacon
ingredients:
  - 350 g pasta (rør eller elbows)
  - 150 g bacon i tern
  - 7 dl mælk (eller 5 dl mælk + 2 dl bouillon)
  - 150 g revet cheddar eller blanding af cheddar og mozzarella
  - 50 g parmesan, revet
  - 1 spsk smør
  - 1 tsk dijonsennep
  - Lidt muskatnød, salt, peber
  - Valgfrit: chiliflager
steps:
  - Steg bacon hårdt i gryden, til det er meget sprødt. Tag op på køkkenrulle.
  - Hæld det meste af fedtet fra — behold 1 spsk. Smør i.
  - Pasta og mælk i. Bring i kog under omrøring. Kog 10–12 minutter, til pastaen er mør, og saucen er tyk.
  - Tag af varmen. Rør ost, sennep og muskat i, til det er blankt. Smag til.
  - Server med bacon ovenpå og evt. chiliflager.
faq:
  - question: Skiller osten?
    answer: Tag gryden af varmen, før osten går i. For høj varme gør saucen grynet.
  - question: Hvilken ost?
    answer: Cheddar smelter godt og smager af noget. Ren mozzarella bliver elastisk — bland gerne.
  - question: Uden bacon?
    answer: Ja — top med ristede brødkrummer eller stegte løg for knas.
  - question: Kan den laves i ovn bagefter?
    answer: Ja. Hæld i fad, drys ost og bacon, gratiner 5–8 minutter — men den er færdig allerede i gryden.
body: |
  One pot ostesovs-pasta er mac & cheese uden roux: pasta kogt i mælk, ost rørt i, bacon på toppen.

  Steg baconen hårdt. Kog pastaen cremet. Ost af varmen.

  Det er børnemad for voksne med flagesalt-attitude.
tip: Gem en håndfuld pasta-kogevæske (mælken), hvis saucen tykner for meget — rør den tilbage til blankhed.
=====
title: One pot krydret kyllingebryst på bund af tomatris i ovn
slug: one-pot-kylling-tomatris
category: ovn
description: One pot krydret kyllingebryst på bund af tomatris i ovn — kylling og ris færdigbages i samme fad.
prepTime: PT15M
cookTime: PT40M
totalTime: PT55M
servings: 4
difficulty: nem
tags:
  - one pot
  - kyllingebryst
  - tomatris
  - ovn
  - hverdagsmad
  - one pan
imageAlt: Krydret kyllingebryst på tomatris bagt i ovn
ingredients:
  - 4 kyllingebryst (ca. 800 g)
  - 250 g langkornet ris
  - 1 dåse (400 g) hakkede tomater
  - 4 dl kyllingebouillon
  - 1 løg, finthakket
  - 2 fed hvidløg
  - 1 rød peberfrugt i tern
  - 2 spsk olie
  - 2 tsk paprika, 1 tsk oregano, 1 tsk spidskommen, ½ tsk chili
  - Salt, peber, citron, persille
steps:
  - Tænd ovnen på 200 °C. Vend kylling i olie, paprika, oregano, spidskommen, chili, salt og peber.
  - Bland ris, tomater, bouillon, løg, hvidløg og peberfrugt i et ovnfast fad. Salt.
  - Læg kyllingen ovenpå risen. Dæk med folie.
  - Bag 25 minutter. Fjern folie, bag 10–15 minutter mere, til kyllingen er gennemstegt, og risen er mør.
  - Hvile 5 minutter. Citron og persille over. Server fra fadet.
faq:
  - question: Bliver risen tør?
    answer: Hold folien på de første 25 minutter. Er risen stadig hård, tilsæt ½ dl kogende bouillon, og bag 5 minutter mere.
  - question: Kan jeg bruge lår?
    answer: Ja — de tåler længere tid. Tjek at risen stadig har væske nok.
  - question: For vandig ris?
    answer: Bag 5 minutter uden folie ekstra, eller rør forsigtigt og lad dampe af.
  - question: Airfryer?
    answer: Ikke til hele fadet. Brug ovnen — det er pointen med bunden af ris.
body: |
  One pot kylling på tomatris er ovnens midtugefad: ris i bunden, krydret bryst ovenpå, ét fad i opvasken.

  Dæk først. Brun til sidst. Hvile før servering.

  Tomaten gør risen saftig uden at den bliver grød.
tip: Dup kyllingen tør, før du vender den i krydderier — ellers damper den i stedet for at få farve til sidst.
=====
title: One pot klassisk biksemad med spejlæg i støbejernspande
slug: one-pot-biksemad-spejlaeg
category: stobejern
description: One pot klassisk biksemad med spejlæg i støbejernspande — restemad med knas, kartofler og blødyolk.
prepTime: PT15M
cookTime: PT25M
totalTime: PT40M
servings: 4
difficulty: nem
tags:
  - one pot
  - biksemad
  - spejlæg
  - støbejern
  - restemad
  - kartofler
imageAlt: Klassisk biksemad med spejlæg i støbejernspande
ingredients:
  - 600 g kogte kartofler i tern (gerne fra dagen før)
  - 300 g stegerest eller kogt kød i tern (steg, medister, pølse)
  - 2 løg i tern
  - 2 spsk smør + 1 spsk olie
  - 4 æg
  - Salt, peber, worcestershire eller sojasauce
  - Valgfrit: rødbeder, pickles, ketchup
steps:
  - Varm støbejernspanden meget varm. Smør og olie i. Svits løg 3–4 minutter.
  - Kartofler i. Steg uden at røre for meget de første 5 minutter — de skal have skorpe. Rør, steg 5–8 minutter mere.
  - Kødet i. Steg 3–4 minutter. Smag til med salt, peber og worcestershire.
  - Lav plads i panden, eller brug en ekstra pande, og steg spejlæg.
  - Server biksemaden med spejlæg ovenpå og evt. rødbeder.
faq:
  - question: Forskel på biksemad på pande?
    answer: Samme ret — her er støbejernet pointen: mere skorpe, mere jævn varme, spejlæg i samme pande hvis den er stor nok.
  - question: Rå kartofler?
    answer: Kog dem først, eller brug ovnstegte. Rå tern tager for lang tid og bliver ujævne.
  - question: Vegetarisk?
    answer: Drop kødet, tilsæt stegte svampe og ekstra løg. Spejlægget bærer stadig retten.
  - question: Airfryer-biksemad?
    answer: Der findes en airfryer-version — men støbejern giver den klassiske stegeskorpe.
body: |
  One pot biksemad i støbejern er restemadens højdepunkt: kartofler med skorpe, kød, spejlæg på toppen.

  Varm pande. Rør sjældent. Blødyolk til sidst.

  Det er ikke finmad — det er den rigtige mad.
tip: Brug kolde, kogte kartofler. Varme, nykogte kartofler smuldrer og bliver til mos i panden.
=====
title: One pot tykkam i mørkt hvidtøls-sauce med kartoffelbåde
slug: one-pot-tykkam-hvidtoel
category: gryde
description: One pot tykkam i mørkt hvidtøls-sauce med kartoffelbåde — braiseret svinekød med øl og kartofler i samme gryde.
prepTime: PT20M
cookTime: PT2H15M
totalTime: PT2H35M
servings: 6
difficulty: mellem
tags:
  - one pot
  - tykkam
  - hvidtøl
  - kartoffelbåde
  - svinekød
  - gryderet
  - gryde
imageAlt: Tykkam i mørkt hvidtøls-sauce med kartoffelbåde
ingredients:
  - 1,2 kg svine tykkam i 4 cm tern (eller i skiver)
  - 800 g kartofler i både
  - 2 løg, hakket
  - 2 gulerødder i skiver
  - 3 dl mørkt hvidtøl eller mørk lager
  - 3 dl svine- eller hønsebouillon
  - 2 spsk tomatpuré
  - 2 fed hvidløg
  - 2 laurbærblade, 2 kviste timian
  - 2 spsk olie eller svinefedt
  - Salt, peber, sennep til servering
steps:
  - Brun tykkammen hårdt i olie i portioner. Tag op.
  - Svits løg og gulerod 8 minutter. Tomatpuré og hvidløg 1 minut.
  - Øl i — skrab bunden. Bouillon, laurbær, timian og kød tilbage. Bring i kog. Skru ned.
  - Simre under låg 1½ time. Kartoflerne i. Simre 30–40 minutter mere, til kød og kartofler er møre.
  - Smag til. Server med sennep og evt. persille.
faq:
  - question: Hvilket øl?
    answer: Mørkt hvidtøl eller en mild mørk lager. Undgå meget humlede øl — bitterheden bliver skarp.
  - question: Kan jeg bruge nakkefilet?
    answer: Ja. Tykkam har mere fedme og bliver saftigere ved langsimre.
  - question: For tynd sauce?
    answer: Tag låget af de sidste 15 minutter, eller mash et par kartoffelstykker ned i saucen.
  - question: Ovnen i stedet?
    answer: Ja — 160 °C med låg på efter bruningen. Samme tider.
body: |
  One pot tykkam i hvidtøl er den mørke ølgryde: svinekød, kartoffelbåde og malt i samme gryde.

  Brun hårdt. Simre lavt. Kartofler sent nok til at de holder formen.

  Hvidtøl giver sødme uden sukker.
tip: Dup kødet tørret, før du bruner — vådt kød damper, og du mister stegeskyen til saucen.
=====
title: One pot cremet laksepasta med spinat og citronpeber
slug: one-pot-laksepasta-spinat
category: gryde
description: One pot cremet laksepasta med spinat og citronpeber — laks, pasta og fløde i samme gryde på ca. 25 minutter.
prepTime: PT10M
cookTime: PT18M
totalTime: PT28M
servings: 4
difficulty: nem
tags:
  - one pot
  - laks
  - pasta
  - spinat
  - citronpeber
  - fløde
  - gryde
imageAlt: Cremet laksepasta med spinat og citronpeber
ingredients:
  - 400 g lakseskær uden skind, i store tern
  - 300 g pasta (penne eller fusilli)
  - 100 g frisk spinat
  - 7 dl fiskebouillon eller vand + 1 fiskebouillonterning
  - 1½ dl piskefløde
  - 1 løg, 2 fed hvidløg
  - 1 citron (skal + saft)
  - 1 spsk smør eller olie
  - Citronpeber eller sort peber + citronskal
  - Salt, dild (valgfrit)
steps:
  - Svits løg i smør 2 minutter. Hvidløg 30 sekunder. Pasta og bouillon i. Bring i kog.
  - Kog 8–10 minutter under omrøring, til pastaen næsten er færdig.
  - Laks i. Kog forsigtigt 3–4 minutter, til den lige er gennemstegt.
  - Tag af varmen. Rør fløde, spinat, citronskal og -saft i. Smag til med citronpeber og salt.
  - Server straks med dild.
faq:
  - question: Bliver laksen tør?
    answer: Den skal kun lige igennem. Overkogt laks smuldrer og bliver tør — tag gryden af, så snart den flager.
  - question: Frossen spinat?
    answer: Ja — tø den op, og press væsken ud, før den røres i.
  - question: Uden fløde?
    answer: Ekstra pasta-stivelse og lidt creme fraiche af varmen virker. Eller bare citron og olie.
  - question: Røget laks?
    answer: Brug den som topping til sidst i stedet for at koge den — ellers bliver den for salt og sej.
body: |
  One pot laksepasta er den lyse fiskepasta: pasta kogt i bouillon, laks i til sidst, spinat og citronpeber.

  Kog pastaen. Laks kort. Spinat af varmen.

  Citronpeber er genvejen til både syre og varme.
tip: Salte forsigtigt — fiskebouillon og citronpeber kan allerede bære retten.
=====
title: One pot græsk inspireret fadkotelet med feta og oliven
slug: one-pot-graesk-fadkotelet
category: ovn
description: One pot græsk inspireret fadkotelet med feta og oliven — koteletter, kartofler og tomat i samme fad.
prepTime: PT15M
cookTime: PT50M
totalTime: PT1H5M
servings: 4
difficulty: nem
tags:
  - one pot
  - fadkotelet
  - græsk
  - feta
  - oliven
  - koteletter
  - ovn
imageAlt: Græsk inspireret fadkotelet med feta og oliven
ingredients:
  - 4 svinekoteletter (ca. 800–900 g)
  - 800 g kartofler i både
  - 1 dåse (400 g) hakkede tomater eller 400 g cherrytomater
  - 1 rød løg i både
  - 3 fed hvidløg, skivede
  - 100 g feta i tern
  - 80 g sorte oliven, udstenende
  - 3 spsk olivenolie
  - 1 tsk oregano, 1 tsk paprika
  - Salt, peber, citron, persille
steps:
  - Tænd ovnen på 200 °C. Vend kartofler, løg og hvidløg med olie, oregano, paprika, salt og peber i et ovnfast fad.
  - Fordel tomater og oliven over. Læg koteletterne ovenpå. Salt og peber kødet.
  - Bag 35 minutter. Fordel feta over. Bag 10–15 minutter mere, til koteletterne er færdige, og kartoflerne er møre.
  - Hvile 5 minutter. Citron og persille over. Server fra fadet.
faq:
  - question: Bliver koteletterne tørre?
    answer: Vælg koteletter med lidt fedtkant, og undgå at overbage dem. Feta og tomat holder fadet saftigt.
  - question: Kan jeg bruge lammekoteletter?
    answer: Ja — de er endnu mere «græske». Tjek stegetiden; tynde lammekoteletter er hurtigere færdige.
  - question: Uden feta?
    answer: Brug en anden saltet ost, eller bare ekstra oliven og citron.
  - question: På grill?
    answer: Grill koteletterne separat, og bag kartoffel-tomat-bunden i ovn — men så er det ikke længere one pot.
body: |
  One pot græsk fadkotelet er ovnfadet med sol: koteletter, kartofler, tomat, feta og oliven.

  Bag kartoflerne med. Feta til sidst. Citron over.

  Oregano og oliven gør det græsk uden at det bliver temaaften.
tip: Læg koteletterne ovenpå — ikke begravet — så de får farve, mens kartoflerne bliver møre i saften.
=====
title: One pot stærk bønnegryde med chili og sprøde flæskesvær
slug: one-pot-boennegryde-flaeskesvaer
category: gryde
description: One pot stærk bønnegryde med chili og sprøde flæskesvær — vegetarisk base med knasende topping.
prepTime: PT15M
cookTime: PT35M
totalTime: PT50M
servings: 4
difficulty: nem
tags:
  - one pot
  - bønnegryde
  - chili
  - flæskesvær
  - kidneybønner
  - gryderet
  - gryde
imageAlt: Stærk bønnegryde med chili og sprøde flæskesvær
ingredients:
  - 2 dåser (á 400 g) kidneybønner, skyllede
  - 1 dåse (400 g) hakkede tomater
  - 1 dåse (400 g) hvide bønner eller sorte bønner, skyllede
  - 1 løg, 3 fed hvidløg
  - 1 rød peberfrugt i tern
  - 1–2 friske chili eller 1–2 tsk chiliflager
  - 2 spsk tomatpuré
  - 2 dl grøntsagsbouillon
  - 1 tsk spidskommen, 1 tsk røget paprika, 1 tsk oregano
  - 2 spsk olie
  - 80–100 g flæskesvær (købte eller hjemmelavede)
  - Salt, peber, lime, koriander
steps:
  - Svits løg og peberfrugt i olie 5–6 minutter. Hvidløg, chili, tomatpuré og krydderier 1 minut.
  - Tomater, bouillon og bønner i. Bring i kog. Simre 20–25 minutter, til gryden er tyk.
  - Smag til med salt, peber og lime.
  - Knus flæskesvær let, og drys over lige før servering, så de bliver sprøde.
  - Top med koriander. Server med ris, brød eller nachos.
faq:
  - question: Er det chili sin carne?
    answer: Næsten — det er bønnegryden uden hakkekød, med flæskesvær som knas. Mere bælgfrugt, samme varme.
  - question: Vegetarisk?
    answer: Skip flæskesvær, og top med ristede tortillachips eller frø. Selve gryden er vegetarisk.
  - question: For stærk?
    answer: Start med én chili uden kerner. Du kan altid røre mere i til sidst.
  - question: Hjemmelavede flæskesvær?
    answer: Ja, hvis du har dem. Ellers købte — vigtigst er, at de først kommer på til sidst.
body: |
  One pot stærk bønnegryde er bælgfrugternes chili: bønner, tomat, chili — og flæskesvær til knas.

  Byg smagen i bunden. Simre tykt. Top sprødt til sidst.

  Det er billig mad med karakter.
tip: Flæskesvær direkte i gryden bliver bløde. Drys dem på tallerkenen eller i sidste sekund.
=====
title: One pot langtidssimret bolognese direkte i støbejernet
slug: one-pot-bolognese-stobejern
category: stobejern
description: One pot langtidssimret bolognese direkte i støbejernet — klassisk kødsovs med tålmodighed og dyb smag.
prepTime: PT25M
cookTime: PT3H
totalTime: PT3H25M
servings: 8
difficulty: mellem
tags:
  - one pot
  - bolognese
  - støbejern
  - kødsovs
  - pasta
  - langtidssimret
imageAlt: Langtidssimret bolognese i støbejernsgryde
ingredients:
  - 500 g hakket oksekød
  - 500 g hakket svinekød
  - 100 g pancetta eller bacon i tern
  - 2 løg, 2 gulerødder, 2 stilke bladselleri — alle finthakkede
  - 4 fed hvidløg
  - 2 spsk tomatpuré
  - 2 dåser (á 400 g) hakkede tomater
  - 2 dl hel- eller semi-skummetmælk
  - 2 dl rødvin
  - 2 dl bouillon
  - 2 laurbærblade, 1 kvist rosmarin eller timian
  - 2 spsk olie
  - Salt, peber, parmesan, pasta til servering
steps:
  - Brun pancetta i støbejernet. Tilsæt kødet i portioner, og brun det hårdt. Tag op, hvis panden bliver for fuld.
  - Svits løg, gulerod og selleri 10–12 minutter i fedtet. Hvidløg og tomatpuré 1 minut.
  - Vin i — skrab bunden. Tomater, bouillon, krydderurter og kød tilbage. Bring i kog.
  - Skru helt ned. Låg på klem. Simre 2½–3 timer, rør jævnligt. Mælk i den sidste time.
  - Smag til. Server med pasta og parmesan — eller lad den køle og frys i portioner.
faq:
  - question: Forskel på almindelig bolognese?
    answer: Samme klassiker — her er støbejernet og den lange simretid pointen. Den bliver dybere end en 30-minutters hverdagssovs.
  - question: Hvorfor mælk?
    answer: Mælken runder syren fra tomaterne og gør kødet silkeagtigt. Det er klassisk i ægte bolognese.
  - question: Trykkoger?
    answer: Se bolognese i trykkoger, hvis du vil have genvejen. Smagen bliver god, men ikke helt den samme.
  - question: Kan den laves dagen før?
    answer: Ja — den bliver bedre overnight. Skum evt. fedt af, før du varmer op.
body: |
  One pot bolognese i støbejern er kødsovsen, der tager sig tid: hakket kød, soffritto, vin, mælk og timer på lav blus.

  Brun hårdt. Simre lavt. Mælk sent.

  Det er ikke hurtigmad — det er den sovs, pastaen er lavet til.
tip: Lad låget stå på klem, så væsken reducerer langsomt. For lukket låg giver en tyndere, mere «suppeagtig» sovs.
=====
'''


SCALAR_KEYS = {
    "title",
    "slug",
    "category",
    "description",
    "prepTime",
    "cookTime",
    "totalTime",
    "servings",
    "difficulty",
    "imageAlt",
    "featured",
}


def parse_block(block: str) -> dict:
    data: dict = {}
    mode = None
    body_lines: list[str] = []
    current_q = ""
    i = 0
    lines = block.strip().split("\n")
    while i < len(lines):
        line = lines[i]

        # Leave list modes when a new top-level key appears
        if mode in {"tags", "ingredients", "steps", "faq"} and ": " in line and not line.startswith(" "):
            mode = None

        if mode != "body" and line.startswith("tags:"):
            mode = "tags"
            data["tags"] = []
        elif mode != "body" and line.startswith("ingredients:"):
            mode = "ingredients"
            data["ingredients"] = []
        elif mode != "body" and line.startswith("steps:"):
            mode = "steps"
            data["steps"] = []
        elif mode != "body" and line.startswith("faq:"):
            mode = "faq"
            data["faq"] = []
        elif line.startswith("body: |"):
            mode = "body"
            body_lines = []
        elif line.startswith("tip: "):
            mode = None
            data["tip"] = line[5:]
        elif mode != "body" and ": " in line and not line.startswith(" "):
            key, _, val = line.partition(": ")
            if key in SCALAR_KEYS:
                data[key] = val
                mode = None
            elif key == "tip":
                mode = None
                data["tip"] = val
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
featured: false
ingredients:
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
    assert d.get("faq") and len(d["faq"]) >= 3, (d.get("slug"), len(d.get("faq", [])))
    assert d.get("tip"), d.get("slug")
    assert d.get("slug") and d.get("category"), d
    out = ROOT / d["category"]
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{d['slug']}.mdx"
    if path.exists():
        raise SystemExit(f"slug collision: {path}")
    path.write_text(to_mdx(d), encoding="utf-8")
    print("wrote", d["category"] + "/" + path.name)
