#!/usr/bin/env python3
"""20 skarpe sylte-gaps — klassikere, modspil, frugt, pickles og sild."""
from pathlib import Path

ROOT = Path("/Users/dklarsen/Desktop/saltet/content/recipes")

RECIPES = r'''
=====
title: Klassisk rødkål med andefedt
slug: klassisk-roedkaal-andefedt
category: sylte
description: Klassisk rødkål med andefedt, ribssaft, nelliker og kanel — den ultimative julesøgning til andesteg og flæskesteg.
prepTime: PT25M
cookTime: PT1H30M
totalTime: PT2H
servings: 8
difficulty: mellem
tags:
  - rødkål
  - andefedt
  - jul
  - klassiker
  - sylte
  - efterår
imageAlt: Mørkogt rødkål med andefedt i skål til julebordet
featured: true
ingredients:
  - 1,5 kg rødkål, fint snittet
  - 3 spsk andefedt (eller gåsefedt)
  - 2 dl ribssaft (uden for meget sukker)
  - 1 dl æblecidereddike
  - 1 dl vand
  - 3 spsk brun farin
  - 1 tsk salt
  - 6 hele nelliker
  - 1 kanelstang
  - 2 laurbærblade
  - 1 æble, groft revet (valgfri)
steps:
  - Smelt andefedtet i en tung gryde. Svits rødkålen 5–8 minutter, til den synker og glinser.
  - Tilsæt ribssaft, eddike, vand, farin, salt, nelliker, kanel og laurbær. Rør æblet i, hvis du bruger det.
  - Bring i kog, skru ned, og lad simre under låg 1–1½ time. Rør undervejs. Kålen skal være helt mør, men stadig holden.
  - Smag til med salt, syre og sødme. Fjern kanel, nelliker og laurbær.
  - Server varm, eller afkøl og stil på glas i køleskab — smagen bliver dybere efter 1–2 dage.
faq:
  - question: Kan jeg bruge smør i stedet for andefedt?
    answer: Ja, men andefedt giver den klassiske julesmag. Bland gerne 2 spsk andefedt + 1 spsk smør.
  - question: Skal den steriliseres?
    answer: Nej til køleskab. Til langtidsopbevaring uden køl: skoldede glas og vandbad efter fyldning.
  - question: Ribssaft eller ribsgele?
    answer: Saft. Gele gør den for sød og geléagtig. Til sidst kan du røre 1 spsk gele i for blankhed.
  - question: Til hvad?
    answer: Andesteg, flæskesteg, gås og stegt flæsk. Den er julebordets søde-syrlige balancør.
body: |
  Klassisk rødkål med andefedt er ikke en hurtig pickles — det er mørkogt efterår i gryde.

  Ribssaft, nelliker og kanel giver julesøgningen. Andefedtet giver den dybde, som smør aldrig rigtig rammer.
tip: Lav den dagen før. Varm den blidt op med en skefuld ekstra ribssaft — den smager mere «færdig» end friskkogt.
=====
title: Syltede grønne valdnødder
slug: syltede-groenne-valdnoedder
category: sylte
description: Syltede grønne valdnødder — tidskrævende luksus-delikatesse til ostebordet. Mørke, søde og intense.
prepTime: PT1H
cookTime: PT45M
totalTime: PT241H
servings: 4
difficulty: svær
tags:
  - valdnødder
  - grønne valdnødder
  - ostebord
  - luksus
  - sylte
  - sommer
imageAlt: Glas med mørke syltede grønne valdnødder
featured: true
ingredients:
  - 1 kg grønne valdnødder (høstet før skallen hærder — typisk juni/juli)
  - Saltlage til udtrækning: 100 g salt pr. liter vand (nok til at dække)
  - 1 liter eddike (5 %)
  - 800 g sukker
  - 1 kanelstang
  - 8 nelliker
  - 1 tsk allehånde
  - 1 vaniljestang, flækket
  - Saft af 1 citron
steps:
  - Prikk hver nød flere gange med en nål (brug handsker — saften farver). Læg i saltlage. Skift lagen dagligt i 8–10 dage, til nødderne er næsten sorte og bittersaften er trukket ud.
  - Skyl godt. Kog 15–20 minutter i friskt vand. Hæld vandet fra. Gentag én gang, hvis de stadig smager meget bittert.
  - Kog eddike, sukker, krydderier og citronsaft til en klar lage.
  - Læg nødderne i skoldede glas. Hæld den kogende lage over, så de er dækket.
  - Luk, vend kort, og lad køle. Gem mørkt og køligt mindst 1 måned — bedst efter 3.
faq:
  - question: Hvornår høster man grønne valdnødder?
    answer: Når du kan stikke en nål igennem uden hård skal — typisk juni til tidlig juli.
  - question: Hvorfor saltlage i dagevis?
    answer: Den trækker bitterstoffer og tanniner ud. Spring over, og de smager medicinske.
  - question: Holdbarhed?
    answer: Et år eller mere under lagen i skoldede glas, mørkt og køligt.
  - question: Til hvad?
    answer: Blåskimmel, cheddar, foie gras-agtige patéer og et lille glas til dig selv.
body: |
  Syltede grønne valdnødder er mormors luksusprojekt: tid, handsker og tålmodighed.

  Når de er færdige, er de næsten sorte, søde og dybe — ostebordets hemmelige våben.
tip: Brug engangshandsker hele vejen. Saften farver hænder og køkkenbord permanent.
=====
title: Syltede kastanjer i sennepslage (Mostarda di Cremona)
slug: syltede-kastanjer-sennepslage
category: sylte
description: Syltede kastanjer i sennepslage — italiensk Mostarda di Cremona-inspireret tilbehør til flæskesteg og sild.
prepTime: PT30M
cookTime: PT40M
totalTime: PT1H10M
servings: 6
difficulty: mellem
tags:
  - kastanjer
  - mostarda
  - sennep
  - flæskesteg
  - sylte
  - jul
imageAlt: Glas med syltede kastanjer i gylden sennepslage
featured: true
ingredients:
  - 500 g kogte, skrællede kastanjer (hele)
  - 3 dl hvidvinseddike
  - 2 dl vand
  - 250 g sukker
  - 2 spsk sennepspulver
  - 1 spsk hele sennepskorn
  - 1 kanelstang
  - 4 nelliker
  - 1 tsk salt
  - Evt. 100 g pære eller kvæde i tern (valgfri)
steps:
  - Kog eddike, vand, sukker, salt, kanel og nelliker op, til sukkeret er opløst.
  - Rør sennepspulver ud i 2 spsk kold lage, og pisk det tilbage i gryden sammen med sennepskornene. Lad koge 2 minutter.
  - Læg kastanjerne (og evt. frugttern) i rene glas.
  - Hæld den varme sennepslage over, så alt er dækket. Fordel krydderierne.
  - Luk, lad køle, og stil koldt mindst 3–5 dage før servering.
faq:
  - question: Friske eller vakuum-kastanjer?
    answer: Begge dele. Friske skal koges og skrælles først. Vakuum-kogte sparer tid og holder formen.
  - question: Er det stærkt?
    answer: Sennepspulver giver varme, ikke chili-brand. Start med 1½ spsk, hvis du er forsigtig.
  - question: Til flæskesteg?
    answer: Ja — og til saltsild, leverpostej og hård ost. Det er det fede køds skarpe modspil.
  - question: Holdbarhed?
    answer: Flere uger i køleskab under lagen.
body: |
  Mostarda di Cremona er italiensk syltekunst: frugt i sød lagen med sennepsbid.

  Her er kastanjerne stjernen — ravgule, faste og med en lage der skærer igennem flæskestegsfedt.
tip: Rør ikke for hårdt i glasset — hele kastanjer ser bedre ud end mos.
=====
title: Sødsyltede paradisæbler
slug: soedsyltede-paradisaebler
category: sylte
description: Sødsyltede paradisæbler — hele små æbler med stilk i krydret sukkerlage. Pynt og tilbehør til efterårssteg.
prepTime: PT20M
cookTime: PT25M
totalTime: PT45M
servings: 4
difficulty: mellem
tags:
  - paradisæbler
  - efterår
  - sylte
  - stegt
  - klassiker
  - pynt
imageAlt: Glas med hele sødsyltede paradisæbler med stilk
featured: true
ingredients:
  - 800 g paradisæbler (små, faste, med stilk)
  - 5 dl eddike (5 %)
  - 3 dl vand
  - 400 g sukker
  - 1 kanelstang
  - 6 nelliker
  - 1 tsk allehånde
  - 1 stjerneanis
  - 1 tsk salt
  - Skræl af ½ citron
steps:
  - Skyl æblerne. Behold stilken. Prikk hvert æble 2–3 gange med en nål, så de ikke sprænger.
  - Kog eddike, vand, sukker, salt og krydderier til en klar lage.
  - Læg æblerne i lagen. Lad dem simre blidt 8–12 minutter, til de er møre, men stadig hele.
  - Fisk æblerne op i skoldede glas. Kog lagen ind 5 minutter mere, og hæld den kogende over.
  - Luk, vend kort, og lad køle. Klar efter ca. 1 uge.
faq:
  - question: Kan jeg bruge almindelige små æbler?
    answer: Gerne crab apples eller meget små, faste sorter. Bløde æbler falder fra hinanden.
  - question: Skal stilken blive på?
    answer: Ja — det er både pynt og greb, når de serveres hele ved stegen.
  - question: Til hvad?
    answer: Flæskesteg, and, vildt og ostebordet. De er både tilbehør og bordpynt.
  - question: Holdbarhed?
    answer: Flere måneder mørkt og køligt under lagen.
body: |
  Sødsyltede paradisæbler er efterårets glas med stilk: små, hele, krydrede.

  De ser ud som juveler og smager af kanel, syre og æble — direkte til stegefadet.
tip: Prikk æblerne, før de kommer i lagen. Ellers sprænger skindet, og skønheden forsvinder.
=====
title: Grov mormor-remoulade på syltede grøntsager
slug: mormor-remoulade-syltede-groentsager
category: sylte
description: Grov mormor-remoulade — sylt først asier, gulerødder og blomkål, hak dem derefter til verdens bedste remoulade.
prepTime: PT45M
cookTime: PT20M
totalTime: PT48H
servings: 8
difficulty: mellem
tags:
  - remoulade
  - mormor
  - asier
  - smørrebrød
  - sylte
  - klassiker
imageAlt: Skål med grov hjemmelavet remoulade af syltede grøntsager
featured: true
ingredients:
  - 300 g asier eller sylteagurk, i skiver
  - 200 g blomkål i små buketter
  - 150 g gulerødder i tern
  - Syltelage: 5 dl eddike (5 %), 3 dl vand, 200 g sukker, 1 spsk salt, 1 spsk sennepskorn, 1 tsk peberkorn, 2 laurbærblade
  - Remoulade: 3 dl mayonnaise, 2 spsk dijonsennep, 1 spsk kapers, 1 spsk finthakket dild, 1 tsk karry (valgfri), peber
steps:
  - Salt asier, blomkål og gulerødder let, og lad trække 1–2 timer. Skyl og dryp.
  - Kog lagen op. Læg grøntsagerne i glas, hæld kogende lage over, og luk. Stil koldt mindst 24 timer (gerne 3–5 dage).
  - Hæld lagen fra. Hak grøntsagerne groft — de skal have bid, ikke blive mos.
  - Rør mayonnaise, sennep, kapers, dild og evt. karry sammen. Vend de hakkede grøntsager i. Smag til med peber og evt. lidt lage.
  - Stil koldt mindst 1 time før servering.
faq:
  - question: Kan jeg bruge købte asier?
    answer: Ja til en hurtig udgave. Hjemmesyltede giver mere kontrol over sødme og knas.
  - question: Hvor grov skal den være?
    answer: Tern på 3–5 mm. For fin bliver det købemad. For grov bliver det salat.
  - question: Holdbarhed?
    answer: Remouladen 4–5 dage i køleskab. De syltede grøntsager holder uger under lagen.
  - question: Til fiskefrikadeller?
    answer: Ja — og til roastbeef, hønsesalat og stegte sild.
body: |
  Grov mormor-remoulade starter med syltning, ikke med en dåse.

  Først lagen. Så hakket. Så mayo. Resultatet er knas, syre og fedme i samme ske.
tip: Gem 2 spsk syltelage. Den redder remouladen, hvis den bliver for tung.
=====
title: Hjemmelavet piccalilli / chow-chow
slug: piccalilli-chow-chow
category: sylte
description: Hjemmelavet piccalilli (chow-chow) — engelsk klassiker med sennep, gurkemeje og grofthakkede efterårsgrøntsager.
prepTime: PT40M
cookTime: PT25M
totalTime: PT1H5M
servings: 8
difficulty: mellem
tags:
  - piccalilli
  - chow-chow
  - sennep
  - efterår
  - sylte
  - tilbehør
imageAlt: Glas med gul piccalilli af hakkede efterårsgrøntsager
featured: true
ingredients:
  - 400 g blomkål i små buketter
  - 200 g agurk eller asier i tern
  - 150 g gulerødder i tern
  - 100 g løg i tern
  - 100 g grønne bønner i stykker
  - 2 spsk salt (til udtrækning)
  - Lage: 5 dl eddike (5 %), 150 g sukker, 2 spsk sennepspulver, 1 spsk gurkemeje, 1 spsk sennepskorn, 1 tsk ingefærpulver, 2 spsk majsstivelse
steps:
  - Bland alle grøntsager med salt. Lad trække 2–3 timer (eller natten over). Skyl og dryp grundigt.
  - Kog eddike, sukker og krydderier (undtagen majsstivelse) op.
  - Rør majsstivelse ud i lidt kold eddike, og pisk det i lagen. Kog til den tykner let og bliver knaldgul.
  - Vend grøntsagerne i den varme lage. Simre 3–5 minutter — de skal stadig have bid.
  - Fyld på skoldede glas. Luk, lad køle, og stil koldt. Bedst efter 1 uge.
faq:
  - question: Piccalilli eller chow-chow?
    answer: Samme familie. Piccalilli er den engelske senneps-gurkemeje-version. Chow-chow er den mere amerikanske/sydstatsagtige fætter.
  - question: Skal den være tyk?
    answer: Lagen skal binde let, ikke være budding. Majsstivelsen er limen.
  - question: Til hvad?
    answer: Ost, cold cuts, pølser, sandwich og julefrokostens pålæg.
  - question: Holdbarhed?
    answer: Flere måneder i køleskab under lagen.
body: |
  Piccalilli er efterårets gule glas: sennep, gurkemeje og groft hakket grønt.

  Den skal knase. Den skal være skarp. Den skal gøre fedt kød interessant igen.
tip: Saltningen er ikke til pynt — den holder grøntsagerne sprøde, når lagen koger.
=====
title: Syltede gule sennepsfrø i mørkt øl
slug: syltede-sennepsfro-oel
category: sylte
description: Syltede gule sennepsfrø i porter eller julebryg — dyb umami-topping til leverpostej, sild og ost.
prepTime: PT10M
cookTime: PT8M
totalTime: PT15M
servings: 1
difficulty: nem
tags:
  - sennepsfrø
  - øl
  - porter
  - smørrebrød
  - sylte
  - jul
imageAlt: Lille glas med gule sennepsfrø syltet i mørkt øl
featured: true
ingredients:
  - 100 g hele gule sennepskorn
  - 1½ dl porter eller julebryg (ikke for bitter IPA)
  - ½ dl æblecidereddike
  - 2 spsk mørk farin
  - ½ tsk salt
  - 1 laurbærblad
  - 3 nelliker (valgfri)
steps:
  - Skyl sennepskornene, og læg dem i et lille glas.
  - Varm øl, eddike, farin, salt, laurbær og nelliker op, til farinen er opløst — kog ikke længe, så alkoholen forsvinder helt, hvis du vil have dybde.
  - Hæld den varme lage over kornene.
  - Luk glasset, og lad køle. Stil i køleskab.
  - Ryst dagligt de første dage. Klar efter 4–5 dage — bedst efter en uge.
faq:
  - question: Hvorfor øl i stedet for bare eddike?
    answer: Porter og julebryg giver malt, bitterhed og umami, som klæber til leverpostej.
  - question: Bliver de alkoholiske?
    answer: Meget mildt. Det meste fordamper ved opvarmning; smagen bliver tilbage.
  - question: Gule eller brune frø?
    answer: Gule til den her. Brune bliver for skarpe sammen med mørkt øl.
  - question: Holdbarhed?
    answer: Flere måneder i køleskab under lagen.
body: |
  Syltede sennepsfrø i mørkt øl er eddike-versionens mørkere fætter.

  Samme knas. Mere dybde. Laget til leverpostej, røget kød og julefrokost.
tip: Brug en porter eller et blødt julebryg — ikke en humlebombe. Humlen bliver bitter i glasset.
=====
title: Syltet peberrod i eddike
slug: syltet-peberrod-eddike
category: sylte
description: Syltet peberrod i eddike — revet peberrod i syrlig lage, der bevarer skarpheden til oksebryst uden at blive brun.
prepTime: PT15M
cookTime: PT5M
totalTime: PT20M
servings: 2
difficulty: nem
tags:
  - peberrod
  - oksebryst
  - smørrebrød
  - sylte
  - klassiker
  - skarp
imageAlt: Glas med hvid syltet peberrod i klar eddikelage
featured: true
ingredients:
  - 200 g frisk peberrod, skrællet
  - 1½ dl hvidvinseddike eller æblecidereddike
  - ½ dl vand
  - 1 tsk salt
  - 1 tsk sukker
  - Evt. 1 spsk citronsaft
steps:
  - Riv peberroden fint (arbejd hurtigt — den oxiderer). Brug gerne handsker og åbent vindue.
  - Kog eddike, vand, salt og sukker op. Tag af varmen, og rør citronsaft i.
  - Læg den revne peberrod i et rent glas. Hæld den varme lage over, så den er dækket.
  - Rør rundt, luk, og lad køle. Stil i køleskab.
  - Klar efter et par timer — skarpest de første dage, stadig god i uger.
faq:
  - question: Hvorfor bliver peberrod brun?
    answer: Ilt. Eddike og citron bremser oxideringen. Arbejd hurtigt, og dæk med lagen med det samme.
  - question: Kan jeg bruge købt peberrod?
    answer: Frisk er skarpere. Købt i glas er mildere og ofte sødet — fin som nødplan.
  - question: Til oksebryst?
    answer: Ja — og til roastbeef, pølser og smørrebrød med leverpostej.
  - question: For stærkt?
    answer: Mere sukker og lidt mere vand. Eller bland med creme fraiche lige før servering.
body: |
  Syltet peberrod i eddike er den hvide, skarpe glas til det fede kød.

  Ingen brun farve. Ingen slatten styrke. Bare syre der holder peberroden vågen.
tip: Riv lige inden lagen er klar. Jo længere peberroden ligger åben, jo mere brun og mild bliver den.
=====
title: Syltede brombær med timian og balsamico
slug: syltede-brombaer-timian-balsamico
category: sylte
description: Syltede brombær med timian og balsamico — sensommerens bær-hit med dyb, saltvenlig smag til vildt og ost.
prepTime: PT15M
cookTime: PT10M
totalTime: PT25M
servings: 4
difficulty: nem
tags:
  - brombær
  - timian
  - balsamico
  - vildt
  - ostebord
  - sylte
imageAlt: Glas med syltede brombær, timian og balsamico
featured: true
ingredients:
  - 500 g faste brombær
  - 2 dl rødvinseddike
  - 2 spsk balsamico
  - 1½ dl sukker
  - 1 tsk salt
  - 4 kvist frisk timian
  - 1 tsk peberkorn
  - 1 laurbærblad
steps:
  - Læg brombærrene forsigtigt i skoldede glas sammen med timian.
  - Kog eddike, balsamico, sukker, salt, peberkorn og laurbær op, til sukkeret er opløst.
  - Hæld den kogende lage over bærrene — rør ikke, så de ikke smuldrer.
  - Luk, lad køle, og stil koldt.
  - Klar efter 2–3 dage. Bedst inden for 2–3 uger, mens bærrene stadig holder form.
faq:
  - question: Frosne brombær?
    answer: Kan bruges, men de bliver blødere. Friske, faste bær er bedst.
  - question: Til krondyr?
    answer: Ja — og rådyr, and og blåskimmel. Balsamico binder det saltede og det søde.
  - question: For sødt?
    answer: Skær sukkeret til 1 dl, og øg balsamicoen med 1 spsk.
  - question: Holdbarhed?
    answer: Et par uger i køleskab. Spis dem, mens de stadig er hele.
body: |
  Syltede brombær med timian og balsamico er sensommer på glas til vildt.

  Syre først. Sødme bagefter. Timian binder det til kødet.
tip: Fyld glasset uden at presse bærrene. Plads i glasset er det, der holder dem hele.
=====
title: Klassisk stikkelsbærkompot til hønsesalat
slug: stikkelsbaerkompot-hoensesalat
category: sylte
description: Klassisk stikkelsbærkompot til hønsesalat — den grovere, mindre søde udgave, der giver syre direkte i frokostsalaten.
prepTime: PT15M
cookTime: PT20M
totalTime: PT35M
servings: 6
difficulty: nem
tags:
  - stikkelsbær
  - kompot
  - hønsesalat
  - smørrebrød
  - sylte
  - sommer
imageAlt: Skål med grov stikkelsbærkompot til hønsesalat
featured: true
ingredients:
  - 500 g stikkelsbær (gerne grønne og faste)
  - 1 dl sukker
  - ½ dl æblecidereddike
  - ½ dl vand
  - 1 knivspids salt
  - ½ vaniljestang eller ½ tsk vaniljesukker (valgfri)
steps:
  - Top og haléstikkelsbærrene. Halvér de største.
  - Læg bær, sukker, eddike, vand, salt og vanilje i en gryde.
  - Bring i kog, og lad simre 12–18 minutter under omrøring. Bærrene skal briste, men ikke blive marmelade.
  - Smag til — den skal være syrlig først, sød bagefter.
  - Hæld på rene glas eller en skål. Køl helt af inden den røres i hønsesalat.
faq:
  - question: Forskel på jeres syltede stikkelsbær?
    answer: De andre er hele bær i sød lage til ost. Den her er grovere kompot med mindre sukker til salater.
  - question: Hvor meget i hønsesalaten?
    answer: Start med 2–3 spsk pr. 400 g kylling. Den skal mærkes, ikke dominere.
  - question: Frosne stikkelsbær?
    answer: Ja — direkte i gryden. Kog et par minutter længere.
  - question: Holdbarhed?
    answer: Ca. 1 uge i køleskab, eller frys i små portioner.
body: |
  Stikkelsbærkompot til hønsesalat er den syrlige ske, ikke dessertglasset.

  Mindre sukker. Mere bid. Den skal skære igennem mayo og kylling.
tip: Lav en dobbelt portion, og frys halvdelen i isterningeposer — én tern pr. frokostsalat.
=====
title: Syltede kvæder i vaniljelage
slug: syltede-kvaeder-vaniljelage
category: sylte
description: Syltede kvæder i vaniljelage — efterårets hårde frugt forvandlet til ravgult tilbehør til skæreost.
prepTime: PT30M
cookTime: PT45M
totalTime: PT1H15M
servings: 6
difficulty: mellem
tags:
  - kvæder
  - vanilje
  - ostebord
  - efterår
  - sylte
  - klassiker
imageAlt: Glas med ravgule syltede kvædeskiver i vaniljelage
featured: true
ingredients:
  - 1 kg kvæder
  - 5 dl æblecidereddike
  - 3 dl vand
  - 400 g sukker
  - 1 vaniljestang, flækket
  - 1 kanelstang
  - 4 nelliker
  - 1 tsk salt
  - Saft af 1 citron
steps:
  - Skræl kvæderne, fjern kernehuset, og skær i både eller skiver. Læg dem i vand med citronsaft, så de ikke brunfarves.
  - Kog eddike, vand, sukker, salt, vanilje, kanel og nelliker til en klar lage.
  - Læg kvæderne i lagen, og lad dem simre 25–40 minutter, til de er møre og ravgule — de skal holde formen.
  - Fisk kvæderne op i skoldede glas. Kog lagen lidt ind, og hæld den kogende over.
  - Luk, lad køle, og gem mørkt. Klar efter ca. 1 uge.
faq:
  - question: Kan man spise rå kvæde?
    answer: Nej — den er for hård og astringerende. Syltning eller kogning er vejen.
  - question: Hvorfor bliver de røde/ravgule?
    answer: Varme og syre frigiver farve. Det er tegn på, at de er færdige.
  - question: Til hvilken ost?
    answer: Manchego, comté, vesterhavsost og blåskimmel.
  - question: Holdbarhed?
    answer: Flere måneder mørkt og køligt under lagen.
body: |
  Syltede kvæder i vaniljelage er efterårets glemte frugt på sit bedste.

  Hårde i kurven. Ravgule i glasset. Perfekte til kniv og ost.
tip: Gem kernehuset til gele en anden dag — men til den her opskrift skal kødet være rent og skåret pænt.
=====
title: Syltede hyben med rom og nelliker
slug: syltede-hyben-rom-nelliker
category: sylte
description: Syltede hyben med rom og nelliker — klassisk mormor-spise fra stranden til vildt og desserter.
prepTime: PT45M
cookTime: PT30M
totalTime: PT1H15M
servings: 4
difficulty: mellem
tags:
  - hyben
  - rom
  - nelliker
  - vildt
  - efterår
  - sylte
imageAlt: Glas med syltede hyben i mørk lage med nelliker
featured: true
ingredients:
  - 500 g hyben (efter første frost er bedst)
  - 4 dl æblecidereddike
  - 250 g sukker
  - ½ dl mørk rom
  - 8 nelliker
  - 1 kanelstang
  - 1 tsk salt
  - 1 dl vand
steps:
  - Top og halést hybenene. Halvér dem, og skrabe kernerne ud (brug handsker — fnuggene irriterer).
  - Kog eddike, vand, sukker, salt, nelliker og kanel op.
  - Læg hybenene i lagen, og lad dem simre 15–20 minutter, til de er møre.
  - Tag gryden af varmen. Rør rommen i.
  - Fyld på skoldede glas med lagen. Luk, lad køle, og stil koldt. Klar efter ca. 1 uge.
faq:
  - question: Skal kernerne væk?
    answer: Ja. Hybenfnug irriterer mund og svælg. Tag dig tid.
  - question: Hvorfor rom?
    answer: Den giver varme og dybde til vildt og dessert. Uden rom er det stadig godt — bare mildere.
  - question: Til hvad?
    answer: Rådyr, and, leverpostej, yoghurt og vaniljeis.
  - question: Holdbarhed?
    answer: Flere måneder i køleskab under lagen.
body: |
  Syltede hyben med rom og nelliker er strandens mormor-glas.

  Syrlige, mørke og lidt vilde — lige så gode til stegen som til skeen over is.
tip: Vent til efter første frost, hvis du kan. Hyben bliver sødere og lettere at arbejde med.
=====
title: Pickled Onion Rings (hele syltede løgringe)
slug: pickled-onion-rings
category: sylte
description: Pickled Onion Rings — hele, intakte rå løgringe i krydret eddike- og sennepslage til dyrlægens natmad og roastbeef.
prepTime: PT15M
cookTime: PT5M
totalTime: PT20M
servings: 4
difficulty: nem
tags:
  - løgringe
  - rødløg
  - pickles
  - smørrebrød
  - roastbeef
  - sylte
  - viral
imageAlt: Glas med store hele syltede rødløgsringe
featured: true
ingredients:
  - 3 store rødløg
  - 3 dl æblecidereddike
  - 1½ dl vand
  - 3 spsk sukker
  - 1½ tsk salt
  - 1 spsk hele sennepskorn
  - 1 tsk peberkorn
  - ½ tsk chiliflager (valgfri)
  - 2 laurbærblade
steps:
  - Skær løgene i 8–10 mm tykke skiver. Adskil dem forsigtigt til hele ringe — behold de pæneste.
  - Læg ringene i et bredt glas eller bøtte, så de ligger fladt og ikke knækker.
  - Kog eddike, vand, sukker, salt og krydderier op, til sukkeret er opløst.
  - Hæld den kogende lage over ringene. Tryk dem let ned, så de er dækket.
  - Lad køle, og stil koldt mindst 2 timer — bedst overnight. De skal forblive sprøde og rå i midten.
faq:
  - question: Forskel på hakkede syltede rødløg?
    answer: De hakkede er til at røre ud. De her er store ringe til at lægge ovenpå roastbeef og natmad.
  - question: Hvide løg?
    answer: Kan. Rødløg giver farve og mildere sødme.
  - question: For skarpe?
    answer: Skold ringene 20 sekunder i kogende vand før lagen, eller øg sukkeret lidt.
  - question: Holdbarhed?
    answer: Ca. 2 uger i køleskab. Spis dem, mens de stadig knaser.
body: |
  Pickled Onion Rings er ikke hakket rødløg i et hjørne af glasset.

  Store, intakte ringe. Krydret lage. Direkte på dyrlægens natmad og roastbeef.
tip: Skær tykkere end du tror. Tynde ringe bliver slatne; tykke ringe beholder knækket.
=====
title: Syltede blomkålsbuketter med karry og chili
slug: syltede-blomkaalsbuketter-karry-chili
category: sylte
description: Syltede blomkålsbuketter med karry og chili — ekstremt sprøde, gule buketter til snack og grillmad.
prepTime: PT20M
cookTime: PT8M
totalTime: PT28M
servings: 6
difficulty: nem
tags:
  - blomkål
  - karry
  - chili
  - pickles
  - grill
  - sylte
  - snack
imageAlt: Glas med gule syltede blomkålsbuketter med chili
featured: true
ingredients:
  - 1 stort blomkålhoved (ca. 800 g), i små buketter
  - 4 dl æblecidereddike
  - 2 dl vand
  - 100 g sukker
  - 1 spsk salt
  - 1 spsk karrypulver
  - 1 tsk gurkemeje
  - 1 tsk sennepskorn
  - 1–2 friske chilier, skåret i skiver
  - 2 fed hvidløg, knuste
steps:
  - Blanchér blomkålen 60–90 sekunder i kogende saltet vand. Hæld i isvand, og dryp godt — det bevarer knækket.
  - Læg blomkål, chili og hvidløg i skoldede glas.
  - Kog eddike, vand, sukker, salt, karry, gurkemeje og sennepskorn op.
  - Hæld den kogende lage over. Bank glasset let, så luftbobler stiger op.
  - Luk, lad køle, og stil koldt. Klar efter 24 timer — sprødest de første 2 uger.
faq:
  - question: Hvorfor blanchere?
    answer: Kort blanchering tager den rå «kålsmag» uden at gøre buketterne bløde.
  - question: Hvor stærke bliver de?
    answer: Du styrer det med chili. Uden chili er det mild karry-syre.
  - question: Til grill?
    answer: Ja — og som snack direkte fra glasset, til burgers og ostebræt.
  - question: Holdbarhed?
    answer: 3–4 uger i køleskab under lagen.
body: |
  Syltede blomkålsbuketter med karry og chili er den gule, sprøde snack-pickle.

  Kort blanchering. Kogende lage. Så knækker de stadig efter en uge.
tip: Små buketter er bedre end store — de suger lagen, og du kan spise dem i én bid.
=====
title: Syltet vandmelon-skal (Watermelon Rind Pickles)
slug: watermelon-rind-pickles
category: sylte
description: Watermelon Rind Pickles — det hvide fra vandmelonskallen syltet med ingefær og kanel. Ultimativ madspilds-pickle.
prepTime: PT30M
cookTime: PT20M
totalTime: PT12H50M
servings: 6
difficulty: mellem
tags:
  - vandmelon
  - madspild
  - pickles
  - ingefær
  - viral
  - sylte
imageAlt: Glas med sprøde syltede stykker af hvid vandmelon-skal
featured: true
ingredients:
  - 800 g hvid vandmelon-skal (grøn skræl og rødt kød fjernet), i 3×1 cm stænger
  - 2 spsk salt (til udtrækning)
  - 5 dl æblecidereddike
  - 300 g sukker
  - 1 dl vand
  - 40 g frisk ingefær, skivet
  - 1 kanelstang
  - 6 nelliker
  - 1 tsk peberkorn
steps:
  - Skær al grøn skræl og rødt kød fra, så kun det faste hvide er tilbage. Skær i stænger.
  - Bland med salt, og lad trække 8–12 timer i køleskab. Skyl og dryp.
  - Kog eddike, sukker, vand og krydderier til en klar lage.
  - Læg skallerne i lagen, og lad dem simre 8–12 minutter, til de er transparente i kanten, men stadig sprøde.
  - Fyld på skoldede glas med lagen. Luk, lad køle, og stil koldt. Klar efter 3–4 dage.
faq:
  - question: Smager det af vandmelon?
    answer: Mere af æble/agurk med ingefær og kanel. Det er tekstur og krydderi, ikke smoothie.
  - question: Kan den grønne skræl blive på?
    answer: Nej — den bliver sej. Kun det hvide.
  - question: Hvorfor er det en trend?
    answer: Madspild + knas. Du får pickle ud af noget, de fleste smider ud.
  - question: Holdbarhed?
    answer: Flere uger i køleskab under lagen.
body: |
  Watermelon Rind Pickles er madspild, der knaser.

  Det hvide fra skallen. Ingefær. Kanel. En amerikansk klassiker, der fortjener en dansk plads i køleskabet.
tip: Salt overnight er hemmeligheden bag sprødhed. Spring over, og stængerne bliver slatne.
=====
title: Syltede grønne asparges med dild
slug: syltede-groenne-asparges-dild
category: sylte
description: Syltede grønne asparges med dild — forårsbebuderen med grønt, sprødt knæk. En anden sag end de hvide.
prepTime: PT15M
cookTime: PT8M
totalTime: PT25M
servings: 4
difficulty: nem
tags:
  - grønne asparges
  - dild
  - forår
  - sylte
  - tilbehør
  - grill
imageAlt: Højt glas med syltede grønne asparges og dild
featured: true
ingredients:
  - 500 g grønne asparges
  - 3 dl æblecidereddike
  - 1½ dl vand
  - 3 spsk sukker
  - 1 spsk salt
  - 1 spsk sennepskorn
  - 1 tsk peberkorn
  - 3 kvist dild
  - 1 fed hvidløg, skivet
  - ½ tsk chiliflager (valgfri)
steps:
  - Knæk de træede ender af. Blanchér aspargesene 60 sekunder i kogende vand. Isvand, dryp.
  - Stil dem oprejst i et højt, skoldet glas med dild og hvidløg.
  - Kog eddike, vand, sukker, salt og krydderier op.
  - Hæld den kogende lage over, så de er dækket.
  - Luk, lad køle, og stil koldt. Klar efter 24 timer — spis inden for 2 uger for maksimalt knæk.
faq:
  - question: Forskel på jeres hvide asparges?
    answer: Hvide skal skrælles og forkoges mere. Grønne er tyndere, grønnere og knaser mere som pickle.
  - question: Kan de være rå uden blanchering?
    answer: Ja til meget tynde. Tykke stænger bliver for seje uden det korte dunk i kogende vand.
  - question: Til hvad?
    answer: Grillbord, æg, røget laks, tapas og forårssandwich.
  - question: Holdbarhed?
    answer: Bedst inden for 2 uger i køleskab.
body: |
  Syltede grønne asparges med dild er forårets knæk — ikke den milde, hvide version.

  Grøn farve. Kort blanchering. Dild i glasset. De skal være sprøde, ikke silkebløde.
tip: Brug et højt glas, så stængerne står hele. Afklippede ender kan syltes i et lille glas til snack.
=====
title: Stegte sild i eddikesennepslage
slug: stegte-sild-eddikesennepslage
category: sylte
description: Stegte sild i eddikesennepslage — panerede, smørstegte sild lagt i varm eddikelage på glas. Nørdet klassiker.
prepTime: PT30M
cookTime: PT25M
totalTime: PT55M
servings: 4
difficulty: mellem
tags:
  - sild
  - stegte sild
  - sennep
  - smørrebrød
  - sylte
  - klassiker
imageAlt: Glas med stegte sildestykker i eddikesennepslage
featured: true
ingredients:
  - 8 sildefileter (friske eller optøede)
  - 1 dl rugmel eller hvedemel
  - Salt og peber
  - 50 g smør til stegning
  - Lage: 3 dl eddike (5 %), 1½ dl vand, 100 g sukker, 2 spsk grov sennep, 1 spsk sennepskorn, 1 rødløg i ringe, 1 tsk peberkorn, 2 laurbærblade, 4 nelliker
steps:
  - Dup sildene tørre. Vend i mel med salt og peber.
  - Steg i smør, til de er gyldne på begge sider. Læg på sugende papir.
  - Kog eddike, vand og sukker op. Rør sennep og krydderier i. Tag af varmen.
  - Læg sild og løgringe i lag i et glas eller fad. Hæld den varme lage over.
  - Køl af, og stil koldt mindst 1 døgn. Server kolde med rugbrød.
faq:
  - question: Varm lage på stegt fisk — koger den ikke?
    answer: Den sætter smagen og blødgør skorpen lidt. Det er meningen med den her disciplin.
  - question: Kan jeg bruge saltsild?
    answer: Nej til den her — den kræver friske/fileterede sild, der kan steges.
  - question: Til frokost?
    answer: Ja. Klassisk med rugbrød, æg og remoulade.
  - question: Holdbarhed?
    answer: 4–5 dage i køleskab under lagen.
body: |
  Stegte sild i eddikesennepslage er den nørdede mellemting mellem stegt fisk og syltet sild.

  Først smør og skorpe. Så varm lage. Dagen efter er de klar til rugbrødet.
tip: Steg ikke for mørkt. Lagen mørkner dem yderligere i glasset.
=====
title: Klassiske kryddersild fra bunden
slug: klassiske-kryddersild
category: sylte
description: Klassiske kryddersild fra bunden — udvandede saltsild i hemmelig krydderlage med allehånde og sandeltræ.
prepTime: PT40M
cookTime: PT15M
totalTime: PT48H
servings: 8
difficulty: svær
tags:
  - kryddersild
  - saltsild
  - jul
  - påske
  - smørrebrød
  - sylte
  - klassiker
imageAlt: Glas med klassiske kryddersild i mørk krydderlage
featured: true
ingredients:
  - 4 hele saltsild (eller 800 g saltsildsfileter)
  - Lage: 3 dl eddike (5 %), 2 dl vand, 200 g sukker
  - 2 spsk hele allehånde
  - 1 spsk peberkorn
  - 1 spsk sennepskorn
  - 8 nelliker
  - 2 kanelstænger
  - 4 laurbærblade
  - 1 tsk sandeltræspåner til madbrug (eller 1 ekstra kanelstang, hvis du ikke har)
  - 1 rødløg i ringe
  - Evt. 1 spsk skåret frisk ingefær
steps:
  - Udblød saltsildene i koldt vand 24–36 timer. Skift vand 3–4 gange. Smag — de skal være behageligt salte, ikke stikkende.
  - Flå, ben og skær i passende stykker. Dup tørre.
  - Kog eddike, vand og sukker op med alle krydderier. Lad lagen køle helt af.
  - Læg sild, løg og krydderier i lag i glas.
  - Hæld den kolde lage over. Stil koldt mindst 3–5 dage før servering.
faq:
  - question: Hvorfor sandeltræ?
    answer: Det er den gamle, røde farve og duft i klassisk kryddersild. Brug kun madgodkendt sandeltræ — ellers ekstra kanel.
  - question: Kan lagen være varm?
    answer: Nej. Varm lage koger fisken. Kryddersild skal have kold lage.
  - question: For salte efter udvanding?
    answer: Endnu et vandskift, eller læg 2 timer mere i friskt vand.
  - question: Til jul?
    answer: Ja — det er højsæsonen sammen med påske.
body: |
  Klassiske kryddersild fra bunden starter med saltsild og tålmodighed.

  Udvand rigtigt. Kold krydderlage. Allehånde og sandeltræ. Så smager de af julefrokost, ikke af købepose.
tip: Smag på silden efter udvanding, før du bygger glasset. For salt nu bliver aldrig godt senere.
=====
title: Rødvins-sild på glas
slug: roedvins-sild
category: sylte
description: Rødvins-sild på glas — sildestykker i dyb, purpurrød lage med rødvin, kanel og nelliker til julefrokosten.
prepTime: PT25M
cookTime: PT10M
totalTime: PT35M
servings: 6
difficulty: mellem
tags:
  - sild
  - rødvin
  - jul
  - smørrebrød
  - sylte
  - klassiker
imageAlt: Glas med sildestykker i purpurrød rødvinslage
featured: true
ingredients:
  - 500 g klar-til-brug sildestykker eller udvandede saltsild
  - 2 dl rødvin (tør, ikke for tanninrig)
  - 1½ dl rødvinseddike
  - 1 dl vand
  - 150 g sukker
  - 1 rødløg i ringe
  - 1 kanelstang
  - 6 nelliker
  - 1 tsk allehånde
  - 2 laurbærblade
  - 1 tsk peberkorn
steps:
  - Hvis saltsild: udvand 12–24 timer, skift vand, skær i stykker. Købesild: skyl fri for gammel lage.
  - Kog rødvin, eddike, vand, sukker og krydderier op. Lad lagen køle helt af.
  - Læg sild og løgringe i lag i glas.
  - Hæld den kolde, røde lage over, så silden er dækket.
  - Stil koldt mindst 2–3 dage. Lagen farver silden dybt purpurrød.
faq:
  - question: Hvilken rødvin?
    answer: En billig, blød, tør rødvin. Undgå meget fadeprægede vine — de smager af eg i glasset.
  - question: Kold eller varm lage?
    answer: Kold. Ellers mister silden teksturen.
  - question: Til julefrokost?
    answer: Ja — de ser festlige ud, og smager af kanel og vin til rugbrødet.
  - question: Holdbarhed?
    answer: Ca. 1 uge i køleskab under lagen.
body: |
  Rødvins-sild er julefrokostens mørkerøde glas.

  Vin, kanel, nelliker. Silden bliver purpurrød og festlig uden at miste bid.
tip: Lav dem i gennemsigtige glas — farven er halvdelen af oplevelsen på bordet.
=====
title: Syltede blæksprutteringe med hvidløg og citron
slug: syltede-blaeksprutteringe-hvidloeg-citron
category: sylte
description: Syltede blæksprutteringe med hvidløg og citron — sydeuropæisk konservering i syrlig, saltet olielage til tapas.
prepTime: PT25M
cookTime: PT15M
totalTime: PT40M
servings: 4
difficulty: mellem
tags:
  - blæksprutte
  - hvidløg
  - citron
  - tapas
  - sylte
  - middelhav
imageAlt: Glas med syltede blæksprutteringe i olie med hvidløg og citron
featured: true
ingredients:
  - 500 g rensede blæksprutteringe (friske eller optøede)
  - 3 dl olivenolie
  - 1 dl hvidvinseddike
  - 4 fed hvidløg, skivet
  - Skræl af 1 citron (uden hvid bitterdel)
  - Saft af ½ citron
  - 1 tsk salt
  - ½ tsk chiliflager
  - 1 tsk peberkorn
  - 1 kvist rosmarin eller oregano
steps:
  - Bring en gryde saltet vand i kog. Kog blæksprutteringene 45–90 sekunder, til de lige bliver ugennemsigtige. Hæld i isvand, og dryp knastørt.
  - Varm olien blidt med hvidløg, citronskal, chili, peber og urter — den må ikke brune hvidløget. Tag af varmen. Rør eddike, citronsaft og salt i.
  - Læg blæksprutteringene i et rent glas.
  - Hæld den lunkne olie-eddike-lage over, så de er dækket.
  - Køl, og stil koldt mindst 12 timer. Server ved stuetemperatur som tapas.
faq:
  - question: Bliver de gummiagtige?
    answer: Kun hvis de koges for længe. Kort blanchering, så olie. For lang kogning = elastik.
  - question: Er det ægte syltning?
    answer: Det er syre- og saltkonservering i olie — mere middelhav end mormor-eddike, men samme glas-idé.
  - question: Til hvad?
    answer: Tapas, pasta, salater og pandestegte grøntsager.
  - question: Holdbarhed?
    answer: 4–5 dage i køleskab, helt dækket af olie. Spis dem friske.
body: |
  Syltede blæksprutteringe med hvidløg og citron er sydeuropæisk glas-mad.

  Kort kog. Olie. Syre. Salt. De skal være møre med bid — klar til tapasbrættet.
tip: Dup ringene ekstremt tørre før olien. Vand i glasset er fjenden for holdbarhed og smag.
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
            data["difficulty"] = line[13:]
        elif line.startswith("imageAlt: "):
            data["imageAlt"] = line[10:]
        elif line.startswith("featured: "):
            data["featured"] = line[10:]
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
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


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
publishedAt: 2026-08-27
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
    path.write_text(to_mdx(d), encoding="utf-8")
    print("wrote", d["category"] + "/" + path.name)
