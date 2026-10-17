#!/usr/bin/env python3
"""Oksespidsbryst-batch — 13 manglende brisket-opskrifter (okt 2026)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"
PUBLISHED = "2026-10-17"

RECIPES = r'''
=====
title: Kaffegnidmet brisket over åben ild
slug: kaffegnidmet-brisket-aaben-ild
category: baalmad
description: Kaffegnidmet brisket over åben ild — oksespidsbryst med espresso-rub, grillet indirekte til mør bark og saftig kerne.
prepTime: PT25M
cookTime: PT6H
totalTime: PT8H
servings: 8
difficulty: svær
tags:
  - brisket
  - oksespidsbryst
  - oksekød
  - BBQ
  - kaffe
  - bål
  - åben ild
imageAlt: Kaffegnidmet brisket skåret i skiver over åben ild med mørk bark
featured: false
ingredients:
  - 2–2,5 kg oksespidsbryst (brisket flat eller point)
  - Rub: 3 spsk groftsalt, 2 spsk grov peber, 2 spsk mørkristet espresso (finmalet), 2 spsk råsukker, 1 spsk paprika, 1 tsk hvidløgspulver, 1 tsk chiliflager
  - 1 spsk gul sennep som binder
  - Lidt oksefond eller vand til wrap
steps:
  - Putse kødet: jævn fedtkappe ca. 5 mm. Smør med sennep. Gnid rubben hårdt ind. Køleskab 1–2 timer (eller natten over).
  - Byg to zoner over bål eller grill: gløder til den ene side, tom plads til indirekte varme. Mål 110–130 °C i den kølige zone.
  - Læg brisketten fedtside op i den indirekte zone. Låg eller tælt på, hvis du har. Vend ikke hvert kvarter — lad barken sætte sig 3–4 timer.
  - Når barken er mørk og kernen ca. 70–75 °C: wrap i butcher paper med lidt fond. Fortsæt til 93–96 °C og probe tender.
  - Hvile indpakket 45–90 minutter. Skær på tværs af fibrene.
faq:
  - question: Espresso eller instant?
    answer: Finmalet mørkristet espresso. Instant bliver bitter og klistrer. Kaffen er farve og dybde — ikke café latte.
  - question: Kan jeg bruge smoker i stedet?
    answer: Ja. Samme rub og temperatur. Se også [smoked beef brisket](/opskrifter/roeg/smoked-beef-brisket) til classic Texas.
  - question: Flat eller point?
    answer: Point er federe og mere tilgivende over åben ild. Flat kræver wrap og tålmodighed.
  - question: Hvor meget rub?
    answer: Generøst. Barken skal se næsten sort ud — det er kaffe + sukker, ikke brændt kød.
body: |
  Kaffegnidmet brisket over åben ild er BBQ med bål-attitude: mørk espresso, råsukker og indirekte varme, til kødet giver sig.

  Rubben er barken. Zonerne er redningen. Hvile er halvdelen.

  Skær tyndt. Sauce er valgfri.
tip: Hold flammerne væk fra kødet. Direkte ild brænder sukkeret i rubben, før kollagenet er smeltet.
=====
title: Pecan-røget brisket flat med senneps-bark
slug: pecan-roget-brisket-flat
category: roeg
description: Pecan-røget brisket flat med senneps-bark — mager flat smurt med gul sennep og tung peber-rub, røget med milde pecan-chunks.
prepTime: PT30M
cookTime: PT10H
totalTime: PT12H
servings: 8
difficulty: svær
tags:
  - brisket
  - oksespidsbryst
  - oksekød
  - BBQ
  - varmrøgning
  - pecan
imageAlt: Pecan-røget brisket flat skåret i skiver med mørk peberbark
featured: false
ingredients:
  - 2–3 kg brisket flat (rensket, jævn tykkelse)
  - 2–3 spsk gul sennep
  - Rub: 3 spsk groft salt, 4 spsk grov sort peber, 1 spsk hvid peber, 1 tsk hvidløgspulver
  - Pecan-chunks (eller pecan + lidt eg)
  - 1 dl oksefond til wrap
steps:
  - Putse flat: fjern sølvhinde, lad ca. 3–5 mm fedt. Smør hele stykket med gul sennep.
  - Rub tungt med salt og peber. Sennepen er binder — ikke smag i sig selv.
  - Røg ved 110–120 °C med pecan. Fedtside op. 5–7 timer til dyb bark og kerne ca. 70–75 °C.
  - Wrap i butcher paper med fond. Fortsæt til 93–95 °C og probe tender i den tykkeste del.
  - Hvile 1–2 timer. Skær blyanttykke skiver på tværs af fibrene.
faq:
  - question: Hvorfor sennep?
    answer: Binder rubben, så peberen sidder. Smagen forsvinder i røgen. Dijon er for fin — gul sennep er klassikeren.
  - question: Pecan eller hickory?
    answer: Pecan er mildere og nøddeagtig — godt til den magre flat. Hickory er hårdere; se chili-glace-versionen.
  - question: Flat tørrer?
    answer: Wrap tidligere end point, hvil længere, og skær tyndt. Hel packer er mere tilgivende — se [smoked beef brisket](/opskrifter/roeg/smoked-beef-brisket).
  - question: Butcher paper eller folie?
    answer: Paper bevarer bark. Folie damper mere og giver softer bark — brug hvis flat er meget mager.
body: |
  Pecan-røget flat er den magre disciplin: sennep, peberbjerg, mild nødderøg.

  Flat har mindre fedt end point. Derfor wrap, hvile og tynde skiver.

  Bark først. Mørhed bagefter.
tip: Køb flat med jævn tykkelse. En tynd ende brænder, før den tykke er mør — trim eller fold den tynde ende under.
=====
title: Hickory-røget spidsbryst med chili-glace
slug: hickory-roget-spidsbryst-chili-glace
category: roeg
description: Hickory-røget oksespidsbryst med chili-glace — lav-og-langsom røgning, afsluttet med klistret, reduceret chiliglace på grillen.
prepTime: PT30M
cookTime: PT11H
totalTime: PT13H
servings: 10
difficulty: svær
tags:
  - oksespidsbryst
  - brisket
  - oksekød
  - BBQ
  - varmrøgning
  - chili
  - hickory
imageAlt: Hickory-røget spidsbryst med blank chili-glace og mørk bark
featured: false
ingredients:
  - 3–4 kg oksespidsbryst (point eller packer)
  - Rub: 3 spsk salt, 3 spsk peber, 1 spsk paprika, 1 tsk chipotlepulver
  - Hickory-chunks
  - Chili-glace: 2 dl BBQ-sauce, 1 dl chili-sauce (fx sriracha eller sweet chili), 2 spsk brun farin, 1 spsk æblecidereddike, 1 tsk røget paprika
steps:
  - Putse og rub. Røg ved 110–120 °C med hickory, fedtside op, til bark og kerne ca. 70–75 °C (typisk 6–8 timer).
  - Wrap i paper. Fortsæt til 93–96 °C og probe tender.
  - Imens: kog glacen sammen 8–10 minutter, til den napper skeen.
  - Pak ud de sidste 25–30 minutter. Pensl glacen i 2–3 lag direkte på grillen/smokeren ved ca. 130 °C, til den klistrer.
  - Hvile 45–60 minutter. Skær og server med ekstra glace ved siden af.
faq:
  - question: Glace for tidligt?
    answer: Sukker brænder. Vent til kødet er mørt, så kun 25–30 minutter finish. Ellers får du bitter bark.
  - question: Hjemmelavet BBQ-sauce?
    answer: Ja — brug din favorit som base. Glacen skal reduceres, ikke bare pensles tynd.
  - question: Point eller flat?
    answer: Point tåler glacen bedst. Flat kan klare det, hvis du pensler let.
  - question: Uden wrap?
    answer: Muligt, men tager længere og tørrer lettere. Wrap er standard på Saltet — se [smoked beef brisket](/opskrifter/roeg/smoked-beef-brisket).
body: |
  Hickory og chili-glace er BBQ med finish: lang røg først, klistret glace til sidst.

  Glacen skal nappe. Vandig sauce er ingen ret.

  Pensl i lag. Lad hvert lag sætte sig.
tip: Hold 1/3 af glacen uberørt til bordet. Den der har været på grillen er bark — den rene er dip.
=====
title: Sprængt spidsbryst-pastrami på trækul
slug: spraengt-spidsbryst-pastrami
category: roeg
description: Hjemmelavet pastrami af oksespidsbryst — sprængt i krydderlage, dækket med knust koriander og peber, røget færdig på trækul.
prepTime: PT45M
cookTime: PT8H
totalTime: PT6D
servings: 10
difficulty: svær
tags:
  - pastrami
  - oksespidsbryst
  - brisket
  - oksekød
  - sprængt oksebryst
  - varmrøgning
  - BBQ
imageAlt: Tynde skiver hjemmelavet pastrami med peber-koriander-skorpe
featured: true
ingredients:
  - 2–2,5 kg oksespidsbryst
  - Lage: 3 l vand, 250 g salt, 100 g sukker, 1 spsk peberkorn, 1 spsk korianderfrø, 4 laurbær, 4 nelliker, 4 fed hvidløg — evt. 1 tsk saltpeter
  - Skorpe: 3 spsk knuste korianderfrø, 3 spsk grov sort peber, 1 spsk brunt sukker
  - Trækul + mild røg (bøg eller æble)
steps:
  - Kog lagen, køl helt. Læg kødet i 5 døgn i køleskab. Vend dagligt.
  - Tag op, skyl, tør. Lufthæng eller stil på rist i køleskab 12–24 timer til let pellicle.
  - Gnid skorpen hårdt ind — koriander og peber i tætte mængder.
  - Røg på trækul ved 110–120 °C til kerne ca. 70 °C og fast bark (typisk 5–7 timer). Evt. wrap sidste del til 90–93 °C, hvis stykket er tykt.
  - Køl helt. Skær iskoldt i papirtynde skiver på tværs — eller varm forsigtigt til sandwiches.
faq:
  - question: Pastrami eller sprængt oksebryst?
    answer: Samme saltlage-familie. Pastrami får koriander-peber-skorpe og røg. Klassisk [sprængt oksebryst](/opskrifter/palaeg/spraengt-oksebryst) koges til pålæg uden skorpe.
  - question: Sous vide i stedet for røg?
    answer: Se [pastrami-brisket sous vide](/opskrifter/sous-vide/pastrami-brisket-sous-vide) til 48-timers præcision. Denne er trækul og bark.
  - question: Saltpeter?
    answer: Valgfrit til pink farve. Vej det — gæt ikke. Uden får du gråere, men stadig god pastrami.
  - question: Skæres varm eller kold?
    answer: Kold til pålæg. Varm (dampet eller sous vide-genopvarmet) til Reuben-agtige sandwiches.
body: |
  Spidsbryst-pastrami er dobbelt disciplin: saltlage, så trækul og et bjerg af koriander.

  Pellicle før røg. Tynde skiver efter køl.

  Det er ikke delikatessebutik. Det er dit eget saltkød med attitude.
tip: Knus korianderfrøene groft i morter — pulver forsvinder, hele frø giver ingen skorpe.
=====
title: Pulled oksebryst sous vide
slug: pulled-oksebryst-sous-vide
category: sous-vide
description: Pulled oksebryst sous vide — brisket ved 74 °C i 24 timer, så kollagenet slipper og kødet trækkes med to gafler.
prepTime: PT20M
cookTime: PT24H
totalTime: PT25H
servings: 8
difficulty: svær
tags:
  - oksespidsbryst
  - brisket
  - oksekød
  - sous vide
  - BBQ
  - pulled beef
imageAlt: Pulled oksebryst sous vide trukket i saftige strenge med BBQ-sauce
featured: false
ingredients:
  - 2–2,5 kg oksespidsbryst
  - 2 spsk salt
  - 2 spsk BBQ-rub (paprika, brunt sukker, peber, hvidløg)
  - 1 spsk sennep som binder
  - 1–2 dl BBQ-sauce til finish
steps:
  - Gnid med sennep, salt og rub. Vakuumpak.
  - Sous vide ved 74 °C i 24 timer — kollagenet skal helt nedbrydes.
  - Tag ud, gem posevæsken. Tør kødet. Træk med to gafler (eller handsker).
  - Bland lidt posevæske og BBQ-sauce i. Finish 10–15 minutter ved 220 °C i ovn eller på grill for kanter.
  - Server i boller, tacos eller med kartoffelsalat.
faq:
  - question: Forskel på skærbar sous vide?
    answer: [Oksespidsbryst sous vide](/opskrifter/sous-vide/oksespidsbryst-sous-vide) ved 70 °C giver skiver. 74 °C her giver trækbart pulled.
  - question: Kan den fryses?
    answer: Ja — køl i isbad, frys i posen. Optø, træk og finish.
  - question: For tør?
    answer: Bland mere posevæske i, og undgå for lang finish uden sauce.
  - question: Grill-røg?
    answer: Kort røg 30–45 minutter efter badet, før du trækker, giver mere BBQ-smag.
body: |
  Pulled oksebryst sous vide er trevel-versionen: ét døgn ved 74 °C, så gaflerne gør resten.

  Skiver er en anden opskrift. Her skal det falde fra hinanden.

  Sauce efter træk. Bark i finish.
tip: Skum fedtet fra posevæsken, før du blander det i — ellers bliver pulled-bøffen fedtet i stedet for saftig.
=====
title: Pastrami-brisket sous vide
slug: pastrami-brisket-sous-vide
category: sous-vide
description: Sous vide pastrami-brisket — sprængt spidsbryst med peber-koriander, tilberedt ved 64 °C i 48 timer til fast, pålægsagtig struktur.
prepTime: PT40M
cookTime: PT48H
totalTime: PT7D
servings: 10
difficulty: svær
tags:
  - pastrami
  - oksespidsbryst
  - brisket
  - oksekød
  - sous vide
  - sprængt oksebryst
  - pålæg
imageAlt: Sous vide pastrami-brisket skåret i tynde pålægsskiver med peber-koriander
featured: false
ingredients:
  - 2–2,5 kg oksespidsbryst
  - Lage: 3 l vand, 250 g salt, 100 g sukker, 1 spsk peberkorn, 1 spsk korianderfrø, 4 laurbær, 4 nelliker — evt. 1 tsk saltpeter
  - Skorpe: 3 spsk knust koriander, 3 spsk grov peber
  - Valgfrit: 1 spsk røgaroma eller kort røg-finish
steps:
  - Spræng 5 døgn i kold lage. Vend dagligt. Skyl og tør.
  - Gnid skorpen ind. Pose tæt (dobbeltpose hvis peber stikker).
  - Sous vide ved 64 °C i 48 timer — lav temperatur giver fast, skærbar pålægsstruktur.
  - Tag ud, køl i isbad, stil under let pres i køleskab 6–12 timer.
  - Skær papirtyndt koldt. Evt. 15 minutter ved 200 °C for let skorpe, hvis du serverer varm.
faq:
  - question: Hvorfor 64 °C og ikke 70?
    answer: 64 °C / 48 t giver fastere skiver til pålæg. 70 °C er mere middag. Se også [sprængt oksebryst sous vide](/opskrifter/sous-vide/spraengt-oksebryst-sous-vide).
  - question: Trækul-pastrami i stedet?
    answer: [Sprængt spidsbryst-pastrami](/opskrifter/roeg/spraengt-spidsbryst-pastrami) er røg og bark. Denne er præcision og skæremaskine.
  - question: Røgaroma?
    answer: En teskefuld i posen eller 30 minutter kold/varm røg efter badet. Ellers er det mere «krydret saltkød» end delikatesse-pastrami.
  - question: Pres?
    answer: Let vægt (fx skærebræt + dåser) giver jævnere skiver. Ikke mursten — bare forme.
body: |
  Pastrami sous vide i 48 timer er tålmodighed med termostat: salt, skorpe, 64 °C, to døgn.

  Strukturen skal være pålæg — ikke pulled. Derfor lav varme og lang tid.

  Skær koldt. Tyndt. Rugbrød eller rye.
tip: Dobbeltpose peber-koriander-skorpen. Hele frø kan punktere poser og ødelægge to døgns arbejde.
=====
title: Oksespidsbryst sous vide med hvidløg og rosmarin
slug: oksespidsbryst-sous-vide-hvidloeg-rosmarin
category: sous-vide
description: Oksespidsbryst sous vide med hvidløgs- og rosmarinfedt — vakuumpakket brisket med afklaret smør, hvidløg og frisk rosmarin.
prepTime: PT20M
cookTime: PT30H
totalTime: PT30H30M
servings: 8
difficulty: svær
tags:
  - oksespidsbryst
  - brisket
  - oksekød
  - sous vide
  - hvidløg
  - rosmarin
imageAlt: Sous vide oksespidsbryst med hvidløg og rosmarin skåret i saftige skiver
featured: false
ingredients:
  - 2–2,5 kg oksespidsbryst
  - 80 g afklaret smør (ghee)
  - 6 fed hvidløg, knuste
  - 4 rosmarinstængler
  - 2 tsk salt, 1 tsk peber
  - Flagesalt til servering
steps:
  - Salt og peber kødet. Læg i pose med afklaret smør, hvidløg og rosmarin.
  - Sous vide ved 70 °C i 30 timer til skærbare, møre skiver.
  - Tag ud. Gem fedtet. Tør overfladen.
  - Finish 10–15 minutter ved 220 °C i ovn eller på pande/grill for skorpe — pensl med det aromatiske fedt.
  - Hvile 15 minutter. Skær på tværs. Flagesalt.
faq:
  - question: Almindeligt smør?
    answer: Afklaret er bedre — mælketørstof brænder ved finish. Almindeligt smør kan bruges i posen, men skim det fra bagefter.
  - question: 74 °C til pulled?
    answer: Ja, samme fedt og urter ved 74 °C / 24 t — se også [pulled oksebryst sous vide](/opskrifter/sous-vide/pulled-oksebryst-sous-vide).
  - question: Timian i stedet?
    answer: Ja. Rosmarin er klassikeren her. Undgå for meget frisk hvidløg i 30 timer, hvis du hader skarphed — rist det let først.
  - question: Posevæsken?
    answer: Skum fedt fra, reducér resten til jus. Det er flydende hvidløgssmør.
body: |
  Hvidløg, rosmarin og afklaret smør i posen — brisket der smager af søndagssteg, men med sous vide-præcision.

  70 °C. Tredive timer. Finish for skorpe.

  Fedtet er dressingen. Brug det.
tip: Knus hvidløgsfeddene, men lad dem være hele. Hakket hvidløg bliver bittert efter et døgn i varmt fedt.
=====
title: Ingefær- og sojaglaseret spidsbryst sous vide
slug: oksespidsbryst-sous-vide-soja-ingefaer
category: sous-vide
description: Ingefær- og sojaglaseret oksespidsbryst sous vide — langtidsbryst penslet med soja-ingefærreduktion og brændt af under grillen.
prepTime: PT25M
cookTime: PT30H
totalTime: PT31H
servings: 8
difficulty: svær
tags:
  - oksespidsbryst
  - brisket
  - oksekød
  - sous vide
  - soja
  - ingefær
  - asiatisk
imageAlt: Soja-ingefærglaseret oksespidsbryst sous vide med blank, karamelliseret skorpe
featured: false
ingredients:
  - 2–2,5 kg oksespidsbryst
  - 1 spsk salt
  - Glace: 1 dl mørk soja, 3 spsk honning eller brun farin, 2 spsk riven frisk ingefær, 2 fed hvidløg, 1 spsk riseddike, 1 tsk sesamolie
  - Sesamfrø og forårsløg til pynt
steps:
  - Salt kødet let. Pose. Sous vide ved 70 °C i 30 timer (eller 74 °C / 24 t til mere trækbar).
  - Kog glacen sammen 8–10 minutter, til den er klistret.
  - Tag kødet ud, tør. Pensl glacen. Grillfunktion eller 250 °C i ovn 8–12 minutter — pensl igen midtvejs.
  - Hvile 10 minutter. Skær tyndt på tværs. Sesam og forårsløg.
faq:
  - question: For salt med soja?
    answer: Gå nemt med salt før badet. Sojaen er saltbomben i finish.
  - question: Kan jeg bruge teriyaki?
    answer: Ja som base — reducér stadig, så den napper. Tynd flaskesauce brænder uden at klæbe.
  - question: Røg?
    answer: Valgfrit kort røg efter badet, før glacen. Ellers er det mere lacquer end BBQ.
  - question: Pulled i stedet?
    answer: 74 °C / 24 t, træk, og vend i glacen — godt til bowls og bao.
body: |
  Soja og ingefær efter badet: brisket der får lacquer under grillen.

  Vandbadet laver mørheden. Glacen laver skorpen.

  Pensl. Brænd af. Gentag.
tip: Tør kødet knastørt før glacen. Våd overflade damper, og sukkeret klistrer aldrig.
=====
title: Rødvinsbraiseret spidsbryst med marv
slug: roedvinsbraiseret-spidsbryst-marv
category: stobejern
description: Rødvinsbraiseret oksespidsbryst med marv og timian — brunet i baconfedt og simret i en flaske tør rødvin og oksemarv.
prepTime: PT30M
cookTime: PT3H30M
totalTime: PT4H
servings: 6
difficulty: mellem
tags:
  - oksespidsbryst
  - oksekød
  - rødvin
  - marv
  - dutch oven
  - støbejern
  - gæstemad
imageAlt: Rødvinsbraiseret spidsbryst med mørk sauce og oksemarv i støbejern
featured: false
ingredients:
  - 1,5–1,8 kg oksespidsbryst i ét stykke
  - 100 g bacon i tern
  - 2 marvben (eller 2–3 spsk rå oksemarv)
  - 2 løg, 2 gulerødder, 2 stilke selleri
  - 2 spsk tomatpuré
  - 1 flaske tør rødvin (75 cl)
  - 3 dl oksefond
  - 4 kviste timian, 2 laurbærblade
  - Salt og peber
steps:
  - Brun bacon i Dutch Oven. Tag op. Brun kødet hårdt i baconfedtet på alle sider. Tag op.
  - Svits grøntsager 8 minutter. Tomatpuré 1 minut. Vin i, skrab bunden, kog 3–4 minutter.
  - Kød, bacon, marvben, fond, timian og laurbær i. Væsken skal næsten dække.
  - Låg på. Ovnen 160 °C i 3–3½ time, til kødet er gaffelmørt.
  - Tag kød og marvben op. Si saucen, reducér til blank. Rør marven ud i saucen. Skær kødet, sauce over.
faq:
  - question: Forskel på mørkt øl?
    answer: [Braiseret oksespidsbryst i mørkt øl](/opskrifter/stobejern/oksespidsbryst-moerkt-oel) er malt og sødme. Her er det vin, marv og dybere fedme.
  - question: Hvilken vin?
    answer: Tør, fyldig — cabernet, syrah eller billig bordeaux. Undgå sød vin.
  - question: Uden marvben?
    answer: Brug 2–3 spsk marv fra slagteren, eller skip og accepter en lidt tyndere sauce.
  - question: Dagen før?
    answer: Ja. Køl i saucen, skrab fedt, varm forsigtigt op.
body: |
  En hel flaske rødvin, baconfedt og marv — spidsbryst der bliver til gæstemad med ekstrem dybde.

  Brun hårdt. Vin ind. Låg på.

  Marven er saucens hemmelighed. Rør den ud til sidst.
tip: Reducér saucen til den napper skeen, før marven går i — ellers fortynder du det fede lag.
=====
title: Spidsbryst i mørk flødesovs
slug: spidsbryst-moerk-floedesovs
category: stobejern
description: Spidsbryst i mørk flødesovs — mormor-braisering i støbejern, hvor skyen piskes op med piskefløde og en smule ribsgele.
prepTime: PT25M
cookTime: PT3H15M
totalTime: PT3H40M
servings: 6
difficulty: mellem
tags:
  - oksespidsbryst
  - oksekød
  - flødesovs
  - mormor
  - dutch oven
  - støbejern
  - gæstemad
imageAlt: Braiseret spidsbryst i mørk flødesovs med ribsgele serveret med kartofler
featured: false
ingredients:
  - 1,5 kg oksespidsbryst
  - 2 spsk smør + 1 spsk olie
  - 2 løg, 2 gulerødder
  - 2 spsk hvedemel
  - 5 dl oksefond
  - 2 dl piskefløde
  - 1–2 spsk ribsgele
  - 2 laurbærblade, 4 peberkorn, 3 kviste timian
  - Salt og peber
steps:
  - Brun kødet hårdt i smør og olie. Tag op. Svits løg og gulerod.
  - Drys mel over, rør 1 minut. Fond i, skrab bunden. Krydderier i.
  - Kød tilbage. Låg på. Ovnen 160 °C i ca. 3 timer, til mørt.
  - Tag kødet op. Si skyen. Rør fløde og ribsgele i. Kog op, smag til — saucen skal være mør og blank.
  - Skær eller træk kødet. Sauce over. Server med kogte kartofler eller kartoffelmos.
faq:
  - question: Ribsgele?
    answer: En skefuld giver sødme og glans — klassisk mormor-trick. Solbærgele virker også.
  - question: Kan den laves dagen før?
    answer: Ja. Fløden røres i ved opvarmning, så saucen ikke skiller i køleskabet.
  - question: Mere festligt?
    answer: Skift fonden delvist ud med rødvin — eller gå direkte til [rødvinsbraiseret spidsbryst med marv](/opskrifter/stobejern/roedvinsbraiseret-spidsbryst-marv).
  - question: For sød sauce?
    answer: Start med 1 spsk gele. Smag. Mere peber og en skvæt eddike retter op.
body: |
  Mormor-style spidsbryst: brun, braiser, fløde og en ske ribsgele i skyen.

  Det er ikke BBQ. Det er søndagsbord.

  Saucen skal være mør. Kødet skal give sig.
tip: Si grøntsagerne fra, før fløden går i — ellers får du grå, knoldet sovs i stedet for blank mormor-sauce.
=====
title: Spidsbryst i fransk løgsuppe
slug: spidsbryst-fransk-loegsuppe
category: stobejern
description: Braiseret oksespidsbryst i fransk løgsuppe — kilo karamelliserede løg, oksefond og hvidvin, bagt under låg til kødet falder fra hinanden.
prepTime: PT40M
cookTime: PT3H30M
totalTime: PT4H10M
servings: 6
difficulty: mellem
tags:
  - oksespidsbryst
  - oksekød
  - løg
  - fransk løgsuppe
  - dutch oven
  - støbejern
  - gæstemad
imageAlt: Braiseret spidsbryst dækket af karamelliserede løg i støbejernsgryde
featured: false
ingredients:
  - 1,5–1,8 kg oksespidsbryst
  - 1,5–2 kg gule løg, tyndt skåret
  - 3 spsk smør + 1 spsk olie
  - 2 dl tør hvidvin
  - 8 dl oksefond
  - 4 kviste timian, 2 laurbærblade
  - 1 spsk cognac (valgfrit)
  - Salt og peber
  - Evt. gruyère-toast til servering
steps:
  - Brun kødet hårdt. Tag op.
  - Karamelliser løgene i smør og olie 35–45 minutter på middel varme — de skal være dybt gyldne, ikke stegte sorte.
  - Vin i, skrab. Fond, timian, laurbær. Kød ned, så løgene dækker det helt.
  - Låg på. Ovnen 160 °C i 3–3½ time, til kødet falder fra hinanden.
  - Smag til, evt. cognac. Træk eller skær kødet. Server med løgene som sauce — og gerne en ostegratineret toast ved siden af.
faq:
  - question: Kun løgsuppe uden kød?
    answer: Se [fransk løgsuppe](/opskrifter/gryde/fransk-loegsuppe). Her er løgene braiseringsmedium til spidsbryst.
  - question: Rødvin i stedet?
    answer: Muligt, men hvidvin holder løgene lysere og sødere. Rødvin gør retten tungere — mere [rødvinsbraiseret spidsbryst](/opskrifter/stobejern/roedvinsbraiseret-spidsbryst-marv).
  - question: Kan løgene laves dagen før?
    answer: Ja. Karamellisér, køl, og braiser dagen efter. Det er den tunge del.
  - question: Gruyère på toppen?
    answer: Bag toast med ost separat. Ost direkte i gryden bliver gummiagtig efter tre timer.
body: |
  Kilo løg, hvidvin og fond — spidsbryst der bader i fransk løgsuppe, til det falder fra hinanden.

  Løgene er retten. Kødet er bonus.

  Karamellisér ordenligt. Genveje smager af rå løg.
tip: Salt løgene tidligt, så de slipper væske. Utålmodighed på denne fase ødelægger hele gryden.
=====
title: Corned beef med spidskål
slug: corned-beef-spidskaal
category: gryde
description: Klassisk corned beef med spidskål — langtidssprængt oksebryst kogt med sennepsfrø og allehånde, serveret med smørdampet spidskål.
prepTime: PT30M
cookTime: PT3H30M
totalTime: PT5D
servings: 6
difficulty: mellem
tags:
  - corned beef
  - sprængt oksebryst
  - oksekød
  - spidskål
  - saltkød
  - gæstemad
  - irsk
imageAlt: Varm corned beef skåret i skiver med smørdampet spidskål
featured: false
ingredients:
  - 1,5–2 kg sprængt oksebryst (færdigsprængt eller hjemmelavet)
  - Til kogning: 1 løg, 2 gulerødder, 1 spsk sennepsfrø, 1 spsk allehånde, 4 laurbærblade, 8 peberkorn
  - 1 spidskål
  - 40 g smør
  - Flagesalt, peber, frisk dild eller persille
  - Sennep til servering
steps:
  - Læg det sprængte bryst i gryde med koldt vand, grøntsager og krydderier. Bring i kog, skum af.
  - Simre blidt 2½–3½ time, til kniven går let i. Tag op, hvil 15 minutter under folie.
  - Snit spidskålen i både. Damp eller steg i smør 6–8 minutter med låg, til den er mør men stadig har bid. Salt og peber.
  - Skær kødet i tykke, varme skiver på tværs af fibrene.
  - Server rygende varmt med kål, sennep og lidt af kogevæsken som jus.
faq:
  - question: Hjemmelavet sprængning?
    answer: Følg [hjemmelavet sprængt oksebryst](/opskrifter/palaeg/spraengt-oksebryst) i 5 døgn, og kog som her til middag i stedet for koldt pålæg.
  - question: Trykkoger?
    answer: [Sprængt oksebryst i trykkoger](/opskrifter/trykkoger/spraengt-oksebryst-trykkoger) er lynversionen. Her er det klassisk gryde og kål.
  - question: Hvidkål i stedet?
    answer: Ja. Spidskål er sødere og hurtigere. Hvidkål skal have længere tid.
  - question: Resten dagen efter?
    answer: Kolde skiver på rugbrød er næsten bedre. Varm kålen i smør.
body: |
  Corned beef med spidskål er saltkød til middagsbordet: lang simring, smørkål, sennep.

  Ikke pålægsskiver. Tykke, varme skiver.

  Krydderierne i gryden er duften. Sennepen er finish.
tip: Smag kogevæsken efter en time. For salt? Skift vandet. For mild? Lad være — kødet er allerede sprængt.
=====
title: Røget og sprængt saltkød
slug: roget-spraengt-saltkoed
category: roeg
description: Røget og sprængt saltkød — oksespidsbryst i saltlage, koldrøget over bøgesmuld i 6 timer, og til sidst kogt blidt til middagsbordet.
prepTime: PT40M
cookTime: PT9H
totalTime: PT6D
servings: 8
difficulty: svær
tags:
  - saltkød
  - sprængt oksebryst
  - oksekød
  - koldrøgning
  - oksespidsbryst
  - gæstemad
imageAlt: Røget sprængt saltkød skåret i skiver med lys røgring
featured: false
ingredients:
  - 2–2,5 kg oksespidsbryst
  - Lage: 3 l vand, 250 g salt, 80 g sukker, 1 spsk peberkorn, 4 laurbær, 4 nelliker, 1 spsk sennepsfrø — evt. 1 tsk saltpeter
  - Bøgesmuld til koldrøgning
  - Til kogning: 1 løg, 2 gulerødder, ekstra peberkorn og laurbær
steps:
  - Spræng kødet 5 døgn i kold lage. Vend dagligt. Skyl og tør.
  - Tør på rist i køleskab 12–24 timer (pellicle).
  - Koldrøg over bøgesmuld 6 timer under 25–30 °C. Kødet skal ikke steges — kun tage røg.
  - Læg i gryde med frisk vand og grøntsager. Simre blidt 2½–3½ time, til mørt.
  - Hvile 15 minutter. Skær tykke skiver. Server varm med sennep og kartofler — eller køl til pålæg.
faq:
  - question: Forskel på pastrami?
    answer: Pastrami får peber-koriander-skorpe og varmrøg/[trækul-pastrami](/opskrifter/roeg/spraengt-spidsbryst-pastrami). Her er det koldrøg + kogning — klassisk røget saltkød.
  - question: Varmrøg i stedet?
    answer: Så nærmer du dig pastrami. Hold koldrøg, hvis du vil have kogt saltkød med røgaroma.
  - question: Uden koldrøger?
    answer: Svært at fake. Kort varmrøg giver anden karakter. Ellers brug [sprængt oksebryst](/opskrifter/palaeg/spraengt-oksebryst) uden røg.
  - question: For stærk røg?
    answer: 6 timer bøg er mild-mellem. Mere end 8 timer kan blive asket. Luft kødet mellem røg og kogning.
body: |
  Først salt, så koldrøg, så blid kogning — dobbeltdisciplin til røget saltkød.

  Pellicle før smuld. Simring efter røg.

  Det er middagsbord og smørrebrød i samme stykke kød.
tip: Hold koldrøgen kold. Over 30 °C begynder kødet at «stege» i overfladen, og du mister den rene saltkøds-konsistens.
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
assert len(blocks) == 13, len(blocks)
for b in blocks:
    d = parse_block(b)
    assert d.get("faq") and len(d["faq"]) >= 3, (d.get("slug"), d.get("faq"))
    assert d.get("tip"), d.get("slug")
    assert "oksekød" in d["tags"], d.get("slug")
    out = ROOT / d["category"]
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{d['slug']}.mdx"
    if path.exists():
        raise SystemExit(f"slug collision: {path}")
    path.write_text(to_mdx(d), encoding="utf-8")
    print("wrote", d["category"] + "/" + path.name)
