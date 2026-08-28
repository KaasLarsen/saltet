#!/usr/bin/env python3
"""20 uundværlige sovse — gaps (aug 2026). Eksisterende: brun-sovs, bearnaisesovs, chimichurri, bearnaise-mayo, BBQ-whiskeysauce."""
from pathlib import Path

ROOT = Path("/Users/dklarsen/Desktop/saltet/content/recipes")
PUBLISHED = "2026-08-27"

RECIPES = r'''
=====
title: Klassisk rødvinssauce
slug: roedvinssauce
category: dips
description: Klassisk rødvinssauce — indkogt på sjalotteløg, oksefond og god rødvin, monteret med koldt smør.
prepTime: PT10M
cookTime: PT25M
totalTime: PT35M
servings: 4
difficulty: mellem
tags:
  - rødvinssauce
  - rødvin
  - fond
  - sauce
  - bøf
  - fransk
imageAlt: Blank, mørk rødvinssauce i skål med sjalotteløg
featured: true
ingredients:
  - 2 sjalotteløg, finthakket
  - 1 spsk smør + 1 spsk olie til svitsning
  - 3 dl tør rødvin (en du også vil drikke)
  - 3 dl oksefond eller god oksebouillon
  - 1 kvist timian, 1 laurbærblad
  - 50–75 g koldt usaltet smør i tern
  - Salt og friskkværnet peber
steps:
  - Svits sjalotteløg i smør og olie på middel varme 3–4 minutter, til de er bløde uden farve.
  - Hæld rødvinen i. Kog ind til ca. 1 dl — alkoholen skal dampe af, og vinen skal smage koncentreret, ikke rå.
  - Tilsæt fond, timian og laurbær. Simre 10–15 minutter, til saucen nappe en ske. Si gennem fin si. Smag — den skal være næsten for skarp, før smørret.
  - Tag af varmen. Visp koldt smør i lidt ad gangen (monter au beurre), til saucen er blank og silkeagtig. Salt og peber til sidst.
faq:
  - question: Hvilken vin?
    answer: Tør, mellemfyldig rødvin — pinot noir, tempranillo eller en billig bordeaux. Aldrig «madlavningsvin» du ikke vil drikke. Se også fond- og reduktionsguiden.
  - question: Kan jeg bruge bouillonterning?
    answer: Ja til hverdag — men reducér forsigtigt, og salt til sidst. Rigtig fond giver gelatine og glans.
  - question: Saucen skilles?
    answer: For varmt under monteringen. Af varmen, en skefuld kold fond eller et koldt smørterning, visp.
  - question: Til hvad?
    answer: Culotte, tournedos, oksemørbrad og vildt. Server ved siden af — ikke over stegen før den hviler.
body: |
  Klassisk rødvinssauce er reduktion plus montering: vin indkogt, fond til krop, koldt smør til glans.

  Vinen skal kunne drikkes. Brændt, billig vin bliver bitter sauce.

  Teknikken er den samme som i [saucer på fond og reduktion](/guides/saucer-fond-reduktion).
tip: Salt først når smørret er i — reduktionen koncentrerer saltet hårdt.
=====
title: Hvidvinssauce med fløde
slug: hvidvinssauce-floede
category: dips
description: Hvidvinssauce med fløde — syrlig, fed og cremet sovs til fisk, kylling og pasta.
prepTime: PT10M
cookTime: PT20M
totalTime: PT30M
servings: 4
difficulty: nem
tags:
  - hvidvinssauce
  - hvidvin
  - fløde
  - fisk
  - kylling
  - sauce
imageAlt: Cremet hvidvinssauce i skål med frisk persille
featured: true
ingredients:
  - 2 sjalotteløg, finthakket
  - 1 spsk smør
  - 2 dl tør hvidvin
  - 1 dl hønse- eller fiskefond (eller bouillon)
  - 2 dl piskefløde
  - 1 spsk citronsaft
  - Salt, hvid peber, finthakket persille
steps:
  - Svits sjalotteløg i smør 2–3 minutter uden farve.
  - Hæld hvidvin i. Kog ind til ca. ½ dl — skarp, koncentreret, uden rå alkohol.
  - Tilsæt fond. Simre 3 minutter. Fløde i. Simre 5–8 minutter, til saucen tykner og frakker en ske.
  - Tag af varmen. Citronsaft, salt, peber og persille. Smag — den skal balancere syre og fedme.
faq:
  - question: Hvilken hvidvin?
    answer: Tør — chenin blanc, sauvignon blanc eller pinot gris. Undgå sød riesling.
  - question: Til fisk eller kylling?
    answer: Begge. Til fisk: brug fiskefond hvis du har. Til kylling: hønsefond.
  - question: For tynd?
    answer: Simre videre uden låg. Undgå mel — fløden og indkogningen er jævningen.
  - question: Kan den laves i forvejen?
    answer: Ja — køl, og varm forsigtigt. Tilsæt frisk citron og persille lige før servering.
body: |
  Hvidvinssauce med fløde er den ultimative hverdagssauce til fisk og kylling: syre fra vinen, krop fra fløden.

  Indkog vinen først. Fløde ovenpå rå vin smager af vinbar-fejl.
tip: Citronsaft til sidst — kogt citron bliver bitter.
=====
title: Portvinssovs
slug: portvinssovs
category: dips
description: Portvinssovs — sødlig, kraftig sovs til mørbradbøffer, and og efterårets vildt.
prepTime: PT10M
cookTime: PT20M
totalTime: PT30M
servings: 4
difficulty: mellem
tags:
  - portvinssovs
  - portvin
  - vildt
  - mørbrad
  - sauce
  - efterår
imageAlt: Blank, mørkerød portvinssovs i skål
featured: true
ingredients:
  - 2 sjalotteløg, finthakket
  - 1 spsk smør + 1 spsk olie
  - 2 dl ruby eller tawny portvin
  - 2½ dl okse- eller vildtfond
  - 1 spsk ribsgele eller solbærgele (valgfrit)
  - 40 g koldt smør i tern
  - Salt og peber
steps:
  - Svits sjalotteløg i smør og olie 3 minutter.
  - Hæld portvin i. Kog ind til ca. ¾ dl — sød, sirupagtig, uden skarp alkohol.
  - Fond i. Simre 8–12 minutter, til den nappe. Si. Rør gele i hvis du vil have ekstra dybde.
  - Af varmen: visp koldt smør i. Salt og peber. Den skal være blank og lidt klæbrig.
faq:
  - question: Ruby eller tawny?
    answer: Ruby er frugtigt og klassisk til kød. Tawny er nøddeagtig og mildere. Begge virker.
  - question: For sød?
    answer: Mere fond, et stænk rødvinseddike, eller spring gele over.
  - question: Til hvad?
    answer: Svinemørbrad, andebryst, rådyr og culotte om efteråret.
  - question: Uden fond?
    answer: God oksebouillon + 1 tsk soja. Reducér lidt længere.
body: |
  Portvinssovs er efterårets tungere søster til rødvinssauce: sødlig, kraftig og bygget til mørbrad og vildt.

  Porten skal koges ind, ellers smager det af dessertvin på bøffen.
tip: Server lidt — den er intens. En kande er for meget.
=====
title: Champagnesauce
slug: champagnesauce
category: dips
description: Champagnesauce — luksus-hvidvinssauce på mousserende vin, fond og fløde til gæstebud og fisk.
prepTime: PT10M
cookTime: PT20M
totalTime: PT30M
servings: 4
difficulty: mellem
tags:
  - champagnesauce
  - champagne
  - mousserende
  - fisk
  - luksus
  - sauce
imageAlt: Lys, cremet champagnesauce i elegant skål
featured: true
ingredients:
  - 2 sjalotteløg, finthakket
  - 1 spsk smør
  - 2½ dl tør champagne, cava eller crémant
  - 1 dl fiskefond eller hønsefond
  - 2 dl piskefløde
  - 1 spsk citronsaft
  - Salt, hvid peber, evt. finthakket estragon
steps:
  - Svits sjalotteløg i smør uden farve.
  - Hæld mousserende vin i. Kog ind til ca. ¾ dl — boblerne skal væk, smagen blive koncentreret.
  - Fond og fløde i. Simre 6–10 minutter, til saucen er cremet og frakker skeen.
  - Af varmen: citron, salt, peber og evt. estragon. Smag — den skal være lys, fed og syrlig.
faq:
  - question: Skal det være ægte champagne?
    answer: Nej. God tør cava eller crémant gør det samme job til en tredjedel af prisen. Undgå sød prosecco.
  - question: Til hvad?
    answer: Pighvar, torsk, kammuslinger, kyllingebryst og nytårsmad.
  - question: Kan jeg bruge stille hvidvin?
    answer: Ja — se [hvidvinssauce med fløde](/opskrifter/dips/hvidvinssauce-floede). Champagne giver bare ekstra umami og fest.
  - question: Skiller den?
    answer: For hård kogning efter fløden. Simre stille, og rør.
body: |
  Champagnesauce er luksusudgaven af hvidvinssaucen: samme teknik, mere umami og boble-syre til gæstebudene.

  Du drikker resten af flasken til maden. Det er pointen.
tip: Åbn flasken til saucen — gårdagens flade rester mangler syre.
=====
title: Balsamicosauce
slug: balsamicosauce
category: dips
description: Balsamicosauce — tyk, indkogt glaseringssovs med dybde til stegt kød, and og grillgrønt.
prepTime: PT5M
cookTime: PT20M
totalTime: PT25M
servings: 4
difficulty: nem
tags:
  - balsamicosauce
  - balsamico
  - glasering
  - sauce
  - and
  - bøf
imageAlt: Tykt, blank balsamicoglaze dryppet på ske
featured: true
ingredients:
  - 2 dl god balsamicoeddike
  - 1 dl oksefond eller bouillon
  - 1 spsk honning eller brun farin
  - 1 sjalotteløg, finthakket (valgfrit)
  - 1 spsk smør
  - Salt og peber
steps:
  - Svits evt. sjalotteløg i smør 2 minutter. Hæld balsamico og fond i. Honning i.
  - Simre uden låg 12–18 minutter, til saucen er sirupagtig og frakker skeen — den tykner mere når den køler.
  - Smag til med salt og peber. Si hvis du brugte sjalotteløg.
  - Server skefuldvis som glasering eller dip ved siden af kødet.
faq:
  - question: Billig balsamico?
    answer: Den virker til indkog, men smager skarpere. En bedre flaske giver blødere dybde. Undgå «balsamico-creme» fra tube som base.
  - question: For sur?
    answer: Mere honning, eller en klatt koldt smør til sidst.
  - question: Til hvad?
    answer: Andebryst, culotte, grillede grøntsager, burrata og ovnstegte tomater.
  - question: Holdbarhed?
    answer: En uge i køleskab. Varm forsigtigt — den brænder nemt.
body: |
  Balsamicosauce er glasering, ikke dressering: indkogt, blank og koncentreret.

  Stop før den bliver tjære. Den sætter sig yderligere af varmen.
tip: Pensl kød de sidste 2 minutter — ellers brænder sukkeret.
=====
title: Mornay-sauce
slug: mornay-sauce
category: dips
description: Mornay-sauce — den klassiske ostesovs på béchamel med gruyère og parmesan til lasagne og blomkålsgratin.
prepTime: PT10M
cookTime: PT20M
totalTime: PT30M
servings: 6
difficulty: mellem
tags:
  - mornay
  - ostesovs
  - béchamel
  - lasagne
  - gratin
  - sauce
imageAlt: Cremet mornay-sauce med smeltet ost i gryde
featured: true
ingredients:
  - 40 g smør
  - 40 g hvedemel
  - 5 dl sødmælk (lun)
  - 80 g gruyère eller emmentaler, reven
  - 40 g parmesan, reven
  - 1 knivspids muskatnød
  - Salt og hvid peber
steps:
  - Smelt smør. Rør mel i, og bag rouxen 1–2 minutter uden farve — den skal dufte nødder, ikke brænde.
  - Tilsæt lun mælk lidt ad gangen under piskning. Bring i kog, og simre 5–8 minutter, til béchamelen er glat og tyk.
  - Tag af varmen. Rør ostene i, til de er smeltet. Muskat, salt og peber. Den skal være blank og elastisk — ikke gummiagtig.
faq:
  - question: Er mornay bare ostesovs?
    answer: Mornay er béchamel med ost. Den er grundstenen i lasagne, blomkålsgratin og croque monsieur.
  - question: Hvilken ost?
    answer: Gruyère + parmesan er klassik. Cheddar virker, men smager mere «britisk».
  - question: Klumper?
    answer: Lun mælk, og pisk hårdt. Si i nød. Start aldrig med kold mælk i kold roux.
  - question: Kan den fryses?
    answer: Béchamel ja. Med ost: bedre frisk — osten kan blive grynet efter optøning.
body: |
  Mornay-sauce er ostesovsen over dem alle: béchamel med gruyère og parmesan.

  Det er lasagnens skjulteskelet og mormors blomkålsgratin i én gryde.
tip: Ost af varmen — kogt ost bliver sej og olieret.
=====
title: Gorgonzolasovs
slug: gorgonzolasovs
category: dips
description: Gorgonzolasovs — tung blåskimmelsovs med fløde til bøf, pasta og ovnbagte kartofler.
prepTime: PT5M
cookTime: PT15M
totalTime: PT20M
servings: 4
difficulty: nem
tags:
  - gorgonzolasovs
  - gorgonzola
  - blåskimmel
  - fløde
  - bøf
  - pasta
  - sauce
imageAlt: Cremet gorgonzolasovs i skål med blåskimmel
featured: true
ingredients:
  - 1 sjalotteløg, finthakket
  - 1 spsk smør
  - ½ dl hvidvin (valgfrit)
  - 2½ dl piskefløde
  - 150 g gorgonzola (dolce eller piccante)
  - Friskkværnet peber
  - Evt. 1 tsk citronsaft
steps:
  - Svits sjalotteløg i smør 2 minutter. Evt. hvidvin i, kog ind til næsten tørt.
  - Fløde i. Simre 4–5 minutter.
  - Smuldr gorgonzola i. Rør på lav varme, til osten er smeltet, og saucen er jævn. Ikke i hård kog.
  - Peber og evt. citron. Smag — den er salt nok fra osten; salt kun hvis nødvendigt.
faq:
  - question: Dolce eller piccante?
    answer: Dolce er blødere og cremet. Piccante er skarpere — mere «herresovs» til bøf.
  - question: Til pasta eller bøf?
    answer: Begge. Til pasta: lidt pasta-kogevand i. Til bøf: tykkere, serveret ved siden af.
  - question: Kan jeg bruge danablu?
    answer: Ja. Samme teknik. Smag dig frem — danablu er ofte saltere.
  - question: Forskel på gorgonzolasmør?
    answer: [Gorgonzolasmør](/opskrifter/dips/gorgonzola-smoer) er koldt smør. Denne er varm flødesauce.
body: |
  Gorgonzolasovs er den tunge herresovs: blåskimmel, fløde og en pande, der lige har haft bøf på.

  Den skal smelte, ikke koge. Hård kog gør osten grynet.
tip: Lav den i bøffens pande — stegeskyen er gratis umami.
=====
title: Parmesansovs med hvidløg
slug: parmesansovs-hvidloeg
category: dips
description: Parmesansovs med hvidløg — cremet, saltet hvid sovs til pasta, ovnkartofler og grønt.
prepTime: PT10M
cookTime: PT15M
totalTime: PT25M
servings: 4
difficulty: nem
tags:
  - parmesansovs
  - parmesan
  - hvidløg
  - pasta
  - sauce
  - cremet
imageAlt: Cremet parmesansovs med hvidløg i skål
featured: true
ingredients:
  - 2 spsk smør
  - 3 fed hvidløg, finthakket
  - 1 spsk hvedemel
  - 3 dl sødmælk eller 2 dl mælk + 1 dl fløde
  - 80 g parmesan, fint reven
  - Salt, peber, evt. muskat
steps:
  - Smelt smør. Svits hvidløg 30–60 sekunder uden farve — brændt hvidløg ødelægger saucen.
  - Drys mel i. Rør 30 sekunder. Tilsæt mælk lidt ad gangen under piskning.
  - Simre 5 minutter, til den tykner. Tag af varmen. Rør parmesan i. Smag til.
faq:
  - question: Frisk reven eller færdigrevet?
    answer: Frisk. Færdigrevet indeholder stivelse og smelter dårligere.
  - question: Til pasta?
    answer: Ja — tilsæt pasta-kogevand til den rigtige konsistens. Den skal binde, ikke plaske.
  - question: For tyk?
    answer: Mere mælk. For tynd: mere parmesan eller 1 minut ekstra simren.
  - question: Vegansk?
    answer: Ikke denne. Brug næringsgær + plantefløde som anden sauce.
body: |
  Parmesansovs med hvidløg er den intensive hvide sovs: salt, umami og hvidløg uden at blive alfredo-slatten.

  Hvidløg skal dufte, ikke brune.
tip: Riv parmesanen på microplane — den smelter ind uden klumper.
=====
title: Cheddar-ostesovs
slug: cheddar-ostesovs
category: dips
description: Cheddar-ostesovs fra bunden — ægte nacho-cheese med cheddar, mælk og sennep, uden pap-tuben.
prepTime: PT10M
cookTime: PT15M
totalTime: PT25M
servings: 6
difficulty: nem
tags:
  - cheddar
  - ostesovs
  - nacho cheese
  - nachos
  - sauce
  - dip
imageAlt: Flydende cheddar-ostesovs hældt over nachos
featured: true
ingredients:
  - 30 g smør
  - 30 g hvedemel
  - 4 dl sødmælk (lun)
  - 200 g mild eller sharp cheddar, reven
  - 1 tsk dijonsennep
  - ½ tsk paprika eller røget paprika
  - Salt, peber, evt. et skud hot sauce
steps:
  - Lav en lys roux: smør + mel 1 minut. Tilsæt lun mælk under piskning. Simre 4–5 minutter til tyk béchamel.
  - Tag af varmen. Rør cheddar i portioner, til den er smeltet og blank. Dijon, paprika, salt, peber og evt. hot sauce.
  - Hold lun over vandbad eller meget lav varme under omrøring — den må ikke koge efter osten er i.
faq:
  - question: Hvorfor skilles min nacho-cheese?
    answer: For høj varme efter osten. Af varmen, og rør. En skefuld mælk redder ofte.
  - question: American cheese?
    answer: Den smelter stabilt, men smager af tube. Denne opskrift er cheddar fra bunden.
  - question: Til hvad?
    answer: Nachos, pommes, broccoli, hotdogs og loaded potatoes.
  - question: Kan den genopvarmes?
    answer: Ja, forsigtigt med ekstra mælk. Undgå mikrobølge på fuld effekt.
body: |
  Cheddar-ostesovs er flydende guld fra bunden — lysår over færdigkøbt nacho-cheese.

  Sennepen er ikke til smag alene: den hjælper emulsionen.
tip: Riv osten selv. Færdigrevet cheddar klumper lettere.
=====
title: Ultimativ pandesovs
slug: pandesovs
category: pande
description: Ultimativ pandesovs — deglazér støbejernspanden efter bøffen med cognac eller vin, og pisk op med fløde.
prepTime: PT5M
cookTime: PT10M
totalTime: PT15M
servings: 2
difficulty: nem
tags:
  - pandesovs
  - deglaze
  - stegesky
  - fløde
  - bøf
  - cognac
  - sauce
imageAlt: Cremet pandesovs i støbejernspande med stegesky
featured: true
ingredients:
  - Stegesky og fedt fra 1–2 bøffer i panden
  - 1 sjalotteløg, finthakket
  - ½ dl cognac, brandy eller tør vin
  - 1½ dl piskefløde
  - 1 tsk dijonsennep (valgfrit)
  - Salt og peber
  - Evt. 1 spsk koldt smør
steps:
  - Tag kødet op til hvile. Hæld overskydende fedt fra — gem 1 spsk og alle brunede rester.
  - Svits sjalotteløg 1 minut i fedtet. Hæld cognac eller vin i. Skrab bunden fri (deglaze). Kog 1–2 minutter, til alkoholen damper af.
  - Fløde i. Simre 3–5 minutter, til saucen tykner. Rør dijon i. Smag til. Evt. koldt smør til glans.
  - Server straks over eller ved siden af den hvilende bøf.
faq:
  - question: Cognac eller vin?
    answer: Cognac giver classic steakhouse. Rødvin er dybere. Hvidvin er lettere. Alle tre virker.
  - question: Flambering?
    answer: Valgfrit. Tag panden af gasblusset, hæld cognac i, antænd forsigtigt, og lad flammen dø. På induktion: bare kog alkoholen af.
  - question: Uden fløde?
    answer: Brug fond + koldt smør (monteret). Se også [brun sovs](/opskrifter/pande/brun-sovs) hvis du vil opbage.
  - question: Til hvad?
    answer: Entrecôte, culotte, hakkebøf og svinemørbrad.
body: |
  Den ultimative pandesovs er ikke en separat gryde — det er det brune i panden, reddet med alkohol og fløde.

  Stegeresterne er smagen. Opvasken er tabet.
tip: Pisk saucen mens kødet hviler. Timing er halvdelen af retten.
=====
title: Whiskey-flødesovs
slug: whiskey-floedesovs
category: pande
description: Whiskey-flødesovs — Jensen-stilen med whiskey, tomatpuré og fløde, tre gange bedre end færdigkøbt.
prepTime: PT5M
cookTime: PT15M
totalTime: PT20M
servings: 4
difficulty: nem
tags:
  - whiskey-flødesovs
  - whiskeysauce
  - whiskey
  - fløde
  - bøf
  - jensen
  - sauce
imageAlt: Cremet whiskey-flødesovs i pande
featured: true
ingredients:
  - 1 sjalotteløg, finthakket
  - 1 spsk smør + stegesky fra kød hvis du har
  - 1 spsk tomatpuré
  - ½ dl whiskey (bourbon eller irsk)
  - 2½ dl piskefløde
  - 1 tsk Worcestershire sauce
  - Salt og peber
steps:
  - Svits sjalotteløg i smør (og stegesky) 2 minutter. Rør tomatpuré i 1 minut — den skal dufte ristet, ikke dåse.
  - Hæld whiskey i. Kog 1–2 minutter, til alkoholen damper af.
  - Fløde og Worcestershire i. Simre 5–8 minutter, til saucen er blank og cremet. Smag til.
faq:
  - question: Er det den samme som grill-whiskeysauce?
    answer: Nej. [Whiskeysauce](/opskrifter/dips/whiskeysauce) er kold BBQ med ketchup. Denne er varm flødesauce til bøf — Jensen-skolen.
  - question: Hvilken whiskey?
    answer: Bourbon er sødere. Irsk er blødere. Undgå peated scotch — den kan smage af medicin i fløde.
  - question: Til hvad?
    answer: Oxfilet, culotte, hakkebøf og ovnkartofler.
  - question: Kan den laves uden kødstege?
    answer: Ja — ekstra smør og ½ tsk soja giver dybde.
body: |
  Whiskey-flødesovs er den klassiske steakhouse-kopi: whiskey, ristet tomatpuré og fløde.

  Tomatpuréen skal steges. Rå puré smager af dåse i en dyr sauce.
tip: Flamber kun hvis du har gas og styr på det — indkogning fjerner alkoholen lige så godt.
=====
title: Madagaskar-pebersovs
slug: madagaskar-pebersovs
category: pande
description: Madagaskar-pebersovs — fløde, cognac og ægte grønne madagaskar-peberkorn til bøf.
prepTime: PT5M
cookTime: PT12M
totalTime: PT17M
servings: 2
difficulty: mellem
tags:
  - madagaskar-pebersovs
  - pebersovs
  - madagaskarpeber
  - cognac
  - bøf
  - sauce
imageAlt: Cremet pebersovs med grønne madagaskar-peberkorn
featured: true
ingredients:
  - 2 spsk grønne madagaskar-peberkorn (dåse, afdryppet)
  - 1 sjalotteløg, finthakket
  - 1 spsk smør + stegesky
  - ½ dl cognac eller brandy
  - 2 dl piskefløde
  - Salt
steps:
  - Tryk ca. halvdelen af peberkornene let med knivsiden, så de åbner sig. Gem resten hele.
  - Svits sjalotteløg i smør og stegesky 1 minut. Tilsæt alle peberkorn. Svits 30 sekunder.
  - Hæld cognac i. Flamber eller kog 1–2 minutter. Fløde i. Simre 4–6 minutter, til saucen tykner. Salt forsigtigt.
faq:
  - question: Kan jeg bruge sorte peberkorn?
    answer: Du kan — men det er en anden sauce. Madagaskar (grønne i lage) er frugtigt og mildere. Sort peber er skarpere.
  - question: For stærk?
    answer: Færre knuste korn, flere hele. Fløde mildner.
  - question: Til hvad?
    answer: Oxfilet, entrecôte og culotte. Klassisk steakhouse.
  - question: Uden cognac?
    answer: Brug madeira eller tør hvidvin. Smagen skifter, teknikken er den samme.
body: |
  Madagaskar-pebersovs er peberkorn på dåse, cognac og fløde — ikke bare kværnet peber i cream.

  De grønne korn er frugtige. Det er hele pointen.
tip: Afdryp peberkornene, men gem 1 tsk lage til saucen hvis du vil have ekstra peber-syre.
=====
title: Mormor-flødesovs
slug: mormor-floedesovs
category: pande
description: Mormor-flødesovs — syrligt-sød sovs med ribsgele og skyen fra grydestegt kylling.
prepTime: PT5M
cookTime: PT15M
totalTime: PT20M
servings: 4
difficulty: nem
tags:
  - mormor-flødesovs
  - flødesovs
  - ribsgele
  - kylling
  - stegesky
  - sauce
  - dansk
imageAlt: Lyserød flødesovs med ribsgele i skål
featured: true
ingredients:
  - 2–3 dl stegesky fra grydestegt kylling (fedt skummet)
  - 1 spsk smør
  - 1 spsk hvedemel (valgfrit, til tykkelse)
  - 2 dl piskefløde
  - 1–2 spsk ribsgele
  - 1 tsk æblecidereddike eller citronsaft
  - Salt og peber
steps:
  - Skum fedtet fra kyllingeskyen. Mål ca. 2–3 dl sky.
  - Smelt smør i panden. Rør evt. mel i 30 sekunder. Hæld sky i under piskning. Bring i kog.
  - Fløde og ribsgele i. Simre 5–8 minutter. Smag til med eddike/citron, salt og peber — den skal være syrligt-sød, ikke dessert.
faq:
  - question: Uden ribsgele?
    answer: Solbærgele eller tyttebærgele virker. Honning alene mangler syre — tilsæt ekstra eddike.
  - question: Til hvad?
    answer: Grydestegt kylling, kyllingebryst, frikadeller og søndagssteg.
  - question: For sød?
    answer: Mere sky og eddike. Gele er til kant — ikke hovedsmag.
  - question: Kan jeg bruge bouillon?
    answer: Ja, hvis du mangler sky — tilsæt 1 tsk soja for dybde.
body: |
  Mormor-flødesovs er den danske søndagssauce: kyllingesky, fløde og et skud ribsgele.

  Den skal balancere sødt og syrligt. For meget gele, og det smager af jul i juli.
tip: Lav den i samme gryde som kyllingen — alle stegerester skal med.
=====
title: Estofado-tomatsauce
slug: estofado-tomatsauce
category: gryde
description: Estofado / langtidssimret tomatsauce — 6 timer med marvben for ekstrem umami til pasta og kød.
prepTime: PT30M
cookTime: PT6H
totalTime: PT6H30M
servings: 8
difficulty: mellem
tags:
  - estofado
  - tomatsauce
  - marvben
  - langtidssimret
  - umami
  - pasta
  - sauce
imageAlt: Dyb, mørkerød langtidssimret tomatsauce i gryde
featured: true
ingredients:
  - 1–1,5 kg okse-marvben eller kraftben, ristet
  - 2 spsk olivenolie
  - 2 løg, 2 gulerødder, 2 stilke bladselleri — hakket
  - 4 fed hvidløg
  - 3 spsk tomatpuré
  - 2 dåser (à 400 g) hakkede tomater
  - 2 dl tør rødvin
  - 5 dl vand eller fond
  - 2 laurbærblade, 1 kvist rosmarin, 4 kviste timian
  - Salt og peber
steps:
  - Tænd ovnen på 160 °C. Rist marvben 30–40 minutter, til de er dybt brune.
  - Svits løg, gulerod og selleri i olie i en tung gryde 10 minutter. Hvidløg og tomatpuré 2 minutter.
  - Vin i. Skrab bunden. Tomater, vand/fond, urter og ben i. Bring i kog.
  - Låg på. I ovnen 5–6 timer (eller simre meget lavt på komfur), til saucen er mørk, tyk og dyb.
  - Tag ben op. Skrab marv og kødrester i saucen. Si eller blend efter smag. Salt og peber til sidst — den er koncentreret.
faq:
  - question: Skal det være 6 timer?
    answer: Minimum 4. 6 timer giver den helt dybe umami. Hurtig tomatsauce er en anden opskrift.
  - question: Til pasta eller kød?
    answer: Begge. Til pasta: lidt pasta-vand. Til kød: server som estofado-sauce ved siden af.
  - question: Kan den fryses?
    answer: Ja — portionér. Den bliver kun bedre efter en nat i køl.
  - question: Uden marvben?
    answer: Brug oksehaler eller skank. Kollagen og marv er pointen — spring dem ikke over.
body: |
  Estofado-tomatsauce er tålmodighed i grydeform: marvben, tomat og 6 timer, til umamien er ekstrem.

  Det er ikke hverdags-napolisauce. Det er søndagsprojektet, der betaler sig i månedsvis i fryseren.
tip: Salt først til sidst. 6 timers reduktion gør tidlig salt til lim.
=====
title: Hollandaisesauce
slug: hollandaisesauce
category: dips
description: Hollandaisesauce fra bunden — cremet, syrlig emulsion til asparges og eggs benedict.
prepTime: PT10M
cookTime: PT15M
totalTime: PT25M
servings: 4
difficulty: svær
tags:
  - hollandaise
  - hollandaisesauce
  - asparges
  - eggs benedict
  - emulsion
  - sauce
imageAlt: Gul, blank hollandaisesauce i skål til asparges
featured: true
ingredients:
  - 3 æggeblommer (stuetemperatur)
  - 200 g usaltet smør
  - 2 spsk citronsaft
  - 1 spsk koldt vand
  - Salt
  - Cayenne eller hvid peber
steps:
  - Smelt smørret. Lad stå 2 minutter, så du kan bruge det klare smør øverst (eller brug hele smeltede smør).
  - Sæt skål over dampende vandbad (skålen må ikke røre vandet). Pisk blommer, vand og 1 spsk citron til tyk, lys sabayon — 2–4 minutter.
  - Tag af varmen. Dryp smeltet smør i under konstant piskning, som mayonnaise, til saucen er blank og tyk.
  - Smag til med resten af citronen, salt og cayenne. Hold lun (50–55 °C) — ikke på direkte varme.
faq:
  - question: Forskel på bearnaise?
    answer: Hollandaise er citron. [Bearnaise](/opskrifter/dips/bearnaisesovs) er eddike-reduktion med estragon.
  - question: Den skilles — redning?
    answer: Start med én æggeblomme i ren skål, og pisk den skillede sauce langsomt i. Scramble kan ikke reddes.
  - question: Sous vide-version?
    answer: Se [hollandaise sous vide](/opskrifter/sous-vide/hollandaise-sous-vide) for den temperaturstyrede metode.
  - question: Til hvad?
    answer: Hvide asparges, eggs benedict, laks og grillede grøntsager.
body: |
  Hollandaisesauce er bearnaisesøsteren: samme emulsion, citron i stedet for estragon.

  Temperaturen er hele spillet. For hed = røræg. For kold = skilt.
tip: Brug en [god saucekasserolle eller kobber](/grej/kobbergryder) hvis du har — jævn varme redder emulsionen.
=====
title: Chorizo-bearnaise
slug: chorizo-bearnaise
category: dips
description: Chorizo-bearnaise / baconaise — bearnaise opgraderet med chorizofedt eller baconfedt til grillbøf.
prepTime: PT15M
cookTime: PT20M
totalTime: PT35M
servings: 4
difficulty: svær
tags:
  - chorizo-bearnaise
  - baconaise
  - bearnaise
  - chorizo
  - bacon
  - sauce
  - grill
imageAlt: Orange-gul chorizo-bearnaise i skål
featured: true
ingredients:
  - 3 æggeblommer
  - 100 g usaltet smør
  - 100 g chorizofedt eller baconfedt (smeltet, siet) — eller 150 g chorizo/bacon stegt ud til fedt + 50 g smør
  - 1 dl hvidvinseddike
  - 1 sjalotteløg, finthakket
  - 1 spsk frisk estragon, hakket
  - 1 tsk knuste peberkorn
  - Salt
steps:
  - Steg chorizo eller bacon, til fedtet er smeltet. Si fedtet. Bland med smeltet smør, så du har ca. 200 g fedt i alt. Hold lunkent.
  - Kog eddike, sjalotteløg, halvdelen af estragonen og peber ned til 2–3 spsk. Si. Køl til lunken.
  - Pisk blommer og reduktion til sabayon over vandbad. Tag af varmen.
  - Dryp fedtblandingen i under konstant piskning. Rør resten af estragonen i. Smag til med salt.
faq:
  - question: Chorizo eller bacon?
    answer: Chorizo giver røget paprika-dybde (chorizo-bearnaise). Bacon giver salt, røg og baconaise. Samme teknik.
  - question: For salt?
    answer: Brug mere smør i blandingen, og salt forsigtigt til sidst — kødfedt er allerede salt.
  - question: Kan den skilles?
    answer: Ja — samme redning som [bearnaisesovs](/opskrifter/dips/bearnaisesovs): ny blomme, pisk den skillede i.
  - question: Til hvad?
    answer: Smashburgere, culotte, ribeye og ovnkartofler.
body: |
  Chorizo-bearnaise er bearnaise med attitude: en del af smørret skiftes ud med chorizo- eller baconfedt.

  Den er saltet, røget og bygget til grillbøffen — ikke til asparges.
tip: Si fedtet godt. Brændte bits gør saucen bitter og prikket.
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
    extra = ""
    if slug in ("hollandaisesauce", "chorizo-bearnaise", "roedvinssauce", "mornay-sauce"):
        if slug in ("hollandaisesauce", "chorizo-bearnaise"):
            extra = "affiliateProduct: boligcenter-saucegryde\nrelatedGrej:\n  - kobbergryder\n"
        elif slug == "roedvinssauce":
            extra = f"affiliateWineUrl: {yaml_str('https://dhwines.dk/collections/rodvine-100-200-kr')}\n"
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
{featured}{extra}ingredients:
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
