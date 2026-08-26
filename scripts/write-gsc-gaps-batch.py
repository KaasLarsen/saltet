#!/usr/bin/env python3
"""GSC content-gap batch — queries uden dedikeret side (aug 2026 export)."""
from pathlib import Path

ROOT = Path("/Users/dklarsen/Desktop/saltet/content/recipes")

RECIPES = r'''
=====
title: Letsaltet flæsk — hjemmelavet saltet flæsk
slug: letsaltet-flaesk
category: palaeg
description: Letsaltet flæsk / saltet flæsk opskrift — tørsaltning af svinebryst til stegt flæsk, æggekage og rugbrød.
prepTime: PT20M
cookTime: PT0M
totalTime: PT72H20M
servings: 8
difficulty: mellem
tags:
  - letsaltet flæsk
  - saltet flæsk
  - saltet flæsk opskrift
  - svinebryst
  - pålæg
  - saltning
imageAlt: Skiver af hjemmelavet letsaltet flæsk på skærebræt
featured: true
ingredients:
  - 1,5 kg svinebryst med svær (eller uden, hvis du vil stege som bacon)
  - 80 g groft salt (ca. 5 % af kødvægten)
  - 2 spsk sukker
  - 1 tsk sort peber, knust
  - 2 laurbærblade, smuldret
  - 1 tsk eneær (valgfrit)
  - 2 fed hvidløg, knust (valgfrit)
steps:
  - Dup kødet tørt. Bland salt, sukker, peber, laurbær, eneær og hvidløg.
  - Gnid blandingen ind i alle sider — også ind i sværen, hvis den er på. Læg i en skål eller pose.
  - Køl 48–72 timer. Vend én gang om dagen. Væske trækker ud — det er meningen.
  - Skyl overfladen let under koldt vand. Dup knastørt. Lufttør på rist i køleskab 12–24 timer uden tætsluttende låg.
  - Skær i skiver. Steg som stegt flæsk, brug i æggekage, eller kog kort til saltmad.
faq:
  - question: Forskel på letsaltet og saltet flæsk?
    answer: Samme idé. Letsaltet er mildere og kortere saltet (2–3 dage). Længere tid = mere saltet, mere holdbart.
  - question: Kan jeg bruge saltpeberblanding fra posen?
    answer: Nej til den her. Du skal styre saltprocenten, ellers bliver det spisebord-salt.
  - question: Holdbarhed?
    answer: Lufttørret i køleskab ca. en uge. Frys skiver med bagepapir imellem.
  - question: Til hvad?
    answer: Stegt flæsk med persillesovs, carbonara-agtig pasta, rugbrød med æg, eller tern i kål.
body: |
  Letsaltet flæsk er Saltets grundstof: salt, tid, svinebryst.

  Fem procent salt. To–tre døgn. Skyl, tør, skær. Resten er stegning.

  Du køber det i butikken. Du laver det bedre selv, fordi du styrer saltet.
tip: Vej kødet. Gæt ikke på saltet. 5 % er letsaltet; 7–8 % er hårdere og mere «gammeldags saltet flæsk».
=====
title: Tebirkes i airfryer
slug: tebirkes-airfryer
category: airfryer
description: Tebirkes i airfryer — frosne eller køleskabs-tebirkes med sprød skorpe og blød midte på under 12 minutter.
prepTime: PT2M
cookTime: PT10M
totalTime: PT12M
servings: 2
difficulty: nem
tags:
  - tebirkes
  - tebirkes i airfryer
  - airfryer
  - morgenmad
  - bake-off
  - wienerbrød
imageAlt: Gyldne tebirkes fra airfryeren med birkes på toppen
featured: true
ingredients:
  - 2–4 tebirkes (frosne bake-off eller køleskab)
  - Valgfrit: 1 æggeblomme + 1 tsk vand til pensling
  - Ekstra birkes eller sesam (valgfrit)
steps:
  - Læg tebirkes direkte i kurven med plads imellem. Frosne behøver ikke optøning.
  - Airfry 160 °C i 8–10 minutter for frosne; 6–8 minutter for køleskabs-tebirkes. Vend ikke — skorpen sætter sig bedst i ro.
  - Vil du have ekstra glans: pensl med æg efter 5 minutter, drys birkes, kør 2–3 minutter mere.
  - Køl 1 minut på rist. Midten skal være lun, ikke gummiagtig.
faq:
  - question: Hvilken temperatur?
    answer: 160 °C. Højere brænder birkesene før midten er færdig.
  - question: Samme tid som wienerbrød?
    answer: Tebirkes er tættere. Giv dem ofte 1–2 minutter mere end et let croissantdeig-stykke.
  - question: Kan de varmes dagen efter?
    answer: 150 °C i 2–3 minutter. De bliver aldrig helt som friske — spis dem varme fra første gang.
  - question: Overfyldt kurv?
    answer: Nej. De hæver og skal have luft. To hold slår ét proppet.
body: |
  Tebirkes i airfryer er morgenmad uden ovn-opvarmning.

  Lav varme. Plads i kurven. Birkesene skal dufte nøddeagtigt, ikke brændt.

  Det er ikke bagværk fra bunden — det er finish på noget, der allerede er næsten færdigt.
tip: Hvis undersiden er bleg, vend dem de sidste 90 sekunder. Ellers lad dem være — toppen er det, du spiser med øjnene.
=====
title: Skinkeculotte i airfryer
slug: skinkeculotte-airfryer
category: airfryer
description: Skinkeculotte i airfryer — saftig svinekød med sprød fedtkappe, kernetemperatur og søndagsmad uden ovn.
prepTime: PT15M
cookTime: PT45M
totalTime: PT1H10M
servings: 6
difficulty: mellem
tags:
  - skinkeculotte
  - skinkeculotte i airfryer
  - airfryer
  - svinekød
  - søndagsmad
  - culotte
imageAlt: Skinkeculotte fra airfryeren skåret i skiver med sprød fedtkappe
featured: true
ingredients:
  - 1–1,2 kg skinkeculotte med fedtkappe
  - 2 tsk salt
  - 1 tsk peber
  - 1 tsk paprika
  - 1 tsk hvidløgspulver
  - 1 spsk olivenolie
  - Valgfrit: frisk rosmarin
steps:
  - Tag kødet ud 30 minutter før. Score fedtkappen i ruder uden at skære i kødet.
  - Gnid med olie, salt, peber, paprika og hvidløgspulver. Rosmarin under snor eller løst ovenpå.
  - Forvarm airfryeren til 180 °C. Læg culotten med fedtsiden op.
  - Steg 35–50 minutter afhængig af tykkelse. Tjek kernetemperatur: træk ved 62–64 °C for saftig, 66–68 °C for mere gennemstegt.
  - Vend fedtsiden ned de sidste 5 minutter, hvis du vil have ekstra knas — ellers lad den være oppe hele vejen.
  - Hvile 10 minutter under løst folie. Skær i skiver på tværs af fibrene.
faq:
  - question: Hvilken kernetemperatur?
    answer: Saftig classic: træk 62–64 °C, slut ca. 65–67 °C efter hvile. Magert svin tåler ikke okse-temperaturer.
  - question: For stor til kurven?
    answer: Bind den strammere, eller skær i to stege. Overfyldt kurv giver damp, ikke skorpe.
  - question: Sous vide i stedet?
    answer: Ja — se skinkeculotte sous vide. Airfryer er finish + hele stegen i ét hug.
  - question: Restemad?
    answer: Tynde skiver på rugbrød, i wraps, eller tern i pastasauce.
body: |
  Skinkeculotte i airfryer er søndagssteg uden at tænde ovnen.

  Score fedtet. Salt. Termometer. Hvile.

  Fedtkappen skal knase. Kødet skal være rosa-beige, ikke gråt og tørt.
tip: Stik termometret midt i den tykkeste del, væk fra fedt. Fedt lyver varmt.
=====
title: Svinekæber i airfryer
slug: svinekaeber-airfryer
category: airfryer
description: Grisekæber / svinekæber i airfryer — møre kæber med stegeskorpe, klar til kartoffelmos eller bløde tortillas.
prepTime: PT15M
cookTime: PT55M
totalTime: PT1H25M
servings: 4
difficulty: mellem
tags:
  - svinekæber
  - grisekæber
  - grisekæber i airfryer
  - airfryer
  - pulled
  - billigt kød
imageAlt: Møre svinekæber fra airfryeren med stegeskorpe
featured: true
ingredients:
  - 800 g–1 kg svinekæber, putset for hinder
  - 2 tsk salt
  - 1 tsk peber
  - 1 tsk røget paprika
  - 1 tsk spidskommen
  - 1 spsk olivenolie
  - 1 dl fond eller vand i bunden af en ildfast form der passer i airfryeren (valgfrit)
steps:
  - Dup kæberne tørre. Vend med olie, salt, peber, paprika og spidskommen.
  - Forvarm til 160 °C. Læg kæberne i ét lag — gerne i en lav form, hvis din model tillader det.
  - Steg 40 minutter. Vend. 10–15 minutter mere, til de er møre nok til at trække fra hinanden med to gafler.
  - Vil du have mere skorpe: 3–4 minutter ved 190 °C til sidst.
  - Hvile 5 minutter. Træk i strimler eller server hele. Skyl formens saft over som jus.
faq:
  - question: Er de færdige, når de er brune?
    answer: Nej. De skal være møre. Brun er skorpe; mørt er collagen der er smeltet. Test med gaffel.
  - question: Grill eller trykkoger i stedet?
    answer: Begge findes på Saltet. Airfryer er midtvejs: mindre røg end grill, mindre væske end trykkoger.
  - question: Tørre kæber?
    answer: For høj varme for tidligt. Hold 160 °C, og giv dem tid. En skvæt fond i formen redder kanten.
  - question: Til hvad?
    answer: Kartoffelmos, bløde tacos, pasta med saft, eller koldt i salat dagen efter.
body: |
  Grisekæber i airfryer er billigt kød, der opfører sig dyrt, når collagen smelter.

  Lav varme. Tid. Vend én gang.

  Du jagter ikke stegt flæsk-knas hele vejen — du jagter mørt kød med en stegt overflade.
tip: Putse hinderne før krydderi. Hinder bliver til gummibånd, uanset hvor længe du steger.
=====
title: Gris tomahawk på grill
slug: gris-tomahawk
category: grill
description: Gris tomahawk / tomahawk steak gris — tyk kotelet på langt ben med skorpe, kernetemperatur og hvile.
prepTime: PT15M
cookTime: PT30M
totalTime: PT1H15M
servings: 2
difficulty: mellem
tags:
  - gris tomahawk
  - tomahawk gris
  - tomahawk steak gris
  - kotelet
  - grill
  - kernetemperatur
  - svinekød
imageAlt: Gris tomahawk på grill med grillstriber og langt ben
featured: true
ingredients:
  - 1 gris-tomahawk / skaftkotelet (ca. 800 g–1,2 kg, 3–4 cm tyk)
  - 1 spsk olivenolie
  - 2 tsk groft salt
  - Friskkværnet peber
  - 1 tsk fennikelfrø, knust (valgfrit)
  - 30 g smør, 2 fed hvidløg, timian til finish (valgfrit)
steps:
  - Tag kødet ud 45 minutter før. Dup tørt. Olie, salt, peber og fennikel på alle sider.
  - To zoner på grillen: hård direkte varme og indirekte medium.
  - Svid 2–3 minutter pr. side over direkte varme. Vend også fedtkanten.
  - Flyt til indirekte. Låg på. Grill til kerne 58–60 °C for saftig rosa (typisk 12–20 minutter). Vend én gang.
  - Tag af. Smør, hvidløg og timian ovenpå hvis du vil. Hvile 8–10 minutter under løst folie.
  - Skær kødet fra benet, skær i skiver på tværs af fibrene. Flagesalt.
faq:
  - question: Er det samme som okse-tomahawk?
    answer: Samme look — langt ribben — men det er svin. Mad sikkerhed og temperatur er anderledes. Træk ikke ved 52 °C som okse.
  - question: Hvilken kernetemperatur?
    answer: Saftig: træk 58–60 °C, slut ca. 62–63 °C efter hvile. Gennemstegt classic: træk 65 °C.
  - question: Gasgrill uden termometer?
    answer: Nej. Tykkelsen lyver. Termometer er ikke til pynt her.
  - question: Ovnen i stedet?
    answer: Svid på pande, finish ved 180 °C til samme kernetemperatur. Grill giver røg; metoden er den samme.
body: |
  Gris tomahawk er teater-kotelet: langt ben, tykt kød, kort tålmodighed hvis du gætter på tid.

  Svid. Indirekte. Termometer. Hvile.

  Fennikel og svinekød er venner. Salt er loven.
tip: Bind en folie om ben-spidsen, hvis den sidder tæt på direkte varme — den brænder før kødet er færdigt.
=====
title: Griseskank i airfryer
slug: griseskank-airfryer
category: airfryer
description: Skank af gris i airfryer — mør skank med stegt overflade, klar til rodfrugter eller bløde boller.
prepTime: PT15M
cookTime: PT1H10M
totalTime: PT1H40M
servings: 3
difficulty: mellem
tags:
  - griseskank
  - skank af gris
  - skank af gris airfryer
  - airfryer
  - svinekød
  - søndagsmad
imageAlt: Mør griseskank fra airfryeren med stegt skorpe
featured: true
ingredients:
  - 2–3 griseskanke (ca. 1–1,2 kg i alt)
  - 2 tsk salt
  - 1 tsk peber
  - 1 tsk paprika
  - 1 tsk tørret timian
  - 1 spsk olie
  - 1 dl æblejuice eller fond i en lav form (valgfrit)
steps:
  - Dup skankene tørre. Vend med olie og krydderier.
  - Forvarm til 160 °C. Læg skankene i kurven eller i en form der passer.
  - Steg 50 minutter. Vend. 15–25 minutter mere, til kødet næsten slipper benet.
  - Sidste 5 minutter ved 190 °C for ekstra skorpe, hvis overfladen er bleg.
  - Hvile 8 minutter. Træk kødet fra benet eller server hele med saften fra formen.
faq:
  - question: Skal skanken være gennemstegt?
    answer: Den skal være mør. Collagen skal smelte. Farve alene er ikke nok — gaffeltesten er.
  - question: For tør?
    answer: For høj varme. Hold 160 °C, og brug en skvæt væske i formen.
  - question: Trykkoger i stedet?
    answer: Hurtigere til mørt. Airfryer giver mere stegeskorpe på ydersiden.
  - question: Tilbehør?
    answer: Rodfrugter, kartoffelmos, sennep, eller bløde boller med syltede løg.
body: |
  Skank af gris i airfryer er vintermad i en kurv.

  Lav varme. Vend. Vent til benet giver slip.

  Det er ikke en kotelet. Det er collagen-arbejde.
tip: Bed slagteren om at save skankene i ens størrelse, så de bliver færdige samtidig.
=====
title: Baconsvøbte svesker
slug: baconsvoebte-svesker
category: airfryer
description: Svesker med bacon — baconsvøbte svesker i airfryer. Sød, salt tapas på under 15 minutter.
prepTime: PT10M
cookTime: PT10M
totalTime: PT20M
servings: 4
difficulty: nem
tags:
  - svesker med bacon
  - baconsvøbte svesker
  - svesker
  - bacon
  - tapas
  - airfryer
  - festmad
imageAlt: Baconsvøbte svesker på tallerken med peber
featured: true
ingredients:
  - 12 bløde svesker, udstenet
  - 6 skiver bacon, delt på langs eller tværs
  - Valgfrit: 40 g mandler eller blåskimmel til fyld
  - Friskkværnet peber
  - Tandstikkere
steps:
  - Fyld hver sveske med en mandel eller en lille klats ost, hvis du vil. Ellers lad dem være hule.
  - Sno bacon stramt rundt. Fastgør med tandstikker. Peber let.
  - Forvarm airfryeren til 190 °C.
  - Steg 8–10 minutter. Vend halvvejs, til baconen er sprød og sveskerne er varme.
  - Fjern tandstikkere. Hvile 1 minut. Server som tapas.
faq:
  - question: Forskel på dadler og svesker?
    answer: Dadler er sødere og blødere. Svesker er dybere, mere karamel-mørke. Samme metode.
  - question: Tørre svesker?
    answer: Udblød 10 minutter i lunkent vand. Dup tørre før bacon.
  - question: Ovnen i stedet?
    answer: 200 °C i 12–15 minutter på rist over bradepande. Airfryer er hurtigere til sprød bacon.
  - question: Kan de laves forud?
    answer: Svøb dem, køl, steg lige før gæsterne. Færdige holder sig varme ca. 10 minutter.
body: |
  Svesker med bacon er den gamle festsnack: sød frugt, salt fedt, sprød finish.

  Stramt bacon. Høj varme. Kort tid.

  Fyld er valgfrit. Bacon og sveske kan stå alene.
tip: Brug koldt bacon lige fra køleskabet — det er nemmere at sno uden at rive.
=====
title: Fyldte koteletter i airfryer
slug: fyldte-koteletter-airfryer
category: airfryer
description: Fyldte koteletter i airfryer — svinekoteletter med ost og urter, sprød yderside og saftig midte.
prepTime: PT20M
cookTime: PT18M
totalTime: PT40M
servings: 4
difficulty: mellem
tags:
  - fyldte koteletter
  - fyldte koteletter i airfryer
  - koteletter
  - airfryer
  - ost
  - svinekød
imageAlt: Fyldte svinekoteletter fra airfryeren skåret så fyldet ses
featured: true
ingredients:
  - 4 tykke svinekoteletter (ca. 2,5–3 cm, uden ben)
  - 80 g flødeost eller mozzarella
  - 2 spsk hakket persille eller spinat
  - 1 fed hvidløg, presset
  - 1 spsk olivenolie
  - 1 tsk salt, peber, paprika
  - Tandstikkere eller kødnål
steps:
  - Skær en lomme ind i siden af hver kotelet uden at skære igennem.
  - Rør ost, persille og hvidløg. Fyld lommerne. Luk med tandstikkere.
  - Pensl med olie. Krydr ydersiden med salt, peber og paprika.
  - Forvarm til 180 °C. Steg 9 minutter. Vend. 7–9 minutter mere, til kerne 65–68 °C.
  - Hvile 5 minutter. Fjern tandstikkere før servering.
faq:
  - question: Fyldet løber ud?
    answer: For meget fyld, eller for åben lomme. Pres kanten sammen, og brug tandstikkere.
  - question: Med grøntsager i fyldet?
    answer: Ja — finthakket spinat eller peberfrugt, men hold det tørt. Vådt fyld koger kødet indefra.
  - question: Almindelige koteletter uden fyld?
    answer: Se koteletter i airfryer — kortere tid og enklere.
  - question: Koteletter i fad?
    answer: Du kan lægge dem i en lav form med lidt fløde og grønt omkring — så er det mere gryderet end stegt skorpe.
body: |
  Fyldte koteletter i airfryer er hverdagsfest: lomme, ost, skorpe.

  Tykkelse betyder noget. Tynde koteletter bliver tørre, før osten er varm.

  Termometer vinder over uret.
tip: Bank koteletterne let ens i tykkelse før du skærer lommen — så bliver de færdige samtidig.
=====
title: Hakkebøf med bacon i airfryer
slug: hakkeboef-bacon-airfryer
category: airfryer
description: Hakkebøf med bacon i airfryer — saftige bøffer med baconsvær, klar på ca. 15 minutter.
prepTime: PT15M
cookTime: PT14M
totalTime: PT30M
servings: 4
difficulty: nem
tags:
  - hakkebøf
  - hakkebøf med bacon
  - hakkebøf med bacon i airfryer
  - bacon
  - airfryer
  - hverdag
imageAlt: Hakkebøffer med bacon fra airfryeren på tallerken
featured: true
ingredients:
  - 500 g hakket oksekød (12–15 %)
  - 4 skiver bacon
  - 1 lille løg, finthakket
  - 1 æg
  - 2 spsk rasp
  - 1 tsk salt, peber
  - 1 tsk dijonsennep
steps:
  - Hak bacon fint, eller skær i små stykker. Bland med kød, løg, æg, rasp, salt, peber og sennep. Arbejd kort — ikke brøddej.
  - Form 4 bøffer, ca. 2 cm tykke. Lav en lille fordybning i midten, så de ikke hvælver.
  - Forvarm til 190 °C. Læg bøfferne i kurven med plads.
  - Steg 7 minutter. Vend. 5–7 minutter mere, til de er gennemstegte midt i (eller lyserøde, hvis du vil have dem mere rosa — brug termometer, ca. 70 °C for through).
  - Hvile 3 minutter. Server med sovs, kartofler eller salat.
faq:
  - question: Bacon ovenpå i stedet for i farsen?
    answer: Ja. Form bøffen, læg en bacon-skive ovenpå, og steg. Den bliver sprødere end bacon i farsen.
  - question: Tørre bøffer?
    answer: For magert kød, eller for lang tid. 12–15 % fedt. Træk i tide.
  - question: Kan de fryses?
    answer: Form rå, frys med papir imellem, steg fra frossen +3–4 minutter.
  - question: Tilbehør?
    answer: Brun sovs, bløde løg, kartofler — eller airfryer-pomfritter.
body: |
  Hakkebøf med bacon i airfryer er hverdag uden panden.

  Kort æltning. Plads i kurven. Vend én gang.

  Baconen salter for dig — smag farsen før du tilsætter ekstra salt, hvis baconen er meget salt.
tip: Koldt kød former nemmere. Tag det først ud af køleskabet, når løg og bacon er klar.
=====
title: Chorizo-tapas på plancha
slug: chorizo-tapas
category: plancha
description: Spansk pølse tapas — chorizo på plancha med olivenolie, sherryeddike og brød. Klar på 15 minutter.
prepTime: PT5M
cookTime: PT10M
totalTime: PT15M
servings: 4
difficulty: nem
tags:
  - spansk pølse
  - spansk pølse tapas
  - chorizo
  - tapas
  - plancha
  - grill
imageAlt: Stegt chorizo i skiver på plancha med brød ved siden af
featured: true
ingredients:
  - 300–400 g spansk chorizo (kureret, til stegning — ikke den bløde pålægsagtige alene)
  - 1 spsk olivenolie
  - 1 spsk sherryeddike eller rødvinseddike
  - Friskkværnet peber
  - Brød til at suge fedtet
  - Valgfrit: oliven, mandler, citron
steps:
  - Skær chorizo i skrå skiver på 1 cm, eller flæk hele pølser på langs.
  - Varm plancha eller pande til medium-høj. Olie på.
  - Steg chorizo 2–3 minutter pr. side, til kanterne bobler og skindet er mørkt.
  - Sluk for varmen. Sprøjt eddike over. Peber. Lad det syde 20 sekunder i fedtet.
  - Server direkte fra pladen med brød. Oliven og mandler ved siden af.
faq:
  - question: Hvilken chorizo?
    answer: En til stegning (ofte mærket «sarta» eller «para freír»). Ren spegepølse-chorizo bliver hård og tør.
  - question: Grill i stedet for plancha?
    answer: Ja. Kurv eller plancha-plade, så fedtet ikke slukker gløderne.
  - question: For stærk?
    answer: Vælg mild chorizo, eller bland med søde peberfrugtstrimler på pladen.
  - question: Drikkevarer?
    answer: Tør sherry, kold øl, eller noget med syre. Fedtet vil have modsvar.
body: |
  Spansk pølse tapas er næsten ingen opskrift: varme, fedt, syre, brød.

  Chorizoen steger i sit eget paprika-fedt. Eddiken skærer.

  Det er ikke en hovedret. Det er det, folk står rundt om.
tip: Gem 1 spsk af det røde fedt. Pensl det på brødet, før du rister det — det er gratis smag.
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
publishedAt: 2026-08-26
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
    assert d.get("faq") and len(d["faq"]) >= 3, d.get("slug")
    assert d.get("tip")
    out = ROOT / d["category"]
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{d['slug']}.mdx"
    if path.exists():
        raise SystemExit(f"slug collision: {path}")
    path.write_text(to_mdx(d), encoding="utf-8")
    print("wrote", d["category"] + "/" + path.name)
