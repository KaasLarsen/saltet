#!/usr/bin/env python3
"""Vinter-comfort batch — gryder, supper, rodfrugt og sødt (okt 2026)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"
PUBLISHED = "2026-10-29"

RECIPES = r'''
=====
title: Vinter Bœuf Bourguignon
slug: vinter-boeuf-bourguignon
category: gryde
description: Klassisk fransk oksegryde simret i rødvin med perleløg, svampe og bacon — den ultimative vinter-simremad.
prepTime: PT40M
cookTime: PT3H
totalTime: PT3H40M
servings: 6
difficulty: mellem
tags:
  - bœuf bourguignon
  - bourguignon
  - oksekød
  - rødvin
  - gryderet
  - vinter
  - bacon
  - svampe
  - gryde
imageAlt: Dyb rødvinssauce med oksekød, perleløg, svampe og bacon i gryde
featured: true
ingredients:
  - 1,5 kg oksekød til gryderet (fx skulder), i 4 cm tern
  - 150 g bacon i tern
  - 2 spsk smør + 1 spsk olie
  - 2 store løg, hakket
  - 2 gulerødder, i skiver
  - 2 fed hvidløg
  - 2 spsk tomatpuré
  - 2 spsk hvedemel
  - 75 cl tør rødvin (pinot noir eller bordeaux)
  - 3 dl oksebouillon
  - 2 laurbærblade, 4 kviste timian
  - 250 g perleløg, skrællede
  - 300 g champignon, halverede
  - Salt, peber, persille
steps:
  - Dup kødet tørt. Salt og peber. Brun bacon i en tung gryde, tag op. Brun kødet i portioner i baconfedt, smør og olie. Tag op.
  - Svits løg og gulerod 8 minutter. Hvidløg og tomatpuré 1 minut. Drys mel over, rør 30 sekunder.
  - Hæld vin i, skrab bunden. Bouillon, laurbær og timian i. Læg kød og bacon tilbage. Bring i kog.
  - Simre med låg 2½–3 timer, til kødet er mørt. Rør jævnligt.
  - Brun perleløg og svampe i en pande med lidt smør. Rør dem i gryden de sidste 20 minutter.
  - Smag til. Persille. Server med kartoffelmos, pasta eller brød.
faq:
  - question: Hvilken vin?
    answer: Tør pinot noir eller en billig bordeaux. Undgå sød vin — den bliver klæg.
  - question: Kan den laves dagen før?
    answer: Ja. Bourguignon smager bedre dagen efter. Køl, og varm forsigtigt op.
  - question: Magert kød?
    answer: Brug skulder eller tykkam med lidt fedt. Filet bliver tør efter tre timer.
  - question: Perleløg frosne?
    answer: Ja — tø dem, og brun dem godt, så de mister vand.
body: |
  Bœuf Bourguignon er vinter i en gryde: oksekød, rødvin, bacon, perleløg og svampe.

  Brun hårdt. Vin ind. Simre længe.

  Det er ikke hurtigmad. Det er tålmodighed med belønning.
tip: Brun kødet i små portioner — overfyldt gryde damper i stedet for at brune.
=====
title: Ossobuco med gremolata
slug: ossobuco-gremolata
category: gryde
description: Langtidssimrede kalveskanke i tomatsauce med hvidvin — serveret med frisk gremolata til vinterbordet.
prepTime: PT30M
cookTime: PT2H30M
totalTime: PT3H
servings: 4
difficulty: mellem
tags:
  - ossobuco
  - kalveskank
  - gremolata
  - hvidvin
  - gryderet
  - vinter
  - italiensk
  - gryde
imageAlt: Møre kalveskanke i tomat-hvidvinssauce med gremolata ovenpå
featured: true
ingredients:
  - 4 kalveskanke (ossobuco), ca. 3–4 cm tykke
  - 3 spsk hvedemel til vendning
  - 2 spsk smør + 2 spsk olie
  - 1 løg, 1 gulerod, 1 stilk bladselleri — finthakket
  - 2 fed hvidløg
  - 2 spsk tomatpuré
  - 2 dl tør hvidvin
  - 400 g hakkede tomater
  - 3 dl kalve- eller hønsebouillon
  - 2 laurbærblade, 2 kviste rosmarin
  - Salt og peber
  - Gremolata: 1 citronskal, 1 fed hvidløg, 3 spsk hakkede bladpersille
steps:
  - Bind skankene med kødsnor, hvis de falder fra hinanden. Vend i mel, salt og peber. Brun i smør og olie på begge sider. Tag op.
  - Svits løg, gulerod og selleri 8–10 minutter. Hvidløg og tomatpuré 1 minut.
  - Hæld vin i, skrab bunden, kog 2 minutter. Tomater, bouillon, laurbær og rosmarin i.
  - Læg skankene tilbage. Simre med låg 2–2½ time, til kødet er mørt og glider fra benet.
  - Bland gremolata lige før servering. Drys over. Server med risotto, polenta eller kartoffelmos.
faq:
  - question: Kan jeg bruge okse i stedet?
    answer: Ja — oksehaler eller okseben med marv. Forlæng simretiden, til kødet er mørt.
  - question: Hvorfor gremolata?
    answer: Den friske citron, hvidløg og persille klipper den tunge sauce. Uden den mangler retten kant.
  - question: Marven?
    answer: Den er pointen. Skub den ud på brødet, eller rør den i saucen til sidst.
  - question: Ovnen i stedet?
    answer: Ja — 160 °C med låg i 2½ time efter den indledende bruning på komfuret.
body: |
  Ossobuco er kalveskank, der får lov at blive mørt i tomat, hvidvin og tid.

  Gremolataen er ikke pynt. Den er syre og friskhed mod den fede sauce.

  Server med noget, der kan samle saucen op.
tip: Bind skankene, før de brunnes — ellers falder kødet fra hinanden i gryden.
=====
title: Gullasch med kartoffelmos
slug: gullasch-kartoffelmos
category: gryde
description: Ungarsk inspireret gryderet med masser af paprika og møre oksekødstern — serveret med cremet kartoffelmos.
prepTime: PT25M
cookTime: PT2H
totalTime: PT2H25M
servings: 6
difficulty: mellem
tags:
  - gullasch
  - kartoffelmos
  - paprika
  - oksekød
  - gryderet
  - vinter
  - ungarsk
  - gryde
imageAlt: Rød gullasch med oksekød ved siden af cremet kartoffelmos
featured: true
ingredients:
  - 1,2 kg oksekød til gryderet, i tern
  - 3 store løg, hakket
  - 3 fed hvidløg
  - 3 spsk sødmefuld paprika
  - 1 tsk røget paprika
  - 2 spsk tomatpuré
  - 2 spsk hvedemel
  - 5 dl oksebouillon
  - 2 dl rødvin (valgfrit)
  - 2 laurbærblade
  - 2 spsk smør + 1 spsk olie
  - Salt, peber, persille
  - Kartoffelmos: 1 kg kartofler, 1 dl mælk, 50 g smør, salt
steps:
  - Brun kødet i portioner i smør og olie. Tag op. Svits løg 10 minutter. Hvidløg 1 minut.
  - Rør paprika og tomatpuré i på lav varme. Drys mel over. Bouillon og vin i under omrøring.
  - Læg kød og laurbær tilbage. Simre med låg 1½–2 timer, til kødet er mørt.
  - Kog kartofler møre. Mos med smør og varm mælk. Salt.
  - Smag gullaschen til. Server over eller ved siden af mosen. Persille.
faq:
  - question: Hvilket kød?
    answer: Skulder, tykkam eller grydestykker. Magert filetkød bliver tørt.
  - question: Bitter paprika?
    answer: Tilsæt paprika på lav varme, og lad den ikke brænde. Brug frisk, god paprika.
  - question: Kan mosen laves på forhånd?
    answer: Ja — varm op med ekstra mælk og smør, så den ikke bliver tør.
  - question: Mere sauce?
    answer: Tilsæt bouillon undervejs. Gullasch skal være dyb, ikke vandig.
body: |
  Gullasch med kartoffelmos er paprika, mørt kød og blød mos på samme tallerken.

  Brun kødet. Vågn paprikaen forsigtigt. Simre.

  Mosen er ikke tilbehør — den er den anden halvdel af retten.
tip: Brug sødmefuld paprika som base og kun en knivspids røget — for meget røg stjæler den klassiske smag.
=====
title: Skipperlabskovs med purløg
slug: skipperlabskovs-purloeg
category: gryde
description: Klassisk dansk herreret med sprængt oksekød, kartofler og masser af frisk purløg — vintermad fra mormors gryde.
prepTime: PT20M
cookTime: PT1H30M
totalTime: PT1H50M
servings: 6
difficulty: nem
tags:
  - skipperlabskovs
  - labskovs
  - sprængt oksekød
  - kartofler
  - purløg
  - dansk
  - vinter
  - gryde
imageAlt: Tykk skipperlabskovs med kartofler, oksekød og purløg ovenpå
featured: true
ingredients:
  - 800 g sprængt oksekød (eller kogt oksekød), i tern
  - 1,2 kg kartofler, skrællet og i store tern
  - 2 store løg, hakket
  - 50 g smør
  - 8–10 dl oksebouillon (eller kogevand fra kødet)
  - 2 laurbærblade
  - Friskkværnet peber
  - 1 stor bundt purløg, hakket
  - Sennep og rugbrød til servering
steps:
  - Smelt smør i en tung gryde. Svits løg bløde uden farve, ca. 8 minutter.
  - Læg kartofler, kød og laurbær i. Hæld bouillon over, så det næsten dækker.
  - Bring i kog, skru ned. Simre med låg 1–1½ time, til kartoflerne er helt møre og begynder at gå i opløsning.
  - Rør kraftigt, så retten bliver tyk og cremet — ikke en klar suppe. Peber. Salt kun hvis kødet ikke er salt nok.
  - Rør masser af purløg i lige før servering. Sennep og rugbrød ved siden af.
faq:
  - question: Sprængt eller kogt kød?
    answer: Sprængt giver den klassiske saltede smag. Kogt oksekød virker også — smag til med salt.
  - question: For tynd?
    answer: Simre uden låg de sidste 15 minutter, og mos flere kartofler ind i saucen.
  - question: Kan den fryses?
    answer: Ja. Tø op i køleskab, og varm op med lidt ekstra bouillon og frisk purløg.
  - question: Purløg erstattes med?
    answer: Forårsløg eller bladselleri-toppe i nød. Men purløg er den danske signatur.
body: |
  Skipperlabskovs er herreret: sprængt oksekød, kartofler, løg og tålmodighed.

  Den skal være tyk. Næsten som en mos med kød i.

  Purløget er det grønne spark, der gør den færdig.
tip: Rør hårdt til sidst — kartoflerne skal delvist gå i opløsning og jævne retten selv.
=====
title: Coq au Vin til vinteren
slug: coq-au-vin-vinter
category: gryde
description: Kylling i rødvinssauce med timian, svampe og bacon — fransk simremad, der varmer på kolde aftener.
prepTime: PT30M
cookTime: PT1H15M
totalTime: PT1H45M
servings: 4
difficulty: mellem
tags:
  - coq au vin
  - kylling
  - rødvin
  - bacon
  - svampe
  - timian
  - vinter
  - gryde
imageAlt: Kyllingestykker i dyb rødvinssauce med svampe, bacon og timian
featured: true
ingredients:
  - 1 hel kylling, skåret i 8, eller 1,2 kg kyllingelår
  - 150 g bacon i tern
  - 2 spsk smør + 1 spsk olie
  - 200 g perleløg eller 2 almindelige løg i både
  - 300 g champignon, halverede
  - 2 fed hvidløg
  - 2 spsk hvedemel
  - 5 dl tør rødvin
  - 2 dl hønsebouillon
  - 2 laurbærblade, 4 kviste timian
  - Salt, peber, persille
steps:
  - Brun bacon, tag op. Brun kylling i fedtet, til skindet er gyldent. Tag op.
  - Svits løg og svampe 8 minutter. Hvidløg 1 minut. Drys mel over.
  - Hæld vin i, skrab bunden. Bouillon, laurbær og timian i. Læg kylling og bacon tilbage.
  - Simre med låg 45–60 minutter, til kyllingen er gennemstegt og saucen er tyknet.
  - Smag til. Persille. Server med kartoffelmos, pasta eller brød.
faq:
  - question: Hvidvin i stedet?
    answer: Så er det mere coq au riesling. Det virker, men smagen bliver lysere og syrligere.
  - question: Bryst eller lår?
    answer: Lår og lårben holder bedre til simring. Bryst bliver let tørt.
  - question: Kan den laves dagen før?
    answer: Ja. Varm forsigtigt op, og tilsæt lidt bouillon hvis saucen er for tyk.
  - question: Alkoholfri?
    answer: Brug ekstra bouillon og 1 spsk rødvinseddike til syre. Det er ikke det samme, men det virker.
body: |
  Coq au Vin er kylling, der får lov at smage af vin, bacon og svampe.

  Brun skindet. Vin ind. Timian på.

  Server med noget stivelsesholdigt — saucen fortjener det.
tip: Dup kyllingen tør før bruning. Vådt skind steger ikke sprødt.
=====
title: Klassisk mørbradgryde
slug: klassisk-moerbradgryde
category: gryde
description: Svinemørbrad i flødesovs med cocktailpølser, bacon og svampe — den danske vintergryde alle kender.
prepTime: PT20M
cookTime: PT35M
totalTime: PT55M
servings: 4
difficulty: nem
tags:
  - mørbradgryde
  - svinemørbrad
  - flødesovs
  - bacon
  - cocktailpølser
  - svampe
  - vinter
  - gryde
imageAlt: Cremet mørbradgryde med bacon, cocktailpølser og svampe
featured: true
ingredients:
  - 600 g svinemørbrad, i skrå skiver
  - 100 g bacon i tern
  - 1 dåse cocktailpølser (ca. 200 g), dryppet
  - 250 g champignon, skivede
  - 1 stort løg, hakket
  - 1 fed hvidløg
  - 1 spsk smør + 1 spsk olie
  - 1 spsk hvedemel
  - 2 dl hønsebouillon
  - 2½ dl piskefløde
  - 1 tsk dijonsennep
  - 1 tsk timian
  - Salt, peber, persille
steps:
  - Brun bacon sprødt. Tag op. Brun cocktailpølser let, tag op. Brun mørbrad i portioner — farve, ikke gennemstegning. Tag op.
  - Svits løg 5 minutter. Svampe i, til væsken er væk. Hvidløg 30 sekunder.
  - Drys mel over. Bouillon i under omrøring. Fløde, sennep og timian i.
  - Læg kød, bacon og pølser tilbage. Simre 8–10 minutter under låg, til mørbraden er netop færdig.
  - Smag til. Persille. Server med kartoffelmos eller ris.
faq:
  - question: Bliver mørbraden tør?
    answer: Brun kort, og simre kun til den er gennemstegt. Overkogt mørbrad er tyggegummi.
  - question: Uden cocktailpølser?
    answer: Brug wienerpølser eller medister i skiver. Eller drop dem — bacon og svampe bærer smagen.
  - question: Lettere version?
    answer: Brug madlavningsfløde 9 %. Saucen bliver tyndere — jævn med lidt ekstra mel.
  - question: Kan den laves i ovnen?
    answer: Ja efter saucen er samlet — 160 °C i 20 minutter med låg.
body: |
  Klassisk mørbradgryde er fløde, bacon, pølser og svampe omkring møre mørbradskiver.

  Det er ikke fin. Det er vinterhygge i grydeform.

  Kartoffelmos er den korrekte makker.
tip: Tag mørbraden op, når den er brun — den færdigsimrer i saucen på få minutter.
=====
title: Gule ærter med flæsk og pølse
slug: gule-aerter-flaesk-poelse
category: gryde
description: Tyk, mættende vintersuppe af gule ærter — serveret med flæsk, pølse og sennep på den klassiske måde.
prepTime: PT20M
cookTime: PT2H
totalTime: PT2H20M
servings: 6
difficulty: nem
tags:
  - gule ærter
  - flæsk
  - pølse
  - vintersuppe
  - dansk
  - sennep
  - vinter
  - gryde
imageAlt: Tyk gule ærter-suppe med flæsk og pølse på tallerkenen
featured: true
ingredients:
  - 500 g tørrede gule ærter, udblødt natten over
  - 500 g saltet sidestykke eller kogeflæsk
  - 2 medisterpølser eller røgede pølser
  - 2 løg, hakket
  - 2 gulerødder, i skiver
  - 1 porre, i skiver
  - 2 laurbærblade
  - 2½ liter vand
  - Salt, peber, timian
  - Sennep og rugbrød til servering
steps:
  - Skyl de udblødte ærter. Læg dem i en stor gryde med vand, løg, gulerod, porre, laurbær og flæsk.
  - Bring i kog, skum af. Simre med låg 1½–2 timer, til ærterne er helt møre.
  - Tag flæsket op. Blend eller mos ærterne til en tyk suppe (eller mos kun halvdelen for tekstur).
  - Skær flæsket i skiver. Kog pølserne i saucen de sidste 15 minutter, eller steg dem separat.
  - Smag til. Server med flæsk, pølseskiver, sennep og rugbrød.
faq:
  - question: Uden udblødning?
    answer: Det kan lade sig gøre, men forlæng kogetiden markant. Udblødning giver jævnere konsistens.
  - question: For tynd?
    answer: Simre uden låg, eller blend flere ærter. Gule ærter skal næsten kunne stå på skeen.
  - question: Vegetarisk?
    answer: Drop flæsk og pølse. Brug grøntsagsbouillon og røget paprika for dybde.
  - question: Kan den fryses?
    answer: Ja i portioner. Den tykner i fryseren — fortynd med vand ved opvarmning.
body: |
  Gule ærter er dansk vintersuppe i dens tungeste form: ærter, flæsk, pølse, sennep.

  Udblød. Simre. Mos.

  Det er ikke elegant. Det er mættende.
tip: Salt først til sidst — flæsket og pølsen bærer allerede salt.
=====
title: Kartoffel-porresuppe
slug: kartoffel-porresuppe
category: gryde
description: Cremet og mild kartoffel-porresuppe — perfekt med sprød bacon og purløg på toppen til kolde dage.
prepTime: PT15M
cookTime: PT35M
totalTime: PT50M
servings: 4
difficulty: nem
tags:
  - kartoffel-porresuppe
  - porresuppe
  - kartoffel
  - bacon
  - cremet
  - vinter
  - suppe
  - gryde
imageAlt: Cremet kartoffel-porresuppe toppet med sprød bacon og purløg
featured: true
ingredients:
  - 500 g kartofler, skrællet og i tern
  - 3 porrer (kun det hvide og lysegrønne), i skiver
  - 1 løg, hakket
  - 2 fed hvidløg
  - 40 g smør
  - 1 liter hønse- eller grøntsagsbouillon
  - 2 dl piskefløde
  - 100 g bacon i tern
  - Salt, peber, muskatnød
  - Purløg til topping
steps:
  - Steg bacon sprødt. Tag op, og gem fedtet.
  - Smelt smør i gryden (gerne med lidt baconfedt). Svits løg og porre 10 minutter uden farve.
  - Hvidløg 30 sekunder. Kartofler og bouillon i. Bring i kog, simre 20 minutter til kartoflerne er møre.
  - Blend glat. Rør fløde i. Smag til med salt, peber og en knivspids muskat.
  - Server med bacon og purløg ovenpå.
faq:
  - question: Uden fløde?
    answer: Brug ekstra kartoffel og en klaps smør. Den bliver stadig cremet efter blending.
  - question: Grønne porretoppe?
    answer: De kan bittert. Brug dem til fond, ikke i den milde suppe.
  - question: Kan den fryses?
    answer: Ja før fløden. Tilsæt fløde ved opvarmning for bedst konsistens.
  - question: Airfryer-bacon?
    answer: Ja — 180 °C i 8–10 minutter. Samme sprødhed, mindre fedtstænk.
body: |
  Kartoffel-porresuppe er vinterens milde skål: blød porre, kartoffel og fløde.

  Bacon ovenpå er ikke obligatorisk. Det er bare korrekt.

  Blend den helt glat — det er den cremede fornemmelse, der gør den.
tip: Svits porrerne længe uden farve. Den søde, milde smag kommer derfra — ikke fra fløden alene.
=====
title: Vinter fransk løgsuppe
slug: vinter-fransk-loegsuppe
category: gryde
description: Intens fransk løgsuppe på karamelliserede løg — gratineret med ostegrillede brødcroutoner til frostvejret.
prepTime: PT20M
cookTime: PT1H10M
totalTime: PT1H30M
servings: 4
difficulty: mellem
tags:
  - fransk løgsuppe
  - løgsuppe
  - gratinering
  - ost
  - brød
  - vinter
  - suppe
  - gryde
imageAlt: Fransk løgsuppe i skål med ostegratineret brød ovenpå
featured: true
ingredients:
  - 1 kg gule løg, tyndt skivede
  - 50 g smør + 1 spsk olie
  - 1 tsk sukker
  - 2 fed hvidløg
  - 2 spsk hvedemel
  - 2 dl tør hvidvin
  - 1,2 liter oksebouillon
  - 2 laurbærblade, 2 kviste timian
  - 4 skiver groft brød
  - 150 g Gruyère eller emmentaler, revet
  - Salt, peber
steps:
  - Smelt smør og olie i en tung gryde. Svits løg på middel varme 35–45 minutter under omrøring, til de er dybt gyldne. Sukker de sidste 5 minutter.
  - Hvidløg 30 sekunder. Drys mel over. Vin i, skrab bunden. Bouillon, laurbær og timian i.
  - Simre 20–25 minutter. Smag til.
  - Læg brød i ovnfaste skåle eller ovenpå suppen i et fad. Drys ost over.
  - Gratinér under grill 3–5 minutter, til osten bobler og er gylden. Server straks.
faq:
  - question: Hvorfor tager løgene så lang tid?
    answer: Karamellisering er smagen. Hastværk giver søde, men flade løg.
  - question: Vegetarisk bouillon?
    answer: Ja — brug kraftig grøntsagsbouillon og lidt soja til umami.
  - question: Osten?
    answer: Gruyère er klassisk. Emmentaler eller en god dansk bjergost virker også.
  - question: Uden vin?
    answer: Brug ekstra bouillon og 1 spsk sherryeddike til syre.
body: |
  Fransk løgsuppe er tålmodighed: løg, der bliver brune, søde og dybe.

  Osten på brødet er finalen. Den skal boble.

  Det er den mest luxuriøse måde at spise løg på.
tip: Brug en bred gryde, så løgene har plads til at karamellisere i stedet for at dampe.
=====
title: Tomatsuppe med bagte peberfrugter
slug: tomatsuppe-bagte-peberfrugter
category: gryde
description: Fyldig vinter-tomatsuppe med bagte peberfrugter, masser af hvidløg og fløde — sødere og dybere end sommerudgaven.
prepTime: PT20M
cookTime: PT50M
totalTime: PT1H10M
servings: 4
difficulty: nem
tags:
  - tomatsuppe
  - peberfrugt
  - bagte peberfrugter
  - fløde
  - hvidløg
  - vinter
  - suppe
  - gryde
imageAlt: Cremet rød tomatsuppe med bagte peberfrugter og et skvæt fløde
featured: true
ingredients:
  - 3 røde peberfrugter
  - 1 kg modne tomater eller 2 dåser hakkede tomater (à 400 g)
  - 1 løg, hakket
  - 4 fed hvidløg
  - 2 spsk olivenolie + 1 spsk smør
  - 1 spsk tomatpuré
  - 7 dl grøntsags- eller hønsebouillon
  - 1 dl piskefløde
  - 1 tsk sukker
  - 1 tsk tørret oregano
  - Salt, peber, basilikum eller persille
steps:
  - Del peberfrugter, fjern kerner. Bag ved 220 °C i 25–30 minutter, til skindet er sortplettet. Læg i pose 10 minutter, træk skindet af.
  - Svits løg i olie og smør 8 minutter. Hvidløg og tomatpuré 1 minut.
  - Tomater, bagte peberfrugter, bouillon, oregano og sukker i. Simre 20 minutter.
  - Blend glat. Rør fløde i. Smag til.
  - Server med brød, basilikum eller et ekstra skvæt fløde.
faq:
  - question: Dåsetomater?
    answer: Ja — om vinteren er de ofte bedre end blege friske. Vælg gode San Marzano-agtige.
  - question: Uden fløde?
    answer: Blend en kogt kartoffel i for cremethed, eller server den ren og syrlig.
  - question: Kan peberfrugterne grilles?
    answer: Ja — på gasblus eller grill, til skindet bobler. Samme trick.
  - question: Krydderi?
    answer: Lidt chiliflager giver varme uden at stjæle den søde peberfrugt-smag.
body: |
  Tomatsuppe med bagte peberfrugter er vinterudgaven: sødere, dybere, mere hvidløg.

  Bag peberfrugterne først. Det er forskellen.

  Fløden lukker smagen uden at gøre den tung.
tip: Træk skindet af peberfrugterne — ellers bliver suppen bitter og med strenge.
=====
title: Linsesuppe med chorizotern
slug: linsesuppe-chorizo
category: gryde
description: Krydret og proteinrig linsesuppe med chorizotern — giver varmen på kolde dage uden at være tung.
prepTime: PT15M
cookTime: PT40M
totalTime: PT55M
servings: 4
difficulty: nem
tags:
  - linsesuppe
  - chorizo
  - linser
  - paprika
  - protein
  - vinter
  - suppe
  - gryde
imageAlt: Rødlig linsesuppe med chorizotern og frisk persille
featured: true
ingredients:
  - 250 g tørrede grønne eller brune linser, skyllede
  - 150 g chorizo, i små tern
  - 1 løg, hakket
  - 2 gulerødder, i tern
  - 2 stilke bladselleri, i tern
  - 3 fed hvidløg
  - 1 spsk tomatpuré
  - 1 tsk røget paprika
  - 1 tsk spidskommen
  - 1,2 liter grøntsags- eller hønsebouillon
  - 1 dåse hakkede tomater (400 g)
  - 1 spsk olivenolie
  - Salt, peber, citronsaft, persille
steps:
  - Steg chorizo i en gryde, til fedtet smelter ud. Tag noget chorizo op til topping.
  - Svits løg, gulerod og selleri i chorizofedtet 8 minutter. Hvidløg, tomatpuré, paprika og spidskommen 1 minut.
  - Linser, tomater og bouillon i. Bring i kog, simre 30–35 minutter, til linserne er møre.
  - Smag til med salt, peber og citronsaft. Evt. blend en øse for mere fylde.
  - Server med chorizotern og persille ovenpå.
faq:
  - question: Røde linser?
    answer: De koges hurtigere og bliver mere mosede. Brug dem, hvis du vil have en cremet variant.
  - question: Mild chorizo?
    answer: Ja — eller pepperoni. Røget paprika redder dybden, hvis pølsen er mild.
  - question: Kan den fryses?
    answer: Ja. Den tykner — fortynd med bouillon ved opvarmning.
  - question: Uden kød?
    answer: Drop chorizo, og tilsæt ekstra røget paprika plus et skvæt soja.
body: |
  Linsesuppe med chorizo er protein, paprika og varme i samme skål.

  Chorizofedtet er smagsbasen. Brug det.

  En skvæt citron til sidst løfter det hele.
tip: Salt sent — chorizo og bouillon kan allerede være salte nok.
=====
title: Brændende kærlighed med rødbeder
slug: braendende-kaerlighed-roedbeder
category: gryde
description: Luftig kartoffelmos toppet med stegte bacontern, løg og syltede rødbeder — den danske vinterklassiker.
prepTime: PT20M
cookTime: PT30M
totalTime: PT50M
servings: 4
difficulty: nem
tags:
  - brændende kærlighed
  - kartoffelmos
  - bacon
  - rødbeder
  - løg
  - dansk
  - vinter
  - gryde
imageAlt: Kartoffelmos med stegt bacon, løg og syltede rødbeder ovenpå
featured: true
ingredients:
  - 1 kg kartofler, skrællet
  - 1 dl mælk
  - 50 g smør
  - 200 g bacon i tern
  - 2 store løg, i tynde ringe
  - 1 glas syltede rødbeder, dryppet og i skiver
  - Salt, peber, muskatnød
  - Evt. frisk persille
steps:
  - Kog kartoflerne møre i saltet vand. Hæld vandet fra. Mos med smør og varm mælk. Salt, peber, muskat.
  - Steg bacon sprødt i en pande. Tag op. Steg løgringene i baconfedtet, til de er bløde og gyldne.
  - Læg mosen på tallerkener i en høj bunke. Top med bacon og løg.
  - Læg rødbedeskiver ved siden af eller ovenpå. Persille hvis du vil.
faq:
  - question: Hvorfor rødbeder?
    answer: Syre og sødme mod det fede bacon. Uden dem mangler retten kontrast.
  - question: Kan mosen laves på forhånd?
    answer: Ja — varm op med ekstra mælk, så den bliver luftig igen.
  - question: Flæskesteg-rester?
    answer: Stegte flæsketern virker også. Det er stadig brændende kærlighed i ånden.
  - question: Homemade rødbeder?
    answer: Endnu bedre. Sylt dem dagen før med eddike, sukker og nellike.
body: |
  Brændende kærlighed er kartoffelmos, bacon, løg og rødbeder — ikke mere, ikke mindre.

  Mosen skal være luftig. Baconet sprødt. Rødbederne syrlige.

  Det er dansk vinter på en tallerken.
tip: Steg løgene i baconfedtet — det er den smag, der binder retten sammen.
=====
title: Stuvet hvidkål med medister
slug: stuvet-hvidkaal-medister
category: gryde
description: Klassisk mormormad — stuvet hvidkål i mild hvid sauce serveret med stegt medister til vinteraftenen.
prepTime: PT20M
cookTime: PT40M
totalTime: PT1H
servings: 4
difficulty: nem
tags:
  - stuvet hvidkål
  - hvidkål
  - medister
  - stuvning
  - mormormad
  - dansk
  - vinter
  - gryde
imageAlt: Stuvet hvidkål i hvid sauce med stegte medisterpølser
featured: true
ingredients:
  - 1 lille hvidkål (ca. 800 g), snittet fint
  - 40 g smør
  - 3 spsk hvedemel
  - 5 dl mælk
  - 1 dl hønsebouillon eller kålvand
  - 1 tsk sukker
  - 1 knivspids muskatnød
  - Salt og peber
  - 600 g medisterpølse
  - 1 spsk olie til stegning
steps:
  - Kog den snittede hvidkål 8–10 minutter i let saltet vand, til den er mør men ikke grød. Hæld fra, gem 1 dl vand.
  - Smelt smør i en gryde. Rør mel i til en hvid roux. Tilsæt mælk og kålvand under piskning, til saucen er glat.
  - Rør kål i. Sukker, muskat, salt og peber. Simre 10 minutter under omrøring.
  - Steg medisteren i olie på panden, til den er gennemstegt og har god skorpe. Skær i skiver.
  - Server stuvningen med medister og evt. kogte kartofler.
faq:
  - question: Spidskål i stedet?
    answer: Ja — den er mildere og koges hurtigere. Kort kogetid, så den ikke bliver grød.
  - question: Klumper i saucen?
    answer: Pisk koldt mælk i den varme roux lidt ad gangen. Brug piskeris.
  - question: Medister i ovnen?
    answer: 180 °C i 25–30 minutter. Vend undervejs for jævn skorpe.
  - question: Kan stuvningen laves dagen før?
    answer: Ja. Den tykner — fortynd med mælk ved opvarmning.
body: |
  Stuvet hvidkål med medister er mormorkøkken: mild sauce, blød kål, stegt pølse.

  Det er ikke trendy. Det er vinter.

  Kartofler ved siden af gør tallerkenen komplet.
tip: Kog kålen kun til den netop er mør — overkogt hvidkål lugter og smager af skolekøkken.
=====
title: Risengrød med smørklat
slug: risengrod-smoerklat
category: gryde
description: Den hyggeligste spise til kolde vinteraftener — risengrød med smørklat, kanelsukker og gerne et glas hvidtøl.
prepTime: PT5M
cookTime: PT50M
totalTime: PT55M
servings: 4
difficulty: nem
tags:
  - risengrød
  - grød
  - kanelsukker
  - smør
  - hvidtøl
  - dansk
  - vinter
  - gryde
imageAlt: Skål risengrød med smørklat og kanelsukker ovenpå
featured: true
ingredients:
  - 2 dl grødris
  - 2 dl vand
  - 1 liter sødmælk
  - 1 tsk salt
  - 1 vaniljestang eller 1 tsk vaniljesukker
  - Smørklatter til servering
  - Kanelsukker: 3 spsk sukker + 1 tsk kanel
steps:
  - Kog ris og vand op i en tung gryde under omrøring, til vandet er opsuget.
  - Tilsæt mælk og vanilje. Bring næsten i kog under hyppig omrøring.
  - Skru helt ned. Simre 40–50 minutter under låg, rør jævnligt så det ikke brænder på.
  - Smag til med salt. Grøden skal være cremet og tyk.
  - Server med en generøs smørklat og kanelsukker. Hvidtøl ved siden af er klassisk.
faq:
  - question: Brænder den på?
    answer: Brug tung gryde, lav varme og rør tit — især i bunden. Et diffusorplade hjælper.
  - question: Resten dagen efter?
    answer: Lav klatkager, eller fortynd med mælk til ny grød. Risalamande kræver kold grød.
  - question: Plantemælk?
    answer: Havre- eller sojamælk virker, men smagen bliver anderledes. Sødmælk er klassikeren.
  - question: Kan den laves i ovnen?
    answer: Ja — 150 °C i ca. 1½ time i ovnfast fad med låg. Rør undervejs.
body: |
  Risengrød med smørklat er vinterhygge uden filter.

  Langsom mælk. Lav varme. Rør.

  Kanelsukkeret og smørret er ikke tilbehør — de er retten.
tip: Salt først til sidst. For tidligt salt kan gøre mælken mere tilbøjelig til at skille.
=====
title: Grønkålssalat med granatæble
slug: groenkaalssalat-granataeble
category: pande
description: Frisk vintersalat med fintsnittet grønkål, valnødder, appelsin, granatæble og mormordressing.
prepTime: PT20M
cookTime: PT5M
totalTime: PT25M
servings: 4
difficulty: nem
tags:
  - grønkålssalat
  - grønkål
  - granatæble
  - valnødder
  - appelsin
  - salat
  - vinter
  - pande
imageAlt: Grønkålssalat med granatæblekerner, valnødder og appelsin
featured: false
ingredients:
  - 200 g grønkål, stilke fjernet, fintsnittet
  - 1 granatæble, kerner
  - 2 appelsiner, fileteret
  - 75 g valnødder
  - 50 g revet parmesan (valgfrit)
  - Dressing: 3 spsk olivenolie, 1 spsk æblecidereddike, 1 tsk dijon, 1 tsk honning, salt, peber
steps:
  - Massage grønkålen med en knivspids salt og 1 spsk af dressingen i 2–3 minutter, til den bliver blødere og mørkere.
  - Rist valnødderne let på en tør pande, til de dufter. Hak groft.
  - Pisk resten af dressingen sammen.
  - Vend grønkål med appelsin, granatæblekerner, valnødder og dressing.
  - Top med parmesan hvis du vil. Server straks eller efter 10 minutters hvil.
faq:
  - question: Hvorfor massegrønkål?
    answer: Det knækker fibrene, så salaten ikke er sejt træ. To minutter gør forskellen.
  - question: Uden granatæble?
    answer: Brug tørrede tranebær eller ekstra appelsin. Du mister den sprøde syre.
  - question: Kan den laves i forvejen?
    answer: Ja op til 4 timer. Hold kerner og nødder separate til sidst for sprødhed.
  - question: Mormordressing?
    answer: Olie, eddike, sennep, honning — den søde-syrlige klassiker til vintergrønt.
body: |
  Grønkålssalat med granatæble er den friske pause mellem gryderetterne.

  Massage kålen. Rist nødderne. Dressing på.

  Granatæblekernerne er de små syrlige juveler.
tip: Fjern de tykke midterstokke — de er bitre og seje, uanset hvor meget du masserer.
=====
title: Pandekager med appelsinsauce
slug: crepes-suzette
category: pande
description: Varme pandekager i en rig, lun orangesauce — Crepes Suzette som vinterhygge til dessertbordet.
prepTime: PT15M
cookTime: PT25M
totalTime: PT40M
servings: 4
difficulty: mellem
tags:
  - crepes suzette
  - pandekager
  - appelsinsauce
  - dessert
  - orange
  - vinter
  - pande
imageAlt: Tynde pandekager i skinnende appelsinsauce med appelsinskiver
featured: true
ingredients:
  - Pandekager: 2 dl hvedemel, 3 æg, 4 dl mælk, 1 spsk sukker, 1 knivspids salt, 30 g smeltet smør
  - Sauce: 75 g smør, 75 g sukker, saft og skal af 2 appelsiner, saft af ½ citron
  - 2 spsk Grand Marnier eller Cointreau (valgfrit)
  - Ekstra appelsinskiver til servering
steps:
  - Pisk pandekagedej sammen. Hvil 15 minutter. Bag tynde pandekager på en varm pande med lidt smør. Hold varme.
  - Smelt smør og sukker i en bred pande. Tilsæt appelsinsaft, skal og citronsaft. Kog til en tyk, blank sauce.
  - Læg pandekagerne foldet i saucen, eller dyp dem en ad gangen. Vend dem, så de suger smag.
  - Flambér med Grand Marnier hvis du vil — eller rør likøren i uden flamme.
  - Server straks med ekstra appelsinskiver.
faq:
  - question: Uden alkohol?
    answer: Drop likøren. Appelsin og smør bærer smagen. En teskefuld vanilje hjælper.
  - question: Kan pandekagerne bages i forvejen?
    answer: Ja. Stabl med bagepapir imellem, og varm dem i saucen.
  - question: Tynde eller tykke?
    answer: Tynde crepes er klassisk. Tykkere danske pandekager virker også — fold dem mindre.
  - question: Blodappelsin?
    answer: Smukt og syrligt om vinteren. Brug samme mængde saft.
body: |
  Crepes Suzette er pandekager, der får lov at svømme i lun orangesauce.

  Det dufter af vinterdessert. Det smager af smør og citrus.

  Flambering er show. Saucen er substansen.
tip: Bag pandekagerne tynde — tykke pandekager suger dårligt og bliver tungere i saucen.
=====
title: Flæskesteg med rødkål
slug: flaeskesteg-med-roedkaal
category: ovn
description: Den ultimative vinterklassiker — flæskesteg med sprød svær, brunede kartofler og hjemmelavet rødkål.
prepTime: PT30M
cookTime: PT1H45M
totalTime: PT2H15M
servings: 6
difficulty: mellem
tags:
  - flæskesteg
  - rødkål
  - svær
  - stegt flæsk
  - dansk
  - søndagsmad
  - vinter
  - ovn
imageAlt: Flæskesteg med sprød svær, rødkål og brunede kartofler
featured: true
ingredients:
  - 1,5–2 kg flæskesteg med svær
  - Groft salt
  - 3 dl vand til bradepanden
  - Rødkål: 1 kg rødkål snittet, 2 æbler, 2 dl solbærsaft eller rødvin, 3 spsk eddike, 3 spsk sukker, 1 spsk smør, salt, peber, 2 nelliker
  - Brunede kartofler eller kogte kartofler til servering
steps:
  - Rid sværen i fine striber ned til kødet — ikke igennem. Gnid groft salt ned i alle riller. Lad gerne trække 30 minutter.
  - Læg stegen på rist over bradepande med vand. Ovn 200 °C i ca. 1 time 20 minutter (kernetemperatur ca. 65–68 °C). Grill sværen sprød de sidste minutter hvis nødvendigt.
  - Rødkål: svits kål og æble i smør. Saft, eddike, sukker, nelliker i. Simre 45–60 minutter under låg. Smag til.
  - Hvile stegen 10–15 minutter før udskæring.
  - Server med rødkål, kartofler og sky fra bradepanden.
faq:
  - question: Blød svær?
    answer: Sværen skal være tør og saltet i rillerne. Afslut under grill, og hold øje — den brænder hurtigt.
  - question: Færdig rødkål fra glas?
    answer: Det virker i nød. Hjemmelavet smager dybere og mindre sødt.
  - question: Kernetemperatur?
    answer: Tag den ud ved ca. 65 °C. Den stiger under hvilen.
  - question: Kan rødkålen laves dagen før?
    answer: Ja — den smager ofte bedre dagen efter. Varm forsigtigt op.
body: |
  Flæskesteg med rødkål er den danske vintertallerken: sprød svær, mørt kød, syrlig-sød kål.

  Salt i rillerne. Tør svær. Tålmodighed i ovnen.

  Rødkålen er ikke tilbehør — den er kontrasten.
tip: Dup sværen helt tør før salt — fugt er fjenden af sprødhed.
=====
title: Rodfrugtsfad med timian og honning
slug: rodfrugtsfad-timian-honning
category: ovn
description: Bagte rødbeder, gulerødder, pastinakker og selleri vendt i honning, olie og timian — vintergrønt i fad.
prepTime: PT20M
cookTime: PT45M
totalTime: PT1H5M
servings: 4
difficulty: nem
tags:
  - rodfrugtsfad
  - rodfrugter
  - timian
  - honning
  - rødbeder
  - pastinak
  - vinter
  - ovn
imageAlt: Fad med bagte rodfrugter glaseret med honning og timian
featured: false
ingredients:
  - 3 rødbeder, skrællet og i både
  - 4 gulerødder, i store stykker
  - 3 pastinakker, i stykker
  - ½ knoldselleri, i tern
  - 3 spsk olivenolie
  - 1½ spsk honning
  - 4 kviste frisk timian (eller 1 tsk tørret)
  - 1 tsk groft salt
  - Friskkværnet peber
  - Evt. 1 spsk balsamico til sidst
steps:
  - Varm ovnen til 200 °C. Vend alle rodfrugter med olie, honning, timian, salt og peber.
  - Fordel i ét lag på en bradepande beklædt med bagepapir. Rødbeder kan ligge for sig, hvis du vil undgå farvesmitte.
  - Bag 40–50 minutter. Vend halvvejs. De skal være møre og have mørke kanter.
  - Dryp evt. balsamico over lige før servering.
  - Server som tilbehør til stege, eller som hovedret med feta og brød.
faq:
  - question: Rå rødbeder farver alt?
    answer: Bag dem på separat bakke, eller accepter den røde farve — den smager stadig godt.
  - question: Uden honning?
    answer: Brug ahornsirup eller et skvæt æblemost. Sødmen hjælper karamelliseringen.
  - question: Airfryer?
    answer: Ja i portioner — 180 °C i 20–25 minutter. Ryst undervejs.
  - question: Kan det laves i forvejen?
    answer: Ja. Varm op i ovnen 10 minutter ved 180 °C, så kanterne bliver sprøde igen.
body: |
  Rodfrugtsfad med timian og honning er vintergrønt, der får lov at blive sødt og karamelliseret.

  Ét lag. Høj varme. Vend undervejs.

  Det er tilbehør, der stjæler billedet.
tip: Skær stykkerne nogenlunde ens, ellers er pastinakken brændt, mens sellerien stadig er hård.
=====
title: Gammeldags æblekage
slug: gammeldags-aeblekage
category: ovn
description: Gammeldags æblekage med rystede æbler, makroner og en generøs mængde flødeskum — klassisk dansk vinterdessert.
prepTime: PT25M
cookTime: PT20M
totalTime: PT45M
servings: 6
difficulty: nem
tags:
  - gammeldags æblekage
  - æblekage
  - makroner
  - flødeskum
  - dessert
  - dansk
  - vinter
  - ovn
imageAlt: Lagkage-agtig gammeldags æblekage med makroner og flødeskum
featured: true
ingredients:
  - 1 kg syrlige æbler, skrællet og i både
  - 100 g sukker (til æbler) + ekstra efter smag
  - 1 tsk vaniljesukker
  - 1 knivspids kanel
  - 150 g makroner, knuste
  - 4 dl piskefløde
  - 1 spsk flormelis
  - Evt. smør til formen
steps:
  - Ryst æbler med sukker, vanilje og kanel i en gryde under låg 10–15 minutter, til de er møre men stadig har form. Køl.
  - Pisk fløde til blødt skum med flormelis.
  - Læg lag i et fad eller portionsglas: æbler, makroner, flødeskum — gentag, og afslut med makroner.
  - Køl gerne 30 minutter, så makronerne blødgøres lidt af æblesaften.
  - Server kold eller let køleskabskold.
faq:
  - question: Hvilke æbler?
    answer: Syrlige som Ingrid Marie, Belle de Boskoop eller Granny Smith. Søde æbler bliver flade.
  - question: Makroner hjemmelavede?
    answer: Gerne. Købemakroner virker — vælg dem uden for meget fyldstof.
  - question: Kan den laves dagen før?
    answer: Ja. Makronerne bliver blødere — nogle synes det er bedre.
  - question: Uden flødeskum?
    answer: Vaniljeis eller skyr. Men flødeskum er den gammeldags signatur.
body: |
  Gammeldags æblekage er rystede æbler, knuste makroner og flødeskum i lag.

  Ingen ovn til kagen selv — kun æblerne på komfuret.

  Det er dessert, der smager af bedsteforældre.
tip: Lad æblerne køle før lagene — varm æblemos smelter flødeskummet.
=====
title: Bagt æblekage med marcipan
slug: bagt-aeblekage-marcipan
category: ovn
description: Varme, ovnbagte æbler dækket af en sprød marcipan- og mandelmasse — vinterdessert lige fra ovnen.
prepTime: PT20M
cookTime: PT35M
totalTime: PT55M
servings: 6
difficulty: nem
tags:
  - bagt æblekage
  - marcipan
  - æbler
  - mandel
  - dessert
  - vinter
  - ovn
imageAlt: Ovnbagte æbler med gylden marcipan- og mandelmasse ovenpå
featured: true
ingredients:
  - 6 store æbler, udhudede
  - 150 g marcipan
  - 75 g smør, blødt
  - 75 g sukker
  - 1 æg
  - 75 g mandelmel eller finthakkede mandler
  - 1 tsk vaniljesukker
  - 1 spsk citronsaft
  - Flormelis til drys
steps:
  - Varm ovnen til 180 °C. Pensl æblerne med citronsaft, og stil dem i et smurt ovnfast fad.
  - Rør marcipan, smør, sukker, æg, mandelmel og vanilje til en blød masse.
  - Fordel massen oven i og oven på æblerne.
  - Bag 30–35 minutter, til æblerne er møre og massen er gylden.
  - Drys flormelis. Server varme med vaniljeis eller flødeskum.
faq:
  - question: Æblerne falder sammen?
    answer: Vælg faste æbler, og bag kun til en kniv glider igennem. Overbagte æbler synker.
  - question: Uden marcipan?
    answer: Brug kun mandelmel, smør, sukker og æg — mere som mandelkage-topping.
  - question: Kan den laves i airfryer?
    answer: Ja i mindre fad — 160 °C i ca. 25 minutter. Hold øje med farven.
  - question: Remonce i stedet?
    answer: Ja. Marcipan-varianten er bare mere vinterlig og fyldig.
body: |
  Bagt æblekage med marcipan er varme æbler under en gylden mandel-marcipanskorpe.

  Fyld. Bag. Server med det samme.

  Isen smelter ned i saften — det er meningen.
tip: Udhud æblerne helt til bunden, så marcipanen har et hul at sætte sig i — ellers glider den af.
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
