#!/usr/bin/env python3
"""10 nye tatar-opskrifter — grej, sprødhed og umami (nov 2026)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"
PUBLIC = Path(__file__).resolve().parent.parent / "public/recipes"
PUBLISHED = "2026-11-24"

RECIPES = [
    {
        "cat": "airfryer",
        "title": "Lakse-tatar med airfryer-rugbrødschips",
        "slug": "laksetatar-rugbroedschips-airfryer",
        "description": "Rå eller koldrøget laksetatar med dild, citron og kapers — serveret med sprøde rugbrødschips fra airfryeren.",
        "prepTime": "PT20M",
        "cookTime": "PT8M",
        "totalTime": "PT28M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": [
            "tatar",
            "laks",
            "fisk",
            "airfryer",
            "rugbrødschips",
            "forret",
            "dild",
            "forår",
            "sommer",
        ],
        "relatedGrej": ["airfryer-tilbehoer", "laksekniv-fleksibel"],
        "imageAlt": "Laksetatar med dild og kapers ved siden af gyldne rugbrødschips",
        "ingredients": [
            "400 g sushi-kvalitet laks eller [koldrøget laks](/opskrifter/roeg/koldroget-laks), iskold",
            "1 spsk kapers, hakket",
            "1 lille skalotteløg, finthakket",
            "2 spsk finthakket dild",
            "1 spsk citronsaft + lidt skal",
            "1 spsk god olivenolie",
            "Flagesalt og friskkværnet peber",
            "8 tynde skiver gammelt rugbrød (til [rugbrødschips](/opskrifter/airfryer/rugbroedschips-airfryer))",
            "2 spsk olivenolie til chips",
        ],
        "steps": [
            "Skær laksen i 5 mm tern med kniv. Hold den kold — gerne 10 minutter i fryseren først.",
            "Vend forsigtigt med kapers, skalotteløg, dild, citron, olie, salt og peber. Smag til — den skal bide.",
            "Pensl rugbrødsskiverne let med olie. Airfry ved 160 °C i 6–8 minutter, ét lag, vend halvvejs — se også [rugbrødschips i airfryer](/opskrifter/airfryer/rugbroedschips-airfryer).",
            "Anret tatar i bunker. Server straks med varme chips ved siden af.",
        ],
        "faq": [
            {
                "question": "Rå eller koldrøget?",
                "answer": "Begge virker. Rå sushi-laks er renere. [Koldrøget laks](/opskrifter/roeg/koldroget-laks) giver mere dybde — skær den lidt tykkere.",
            },
            {
                "question": "Sikkert at spise rå laks?",
                "answer": "Brug sushi-kvalitet, eller fisk der har været frosset ved −20 °C i mindst 24 timer. Spis med det samme.",
            },
            {
                "question": "Kan chips laves i ovn?",
                "answer": "Ja — 170 °C i 12–18 minutter. Airfryer er hurtigere og sprødere.",
            },
            {
                "question": "Forskel på [tuntatar](/opskrifter/antipasti/tuntatar-kapers)?",
                "answer": "Tun er mere kødagtig. Laks er federe og tager dild og citron bedre.",
            },
        ],
        "body": "Laksetatar er nordisk knivarbejde: tern, dild, citron, kapers.\n\nChipsene er grejet. Airfryer. Knas. Kontrast.",
        "tip": "Server chipsene varme og tatar kold. Temperaturkontrasten er halvdelen af retten.",
    },
    {
        "cat": "ovn",
        "title": "Rødbedetatar med peberrod og hytteost-creme",
        "slug": "roedbedetatar-peberrod-hytteost",
        "description": "Bagte rødbeder hakket groft med kapers og løg — vegetarisk tatar med cremet peberrod-hytteost.",
        "prepTime": "PT20M",
        "cookTime": "PT1H",
        "totalTime": "PT1H20M",
        "servings": 4,
        "difficulty": "nem",
        "tags": [
            "tatar",
            "rødbeder",
            "vegetar",
            "hytteost",
            "peberrod",
            "forret",
            "efterår",
            "vinter",
        ],
        "relatedGrej": [],
        "imageAlt": "Dybrød rødbedetatar med hvid peberrod-hytteostcreme og flagesalt",
        "ingredients": [
            "600 g rødbeder (gerne [saltbagte](/opskrifter/ovn/saltbagte-roedbeder) eller bagte i folie)",
            "1 sjalotteløg, finthakket",
            "1 spsk kapers, hakket",
            "1 spsk æbleeddike eller citronsaft",
            "2 spsk olivenolie",
            "Flagesalt og peber",
            "150 g hytteost",
            "1–2 spsk friskrevet peberrod",
            "1 tsk citronsaft til cremen",
            "Evt. dild eller purløg",
        ],
        "steps": [
            "Bag rødbederne ved 200 °C i 45–60 minutter (folie eller saltdej), til de er møre. Skræl og køl.",
            "Hak groft med kniv — tern, ikke puré. Vend med sjalot, kapers, eddike, olie, salt og peber.",
            "Blend eller mos hytteost med peberrod, citron og en knivspids salt, til den er cremet.",
            "Anret rødbedetatar. Læg en klat peberrod-creme ved siden af. Drys urter og flagesalt.",
        ],
        "faq": [
            {
                "question": "Rå rødbede?",
                "answer": "Nej til den her. Bagte rødbeder er søde og bløde nok til at hakke. Rå bliver træagtig.",
            },
            {
                "question": "Uden hytteost?",
                "answer": "Creme fraiche eller skyr virker. Peberroden er det vigtige — den skal bide.",
            },
            {
                "question": "Saltbagte rødbeder?",
                "answer": "Ja — [saltbagte rødbeder](/opskrifter/ovn/saltbagte-roedbeder) giver den dybeste smag. Folie er hurtigere.",
            },
            {
                "question": "Kan den laves dagen før?",
                "answer": "Hak rødbederne dagen før. Bland cremen lige før servering, ellers bliver peberroden mild.",
            },
        ],
        "body": "Rødbedetatar er vegetarisk umami uden at lyve om kød.\n\nBagt rod. Kapers. Peberrod. Hytteost der bider.",
        "tip": "Brug handsker når du hakker. Ellers ser køkkenet ud som et mordsted i ugevis.",
    },
    {
        "cat": "antipasti",
        "title": "Tun-tatar med sriracha-mayo og ristet sesam",
        "slug": "tuntatar-sriracha-mayo-sesam",
        "description": "Asiatisk tuntatar med soya, ingefær og forårsløg — serveret med sriracha-mayo, ristet sesam og sprødt rispapir.",
        "prepTime": "PT25M",
        "cookTime": "PT5M",
        "totalTime": "PT30M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": [
            "tatar",
            "tun",
            "antipasti",
            "sriracha",
            "sesam",
            "asiatisk",
            "forret",
            "fisk",
            "råt",
        ],
        "relatedGrej": [],
        "imageAlt": "Tun-tatar med sriracha-mayo, ristet sesam og sprøde rispapirchips",
        "ingredients": [
            "400 g sushi-kvalitet tunfilet, iskold",
            "1 spsk sojasauce",
            "1 tsk friskrevet ingefær",
            "2 forårsløg, tyndt skåret",
            "1 tsk sesamolie",
            "1 spsk ristede sesamfrø",
            "3 spsk mayonnaise",
            "1–2 tsk [sriracha](/opskrifter/fermentering/sriracha-fra-bunden) eller færdig",
            "4 ark rispapir eller wonton-skaller",
            "Neutral olie til stegning/airfry",
            "Flagesalt, lime",
        ],
        "steps": [
            "Skær tunen i 5 mm tern. Vend forsigtigt med soja, ingefær, forårsløg og sesamolie. Hold kold.",
            "Rør mayo med sriracha. Smag til — den skal være skarp, ikke sød.",
            "Pensl rispapir let med olie. Airfry ved 180 °C i 3–4 minutter, til det bobler og knaser — eller steg kort i olie.",
            "Anret tatar. Dryp sriracha-mayo. Drys sesam. Server med chipsene med det samme.",
        ],
        "faq": [
            {
                "question": "Forskel på [tuntatar med kapers](/opskrifter/antipasti/tuntatar-kapers)?",
                "answer": "Den klassiske er olivenolie og kapers. Her er soya, ingefær, varme og knas — asiatisk linje.",
            },
            {
                "question": "Hvilken tun?",
                "answer": "Sushi-/sashimi-kvalitet. Rød, fast, uden brun kant. Ikke steak-tun til grill.",
            },
            {
                "question": "Wonton i stedet for rispapir?",
                "answer": "Ja. Skær i trekanter, pensl med olie, airfry 160 °C i 4–5 minutter.",
            },
            {
                "question": "Uden mayo?",
                "answer": "Brug yoghurt blandet med sriracha, eller bare sriracha og sesamolie. Knaset mangler du dog.",
            },
        ],
        "body": "Tun-tatar med sriracha er den skarpe kusine til den italienske.\n\nSoya. Ingefær. Sesam. Chips der knaser.",
        "tip": "Bland dressingen først. Vend tunen i sidste sekund — soya trækker væske ud, hvis den står.",
    },
    {
        "cat": "stobejern",
        "title": "Oksetatar på sprød kartoffel-rösti",
        "slug": "oksetatar-kartoffelroesti-stobejern",
        "description": "Klassisk rørt oksetatar anrettet på varm, sprødstegt kartoffel-rösti fra støbejernspanden — koldt kød, varm knas.",
        "prepTime": "PT30M",
        "cookTime": "PT20M",
        "totalTime": "PT50M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": [
            "tatar",
            "oksekød",
            "rösti",
            "støbejern",
            "forret",
            "bistro",
            "nytår",
            "kartofler",
        ],
        "relatedGrej": ["stoebejern-vs-carbonstaal", "stoebjern-rene-skole"],
        "imageAlt": "Oksetatar på gylden kartoffel-rösti i støbejernspande",
        "ingredients": [
            "400 g oxfilet eller culotte, sushi-kvalitet, iskold",
            "1 æggeblomme",
            "1 tsk dijonsennep",
            "1 spsk kapers, hakket",
            "1 sjalotteløg, finthakket",
            "Worcestershire, flagesalt, peber, citron",
            "600 g fastkogende kartofler",
            "1 lille løg, fintrevet (valgfrit)",
            "1 æg + 1 spsk majsstivelse til rösti",
            "2–3 spsk smør eller olie til støbejernet",
        ],
        "steps": [
            "Riv kartoflerne groft. Vrid hårdt i et viskestykke — væsken skal ud. Bland med løg, æg, majsstivelse og salt.",
            "Varm støbejernspanden rygende. Smør i. Pres kartoffelmassen fladt. Steg 8–10 minutter uden at rode, vend (eller fold), steg 6–8 minutter mere til dybt gylden skorpe.",
            "Hak kødet i 5 mm tern. Rør forsigtigt med blomme, sennep, kapers, sjalot, worcestershire, salt, peber og citron — som [grovhakket oksetatar](/opskrifter/pande/oksetatar-sennepskorn-estragon).",
            "Skær röstien i portioner. Læg tatar ovenpå med det samme. Server: koldt kød, varm knas.",
        ],
        "faq": [
            {
                "question": "Airfryer-rösti?",
                "answer": "Ja — se [kartoffelrösti i airfryer](/opskrifter/airfryer/kartoffelroesti). Støbejern giver dybere skorpe og teater.",
            },
            {
                "question": "Kan röstien laves først?",
                "answer": "Lav den lige før. Genopvarm gør den læderagtig. Tatar må gerne stå 10 minutter koldt.",
            },
            {
                "question": "Hakket i maskine?",
                "answer": "Nej. Kniv. Maskine smører kødet — det skal tygges.",
            },
            {
                "question": "Sikkert?",
                "answer": "Friskt kød, koldt bræt, spis med det samme. Frys 24 timer ved −20 °C, hvis du er i tvivl om parasitter.",
            },
        ],
        "body": "Oksetatar på rösti er bistro-kontrast: koldt, syrligt kød på varm kartoffelskorpe.\n\nStøbejern. Ingen undskyldning.",
        "tip": "Pres röstien flad og rør den ikke. Skorpen kommer af ro — ikke af pisk.",
    },
    {
        "cat": "roeg",
        "title": "Koldrøget laksetatar fra grillen",
        "slug": "koldroget-laksetatar-grill",
        "description": "Lakseside koldrøges på grill eller i røgovn med røgsmuld, hakkes og røres til tatar med dild, citron og kapers.",
        "prepTime": "PT30M",
        "cookTime": "PT4H",
        "totalTime": "PT28H",
        "servings": 6,
        "difficulty": "svær",
        "tags": [
            "tatar",
            "laks",
            "koldrøgning",
            "grill",
            "røg",
            "forret",
            "nytår",
            "fisk",
            "festmad",
        ],
        "relatedGrej": [
            "koldroegningsbakke",
            "rygesmuld-flis-og-chunks",
            "laksekniv-fleksibel",
        ],
        "imageAlt": "Koldrøget laksetatar med dild og citron på mørk tallerken",
        "ingredients": [
            "600–800 g lakseside, skind på, sushi-kvalitet eller forudfrossen",
            "40 g salt + 20 g sukker til cure",
            "½ tsk peber",
            "Røgsmuld: bøg eller el (ikke hickory)",
            "1 spsk kapers, hakket",
            "1 sjalotteløg, finthakket",
            "2 spsk dild",
            "1 spsk citronsaft + skal",
            "1 spsk olivenolie",
            "Flagesalt",
        ],
        "steps": [
            "Cure laksen med salt, sukker og peber 12–18 timer i køleskab. Skyl, tør, pellicle 6–8 timer på rist i køleskab — som [koldrøget laks](/opskrifter/roeg/koldroget-laks).",
            "Koldrøg under 20 °C på grill med koldrøgningsbakke eller i røgovn 3–5 timer, til farve og aroma er der. Hvil i køleskab mindst 6 timer.",
            "Skær kødet fra skindet. Hak i 5–8 mm tern med kniv.",
            "Vend med kapers, sjalot, dild, citron, olie og flagesalt. Smag til. Server koldt med ristet brød eller rugbrødschips.",
        ],
        "faq": [
            {
                "question": "Forskel på [røget tatar](/opskrifter/roeg/roget-tatar)?",
                "answer": "Røget tatar er rå okse under røgpistol. Her er laksen ægte koldrøget først — dybere røg, mere arbejde.",
            },
            {
                "question": "Temperatur på grillen?",
                "answer": "Under 20 °C. Kun indirekte, røgsmuld i bakke, låget på. Blus = varmrøg = anden ret.",
            },
            {
                "question": "Kan jeg bruge købt koldrøget laks?",
                "answer": "Ja — så spring cure og røg over. Hak og rør. Mindre grej-flex, stadig god tatar.",
            },
            {
                "question": "Hvilket træ?",
                "answer": "Bøg eller el. Hickory og mesquite overdøver laks. Se [røgsmuld-guiden](/grej/rygesmuld-flis-og-chunks).",
            },
        ],
        "body": "Koldrøget laksetatar er weekend-projekt med payoff: cure, pellicle, røg, kniv.\n\nIkke røgpistol-teater. Ægte koldrøg.",
        "tip": "Hak først dagen efter røgning. Smagen sætter sig, og kødet skærer renere.",
    },
    {
        "cat": "stobejern",
        "title": "Svampetatar med brunet smør og estragon",
        "slug": "svampetatar-brunet-smoer-estragon",
        "description": "Hårdt ristede svampe på støbejern — afkølet og rørt med brunet smør, skalotteløg og estragon for maksimal umami.",
        "prepTime": "PT20M",
        "cookTime": "PT25M",
        "totalTime": "PT45M",
        "servings": 4,
        "difficulty": "nem",
        "tags": [
            "tatar",
            "svampe",
            "vegetar",
            "brunet smør",
            "estragon",
            "støbejern",
            "umami",
            "forret",
            "efterår",
        ],
        "relatedGrej": ["stoebejern-vs-carbonstaal", "stoebjern-rene-skole"],
        "imageAlt": "Svampetatar med brunet smør, estragon og ristet surdej",
        "ingredients": [
            "500 g blandede svampe (champignon, portobello, evt. shiitake eller kantarel)",
            "2 spsk olie til stegning",
            "75 g smør til brunet smør",
            "1 sjalotteløg, finthakket",
            "1 tsk finthakket estragon (eller ½ tsk tørret)",
            "1 spsk citronsaft",
            "Flagesalt og peber",
            "Evt. 1 tsk sojasauce eller worcestershire",
            "Ristet surdejsbrød til servering",
        ],
        "steps": [
            "Rens svampene. Skær i grove tern. Varm støbejernet rygende. Steg i hold uden at røre for meget, til de er dybt brune og næsten tørre — se også [tørstegte svampe](/opskrifter/stobejern/toerstegte-svampe).",
            "Afkøl svampene til lunkne. Hak finere med kniv, hvis de er for store.",
            "Brun smørret i en lille gryde til nøddeagtigt og gyldent. Afkøl 1 minut.",
            "Vend svampe med sjalot, estragon, citron, salt, peber, evt. soja og det lune brune smør. Server straks med brød.",
        ],
        "faq": [
            {
                "question": "Er det råt?",
                "answer": "Nej. Svampene er hårdt ristede. Tatar-stilen er den kolde, hakkede anretning — ikke rå svamp.",
            },
            {
                "question": "Hvilke svampe?",
                "answer": "Champignon + portobello er basen. Shiitake og kantarel løfter umami. Undgå vandede champignon alene uden hård stegning.",
            },
            {
                "question": "Uden estragon?",
                "answer": "Timian eller persille. Estragon er den franske linje, der spejler [oksetatar med estragon](/opskrifter/pande/oksetatar-sennepskorn-estragon).",
            },
            {
                "question": "Kan den være varm?",
                "answer": "Lunken er bedst. Varm bliver grød. Kold mister smør-aromaen.",
            },
        ],
        "body": "Svampetatar er umami uden kød: hård ristning, brunet smør, estragon.\n\nStøbejern tørrer. Smørret binder. Urten løfter.",
        "tip": "Fyld ikke panden. Dampede svampe er supperåvarer — ikke tatar.",
    },
    {
        "cat": "airfryer",
        "title": "Oksetatar med pommes frites fra airfryeren",
        "slug": "oksetatar-pommes-airfryer",
        "description": "Bistro-oksetatar med helt sprøde airfryer-pommes — kontrast mellem koldt, syrligt kød og varm fritte.",
        "prepTime": "PT30M",
        "cookTime": "PT25M",
        "totalTime": "PT55M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": [
            "tatar",
            "oksekød",
            "pommes",
            "airfryer",
            "bistro",
            "forret",
            "hovedret",
            "nytår",
        ],
        "relatedGrej": ["airfryer-tilbehoer", "oliesprayflasker-airfryer"],
        "imageAlt": "Oksetatar ved siden af gyldne airfryer-pommes frites",
        "ingredients": [
            "400 g oxfilet eller culotte, sushi-kvalitet, iskold",
            "1 æggeblomme",
            "1 tsk dijonsennep + 1 tsk sennepskorn",
            "1 spsk kapers, 1 sjalotteløg",
            "Worcestershire, flagesalt, peber, citron",
            "800 g bagekartofler til [pommes](/opskrifter/airfryer/pommes-frites-bagekartofler) eller [sprøde pomfritter](/opskrifter/airfryer/sproede-pomfritter)",
            "1–2 spsk olie",
            "Flagesalt til fritterne",
        ],
        "steps": [
            "Skær kartoflerne til fritter. Skyl, tør grundigt. Vend med olie og salt. Airfry ved 200 °C i 18–22 minutter, ryst undervejs — se [pommes frites af bagekartofler](/opskrifter/airfryer/pommes-frites-bagekartofler).",
            "Hak kødet i 5 mm tern. Rør med blomme, sennep, sennepskorn, kapers, sjalot, worcestershire, salt, peber og citron.",
            "Anret tatar i bunker. Server fritterne varme ved siden af — ikke ovenpå.",
            "Spis med det samme: koldt kød, varm fritte, samme gaffel.",
        ],
        "faq": [
            {
                "question": "Forskel på [oksetatar på rösti](/opskrifter/stobejern/oksetatar-kartoffelroesti-stobejern)?",
                "answer": "Rösti er én skorpe under kødet. Her er fritterne frit tilbehør — mere bistro-tallerken, mere grej-airfryer.",
            },
            {
                "question": "Frosne fritter?",
                "answer": "Ja — [frosne pomfritter](/opskrifter/airfryer/frosne-pomfritter) virker. Hjemmelavede er mere Saltet.",
            },
            {
                "question": "Sauce til?",
                "answer": "Ikke nødvendig. En klat [aioli](/opskrifter/dips/aioli) eller bare ekstra sennep. Kødet er dressingen.",
            },
            {
                "question": "Hovedret eller forret?",
                "answer": "Med 200 g kød og en bunke fritter er det hovedret til to — eller forret til fire med mindre portioner.",
            },
        ],
        "body": "Oksetatar med pommes er den franske bistro på dansk grej: kniv, syre, airfryer.\n\nKoldt. Varmt. Sprødt. Færdigt.",
        "tip": "Salt fritterne når de kommer ud. Salt tatar når den er rørt. To salte. To jobs.",
    },
    {
        "cat": "antipasti",
        "title": "Kammuslingetatar med brunet smør og hasselnødder",
        "slug": "kammuslingetatar-brunet-smoer-hasselnodder",
        "description": "Finthakkede rå kammuslinger med citron, ristede hasselnødder og lunt brunet smør — nytårsforret med knas og nøddeagtig dybde.",
        "prepTime": "PT20M",
        "cookTime": "PT5M",
        "totalTime": "PT25M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": [
            "tatar",
            "kammusling",
            "skaldyr",
            "brunet smør",
            "hasselnødder",
            "forret",
            "nytår",
            "antipasti",
            "festmad",
        ],
        "relatedGrej": [],
        "imageAlt": "Kammuslingetatar med brunet smør, hasselnødder og citronskal",
        "ingredients": [
            "400 g friske kammuslinger (uden roe, eller med hvis du vil), iskold",
            "1 sjalotteløg, meget finthakket",
            "1 spsk citronsaft + fin skal",
            "50 g smør",
            "40 g hasselnødder, ristede og grofthakkede",
            "Flagesalt og hvid peber",
            "Evt. lidt purløg eller kørvel",
        ],
        "steps": [
            "Dup kammuslingerne tørre. Skær i fine tern (3–5 mm). Hold iskold.",
            "Vend forsigtigt med sjalot, citronsaft, skal, salt og peber.",
            "Rist hasselnødderne tørre på pande, til de dufter. Hak groft.",
            "Brun smørret til nøddeagtigt gyldent. Anret tatar. Drys nødder. Hæld lunt brunet smør over lige før bordet.",
        ],
        "faq": [
            {
                "question": "Frosne kammuslinger?",
                "answer": "Ja, hvis de er IQF og tøet korrekt i køleskab. Dup dem ekstra tørre — væske dræber tatar.",
            },
            {
                "question": "Med eller uden roe?",
                "answer": "Uden er mildere og pænere. Roe giver mere havsmag — hak den separat og bland i.",
            },
            {
                "question": "Kan smørret være koldt?",
                "answer": "Nej. Det skal være lunt, så det dufter. Koldt smør er bare fedt.",
            },
            {
                "question": "Erstatning for hasselnødder?",
                "answer": "Mandler eller pinjekerner. Hasselnød spejler det brune smør bedst.",
            },
        ],
        "body": "Kammuslingetatar er nytår uden snobberi: rå musling, citron, brunet smør, nød.\n\nLunt smør over koldt kød. Det er showet.",
        "tip": "Anret på kolde tallerkener. Hæld smørret ved bordet — aromaen er halvdelen.",
    },
    {
        "cat": "antipasti",
        "title": "Tomattatar med flagesalt og basilikum",
        "slug": "tomattatar-flagesalt-basilikum",
        "description": "Modne, drænede tomater rørt med kapers, olivenolie og basilikum — sommer- og efterårs-tatar til sprødt surdejsbrød.",
        "prepTime": "PT25M",
        "cookTime": "PT0M",
        "totalTime": "PT40M",
        "servings": 4,
        "difficulty": "nem",
        "tags": [
            "tatar",
            "tomat",
            "vegetar",
            "basilikum",
            "flagesalt",
            "antipasti",
            "forret",
            "sommer",
            "efterår",
        ],
        "relatedGrej": [],
        "imageAlt": "Tomattatar med basilikum, kapers og flagesalt på surdejsbrød",
        "ingredients": [
            "800 g meget modne tomater (gerne blandede sorter)",
            "1 spsk kapers, hakket",
            "1 sjalotteløg, finthakket",
            "3 spsk god olivenolie",
            "1 spsk rødvinsseddike eller sherryeddike",
            "Flagesalt og peber",
            "En håndfuld frisk basilikum",
            "Sprødt surdejsbrød eller crostini",
            "Evt. lidt [semidried tomater](/opskrifter/antipasti/semidried-tomater-timian) for dybde",
        ],
        "steps": [
            "Skold og skræl tomaterne, eller skær dem i kvarte og fjern kerner. Hak kødet groft.",
            "Læg hakket tomat i et dørslag med en knivspids salt. Dræn 15–20 minutter — væsken skal væk.",
            "Vend med kapers, sjalot, olie, eddike, peber og flagesalt. Riv basilikum i til sidst.",
            "Server på ristet surdej. Mere flagesalt ovenpå. Spis med det samme.",
        ],
        "faq": [
            {
                "question": "Vintertomater?",
                "answer": "Nej. Denne ret kræver rigtig modne tomater. Om vinteren: brug [semidried tomater](/opskrifter/antipasti/semidried-tomater-timian) som base i stedet.",
            },
            {
                "question": "Hvorfor dræne?",
                "answer": "Ellers bliver det suppe på brødet. Tatar skal kunne ligge, ikke flyde.",
            },
            {
                "question": "Mozzarella med?",
                "answer": "Lidt buffalo i tern virker. Så er det tættere på caprese — stadig fint, men anden ret.",
            },
            {
                "question": "Kan den stå?",
                "answer": "Hak og dræn op til 2 timer før. Bland olie og basilikum lige før servering.",
            },
        ],
        "body": "Tomattatar er rå sommer på ske: drænet tomat, kapers, olie, basilikum, flagesalt.\n\nIngen mayonnaise. Ingen ost nødvendig. Bare koncentreret tomat.",
        "tip": "Salt i dørslaget, flagesalt ved bordet. Første salt trækker væske. Andet salt er smag.",
    },
    {
        "cat": "pande",
        "title": "Vildttatar med enebær og tyttebær",
        "slug": "vildttatar-enebaer-tyttebaer",
        "description": "Efterårs- og jagtsæson-tatar på rådyr- eller krondyrmørbrad med knuste enebær, tyttebær og peberrod.",
        "prepTime": "PT25M",
        "cookTime": "PT0M",
        "totalTime": "PT25M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": [
            "tatar",
            "vildt",
            "rådyr",
            "krondyr",
            "enebær",
            "tyttebær",
            "peberrod",
            "forret",
            "efterår",
            "jagtsæson",
        ],
        "relatedGrej": ["skaerebraet-endetrae-vs-plastik"],
        "imageAlt": "Vildttatar med tyttebær, knuste enebær og peberrod",
        "ingredients": [
            "400 g rådyr- eller krondyrmørbrad, sushi-kvalitet / jagtsikkert, iskold",
            "6–8 enebær, knust i morter",
            "2 spsk tyttebær (syltede, dryppet — eller friske hvis milde)",
            "1 spsk friskrevet peberrod",
            "1 sjalotteløg, finthakket",
            "1 tsk dijonsennep",
            "1 spsk olivenolie eller neutral olie",
            "Flagesalt og friskkværnet peber",
            "Evt. lidt citronsaft",
            "Ristet rugbrød til servering",
        ],
        "steps": [
            "Skær mørbraden i 5 mm tern med kniv. Ikke kværn. Hold kødet iskoldt.",
            "Knus enebær groft. Vend forsigtigt kød med enebær, sjalot, sennep, olie, peberrod, salt og peber.",
            "Fold tyttebær i til sidst, så de ikke farver alt pink. Smag til med citron hvis det mangler syre.",
            "Anret bunker. Ekstra peberrod og tyttebær ved siden af. Server med rugbrød.",
        ],
        "faq": [
            {
                "question": "Okse i stedet?",
                "answer": "Ja — så er det tættere på [grovhakket oksetatar](/opskrifter/pande/oksetatar-sennepskorn-estragon). Enebær og tyttebær fungerer stadig, men vildt er pointen.",
            },
            {
                "question": "Sikkert at spise råt vildt?",
                "answer": "Kun fra kilde du stoler på, korrekt håndteret og gerne forudfrosset ved −20 °C i 24 timer. Spis med det samme. Er du i tvivl: steg det.",
            },
            {
                "question": "For bitter enebær?",
                "answer": "For mange. Start med 4–5 bær. De skal være baggrund, ikke gin.",
            },
            {
                "question": "Dyrekølle i stedet for mørbrad?",
                "answer": "Mørbrad er bedst til tatar. Kølle er sejere — brug den til [koldrøget dyrekølle](/opskrifter/roeg/koldroget-dyrekoelle) eller gryde.",
            },
        ],
        "body": "Vildttatar er jagtsæson på tallerkenen: mørbrad, enebær, tyttebær, peberrod.\n\nIkke okse med pynt. Rigtigt vildt. Kort sæson.",
        "tip": "Knus enebær, hak dem ikke til pulver. Du vil have små bits, der popper — ikke savsmuld.",
    },
]


def yaml_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def to_mdx(d: dict) -> str:
    cat = d["cat"]
    tags = "\n".join(f"  - {yaml_str(t)}" for t in d["tags"])
    ings = "\n".join(f"  - {yaml_str(x)}" for x in d["ingredients"])
    steps = "\n".join(f"  - {yaml_str(x)}" for x in d["steps"])
    faqs = "\n".join(
        f'  - question: {yaml_str(f["question"])}\n    answer: {yaml_str(f["answer"])}'
        for f in d["faq"]
    )
    grej = ""
    if d.get("relatedGrej"):
        grej_lines = "\n".join(f"  - {yaml_str(g)}" for g in d["relatedGrej"])
        grej = f"relatedGrej:\n{grej_lines}\n"
    slug = d["slug"]
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
{grej}image: /recipes/{cat}/{slug}.jpg
imageAlt: {yaml_str(d["imageAlt"])}
publishedAt: {PUBLISHED}
ingredients:
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


def main() -> None:
    assert len(RECIPES) == 10, f"expected 10 recipes, got {len(RECIPES)}"
    slugs = [r["slug"] for r in RECIPES]
    assert len(slugs) == len(set(slugs)), "duplicate slugs"

    written = []
    for d in RECIPES:
        assert len(d["faq"]) >= 3, d["slug"]
        assert d.get("tip")
        assert len(d["ingredients"]) >= 3
        assert len(d["steps"]) >= 3
        cat = d["cat"]
        out = ROOT / cat
        out.mkdir(parents=True, exist_ok=True)
        (PUBLIC / cat).mkdir(parents=True, exist_ok=True)
        path = out / f"{d['slug']}.mdx"
        if path.exists():
            raise SystemExit(f"slug collision: {path}")
        path.write_text(to_mdx(d), encoding="utf-8")
        written.append(f"{cat}/{d['slug']}")
        print("wrote", f"{cat}/{path.name}")

    print(f"done: {len(written)} recipes")


if __name__ == "__main__":
    main()
