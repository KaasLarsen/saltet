#!/usr/bin/env python3
"""15 virale airfryer-opskrifter (Hot Honey, rispapir, kød, grønt, baking) — nov 2026."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes/airfryer"
PUBLISHED = "2026-11-19"

RECIPES = [
    {
        "title": "Crispy Bang Bang Chicken Bites i airfryer",
        "slug": "crispy-bang-bang-chicken-bites",
        "description": "Crispy Bang Bang Chicken Bites i airfryer — kyllingetern i knuste cornflakes og cremet sød-stærk sriracha-mayo.",
        "prepTime": "PT15M",
        "cookTime": "PT14M",
        "totalTime": "PT29M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["kylling", "bang bang", "sriracha", "cornflakes", "snack", "party", "airfryer"],
        "imageAlt": "Sprøde Bang Bang chicken bites med cremet sriracha-mayo",
        "ingredients": [
            "600 g kyllingebryst, i 2–3 cm tern",
            "1 tsk salt, peber",
            "2 spsk majsstivelse",
            "1 æg",
            "80 g cornflakes, groft knust",
            "Olie-spray",
            "Sauce: 4 spsk mayonnaise, 2 spsk sriracha, 1 spsk honning, 1 tsk riseddike",
            "Forårsløg og sesam til servering",
        ],
        "steps": [
            "Tør kyllingen. Krydr med salt og peber. Vend i majsstivelse, derefter æg, til sidst knuste cornflakes. Press fast.",
            "Spray let med olie. Airfry 200 °C i 12–14 minutter. Vend halvvejs, til skorpen er dybt gylden og kernen 74 °C.",
            "Rør mayonnaise, sriracha, honning og eddike. Vend de varme bites i saucen — eller server den ved siden af, hvis du vil beholde maks knas.",
            "Forårsløg og sesam. Spis med det samme.",
        ],
        "faq": [
            {
                "question": "Cornflakes vs panko?",
                "answer": "Cornflakes giver den virale, knasende skorpe. Panko er finere — begge virker, men cornflakes er Bang Bang-sporet.",
            },
            {
                "question": "For stærkt?",
                "answer": "Halvér sriracha, behold honning. Saucen skal være sød-stærk, ikke brand.",
            },
            {
                "question": "Lårkød i stedet?",
                "answer": "Ja. Samme tid, mere saft. Tern i samme størrelse.",
            },
            {
                "question": "Saucen på før?",
                "answer": "Nej. Glaze til sidst — ellers bliver cornflakesne bløde.",
            },
        ],
        "body": """Bang Bang-bites er knas først, sauce sidst: cornflakes-skorpen skal være færdig, før sriracha-mayoen klæber.

  Cremet varme. Ikke friture. Airfryeren gør det party-klart.""",
        "tip": "Knus cornflakes med hænderne — ikke pulver. Store flager = krater-knas.",
    },
    {
        "title": "Bagt brie med Hot Honey, valnødder og rosmarin",
        "slug": "bagt-brie-hot-honey-valnoedder",
        "description": "Bagt brie i airfryer med Hot Honey, valnødder og rosmarin — boblende kerne, chili-honning og flagesalt.",
        "prepTime": "PT5M",
        "cookTime": "PT10M",
        "totalTime": "PT15M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["brie", "hot honey", "ost", "snack", "party", "forret", "airfryer"],
        "imageAlt": "Bagt brie med hot honey, valnødder og rosmarin",
        "ingredients": [
            "1 hel brie (ca. 200–250 g)",
            "2 spsk honning",
            "½–1 tsk chiliflager (eller 1 tsk chiliolie)",
            "30 g valnødder, groft hakket",
            "2 kviste frisk rosmarin",
            "Flagesalt",
            "Brød, kiks eller æbleskiver til dipping",
        ],
        "steps": [
            "Læg brien i en lille ovnfast form eller airfryer-egnet skål, der passer i kurven. Rid forsigtigt kryds i toppen af skorpen.",
            "Rør honning med chiliflager. Hæld over osten. Drys valnødder og pluk rosmarinblade ud over.",
            "Airfry 170 °C i 8–10 minutter, til midten er blød og bobler let under skorpen.",
            "Flagesalt. Server med det samme — dip brød i den smeltende kerne.",
        ],
        "faq": [
            {
                "question": "Hvad er Hot Honey?",
                "answer": "Honning med chili. Hjemmelavet: honning + chiliflager eller chiliolie. Klar på 10 sekunder.",
            },
            {
                "question": "Løber osten ud?",
                "answer": "Brug en lav skål med kant. Uden form flyder den gennem kurven.",
            },
            {
                "question": "Camembert i stedet?",
                "answer": "Ja. Samme tid. Camembert er ofte lidt mere jordagtig.",
            },
            {
                "question": "For stærkt?",
                "answer": "Start med ½ tsk chiliflager. Du kan altid dryppe mere honning ved bordet.",
            },
        ],
        "body": """Bagt brie med Hot Honey er party på 10 minutter: boblende kerne, chili-sødme, knasende nødder.

  Lav varme. Kort tid. Osten skal give efter for en ske — ikke være en pool.""",
        "tip": "Tag brien ud, når midten dirrer under skorpen. Den smelter videre 1 minut efter kurven.",
    },
    {
        "title": "Hot Honey Pork Belly Bites i airfryer",
        "slug": "hot-honey-pork-belly-bites",
        "description": "Hot Honey Pork Belly Bites i airfryer — sprøde svinebryst-tern med chili-honning og hvidløg på under 20 minutter.",
        "prepTime": "PT5M",
        "cookTime": "PT16M",
        "totalTime": "PT21M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["svinebryst", "pork belly", "hot honey", "snack", "party", "airfryer"],
        "imageAlt": "Sprøde pork belly bites med hot honey-glaze",
        "ingredients": [
            "600 g svinebryst uden knogler, i 2–3 cm tern",
            "1 tsk salt, peber",
            "1 tsk bagepulver (valgfrit, til ekstra knas)",
            "2 fed hvidløg, finthakket",
            "2 spsk honning",
            "1 tsk chiliflager eller 1 tsk sriracha",
            "1 tsk sojasauce",
            "Forårsløg til servering",
        ],
        "steps": [
            "Dup ternene tørre. Vend med salt, peber og bagepulver.",
            "Airfry 200 °C i 12 minutter. Vend. 3–4 minutter mere, til kanterne er dybt gyldne og sprøde.",
            "Rør honning, chili, soja og hvidløg. Vend de varme bites i glazen. 1–2 minutter mere, til det bobler og klæber.",
            "Forårsløg. Server med det samme.",
        ],
        "faq": [
            {
                "question": "For fedtet?",
                "answer": "Svinebryst er fedt — det er pointen. Dryp kurven undervejs, eller læg ternene på en rist-indsats.",
            },
            {
                "question": "Uden bagepulver?",
                "answer": "Ja. Bagepulver hæver pH og giver ekstra knas. Skip det, og giv 1–2 minutter mere.",
            },
            {
                "question": "Fra frost?",
                "answer": "Tø først. Våde tern damper i stedet for at brune.",
            },
            {
                "question": "Ovn?",
                "answer": "220 °C, 20–25 minutter. Glaze de sidste 5.",
            },
        ],
        "body": """Pork belly bites med Hot Honey er sticky streetfood uden dybstegning.

  Sprød kant først. Chili-honning til sidst — ellers brænder sukkeret.""",
        "tip": "Tern i ens størrelse. Små stykker brænder, store forbliver gummi midt i.",
    },
    {
        "title": "Crispy sushi-ruller i rispapir",
        "slug": "crispy-sushi-rolls-rispapir",
        "description": "Crispy sushi-ruller i rispapir i airfryer — laks, avokado og flødeost, penslet med olie og stegt sprøde.",
        "prepTime": "PT20M",
        "cookTime": "PT8M",
        "totalTime": "PT28M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": ["rispapir", "sushi", "laks", "snack", "airfryer", "party"],
        "imageAlt": "Sprøde rispapir-sushiruller med laks og avokado",
        "ingredients": [
            "8 ark rispapir (ca. 22 cm)",
            "150 g sushi-laks eller røget laks, i strimler",
            "1 avokado, i tynde skiver",
            "100 g flødeost",
            "½ agurk, i tynde stave (valgfrit)",
            "Olie til pensling",
            "Soja, wasabi eller sriracha-mayo til dipping",
        ],
        "steps": [
            "Blød ét rispapir 5–8 sekunder i lunkent vand, til det er smidigt men ikke pjasket. Læg på et fugtigt viskestykke.",
            "Spred en stribe flødeost midt på. Læg laks, avokado og agurk. Fold siderne ind, rull stramt som en forårsrulle.",
            "Pensl med olie. Airfry 190 °C i 6–8 minutter. Vend halvvejs, til papiret er boblende og gyldent.",
            "Skær diagonal. Server med soja eller sriracha-mayo.",
        ],
        "faq": [
            {
                "question": "Rispapiret flækker?",
                "answer": "For kort blødning, eller for tørt fyld-tryk. Blød lidt længere, rull strammere uden at presse luftbobler.",
            },
            {
                "question": "Uden rå laks?",
                "answer": "Røget laks, kogte rejer eller kun avokado/flødeost. Samme teknik.",
            },
            {
                "question": "Bliver de bløde?",
                "answer": "For meget vand i papiret, eller for lav varme. Pensl olie, 190 °C, plads i kurven.",
            },
            {
                "question": "Kan man forberede dem?",
                "answer": "Rul lige før stegning. Stående rispapir klistrer og tørrer ujævnt.",
            },
        ],
        "body": """Crispy sushi-ruller er rispapir møder airfryer: boblende skorpe uden dybstegning.

  Fyld sparsomt. Rull stramt. Olie er ikke valgfri — den giver farven.""",
        "tip": "Arbejd med ét ark ad gangen. Stablede våde ark klistrer uopretteligt.",
    },
    {
        "title": "Rispapir-pølsehorn i airfryer",
        "slug": "rispapir-poelsehorn",
        "description": "Rispapir-pølsehorn i airfryer — glutenfrit, ekstremt sprødt alternativ til klassiske pølsehorn med medister- eller kyllingefars.",
        "prepTime": "PT15M",
        "cookTime": "PT12M",
        "totalTime": "PT27M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["rispapir", "pølsehorn", "glutenfri", "medister", "snack", "airfryer"],
        "imageAlt": "Sprøde rispapir-pølsehorn fra airfryeren",
        "ingredients": [
            "8 ark rispapir",
            "400 g medisterfars eller krydret kyllingefars",
            "1 tsk salt, peber (hvis farsen er mild)",
            "½ tsk stødt fennikel eller paprika (valgfrit)",
            "Olie til pensling",
            "Sennep eller ketchup til servering",
        ],
        "steps": [
            "Del farsen i 8 pølseformede stænger (ca. 50 g).",
            "Blød ét rispapir kort i lunkent vand. Læg farsen på kanten, fold siderne ind, rull stramt.",
            "Pensl med olie. Airfry 190 °C i 10–12 minutter. Vend halvvejs, til papiret er knasende gyldent og farsen 74 °C.",
            "Server med sennep. Spis varme.",
        ],
        "faq": [
            {
                "question": "Glutenfri?",
                "answer": "Ja — rispapir er typisk kun ris og salt. Tjek pakken. Klassisk butterdej er hvede.",
            },
            {
                "question": "Farsen er rå midt i?",
                "answer": "For tykke stænger. Hold dem finger-tykke, eller giv 2–3 minutter mere.",
            },
            {
                "question": "Vegetarisk?",
                "answer": "Plantemedister eller krydret kikærtefars. Samme rulle-teknik.",
            },
            {
                "question": "Forskel på klassiske pølsehorn?",
                "answer": "Mere knas, mindre butterdej-smør. Se også [lynhurtige pølsehorn](/opskrifter/airfryer/poelsehorn) med færdig dej.",
            },
        ],
        "body": """Rispapir-pølsehorn er glutenfri knas uden butterdej: vådt ark, fars, olie, hed kurv.

  Stramt rul. Tynd fars. Papiret skal boble, ikke koge.""",
        "tip": "Dobbelt lag rispapir, hvis arkene er tynde — ekstra skorpe, mindre risiko for huller.",
    },
    {
        "title": "Kylling Kiev i airfryer",
        "slug": "kylling-kiev-airfryer",
        "description": "Kylling Kiev i airfryer — sprød panko omkring kyllingebryst med smeltende hvidløgs- og urtesmør uden friture.",
        "prepTime": "PT25M",
        "cookTime": "PT22M",
        "totalTime": "PT55M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": ["kylling", "kiev", "hvidløg", "smør", "panering", "airfryer"],
        "imageAlt": "Gennemskåret kylling Kiev med smeltende hvidløgssmør",
        "ingredients": [
            "4 kyllingebryster (ca. 150–180 g hver)",
            "80 g smør, blødt",
            "2 fed hvidløg, presset",
            "2 spsk hakket persille",
            "1 tsk citronskal, salt, peber",
            "Panering: 4 spsk mel, 2 æg, 100 g panko",
            "Olie-spray",
        ],
        "steps": [
            "Rør smør med hvidløg, persille, citronskal, salt og peber. Form 4 cylindre. Frys 20 minutter.",
            "Skær en lomme i hvert bryst fra den tykke ende. Skub et smør-cylinder ind. Luk med kød og eventuelt en tandstik. Krydr udenpå.",
            "Vend i mel, æg, panko. Press paneringen godt. Spray olie.",
            "Airfry 180 °C i 18–22 minutter, til skorpen er gylden og kernen 74 °C. Hvile 3 minutter før skæring — smørret skyder ellers ud.",
        ],
        "faq": [
            {
                "question": "Smørret løber ud?",
                "answer": "Lommen var ikke lukket, eller smørret var for blødt. Frys smørret hårdt, og sørg for at kødet lukker tæt.",
            },
            {
                "question": "Uden friture — bliver den sprød?",
                "answer": "Ja, med olie-spray og panko. Vend ikke for tidligt — lad skorpen sætte sig.",
            },
            {
                "question": "Kan man forberede dem?",
                "answer": "Panér og køl op til 4 timer, eller frys panerede. Fra frost: +5–7 minutter.",
            },
            {
                "question": "Lårkød?",
                "answer": "Sværere at lukke. Bryst er klassikeren til Kiev.",
            },
        ],
        "body": """Kylling Kiev i airfryer er smør-bombe med skorpe: hvidløgssmør indeni, panko udenpå, ingen oliekedel.

  Frys smørret. Luk lommen. Skær først efter hvile.""",
        "tip": "Bank brystet let fladt før lomme — mere overflade at lukke med, mindre risiko for læk.",
    },
    {
        "title": "Hvidløgs- og parmesan-kyllingeinderfilet",
        "slug": "hvidloeg-parmesan-kyllingeinderfilet",
        "description": "Hvidløgs- og parmesan-kyllingeinderfilet i airfryer — saftige tenders i brunet smør, hvidløg og lagret parmesan.",
        "prepTime": "PT10M",
        "cookTime": "PT12M",
        "totalTime": "PT22M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["kylling", "inderfilet", "parmesan", "hvidløg", "airfryer", "hverdag"],
        "imageAlt": "Gyldne kyllingeinderfileter med hvidløg og parmesan",
        "ingredients": [
            "600 g kyllingeinderfileter",
            "1 tsk salt, peber",
            "1 tsk hvidløgspulver",
            "½ tsk paprika",
            "40 g smør",
            "3 fed hvidløg, finthakket",
            "40 g friskrevet parmesan",
            "1 spsk hakket persille",
            "Olie-spray",
        ],
        "steps": [
            "Tør inderfileterne. Vend med salt, peber, hvidløgspulver og paprika. Spray let med olie.",
            "Airfry 190 °C i 8–10 minutter. Vend halvvejs, til kernen er 74 °C.",
            "Brun smørret på pande, til det dufter nøddeagtigt. Tag af varmen, rør hvidløg i (det må ikke brænde).",
            "Vend de varme tenders i smørret. Drys parmesan og persille over, så osten smelter let. Server med det samme.",
        ],
        "faq": [
            {
                "question": "Bryststrimler i stedet?",
                "answer": "Ja. Skær i samme tykkelse. Inderfilet er mere tilgivende og saftig.",
            },
            {
                "question": "Parmesan i kurven?",
                "answer": "Nej — den brænder. Ost efter stegning, i det varme smør.",
            },
            {
                "question": "Uden pande til smør?",
                "answer": "Smelt smør i en lille skål 1 minut i airfryeren ved 160 °C, rør hvidløg i udenfor.",
            },
            {
                "question": "Dip?",
                "answer": "Ranch, aioli eller bare citron. De er stærke nok alene.",
            },
        ],
        "body": """Garlic Parmesan tenders er brunet smør og ost på saftig inderfilet — ikke panering, bare glaze.

  Steg tørt. Smør efter. Parmesan til sidst.""",
        "tip": "Friskrevet parmesan smelter. Pose-revet ligger som sand ovenpå.",
    },
    {
        "title": "Porchetta-rulle af svineslag i airfryer",
        "slug": "porchetta-rulle-airfryer",
        "description": "Lille porchetta-rulle i airfryer — fennikelfrø, hvidløg og salvie, med garanteret sprøde svær fra blæseren.",
        "prepTime": "PT20M",
        "cookTime": "PT45M",
        "totalTime": "PT1H15M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": ["porchetta", "svineslag", "fennikel", "svær", "airfryer", "søndag"],
        "imageAlt": "Porchetta-rulle med sprøde svær fra airfryeren",
        "ingredients": [
            "800 g–1 kg svineslag med svær (udbenet, til rulle)",
            "2 tsk salt til sværen + 1 tsk til kødet",
            "2 tsk fennikelfrø, knust",
            "3 fed hvidløg, finthakket",
            "6–8 blade frisk salvie, hakket",
            "1 tsk peber",
            "1 spsk olivenolie",
            "Køkkengarn",
        ],
        "steps": [
            "Tør sværen grundigt. Rid den i tætte ruder uden at skære i kødet. Salt sværen generøst. Vend kødsiden op.",
            "Fordel olie, fennikel, hvidløg, salvie, salt og peber på kødet. Rull stramt med sværen udad. Bind med garn.",
            "Airfry 160 °C i 25 minutter. Skru op til 200 °C i 15–20 minutter mere, til sværen er boblende sprød og kernen ca. 70–72 °C.",
            "Hvile 10 minutter. Skær tykke skiver. Server med sennep eller salsa verde.",
        ],
        "faq": [
            {
                "question": "Sværen er sej?",
                "answer": "For våd eller for lav slutvarme. Dup tør, salt i forvejen, afslut hot. Se også fejlfinding for sej flæskesvær.",
            },
            {
                "question": "For stor til kurven?",
                "answer": "Bed slagteren om en lille rulle, eller del i to. Airfryeren skal have luft rundt om.",
            },
            {
                "question": "Uden fennikel?",
                "answer": "Porchetta smager af fennikel. Erstat med rosmarin + lidt anis, hvis du må.",
            },
            {
                "question": "Kan den laves dagen før?",
                "answer": "Rull og salt aftenen før. Tør svær i køleskab uden låg — ekstra knas næste dag.",
            },
        ],
        "body": """Porchetta i airfryer er lille rulle, stor svær: fennikel og salvie indeni, blæseren gør skorpen.

  Tør svær. Lav start. Hed finish.""",
        "tip": "Salt sværen aftenen før og lad den stå åbent i køleskabet — fugten er fjenden af knas.",
    },
    {
        "title": "Sprød paneret halloumi-burger med chilimayo",
        "slug": "halloumi-burger-chilimayo",
        "description": "Sprød paneret halloumi-burger i airfryer — tykke panko-skiver med sesam, chilimayo og maksimal knas.",
        "prepTime": "PT15M",
        "cookTime": "PT12M",
        "totalTime": "PT27M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["halloumi", "burger", "vegetar", "panko", "chili", "airfryer"],
        "imageAlt": "Paneret halloumi-burger med chilimayo og salat",
        "ingredients": [
            "400 g halloumi, i 4 tykke skiver (ca. 1,5 cm)",
            "Panering: 3 spsk mel, 1 æg, 80 g panko blandet med 2 spsk sesamfrø",
            "Olie-spray",
            "Chilimayo: 4 spsk mayonnaise, 1–2 tsk sriracha eller chiliolie, ½ tsk citronsaft",
            "4 burgerboller",
            "Salat, tomat, rødløg",
        ],
        "steps": [
            "Dup halloumi tør. Vend i mel, æg, panko-sesam. Press fast. Spray olie.",
            "Airfry 190 °C i 10–12 minutter. Vend halvvejs, til skorpen er dybt gylden.",
            "Rør chilimayo. Rist bollerne 2 minutter i kurven, hvis du vil.",
            "Samling: bolle, salat, halloumi, chilimayo, tomat, løg. Spis med det samme.",
        ],
        "faq": [
            {
                "question": "Halloumi bliver gummi?",
                "answer": "For tynd skive eller for lang tid. Hold 1,5 cm og stop, når paneringen er gylden — osten er færdig, når midten er blød.",
            },
            {
                "question": "Uden gluten?",
                "answer": "Majsstivelse + glutenfri rasp/panko. Samme teknik.",
            },
            {
                "question": "Kun halloumi uden bolle?",
                "answer": "Ja — som tenders med chilimayo-dip.",
            },
            {
                "question": "Paneringen falder af?",
                "answer": "Dup tør, press panko hårdt, spray olie. Se fejlfinding for panering i airfryer.",
            },
        ],
        "body": """Paneret halloumi-burger er vegetar med knas: tyk skive, sesam-panko, chilimayo.

  Halloumi skal brune, ikke koge. Panering holder formen.""",
        "tip": "Køl de panerede skiver 10 minutter før airfry — paneringen sætter sig bedre.",
    },
    {
        "title": "Honning- og sesamglaserede blomkåls-wings",
        "slug": "honning-sesam-blomkaalswings",
        "description": "Honning- og sesamglaserede blomkåls-wings i airfryer — pankopanerede buketter i klistret honning-soja-ingefær-glaze.",
        "prepTime": "PT15M",
        "cookTime": "PT18M",
        "totalTime": "PT33M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["blomkål", "vegetar", "wings", "honning", "sesam", "airfryer", "snack"],
        "imageAlt": "Glaserede blomkåls-wings med sesam",
        "ingredients": [
            "1 stor blomkål, i wing-store buketter",
            "Panering: 50 g mel, 1 dl plante- eller komælk, 80 g panko, ½ tsk salt, ½ tsk paprika",
            "Olie-spray",
            "Glaze: 3 spsk honning, 2 spsk sojasauce, 1 tsk frisk ingefær, 1 fed hvidløg, 1 tsk sesamolie",
            "Sesamfrø og forårsløg",
        ],
        "steps": [
            "Vend buketter i mel, mælk, derefter krydret panko. Spray olie.",
            "Airfry 200 °C i 14–16 minutter. Vend halvvejs, til skorpen er gylden og blomkålen mør.",
            "Varm glaze 1 minut på pande eller i skål, til den trækker. Vend wings i glazen. 2 minutter mere i kurven.",
            "Sesam og forårsløg. Server varme.",
        ],
        "faq": [
            {
                "question": "Sødt eller stærkt?",
                "answer": "Basis er sticky-sød. Tilføj sriracha i glazen, hvis du vil have heat.",
            },
            {
                "question": "Uden panering?",
                "answer": "Muligt, men knaset forsvinder. Spray olie direkte på buketter + glaze — mere soft-wing.",
            },
            {
                "question": "Frosne buketter?",
                "answer": "Tø og dup tør først. Våd blomkål = slatten panko.",
            },
            {
                "question": "Dip?",
                "answer": "Yoghurt-ranch eller ekstra glaze. De er allerede sticky.",
            },
        ],
        "body": """Blomkåls-wings er vegetar-streetfood: panko-knas, honning-soja der klæber, sesam på toppen.

  Steg tørt. Glaze til sidst.""",
        "tip": "Skær buketterne ens — for store er rå midt i, for små brænder paneringen.",
    },
    {
        "title": "Hasselback-tofu med chili- og hvidløgsolie",
        "slug": "hasselback-tofu-chili-hvidloegsolie",
        "description": "Hasselback-tofu i airfryer — tætte lameller for sprøde kanter og blød midte, overøst med sydende chili-hvidløgsolie.",
        "prepTime": "PT15M",
        "cookTime": "PT20M",
        "totalTime": "PT35M",
        "servings": 3,
        "difficulty": "mellem",
        "tags": ["tofu", "hasselback", "chili", "hvidløg", "vegetar", "airfryer", "vegan"],
        "imageAlt": "Hasselback-skåret tofu med chili-hvidløgsolie",
        "ingredients": [
            "400 g fast tofu, godt presset",
            "1 spsk soja",
            "1 tsk majsstivelse",
            "Olie-spray",
            "Chili-hvidløgsolie: 3 spsk olie, 3 fed hvidløg i skiver, 1 tsk chiliflager, ½ tsk sukker, 1 knivspids salt",
            "Forårsløg og sesam",
        ],
        "steps": [
            "Pres tofu 10–15 minutter. Skær i 2–3 blokke. Læg spisepinde langs siderne og skær tætte lameller næsten igennem (hasselback).",
            "Pensl soja ned i snittene. Drys majsstivelse let over. Spray olie.",
            "Airfry 190 °C i 16–20 minutter, til kanterne er dybt gyldne og sprøde.",
            "Varm olie med hvidløg og chiliflager, til hvidløget er gyldent. Sukker og salt i. Hæld over tofu. Forårsløg og sesam.",
        ],
        "faq": [
            {
                "question": "Silketofu?",
                "answer": "Nej. Kun fast eller ekstra fast — ellers falder den sammen.",
            },
            {
                "question": "Skærer jeg igennem?",
                "answer": "Stop 5 mm fra bunden. Spisepinde som stop er trikset.",
            },
            {
                "question": "Uden chili?",
                "answer": "Kun hvidløgsolie + sesam. Stadig god.",
            },
            {
                "question": "Mere protein-knas?",
                "answer": "Se også [sprødbagt tofu i soya-sesam](/opskrifter/airfryer/sproed-tofu-soya-sesam).",
            },
        ],
        "body": """Hasselback-tofu er maksimal overflade: sprøde flager yderst, blød kerne, olie der syder ned i snittene.

  Pres tofuen. Skær tæt. Olie til sidst.""",
        "tip": "Jo tørrere tofu før snit, desto mere knas. Press længere end du tror.",
    },
    {
        "title": "Sprøde gyoza med sesam-ponzu",
        "slug": "sproede-gyoza-sesam-ponzu",
        "description": "Sprøde gyoza og dumplings i airfryer — direkte fra frost eller køl med pandesprød bund og sesam-ponzu.",
        "prepTime": "PT5M",
        "cookTime": "PT12M",
        "totalTime": "PT17M",
        "servings": 3,
        "difficulty": "nem",
        "tags": ["gyoza", "dumplings", "snack", "asiatisk", "airfryer", "frost"],
        "imageAlt": "Sprøde gyoza med sesam-ponzu dip",
        "ingredients": [
            "12–16 gyoza eller dumplings (frost eller køl)",
            "Olie-spray",
            "1–2 spsk vand til damp-start (valgfrit)",
            "Ponzu-dip: 3 spsk ponzu eller soja + citron, 1 tsk riseddike, 1 tsk sesamolie, 1 tsk sesamfrø",
            "Chiliolie efter smag",
        ],
        "steps": [
            "Spray kurven og gyoza let med olie. Stil dem med plads — ikke stablet.",
            "Airfry 180 °C i 8 minutter. Vend eller ryst. 3–4 minutter mere, til undersiden er gylden og fyldet er hot.",
            "Valgfrit damp-trick: de første 3 minutter med 1 spsk vand i bunden under en rist, derefter tørt til knas.",
            "Rør ponzu-dip. Server gyoza med dip og chiliolie.",
        ],
        "faq": [
            {
                "question": "Fra frost uden optøning?",
                "answer": "Ja. +2–3 minutter. Spray olie, så skindet ikke tørrer ud.",
            },
            {
                "question": "Hjemmelavede gyoza?",
                "answer": "Ja — se [gyoza på pande](/opskrifter/pande/gyoza-pande) for fyld, airfry færdiggøringen her.",
            },
            {
                "question": "Bliver bunden sprød som på panden?",
                "answer": "Tæt på. Olie på bunden + høj varme. Ren damp uden olie giver bløde skind.",
            },
            {
                "question": "Uden ponzu?",
                "answer": "Soja + lime + sesamolie. Samme umami.",
            },
        ],
        "body": """Gyoza i airfryer er frost-hack med pandeknas: olie, plads, vend én gang.

  Ingen gryde. Dip ved siden af.""",
        "tip": "Læg dem på siden eller med den flade bund ned — den flade flade er der, knaset skal lande.",
    },
    {
        "title": "Sprød paneret tortellini med marinara-dip",
        "slug": "paneret-tortellini-marinara",
        "description": "Sprød paneret tortellini i airfryer — friske ricotta-spinat-tortellini i panko og parmesan med varm marinara.",
        "prepTime": "PT15M",
        "cookTime": "PT10M",
        "totalTime": "PT25M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["tortellini", "pasta", "snack", "forret", "panko", "airfryer", "party"],
        "imageAlt": "Panerede tortellini med marinara-dip",
        "ingredients": [
            "300 g friske tortellini (ricotta-spinat eller ost)",
            "Panering: 4 spsk mel, 2 æg, 80 g panko + 30 g parmesan",
            "Olie-spray",
            "Marinara: 2 dl passata, 1 fed hvidløg, 1 tsk olivenolie, salt, oregano, peber",
            "Frisk basilikum (valgfrit)",
        ],
        "steps": [
            "Kog tortellini 1–2 minutter kortere end pakken (de skal holde formen). Dryp og køl 2 minutter.",
            "Vend i mel, æg, panko-parmesan. Spray olie.",
            "Airfry 190 °C i 8–10 minutter. Vend halvvejs, til skorpen er gylden.",
            "Varm marinara med hvidløg og oregano 3–4 minutter. Server tortellini med varm dip.",
        ],
        "faq": [
            {
                "question": "Tørrede tortellini?",
                "answer": "Kog dem først al dente. Friske er nemmere at panere uden at de springer.",
            },
            {
                "question": "Uden forkogning?",
                "answer": "Friske kan gå direkte i panering, men midten kan blive sej. Kort forkog er sikrest.",
            },
            {
                "question": "Dip færdig fra glas?",
                "answer": "Ja. Varm den. Hjemmelavet passata smager renere.",
            },
            {
                "question": "Mager variant?",
                "answer": "Spray sparsomt og brug magre tortellini — knaset kræver stadig olie på panko.",
            },
        ],
        "body": """Paneret tortellini er forret-snack: pasta-hapser med osteskorpe og rød dip.

  Kort kog. Tør overflade. Hed kurv.""",
        "tip": "Dup tortellini tørre efter kog — våd pasta smider paneringen.",
    },
    {
        "title": "Sicilianske aubergine-kødboller med ostekerne",
        "slug": "sicilianske-aubergine-koedboller",
        "description": "Sicilianske aubergine-kødboller i airfryer — bagt aubergine med pecorino og rasp omkring en smeltende mozzarella-kerne.",
        "prepTime": "PT25M",
        "cookTime": "PT18M",
        "totalTime": "PT50M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": ["aubergine", "vegetar", "kødboller", "mozzarella", "siciliansk", "airfryer"],
        "imageAlt": "Aubergine-kødboller med smeltende ostekerne",
        "ingredients": [
            "2 mellemstore auberginer (ca. 600 g)",
            "80 g rasp eller panko",
            "50 g pecorino eller parmesan, reven",
            "1 æg",
            "1 fed hvidløg, presset",
            "2 spsk hakket basilikum eller persille",
            "Salt, peber",
            "100 g mozzarella eller scamorza, i 12 små tern",
            "Olie-spray",
            "Marinara eller tomatsauce til servering",
        ],
        "steps": [
            "Prikk auberginerne. Airfry 200 °C i 15–20 minutter, til de er møre. Køl, skræl, hak kødet fint. Pres overskydende væske ud i et viskestykke.",
            "Rør aubergine med rasp, pecorino, æg, hvidløg, urter, salt og peber. Massen skal forme sig — tilsæt rasp hvis den er våd.",
            "Form 12 boller. Tryk en ostetern ind i midten og luk tæt. Spray olie.",
            "Airfry 190 °C i 12–15 minutter. Vend halvvejs, til de er gyldne. Server med varm tomatsauce.",
        ],
        "faq": [
            {
                "question": "Bollerne falder fra hinanden?",
                "answer": "For våd aubergine. Pres hårdere, tilsæt mere rasp, og køl massen 10 minutter før formning.",
            },
            {
                "question": "Uden æg?",
                "answer": "1 spsk chia + 3 spsk vand, eller ekstra rasp og pecorino. Lidt mere skrøbeligt.",
            },
            {
                "question": "Scamorza vs mozzarella?",
                "answer": "Scamorza smelter mindre løbende og smager røget. Mozzarella giver den klassiske tråd.",
            },
            {
                "question": "Kan de fryses?",
                "answer": "Ja, efter stegning. Genopvarm 160 °C i 8–10 minutter.",
            },
        ],
        "body": """Sicilianske aubergine-kødboller er kødfri umami med ostebombe i midten.

  Pres auberginen tør. Luk osten tæt. Airfry til skorpe.""",
        "tip": "Pres aubergine-kødet som var det hakkekød til frikadeller — væske er den største fejl.",
    },
    {
        "title": "Chokoladefondant i airfryer",
        "slug": "chokoladefondant-airfryer",
        "description": "Chokoladefondant i airfryer — portionsanrettede lava cakes i ramekiner på ca. 10 minutter med flagesalt på toppen.",
        "prepTime": "PT15M",
        "cookTime": "PT10M",
        "totalTime": "PT35M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": ["chokoladefondant", "dessert", "chokolade", "airfryer", "lava cake"],
        "imageAlt": "Chokoladefondant fra airfryer med flydende midte og flagesalt",
        "ingredients": [
            "100 g mørk chokolade (70 %)",
            "100 g smør + smør til formene",
            "2 æg + 2 æggeblommer",
            "80 g sukker",
            "40 g hvedemel",
            "1 knivspids salt",
            "Kakao til formene",
            "Flagesalt til topping",
            "Vaniljeis eller bær til servering",
        ],
        "steps": [
            "Smør 4 ramekiner (á ca. 1–1,5 dl). Kakao i, bank overskuddet af. Stil koldt.",
            "Smelt chokolade og smør. Køl lidt. Pisk æg, blommer og sukker lyse. Rør chokoladen i. Fold mel og salt i.",
            "Fordel i formene. Køl 15–20 minutter.",
            "Airfry 180 °C i 8–10 minutter, til kanten er sat og midten stadig dirrer. Flagesalt. Server med det samme — is ved siden af.",
        ],
        "faq": [
            {
                "question": "Fast i midten?",
                "answer": "For lang tid. Start med 8 minutter. Airfryere varierer — notér dit minut.",
            },
            {
                "question": "Forskel på ovn-versionen?",
                "answer": "Samme dej. Airfryer er typisk 180 °C og 1–2 minutter kortere end [ovn-fondanten](/opskrifter/ovn/chokoladefondant).",
            },
            {
                "question": "Metalforme?",
                "answer": "Ja, hvis de passer i kurven. Keramik holder varmen godt. Undgå tynd plast.",
            },
            {
                "question": "Fra frost?",
                "answer": "Bag i formene fra frost 11–13 minutter ved 180 °C.",
            },
        ],
        "body": """Chokoladefondant i airfryer er lava cake uden at tænde ovnen: kold dej, hed kurv, flagesalt på skorpen.

  Kanten sat. Midten flydende. Et minut for meget er brownie.""",
        "tip": "Bag én test-ramekin først, hvis din airfryer er ny for dig. Notér sekundet — resten rammer midten.",
    },
]


def yaml_str(s: str) -> str:
    if any(c in s for c in ':#"\'\n') or s.startswith(("-", "?", "[", "{", "*", "&", "!", "|", ">", "%", "@", "`")):
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return '"' + s + '"'


def dump_list(items: list[str], indent: int = 2) -> str:
    pad = " " * indent
    return "\n".join(f'{pad}- {yaml_str(i)}' for i in items)


def dump_faq(faq: list[dict], indent: int = 2) -> str:
    pad = " " * indent
    blocks = []
    for f in faq:
        blocks.append(f"{pad}- question: {yaml_str(f['question'])}\n{pad}  answer: {yaml_str(f['answer'])}")
    return "\n".join(blocks)


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    for r in RECIPES:
        path = ROOT / f"{r['slug']}.mdx"
        content = f"""---
title: {yaml_str(r['title'])}
slug: {r['slug']}
category: airfryer
description: {yaml_str(r['description'])}
prepTime: "{r['prepTime']}"
cookTime: "{r['cookTime']}"
totalTime: "{r['totalTime']}"
servings: {r['servings']}
difficulty: {r['difficulty']}
tags:
{dump_list(r['tags'])}
image: /recipes/airfryer/{r['slug']}.jpg
imageAlt: {yaml_str(r['imageAlt'])}
publishedAt: {PUBLISHED}
featured: true
ingredients:
{dump_list(r['ingredients'])}
steps:
{dump_list(r['steps'])}
faq:
{dump_faq(r['faq'])}
---

{r['body']}

<Tip>
{r['tip']}
</Tip>
"""
        path.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"Wrote {path.relative_to(path.parents[2])}")


if __name__ == "__main__":
    main()
