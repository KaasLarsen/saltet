#!/usr/bin/env python3
"""Danske klassikere batch — long-tail SEO på tværs af metoder (aug 2026)."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"
PUBLIC = Path(__file__).resolve().parent.parent / "public/recipes"
PUBLISHED = "2026-08-31"

IMG_MAP = {
    "klassisk-rodgroed": PUBLIC / "gryde" / "klassisk-risengrod.jpg",
    "klassisk-aeblekage": PUBLIC / "airfryer" / "bagte-aebler-bananer.jpg",
    "koldskal": PUBLIC / "trykkoger" / "risengrod-trykkoger.jpg",
    "karamelrand": PUBLIC / "ovn" / "saltkaramel-brownie-havsalt.jpg",
    "blodpoelse-pande": PUBLIC / "pande" / "medisterpoelse-pande.jpg",
    "hjemmelavet-leverpostej": PUBLIC / "palaeg" / "leverpostej.jpg",
    "boller-i-karry-trykkoger": PUBLIC / "gryde" / "boller-i-karry.jpg",
    "stjerneskud-airfryer": PUBLIC / "pande" / "stjerneskud.jpg",
    "krebinetter-airfryer": PUBLIC / "pande" / "krebinetter.jpg",
    "hjerter-i-floedesovs-trykkoger": PUBLIC / "gryde" / "hjerter-i-floedesovs.jpg",
    "stegt-flaesk-grill": PUBLIC / "airfryer" / "stegt-flaesk.jpg",
    "stegt-flaesk-ovn": PUBLIC / "pande" / "stegt-flaesk-pande.jpg",
    "forloren-hare-stobejern": PUBLIC / "gryde" / "forloren-hare-gryde.jpg",
    "skipperlabskovs-stobejern": PUBLIC / "gryde" / "skipperlabskovs.jpg",
    "moerbradboeffer-airfryer": PUBLIC / "pande" / "tykke-moerbradboeffer-bloede-loeg.jpg",
    "moerbradboeffer-grill": PUBLIC / "grill" / "moerbradspyd-sennep-timian.jpg",
    "aeggekage-ovn": PUBLIC / "airfryer" / "aeggekage.jpg",
    "tarteletter-ovn": PUBLIC / "airfryer" / "tarteletter-hoens-asparges.jpg",
}

RECIPES = r'''
=====
title: Klassisk rødgrød
slug: klassisk-rodgroed
category: gryde
description: Klassisk rødgrød — dansk sommerdessert med jordbær, ribs og vanilje. Server med fløde eller mælk.
prepTime: PT15M
cookTime: PT15M
totalTime: PT30M
servings: 4
difficulty: nem
tags:
  - rødgrød
  - rødgrød opskrift
  - dansk klassiker
  - dansk-klassiker
  - dessert
  - sommer
  - gryde
imageAlt: Klassisk rødgrød i skål med fløde
featured: true
ingredients:
  - 500 g jordbær og ribs (frisk eller frosne)
  - 150 g sukker
  - 2 dl vand
  - 2 spsk kartoffelmel eller majsstivelse
  - 1 tsk vaniljesukker eller vaniljestang
  - Fløde eller mælk til servering
steps:
  - Bring bær, sukker og vand i kog i gryde. Skum hvis nødvendigt. Simre 5–8 minutter.
  - Rør kartoffelmel i lidt koldt vand. Pisk i under omrøring. Kog 1 minut til tyk, klar grød.
  - Smag til — mere sukker hvis bærrene var syrlige. Hæld i skål, dæk med folie mod skind.
  - Køl. Server med kold fløde eller mælk.
faq:
  - question: Kartoffelmel eller hvedemel?
    answer: Kartoffelmel giver klar, blank rødgrød. Hvedemel gør den uklar — undgå.
  - question: Frosne bær?
    answer: Ja. Ekstra minut kogning, lidt ekstra sukker hvis de var syrlige.
  - question: Hvor længe holder den?
    answer: 3–4 dage i køl. Smager bedst dagen efter.
  - question: Med fløde eller mælk?
    answer: Klassisk er fløde. Mælk er barndom. Begge dele er korrekt.
body: |
  Klassisk rødgrød er dansk sommer i en skål.

  Bær. Sukker. Kartoffelmel. Kold fløde.

  Det er ikke gourmet — det er det du lavede, da bedsteforældrene havde have.
tip: Rør kartoffelmel i koldt vand først — ellers klumper det i den varme grød.
=====
title: Klassisk æblekage
slug: klassisk-aeblekage
category: ovn
description: Klassisk æblekage — dansk dessert med saftige æbler, kanel og sprød crumble-top i ovn.
prepTime: PT20M
cookTime: PT35M
totalTime: PT55M
servings: 6
difficulty: nem
tags:
  - æblekage
  - æblekage opskrift
  - dansk klassiker
  - dansk-klassiker
  - dessert
  - ovn
imageAlt: Klassisk æblekage med crumble og kanel
featured: true
ingredients:
  - 800 g syrlige æbler, skrællede og i skiver
  - 100 g sukker + 1 spsk til æbler
  - 1 tsk kanel
  - Saft af ½ citron
  - 150 g hvedemel
  - 100 g smør, koldt i tern
  - 75 g sukker til crumble
  - Valgfrit: 2 spsk havregryn i crumble
steps:
  - Tænd ovn 180 °C. Læg æbler i fad med sukker, kanel og citron. Bland.
  - Smuldr mel, smør og sukker til crumble — grove klumper, ikke dej.
  - Fordel crumble over æblerne. Bag 30–35 min til gylden top og møre æbler.
  - Server lun med vaniljeis eller fløde.
faq:
  - question: Syrlige eller søde æbler?
    answer: Syrlige (Gravenstein, Ingrid Marie). Søde æbler bliver mos uden struktur.
  - question: Skal skallerne af?
    answer: Ja til klassisk dansk æblekage — ensartet tekstur og kortere bagetid.
  - question: Dagen før?
    answer: Smager fint dagen efter — genopvarm 160 °C i 15 min for sprød crumble.
  - question: Crumble eller dej?
    answer: Crumble — sprød top. Dej bliver kage; det er en anden ret.
body: |
  Klassisk æblekage er mormors dessert uden fuss.

  Syrlige æbler. Kanel. Smør-crumbler der knaser.

  Server lun — fløde eller is er ikke pynt, det er kontrasten.
tip: Bland ikke crumble for længe — klumperne skal være ujævne, ellers bliver det kagebund.
=====
title: Koldskål
slug: koldskal
category: gryde
description: Koldskål opskrift — klassisk dansk sommerret med kærnemælk, æg og vanilje. Server med kammerjunkere.
prepTime: PT15M
cookTime: PT5M
totalTime: PT2H20M
servings: 4
difficulty: nem
tags:
  - koldskål
  - koldskål opskrift
  - dansk klassiker
  - dansk-klassiker
  - sommer
  - dessert
  - gryde
imageAlt: Koldskål i skål med kammerjunkere
featured: true
ingredients:
  - 1 l kærnemælk eller tyk koldskål fra butik som base
  - 2 pasteuriserede æggeblommer
  - 2 spsk sukker
  - 1 tsk vaniljesukker
  - Saft af ½ citron
  - 1 dl piskefløde, pisket let (valgfrit)
  - Kammerjunkere til servering
steps:
  - Pisk æggeblommer, sukker og vanilje lyst og luftigt.
  - Varm kærnemælk til lige under kogepunkt i gryde — den må ikke koge hårdt.
  - Pisk lidt varm mælk i æggeblommerne. Hæld tilbage i gryden under omrørning.
  - Varm til 82–85 °C under konstant omrøring — tyk, cremet konsistens. Si hvis nødvendigt.
  - Køl hurtigt. Citron. Vend evt. fløde i. Server med kammerjunkere.
faq:
  - question: Forskel på koldskål og koldskålssalat?
    answer: Koldskål er den cremede mælkeret med kammerjunkere. Koldskålssalat er grøntsagssalat — se pålæg.
  - question: Rå æg?
    answer: Brug pasteuriserede æggeblommer eller varm mælken til 85 °C som her.
  - question: Butikskoldskål forbedret?
    answer: Ja — pisk vanilje, citron og pisket fløde i. Hurtig sommerversion.
  - question: Uden kærnemælk?
    answer: Tyk kærnemælk fra butik eller surmælksprodukt — ikke almindelig letmælk.
body: |
  Koldskål er dansk sommer i en skål — ikke en salat.

  Varm mælk. Æggeblommer. Køl. Kammerjunkere.

  Det er barndom, terrasse og «der er ikke mere varmt at spise».
tip: Rør hele tiden ved opvarmning — én klump æg er nok til at ødelægge silken.
=====
title: Karamelrand
slug: karamelrand
category: ovn
description: Karamelrand opskrift — klassisk dansk dessert med karamel, æg og fløde bagt i ovn.
prepTime: PT20M
cookTime: PT45M
totalTime: PT1H5M
servings: 6
difficulty: mellem
tags:
  - karamelrand
  - karamelrand opskrift
  - dansk klassiker
  - dansk-klassiker
  - dessert
  - ovn
imageAlt: Gylden karamelrand skåret i skiver
featured: false
ingredients:
  - 150 g sukker til karamel
  - 2 spsk vand
  - 4 æg
  - 5 dl piskefløde
  - 1 tsk vanilje
  - Valgfrit: 1 spsk rom
steps:
  - Tænd ovn 150 °C. Smelt sukker og vand til gylden karamel i ovnfast form — pas på brænding.
  - Pisk æg, fløde, vanilje og evt. rom. Hæld forsigtigt over karamellen.
  - Bag vandbad 40–45 min, til randen er stivnet men stadig let vuggende i midten.
  - Køl minimum 2 timer. Vend ud på fad. Skær i skiver.
faq:
  - question: Karamel stivner?
    answer: Arbejd hurtigt når karamellen er gylden — den hærder. Varm formen i ovnen igen hvis nødvendigt.
  - question: Revner ved vending?
    answer: Køl grundigt. Løs kanterne med varm kniv før du vender.
  - question: Uden vandbad?
    answer: Muligt ved lavere varme, men vandbad giver jævn stivning uden kogte æg.
  - question: Dagen før?
    answer: Ja — smager bedre efter nat i køl.
body: |
  Karamelrand er den dessert der kræver tålmodighed og en ovnfast form.

  Karamel i bunden. Fløde og æg ovenpå. Lang, lav varme.

  Den falder ikke i «hverdags»-kategorien — det er søndags- og fødselsdags-territorium.
tip: Brug ramekiner til portioner — nemmere at vende end én stor rand.
=====
title: Stegt blodpølse på pande
slug: blodpoelse-pande
category: pande
description: Stegt blodpølse på pande — sprød skorpe udenpå, blød indeni. Klassisk dansk mormor-mad.
prepTime: PT5M
cookTime: PT12M
totalTime: PT17M
servings: 2
difficulty: nem
tags:
  - blodpølse
  - blodpølse på panden
  - dansk klassiker
  - dansk-klassiker
  - pande
  - mormormad
imageAlt: Stegte skiver blodpølse med sprød skorpe
featured: false
ingredients:
  - 1 blodpølse (ca. 300–400 g)
  - 1 spsk smør eller svinefedt
  - Valgfrit: 1 løg i ringe, stegt i samme pande
  - Æblemos, rugbrød eller kartofler til servering
steps:
  - Skær blodpølse i skiver ca. 1 cm tykke. Dup tør forsigtigt.
  - Varm smør på medium-høj pande. Læg skiver i ét lag.
  - Steg 3–4 minutter per side til gylden skorpe — vend forsigtigt, den er skør.
  - Server med løg, æblemos og rugbrød — eller som tilbehør til steg.
faq:
  - question: Falder den fra hinanden?
    answer: Steg på medium — for høj varme og den smuldrer. Vend med bred spatel.
  - question: Skal den gennemsteges?
    answer: Den er forkogt — du jager skorpe og varme, ikke mad sikkerhed som råt kød.
  - question: Med svinekød indeni?
    answer: Ja, mange blodpølser har fedt/stykker — steg til fedtet er gyldent.
  - question: Alternativ til pande?
    answer: Ovn 200 °C på bagepapir 12–15 min — mindre skorpe, mere jævn.
body: |
  Stegt blodpølse er polariserende — og for dem der elsker den, er pande-versionen hellig.

  Medium varme. Tykke skiver. Sprød kant, blød midte.

  Æblemos er ikke valgfrit for mange — syre mod blod og fedt.
tip: Tag pølsen ud af køleskabet 10 min før — kold skive på varm pande revner.
=====
title: Hjemmelavet leverpostej i ovn
slug: hjemmelavet-leverpostej
category: ovn
description: Hjemmelavet leverpostej i ovn — cremet, fyldig postej med bacon og løg. Bedre end tube.
prepTime: PT25M
cookTime: PT50M
totalTime: PT1H15M
servings: 8
difficulty: mellem
tags:
  - leverpostej
  - hjemmelavet leverpostej
  - dansk klassiker
  - dansk-klassiker
  - julefrokost
  - ovn
imageAlt: Hjemmelavet leverpostej i ovnfast form
featured: false
ingredients:
  - 500 g kalve- eller griselever, renset
  - 200 g bacon i tern
  - 2 løg, hakket
  - 2 æg
  - 100 g smør, smeltet
  - 2 dl fløde
  - 2 spsk hvedemel
  - 1 tsk salt, peber, allehånde
  - Valgfrit: 2 spsk madeira eller sherry
steps:
  - Steg bacon og løg bløde i pande. Afkøl let.
  - Blend lever med æg, smør, fløde og mel til glat masse.
  - Vend bacon, løg og krydderier i. Smag til — salt forsigtigt pga. bacon.
  - Hæld i smurt ovnfast form. Bag 160 °C i 45–50 min, til kerne 70 °C og top fast.
  - Køl i formen. Vend ud eller skær i skiver. Server kold på rugbrød.
faq:
  - question: Bitter lever?
    answer: Blød lever i mælk 30 min før. Fjern hinder og blodkar grundigt.
  - question: Samme som pålæg-opskriften?
    answer: Samme familie — ovn-versionen er til hele postejen. Se også palaeg/leverpostej.
  - question: Fryses?
    answer: Ja — skiver med bagepapir imellem. Tiner langsomt i køl.
  - question: Til julefrokost?
    answer: Klassisk. Lav uge 48 og server med syltede agurker og bacon.
body: |
  Hjemmelavet leverpostej i ovn er julefrokost der smager af noget.

  Ren lever. Bacon. Lang, lav bagning.

  Tube er praktisk — ovn er smag. Du bestemmer salt og peber.
tip: Si postejen mens den er lun — finere silke end at si kold skive til skive.
=====
title: Boller i karry i trykkoger
slug: boller-i-karry-trykkoger
category: trykkoger
description: Boller i karry i trykkoger — Danmarks nationalret klar på under 30 minutter med møre kødboller.
prepTime: PT20M
cookTime: PT20M
totalTime: PT40M
servings: 4
difficulty: nem
tags:
  - boller i karry
  - boller i karry trykkoger
  - dansk klassiker
  - dansk-klassiker
  - trykkoger
  - karry
imageAlt: Boller i karry fra trykkoger med ris
featured: true
ingredients:
  - 500 g hakket kalv og flæsk
  - 1 æg, ½ dl mælk, ½ dl rasp, løg, salt, peber
  - 2 spsk smør
  - 2 løg, hakket
  - 1 æble, i tern
  - 2 spsk hvedemel, 2 spsk mild karry
  - 4 dl bouillon, 1 dl fløde
steps:
  - Form boller. Brun dem i trykkoger på sauter uden låg. Tag op.
  - Svits løg og æble i fedtet. Drys mel og karry i. Rør 1 minut.
  - Hæld bouillon i. Læg boller tilbage. Luk låg — høj tryk 8 minutter.
  - Hurtig eller naturlig frigivelse efter maskine. Rør fløde i. Server med ris.
faq:
  - question: Forskel på gryde-versionen?
    answer: Samme smag — trykkoger giver kortere simretid. Se gryde/boller-i-karry.
  - question: Bollerne falder fra hinanden?
    answer: Bind farsen godt. Undgå at røre for hårdt efter tryk — de er møre.
  - question: For mild karry?
    answer: Tilsæt ekstra karry efter tryk, eller brug karrypaste — smag til.
  - question: Kan saucen brænde på?
    answer: Dæk med nok bouillon. Rør mel/karry godt før væske.
body: |
  Boller i karry i trykkoger er hverdags-nationalret når tiden er knap.

  Brun boller. Tryk 8 minutter. Fløde til sidst.

  Gryde-versionen er her: boller i karry i gryde — samme ret, to tempoer.
tip: Efterlad trykkogeren på sauter til løg og æble er bløde — det er saucens fundament.
=====
title: Stjerneskud i airfryer
slug: stjerneskud-airfryer
category: airfryer
description: Stjerneskud i airfryer — stegt fiskefilet sprød uden pande, klar til luksus-frokost.
prepTime: PT25M
cookTime: PT12M
totalTime: PT37M
servings: 2
difficulty: mellem
tags:
  - stjerneskud
  - stjerneskud airfryer
  - dansk klassiker
  - dansk-klassiker
  - fisk
  - airfryer
  - frokost
imageAlt: Stjerneskud med stegt fisk fra airfryer
featured: true
ingredients:
  - 2 rødspættefileter til stegning
  - 2 fileter til dampning (samme eller torsk)
  - Mel, æg, rasp
  - 2 skiver franskbrød, ristet
  - 150 g rejer, asparges, mayonnaise, citron, dild
steps:
  - Damp den ene fisk 4–6 min over gryde. Køl let.
  - Paner de andre fileter. Airfry 190 °C i 8–10 min, vend én gang — gylden og gennemstegt.
  - Byg på brød: mayonnaise, dampet fisk, stegt fisk, rejer, asparges, citron.
faq:
  - question: Hele stjerneskud i airfryer?
    answer: Kun stegt komponent — dampet fisk og rejer samles kold/varm. Se pande/stjerneskud.
  - question: Tør fisk?
    answer: Tynde fileter, ét lag, ikke overfyldt kurv. Tjek ved 8 min.
  - question: Frosne fileter?
    answer: Optø helt. Dup tør. +2 minutter. Paner efter optøning.
  - question: Er det snyd?
    answer: Stegt fisk uden stegesprøjt — resten er klassisk stjerneskud.
body: |
  Stjerneskud i airfryer er frokost-luksus uden fedtet pande.

  Damp én fillet. Paner og airfry den anden. Byg.

  Pande-versionen findes på Saltet — her er det sprød steg uden stegesprøjt.
tip: Pensl panerede fileter let med olie — airfryer giver bedre skorpe med fedt på overfladen.
=====
title: Krebinetter i airfryer
slug: krebinetter-airfryer
category: airfryer
description: Krebinetter i airfryer — sprøde panerede karbonader klar på 15 minutter uden stegesprøjt.
prepTime: PT15M
cookTime: PT12M
totalTime: PT27M
servings: 4
difficulty: nem
tags:
  - krebinetter
  - krebinetter airfryer
  - karbonader
  - dansk klassiker
  - dansk-klassiker
  - airfryer
imageAlt: Gyldne krebinetter fra airfryer
featured: false
ingredients:
  - 500 g hakket svinekød (eller kalv/svineblanding)
  - 1 æg, ½ dl mælk, ½ dl rasp, løg, salt, peber
  - Mel, æg, rasp til panering
  - 1 spsk olie til pensling
steps:
  - Bland fars. Form 8 flade krebinetter.
  - Vend i mel, æg, rasp. Pensl let med olie.
  - Airfry 190 °C i 10–12 min, vend halvvejs — kerne 65 °C.
  - Server med kartofler, brun sovs eller agurkesalat.
faq:
  - question: Forskel på karbonader og krebinetter?
    answer: Krebinetter er fladere, paneret klassiker. Karbonader findes også i airfryer på Saltet.
  - question: Tørre kanter?
    answer: Fars med lidt fedt (flæsk). Ikke overkog — træk ved 65 °C.
  - question: Pande-version?
    answer: Se pande/krebinetter — samme fars, mere stegeskorpe i smør.
  - question: Meal prep?
    answer: Paner og fryse rå — airfry fra frosne +4 min.
body: |
  Krebinetter i airfryer er fredagshverdag uden stegesprøjt.

  Paner. Pensl olie. 190 °C til gylden.

  Det smager som pande — bare uden at vaske stænkskærmen.
tip: Pres krebinetterne flade og ens — tykkelse styrer tiden mere end vægt.
=====
title: Hjerter i flødesovs i trykkoger
slug: hjerter-i-floedesovs-trykkoger
category: trykkoger
description: Hjerter i flødesovs i trykkoger — mormor-klassikeren mør på 25 minutter i stedet for 1½ time.
prepTime: PT20M
cookTime: PT25M
totalTime: PT45M
servings: 4
difficulty: mellem
tags:
  - hjerter i flødesovs
  - hjerter trykkoger
  - dansk klassiker
  - dansk-klassiker
  - mormormad
  - trykkoger
imageAlt: Hjerter i flødesovs fra trykkoger
featured: false
ingredients:
  - 800 g kalve- eller grisehjerter, i tern
  - 100 g bacon, 2 løg, 200 g champignoner
  - 2 spsk smør, 2 spsk mel, 2 dl bouillon, 2 dl fløde
  - Tomatpuré, soya, salt, peber, timian
steps:
  - Brun bacon og hjerter i trykkoger på sauter. Tag op. Svits løg og svampe.
  - Rør mel i. Bouillon i. Læg kød tilbage. Luk låg — høj tryk 20 minutter.
  - Frigiv tryk. Rør fløde i. Simre 5 min uden låg til sauce tykner. Smag til.
faq:
  - question: Gryde vs trykkoger?
    answer: Samme ret — trykkoger forkorter simretiden. Se gryde/hjerter-i-floedesovs.
  - question: Hvor køber man hjerter?
    answer: Slagter eller indmad-afdeling. Frosne hjerter virker — tø helt.
  - question: Møre nok?
    answer: 20 min høj tryk giver mør indmad. Over 25 min kan det blive grød.
  - question: Alternativ til hjerter?
    answer: Nyrer eller lever i samme sauce — kortere tryk for lever.
body: |
  Hjerter i flødesovs i trykkoger er mormormad på hverdags-tid.

  Brun. Tryk. Fløde.

  Det er ikke trendy — det er dybde, salt og brun sauce der smager af efterår.
tip: Skær hjerter i ens store tern — ujævn størrelse giver halvmørt og tør i samme gryde.
=====
title: Stegt flæsk på grill
slug: stegt-flaesk-grill
category: grill
description: Stegt flæsk på grill — sprøde skiver med røgsmag til persillesovs og kartofler.
prepTime: PT10M
cookTime: PT15M
totalTime: PT25M
servings: 4
difficulty: nem
tags:
  - stegt flæsk
  - stegt flæsk grill
  - dansk klassiker
  - dansk-klassiker
  - grill
  - persillesovs
imageAlt: Stegt flæsk fra grill med sprøde kanter
featured: true
ingredients:
  - 600 g tykke flæskeskiver
  - Peber, evt. groft salt
  - Valgfrit: 1 tsk paprika til skorpe
steps:
  - Tør flæsket. Forvarm grill til medium-høj direkte varme.
  - Grill skiver 4–5 min per side med låg af — til dyb gylden og sprøde kanter.
  - Læg på rist kort. Server med persillesovs og kogte kartofler.
faq:
  - question: Flammer?
    answer: Fedt drypper — brug to-zoner eller løft over indirekte efter farve.
  - question: Airfryer i stedet?
    answer: Se airfryer/stegt-flaesk — mindre røg, samme sprødhed.
  - question: Skal det saltes?
    answer: Smag først — de fleste skiver er saltede fra butik.
  - question: Persillesovs?
    answer: Se dips/persillesovs — klassisk par til stegt flæsk.
body: |
  Stegt flæsk på grill er dansk klassiker med røg i kanterne.

  Medium-høj varme. Ét lag. Sprød kant.

  Persillesovs og kartofler — intet andet behøver at opfinde sig.
tip: Skær snit i fedtkanten — skiverne krøller ikke, og fedtet smelter jævnere.
=====
title: Stegt flæsk i ovn
slug: stegt-flaesk-ovn
category: ovn
description: Stegt flæsk i ovn — sprøde skiver på bageplade, nem til mange gæster og persillesovs.
prepTime: PT10M
cookTime: PT25M
totalTime: PT35M
servings: 4
difficulty: nem
tags:
  - stegt flæsk
  - stegt flæsk ovn
  - dansk klassiker
  - dansk-klassiker
  - ovn
  - persillesovs
imageAlt: Stegt flæsk fra ovn på bageplade
featured: true
ingredients:
  - 600 g tykke flæskeskiver
  - Peber
steps:
  - Tænd ovn 220 °C. Læg flæsk på rist over bageplade — fedt skal dryppe væk.
  - Bag 20–25 min, vend én gang, til sprøde gyldne kanter.
  - Afdryp på papir. Server med persillesovs og kartofler.
faq:
  - question: Rist eller plade?
    answer: Rist over plade — ellers steger flæsk i eget fedt og bliver blødt.
  - question: Batch til mange?
    answer: Ovn slår pande til 8+ personer — to plader, vend halvvejs.
  - question: Airfryer vs ovn?
    answer: Airfryer hurtigere til små portioner. Ovn bedre til gæster.
  - question: Sprød nok?
    answer: Sidste 3 min grillfunktion eller 240 °C — hold øje.
body: |
  Stegt flæsk i ovn er søndagsmad til ti uden stegesprøjt.

  Høj varme. Rist. Afdryp.

  Persillesovs koger på blusset imens — se persillesovs på Saltet.
tip: Start med kold ovn og flæsk — langsom fedt-udsmeltning, ekstra sprødhed ( +5 min total).
=====
title: Forloren hare i støbejern
slug: forloren-hare-stobejern
category: stobejern
description: Forloren hare i støbejern — hakkebøf i bacon og flødesovs braiseret i Dutch Oven.
prepTime: PT25M
cookTime: PT45M
totalTime: PT1H10M
servings: 4
difficulty: mellem
tags:
  - forloren hare
  - forloren hare støbejern
  - dansk klassiker
  - dansk-klassiker
  - støbejern
  - hakkebøf
imageAlt: Forloren hare i støbejernsgryde med sauce
featured: false
ingredients:
  - 4 tykke hakkebøffer (bøffer af hakket okse)
  - 4 skiver bacon
  - 2 løg, skiver
  - 2 spsk smør, 2 spsk mel, 3 dl bouillon, 2 dl fløde
  - Salt, peber, laurbaer
steps:
  - Form bøffer. Wrap bacon om. Brun i støbejernsgryde. Tag op.
  - Svits løg. Mel i. Bouillon i under omrøring. Fløde og laurbaer.
  - Læg bøffer tilbage. Låg på. Ovn 160 °C i 35–40 min — møre, saftige.
  - Server med kartofler og syrlig tilbehør.
faq:
  - question: Ovn eller blus?
    answer: Ovn giver jævn varme i støbejern — blus alene kræver lav simre og vend.
  - question: Andre varianter?
    answer: Se ovn, gryde og trykkoger — samme ret, fire metoder.
  - question: Tør bøf?
    answer: Tykke bøffer + lav simre. Træk ved 65 °C hvis usikker.
  - question: Hvorfor forloren hare?
    answer: Ingen hare — bare hakkebøf i flødesovs. Danske navne er mærkelige.
body: |
  Forloren hare i støbejern er hakkebøf med attitude og låg på.

  Bacon. Brun. Simre i fløde og bouillon.

  Det er ikke hare — det er Danmark der kalder hakkebøf noget poetisk.
tip: Sear bøfferne hårdt før låg — Maillard er det meste af smagen i saucen.
=====
title: Skipperlabskovs i støbejern
slug: skipperlabskovs-stobejern
category: stobejern
description: Skipperlabskovs i støbejern — dansk gryderet med kartofler, løg og pølse i Dutch Oven.
prepTime: PT15M
cookTime: PT40M
totalTime: PT55M
servings: 4
difficulty: nem
tags:
  - skipperlabskovs
  - labskovs
  - dansk klassiker
  - dansk-klassiker
  - støbejern
  - gryderet
imageAlt: Skipperlabskovs i støbejernsgryde
featured: false
ingredients:
  - 800 g kartofler i skiver
  - 3 løg i ringe
  - 4 pølser (medister eller wiener)
  - 3 dl vand eller bouillon
  - 2 spsk smør, salt, peber, laurbaer
steps:
  - Lag kartofler, løg og pølser i støbejernsgryde. Dæk med væske næsten til top.
  - Låg på. Ovn 180 °C i 35–40 min — kartofler møre, pølser varme.
  - Smag til. Server direkte fra gryden.
faq:
  - question: Forskel på gryde-version?
    answer: Samme ret — støbejern giver jævn varme i ovn. Se gryde/skipperlabskovs.
  - question: Pølse skiver eller hele?
    answer: Hele pølser er klassisk — skær ved bordet. Skiver giver mere smag i laget.
  - question: Trykkoger?
    answer: Hurtigere — se trykkoger/skipperlabskovs-trykkoger.
  - question: Bål?
    answer: Ja — se baalmad/skipperlabskovs-over-baal.
body: |
  Skipperlabskovs i støbejern er havnearbejder-mad i en Dutch Oven.

  Kartofler. Løg. Pølse. Låg på.

  Det er ikke fancy — det er mættende, salt og varmt.
tip: Brug medister med fedt — magre pølser giver tyndere smag i lagene.
=====
title: Mørbradbøffer i airfryer
slug: moerbradboeffer-airfryer
category: airfryer
description: Mørbradbøffer i airfryer — saftige svinemørbradbøffer med brun sovs på under 20 minutter.
prepTime: PT10M
cookTime: PT12M
totalTime: PT22M
servings: 2
difficulty: nem
tags:
  - mørbradbøffer
  - mørbradbøffer airfryer
  - dansk klassiker
  - dansk-klassiker
  - airfryer
  - svinemørbrad
imageAlt: Mørbradbøffer fra airfryer i skiver
featured: false
ingredients:
  - 2 svinemørbradbøffer (ca. 150 g hver)
  - Salt, peber
  - 1 spsk olie
  - Valgfrit: smør og timian til finish
steps:
  - Dup bøffer tørre. Salt og peber. Pensl med olie.
  - Airfry 200 °C i 6 min. Vend. 4–6 min mere til 63–65 °C kerne.
  - Hvil 3 min. Server med brun sovs, kartofler og grønt.
faq:
  - question: Tørre bøffer?
    answer: Træk ved 63 °C — mørbrad tørrer hurtigt over 68 °C.
  - question: Pande-version?
    answer: Se pande/tykke-moerbradboeffer-bloede-loeg — stegesky til sovs.
  - question: Grill?
    answer: Se moerbradboeffer-grill — samme kerne, røgsmag.
  - question: Tykkelse?
    answer: 2–3 cm optimalt — tyndere = kortere tid, tykkere = lavere temp.
body: |
  Mørbradbøffer i airfryer er festmad på hverdags-tid.

  Høj varme kort. Termometer. Hvile.

  Brun sovs laver du i gryden imens — eller brug pande-versionen for stegesky.
tip: Hvil bøfferne under løst folie — saften trækker tilbage, og skæring bliver rosa.
=====
title: Mørbradbøffer på grill
slug: moerbradboeffer-grill
category: grill
description: Mørbradbøffer på grill — saftige svinemørbrad med stegeskorpe og sommer-sovs tilbehør.
prepTime: PT10M
cookTime: PT10M
totalTime: PT20M
servings: 2
difficulty: nem
tags:
  - mørbradbøffer
  - mørbradbøffer grill
  - dansk klassiker
  - dansk-klassiker
  - grill
  - svinemørbrad
imageAlt: Mørbradbøffer fra grill med grillstriber
featured: false
ingredients:
  - 2 svinemørbradbøffer
  - Salt, peber, olie
  - Valgfrit: smør med hvidløg til finish
steps:
  - Tør bøffer. Salt, peber, olie. Grill medium-høj direkte varme.
  - 3–4 min per side til 63–65 °C. Smør hvidløg over ved hvile.
  - Hvil 5 min. Skær og server med kartofler og salat.
faq:
  - question: Hvilken kerne?
    answer: 63–65 °C for saftig mørbrad — dansk klassiker, ikke well done.
  - question: Airfryer i stedet?
    answer: Se airfryer/moerbradboeffer-airfryer — ingen røg, samme tid.
  - question: Flammer fra fedt?
    answer: Trim fedtkanter. Flyt til indirekte hvis flammer — mørbrad tåler ikke kul.
  - question: Marinade?
    answer: Salt og peber er nok — syre marinader gør mørbrad gråt hvis de står for længe.
body: |
  Mørbradbøffer på grill er dansk sommerfest på tallerken.

  Høj varme. Kort tid. Rosa kerne.

  Det er den ret der altid var der til konfirmation og grillaftener.
tip: Skær tynde fedtkanter — de flammer på grill og giver bitter smag.
=====
title: Æggekage i ovn
slug: aeggekage-ovn
category: ovn
description: Æggekage i ovn — fluffy dansk æggekage til mange i ovnfast form med bacon og purløg.
prepTime: PT15M
cookTime: PT25M
totalTime: PT40M
servings: 6
difficulty: nem
tags:
  - æggekage
  - æggekage ovn
  - dansk klassiker
  - dansk-klassiker
  - ovn
  - morgenmad
imageAlt: Fluffy æggekage fra ovn med bacon
featured: false
ingredients:
  - 8 æg
  - 2 dl mælk
  - 100 g bacon i tern
  - 1 bundt purløg, hakket
  - Salt, peber
  - 1 spsk smør til form
steps:
  - Tænd ovn 180 °C. Steg bacon sprødt i ovnfast form på blus — tag ud, behold fedt.
  - Pisk æg og mælk. Salt, peber, purløg. Hæld i form med bacon.
  - Bag 22–28 min til top fast og gylden — midten må gerne være let cremet.
  - Server med rugbrød eller brød.
faq:
  - question: Airfryer vs ovn?
    answer: Airfryer til 2–4 personer. Ovn til store forme og gæster.
  - question: Gummiagtig?
    answer: For mange æg uden mælk, eller for lav varme — 180 °C og korrekt ratio.
  - question: Uden bacon?
    answer: Ja — smør formen, brug champignon eller tomater i stedet.
  - question: Meal prep?
    answer: Holder 2 dage i køl — genopvarm 150 °C eller spis kold.
body: |
  Æggekage i ovn er morgenmad til seks uden at stå ved panden.

  Bacon i bunden. Æg og mælk. Ovn gør resten.

  Pande-versioner findes — her er portionen til familien.
tip: Varm formen med baconfedt før æg — mindre sticking, mere smag i skorpen.
=====
title: Tarteletter i ovn
slug: tarteletter-ovn
category: ovn
description: Tarteletter i ovn — sprøde tartelet-skaller varmet i ovn, fyldt med kylling og asparges.
prepTime: PT15M
cookTime: PT20M
totalTime: PT35M
servings: 4
difficulty: nem
tags:
  - tarteletter
  - tarteletter ovn
  - dansk klassiker
  - dansk-klassiker
  - ovn
  - festmad
imageAlt: Varme tarteletter med kylling og asparges
featured: false
ingredients:
  - 8–12 tartelet-skaller (købte)
  - 300 g kylling, i tern
  - 200 g asparges, i stykker
  - 2 dl fløde, 1 dl bouillon, 2 spsk mel, smør
  - Salt, peber, muskat
steps:
  - Varm skaller 160 °C i 5–8 min på bageplade — sprøde, ikke brune.
  - Steg kylling på blus. Asparges kort med. Lav hvid sovs af smør, mel, bouillon, fløde.
  - Fyld skaller lige før servering — ellers bliver de bløde.
faq:
  - question: Airfryer til skaller?
    answer: Se airfryer/tarteletter-hoens-asparges — hurtigere til få skaller.
  - question: Skaller bløde?
    answer: Fyld først ved bordet — væske i skaller = soggy tarteletter.
  - question: Rejer i stedet?
    answer: Klassisk variant — byt kylling med rejer til sidst.
  - question: Dagen før?
    answer: Fyld og sovs ja — varm adskilt. Skaller varmes frisk.
body: |
  Tarteletter i ovn er 80'er-festmad der stadig virker.

  Sprød skal. Varm fyld. Server med det samme.

  Det er timing — ikke teknik. Bløde skaller er den eneste synd.
tip: Stil skallerne op i muffinform — de holder formen når fyldet hældes i.
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
    src = IMG_MAP.get(slug, PUBLIC / "gryde" / "boller-i-karry.jpg")
    if not dest.exists() and src.exists():
        shutil.copy2(src, dest)
        print("image", dest.relative_to(PUBLIC.parent))
    elif not src.exists():
        print("warn: no src image for", slug)

print(f"done: {len(written)} recipes")
