#!/usr/bin/env python3
"""Efterårs-comfort batch 2 — gryder, supper, grød og ben-mad (aug 2026)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"
PUBLISHED = "2026-08-27"

RECIPES = r'''
=====
title: Stroganoff med svinemørbrad
slug: stroganoff-svinemoerbrad
category: pande
description: Stroganoff med svinemørbrad — lynhurtig luksus til panden med sennep, paprika og cornichoner.
prepTime: PT15M
cookTime: PT20M
totalTime: PT35M
servings: 4
difficulty: nem
tags:
  - stroganoff
  - svinemørbrad
  - mørbrad stroganoff
  - sennep
  - paprika
  - cornichoner
  - efterår
  - pande
imageAlt: Cremét stroganoff med svinemørbrad, paprika og cornichoner
featured: true
ingredients:
  - 600–700 g svinemørbrad, skåret i strimler
  - 250 g champignoner, skivede
  - 1 stort løg, hakket
  - 2 spsk smør + 1 spsk olie
  - 1 spsk dijonsennep
  - 1 tsk paprika
  - 1 spsk tomatpuré
  - 1 dl bouillon
  - 2 dl creme fraiche eller piskefløde
  - 6–8 cornichoner, skåret i skiver
  - Salt, peber, persille
steps:
  - Dup mørbrad tør. Salt og peber. Brun hurtigt i portioner i meget varm pande — 1–2 minutter. Tag op.
  - Svits champignon og løg i smør, til væsken er væk, og de har farve.
  - Rør sennep, paprika og tomatpuré i på lav varme 30 sekunder. Bouillon i, skrab bunden.
  - Tag af varmen. Rør creme fraiche og cornichoner i. Læg kødet tilbage, og varm forsigtigt — undgå hård kogning.
  - Smag til. Persille. Server med ris, pasta eller kartoffelmos.
faq:
  - question: Forskel på bøf stroganoff?
    answer: Samme sauce-idé. Se bøf stroganoff for okse. Her er mørbrad hurtigere og billigere.
  - question: Bliver mørbraden tør?
    answer: Brun kort, og varm kun igennem i saucen. Overkogt mørbrad er sejt.
  - question: Cornichoner?
    answer: De er pointen — syre og salt skærer det cremede. Syltede agurker virker også.
  - question: Fløde eller creme fraiche?
    answer: Creme fraiche er klassisk og mere syrlig. Fløde er mildere — tilsæt ekstra sennep.
body: |
  Stroganoff med svinemørbrad er pandens lynluksus: kort bruning, cremet sauce, paprika og knasende syre fra cornichoner.

  Kødet skal have farve — ikke simre i timevis.

  Det er efterårsmad, der er færdig, før ovnen er varm.
tip: Skær mørbraden på tværs af fibrene i tynde strimler. De føles mørere, og stegetiden bliver kortere.
=====
title: Ungarsk paprikagryde med skært oksekød
slug: ungarsk-paprikagryde
category: stobejern
description: Ungarsk paprikagryde med skært oksekød — tung gryderet, der simrer i timevis med bløde peberfrugter og masser af paprika.
prepTime: PT25M
cookTime: PT2H30M
totalTime: PT2H55M
servings: 6
difficulty: mellem
tags:
  - ungarsk paprikagryde
  - paprikagryde
  - oksekød
  - paprika
  - peberfrugt
  - gryderet
  - efterår
  - støbejern
imageAlt: Ungarsk paprikagryde med oksekød, paprika og peberfrugter
featured: true
ingredients:
  - 1,2 kg skært oksekød til gryderet (bov, tykkam eller højreb) i 3 cm tern
  - 3 store løg, finthakket
  - 3 røde peberfrugter i strimler
  - 3 spsk sødmefuld ungarsk paprika + 1 tsk stærk paprika
  - 2 spsk svinefedt eller olie
  - 2 spsk tomatpuré
  - 2 fed hvidløg
  - 4 dl oksebouillon
  - 2 laurbærblade, 1 tsk spidskommen
  - Salt, peber
  - Valgfrit: 1 dl creme fraiche til servering
steps:
  - Tænd ovnen på 160 °C. Brun kødet hårdt i portioner i Dutch Oven. Tag op.
  - Svits løg i fedtet 10 minutter, til de er bløde. Peberfrugt i 5 minutter.
  - Tag gryden af varmen. Rør paprika og tomatpuré i — paprikaen må ikke brænde. Hvidløg 30 sekunder.
  - Bouillon, laurbær, spidskommen og kød tilbage. Låg på. I ovnen 2–2½ time, til kødet er smørmørt.
  - Smag til. Server med creme fraiche, brød eller kartoffelmos — peberfrugterne skal være bløde, ikke sprøde.
faq:
  - question: Forskel på ungarsk gullasch?
    answer: Gullasch har ofte kartofler i gryden. Her er peberfrugt og paprika-sauce i fokus — mere «paprikagryde» end kartoffelgryde.
  - question: Bitter paprika?
    answer: Den blev for varm. Rør paprika i af varmen, eller på meget lav blus i sekunder.
  - question: Hvilket kød?
    answer: Skært grydekød med lidt bindevæv. Filet er spild — den bliver tør ved lang simre.
  - question: Gulaschsuppe i stedet?
    answer: Se gulaschsuppe, hvis du vil have mere bouillon og kartofler i skålen.
body: |
  Ungarsk paprikagryde er paprika i støbejern: skært kød, bløde peberfrugter og en sauce, der bliver dybere for hver time.

  Brun hårdt. Paprika af varmen. Simre lavt.

  Det er den ret, der dufter af efterår, allerede før du åbner døren.
tip: Brug sødmefuld paprika som hovedmængde. Den stærke er en knivspids — ellers bliver det kun varme, ikke smag.
=====
title: Glaseret skinke i ovn med grønlangkål
slug: glaseret-skinke-groenlangkaal
category: ovn
description: Glaseret skinke i ovn med grønlangkål — den tunge, saltede og søde klassiker til sene efterårsaftener.
prepTime: PT20M
cookTime: PT1H30M
totalTime: PT1H50M
servings: 8
difficulty: mellem
tags:
  - glaseret skinke
  - skinke i ovn
  - grønlangkål
  - glasur
  - efterår
  - ovn
imageAlt: Glaseret skinke skåret i skiver med grønlangkål
featured: true
ingredients:
  - 1 kogt eller røget skinke (ca. 1,5–2 kg), uden pose
  - 3 spsk dijonsennep
  - 3 spsk brun farin eller honning
  - 2 spsk æbleeddike eller appelsinsaft
  - 1 tsk stødt nellike eller 8 hele nelliker
  - 1 kg grønlangkål, afribbede blade
  - 50 g smør
  - 1 dl fløde eller mælk
  - Salt, peber, evt. muskatnød
steps:
  - Tænd ovnen på 180 °C. Score skinkens fedtside i rudemønster. Bland sennep, farin og eddike til glasur.
  - Pensl skinken. Evt. stik nelliker i. Læg i bradepande med lidt vand i bunden.
  - Bag 60–90 minutter (ca. 20 minutter pr. 500 g), pensl undervejs, til glasuren er blank og karamelliseret.
  - Imens: Blanchér grønlangkål 3–4 minutter i saltet vand. Dræn. Svits i smør, tilsæt fløde, salt, peber og muskat.
  - Hvil skinken 10 minutter. Skær i skiver. Server med grønlangkål og kogte kartofler.
faq:
  - question: Rå eller kogt skinke?
    answer: Kogt/røget er nemmest. Rå saltet skinke skal koges først, til den er gennemvarm, før glasur.
  - question: Brænder glasuren?
    answer: Dæk med folie de første 40 minutter, og pensl først til sidst. Eller sænk til 170 °C.
  - question: Grønlangkål for bitter?
    answer: Blanchér godt, og tilsæt lidt sukker eller æble i smørret.
  - question: Rester?
    answer: Kolde skiver på rugbrød, eller tern i æggekage og supper.
body: |
  Glaseret skinke med grønlangkål er efterårets søndagsbord: saltet kød, sød glasur og grønt, der kan bære fedtet.

  Score. Pensl. Bag blank.

  Grønlangkålen er ikke tilbehør — den er den grønne modsætning til det søde.
tip: Gem skinkeskyen fra bradepanden. En skefuld i grønlangkålen giver mere kødsmag end ekstra salt.
=====
title: Braiseret spidskål med bacon og fløde
slug: braiseret-spidskaal-bacon-floede
category: gryde
description: Braiseret spidskål med bacon og fløde — fed efterårsret, der fungerer som hovedret eller tungt tilbehør.
prepTime: PT15M
cookTime: PT35M
totalTime: PT50M
servings: 4
difficulty: nem
tags:
  - braiseret spidskål
  - spidskål
  - bacon
  - fløde
  - tilbehør
  - efterår
  - gryde
imageAlt: Braiseret spidskål med bacontern i cremet sauce
featured: true
ingredients:
  - 1 stor spidskål (ca. 800 g–1 kg), skåret i 6–8 både
  - 150 g bacon i tern
  - 1 løg, hakket
  - 2 dl honsebouillon
  - 2 dl piskefløde
  - 1 spsk dijonsennep
  - 1 spsk smør (hvis baconet er magert)
  - Salt, peber, evt. muskatnød
  - Frisk timian eller persille
steps:
  - Steg bacon sprødt i en bred gryde. Tag op. Gem 1–2 spsk fedt.
  - Brun spidskålsbådene i fedtet 2–3 minutter på snitfladerne, til de får farve. Tag op.
  - Svits løg 3 minutter. Bouillon i. Læg kål tilbage i ét lag. Låg på, og braiser 15–20 minutter, til kålen er mør men stadig holder formen.
  - Fløde og sennep i. Simre uden låg 5–8 minutter, til saucen tykner. Bacon tilbage.
  - Smag til. Urter. Server som hovedret med brød, eller til koteletter og kylling.
faq:
  - question: Hvidkål i stedet?
    answer: Ja, men giv den længere tid. Spidskål er sødere og bliver mør hurtigere.
  - question: For vandig?
    answer: Kog ind uden låg, eller tag kålen op og reducér saucen alene.
  - question: Uden fløde?
    answer: Brug creme fraiche eller ekstra bouillon + en klat smør. Den bliver mindre rund.
  - question: Airfryer-spidskål?
    answer: Se karamelliseret spidskål i airfryer, hvis du vil have knas — her er det blødt og cremet.
body: |
  Braiseret spidskål med bacon og fløde er efterårets grøntsagsgryde: sød kål, salt bacon, cremet sauce.

  Brun snitfladerne. Braiser under låg. Fløde til sidst.

  Den kan stå alene — eller bære en kotelet.
tip: Lad midtribben sidde i bådene. Den holder kålen samlet, mens bladene bliver silkebløde.
=====
title: Fårikål
slug: faarikaal
category: gryde
description: Fårikål — klassisk nordisk simreret med lag af fedt lammekød, hvidkål og hele sort peberkorn.
prepTime: PT20M
cookTime: PT2H30M
totalTime: PT2H50M
servings: 6
difficulty: mellem
tags:
  - fårikål
  - lam
  - hvidkål
  - peberkorn
  - norsk
  - gryderet
  - efterår
  - gryde
imageAlt: Fårikål med lammekød, hvidkål og hele peberkorn i gryde
featured: true
ingredients:
  - 1,5 kg lammekød med ben (bov, nakke eller fårekølle i store stykker)
  - 1,5–2 kg hvidkål, skåret i grove både
  - 2–3 spsk hele sorte peberkorn
  - Ca. 4–5 dl vand eller honsebouillon
  - 2 tsk salt (smag til — kødet kan være salt)
  - Evt. 2 laurbærblade
  - Kogte kartofler til servering
steps:
  - Dup kødet tørt. Læg et lag kål i bunden af en tung gryde, derefter kød, peberkorn og salt. Gentag, til alt er brugt — kål øverst.
  - Hæld vand i, så det når ca. halvvejs op ad indholdet — ikke mere. Låg på.
  - Bring langsomt i kog. Skru ned, og simre meget svagt 2–2½ time, til kødet er mørt, og kålen er blød.
  - Rør ikke rundt undervejs — lagene skal holde. Sæt gryden på bordet, og lad den trække 10 minutter.
  - Server med kogte kartofler. Peberkornene spises eller skubbes til side — de er smagen, ikke pynt.
faq:
  - question: Skal der mel i?
    answer: Klassisk norsk fårikål er uden jævning. Væsken bliver til en klar, peberfyldt sky.
  - question: Får eller lam?
    answer: Lam er mildere. Får er mere markant. Begge virker — vælg det, du kan få med ben.
  - question: For peberstærk?
    answer: Start med 1½ spsk peberkorn. Du kan altid knuse flere i tallerkenen.
  - question: Kan den laves dagen før?
    answer: Ja. Den smager bedre. Skim fedt af, når den er kold, hvis du vil.
body: |
  Fårikål er lag på lag: kål, lam, peberkorn — og så tid nok til, at det hele smelter sammen.

  Lidt væske. Meget peber. Ingen unødvendig jævning.

  Det er nordisk efterår uden filter.
tip: Brug kød med ben og fedtkant. Magert udbenet lam bliver tørt i den lange simre.
=====
title: Ungarsk fiskesuppe (Halászlé)
slug: ungarsk-fiskesuppe-halaszle
category: gryde
description: Ungarsk fiskesuppe (Halászlé) — stærk, rød og saltet suppe med masser af paprika og ferskvandsfisk.
prepTime: PT25M
cookTime: PT50M
totalTime: PT1H15M
servings: 4
difficulty: mellem
tags:
  - halászlé
  - ungarsk fiskesuppe
  - fiskesuppe
  - paprika
  - ferskvandsfisk
  - efterår
  - gryde
imageAlt: Rød ungarsk fiskesuppe med paprika og fiskestykker
featured: true
ingredients:
  - 800 g ferskvandsfisk i stykker (karpe, sandart, torsk eller laks — gerne med hoved/ben til fond)
  - 2 store løg, finthakket
  - 2 spsk svinefedt eller olie
  - 3 spsk sødmefuld paprika + 1 tsk stærk paprika
  - 1 rød peberfrugt i strimler
  - 2 tomater i tern (eller 1 dl hakkede tomater)
  - 1,2 l fiskefond eller vand
  - 1 laurbærblad
  - Salt — generøst
  - Frisk chili eller chiliflager (valgfrit)
  - Citron og brød til servering
steps:
  - Hvis du har hoved/ben: kog dem 20 minutter i vand, si — det er fonden. Ellers brug færdig fiskefond.
  - Svits løg i fedt 8–10 minutter, til de er bløde. Tag af varmen. Rør paprika i.
  - Peberfrugt, tomat, fond og laurbær i. Bring i kog, simre 15 minutter.
  - Læg fiskestykker i. Simre forsigtigt 8–12 minutter, til fisken er netop gennemstegt — ikke omrør hårdt.
  - Smag kraftigt til med salt og chili. Server rygende varm med brød og citron.
faq:
  - question: Hvilken fisk?
    answer: Klassisk er karpe og andre ferskvandsfisk. Sandart, torsk eller laks virker fint i Danmark.
  - question: For stærk?
    answer: Drop den stærke paprika, og hold dig til sødmefuld. Chili er valgfri.
  - question: Kan den laves uden hoved/ben?
    answer: Ja — men fond på skrog giver den dybe fiskesmag, paprika alene ikke kan.
  - question: Tykkere?
    answer: Blend en del af løg/peberfrugt-basen, før fisken kommer i.
body: |
  Halászlé er paprika-rød fiskesuppe: løg, masser af paprika, salt — og fisk, der kun lige når at blive færdig.

  Fond først. Paprika af varmen. Fisk til sidst.

  Det er den suppe, der varmer indefra, når efteråret bider.
tip: Salt mere, end du tror. Den ungarske stil er tydeligt saltet — ellers smager det bare af rød bouillon.
=====
title: Cremet jordskokkesuppe med bacontern
slug: cremet-jordskokkesuppe-bacon
category: gryde
description: Cremet jordskokkesuppe med bacontern — jordagtig, sødmefuld efterårssuppe med saltet baconknas.
prepTime: PT20M
cookTime: PT35M
totalTime: PT55M
servings: 4
difficulty: nem
tags:
  - jordskokkesuppe
  - jordskok
  - bacon
  - cremet suppe
  - efterår
  - gryde
imageAlt: Cremet jordskokkesuppe toppet med sprøde bacontern
featured: true
ingredients:
  - 800 g jordskokker, skrællet og i tern
  - 150 g bacon i tern
  - 1 løg, hakket
  - 1 fed hvidløg
  - 1 kartoffel i tern (til cremethed)
  - 8 dl honse- eller grøntsagsbouillon
  - 1 dl piskefløde
  - 1 spsk smør (hvis baconet er magert)
  - Salt, peber, evt. lidt citronsaft
steps:
  - Steg bacon sprødt. Tag op. Gem 1–2 spsk fedt.
  - Svits løg i fedtet 5 minutter. Hvidløg 30 sekunder. Jordskokker og kartoffel i, vend rundt 2 minutter.
  - Bouillon i. Bring i kog, simre 20–25 minutter, til jordskokkerne er bløde.
  - Blend glat. Rør fløde i. Smag til med salt, peber og en dråbe citron, hvis den er for sød/jordagtig.
  - Server med bacontern ovenpå.
faq:
  - question: Skrælle jordskokker?
    answer: Ja til cremet suppe. Brug handsker eller citronvand — de mørkner hurtigt.
  - question: Bål-versionen?
    answer: Se cremet jordskokkesuppe over bål — samme idé, åben ild.
  - question: Uden fløde?
    answer: Ekstra kartoffel og en klat creme fraiche. Eller bare blend godt.
  - question: Kan den fryses?
    answer: Ja uden fløde og bacon. Tilsæt dem efter optøning.
body: |
  Cremet jordskokkesuppe er efterårets jordsmag i skål: sød, nøddeagtig — og bacontern, der giver det salt, den skriger efter.

  Baconfedt til løgene. Blend glat. Knas ovenpå.

  Det er den suppe, der får folk til at spørge, hvad der er i — og bede om mere.
tip: En skefuld creme fraiche eller et drys parmesan forstærker saltet uden at overdøve jordskokken.
=====
title: Kartoffelsuppe med porrer og chorizotern
slug: kartoffelsuppe-porre-chorizo
category: gryde
description: Kartoffelsuppe med porrer og chorizotern — mormor-suppen opgraderet med stærk, saltet spansk pølse.
prepTime: PT20M
cookTime: PT35M
totalTime: PT55M
servings: 4
difficulty: nem
tags:
  - kartoffelsuppe
  - porresuppe
  - chorizo
  - kartoffel-porresuppe
  - efterår
  - gryde
imageAlt: Cremét kartoffelsuppe med porrer og chorizotern
featured: true
ingredients:
  - 150 g chorizo i tern
  - 2 porrer, skåret i skiver (kun det lyse)
  - 600 g kartofler i tern
  - 1 løg, hakket
  - 1 fed hvidløg
  - 1 liter honse- eller grøntsagsbouillon
  - 1 dl piskefløde (valgfrit)
  - 1 spsk smør, hvis chorizoen er mager
  - Salt, peber, evt. paprika
  - Frisk persille
steps:
  - Steg chorizotern, til de afgiver olie og er let sprøde. Tag op. Gem 1–2 spsk fedt i gryden.
  - Svits løg og porrer i fedtet 8–10 minutter, til de er bløde. Hvidløg 30 sekunder.
  - Kartofler og bouillon i. Bring i kog, simre 20 minutter, til kartoflerne er møre.
  - Blend delvist eller helt — rustik med bidder, eller cremet. Fløde i efter smag.
  - Smag til (chorizoen er salt). Top med chorizotern og persille.
faq:
  - question: Ungarsk kartoffelsuppe i stedet?
    answer: Se ungarsk kartoffelsuppe for paprika-versionen uden chorizo.
  - question: Trykkoger?
    answer: Se kartoffel-porresuppe i trykkoger — tilsæt stegt chorizo til sidst.
  - question: Mild chorizo?
    answer: Brug mild, eller bland med bacon. Den stærke er pointen for de fleste.
  - question: For tyk?
    answer: Fortynd med bouillon. Kartofler suger ved henstand.
body: |
  Kartoffelsuppe med porrer og chorizo er mormor møder Spanien: blød kartoffelbase, søde porrer, saltet pølseknas.

  Steg chorizoen først. Brug olien. Blend efter humør.

  Det er hverdagssuppe, der smager af weekend.
tip: Gem chorizoternene til toppen. Blandes alt i, mister du kontrasten mellem cremet og salt-sprødt.
=====
title: Minestronesuppe med parmesanskorper
slug: minestrone-parmesanskorper
category: gryde
description: Minestronesuppe med parmesanskorper — italiensk efterårssuppe kogt på salte osteskorper for maksimal umami.
prepTime: PT25M
cookTime: PT45M
totalTime: PT1H10M
servings: 6
difficulty: nem
tags:
  - minestrone
  - minestronesuppe
  - parmesan
  - osteskorper
  - italiensk
  - efterår
  - gryde
imageAlt: Minestronesuppe med grøntsager, pasta og parmesan
featured: true
ingredients:
  - 2 spsk olivenolie
  - 1 løg, 2 gulerødder, 2 stilke bladselleri — hakket
  - 2 fed hvidløg
  - 1 dåse (400 g) hakkede tomater
  - 1,2 l grøntsags- eller honsebouillon
  - 1–2 parmesanskorper (rengjorte)
  - 1 courgette i tern, 100 g grønne bønner
  - 1 dåse (240 g) cannellini- eller hvide bønner, skyllede
  - 80 g små pasta (ditalini eller øjne)
  - 1 kvist rosmarin eller 1 tsk oregano
  - Salt, peber, olivenolie og revet parmesan til servering
steps:
  - Svits løg, gulerod og selleri i olie 10 minutter (sofrito). Hvidløg 1 minut.
  - Tomater i. Kog 3 minutter. Bouillon, parmesanskorper og rosmarin i. Simre 20 minutter.
  - Courgette, bønner og grønne bønner i. Simre 10 minutter.
  - Pasta i. Kog til al dente. Fjern skorperne (skær det bløde af, og læg tilbage — smid den hårde skorpe ud).
  - Smag til. Server med olivenolie og masser af revet parmesan.
faq:
  - question: Ingen parmesanskorper?
    answer: Et stykke parmesan i gryden, eller ekstra bouillon + mere ost ved servering. Skorperne er umami-tricket.
  - question: Trykkoger?
    answer: Se minestrone i trykkoger — hurtigere, men skorperne får mindre tid at afgive smag.
  - question: Glutenfri?
    answer: Drop pasta, eller brug glutenfri. Ris eller ekstra bønner fylder.
  - question: Kan den fryses?
    answer: Ja uden pasta. Tilsæt pasta ved opvarmning.
body: |
  Minestrone med parmesanskorper er efterårets italienske sparebøsse: grøntsager, bønner — og de gamle osteskorper, der giver dybden.

  Sofrito først. Skorper i bouillonen. Pasta til sidst.

  Det er den suppe, der smager dyrere, end den er.
tip: Gem parmesanskorper i fryseren. To skorper i en minestrone er gratis umami.
=====
title: Klassisk svampesuppe på vilde svampe
slug: klassisk-svampesuppe
category: gryde
description: Klassisk svampesuppe på vilde svampe — tyk, cremet efterårssuppe med kantareller og karl johan.
prepTime: PT25M
cookTime: PT30M
totalTime: PT55M
servings: 4
difficulty: nem
tags:
  - svampesuppe
  - vilde svampe
  - kantareller
  - karl johan
  - cremet suppe
  - efterår
  - gryde
imageAlt: Cremét svampesuppe med kantareller og karl johan
featured: true
ingredients:
  - 500 g vilde svampe (kantareller, karl johan, evt. blandet) — renset
  - 200 g champignon (hvis du mangler vilde)
  - 1 skalotteløg eller 1 lille løg, finthakket
  - 2 fed hvidløg
  - 40 g smør
  - 2 spsk hvedemel
  - 8 dl honse- eller grøntsagsbouillon
  - 2 dl piskefløde
  - 1 spsk sherry eller cognac (valgfrit)
  - Salt, peber, timian, persille
steps:
  - Svits svampene i portioner i smør på høj varme, til væsken er væk, og de har stegeskorpe. Tag ⅓ op til topping.
  - Svits løg med resten af svampene 3 minutter. Hvidløg 30 sekunder. Sherry i, lad fordampe.
  - Drys mel over, rør 1 minut. Bouillon i under omrøring. Simre 10 minutter.
  - Blend delvist for tykkelse, eller helt glat. Fløde i. Smag til.
  - Server med de gemte svampe ovenpå og persille.
faq:
  - question: Kun champignon?
    answer: Ja — men tilsæt 10 g tørrede karl johan udblødt i bouillon for skovsmag.
  - question: For tynd?
    answer: Mere mel i roux, eller blend flere svampe. Kog ind uden låg.
  - question: Kan den fryses?
    answer: Ja uden fløde. Fløde i ved opvarmning.
  - question: Tilbehør?
    answer: Surdejsbrød, crostini, eller en klat creme fraiche.
body: |
  Klassisk svampesuppe er efterårets høst i gryde: kantareller, karl johan, smør og fløde.

  Stegeskorpe først. Væsken væk. Fløde til sidst.

  Det er den suppe, der lugter af skovtur — også hvis svampene er fra køledisken.
tip: Svampene skal nesten snerte i panden. Damper de i bunke, bliver de grå og kedelige.
=====
title: Kyllingesuppe med ingefær og chili
slug: kyllingesuppe-ingefaer-chili
category: gryde
description: Kyllingesuppe med ingefær og chili — bliv-rask-suppe til efterårets forkølelser, kogt på skrog og urter.
prepTime: PT20M
cookTime: PT1H30M
totalTime: PT1H50M
servings: 4
difficulty: nem
tags:
  - kyllingesuppe
  - ingefær
  - chili
  - bliv rask-suppe
  - forkølelse
  - efterår
  - gryde
imageAlt: Klar kyllingesuppe med ingefær, chili og urter
featured: true
ingredients:
  - 1 kg kyllingeskovle, vinger eller 1 hel kylling
  - 1 løg, 2 gulerødder, 2 stilke bladselleri
  - 1 porre (valgfrit)
  - 5 cm frisk ingefær, skåret i skiver
  - 2–3 fed hvidløg, knust
  - 1–2 friske chili eller 1 tsk chiliflager
  - 2 liter vand
  - 2 laurbærblade, 8 peberkorn
  - Salt
  - Frisk koriander eller persille, citron
  - Evt. nudler eller ris til servering
steps:
  - Læg kylling i gryde med koldt vand. Bring langsomt i kog, skum grundigt.
  - Tilsæt grøntsager, ingefær, hvidløg, chili, laurbær og peberkorn. Simre svagt 1–1½ time.
  - Tag kylling op. Pluk kødet fra benene. Si bouillonen.
  - Bring bouillon i kog igen. Smag til med salt. Læg kød tilbage. Evt. kog nudler i bouillonen.
  - Server med masser af frisk urter, ekstra chili og citronsaft.
faq:
  - question: Forskel på hønsekødssuppe?
    answer: Hønsekødssuppe er den klare danske klassiker med melboller. Her er ingefær og chili den varme, «bliv rask»-profil.
  - question: For stærk?
    answer: Fjern chili efter 20 minutter, eller brug kun ingefær.
  - question: Hurtigere?
    answer: Brug færdig fond, og simre 20 minutter med ingefær, chili og plukket kyllingekød.
  - question: Kan bouillonen fryses?
    answer: Absolut. Frys uden nudler.
body: |
  Kyllingesuppe med ingefær og chili er medicin, der smager af mad: skrog, skum, lang simre — og varme fra ingefær.

  Klar bouillon. Frisk chili. Citron til sidst.

  Det er den skål, man laver, når halsen siger nej, og efteråret siger ja til sygdom.
tip: Knus ingefæren let med knivsiden, før den går i gryden. Mere saft, mere effekt.
=====
title: Polenta med braiseret oksekød
slug: polenta-braiseret-oksekoed
category: gryde
description: Polenta med braiseret oksekød — majsgrød med smør og parmesan, toppet med mørt kød og indkogt skysovs.
prepTime: PT25M
cookTime: PT2H45M
totalTime: PT3H10M
servings: 4
difficulty: mellem
tags:
  - polenta
  - braiseret oksekød
  - majsgrød
  - skysovs
  - comfort food
  - efterår
  - gryde
imageAlt: Cremét polenta toppet med braiseret oksekød og skysovs
featured: true
ingredients:
  - 800 g oksekød til gryderet i 3 cm tern
  - 2 spsk olie
  - 1 løg, 1 gulerod, 1 stilk bladselleri — hakket
  - 1 spsk tomatpuré
  - 2 dl rødvin
  - 4 dl oksebouillon
  - 2 laurbærblade, timian
  - Salt og peber
  - Polenta: 2 dl polenta (majsgryn), 8 dl vand eller mælk/vand, 40 g smør, 50 g parmesan, salt
steps:
  - Brun kødet i olie i portioner. Tag op. Svits grøntsager 8 minutter. Tomatpuré 1 minut.
  - Vin i, skrab, kog 3 minutter. Bouillon, krydderier, kød tilbage. Simre under låg 2–2½ time, til kødet er mørt. Kog saucen ind.
  - Polenta: Bring væske i kog med salt. Pisk polenta i. Rør ofte 20–30 minutter (eller følg pakken), til den er cremet.
  - Rør smør og parmesan i polentaen. Smag til.
  - Anret polenta i skåle. Top med kød og skysovs.
faq:
  - question: Instant polenta?
    answer: Ja — kortere tid. Rør stadig smør og parmesan i til sidst.
  - question: Til overs?
    answer: Hæld rest-polenta i fad, køl, skær skiver, og steg dem dagen efter.
  - question: Andet kød?
    answer: Oksehale, lam eller vildt. Se også osobuko med polenta.
  - question: Klumper i polenta?
    answer: Pisk, mens du drysser grynene i kogende væske. Rør tit.
body: |
  Polenta med braiseret oksekød er rustik comfort: blød majsgrød, saltet ost, og kød der falder fra hinanden i skysovs.

  Kød først. Polenta mens det trækker. Smør og parmesan i grøden.

  Det er tallerkenen, der erstatter kartoffelmos en tirsdag i november.
tip: Polentaen stivner hurtigt. Server med det samme — eller hold den lun med ekstra væske klar til at røre i.
=====
title: Gammeldags fløjlsgrød
slug: gammeldags-floejsgoed
category: gryde
description: Gammeldags fløjlsgrød med smørklat — mormor-klassikeren på smør og mel, serveret varm med hvidtølssukker.
prepTime: PT5M
cookTime: PT20M
totalTime: PT25M
servings: 4
difficulty: nem
tags:
  - fløjlsgrød
  - gammeldags fløjlsgrød
  - melgrød
  - hvidtølssukker
  - mormormad
  - efterår
  - gryde
imageAlt: Fløjlsgrød med smørklat og hvidtølssukker
featured: true
ingredients:
  - 50 g smør
  - 1 dl hvedemel
  - 1 liter sødmælk
  - ½ tsk salt
  - Smørklat til servering
  - Hvidtølssukker eller kanelsukker
steps:
  - Smelt smør i en tung gryde. Rør melet i, og lad det lyse stege 1–2 minutter under omrøring — det må ikke blive mørkt.
  - Tilsæt mælk lidt ad gangen under kraftig piskning, så der ikke kommer klumper.
  - Bring i kog under omrøring. Skru ned, og simre 10–15 minutter, til grøden er tyk og blank som fløjl.
  - Smag til med salt.
  - Server rygende varm med en stor smørklat og hvidtølssukker.
faq:
  - question: Hvad er hvidtølssukker?
    answer: Sukker med stødt kanel og ofte lidt stødt nellike — klassisk til melgrød og øllebrød.
  - question: Klumper?
    answer: Pisk energisk, og tilsæt mælken gradvist. En stavblender redder en klumpet gryde.
  - question: For tyk?
    answer: Rør mere mælk i. Den tykner mere ved henstand.
  - question: Er det det samme som buttergrød?
    answer: Tæt beslægtet. Fløjlsgrød er den blanke, mælkerige version på smør-roux.
body: |
  Fløjlsgrød er mormors genvej til varme: smør, mel, mælk — og en smørklat, der smelter i midten.

  Lys roux. Pisk. Simre til blank.

  Det er grød uden korn, og den smager af barndom i november.
tip: Salt er ikke valgfrit. Uden salt smager den kun af lim — med salt smager den af fløjl.
=====
title: Byg-otto med confiteret and
slug: byg-otto-confiteret-and
category: gryde
description: Byg-otto med confiteret and — fed, saltet efterårs-byggrød toppet med plukket andekød og timian.
prepTime: PT20M
cookTime: PT50M
totalTime: PT1H10M
servings: 4
difficulty: mellem
tags:
  - byg-otto
  - byggrød
  - confiteret and
  - andelår
  - timian
  - efterår
  - gryde
imageAlt: Byggrød toppet med confiteret andekød og timian
featured: true
ingredients:
  - 3 dl perlebyg, skyllet
  - 1 liter honsebouillon, lun
  - 2 confiterede andelår (købte eller hjemmelavede)
  - 1 skalotteløg, finthakket
  - 1 fed hvidløg
  - 2 spsk andefedt eller smør
  - 1 dl tør hvidvin (valgfrit)
  - 50 g parmesan eller vesterhavsost, revet
  - 2 kviste timian
  - Salt, peber
steps:
  - Varm andelårene, til skindet er sprødt, og kødet slipper benet. Pluk kødet i store bidder. Gem lidt fedt.
  - Svits løg i andefedt 3 minutter. Perlebyg i, rist 2 minutter. Vin i, lad suge.
  - Tilsæt bouillon en øse ad gangen under omrøring ca. 35–40 minutter, til byggen er mør med bid.
  - Rør ost og timianblade i. Smag til.
  - Anret byggrød. Top med plukket and og evt. knasende skind.
faq:
  - question: Ingen confiteret and?
    answer: Brug stegte andelår, eller se confiterede andelår. Restekød fra andesteg virker også.
  - question: Almindelig byggrød?
    answer: Se byggrød med vesterhavsost og svampe — samme base uden and.
  - question: For tør byg?
    answer: Mere lun bouillon. Byg suger mere end ris.
  - question: Tilbehør?
    answer: En syrlig salat eller ribsgele på siden skærer fedtet.
body: |
  Byg-otto med confiteret and er den salte efterårsrisotto: perlebyg, ost — og plukket and, der gør grøden til hovedret.

  Byggen skal have bid. Anden skal være varm og fed.

  Det er den tallerken, man laver, når der er andelår i køleskabet, og man vil have mere end bare kød med kartofler.
tip: Brug andefedtet til at riste byggen i. Det er gratis smag, smør ikke kan matche.
=====
title: Klatkager af risengrød
slug: klatkager-risengrod
category: pande
description: Klatkager af risengrød — forvandl efterårets risengrødsrester til sprøde, smørstegte klatkager.
prepTime: PT10M
cookTime: PT15M
totalTime: PT25M
servings: 4
difficulty: nem
tags:
  - klatkager
  - risengrød
  - bagt risengrød
  - rester
  - smørstegt
  - efterår
  - pande
imageAlt: Sprøde smørstegte klatkager af risengrød med kanelsukker
featured: true
ingredients:
  - 6–8 dl kold risengrød (fra dagen før)
  - 1–2 æg
  - 2–4 spsk hvedemel (efter konsistens)
  - ½ tsk salt
  - Smør til stegning
  - Kanelsukker eller hvidtølssukker til servering
  - Evt. syltetøj eller æblemos
steps:
  - Rør kold risengrød med æg, mel og salt til en tyk dej, der kan formes — ikke løbende.
  - Form flade kager med en ske eller våde hænder (ca. 1 cm tykke).
  - Steg i rigeligt smør på middel varme 3–4 minutter på hver side, til de er dybt gyldne og sprøde i kanten.
  - Hold færdige klatkager varme i ovn ved 80 °C, mens du steger resten.
  - Server med kanelsukker og evt. syltetøj.
faq:
  - question: For løs dej?
    answer: Mere mel, eller køl grøden længere. Varm grød laves ikke til klatkager.
  - question: Kan man bage dem i ovn?
    answer: Ja — pensl med smør, 200 °C i ca. 15–20 minutter, vend halvvejs. Panden giver bedre skorpe.
  - question: Ingen rester?
    answer: Kog en portion klassisk risengrød dagen før med vilje. Det er klatkage-kit.
  - question: Salte klatkager?
    answer: Drop sukkeret, tilsæt ost og forårsløg — så er det en anden ret.
body: |
  Klatkager er risengrødens anden akt: kolde rester, æg, mel — og smør nok til en ærlig skorpe.

  Kold grød. Fast dej. Gylden stegeskorpe.

  Det er derfor, man altid laver for meget risengrød i oktober.
tip: Tryk kagerne flade. Tykkeklatkager bliver varme udenpå og kolde indeni.
=====
title: Braiseret tykkam i porter
slug: braiseret-tykkam-porter
category: stobejern
description: Braiseret tykkam i porter — mørkt, trevlet oksekød, der har trukket smag fra en flaske tung øl i støbejernsgryden.
prepTime: PT25M
cookTime: PT3H30M
totalTime: PT3H55M
servings: 6
difficulty: mellem
tags:
  - tykkam
  - oksetand
  - porter
  - mørkt øl
  - braiseret oksekød
  - efterår
  - støbejern
imageAlt: Braiseret tykkam i porter med indkogt mørk sauce
featured: true
ingredients:
  - 1,5 kg tykkam eller oksetand i store stykker
  - 2 spsk olie
  - 2 løg, 2 gulerødder, 2 stilke bladselleri
  - 2 spsk tomatpuré
  - 1 flaske porter eller stout (33–44 cl)
  - 4 dl oksebouillon
  - 2 laurbærblade, 6 peberkorn, 3 kviste timian
  - 1 spsk dijonsennep
  - Salt og peber
steps:
  - Tænd ovnen på 150 °C. Dup kødet tørt. Brun hårdt på alle sider i Dutch Oven. Tag op.
  - Svits grøntsager 8 minutter. Tomatpuré 2 minutter. Øl i, skrab bunden, kog 3 minutter.
  - Bouillon og krydderier i. Kød tilbage. Låg på. I ovnen 3–3½ time, til kødet er trevlet mørt.
  - Tag kødet op. Si saucen, kog ind, rør sennep i. Smag til.
  - Træk kødet i store tråde eller skær i skiver. Overhæld med sauce. Server med kartoffelmos eller polenta.
faq:
  - question: Tykkam eller oksetand?
    answer: Begge er rige på bindevæv og elsker lang braserering. Oksetand er ofte mere markant i smagen.
  - question: Forskel på oksehale i øl?
    answer: Se oksehale i mørkt øl. Her er det et større stegestykke, der kan skæres eller trevles.
  - question: For bitter sauce?
    answer: Brug porter, ikke IPA. En knivspids sukker eller ekstra tomatpuré balancerer.
  - question: Kan den laves dagen før?
    answer: Ja — den bliver bedre. Skim fedt af efter køling.
body: |
  Braiseret tykkam i porter er trevlet efterårskød: hård bruning, mørkt øl, lav ovn i timer.

  Øllet skal koge ind. Kødet skal give efter.

  Det er den ret, man sætter i ovnen, før man tænder film.
tip: Brun kødet i portioner, hvis stykkerne er mange. Fyldt gryde damper — og så mister du skorpen i saucen.
=====
title: Sprængt svineskank med sennep
slug: spraengt-svineskank-sennep
category: gryde
description: Sprængt svineskank med sennep — saltet skank kogt mør med laurbær, serveret med groft rugbrød.
prepTime: PT20M
cookTime: PT2H30M
totalTime: PT48H50M
servings: 4
difficulty: mellem
tags:
  - sprængt svineskank
  - svineskank
  - saltet skank
  - sennep
  - rugbrød
  - efterår
  - gryde
imageAlt: Mør sprængt svineskank med sennep og rugbrød
featured: true
ingredients:
  - 2–4 svineskanker (ca. 1,5–2 kg)
  - 80 g groft salt
  - 1 spsk sukker
  - 1 tsk peber
  - 2 laurbærblade
  - 8 peberkorn
  - 1 løg, 1 gulerod
  - Vand til dækning
  - Groft sennep og rugbrød til servering
steps:
  - Bland salt, sukker og peber. Gnid ind i skankerne. Læg i pose eller skål, og køl 24–48 timer. Vend en gang.
  - Skyl skankerne. Læg i gryde med koldt vand, løg, gulerod, laurbær og peberkorn. Bring langsomt i kog, skum.
  - Simre meget svagt 2–2½ time, til kødet slipper benet.
  - Tag op, og lad trække 10 minutter. Skær eller pluk kødet fra.
  - Server lun eller kold med groft sennep og rugbrød — eventuelt med kogte kartofler og syltede rødbeder.
faq:
  - question: Forskel på braiseret skank i øl?
    answer: Den er stegt/braiseret med ølsauce. Her er skanken saltet først og kogt som saltmad til sennep og rugbrød.
  - question: For salt?
    answer: Udblød 1–2 timer i koldt vand efter saltningen, før kogning — eller salt kortere tid.
  - question: Kan jeg købe saltet skank?
    answer: Ja. Så springer du saltningen over, og går direkte til kogning.
  - question: Svær på?
    answer: Gerne. Den giver smag til bouillonen. Spis den eller smid den efter.
body: |
  Sprængt svineskank er saltmad i efterårsform: salt, tid, langsom kogning — og sennep på groft rugbrød.

  24–48 timer i salt. Svag simre. Kød der glider af.

  Det er frokost eller aftensmad uden finesser, kun smag.
tip: Gem kogevandet. Det er en salt bouillon, der kan fortyndes til ærtesuppe eller kål.
=====
title: Gammeldags hjerter i flødesovs
slug: hjerter-i-floedesovs
category: gryde
description: Gammeldags hjerter i flødesovs — intens mormor-simremad med indmad, bacon og tyk, brun flødesovs.
prepTime: PT25M
cookTime: PT1H30M
totalTime: PT1H55M
servings: 4
difficulty: mellem
tags:
  - hjerter
  - kalvehjerter
  - flødesovs
  - indmad
  - mormormad
  - efterår
  - gryde
imageAlt: Hjerter i brun flødesovs med bacon
featured: true
ingredients:
  - 800 g kalve- eller grisehjerter, renset og i skiver eller tern
  - 100 g bacon i tern
  - 2 løg, hakket
  - 200 g champignoner, skivede
  - 2 spsk smør + 1 spsk olie
  - 2 spsk hvedemel
  - 2 dl okse- eller honsebouillon
  - 2 dl piskefløde
  - 1 spsk tomatpuré
  - 1 spsk soya eller Worcestershire
  - Salt, peber, timian
steps:
  - Dup hjerter tørre. Brun bacon, tag op. Brun hjerter i portioner i smør/olie. Tag op.
  - Svits løg og champignon 6–8 minutter. Tomatpuré 1 minut. Drys mel over, rør 1 minut.
  - Bouillon i under omrøring. Fløde, soya og timian i. Læg hjerter og bacon tilbage.
  - Simre under låg 60–75 minutter, til hjerterne er møre (kalv er hurtigere end gris).
  - Smag til. Server med kartoffelmos eller kogte kartofler.
faq:
  - question: Hvordan renses hjerter?
    answer: Skær sener, blodpropper og hårde rør væk. Skyl i koldt vand, og dup tørre.
  - question: Sejt kød?
    answer: For kort tid eller for høj varme. Simre lavt, til en gaffel går nemt i.
  - question: Kan man bruge kyllingehjerter?
    answer: Ja — kortere tid, ca. 20–30 minutter i saucen efter bruning.
  - question: For stærk indmadssmag?
    answer: Udblød skiver 30 minutter i mælk, før stegning.
body: |
  Hjerter i flødesovs er mormor uden filter: indmad, bacon, brun sauce — og tålmodighed, til kødet giver efter.

  Brun. Jævn. Simre.

  Det er den ret, der deler bordet — og vinder dem, der smager.
tip: Skær hjerterne i ensartede skiver på tværs. De bliver mørere, og stegetiden bliver mere forudsigelig.
=====
title: Andelår i fad med rodfrugter
slug: andelaar-i-fad-rodfrugter
category: ovn
description: Andelår i fad med rodfrugter — langtidsstegte lår i andefedt og sky, mens rodfrugterne suger smagen til sig.
prepTime: PT25M
cookTime: PT1H45M
totalTime: PT2H10M
servings: 4
difficulty: mellem
tags:
  - andelår
  - andelår i fad
  - rodfrugter
  - andefedt
  - efterår
  - ovn
imageAlt: Andelår bagt i fad med rodfrugter og sky
featured: true
ingredients:
  - 4 andelår med skind
  - 800 g blandede rodfrugter (gulerod, pastinak, selleri, kartofler) i store stykker
  - 2 rødløg i både
  - 4 fed hvidløg, knuste
  - 2 kviste timian, 2 laurbærblade
  - 2 dl æblecider eller honsebouillon
  - 1 spsk olie eller andefedt
  - Salt og peber
steps:
  - Tænd ovnen på 180 °C. Score skindet. Salt og peber andelårene generøst.
  - Fordel rodfrugter, løg, hvidløg og krydderier i et ovnfast fad. Vend med olie, salt og peber.
  - Læg andelårene ovenpå, skind opad. Hæld cider/bouillon i bunden — ikke over skindet.
  - Bag 90–105 minutter, til skindet er knasende, og kødet er mørt (ca. 80 °C ved benet). Hæld sky over rodfrugterne undervejs.
  - Hvil 5–10 minutter. Server lårene med rodfrugter og sky fra fadet.
faq:
  - question: Forskel på confiterede andelår?
    answer: Confitering er lav temperatur i fedt. Her er det ovnstegning på rodfrugter — mere hverdag, stadig fedt og mørt.
  - question: Blødt skind?
    answer: Tør skindet godt, start ikke med væske over skindet, og giv evt. 5 minutter grill til sidst.
  - question: Sous vide?
    answer: Se andelår sous vide for præcis mørhed — finish skindet i ovn eller pande.
  - question: Tilbehør?
    answer: Rødkål eller en syrlig salat. Rodfrugterne er allerede tilbehøret.
body: |
  Andelår i fad med rodfrugter er ét-fad-efterår: skind der knaser, kød der slipper, rødder der bader i sky.

  Salt. Score. Ovnen klarer resten.

  Det er den ret, der føles som gæstemad, men er mest ventetid.
tip: Læg lårene ovenpå — ikke ned i væsken. Skindet skal stege tørt for at blive knasende.
=====
title: Braiseret kalvespidsbryst med æblesky
slug: braiseret-kalvespidsbryst-aebler
category: stobejern
description: Braiseret kalvespidsbryst — mørt efterårskød med syrlig-sød skysovs lavet på efterårets æbler.
prepTime: PT30M
cookTime: PT3H
totalTime: PT3H30M
servings: 6
difficulty: mellem
tags:
  - kalvespidsbryst
  - spidsbryst
  - æblesky
  - braiseret kalv
  - efterår
  - støbejern
imageAlt: Braiseret kalvespidsbryst med æblesky og rodfrugter
featured: true
ingredients:
  - 1,5 kg kalvespidsbryst i ét stykke eller store skiver
  - 2 spsk olie eller smør
  - 2 løg i både
  - 2 gulerødder, 2 stilke bladselleri
  - 2 syrlige æbler i både (fx Ingrid Marie eller Granny Smith)
  - 2 spsk tomatpuré
  - 2 dl æblecider eller tør hvidvin
  - 5 dl kalve- eller honsebouillon
  - 2 laurbærblade, 3 kviste timian
  - 1 spsk æbleeddike eller citronsaft
  - Salt og peber
steps:
  - Tænd ovnen på 150 °C. Dup kødet tørt. Brun på alle sider i Dutch Oven. Tag op.
  - Svits løg, gulerod og selleri 8 minutter. Æbler og tomatpuré 2 minutter.
  - Cider/vin i, skrab, kog 3 minutter. Bouillon, krydderier, kød tilbage.
  - Låg på. I ovnen 2½–3 timer, til kødet er smørmørt.
  - Tag kødet op. Si saucen, kog ind, smag til med eddike/citron, salt og peber. Skær kød i skiver. Server med sky og evt. kartoffelmos.
faq:
  - question: Kan jeg bruge okse-spidsbryst?
    answer: Ja — se også okse-spidsbryst i mørkt øl. Kalv er mildere og passer bedre til æblesky.
  - question: For sød sauce?
    answer: Brug syrlige æbler, og finish med eddike. Undgå søde spiseæbler alene.
  - question: Skal hinden af?
    answer: Den sølvagtige hinde kan strammes under stegning — trim de tykkeste stykker, men lidt fedt er godt.
  - question: Tilbehør?
    answer: Kartoffelmos, brasede rødløg, eller ovnbagte rodfrugter.
body: |
  Braiseret kalvespidsbryst med æblesky er efterår på tallerkenen: mørt kalvekød og en sauce med syre fra æbler.

  Brun. Æbler i. Lav ovn.

  Det er den ret, der føles fin — uden at kræve fin teknik.
tip: Smag skysovsen til sidst med eddike. Æblerne giver sødme; syren gør den appetitlig i stedet for dessert-agtig.
'''


def parse_block(text: str) -> dict:
    data = {}
    mode = None
    body_lines = []
    current_q = None
    lines = text.splitlines()
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
    assert d.get("faq") and len(d["faq"]) >= 3, (d.get("slug"), len(d.get("faq", [])))
    assert d.get("tip"), d.get("slug")
    out = ROOT / d["category"]
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{d['slug']}.mdx"
    if path.exists():
        raise SystemExit(f"slug collision: {path}")
    path.write_text(to_mdx(d), encoding="utf-8")
    print("wrote", d["category"] + "/" + path.name)
