#!/usr/bin/env python3
"""15 airfryer-opskrifter batch 21–40 (miso, crispy rice, elotes, baking) — nov 2026."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes/airfryer"
PUBLISHED = "2026-11-19"

RECIPES = [
    {
        "title": "Crispy Rice Bites med spicy laks",
        "slug": "crispy-rice-bites-spicy-laks",
        "description": "Crispy Rice Bites i airfryer — sammenpressede sushiris-firkanter som croutoner, toppet med spicy laks-tatar.",
        "prepTime": "PT20M",
        "cookTime": "PT14M",
        "totalTime": "PT50M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": ["crispy rice", "laks", "sushi", "snack", "party", "airfryer"],
        "imageAlt": "Sprøde crispy rice bites med spicy laks på toppen",
        "ingredients": [
            "400 g kogt sushiris (afkølet, klæbrig)",
            "1 spsk riseddike, ½ tsk salt, ½ tsk sukker",
            "Olie-spray",
            "Topping: 200 g sushi-laks eller røget laks, finthakket",
            "2 spsk mayonnaise, 1–2 tsk sriracha, 1 tsk sojasauce",
            "Forårsløg, sesam, lime",
        ],
        "steps": [
            "Rør riseddike, salt og sukker i det kolde ris. Press i et tyndt lag (ca. 1,5 cm) i en bakke beklædt med film. Køl 20–30 minutter.",
            "Skær i firkanter (ca. 4×4 cm). Spray begge sider med olie.",
            "Airfry 200 °C i 12–14 minutter. Vend halvvejs, til siderne er dybt gyldne og knasende som croutoner.",
            "Rør laks med mayo, sriracha og soja. Top hver bite. Forårsløg, sesam, lime. Spis med det samme.",
        ],
        "faq": [
            {
                "question": "Tun i stedet for laks?",
                "answer": "Ja — samme spicy mayo. Brug sushi-kvalitet eller godt røget.",
            },
            {
                "question": "Risene falder fra hinanden?",
                "answer": "For tørt ris eller for tykt lag. Brug klæbrigt sushiris, press hårdt, køl før skæring.",
            },
            {
                "question": "Røræg i stedet for tatar?",
                "answer": "Klassisk brunch-twist. Blødkogt røræg + chiliolie på de varme bites.",
            },
            {
                "question": "Fra rester?",
                "answer": "Ja — gårsdagens sushiris er ofte bedre. Lidt mere eddike, hvis det er tørt.",
            },
        ],
        "body": """Crispy Rice Bites er sushiris møder crouton: press, køl, airfry hot, top med spicy tatar.

  Knaset er i risen. Topping er kold og cremet.""",
        "tip": "Press risen hårdere end du tror. Løst ris = smuldrende firkanter i kurven.",
    },
    {
        "title": "Miso- og ahornglaseret aubergine (Nasu Dengaku)",
        "slug": "miso-ahorn-aubergine-nasu-dengaku",
        "description": "Nasu Dengaku i airfryer — halverede auberginer med ridsede tern og sød hvid miso-ahorn-glaze til karamelliserede kanter.",
        "prepTime": "PT10M",
        "cookTime": "PT18M",
        "totalTime": "PT28M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["aubergine", "miso", "nasu dengaku", "vegetar", "japansk", "airfryer"],
        "imageAlt": "Miso-glaseret aubergine med karamelliserede kanter",
        "ingredients": [
            "2 mellemstore auberginer",
            "1 spsk olie",
            "Glaze: 3 spsk hvid miso (shiro), 2 spsk ahornsirop eller honning, 1 spsk mirin, 1 tsk sojasauce, 1 tsk sesamolie",
            "Sesamfrø og forårsløg",
        ],
        "steps": [
            "Halvér auberginerne på langs. Rid kødet i 1 cm tern uden at skære gennem skindet. Pensl med olie.",
            "Airfry 190 °C i 12 minutter, til kødet er mørt og kanterne begynder at brune.",
            "Rør glaze. Pensl generøst ned i ridserne. 5–6 minutter mere, til glazen bobler og karamelliserer.",
            "Sesam og forårsløg. Server varme.",
        ],
        "faq": [
            {
                "question": "Rød miso i stedet?",
                "answer": "Den er saltigere og kraftigere. Brug halv dosis, eller bland med hvid miso.",
            },
            {
                "question": "Bitter aubergine?",
                "answer": "Salt ridserne 10 minutter, skyl og dup tør før olie — eller vælg mindre, friske frugter.",
            },
            {
                "question": "Uden mirin?",
                "answer": "1 spsk riseddike + ½ tsk sukker. Glazen skal være sød-salt.",
            },
            {
                "question": "Tilbehør?",
                "answer": "Ris, agurkesalat eller som side til miso-laks.",
            },
        ],
        "body": """Nasu Dengaku er miso der karamelliserer i ridserne: mør aubergine, blank glaze, sesam på toppen.

  Rid dybt. Glaze sent. Kanterne skal næsten brænde.""",
        "tip": "Jo dybere ridser, desto mere glaze — og desto mere knasende karamel på kanterne.",
    },
    {
        "title": "Sprød paneret feta med Hot Honey og sesam",
        "slug": "paneret-feta-hot-honey-sesam",
        "description": "Sprød paneret feta i airfryer — hel blok i æg, panko og sesam, bagt til skorpe med blød midte og Hot Honey.",
        "prepTime": "PT10M",
        "cookTime": "PT12M",
        "totalTime": "PT22M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["feta", "hot honey", "panering", "snack", "forret", "vegetar", "airfryer"],
        "imageAlt": "Paneret feta med hot honey og sesam",
        "ingredients": [
            "1 blok feta (ca. 200 g), gerne i 2 tykke skiver",
            "Panering: 3 spsk mel, 1 æg, 60 g panko + 2 spsk sesamfrø",
            "Olie-spray",
            "Hot Honey: 2 spsk honning + ½–1 tsk chiliflager",
            "Flagesalt, frisk oregano eller timian",
        ],
        "steps": [
            "Dup feta tør. Vend i mel, æg, panko-sesam. Press paneringen godt. Spray olie.",
            "Airfry 190 °C i 10–12 minutter. Vend forsigtigt halvvejs, til skorpen er dybt gylden.",
            "Rør honning med chiliflager. Dryp over den varme feta. Flagesalt og urter.",
            "Server med det samme — midten skal være varm og blød.",
        ],
        "faq": [
            {
                "question": "Fetaen løber ud?",
                "answer": "For tynd skive eller for høj varme. Hold tykke stykker og 190 °C. Paneringen er diget.",
            },
            {
                "question": "Pande-version?",
                "answer": "Se [paneret feta med honning og sesam](/opskrifter/pande/paneret-feta-honning-sesam). Her er Hot Honey-sporet.",
            },
            {
                "question": "Halloumi i stedet?",
                "answer": "Ja — se også [halloumi-burger med chilimayo](/opskrifter/airfryer/halloumi-burger-chilimayo).",
            },
            {
                "question": "Tilbehør?",
                "answer": "Salat, tomater, brød. Eller bare ske og Hot Honey.",
            },
        ],
        "body": """Paneret feta med Hot Honey er forret på 12 minutter: knas udenpå, smelt indenfor, chili-sødme ovenpå.

  Dup tør. Press panko. Honning til sidst.""",
        "tip": "Køl den panerede feta 10 minutter før airfry — skorpen sætter sig og flager mindre.",
    },
    {
        "title": "Miso- og brunet smør-gulerødder",
        "slug": "miso-brunet-smoer-guleroedder",
        "description": "Karamelliserede miso- og brunet smør-gulerødder i airfryer — spæde gulerødder med ekstrem umami og sprøde spidser.",
        "prepTime": "PT10M",
        "cookTime": "PT18M",
        "totalTime": "PT28M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["gulerødder", "miso", "brunet smør", "tilbehør", "vegetar", "airfryer"],
        "imageAlt": "Gulerødder med miso og brunet smør",
        "ingredients": [
            "600 g spæde gulerødder (eller almindelige i stave)",
            "40 g smør",
            "1 spsk hvid miso",
            "1 tsk honning eller ahornsirop",
            "Peber, flagesalt",
            "Frisk timian eller persille",
        ],
        "steps": [
            "Brun smørret på pande, til det dufter nøddeagtigt. Tag af varmen, rør miso og honning i til en blank glaze.",
            "Vend gulerødderne i glazen. Læg i kurven i ét lag.",
            "Airfry 190 °C i 14–18 minutter. Vend halvvejs, til spidserne er karamelliserede og midten mør.",
            "Flagesalt, peber, urter. Server varme.",
        ],
        "faq": [
            {
                "question": "Store gulerødder?",
                "answer": "Skær i halve eller stave. Ens tykkelse = ens tid.",
            },
            {
                "question": "Uden miso?",
                "answer": "Kun brunet smør + honning virker — men umamien mangler. 1 tsk soja er nødplan.",
            },
            {
                "question": "Vegan?",
                "answer": "Brun plantebaseret smør eller olivenolie + miso. Nøddeagtigheden bliver mildere.",
            },
            {
                "question": "Til hvad?",
                "answer": "Kylling, laks, halloumi eller bare ris.",
            },
        ],
        "body": """Miso-brunet smør-gulerødder er tilbehør der stjæler tallerkener: nøddeagtigt smør, salt-sød miso, sprøde spidser.

  Brun smørret først. Vend. Hed kurv.""",
        "tip": "Miso klumper i koldt smør. Rør den i, mens smørret stadig er flydende og varmt.",
    },
    {
        "title": "Elotes — mexicanske majskolber i airfryer",
        "slug": "elotes-majskolber-airfryer",
        "description": "Elotes i airfryer — majskolber med ristede kerner, chipotle-mayo, feta, lime og koriander.",
        "prepTime": "PT5M",
        "cookTime": "PT14M",
        "totalTime": "PT19M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["elotes", "majskolber", "mexicansk", "snack", "grillmad", "airfryer"],
        "imageAlt": "Elotes majskolber med chipotle-mayo og feta",
        "ingredients": [
            "4 majskolber, renset",
            "1 spsk olie",
            "Chipotle-mayo: 4 spsk mayonnaise, 1–2 tsk chipotle i adobo eller røget paprika + chili, 1 tsk limejuice",
            "60 g smuldret feta eller cotija",
            "Frisk koriander, limebåde, chiliflager",
        ],
        "steps": [
            "Pensl kolberne med olie. Airfry 200 °C i 12–14 minutter. Vend halvvejs, til kernerne er ristede og enkelte er mørke.",
            "Rør chipotle-mayo. Smør de varme kolber generøst.",
            "Drys feta, koriander og chiliflager. Lime over. Spis med det samme.",
        ],
        "faq": [
            {
                "question": "Forskel på majskolber med urtesmør?",
                "answer": "Urtesmør er dansk side. Elotes er streetfood: mayo, chili, ost, lime. Se også [majskolber med urtesmør](/opskrifter/airfryer/majskolber-urtesmoer).",
            },
            {
                "question": "Uden chipotle?",
                "answer": "Røget paprika + sriracha i mayoen. Røgen er vigtig.",
            },
            {
                "question": "Frosne kolber?",
                "answer": "Ja — +2–3 minutter. Dup overfladen, så olien klæber.",
            },
            {
                "question": "Cotija?",
                "answer": "Klassisk. Feta er den danske stand-in — salt og smuld.",
            },
        ],
        "body": """Elotes i airfryer er mexicansk street corn uden grill: ristede kerner, cremet varme, lime der klipper igennem.

  Steg tørt. Smør efter. Ost ovenpå.""",
        "tip": "Lad enkelte kerner blive mørke — det er char, ikke fejl.",
    },
    {
        "title": "Rispapir-chips med edamame-hummus",
        "slug": "rispapir-chips-edamame-hummus",
        "description": "Rispapir-chips i airfryer — trekanter klar på ca. 3 minutter til luftige, knasende snacks med edamame-hummus.",
        "prepTime": "PT10M",
        "cookTime": "PT3M",
        "totalTime": "PT13M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["rispapir", "chips", "edamame", "hummus", "snack", "airfryer", "glutenfri"],
        "imageAlt": "Sprøde rispapir-chips med edamame-hummus",
        "ingredients": [
            "6–8 ark rispapir",
            "Olie-spray",
            "Flagesalt, valgfrit: sesam, chiliflager",
            "Edamame-hummus: 200 g edamame (kogt), 1 spsk tahin, 1 spsk citron, 1 fed hvidløg, 2 spsk olie, salt — eller færdig [edamame-hummus](/opskrifter/dips/edamame-hummus)",
        ],
        "steps": [
            "Klip eller bræk rispapir i trekanter (tørt — ikke blødt i vand).",
            "Læg i ét lag i kurven. Spray let med olie. Drys salt.",
            "Airfry 180 °C i 2–4 minutter. Hold øje — de bruner på sekunder. Vend eller ryst efter 2 minutter.",
            "Blend edamame-hummus, hvis du laver den frisk. Server chips varme med dip.",
        ],
        "faq": [
            {
                "question": "Brænder hurtigt?",
                "answer": "Ja. Start med 2 minutter. De går fra hvid til brun på et øjeblik.",
            },
            {
                "question": "Skal de blødes?",
                "answer": "Nej. Tørt rispapir = chips. Vådt = wraps (sushi-ruller, pølsehorn).",
            },
            {
                "question": "Uden hummus?",
                "answer": "Guacamole, tzatziki eller bare chili-salt. Chipsene står alene.",
            },
            {
                "question": "Holder de?",
                "answer": "Lufttæt dåse samme dag. Fugtig luft gør dem slappe — genopvarm 1 minut.",
            },
        ],
        "body": """Rispapir-chips er snack på 3 minutter: tørt ark, olie, hed kurv, knas som rejechips.

  Ikke blød. Hold øje. Dip ved siden af.""",
        "tip": "Ét lag. Stablede ark klistrer og bruner ujævnt.",
    },
    {
        "title": "Miso-glaseret laks med sesamskorpe",
        "slug": "miso-glaseret-laks-sesam",
        "description": "Miso-glaseret laks i airfryer — fileter i hvid miso, mirin og ingefær på ca. 8 minutter med karamelliseret sesamskorpe.",
        "prepTime": "PT10M",
        "cookTime": "PT8M",
        "totalTime": "PT25M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["laks", "miso", "sesam", "fisk", "hverdag", "airfryer"],
        "imageAlt": "Miso-glaseret laks med sesamskorpe",
        "ingredients": [
            "4 laksefileter (á ca. 150 g)",
            "Marinade: 2 spsk hvid miso, 1 spsk mirin, 1 spsk sojasauce, 1 tsk frisk ingefær, 1 tsk honning",
            "2 spsk sesamfrø",
            "Olie-spray, forårsløg, lime",
        ],
        "steps": [
            "Rør marinade. Pensl laksen. Mariner 10–15 minutter (ikke meget længere — miso er salt).",
            "Drys sesam på oversiden. Spray let med olie.",
            "Airfry 180 °C i 7–9 minutter, til overfladen er karamelliseret og kernen stadig saftig (ca. 50–52 °C for rosa).",
            "Forårsløg og lime. Server med det samme.",
        ],
        "faq": [
            {
                "question": "Forskel på teriyaki-laks?",
                "answer": "Teriyaki er soja-sød. Miso er dybere umami. Se også [crispy skin laks teriyaki](/opskrifter/airfryer/crispy-skin-laks-teriyaki).",
            },
            {
                "question": "Med skind?",
                "answer": "Ja — skind ned først 3 minutter, vend, glaze-side op resten. Skindet bliver sprødere.",
            },
            {
                "question": "For salt?",
                "answer": "Halvér soja, behold miso og mirin. Eller kort marinade.",
            },
            {
                "question": "Tilbehør?",
                "answer": "Ris, nasu dengaku-aubergine eller agurk med riseddike.",
            },
        ],
        "body": """Miso-laks er 8 minutter til karamel-overflade: hvid miso, mirin, sesam der bruner.

  Kort marinade. Medium varme. Rosa midte.""",
        "tip": "Træk laksen 2 minutter før tid, hvis fileterne er tynde — de eftersteger udenfor kurven.",
    },
    {
        "title": "Sprøde torske-nuggets med grov remoulade",
        "slug": "torske-nuggets-remoulade",
        "description": "Sprøde torske-nuggets i airfryer — tykke loins i panko og danskvand, fish & chips-style med grov remoulade.",
        "prepTime": "PT15M",
        "cookTime": "PT12M",
        "totalTime": "PT27M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["torsk", "nuggets", "fish and chips", "remoulade", "fisk", "airfryer"],
        "imageAlt": "Sprøde torske-nuggets med grov remoulade",
        "ingredients": [
            "600 g torskeloins, i 3–4 cm nuggets",
            "1 tsk salt, peber",
            "Dej: 80 g hvedemel, ½ tsk bagepulver, 1 dl kold danskvand eller øl",
            "100 g panko",
            "Olie-spray",
            "Grov remoulade, citron, evt. pommes",
        ],
        "steps": [
            "Dup torsk tør. Krydr med salt og peber.",
            "Rør mel, bagepulver og iskold danskvand til en tyk dej. Vend fisk i dej, derefter panko. Press fast. Spray olie.",
            "Airfry 200 °C i 10–12 minutter. Vend halvvejs, til skorpen er dybt gylden og fisken er flager (ca. 60 °C).",
            "Server med grov remoulade og citron — fish & chips uden friture.",
        ],
        "faq": [
            {
                "question": "Øl eller danskvand?",
                "answer": "Begge giver luft. Øl smager mere pub. Danskvand er neutralt og børnevenligt.",
            },
            {
                "question": "Fileter i stedet for nuggets?",
                "answer": "Se [fiskefileter med panko](/opskrifter/airfryer/fiskefileter-panko). Nuggets er hurtigere og mere snack.",
            },
            {
                "question": "Paneringen falder af?",
                "answer": "Fisken var våd, eller dejen for tynd. Dup tør, tyk dej, press panko.",
            },
            {
                "question": "Hjemmelavet remoulade?",
                "answer": "Mayo + hakkede cornichoner + kapers + dild + sennep. Grov er loven.",
            },
        ],
        "body": """Torske-nuggets er fish & chips i hapser: kold danskvandsdej, panko, hed kurv, grov remoulade.

  Tør fisk. Kold dej. Høj varme.""",
        "tip": "Hold danskvandet iskoldt — boblerne i dejen giver lettere skorpe.",
    },
    {
        "title": "Laksefrikadeller med citron og dild",
        "slug": "laksefrikadeller-citron-dild",
        "description": "Laksefrikadeller i airfryer — luftige, sprøde fiskedeller med citron, dild og minimal bindemiddel.",
        "prepTime": "PT15M",
        "cookTime": "PT12M",
        "totalTime": "PT30M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["laks", "frikadeller", "fiskekager", "dild", "citron", "airfryer"],
        "imageAlt": "Sprøde laksefrikadeller med dild og citron",
        "ingredients": [
            "500 g laksefilet uden skind, groft hakket (ikke puré)",
            "1 æg",
            "2 spsk panko eller rasp",
            "2 spsk creme fraiche eller græsk yoghurt",
            "2 spsk hakket dild, 1 tsk citronskal, 1 spsk citronsaft",
            "1 tsk salt, peber",
            "Olie-spray",
        ],
        "steps": [
            "Hak laksen med kniv, så der er struktur. Rør æg, panko, creme fraiche, dild, citron, salt og peber i. Køl 10 minutter.",
            "Form 8–10 flade frikadeller. Spray olie.",
            "Airfry 190 °C i 10–12 minutter. Vend halvvejs, til skorpen er gylden.",
            "Server med citron, dildyoghurt eller salat.",
        ],
        "faq": [
            {
                "question": "Krabbe i stedet?",
                "answer": "Ja — erstat halvdelen eller det hele med krabbekød. Samme binder, mere delikat smag.",
            },
            {
                "question": "Puré i foodprocessor?",
                "answer": "Undgå det. For fin fars bliver limet. Kniv = cakes med bid.",
            },
            {
                "question": "Falder fra hinanden?",
                "answer": "For lidt æg/panko, eller for våd fisk. Dup laksen, køl farsen, form flattere.",
            },
            {
                "question": "Klassisk fiskefars?",
                "answer": "Se [fiskefrikadelle-fars](/opskrifter/palaeg/fiskefrikadelle-fars) til pålæg. Her er airfryer-cakes.",
            },
        ],
        "body": """Laksefrikadeller er fiskekager med knas: hakket — ikke blendet — laks, citron, dild, minimal binder.

  Struktur i farsen. Hed kurv. Citron ved bordet.""",
        "tip": "Lad farsen hvile koldt — pankoen suger, og bollerne holder bedre.",
    },
    {
        "title": "Svenske kødboller med tyttebær-glaze",
        "slug": "svenske-koedboller-tyttebaer",
        "description": "Svenske kødboller i airfryer — saftige kalve-/svinekødboller med mørk stegeskorpe og tyttebær-glaze.",
        "prepTime": "PT20M",
        "cookTime": "PT14M",
        "totalTime": "PT34M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["kødboller", "svensk", "tyttebær", "kalv", "svinekød", "airfryer"],
        "imageAlt": "Svenske kødboller med tyttebær-glaze",
        "ingredients": [
            "400 g hakket kalv/svin (eller okse/svin)",
            "1 dl mælk, 2 spsk rasp",
            "1 æg, ½ finthakket løg",
            "½ tsk allehånde, 1 tsk salt, peber",
            "Olie-spray",
            "Glaze: 3 spsk tyttebærsyltetøj, 1 spsk sojasauce eller worcestershire, 1 tsk smør",
        ],
        "steps": [
            "Læg rasp i mælk 5 minutter. Rør kød, æg, løg, allehånde, salt og peber i. Form 16–20 små boller.",
            "Spray olie. Airfry 200 °C i 10–12 minutter. Vend halvvejs, til skorpen er mørk og kernen 72 °C.",
            "Varm tyttebær, soja og smør til en blank glaze. Vend de varme boller i den.",
            "Server med kartoffelmos eller bare ske — svensk husmand uden flødesovs-stress.",
        ],
        "faq": [
            {
                "question": "Uden glaze — med flødesovs?",
                "answer": "Klassisk. Brun fond + fløde på pande. Glazen her er det hurtige twist.",
            },
            {
                "question": "Tyttebær uden sukker?",
                "answer": "Brug [syltede tyttebær](/opskrifter/sylte/syltede-tyttebaer) og lidt honning i glazen.",
            },
            {
                "question": "For tørre?",
                "answer": "For magert kød eller for lang tid. 10–12 % fedt og stop ved 72 °C.",
            },
            {
                "question": "Forskel på danske frikadeller?",
                "answer": "Mindre, mere krydret med allehånde, ofte kalv/svin. Se også [frikadeller](/opskrifter/airfryer/frikadeller).",
            },
        ],
        "body": """Svenske kødboller i airfryer er høj varme til mørk skorpe, derefter tyttebær der klæber.

  Små boller. Hot finish. Glaze til sidst.""",
        "tip": "Våde hænder når du ruller — farsen klistrer mindre, bollerne bliver runde.",
    },
    {
        "title": "Fyldte portobellosvampe med salsiccia og taleggio",
        "slug": "fyldte-portobello-salsiccia-taleggio",
        "description": "Fyldte portobellosvampe i airfryer — salsiccia, salvie og smeltet taleggio i store hatte.",
        "prepTime": "PT15M",
        "cookTime": "PT14M",
        "totalTime": "PT29M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["portobello", "salsiccia", "taleggio", "svampe", "italiensk", "airfryer"],
        "imageAlt": "Portobellos fyldt med salsiccia og smeltet taleggio",
        "ingredients": [
            "4 store portobellosvampe, stilke fjernet",
            "250 g salsiccia eller anden krydret italiensk pølsefars (skal af)",
            "100 g taleggio eller anden blød ost, i tern",
            "6–8 blade salvie, hakket",
            "1 fed hvidløg, finthakket",
            "1 spsk olivenolie, peber, flagesalt",
        ],
        "steps": [
            "Scrabe forsigtigt lamellerne lidt, hvis hattene er meget dybe. Pensl med olie. Krydr let.",
            "Steg farsen af i en pande 3–4 minutter med hvidløg og salvie (eller 4 minutter i airfryeren i en skål). Dryp fedt fra.",
            "Fyld hattene med fars og ostetern. Airfry 180 °C i 10–12 minutter, til svampen er mør og osten bobler.",
            "Flagesalt og peber. Server med salat eller brød.",
        ],
        "faq": [
            {
                "question": "Uden salsiccia?",
                "answer": "Hakket svinekød + fennikel + chili. Eller pesto-mozzarella — se [pesto-portobello](/opskrifter/airfryer/pesto-portobello).",
            },
            {
                "question": "Taleggio for stærk?",
                "answer": "Mozzarella eller fontina. Taleggio giver den nøddeagtige stank, der hører til.",
            },
            {
                "question": "Vandige svampe?",
                "answer": "Dup hattene tørre. Undgå at vaske under vand — børst rent.",
            },
            {
                "question": "Kan de forberedes?",
                "answer": "Fyld op til 4 timer før. Airfry lige før servering.",
            },
        ],
        "body": """Portobello med salsiccia og taleggio er pizza uden dej: krydret fars, salvie, ost der løber.

  Tør hat. Forsteg fars. Ost til sidst i fyldet.""",
        "tip": "Vend hattene på hovedet i kurven, så fyldet ikke drypper gennem risten — brug gerne en lav form.",
    },
    {
        "title": "Bagt havregrød med pistaciecreme og mørk chokolade",
        "slug": "bagt-havregrod-pistacie-chokolade",
        "description": "Baked oats i airfryer — portionsanrettet kageagtig morgenmad med pistaciecreme og mørk chokolade på ca. 12 minutter.",
        "prepTime": "PT5M",
        "cookTime": "PT12M",
        "totalTime": "PT17M",
        "servings": 2,
        "difficulty": "nem",
        "tags": ["baked oats", "havregrød", "pistacie", "chokolade", "morgenmad", "protein", "airfryer"],
        "imageAlt": "Bagt havregrød med pistaciecreme og mørk chokolade",
        "ingredients": [
            "80 g havregryn",
            "1 dl mælk eller plantemælk",
            "1 æg",
            "1 spsk proteinpulver eller ekstra 2 spsk havre (valgfrit)",
            "1 tsk bakepulver, 1 knivspids salt",
            "2 spsk pistaciecreme eller finthakkede pistacier + 1 tsk honning",
            "30 g mørk chokolade, hakket",
            "Smør til formene",
        ],
        "steps": [
            "Smør 2 ramekiner eller én lille form, der passer i kurven.",
            "Rør havre, mælk, æg, bakepulver og salt. Fordel halvdelen i formene. Læg en klat pistaciecreme midt i. Resten af dejen over. Drys chokolade.",
            "Airfry 170 °C i 10–12 minutter, til overfladen er sat og midten stadig lidt blød.",
            "Køl 2 minutter. Spis direkte fra formen — pistaciekerne skal være flydende.",
        ],
        "faq": [
            {
                "question": "Forskel på bagt havregrød med bær?",
                "answer": "Samme teknik, anden kerne. Se [bagt havregrød med bær](/opskrifter/airfryer/bagt-havregrod-baer). Her er pistacie-chokolade-sporet.",
            },
            {
                "question": "Uden pistaciecreme?",
                "answer": "Peanutbutter eller mandelsmør. Eller kun chokolade.",
            },
            {
                "question": "For tør?",
                "answer": "For lang tid eller for lidt mælk. Start 10 minutter. Midten må gerne dirre lidt.",
            },
            {
                "question": "Meal prep?",
                "answer": "Rør dejen aftenen før. Bag om morgenen. Fyld pistacie lige før bagning.",
            },
        ],
        "body": """Baked oats med pistacie og chokolade er morgenmad der smager dessert: kageagtig kant, flydende kerne.

  Lav varme. Kort tid. Kerne i midten.""",
        "tip": "Gem en teskefuld pistaciecreme til toppen efter bagning — blank og Instagram-klar.",
    },
    {
        "title": "Kardemommesnurrer af butterdej med brunet smør",
        "slug": "kardemommesnurrer-butterdej",
        "description": "Kardemommesnurrer af butterdej i airfryer — hurtigt bagværk på ca. 10 minutter med brunet smør-remonce og sprøde lag.",
        "prepTime": "PT10M",
        "cookTime": "PT10M",
        "totalTime": "PT20M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["kardemomme", "butterdej", "snurrer", "bagværk", "brunch", "airfryer"],
        "imageAlt": "Kardemommesnurrer af butterdej med brunet smør",
        "ingredients": [
            "1 rulle butterdej (ca. 250 g)",
            "Remonce: 40 g smør (brunet og kølet til smørbart), 40 g sukker, 1–1½ tsk stødt kardemomme",
            "1 æg til pensling (valgfrit)",
            "Perlesukker eller flagesalt",
        ],
        "steps": [
            "Brun smørret, køl til det er blødt. Rør sukker og kardemomme i.",
            "Rul butterdejen ud. Smør remonce jævnt. Rull stramt fra den lange side. Skær i 8 snurrer.",
            "Læg i kurven med plads. Pensl æg. Drys perlesukker.",
            "Airfry 170 °C i 8–11 minutter, til lagene er gyldne og bunden karamelliseret. Køl 2 minutter — sukkeret er lava.",
        ],
        "faq": [
            {
                "question": "Kanelsnegle i stedet?",
                "answer": "Ja — bytt kardemomme ud med kanel. Se også [kanelsnegle af færdigdej](/opskrifter/airfryer/kanelsnegle-faerdigdej). Brunet smør er opgraderingen.",
            },
            {
                "question": "Remonce løber ud?",
                "answer": "For varmt smør. Det skal være smørbart, ikke flydende. Eller brug bagepapir under.",
            },
            {
                "question": "Gærdej?",
                "answer": "Muligt, men butterdej er 10-minutters-sporet. Gærdej kræver hævning.",
            },
            {
                "question": "Frosting?",
                "answer": "Tynd glasur af flormelis + mælk, eller bare flagesalt på den karamelliserede bund.",
            },
        ],
        "body": """Kardemommesnurrer af butterdej er hurtig wienerbrød-energi: brunet smør, kardemomme, sprøde lag.

  Køl smørret. Rull stramt. Medium varme.""",
        "tip": "Skær med skarp kniv i én bevægelse — savning presser lagene flade.",
    },
    {
        "title": "Cinnamon Roll French Toast Bites",
        "slug": "cinnamon-roll-french-toast-bites",
        "description": "Cinnamon Roll French Toast Bites i airfryer — brioche-tern i æggemasse, sprøde i kanelsukker med flødeost-glasur.",
        "prepTime": "PT10M",
        "cookTime": "PT10M",
        "totalTime": "PT20M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["french toast", "kanel", "brioche", "brunch", "dessert", "airfryer"],
        "imageAlt": "Cinnamon roll french toast bites med flødeost-glasur",
        "ingredients": [
            "400 g brioche eller blødt toastbrød, i 2–3 cm tern",
            "Æggemasse: 2 æg, 1 dl mælk, 1 tsk vanilje, 1 knivspids salt",
            "Kanelsukker: 3 spsk sukker + 1 tsk kanel",
            "Olie-spray eller smeltet smør",
            "Glasur: 50 g flødeost, 2 spsk flormelis, 1–2 spsk mælk",
        ],
        "steps": [
            "Vend brødternene kort i æggemassen — de skal være vædet, ikke gennemvædet. Dryp overskud af.",
            "Spray kurven. Læg ternene med plads. Spray eller pensl smør. Airfry 180 °C i 8–10 minutter. Vend halvvejs.",
            "Vend de varme bites i kanelsukker.",
            "Rør flødeost-glasur. Dryp over. Server med det samme.",
        ],
        "faq": [
            {
                "question": "Tørt brød?",
                "answer": "Bedre end frisk. Daggammelt brioche suger æggemassen uden at klaske.",
            },
            {
                "question": "Uden flødeost?",
                "answer": "Kun kanelsukker, eller tynd flormelis-glasur. Flødeost er cinnamon-roll-illusionen.",
            },
            {
                "question": "Hele skiver french toast?",
                "answer": "Muligt, men bites er mere sprøde overalt. Plancha-version: [arme riddere](/opskrifter/plancha/arme-riddere-plancha).",
            },
            {
                "question": "For bløde?",
                "answer": "For meget æggemasse eller for tæt pakket. Dryp godt, giv plads, +2 minutter.",
            },
        ],
        "body": """Cinnamon Roll French Toast Bites er brunch-hack: brioche-tern, kanelsukker, flødeost-glasur — uden at bage snurrer.

  Kort dyp. Hed kurv. Glasur til sidst.""",
        "tip": "Arbejd i hold, hvis kurven er lille — overfyldte tern damper i stedet for at brune.",
    },
    {
        "title": "Bagte ferskner med mascarpone og amaretti",
        "slug": "bagte-ferskner-mascarpone-amaretti",
        "description": "Bagte ferskner i airfryer — karamelliseret med honning og timian, toppet med mascarpone og knuste amaretti.",
        "prepTime": "PT5M",
        "cookTime": "PT12M",
        "totalTime": "PT17M",
        "servings": 4,
        "difficulty": "nem",
        "tags": ["ferskner", "mascarpone", "amaretti", "dessert", "sommer", "airfryer"],
        "imageAlt": "Bagte ferskner med mascarpone og amaretti-krummer",
        "ingredients": [
            "4 modne men faste ferskner (eller blommer), halveret og stenet",
            "2 spsk honning",
            "4 kviste frisk timian",
            "1 knivspids flagesalt",
            "150 g mascarpone",
            "8 amaretti-makroner, knust",
            "Valgfrit: lidt vanilje i mascarponen",
        ],
        "steps": [
            "Læg ferskenhalvdelene snitflade op. Dryp honning i hulrummene. Læg timian på. Drys flagesalt.",
            "Airfry 180 °C i 10–12 minutter, til frugten er mør og kanterne karamelliserer.",
            "Rør mascarpone let (evt. med vanilje). Fordel på de varme ferskner.",
            "Drys knuste amaretti over. Server med det samme.",
        ],
        "faq": [
            {
                "question": "Blommer i stedet?",
                "answer": "Ja — samme tid. Blommer er mere syrlige og tåler ekstra honning.",
            },
            {
                "question": "Grill-version?",
                "answer": "Se [grillede ferskner med mascarpone](/opskrifter/grill/grillede-ferskner-mascarpone). Her er amaretti-krummen ekstra.",
            },
            {
                "question": "Uden amaretti?",
                "answer": "Digestive, mandler eller havreknas. Amaretti giver bitter-mandel.",
            },
            {
                "question": "Hårde ferskner?",
                "answer": "+3–4 minutter, eller vælg blommer. Overmodne falder sammen.",
            },
        ],
        "body": """Bagte ferskner med mascarpone og amaretti er dessert uden dej: honning, timian, cremet ost, knasende makroner.

  Fast frugt. Hed kurv. Krummer til sidst.""",
        "tip": "Kom amaretti på lige før servering — ellers bliver de bløde af frugtsaften.",
    },
]


def yaml_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def dump_list(items: list[str], indent: int = 2) -> str:
    pad = " " * indent
    return "\n".join(f"{pad}- {yaml_str(i)}" for i in items)


def dump_faq(faq: list[dict], indent: int = 2) -> str:
    pad = " " * indent
    blocks = []
    for f in faq:
        blocks.append(
            f"{pad}- question: {yaml_str(f['question'])}\n{pad}  answer: {yaml_str(f['answer'])}"
        )
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
