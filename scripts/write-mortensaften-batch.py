#!/usr/bin/env python3
"""Mortensaften batch — and, tilbehør og restemad (aug 2026)."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"
PUBLIC = Path(__file__).resolve().parent.parent / "public/recipes"
PUBLISHED = "2026-08-31"
IMG_SRC = PUBLIC / "grill" / "andesteg-paa-grill.jpg"

RECIPES = r'''
=====
title: Andesteg i airfryer
slug: andesteg-airfryer
category: airfryer
description: Andesteg i airfryer — hel and til Mortensaften med sprødt skind, kernetemperatur og saftigt kød uden ovn.
prepTime: PT30M
cookTime: PT1H15M
totalTime: PT14H45M
servings: 4
difficulty: mellem
tags:
  - andesteg
  - andesteg i airfryer
  - and
  - Mortensaften
  - jul
  - airfryer
  - festmad
imageAlt: Hel andesteg fra airfryeren med gyldent sprødt skind
featured: true
ingredients:
  - 1 hel and (2–2,5 kg)
  - 2 tsk salt
  - 1 tsk peber
  - 1 tsk paprika
  - Valgfrit fyld: 1 appelsin, 1 æble, rosmarin
steps:
  - Dagen før: tør anden. Score skindet på brystet i ruder. Salt hele anden. Stil åbent i køleskab natten over.
  - Tag ud 45 minutter før. Dup tør. Peber og paprika. Fyld evt. med appelsin og æble. Bind vinger.
  - Forvarm airfryer til 160 °C. Læg anden bryst opad i kurven eller lav ildfast form der passer.
  - Steg 55–70 minutter, til låret er 80–82 °C. Vend én gang hvis den ene side er bleg.
  - Boost 190 °C i 5–8 minutter til skindet knaser. Hvil 15 minutter.
  - Skær op. Server med rødkål og brunede kartofler.
faq:
  - question: Passer hel and i airfryer?
    answer: 2–2,5 kg ja — i de fleste XL-kurve. Større and skal i ovn eller på grill.
  - question: Hvilken kernetemperatur?
    answer: Låret 80–82 °C. Brystet er færdigt tidligere — hvil og skær, så saften løber tilbage.
  - question: Tørt bryst?
    answer: For høj varme for tidligt. Hold 160 °C til låret er tæt på, så kort skorpe-boost til sidst.
  - question: Mortensaften eller jul?
    answer: Samme andesteg. Tilbehør bestemmer højtiden — rødkål og brunede kartofler passer begge.
body: |
  Andesteg i airfryer er Mortensaften uden at fylde ovnen.

  Salt natten over. Lav varme. Termometer i låret. Kort høj finish til skindet.

  Det er ikke rotisseri — det er konvektion i en lille ovn. Fedtet skal dryppe væk, ikke dampe kødet blødt.
tip: Brug en lav form i kurven, så fedtet samles og ikke ryger op i skindet. Skum fedtet til sauce bagefter.
=====
title: Andesteg i trykkoger
slug: andesteg-trykkoger
category: trykkoger
description: Andesteg i trykkoger — mørt kød på under en time, sprødt skind i ovn eller airfryer bagefter.
prepTime: PT20M
cookTime: PT35M
totalTime: PT1H30M
servings: 4
difficulty: mellem
tags:
  - andesteg
  - andesteg trykkoger
  - and
  - Mortensaften
  - trykkoger
  - festmad
imageAlt: Andesteg fra trykkoger med gyldent skind efter finish
featured: true
ingredients:
  - 1 hel and (2–2,5 kg), delt i bryst og lår (eller hel hvis den passer)
  - 2 tsk salt, peber
  - 1 dl vand eller bouillon i bunden
  - 1 løg, halvt
  - Valgfrit: 1 appelsin i skiver
steps:
  - Salt anden. Dup tør. Læg i trykkoger med vand, løg og evt. appelsin.
  - Luk låg. Kog på høj tryk 25–30 minutter (naturlig eller hurtig frigivelse efter maskine).
  - Tag anden ud. Dup tør. Score skindet let.
  - Finish skind: 220 °C ovn 10–15 min, eller airfryer 190 °C 6–10 min, til knasende.
  - Hvil 10 minutter. Skær. Brug skyen fra trykkogeren som sauce-base.
faq:
  - question: Bliver skindet sprødt i trykkogeren?
    answer: Nej. Trykkogeren gør kødet mørt. Sprødhed kræver tør finish i ovn eller airfryer.
  - question: Hel and eller delt?
    answer: Delt giver bedre tryk og jævn mørhed. Hel and kræver større trykkoger og længere tid.
  - question: For kogt?
    answer: And tåler 80 °C i låret. Over det bliver brystet tørt — træk ved 78 °C og finish skind hurtigt.
  - question: Hvad med skyen?
    answer: Si den, skum fedt, kog ind med lidt rødvin eller portvin. Bedre end butikssauce.
body: |
  Andesteg i trykkoger er tids-besparelsen Mortensaften har brug for.

  Tryk gør kødet mørt. Ovnen gør skindet ærefuldt.

  To-trins: mørhed under låg, sprødhed under høj varme. Spring ikke finish-trinnet over.
tip: Dup anden knastørt før finish — vådt skind bliver gummi, uanset temperatur.
=====
title: Brunede kartofler til and
slug: brunede-kartofler-and
category: pande
description: Brunede kartofler til andesteg og Mortensaften — karamelliserede små kartofler i smør og sukker med salt balance.
prepTime: PT15M
cookTime: PT25M
totalTime: PT40M
servings: 4
difficulty: nem
tags:
  - brunede kartofler
  - kartofler
  - Mortensaften
  - jul
  - tilbehør
  - andesteg
  - pande
imageAlt: Brunede kartofler i pande med gylden karamelglace
featured: true
ingredients:
  - 800 g små kartofler, skrubbede
  - 40 g smør
  - 2 spsk sukker
  - 1 tsk salt
  - Friskkværnet peber
steps:
  - Kog kartoflerne møre i letsaltet vand, 15–20 minutter. Hæld af. Lad dampe tørre 2 minutter.
  - Smelt smør i bred pande på medium-høj varme. Læg kartofler i ét lag.
  - Rist 5–7 minutter, til gyldne pletter. Drys sukker over. Vend forsigtigt.
  - Karamelliser 3–5 minutter, til glace og brune kanter. Salt og peber. Server med det samme.
faq:
  - question: Kartoflerne falder fra hinanden?
    answer: Kog dem lige møre, ikke mos. Vend blidt. En revne er ok — det suger karamel.
  - question: Kan de laves forvejen?
    answer: Kog kartoflerne. Brun dem lige før servering. Genopvarmede brune kartofler bliver bløde.
  - question: Sukker eller honning?
    answer: Sukker giver klassisk brun glace. Honning brænder hurtigere — hold lavere varme.
  - question: Til and eller flæskesteg?
    answer: Begge. Det er det danske jule- og mortens-tilbehør par excellence.
body: |
  Brunede kartofler er fedtets bedste ven.

  Smør. Sukker. Salt. Små kartofler der tåler at blive vendt.

  De skal serveres varme — karamel og andefedt mødes på tallerkenen, ikke i køleskabet.
tip: Tør kartoflerne godt efter kogning. Våd kartoffel i varm pande = kog i stedet for brun.
=====
title: Æblekompot til and
slug: aeble-kompot-and
category: gryde
description: Æblekompot til andesteg — syrlig-sød kompot med kanel og lidt smør til Mortensaften og jul.
prepTime: PT10M
cookTime: PT20M
totalTime: PT30M
servings: 4
difficulty: nem
tags:
  - æblekompot
  - æbler
  - Mortensaften
  - jul
  - tilbehør
  - andesteg
  - gryde
imageAlt: Varm æblekompot i skål med kanel
featured: true
ingredients:
  - 4–5 syrlige æbler (fx Gravenstein), skrællede og i tern
  - 1 dl vand eller æblemost
  - 2 spsk sukker (juster efter æblets syre)
  - ½ tsk kanel
  - 1 spsk smør
  - Valgfrit: saft af ½ citron
steps:
  - Læg æbler, vand og sukker i gryde. Kog under låg 10–12 minutter, til møre men ikke mos.
  - Rør kanel og smør i. Smag til — syre fra citron hvis det er for sødt.
  - Server lun til andesteg. Kan spises kold dagen efter til rester.
faq:
  - question: Mos eller stykker?
    answer: Klassisk kompot har stykker. Mos æblerne let med gaffel, hvis du vil have tykkere konsistens.
  - question: Tørre æbler?
    answer: Brug syrlige sorter og nok væske. Gravenstein og Ingrid Marie er gode til and.
  - question: Kan den laves dagen før?
    answer: Ja. Opvarm lun eller server kold — begge dele virker til and.
  - question: Uden sukker?
    answer: Syrlige æbler + most kan klare sig med mindre. Andefedtet bærer sødmen.
body: |
  Æblekompot er syren der skærer gennem andefedtet.

  Syrlige æbler. Kort kogning. Smør til rundhed.

  Det er ikke dessert — det er tilbehør med attitude. Server ved siden af rødkål, ikke i stedet for.
tip: Gem en skål til dagen efter — æblekompot og andesandwich er et par.
=====
title: Andesandwich med rødkål
slug: andesandwich
category: airfryer
description: Andesandwich — restemad fra Mortensaften med sprød and, rødkål og sennep i ristet bolle.
prepTime: PT10M
cookTime: PT8M
totalTime: PT18M
servings: 2
difficulty: nem
tags:
  - andesandwich
  - restemad
  - Mortensaften
  - jul
  - sandwich
  - airfryer
imageAlt: Andesandwich med sprød and og rødkål i bolle
featured: true
ingredients:
  - 2 boller eller ciabatta, halveret
  - 200–250 g andekød med skind, i skiver
  - 2 spsk rødkål (hjemmelavet eller rester)
  - 1 spsk sennep eller mayo
  - Valgfrit: frisk salat, pickles
steps:
  - Varm airfryer til 180 °C. Læg andeskiver med skind opad på rist eller i kurv. Varm 4–5 minutter til skindet er sprødt.
  - Rist bollerne kort ved 160 °C, 2–3 minutter.
  - Smør sennep på boller. And, rødkål, evt. salat. Pres let sammen.
faq:
  - question: Tør and fra i går?
    answer: Varm den med skind opad i airfryer — fedtet genoplivs, skindet knaser igen.
  - question: Kold sandwich?
    answer: Ja, men varm and + sprødt skind er pointen. Restemad fortjener finish.
  - question: Hvilken bolle?
    answer: Ciabatta eller surdejsbolle der tåler fedt. Blød hotdog-bolle bliver sodden.
  - question: Andeburger i stedet?
    answer: Samme idé — se andeburger på grill. Her er det det danske jule- og mortensbrød.
body: |
  Andesandwich er grunden til at lave for meget and.

  Sprød genopvarmet skind. Syrlig rødkål. Sennep der tørster efter en øl.

  Det er ikke gourmet — det er fredag efter Mortensaften, og det smager bedre end det burde.
tip: Skær anden på tværs af skindet, så hver skive har skorpe — ellers er sandwich'et blødt i den ene ende.
=====
title: Ande-wok med grønt
slug: ande-wok
category: pande
description: Ande-wok — restemad fra andesteg med pak choi, forårsløg og soja-honning til hurtig middag dagen efter.
prepTime: PT10M
cookTime: PT8M
totalTime: PT18M
servings: 2
difficulty: nem
tags:
  - ande-wok
  - wok
  - restemad
  - Mortensaften
  - and
  - pande
imageAlt: Ande-wok i pande med grønt og sojasauce
featured: true
ingredients:
  - 250 g andekød uden skind, i strimler
  - 1 pak choi, i stykker
  - 2 forårsløg, i skrå skiver
  - 1 spsk soja
  - 1 tsk honning
  - 1 tsk sesamolie
  - 1 fed hvidløg, hakket
  - 1 spsk olie til pande
steps:
  - Bland soja, honning og sesamolie. Vend and i halvdelen af blandingen.
  - Høj varme i wok eller pande. Olie ind. And i — 1–2 minutter, til farve. Tag ud.
  - Pak choi og hvidløg 1 minut. And tilbage. Resten af saucen. Vend 30 sekunder.
  - Forårsløg over. Server med ris eller nudler.
faq:
  - question: Tør and i wok?
    answer: Strimler tynde. Høj varme kort. And er fed — du skal bruge varme, ikke tid.
  - question: Med skind?
    answer: Uden i wok. Gem skindet til sandwich — det bliver gummi i soja.
  - question: Frosne grøntsager?
    answer: Ja, men tørsautér dem først, så de ikke damper panden ned.
  - question: Hvad med rester af rødkål?
    answer: Vend det i til sidst — syre og sødme løfter wok'en.
body: |
  Ande-wok er restemad uden undskyldning.

  Tynde strimler. Het pande. Pak choi der stadig knaser.

  Du har allerede lavet festen — det her tager otte minutter og føles som takeaway med kant.
tip: Frys andestrimler i portioner, hvis du ved du laver wok senere på ugen — de tiner hurtigt i panden.
=====
title: Andeburger med rødkål
slug: andeburger
category: grill
description: Andeburger — sprød and, rødkål og sennep-mayo i brioche til restemad efter Mortensaften.
prepTime: PT15M
cookTime: PT10M
totalTime: PT25M
servings: 2
difficulty: nem
tags:
  - andeburger
  - burger
  - restemad
  - Mortensaften
  - jul
  - grill
imageAlt: Andeburger med sprød and og rødkål i brioche
featured: true
ingredients:
  - 2 brioche-burgerboller
  - 200 g andekød med skind, i skiver eller hele bryststykker
  - 2 spsk rødkål
  - 2 spsk mayo + 1 tsk sennep
  - Valgfrit: syltede agurker, salat
steps:
  - Bland mayo og sennep. Del boller. Smør indersiden let med smør.
  - Grill eller pande medium-høj: and med skind ned først 3–4 min, vend, 2–3 min mere til sprødt.
  - Rist bollerne kort på grillen. Byg: sauce, and, rødkål, top.
faq:
  - question: Hvorfor burger efter Mortensaften?
    answer: Fordi rester smager bedst som noget nyt. Andeburger er jule- og mortens-streetfood.
  - question: Hel bryst eller skiver?
    answer: Hele lille bryststykke med skind er teatret. Skiver er nemmere at tygge.
  - question: Gas eller kul?
    answer: Begge. Indirekte varme + kort direkte til skindet. Pande virker også.
  - question: Ost?
    answer: Skip. Andefedt + rødkål er nok fede lag.
body: |
  Andeburger er Mortensaften dagen to.

  Sprødt skind som bacon. Rødkål som coleslaw med attitude. Brioche der sluger fedtet.

  Det er ikke fusion — det er restemad med selvrespekt.
tip: Pres burgeren let med spatlen efter samling — skindet knaser bedre mod bolle.
=====
title: Andelår i airfryer
slug: andelaar-airfryer
category: airfryer
description: Andelår i airfryer — sprødt skind og mørt kød til Mortensaften når hel and er for meget.
prepTime: PT15M
cookTime: PT35M
totalTime: PT50M
servings: 2
difficulty: nem
tags:
  - andelår
  - and
  - Mortensaften
  - jul
  - airfryer
  - festmad
imageAlt: Andelår fra airfryer med sprødt skind
featured: true
ingredients:
  - 2 andelår (ca. 400–500 g i alt)
  - 1 tsk salt, peber
  - ½ tsk paprika
  - Valgfrit: 1 tsk honning til glaze
steps:
  - Dup lårene tørre. Score skindet let. Salt, peber, paprika.
  - Forvarm til 170 °C. Læg lårene med skind opad.
  - Steg 25–30 minutter, til kødet er 80 °C ved benet.
  - Pensl evt. honning. 190 °C i 5 minutter til sprødt skind. Hvil 5 minutter.
faq:
  - question: Bedre end hel and?
    answer: Til to personer — ja. Mindre setup, samme smag, kortere tid.
  - question: Rå ved benet?
    answer: Stik termometer ved thickest part, ikke mod ben. 80 °C i kødet er målet.
  - question: Med rødkål?
    answer: Klassisk par. Se klassisk rødkål og brunede kartofler på Saltet.
  - question: Kan lårene marineres?
    answer: Salt natten over som hel and. Våd marinade gør skindet slattent — tør før varme.
body: |
  Andelår i airfryer er Mortensaften i miniformat.

  Score skind. Termometer. Kort høj finish.

  To lår, fuld fest — uden at binde en hel and.
tip: Læg lårene på rist i kurven, så fedt drypper væk — ellers steger de i eget fedt og bliver bløde.
=====
title: Andesteg på plancha
slug: andesteg-plancha
category: plancha
description: Andebryst på plancha — sprødt skind og saftigt kød med høj varme til Mortensaften for to.
prepTime: PT15M
cookTime: PT20M
totalTime: PT35M
servings: 2
difficulty: mellem
tags:
  - andesteg
  - andebryst
  - plancha
  - Mortensaften
  - festmad
imageAlt: Andebryst på plancha med sprødt skind
featured: true
ingredients:
  - 2 andebryster med skind (ca. 350–400 g)
  - 1 tsk salt, peber
  - Valgfrit: timian, honning til glaze
steps:
  - Score skind i ruder. Salt generøst. Dup tør. Tag ud 15 minutter før.
  - Plancha eller støbejernspande meget varm. Andebryst skind ned — pres let 30 sekunder.
  - Skru ned til medium. 6–8 minutter skind ned, til gylden. Vend. 4–6 minutter til 54–56 °C i midten.
  - Hvil 5 minutter. Skær på skrå. Glasér evt. med honning under sidste minut skind ned.
faq:
  - question: Plancha eller almindelig pande?
    answer: Begge — det handler om høj startvarme og tør overflade. Plancha giver jævnere skorpe.
  - question: Rosa andebryst?
    answer: Ja. 54–56 °C i midten. Over 60 °C bliver det tørt — andebryst er ikke kylling.
  - question: Fedt overalt?
    answer: Skær overskydende fedt fra skindet før stegning. Tøm fedt fra pladen undervejs.
  - question: Til to personer?
    answer: Præcis. To bryster på plancha slår halv and i ovn til en lille middag.
body: |
  Andebryst på plancha er Mortensaften uden ovn-tid.

  Varm plade. Skind ned. Termometer i tykkeste del.

  Det er steak-logik på and — høj varme, kort tid, rosa midte.
tip: Skær et net i skindet — kryds, ikke dybt. Skindet flader ud og sprødes jævnere på pladen.
=====
title: Andesky til andesteg
slug: andesky
category: dips
description: Andesky — sauce af andefedt, fond og eddike til Mortensaften. Brug skyen fra stegningen.
prepTime: PT5M
cookTime: PT15M
totalTime: PT20M
servings: 4
difficulty: nem
tags:
  - andesky
  - sauce
  - andesteg
  - Mortensaften
  - jul
  - dip
imageAlt: Brun andesky i saucekande
featured: true
ingredients:
  - 2 spsk andefedt fra stegningen
  - 2 spsk hvedemel
  - 3 dl andefond eller bouillon
  - 1 spsk rød eddike eller portvin
  - Salt, peber
  - Valgfrit: 1 spsk syltet saft fra rødkål
steps:
  - Hæld fedt fra anden i gryde — gem 1 spsk til roux. Skum evt. resten eller brug det hele til smag.
  - Rør mel i fedtet 1 minut. Pisk fond i under omrøring. Simre 5–8 minutter.
  - Tilsæt eddike og evt. rødkålsaft. Smag til. Si hvis klumper.
faq:
  - question: Ingen sky fra min and?
    answer: Brug bouillon + 1 tsk soya for dybde. Smør + mel giver stadig body.
  - question: For fed?
    answer: Skum fedtet før roux. Gem andefedt til kartofler — sauce skal være silke, ikke olie.
  - question: Kan den fryses?
    answer: Ja, uden mel kan du fryse sky. Lav roux ved genopvarmning.
  - question: Portvin i stedet for eddike?
    answer: Ja — sødme til syre. Mortensaften-klassiker med rødkål.
body: |
  Andesky er det fedt du allerede har betalt for.

  Fedt. Mel. Fond. Eddike der skærer.

  Skyen fra fadet er bedre end tube — brug den, eller bouillon uden at undskylde.
tip: Si saucen før servering — rødkål-rester i skyen er gourmet, men klumper i gryden er ikke.
=====
title: Rødbeder til and
slug: rodbeder-til-and
category: gryde
description: Rødbeder til andesteg — varme rødbeder med eddike og sukker til Mortensaften ved siden af rødkål.
prepTime: PT10M
cookTime: PT25M
totalTime: PT35M
servings: 4
difficulty: nem
tags:
  - rødbeder
  - tilbehør
  - Mortensaften
  - jul
  - andesteg
  - gryde
imageAlt: Varme rødbeder i skål til andesteg
featured: true
ingredients:
  - 4–5 friske rødbeder (eller 1 glas færdige), i tern eller både
  - 1 spsk smør
  - 1 spsk sukker
  - 1 spsk eddike
  - Salt, peber
steps:
  - Friske rødbeder: kog møre i letsaltet vand, 25–35 min. Skyl, skræl, skær.
  - Smelt smør. Rødbeder i. Svits 2 minutter. Sukker og eddike i. Simre 5 minutter under låg.
  - Smag til. Salt og peber. Server lun til and.
faq:
  - question: Friske eller glas?
    answer: Glas er hurtigere — dræn og varm i smør-eddike. Friske smager jordnært og sødere.
  - question: Forskel på rødkål?
    answer: Rødkål er langtidskogt kål. Rødbeder er jord, sødme og syre — begge hører til and.
  - question: Dagen før?
    answer: Ja. Varm op i gryde med lidt smør. Farven er fest — beskyt dit tøj ved skrælling.
  - question: Med appelsin?
    answer: Riv skal af ½ appelsin til sidst — klassisk nordisk kombination til andefedt.
body: |
  Rødbeder til and er farve og syre på tallerkenen.

  Kog. Skræl. Varm i eddike og smør.

  De lever ved siden af rødkål — ikke i stedet for. To røde, to teksturer.
tip: Brug handsker ved friske rødbeder — eller riv dem med skræl på i gryden og si bagefter.
=====
title: Ande-tacos med rødkål
slug: ande-tacos
category: pande
description: Ande-tacos — restemad med sprød and, rødkål og lime til løs hverdag efter Mortensaften.
prepTime: PT10M
cookTime: PT10M
totalTime: PT20M
servings: 2
difficulty: nem
tags:
  - ande-tacos
  - tacos
  - restemad
  - Mortensaften
  - pande
imageAlt: Ande-tacos med rødkål og lime
featured: true
ingredients:
  - 8 små tortillas
  - 200 g andekød, i strimler
  - 1 spsk rødkål eller syltet rødkål
  - ½ lime, saft
  - 2 spsk creme fraiche eller skyr
  - Valgfrit: koriander, chili
steps:
  - Varm and i pande på høj varme til skind/kød er varmt og let sprødt.
  - Varm tortillas i tør pande eller over gasblus.
  - Fordel and, rødkål, creme fraiche, lime og koriander. Fold og spis.
faq:
  - question: Hårde eller bløde tacos?
    answer: Bløde tortillas til dansk and — sprød skal komme fra anden, ikke skallen.
  - question: Hvad med syltet rødkål fra glas?
    answer: Perfekt. Syre og sødme uden ekstra arbejde.
  - question: Meal prep?
    answer: Opbevar and og rødkål adskilt. Varm and, byg tacos til sidst.
  - question: Barnet gider rødkål?
    answer: Skyr + lime uden kål. And i tortilla er stadig en sejr.
body: |
  Ande-tacos er restemad der ikke føles som rester.

  Varm and. Syrlig rødkål. Lime der vækker fedtet.

  Det tager ti minutter og omgår hele diskussionen om «hvad skal vi spise i morgen».
tip: Riv skindet fra og steg det separat sprødt — drys som «bacon» over tacos.
=====
title: Andesteg i støbejernsgryde
slug: andesteg-stobejern
category: stobejern
description: Andesteg i støbejern — hel and i Dutch Oven med låg og ovn-finish til sprødt skind til Mortensaften.
prepTime: PT25M
cookTime: PT1H30M
totalTime: PT2H15M
servings: 4
difficulty: mellem
tags:
  - andesteg
  - støbejern
  - Mortensaften
  - jul
  - festmad
imageAlt: Andesteg i støbejernsgryde med sprødt skind
featured: true
ingredients:
  - 1 hel and (2–2,5 kg)
  - 2 tsk salt, peber
  - 2 spsk andefedt eller smør
  - 1 løg, kvart
  - Valgfrit: æbler og svesker i bunden
steps:
  - Salt anden natten over, tør. Forvarm ovn 180 °C. Varm støbejernsgryde på komfuret.
  - Brun anden let på alle sider i fedt. Læg løg og evt. frugt i bunden. Låg på.
  - Ovn 90 minutter. Tag låg af. 220 °C i 15–20 min til sprødt skind. Hvil 15 min.
faq:
  - question: Hvorfor støbejern?
    answer: Jævn varme, god fond i bunden, låg holder saften — så høj finish uden låg til skind.
  - question: Dutch Oven størrelse?
    answer: 6–7 liter til 2–2,5 kg and. Anden skal have plads — ellers damper den.
  - question: Samme som ovnfad?
    answer: Ja, men støbejernet giver bedre stegeskorpe i bunden og fond til andesky.
  - question: På bål?
    answer: Muligt med gløder ovenpå låg — se bålmad-guiden. Ovn er nemmere til Mortensaften.
body: |
  Andesteg i støbejern er ovn-metoden med ekstra fond.

  Brun. Låg. Høj finish uden låg.

  Gryden giver sky du faktisk vil spise — ikke bare fedt i bagepapir.
tip: Tag anden op på rist de sidste minutter, hvis bunden er våd — skindet skal tørres mod varmen.
=====
title: Kartoffelmos med andefedt
slug: kartoffelmos-andefedt
category: gryde
description: Kartoffelmos med andefedt — cremet mos til Mortensaften og jul når anden efterlader guld i fadet.
prepTime: PT10M
cookTime: PT25M
totalTime: PT35M
servings: 4
difficulty: nem
tags:
  - kartoffelmos
  - andefedt
  - tilbehør
  - Mortensaften
  - jul
  - gryde
imageAlt: Fløjlsblød kartoffelmos med andefedt
featured: true
ingredients:
  - 1 kg kartofler, skrællede
  - 3–4 spsk andefedt fra stegningen (eller smør)
  - 1 dl varm mælk
  - Salt, peber
  - Valgfrit: muskatnød
steps:
  - Kog kartofler møre. Hæld af. Damp tør 1 minut.
  - Mos med andefedt og varm mælk. Smag til. Si hvis du vil have silke — ellers rustikt.
  - Hold varm til anden er klar. Top med ekstra fedt og peber ved servering.
faq:
  - question: For fedt?
    answer: Brug halv fedt, halv smør. Andefedt er smagen — uden det er det almindeligt mos.
  - question: Gemme fedt fra anden?
    answer: Si til glas i køl. Fedtlaget er guld til mos og brunede kartofler dagen efter.
  - question: Kan mos laves før?
    answer: Ja. Varm i gryde med lidt mælk under omrøring — mikro gør det gummi.
  - question: Med skind i mos?
    answer: Nej. Det er fedt og fond du vil have — ikke skind-chips i mos.
body: |
  Kartoffelmos med andefedt er grunden til at gemme fadet.

  Fedt fra anden. Varm mælk. Salt.

  Det er ikke sundt. Det er Mortensaften — og det smager præcis som det skal.
tip: Si fedtet fra fadet før du hælder — brune bidder i mos er sauce, ikke tekstur.
=====
title: Confit-andelår med rodfrugter
slug: confit-andelaar-pande
category: pande
description: Confit-andelår — møre lår i andefedt med rodfrugter til alternativ Mortensaften uden hel and.
prepTime: PT20M
cookTime: PT1H30M
totalTime: PT1H50M
servings: 2
difficulty: mellem
tags:
  - confit
  - andelår
  - Mortensaften
  - and
  - pande
  - festmad
imageAlt: Confit-andelår med rodfrugter i pande
featured: true
ingredients:
  - 2 andelår
  - 400 ml andefedt eller neutral olie + 2 spsk andefedt
  - 2 gulerødder, i skiver
  - 2 pastinakker, i skiver
  - 4 kartoffler, i halve
  - Salt, timian
steps:
  - Salt lårene. Læg i small gryde/pande. Dæk med smeltet fedt/olie. Simre 75–90 min på lav varme, til møre.
  - Tag lårene op. Skru op til medium. Brun skindet 2–3 min per side. Tag ud.
  - Steg rodfrugter i fedtet til gyldne. Server lår på rodfrugt-bund.
faq:
  - question: Virkelig confit?
    answer: Ja — langsom i fedt. Du kan bruge ovn 120 °C i stedet for blus, hvis panden er ovnfast.
  - question: Sprødt skind?
    answer: Fedt gør kødet mørt — brun skindet hårdt til sidst i tør pande eller under grill.
  - question: Hvor meget fedt?
    answer: Lårene skal være næsten dækket. Gem fedtet — det er guld til næste gang.
  - question: Til to?
    answer: Præcis. Confit-andelår er Mortensaften uden gæster og uden hel fugl.
body: |
  Confit-andelår er Mortensaften for dem der vil have mørhed før teater.

  Fedt. Lav varme. Hård finish på skindet.

  Rodfrugterne steger i samme fedt — det er one-pan fest uden at lyde som meal-prep-bro.
tip: Gem confit-fedtet si'et — brug det til brunede kartofler dagen efter. Det er to middage i ét fad.
'''


def parse_block(text: str) -> dict:
    lines = text.strip().split("\n")
    data: dict = {}
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
        elif line.startswith("featured: "):
            data["featured"] = line[10:]
        elif line.startswith("imageAlt: "):
            data["imageAlt"] = line[10:]
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
written = []
for b in blocks:
    d = parse_block(b)
    if not d.get("ingredients"):
        continue
    assert d.get("faq") and len(d["faq"]) >= 3, d.get("slug")
    assert d.get("tip")
    out = ROOT / d["category"]
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{d['slug']}.mdx"
    if path.exists():
        raise SystemExit(f"slug collision: {path}")
    path.write_text(to_mdx(d), encoding="utf-8")
    written.append((d["category"], d["slug"]))
    print("wrote", d["category"] + "/" + path.name)

for cat, slug in written:
    dest = PUBLIC / cat / f"{slug}.jpg"
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists() and IMG_SRC.exists():
        shutil.copy2(IMG_SRC, dest)
        print("image", dest.relative_to(PUBLIC.parent))

print(f"done: {len(written)} recipes")
