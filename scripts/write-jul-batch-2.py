#!/usr/bin/env python3
"""Jul batch 2 — 20 småkager, drikke, tilbehør og hovedretter (nov 2026)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"
PUBLIC = Path(__file__).resolve().parent.parent / "public/recipes"
PUBLISHED = "2026-11-15"

RECIPES = r'''
=====
title: Pebernødder
slug: pebernoedder
category: ovn
description: Pebernødder — små, krydrede julesmåkager med peber, kanel og ingefær. Sprøde, brune og uundværlige i juleskålen.
prepTime: PT25M
cookTime: PT12M
totalTime: PT1H40M
servings: 50
difficulty: nem
tags:
  - pebernødder
  - småkager
  - jul
  - dessert
  - ovn
  - festmad
imageAlt: Små brune pebernødder i en skål på julebord
featured: true
ingredients:
  - 250 g hvedemel
  - 125 g smør, blødt
  - 125 g farin
  - 1 æg
  - 1 tsk stødt peber
  - 1 tsk kanel
  - ½ tsk stødt ingefær
  - ½ tsk stødt nellike
  - ½ tsk bagepulver
  - 1 knivspids salt
steps:
  - Rør smør og farin luftigt. Tilsæt æg. Bland mel, krydderier, bagepulver og salt, og fold i.
  - Ælt til en smidig dej. Form til lange pølser (ca. 1,5 cm tykke). Pak ind, og køl 1 time.
  - Skær i 1 cm stykker. Læg på bagepapir med afstand.
  - Bag ved 180 °C varmluft 10–12 minutter, til de er gyldne og faste. Køl på rist — de hærder, når de køler.
faq:
  - question: For bløde pebernødder?
    answer: Dejen var for varm, eller de bagte for kort. Køl dejen, og bag til de er faste i kanten. De bliver sprødere overnight i lukket dåse.
  - question: Kan dejen fryses?
    answer: Ja. Frys pølserne. Tø i køleskab, skær og bag. Eller bag først, og frys færdige pebernødder.
  - question: Hvor stærke skal de være?
    answer: Peber skal mærkes, ikke brænde. Start med 1 tsk — øg næste gang, hvis du vil have mere jutlandsk bid.
  - question: Holdbarhed?
    answer: 2–3 uger i tæt dåse ved stuetemperatur. Smagen bliver dybere efter et par dage.
body: |
  Pebernødder er jul i en skål — små, brune, krydrede og umulige at stoppe ved én.

  Peber, kanel, ingefær, nellike. Ikke pynt. Ikke glasur. Bare dej, varme og tålmodighed.

  Køl dejen. Skær jævnt. Bag til de er faste — sprødheden kommer, når de køler.
tip: Rul pølserne på let melet bord, og skær med skarp kniv — ujævne stykker brænder i spidserne.
=====
title: Brunkager
slug: brunkager
category: ovn
description: Brunkager — tynde, sprøde julesmåkager med sirup, kanel og nellike. Den klassiske rulledej, der skæres tyndt og bages gylden.
prepTime: PT30M
cookTime: PT10M
totalTime: PT4H45M
servings: 80
difficulty: mellem
tags:
  - brunkager
  - småkager
  - jul
  - dessert
  - ovn
  - festmad
imageAlt: Tynde gyldne brunkager stablet på fad
featured: true
ingredients:
  - 250 g hvedemel
  - 125 g smør
  - 125 g farin
  - 50 g lys sirup
  - 1 æg
  - 1 tsk kanel
  - ½ tsk stødt nellike
  - ½ tsk stødt ingefær
  - ½ tsk bagepulver
  - 1 knivspids salt
  - Evt. mandelspåner til pynt
steps:
  - Smelt smør, farin og sirup sammen under omrøring. Køl til lunkent.
  - Rør æg i. Bland mel, krydderier, bagepulver og salt, og ælt til en blød dej.
  - Form to pølser (ca. 4–5 cm tykke). Pak i film, og køl mindst 3 timer — gerne overnight.
  - Skær i meget tynde skiver (2–3 mm). Læg på bagepapir. Evt. drys mandelspåner.
  - Bag ved 175 °C varmluft 8–10 minutter, til de er dybt gyldne. Køl på rist — de sprøder op.
faq:
  - question: Dejen er for blød at skære?
    answer: Ikke kølet nok. Frys 20 minutter, så skær. Tynde skiver kræver kold, fast dej.
  - question: Brunkagerne er seje?
    answer: For tykke, eller bagt for kort. De skal være mørke gyldne og knække. Opbevar i tæt dåse med tørrepapir.
  - question: Sirup eller honning?
    answer: Lys sirup er klassikeren. Honning gør dem blødere og sødere — brug kun hvis du vil have den smag.
  - question: Hvor længe holder de?
    answer: Op til 3 uger i dåse. Smagen bliver mere krydret efter et par dage.
body: |
  Brunkager er den tynde, sirupsagtige julesmåkage, der knækker mellem tænderne.

  Sirup, farin, kanel, nellike. Dejen skal være kold. Skiverne skal være tynde.

  For tykke brunkager er bare cookies. Tynde er tradition.
tip: Skær med skarp kniv og let tryk — trykker du hårdt, bliver skiverne ovale og ujævne i tykkelsen.
=====
title: Vaniljekranse
slug: vaniljekranse
category: ovn
description: Vaniljekranse — sprøde smørsmåkager sprøjtet i kranse med ægte vanilje. Den danske juleklassiker til kaffebordet.
prepTime: PT40M
cookTime: PT12M
totalTime: PT1H
servings: 40
difficulty: mellem
tags:
  - vaniljekranse
  - småkager
  - jul
  - dessert
  - ovn
  - vanilje
imageAlt: Gyldne vaniljekranse på bageplade
featured: true
ingredients:
  - 250 g hvedemel
  - 200 g smør, koldt og i tern
  - 100 g flormelis
  - 1 æg
  - 1 vaniljestang, frøene (eller 2 tsk vaniljesukker)
  - 1 knivspids salt
steps:
  - Bland mel, flormelis, vaniljefrø og salt. Smuldr smørret i, til det ligner sand. Tilsæt æg, og ælt hurtigt til en smidig dej.
  - Fyld dejen i sprøjtepose med stjernetylle (ca. 10–12 mm). Sprøjt kranse (5–6 cm) på bagepapir.
  - Køl pladerne 15 minutter i køleskab, så kranse holder formen.
  - Bag ved 190 °C traditionel varme 10–12 minutter, til de er lyse gyldne i kanten. Køl på rist.
faq:
  - question: Dejen er for blød til at sprøjte?
    answer: Smørret var for varmt. Køl dejen 20 minutter, og prøv igen. For kold dej sprøjter heller ikke — den skal være plastisk.
  - question: Kranse flyder ud?
    answer: For varm ovn, eller dejen for blød. Køl før bagning. Brug traditionel varme, ikke for aggressiv varmluft.
  - question: Vaniljestang eller sukker?
    answer: Stang giver dybere smag og sorte prikker. Vaniljesukker virker — brug 2 tsk, og skip ikke saltet.
  - question: Uden sprøjtepose?
    answer: Du kan rulle små stænger og forme ringe, men det er ikke den klassiske rifledes kant. En god tyllé er halvdelen af kagen.
body: |
  Vaniljekranse er smør, vanilje og tålmodighed med en sprøjtepose.

  Dejen skal være kold nok til at holde riflerne, blød nok til at presse. Det er balancen.

  Lyse gyldne — ikke brune. Vaniljen skal smage, ikke karamel.
tip: Hold posen lodret og tæt på pladen. Træk i en jævn cirkel — stopper du midtvejs, får du en tyk samling.
=====
title: Honningkagehjerter
slug: honningkagehjerter
category: ovn
description: Honningkagehjerter — bløde, krydrede hjerter med honning og glasur. Klassisk julesmåkage der holder i uger.
prepTime: PT35M
cookTime: PT12M
totalTime: PT1H50M
servings: 30
difficulty: mellem
tags:
  - honningkagehjerter
  - honningkager
  - småkager
  - jul
  - dessert
  - ovn
imageAlt: Honningkagehjerter med hvid glasur på fad
featured: true
ingredients:
  - 300 g hvedemel
  - 100 g honning
  - 75 g farin
  - 75 g smør
  - 1 æg
  - 1 tsk kanel
  - ½ tsk stødt ingefær
  - ½ tsk stødt nellike
  - 1 tsk bagepulver
  - 1 knivspids salt
  - Glasur: 100 g flormelis + 1–2 spsk vand eller citronsaft
steps:
  - Varm honning, farin og smør forsigtigt, til det er smeltet og rørt sammen. Køl til lunkent.
  - Rør æg i. Bland mel, krydderier, bagepulver og salt, og ælt til en blød dej. Køl 1 time.
  - Rul ud på melet bord til ca. 5 mm. Stik hjerter ud. Læg på bagepapir.
  - Bag ved 175 °C varmluft 10–12 minutter, til de er gyldne. Køl helt.
  - Rør glasur, og pensl eller dryp på. Lad sætte, før du lægger i dåse.
faq:
  - question: Bløde eller sprøde?
    answer: Honningkagehjerter skal være bløde midt i og faste i kanten. For tynde = knækbrød. Hold 5 mm.
  - question: Kan dejen laves dagen før?
    answer: Ja — den bliver lettere at rulle efter en nat i køleskab. Tag den ud 15 minutter før udrulning.
  - question: Glasur med æggehvide?
    answer: Klassisk royal icing holder længere. Flormelis og vand er hurtigere og fint til hjemmebrug.
  - question: Holdbarhed?
    answer: 2–3 uger i tæt dåse. Honningen holder dem fugtige — pak ikke varme kager.
body: |
  Honningkagehjerter er bløde, krydrede og søde nok til at høre julen til — uden at være pebernødder.

  Honning giver fugt. Krydderierne giver dybde. Glasuren er pynt, ikke struktur.

  Rul jævnt. Bag gyldent. Glasér kolde.
tip: Dyp udstikkeren i mel mellem hvert hjerte, så dejen ikke hænger fast og trækker formen skæv.
=====
title: Finske brød
slug: finske-broed
category: ovn
description: Finske brød — smørsmåkager formet som små brød med rille og perlesukker. Sprøde, enkle og fast inventar i juleskålen.
prepTime: PT30M
cookTime: PT12M
totalTime: PT1H15M
servings: 40
difficulty: nem
tags:
  - finske brød
  - småkager
  - jul
  - dessert
  - ovn
imageAlt: Finske brød med perlesukker på bageplade
featured: true
ingredients:
  - 250 g hvedemel
  - 200 g smør, blødt
  - 80 g flormelis
  - 1 æggeblomme til dejen
  - 1 æggehvide til pensling
  - 1 tsk vaniljesukker
  - 1 knivspids salt
  - Perlesukker til drys
steps:
  - Rør smør og flormelis luftigt. Tilsæt æggeblomme og vaniljesukker. Fold mel og salt i til en smidig dej.
  - Form små brød (ca. 5 cm lange). Læg på bagepapir. Tryk en rille på langs med knivryggen.
  - Pensl med æggehvide. Drys perlesukker i rillen og ovenpå.
  - Bag ved 180 °C varmluft 10–12 minutter, til de er lyse gyldne. Køl på rist.
faq:
  - question: Hvorfor hedder de finske brød?
    answer: Navnet er dansk tradition — formen ligner små brød. Dejen er en klassisk dansk smørsmåkage.
  - question: Dejen smuldrer?
    answer: For koldt smør, eller for meget mel. Smørret skal være blødt, ikke smeltet. Ælt kort.
  - question: Perlesukker falder af?
    answer: Pensl ordentligt med æggehvide, og tryk sukkeret let ned. Bag, mens det er vådt.
  - question: Kan de fryses?
    answer: Ja, både som rå formede brød og bagte. Bag direkte fra fryser med 1–2 min ekstra.
body: |
  Finske brød er den enkle julesmåkage — smør, flormelis, en rille og perlesukker.

  Ingen krydderier. Ingen glasur. Bare form og knas.

  Rillen er ikke pynt — den holder sukkeret, og giver det lille brød sin silhuet.
tip: Form alle brødene først, så pensl og drys i ét hug — æggehviden må ikke tørre før sukkeret lander.
=====
title: Jødekager
slug: joedekager
category: ovn
description: Jødekager — tynde, sprøde julesmåkager med kanel og farin ovenpå. Udstukket rundt og bagt til de er knasende.
prepTime: PT30M
cookTime: PT10M
totalTime: PT1H40M
servings: 50
difficulty: nem
tags:
  - jødekager
  - småkager
  - jul
  - dessert
  - ovn
imageAlt: Runde jødekager med kanelsukker på fad
featured: true
ingredients:
  - 250 g hvedemel
  - 150 g smør, blødt
  - 100 g sukker
  - 1 æg
  - 1 tsk vaniljesukker
  - ½ tsk bagepulver
  - 1 knivspids salt
  - Topping: 2 spsk farin + 1 tsk kanel
  - 1 æggehvide til pensling
steps:
  - Rør smør og sukker luftigt. Tilsæt æg og vaniljesukker. Fold mel, bagepulver og salt i. Køl dejen 1 time.
  - Rul ud til ca. 3 mm på melet bord. Stik runde kager ud (5–6 cm).
  - Pensl med æggehvide. Drys kanelsukker. Læg på bagepapir.
  - Bag ved 180 °C varmluft 8–10 minutter, til de er lyse gyldne. Køl på rist.
faq:
  - question: For tykke jødekager?
    answer: De skal være tynde og sprøde. 3 mm er målet. Tykkere bliver bløde midt i.
  - question: Kanelsukkeret brænder?
    answer: For høj varme eller for lang tid. Hold øje fra minut 7 — farin bruner hurtigt.
  - question: Dejen klistrede ved udrulning?
    answer: Køl mere, eller rul mellem to stykker bagepapir. Mindre mel ovenpå = mere møre kager.
  - question: Samme dej som brunkager?
    answer: Nej — jødekager er lysere, mindre krydrede, og får kanelsukker ovenpå i stedet for sirup i dejen.
body: |
  Jødekager er den lyse, tynde julesmåkage med kanelsukker på toppen.

  Ikke pebernødder. Ikke brunkager. Rund, sprød, og færdig på under et kvarter i ovnen.

  Tyndt rullet. Let penslet. Gylden — ikke mørk.
tip: Stik kagerne tæt, så du genbruger mindst mulig dej — for meget genæltning gør dem seje.
=====
title: Lussekatter
slug: lussekatter
category: ovn
description: Lussekatter — safranfarvede juleboller snoet som S med rosiner. Klassisk Lucia-brød til advent og julemorgen.
prepTime: PT40M
cookTime: PT12M
totalTime: PT2H30M
servings: 16
difficulty: mellem
tags:
  - lussekatter
  - saffransbrød
  - jul
  - brød
  - ovn
  - festmad
imageAlt: Gyldne lussekatter med rosiner på bageplade
featured: true
ingredients:
  - 500 g hvedemel
  - 25 g gær
  - 2½ dl mælk, lun
  - 100 g smør, smeltet og afkølet
  - 100 g sukker
  - 1 g safran (1 brev)
  - 1 æg
  - 1 tsk salt
  - Rosiner til pynt
  - 1 æg til pensling
steps:
  - Kom safran i den lune mælk, og lad trække 10 minutter, så farven slipper.
  - Opløs gæren i mælken. Tilsæt sukker, æg, salt og det meste af melet. Ælt smørret i, og resten af melet til en smidig dej. Hæv 1 time under klæde.
  - Del i 16 stykker. Rul til snore, og form S-formede lussekatter. Læg rosiner i snoene. Hæv 30–40 minutter på bagepapir.
  - Pensl med sammenpisket æg. Bag ved 200 °C traditionel varme 10–12 minutter, til de er gyldne. Køl på rist.
faq:
  - question: Safran er dyrt — kan jeg skippe?
    answer: Så er det bare søde boller. Safran er smagen og den gule farve. Brug ægte safran, ikke farvestof.
  - question: Tøre lussekatter næste dag?
    answer: Normal. Frys samme dag, og tø/rist let. Eller opbevar i pose og varm 5 minutter i ovn ved 150 °C.
  - question: Kan dejen hæve overnight?
    answer: Ja i køleskab. Tag ud, form, og giv dem en anden hævning før bagning.
  - question: Uden rosiner?
    answer: Ja — traditionelt sidder de i snoene, men smagen er i safran og smør.
body: |
  Lussekatter er Lucia-morgenens gule brød — safran, smør og en S der holder rosinerne.

  Mælken skal trække safranen. Dejen skal hæve ordentligt. Snoen skal være stram nok til at holde formen.

  Gyldne, bløde, og bedst lune med smør.
tip: Pres rosinerne godt ned i dejen før anden hævning — ellers falder de af i ovnen.
=====
title: Julebrød
slug: julebroed
category: ovn
description: Julebrød — sødt gærbrød med rosiner, candied citrus og kardemomme. Ét stort brød til julemorgen eller adventskaffen.
prepTime: PT35M
cookTime: PT35M
totalTime: PT3H
servings: 12
difficulty: mellem
tags:
  - julebrød
  - julekage
  - jul
  - brød
  - ovn
  - festmad
imageAlt: Skiveskåret julebrød med rosiner og glasur
featured: true
ingredients:
  - 500 g hvedemel
  - 25 g gær
  - 2½ dl mælk, lun
  - 100 g smør, blødt
  - 80 g sukker
  - 1 æg
  - 1 tsk stødt kardemomme
  - 1 tsk salt
  - 150 g rosiner
  - 50 g candied orange eller citronskal, hakket
  - 1 æg til pensling
  - Evt. glasur: 100 g flormelis + 1 spsk vand
steps:
  - Opløs gær i mælk. Tilsæt sukker, æg, kardemomme, salt og det meste af melet. Ælt smørret i. Ælt 8–10 minutter til en smidig dej.
  - Fold rosiner og candied citrus i. Hæv 1–1½ time under klæde, til dejen er fordoblet.
  - Form til et langt brød eller fletning på bagepapir. Hæv 40–50 minutter.
  - Pensl med æg. Bag ved 180 °C varmluft 30–35 minutter, til det er dybt gyldent og lyder hult. Køl på rist.
  - Evt. glasér, når brødet er køligt.
faq:
  - question: Tørt julebrød?
    answer: Overbagt, eller for lidt fedt. Tjek ved 28 minutter. Frys skiver, og rist dem — bedre end tørt brød på bordet.
  - question: Kan jeg bruge surdej?
    answer: Ja, men det er en anden opskrift. Her er gær og kardemomme den danske julebrøds-vej.
  - question: Uden candied citrus?
    answer: Brug ekstra rosiner og lidt finrevet citronskal. Citrussen er duft, ikke struktur.
  - question: Dagen før?
    answer: Bag dagen før, og pak godt ind. Varm skiver let, eller toast. Glasér lige før servering.
body: |
  Julebrød er det søde gærbrød, der lugter af kardemomme og rosiner, når ovnen åbnes.

  Ikke stollen. Ikke lussekatter. Ét brød midt på bordet til kaffe og smør.

  Hæv tålmodigt. Bag gyldent. Skær, når det er køligt nok til ikke at smuldre.
tip: Læg rosinerne i blød 10 minutter i lunkent vand eller saft, og dup tørre — tørre rosiner stjæler fugt fra krummen.
=====
title: Berlinerkranser
slug: berlinerkranser
category: ovn
description: Berlinerkranser — smørsmåkager snoet som små kranser og dyppet i æggehvide og perlesukker. Sprød juleklassiker.
prepTime: PT35M
cookTime: PT12M
totalTime: PT1H20M
servings: 35
difficulty: mellem
tags:
  - berlinerkranser
  - småkager
  - jul
  - dessert
  - ovn
imageAlt: Berlinerkranser med perlesukker på fad
featured: true
ingredients:
  - 250 g hvedemel
  - 200 g smør, blødt
  - 2 æggeblommer hårdkogte, mosede
  - 2 rå æggeblommer
  - 80 g flormelis
  - 1 tsk vaniljesukker
  - 1 knivspids salt
  - 1 æggehvide til pensling
  - Perlesukker til drys
steps:
  - Rør smør og flormelis. Tilsæt mosede kogte blommer, rå blommer, vanilje og salt. Fold mel i til en smidig dej. Køl 30 minutter.
  - Tag små stykker, rul til snore (ca. 12 cm), og form kranser. Læg på bagepapir.
  - Pensl med æggehvide. Drys perlesukker.
  - Bag ved 180 °C varmluft 10–12 minutter, til de er lyse gyldne. Køl på rist.
faq:
  - question: Hvorfor kogte æggeblommer?
    answer: De giver den klassiske, smuldrende krumme. Skip dem, og du får bare en almindelig smørsmåkage.
  - question: Kransene åbner sig i ovnen?
    answer: Pres enderne godt sammen med lidt vand. Køl formede kranser 10 minutter før bagning.
  - question: Dejen er grålig?
    answer: De kogte blommer var for varme, eller for hårdt mosede med jern. Mos fint, og bland hurtigt.
  - question: Samme som vaniljekranse?
    answer: Nej — vaniljekranse sprøjtes. Berlinerkranser rulles og snoes, og har kogte blommer i dejen.
body: |
  Berlinerkranser er den snoede julesmåkage med perlesukker — og hemmeligheden er de kogte æggeblommer.

  Smuldrende krumme. Lyse gyldne. Sukker der knaser.

  Rul jævne snore. Luk kransen tæt. Bag forsigtigt.
tip: Kog æggene 9–10 minutter, og skræl under koldt vand — grønne blommer smager af svovl i dejen.
=====
title: Klassiske klejner
slug: klejner-friture
category: pande
description: Klassiske klejner — tynd dej snoet og friturestegt til gyldne, sprøde julesmåkager. Den originale metode før ovn og airfryer.
prepTime: PT40M
cookTime: PT30M
totalTime: PT2H30M
servings: 40
difficulty: mellem
tags:
  - klejner
  - småkager
  - jul
  - dessert
  - pande
  - friture
imageAlt: Gyldne friturestegte klejner med flormelis
featured: true
ingredients:
  - 300 g hvedemel
  - 75 g smør, blødt
  - 75 g sukker
  - 2 æg
  - 1 dl piskefløde
  - 1 tsk kardemomme
  - 1 tsk finrevet citronskal
  - ½ tsk bagepulver
  - 1 knivspids salt
  - Neutral olie til friture (ca. 1 liter)
  - Flormelis til drys
steps:
  - Rør smør og sukker. Tilsæt æg, fløde, kardemomme, citronskal og salt. Fold mel og bagepulver i. Køl dejen 1 time.
  - Rul ud tyndt (2–3 mm) på melet bord. Skær romber (ca. 3×8 cm). Lav et midtersnit, og træk den ene ende igennem — den klassiske sno.
  - Varm olie til 175 °C. Steg få klejner ad gangen 1–2 minutter, til de er gyldne. Vend undervejs.
  - Løft op på sugende papir. Drys flormelis, når de er lune.
faq:
  - question: Olien er for varm?
    answer: Klejnerne bruner udenpå og er råt indenunder. Hold 170–175 °C med termometer. For kold olie = fedtede klejner.
  - question: Sammenlignet med ovn-klejner?
    answer: Friture giver den ægte, lette knas. [Klejner i ovn](/opskrifter/ovn/klejner-ovn) er mindre rod — men smager anderledes.
  - question: Dejen er for elastisk?
    answer: For meget æltning eller for varm dej. Køl, og rul med bestemthed — tyndt er vigtigere end perfekt form.
  - question: Kan olien genbruges?
    answer: Ja et par gange til sødt. Si den, og gem køligt. Smid ud, når den lugter eller skummer vildt.
body: |
  Klassiske klejner er friture — ikke ovn, ikke airfryer. Tynd dej, sno, gylden olie.

  Kardemomme og citron i dejen. Flormelis ovenpå. Sprødhed, der kun kommer af boblende fedt.

  Hold temperaturen. Steg få ad gangen. Drys, mens de er lune.
tip: Hav en hæklenål eller spyd klar til at vende klejnerne — en gaffel river snoen op.
=====
title: Romkugler
slug: romkugler
category: pande
description: Romkugler — restekager blendet med kakao, rom og kokos. Nem juleslik uden ovn, klar på under en time.
prepTime: PT25M
cookTime: PT0M
totalTime: PT55M
servings: 25
difficulty: nem
tags:
  - romkugler
  - jul
  - dessert
  - slik
  - pande
  - restemad
imageAlt: Romkugler rullet i kokos på fad
featured: true
ingredients:
  - 300 g tørre kagerester eller kagerester (ca. ½ tårn)
  - 100 g smør, blødt
  - 75 g flormelis
  - 2 spsk kakao
  - 2–3 spsk rom (eller rom-essens + 1 spsk vand)
  - 1 spsk stærk kaffe, kold (valgfrit)
  - Kokosmel eller krymmel til rullning
steps:
  - Smuldr kagerne fint — blender eller rivejern. De skal ligne groft sand.
  - Rør smør, flormelis, kakao, rom og evt. kaffe i. Bland kagesmuld i til en formbar masse. Smag til — mere rom eller kakao efter behov.
  - Køl 20–30 minutter, så massen sætter sig.
  - Rul kugler (ca. 3 cm). Vend i kokos eller krymmel. Sæt køligt til servering.
faq:
  - question: Uden alkohol?
    answer: Brug rom-essens og en skvæt kaffe eller mælk. Smagen skal stadig være rund og sød.
  - question: Massen smuldrer?
    answer: For tørre kager. Tilsæt mere smør eller en skvæt mælk/rom, til den klistrer mellem fingrene.
  - question: Hvilke kagerester?
    answer: Sandkage, muffins, tørre bunde — blandet er fint. Undgå cremede lagkager med meget fløde.
  - question: Holdbarhed?
    answer: 4–5 dage i køleskab i lukket boks. Frys i op til en måned.
body: |
  Romkugler er julens resteslik — tørre kager, kakao, rom og kokos.

  Ingen ovn. Ingen dej. Bare blanding, køl og rul.

  De skal smage af rom og kakao, ikke af gamle muffins. Smag til, før du ruller.
tip: Rul med let fugtige hænder, så massen ikke klistre — tør hænderne, før du vender i kokos.
=====
title: Gløgg
slug: gloegg
category: gryde
description: Hjemmelavet gløgg — rødvin med snaps, safran, kanel og mandler. Varm juleklassiker til advent og julefrokost.
prepTime: PT15M
cookTime: PT30M
totalTime: PT1H
servings: 8
difficulty: nem
tags:
  - gløgg
  - jul
  - drikke
  - festmad
  - gryde
  - advent
imageAlt: Dampende gløgg med mandler og rosiner i glas
featured: true
ingredients:
  - 1 flaske rødvin (75 cl)
  - 2 dl portvin eller sød rødvin (valgfrit)
  - 1 dl snaps eller vodka
  - 100 g sukker
  - 2 kanelstænger
  - 8 hele nelliker
  - 4 kardemommefrø, knuste
  - 1 stykke frisk ingefær (2 cm), skåret
  - Skal af ½ appelsin
  - 1 knivspids safran (valgfrit)
  - 50 g mandler, skoldede
  - 50 g rosiner
steps:
  - Læg mandler og rosiner i blød i lidt af snapsen eller varmt vand.
  - Kom vin, portvin, sukker, kanel, nelliker, kardemomme, ingefær, appelsinskal og safran i en gryde. Varm langsomt op — må ikke koge.
  - Simre meget lavt 20–30 minutter under låg, så krydderierne trækker. Smag til med sukker.
  - Si krydderierne fra. Tilsæt snaps. Hold varm uden at koge.
  - Server i glas med mandler og rosiner i bunden.
faq:
  - question: Må gløggen koge?
    answer: Nej — så forsvinder alkoholen, og smagen bliver flad. Hold den under kogepunktet. Brug termometer, hvis du er i tvivl (under 80 °C).
  - question: Alkoholfri gløgg?
    answer: Brug saft (solbær/æble) i stedet for vin, og skip snaps. Krydderierne er de samme. Sødn til.
  - question: Kan den laves dagen før?
    answer: Ja. Lav basen uden snaps, køl, og varm forsigtigt op. Tilsæt snaps lige før servering.
  - question: Til [gløgg-mørbrad](/opskrifter/ovn/gloegg-svinemoerbrad-jul)?
    answer: Samme krydderprofil — men her drikker du den. Brug en tør-ish rødvin, så den ikke bliver sirup.
body: |
  Gløgg er varm vin, krydderier og snaps — ikke en dessert i et glas.

  Den må ikke koge. Sukkeret skal smelte. Mandler og rosiner er bunden i glasset.

  Lav mere end du tror. Den forsvinder, når døren åbnes.
tip: Varm gløggen i en tung gryde på laveste blus, og hold den med låg — mikrobølgeovn dræber aromaen.
=====
title: Kirsebærsauce
slug: kirsebaersauce
category: gryde
description: Kirsebærsauce — blank, syrlig sauce til risalamande. Lavet på frostkirsebær, sukker og citron på under 20 minutter.
prepTime: PT5M
cookTime: PT15M
totalTime: PT20M
servings: 8
difficulty: nem
tags:
  - kirsebærsauce
  - jul
  - dessert
  - sauce
  - tilbehør
  - gryde
imageAlt: Blank kirsebærsauce i skål med hele kirsebær
featured: true
ingredients:
  - 500 g kirsebær (frost eller glas, afløbne)
  - 1 dl sukker
  - 1 dl saft fra kirsebær eller vand
  - 1 spsk majsstivelse
  - Saft af ½ citron
  - 1 knivspids salt
  - Evt. 1 spsk kirsebærvin eller portvin
steps:
  - Kom kirsebær, sukker, saft/vand og salt i en gryde. Kog op, og simre 5–8 minutter, til bærrene er bløde.
  - Rør majsstivelse ud i 2 spsk koldt vand. Hæld i under omrøring, og kog 1 minut, til saucen er blank og tykner.
  - Smag til med citronsaft og evt. vin. Den skal være syrlig nok til at skære fløde.
  - Server lun til kold [risalamande](/opskrifter/gryde/risalamande-kirsebaersauce).
faq:
  - question: For sød sauce?
    answer: Mere citron. Glas-kirsebær er ofte søde i forvejen — skær sukkeret ned, og byg syre op.
  - question: For tynd?
    answer: Lidt mere majsstivelse udrørt i koldt vand, og kog op igen. Den tykner også lidt, når den køler.
  - question: Dagen før?
    answer: Ja. Køl, og varm forsigtigt op. Rør, så den bliver blank igen.
  - question: Uden majsstivelse?
    answer: Reducér længere — men majsstivelse giver den klassiske blanke konsistens uden at koge bærrene i stykker.
body: |
  Kirsebærsauce er risalamandens syrlige modvægt — blank, rød og ikke kun sød.

  Frostbær slår de fleste glas. Citron er ikke valgfri.

  Tykn kort. Smag til. Server lun til kold dessert.
tip: Si ikke bærrene fra — hele kirsebær i saucen er halvdelen af oplevelsen på skeen.
=====
title: Sølvkål
slug: soelvkaal
category: gryde
description: Sølvkål — hvidkål simret med eddike, sukker og ribsgele til syrlig juletilbehør. Det lyse alternativ til rødkål.
prepTime: PT20M
cookTime: PT45M
totalTime: PT1H5M
servings: 8
difficulty: nem
tags:
  - sølvkål
  - hvidkål
  - jul
  - tilbehør
  - gryde
  - festmad
imageAlt: Lys sølvkål i gryde med blank sauce
featured: true
ingredients:
  - 1 kg hvidkål, fint snittet
  - 1 stort æble, groft revet
  - 1 løg, fint hakket
  - 2 spsk smør
  - 2 spsk eddike (æble- eller hvidvinseddike)
  - 2 spsk sukker
  - 2 spsk ribsgele eller solbærgele
  - 1 tsk salt
  - ½ tsk peber
  - 1 dl vand eller æblejuice
steps:
  - Smelt smør i en bred gryde. Svits løg 3–4 minutter uden farve.
  - Tilsæt kål og æble. Vend godt. Kom vand, eddike, sukker, salt og peber i.
  - Simre under låg 35–45 minutter på lav varme, rør jævnligt, til kålen er mør men stadig har bid.
  - Rør ribsgele i. Smag til — den skal være syrlig-sød. Evt. mere eddike eller sukker.
  - Server lun til flæskesteg, and eller [hamburgerryg](/opskrifter/gryde/hamburgerryg).
faq:
  - question: Samme som stuvet hvidkål?
    answer: Nej — sølvkål er syrlig og blank med gele/eddike, ikke cremet hvid sauce.
  - question: Kan den laves dagen før?
    answer: Ja. Den bliver ofte bedre. Varm forsigtigt, og smag til med eddike igen.
  - question: Rødkål i stedet?
    answer: Så er det [hjemmelavet rødkål](/opskrifter/gryde/hjemmelavet-roedkaal). Sølvkål er den lyse variant til samme bord.
  - question: For våd?
    answer: Kog færdig uden låg 5 minutter. Kålen skal skinne, ikke svømme.
body: |
  Sølvkål er julebordets lyse kål — hvidkål, æble, eddike og gele.

  Den skal være syrlig nok til at skære fedt fra flæskesteg og and. Ikke stuvet. Ikke rå.

  Simre lavt. Rør gele i til sidst. Smag til skarpt.
tip: Snit kålen fint på mandolin eller med skarp kniv — grove stykker bliver ujævnt møre.
=====
title: Rødkålssalat
slug: roedkaalssalat
category: palaeg
description: Rødkålssalat — rå rødkål med æble, mandler og syrlig dressing. Friskt juletilbehør til frokostbordet uden kogning.
prepTime: PT20M
cookTime: PT0M
totalTime: PT20M
servings: 6
difficulty: nem
tags:
  - rødkålssalat
  - rødkål
  - jul
  - salat
  - tilbehør
  - pålæg
  - frokost
imageAlt: Rødkålssalat med æble og mandler i skål
featured: true
ingredients:
  - ½ lille rødkål (ca. 400 g), meget fint snittet
  - 1 æble, i tynde både
  - 50 g mandler, groft hakkede og ristede
  - 2 spsk rosiner eller tranebær
  - Dressing: 2 spsk æblecidereddike, 1 spsk dijonsennep, 1 spsk honning, 3 spsk olie, salt og peber
steps:
  - Snit rødkålen so fine strimler. Læg i en skål.
  - Pisk dressingen sammen. Hæld over kålen, og massage den ind med hænderne 1 minut — kålen blødgøres.
  - Vend æble, rosiner/tranebær og mandler i. Smag til med salt, peber og evt. mere eddike.
  - Server med det samme, eller lad trække 15–30 minutter i køleskab.
faq:
  - question: I stedet for kogt rødkål?
    answer: Ja til frokost og buffet. Til juleaftens flæskesteg er [hjemmelavet rødkål](/opskrifter/gryde/hjemmelavet-roedkaal) stadig klassikeren.
  - question: Kålen er for hård?
    answer: Snit finere, og massage længere med dressingen. Salt hjælper med at trække væske.
  - question: Dagen før?
    answer: Gerne — men tilsæt mandler lige før servering, så de forbliver knasende.
  - question: Mayo-version?
    answer: Du kan erstatte olien med 3 spsk mayonnaise til en cremet julesalat. Hold syren.
body: |
  Rødkålssalat er den rå, knasende side til julefrokosten — ikke den kogte i gryden.

  Fin snit. Syrlig dressing. Æble og mandler for sødme og knas.

  Massér dressingen ind. Det er forskellen på salat og hård kål.
tip: Brug de yderste blade til noget andet — midten af kålhovedet er sødere og finere at snitte.
=====
title: Nødderost til jul
slug: noedderost-jul
category: ovn
description: Nødderost til jul — vegetarisk julehovedret med blandede nødder, linser og krydderurter bagt som en stege. Skærbar og festlig.
prepTime: PT30M
cookTime: PT50M
totalTime: PT1H20M
servings: 8
difficulty: mellem
tags:
  - nødderost
  - vegetar
  - jul
  - festmad
  - ovn
  - hovedret
imageAlt: Skiveskåret nødderost med urter på fad
featured: true
ingredients:
  - 200 g blandede nødder (valnød, hasselnød, mandel), groft hakkede
  - 150 g kogte grønne eller brune linser
  - 1 stort løg, hakket
  - 2 fed hvidløg, hakket
  - 100 g champignon, hakket
  - 2 spsk smør eller olie
  - 100 g rasp eller havregryn
  - 2 æg
  - 2 spsk soyasauce
  - 1 spsk tomatpuré
  - 1 tsk timian
  - 1 tsk rosmarin, hakket
  - ½ tsk peber
  - 1 tsk salt
  - 50 g parmesan eller stærk ost, revet (valgfrit)
steps:
  - Svits løg, hvidløg og champignon i smør, til væsken er væk, og det dufter. Køl lidt.
  - Bland nødder, linser, rasp, æg, soja, tomatpuré, urter, salt, peber og ost. Tilsæt svitsede grøntsager. Massen skal kunne formes — tilsæt rasp hvis den er for våd.
  - Beklæd en brødform (ca. 1,5 L) med bagepapir. Press massen godt ned.
  - Bag ved 180 °C varmluft 45–50 minutter, til den er fast og dybt gylden ovenpå.
  - Hvil 10 minutter. Løft ud, og skær i skiver. Server med [brun sovs](/opskrifter/pande/brun-sovs), [brunede kartofler](/opskrifter/gryde/brunede-kartofler) og [sølvkål](/opskrifter/gryde/soelvkaal).
faq:
  - question: Kan den være vegansk?
    answer: Erstat æg med 2 spsk chia + 6 spsk vand (gelé 10 min), og skip osten. Bindningen bliver lidt løsere — press godt i formen.
  - question: For smuldrende?
    answer: For lidt væske/æg, eller hakkede nødder for grove. Blend ⅓ af nødderne finere, og press massen hårdt.
  - question: Dagen før?
    answer: Ja. Bag, køl, og varm skiver i ovn 160 °C i 15 minutter. Eller bag lige før gæsterne kommer.
  - question: Hvilke nødder?
    answer: Blanding vinder. Kun mandel bliver mild. Kun valnød kan bitter — rist nødderne let først for dybde.
body: |
  Nødderost er den vegetariske julehovedret, der faktisk kan skæres og stå midt på bordet.

  Nødder, linser, svitsede svampe. Presset, bagt, hvilende.

  Den skal have skorpe udenpå og være saftig nok indenunder til brun sovs.
tip: Rist de hakkede nødder 8 minutter i ovnen først — rå nødder smager fladt i en ellers lang bagning.
=====
title: Hamburgerryg
slug: hamburgerryg
category: gryde
description: Hamburgerryg — kogt, glaseret hamburgerryg til julefrokost. Mør, skærbar og klassisk med sølvkål eller grønlangkål.
prepTime: PT15M
cookTime: PT1H30M
totalTime: PT1H50M
servings: 8
difficulty: nem
tags:
  - hamburgerryg
  - jul
  - svinekød
  - festmad
  - gryde
  - frokost
imageAlt: Glaseret hamburgerryg skåret i skiver
featured: true
ingredients:
  - 1 hamburgerryg (ca. 1,2–1,5 kg), røget eller urøget
  - 1 løg, kvart
  - 2 laurbærblade
  - 8 hele peberkorn
  - Glasur: 3 spsk ribsgele eller appelsinmarmelade, 1 spsk dijonsennep, 1 spsk brun farin
steps:
  - Læg hamburgerrygen i en gryde. Dæk med koldt vand. Tilsæt løg, laurbær og peber. Kog op, skum af, og simre lavt 60–75 minutter (ca. 30 min pr. 500 g).
  - Tag op, og dup tør. Læg i et ildfast fad. Bland glasuren, og pensl tykt på.
  - Gratinér i ovn ved 220 °C i 10–15 minutter, til glasuren bobler og karamelliserer. Pensl evt. midtvejs.
  - Hvil 10 minutter. Skær i tynde skiver. Server lun eller kold til julefrokost.
faq:
  - question: Røget eller urøget?
    answer: Begge virker. Røget er mere klassisk til frokostbord. Urøget er mildere til dem, der synes røg er skarpt.
  - question: Kernetemperatur?
    answer: Den er saltet/røget og skal primært varmes igennem. Sigte efter ca. 65–70 °C i midten — ikke tørre den ud.
  - question: Samme som glaseret skinke?
    answer: I familien. Se også [glaseret skinke med grønlangkål](/opskrifter/ovn/glaseret-skinke-groenlangkaal). Hamburgerryg er ofte mindre og til frokost.
  - question: Dagen før?
    answer: Kog dagen før, køl i lagen. Glasér og gratiner lige før servering, eller server kold uden glasur.
body: |
  Hamburgerryg er julefrokostens skærebord — kogt mør, glaseret blank.

  Simre lavt. Ikke rulle-kog. Glasuren er sød sennep og gele, ikke et centimeter-lag.

  Skær tyndt. Server med sennep, [sølvkål](/opskrifter/gryde/soelvkaal) eller rugbrød.
tip: Gem lidt af kogevæsken — den er god base til en hurtig sennepssauce eller til at varme skiver i.
=====
title: Ribbensteg i ovn
slug: ribbensteg-ovn
category: ovn
description: Ribbensteg i ovn — svinekam med sprød svær bagt lavt og færdig ved høj varme. Juleklassiker uden grill og airfryer.
prepTime: PT20M
cookTime: PT2H
totalTime: PT14H20M
servings: 6
difficulty: mellem
tags:
  - ribbensteg
  - flæskesteg
  - sprød svær
  - jul
  - ovn
  - festmad
  - svinekød
imageAlt: Ribbensteg i ovn med sprød svær og skysauce
featured: true
ingredients:
  - 1,5–2 kg ribbensteg / kamsteg med svær
  - 2–3 tsk groft salt
  - 1 tsk peber
  - 2 dl vand eller bouillon i bradepanden
  - 1 løg, kvart
  - 2 laurbærblade
steps:
  - Rid sværen i fine riller ned til kødet — ikke gennem. Gnid salt dybt i rillerne og på kødet. Peber på kødsiden. Stil frit overnight i køleskab, svær opad, hvis du kan.
  - Tag stegen frem 30 minutter før. Læg i bradepande med vand, løg og laurbær. Svær opad, så jævn som muligt.
  - Bag ved 160 °C varmluft ca. 1 time 15 min–1 time 45 min, til kernetemperatur 62–65 °C. Tjek at sværen tørrer.
  - Skru op til 220–230 °C, og bag 10–20 minutter mere, til sværen bobler og er knasende. Hold øje.
  - Hvil 15 minutter. Skær langs rillerne. Brug sky til [brun sovs](/opskrifter/pande/brun-sovs).
faq:
  - question: Sværen bliver sej?
    answer: For våd, for lidt salt i rillerne, eller for lav slutvarme. Dup tør før ovn, og giv den hedt finish. Se også airfryer-versionen: [ribbensteg i airfryer](/opskrifter/airfryer/ribbensteg).
  - question: Ribbensteg vs flæskesteg?
    answer: Samme familie — kam med svær. Ribbensteg har ofte ribbenene i; flæskesteg kan være uden. Teknikken til svær er den samme.
  - question: Uden overnight?
    answer: Salt mindst 1 time før. Overnight giver tørrere svær og dybere smag.
  - question: Kernetemperatur?
    answer: Træk ved 62–65 °C før finish. Over 70 °C midt i bliver kødet tørt, mens du venter på sværen.
body: |
  Ribbensteg i ovn er juleaftens kam med svær — lav varme til kødet, hedt finish til knas.

  Rid. Salt. Tør. Termometer.

  Sværen er ikke held. Den er tørhed, salt og høj varme til sidst.
tip: Læg en bold folie under den tynde ende, hvis stegen skråner — sværen skal ligge vandret for at boble jævnt.
=====
title: Julepostej
slug: julepostej
category: ovn
description: Julepostej — kraftig leverpostej med bacon, ansjos og krydderier til julefrokosten. Bages i form og serveres kold på rugbrød.
prepTime: PT25M
cookTime: PT1H15M
totalTime: PT1H50M
servings: 10
difficulty: mellem
tags:
  - julepostej
  - leverpostej
  - jul
  - pålæg
  - ovn
  - frokost
  - festmad
imageAlt: Julepostej i form med baconlag ovenpå
featured: true
ingredients:
  - 500 g griselever
  - 300 g spæk eller fedt flæsk
  - 200 g bacon i skiver (til form og top)
  - 1 stort løg
  - 2 æg
  - 2 dl mælk
  - 2 spsk hvedemel
  - 4 ansjosfileter (eller 1 spsk ansjospasta)
  - 1 tsk salt
  - 1 tsk peber
  - ½ tsk stødt allehånde
  - ½ tsk timian
  - Smør til formen
steps:
  - Hak lever, spæk og løg — eller kør i foodprocessor til en grov puree. Tilsæt æg, mælk, mel, ansjos, salt, peber, allehånde og timian. Blend til en jævn farce.
  - Smør en postejform eller brødform. Beklæd med baconskiver. Hæld farcen i. Læg bacon over toppen.
  - Sæt formen i et vandbad (bradepande med kogende vand midt op ad formen).
  - Bag ved 160 °C traditionel varme 70–80 minutter, til midten er fast (ca. 75 °C).
  - Køl helt — gerne overnight. Skær i skiver, og server på rugbrød med rødbeder og agurk.
faq:
  - question: Forskel på almindelig leverpostej?
    answer: Julepostej er kraftigere — mere krydderi, ansjos og ofte bacon rundt om. Se også [klassisk leverpostej](/opskrifter/palaeg/leverpostej).
  - question: Uden vandbad?
    answer: Den tørrer lettere og kan skille. Vandbad holder temperaturen mild og postejen saftig.
  - question: Kan den fryses?
    answer: Ja, i skiver eller hele formen. Tø i køleskab overnight.
  - question: For bitter?
    answer: Leveren var ikke frisk nok, eller du fik galdegange med. Skær leveren ren, og brug frisk råvare.
body: |
  Julepostej er leverpostej med festtøj — bacon, ansjos og krydderier til frokostbordet.

  Fin farce. Vandbad. Kold udskæring.

  Den skal være kraftig nok til sennep og rødbeder, ikke mild som hverdagspålæg.
tip: Blend farcen længe nok til den er ensartet — kornede bidder af spæk føles fedtede på rugbrødet.
=====
title: Æblesnaps
slug: aeblesnaps
category: sylte
description: Æblesnaps — hjemmelavet snaps på æbler, kanel og vanilje. Sæt den i november, nyd den til julefrokosten.
prepTime: PT20M
cookTime: PT0M
totalTime: PT336H
servings: 20
difficulty: nem
tags:
  - æblesnaps
  - snaps
  - jul
  - drikke
  - sylte
  - festmad
imageAlt: Flaske æblesnaps med æbleskiver og kanel
featured: true
ingredients:
  - 4–5 sure æbler (fx Ingrid Marie eller Granny Smith)
  - 1 vaniljestang, flækket
  - 1 kanelstang
  - 3–4 hele nelliker
  - 70 cl klar snaps eller vodka (32–40 %)
  - Evt. 1–2 spsk sukker efter smag
steps:
  - Vask æblerne, og skær i både — behold skrællen, fjern kernehuset.
  - Læg æbler, vanilje, kanel og nelliker i et rent glas med tæt låg. Fyld snaps over, så alt er dækket.
  - Stil mørkt ved stuetemperatur 1–2 uger. Ryst forsigtigt hver anden dag.
  - Smag til. Si frugt og krydderier fra. Evt. sød let med sukker, og ryst til det er opløst.
  - Flask på rene flasker. Gem køligt. Bedst efter yderligere en uges hvile.
faq:
  - question: Hvor længe skal den trække?
    answer: Mindst 1 uge, gerne 2. Længere end 3 uger kan gøre den bitter fra kerner/skal — si i tide.
  - question: Klar eller brændevin?
    answer: Klar snaps eller vodka giver ren æblesmag. Brændevin er kraftigere og mere rustik.
  - question: Kan jeg bruge restæbler?
    answer: Gerne — men undgå rådne. Overmodne æbler gør snapsen flad og sød.
  - question: Til julefrokost?
    answer: Ja — lille glas ved sild og leverpostej. Eller som base i en æble-gløgg uden for meget sødme.
body: |
  Æblesnaps er november-arbejde til december-bordet — æbler, kanel, vanilje og klar snaps.

  Ingen kogning. Bare tid, ryst og si.

  Den skal smage af æble og krydderi, ikke af billig sodavand. Hold sukkeret i ave.
tip: Brug et patentglas, og fyld snaps til randen — mindre luft betyder mindre oxidation og klarere smag.
'''


def parse_block(text: str) -> dict:
    data: dict = {}
    mode = None
    body_lines: list[str] = []
    current_q = None
    lines = text.strip().split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("title: "):
            data["title"] = line[7:]
            mode = None
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
        print("skip empty", d.get("slug"))
        continue
    assert d.get("faq") and len(d["faq"]) >= 3, (d.get("slug"), len(d.get("faq", [])))
    assert d.get("tip"), d.get("slug")
    assert "jul" in d["tags"], d.get("slug")
    out = ROOT / d["category"]
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{d['slug']}.mdx"
    if path.exists():
        raise SystemExit(f"slug collision: {path}")
    path.write_text(to_mdx(d), encoding="utf-8")
    written.append((d["category"], d["slug"]))
    print("wrote", d["category"] + "/" + path.name)

print(f"done: {len(written)} recipes")
for cat, slug in written:
    print(f"  {cat}/{slug}")
