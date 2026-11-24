#!/usr/bin/env python3
"""9 airfryer-gaps — søgetrafik, grej, sæson + tatar/tilbehør (nov 2026).

Springer rugbrødschips (#2) og gochujang/KFC (#5) over — de findes allerede.
Idé #9 bliver to opskrifter: forårsruller + wonton-chips.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"
PUBLIC = Path(__file__).resolve().parent.parent / "public/recipes"
PUBLISHED = "2026-11-24"
CAT = "airfryer"

RECIPES = [
    {
        "title": "Knuste kartofler med brunet smør og parmesan",
        "slug": "knuste-kartofler-brunet-smoer-parmesan",
        "description": "Smashed potatoes i airfryer med brunet smør og parmesan — ultra-sprødt tilbehør til bøf og tatar.",
        "prepTime": "PT20M",
        "cookTime": "PT22M",
        "totalTime": "PT42M",
        "servings": 4,
        "difficulty": "nem",
        "tags": [
            "smashed potatoes",
            "knuste kartofler",
            "brunet smør",
            "parmesan",
            "tilbehør",
            "kartofler",
            "sprød",
            "tatar",
        ],
        "relatedGrej": ["airfryer-tilbehoer"],
        "imageAlt": "Knuste kartofler med brunet smør, parmesan og flagesalt",
        "ingredients": [
            "800 g små kartofler",
            "2 spsk olivenolie",
            "50 g fint reven parmesan",
            "75 g smør til brunet smør",
            "Flagesalt og peber",
            "Evt. frisk rosmarin eller estragon",
        ],
        "steps": [
            "Kog kartoflerne i saltet vand 12–15 minutter, til de er møre. Dryp og tør godt.",
            "Pres hver kartoffel flad med et glas, så de revner men hænger sammen. Pensl med olie. Salt og peber.",
            "Airfry 200 °C i 15–18 minutter, til undersiden er dybt gylden. Drys parmesan over de sidste 3–4 minutter.",
            "Brun smørret i en lille gryde til nøddeagtigt gyldent. Hæld over de varme kartofler. Flagesalt. Server straks — også til [oksetatar](/opskrifter/airfryer/oksetatar-pommes-airfryer) eller bøf.",
        ],
        "faq": [
            {
                "question": "Forskel på [knuste kartofler med parmesan](/opskrifter/airfryer/smashed-parmesan-potatoes)?",
                "answer": "Den klassiske er olie + parmesan. Her er brunet smør finishen — nøddeagtig umami ovenpå knaset.",
            },
            {
                "question": "Kan smørret i kurven?",
                "answer": "Nej. Det brænder. Brun det i gryde, hæld over når kartoflerne er færdige.",
            },
            {
                "question": "Til tatar?",
                "answer": "Ja. Koldt kød, varm smash — samme kontrast som [oksetatar på rösti](/opskrifter/stobejern/oksetatar-kartoffelroesti-stobejern).",
            },
            {
                "question": "Store kartofler?",
                "answer": "Halvér efter kogning. Små hele er jævnest.",
            },
        ],
        "body": "Knuste kartofler med brunet smør er smash med upgrade: knas fra airfryeren, nøddeagtigt smør ovenpå.\n\nParmesan til sidst. Smør udenpå. Ikke omvendt.",
        "tip": "Tør kartoflerne efter kogning. Våd overflade = damp, ikke skorpe.",
    },
    {
        "title": "Glaseret laks med miso og sesam",
        "slug": "miso-sesam-laks-airfryer",
        "description": "Lynhurtig miso-sesam-laks i airfryer — karamelliseret glaze og sprød skorpe på 8–10 minutter.",
        "prepTime": "PT10M",
        "cookTime": "PT10M",
        "totalTime": "PT20M",
        "servings": 2,
        "difficulty": "nem",
        "tags": [
            "laks",
            "miso",
            "sesam",
            "fisk",
            "umami",
            "glaze",
            "asiatisk",
            "hverdag",
        ],
        "relatedGrej": ["airfryer-tilbehoer"],
        "imageAlt": "Glaseret lakseside med miso, sesam og forårsløg fra airfryeren",
        "ingredients": [
            "2 lakseskiver (á ca. 150–180 g), skind på",
            "1½ spsk hvid [miso](/opskrifter/fermentering/hjemmelavet-shiro-miso) eller færdig shiro-miso",
            "1 spsk honning eller ahornsirop",
            "1 tsk sojasauce",
            "1 tsk sesamolie",
            "1 tsk riseddike eller citron",
            "1 spsk ristede sesamfrø",
            "Forårsløg til servering",
        ],
        "steps": [
            "Dup laksen tør. Rør miso, honning, soja, sesamolie og eddike til en tyk glaze.",
            "Pensl kødsiden generøst. Lad stå 5 minutter, mens airfryeren forvarmer til 190 °C.",
            "Læg skind-side ned. Airfry 8–10 minutter, til glazen bobler og kanterne karamelliserer. Tykkere fileter: +1–2 minutter.",
            "Drys sesam og forårsløg. Server med ris eller [rugbrødschips](/opskrifter/airfryer/rugbroedschips-airfryer).",
        ],
        "faq": [
            {
                "question": "Forskel på [crispy skin teriyaki-laks](/opskrifter/airfryer/crispy-skin-laks-teriyaki)?",
                "answer": "Teriyaki er soja-sød. Miso er dybere, mere fermenteret umami — mindre sticky, mere rund.",
            },
            {
                "question": "Rød miso?",
                "answer": "Brug halv dosis. Den er saltigere og mere aggressiv. Shiro er standard her.",
            },
            {
                "question": "Uden skind?",
                "answer": "Ja, men hold øje 1 minut tidligere. Skindet beskytter og bliver sprødt nedad.",
            },
            {
                "question": "Brænder glazen?",
                "answer": "For meget honning eller for høj varme. 190 °C. Pensl tykt, men ikke dryppende.",
            },
        ],
        "body": "Miso-sesam-laks er umami på turbo: miso, honning, sesam, 10 minutter.\n\nIkke teriyaki. Fermenteret dybde. Karamelkant.",
        "tip": "Dup skindet tørt, før laksen går i kurven. Vådt skind damper i stedet for at knase.",
    },
    {
        "title": "Ristede marvben med persillesalat i airfryer",
        "slug": "marvben-persillesalat-airfryer",
        "description": "Flækkede marvben i airfryer på 12–15 minutter med groft salt og klassisk persillesalat — grej-nørderi til oksetatar.",
        "prepTime": "PT15M",
        "cookTime": "PT15M",
        "totalTime": "PT30M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": [
            "marvben",
            "persillesalat",
            "grej",
            "forret",
            "umami",
            "tatar",
            "oksekød",
            "festmad",
        ],
        "relatedGrej": ["airfryer-tilbehoer"],
        "imageAlt": "Ristede marvben fra airfryeren med persillesalat og ristet brød",
        "ingredients": [
            "4–6 flækkede marvben (canoe-cut)",
            "Flagesalt",
            "Persillesalat: 1 bundt flatbladet persille, 1 sjalotteløg, 1 spsk kapers, 1 spsk citronsaft, 2 spsk olivenolie",
            "Ristet surdejsbrød eller [rugbrødschips](/opskrifter/airfryer/rugbroedschips-airfryer)",
        ],
        "steps": [
            "Dup marvbenene tørre. Salt let cut-side. Forvarm airfryer til 200 °C.",
            "Læg cut-side op. Airfry 12–15 minutter, til marven bobler og er gennemvarm som smør. Ikke længere — den bliver tør.",
            "Hak persille groft. Vend med sjalot, kapers, citron, olie og salt.",
            "Server marvben varme med persillesalat og brød. Ske marven ud. Også til [grovhakket oksetatar](/opskrifter/pande/oksetatar-sennepskorn-estragon).",
        ],
        "faq": [
            {
                "question": "Ovn eller grill?",
                "answer": "Ja — se [bagt marvben](/opskrifter/ovn/bagt-marvben-persillesalat) og [røget marvben](/opskrifter/grill/roget-marvben-persillesalat). Airfryer er hurtigst og mest koncentreret varme.",
            },
            {
                "question": "Hel marvben?",
                "answer": "Nej til airfryer. Flækket canoe-cut. Hel kræver længere tid og er svær at anrette.",
            },
            {
                "question": "Fedt i kurven?",
                "answer": "Læg en skål eller bagepapir under, hvis din model drypper. Eller tøm kurven efter.",
            },
            {
                "question": "Til tatar?",
                "answer": "Perfekt. Varm marv på koldt kød — eller brød først, tatar ved siden af.",
            },
        ],
        "body": "Marvben i airfryer er grej-flex uden ovn-ventetid: 15 minutter, boblende marv, persille der klipper fedtet.\n\nSalt. Brød. Ske.",
        "tip": "Køb canoe-cut hos slagteren. At flække selv kræver sav — og tålmodighed du ikke har en tirsdag.",
    },
    {
        "title": "Sprøde svinebryst-bites med æbleglaze",
        "slug": "svinebryst-bites-aebleglasur-airfryer",
        "description": "Pork belly bites i airfryer med æbleglaze — sprød kant, sticky æble-sødme på under 25 minutter.",
        "prepTime": "PT10M",
        "cookTime": "PT18M",
        "totalTime": "PT28M",
        "servings": 4,
        "difficulty": "nem",
        "tags": [
            "svinebryst",
            "pork belly",
            "æble",
            "glaze",
            "snack",
            "party",
            "weekend",
            "sprød",
        ],
        "relatedGrej": ["airfryer-tilbehoer", "oliesprayflasker-airfryer"],
        "imageAlt": "Sprøde svinebryst-bites med blank æbleglaze og forårsløg",
        "ingredients": [
            "600 g svinebryst uden knogler, i 2–3 cm tern",
            "1 tsk salt, peber",
            "1 tsk bagepulver (valgfrit, ekstra knas)",
            "Glaze: 2 spsk æblegele eller æblemost reduceret + 1 spsk æblecidereddike, 1 spsk brun farin, 1 tsk dijonsennep, 1 knivspids kanel",
            "Forårsløg eller syrlige æbleskiver til servering",
        ],
        "steps": [
            "Dup ternene tørre. Vend med salt, peber og bagepulver.",
            "Airfry 200 °C i 12 minutter. Vend. 4–5 minutter mere, til kanterne er dybt gyldne.",
            "Rør glazen. Vend de varme bites i den. 1–2 minutter mere, til det bobler og klæber.",
            "Forårsløg. Server med det samme — weekend-snack eller gæstemad.",
        ],
        "faq": [
            {
                "question": "Forskel på [Hot Honey pork belly bites](/opskrifter/airfryer/hot-honey-pork-belly-bites)?",
                "answer": "Hot Honey er chili-honning. Her er æble, eddike og sennep — mere nordisk sticky, mindre streetfood-varme.",
            },
            {
                "question": "Uden æblegele?",
                "answer": "Reducer 1 dl æblemost med farin til sirup. Eller brug æblemos siet + eddike.",
            },
            {
                "question": "Med svær?",
                "answer": "Svær-side op, ekstra 3–4 minutter. Eller se [tørsaltet flæskestegssnack](/opskrifter/airfryer/torsaltet-flaeskestegssnack).",
            },
            {
                "question": "For sødt?",
                "answer": "Mere eddike og sennep i glazen. Æble skal bide, ikke slikke.",
            },
        ],
        "body": "Svinebryst-bites med æbleglaze er fedt, salt og knas — med efterår i glazen.\n\nSprød først. Sticky til sidst.",
        "tip": "Glaze først når kødet er sprødt. Sukker for tidligt = bitter kant, blød midte.",
    },
    {
        "title": "Hasselback-butternut med salvie og brunet smør",
        "slug": "hasselback-butternut-salvie-brunet-smoer",
        "description": "Hasselback-skåret butternut i airfryer med salvie og brunet smør — sprøde kanter, blød midte hurtigere end ovnen.",
        "prepTime": "PT15M",
        "cookTime": "PT25M",
        "totalTime": "PT40M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": [
            "hasselback",
            "butternut",
            "græskar",
            "salvie",
            "brunet smør",
            "vegetar",
            "efterår",
            "vinter",
        ],
        "relatedGrej": ["airfryer-tilbehoer"],
        "imageAlt": "Hasselback-butternut med brunet smør og frisk salvie",
        "ingredients": [
            "1 butternut (ca. 1 kg), halveret på langs, kerner skrabet ud",
            "2 spsk olivenolie",
            "Flagesalt og peber",
            "75 g smør",
            "8–10 friske salvieblade",
            "Evt. reven parmesan til servering",
        ],
        "steps": [
            "Læg halvcylindrene cut-side ned. Skær hasselback-snit på tværs med 3–4 mm mellemrum — stop før bunden (læg spisepinde langs siderne som stop).",
            "Pensl med olie. Salt og peber. Airfry 180 °C i 20–25 minutter, til midten er blød og kanterne gyldne. Pensl med mere olie halvvejs.",
            "Brun smørret med salvieblade, til smørret er nøddeagtigt og salvien sprød.",
            "Hæld brunet smør og salvie over butternut. Flagesalt. Evt. parmesan. Server som tilbehør eller vegetarisk hovedret.",
        ],
        "faq": [
            {
                "question": "Hokkaido i stedet?",
                "answer": "Ja — se også [græskarbåde med rosmarin](/opskrifter/airfryer/graeskarbaade-rosmarin). Butternut er sødere og nemmere at hasselback'e.",
            },
            {
                "question": "Forskel på [hasselback-kartofler](/opskrifter/airfryer/hasselback-kartofler)?",
                "answer": "Samme snit. Butternut er sødere og blødere — lavere varme, mere smør-salvie.",
            },
            {
                "question": "Skræl af?",
                "answer": "Nej. Skrællen holder formen. Den bliver spiselig efter stegning.",
            },
            {
                "question": "Ovn?",
                "answer": "200 °C i 35–45 minutter. Airfryer er hurtigere og giver mere kant.",
            },
        ],
        "body": "Hasselback-butternut er efterårsskåret til airfryer: snit, varmluft, brunet smør, salvie.\n\nKanter knaser. Midten bliver dessertagtig. Fedtet binder.",
        "tip": "Spisepinde langs siderne stopper kniven. Uden dem skærer du igennem — og det falder fra hinanden.",
    },
    {
        "title": "Ristet blomkål med tahin-dressing og granatæble",
        "slug": "blomkaal-tahin-granataeble-airfryer",
        "description": "Airfryer-ristet blomkål med tahin-dressing og granatæble — nøddeagtig Maillard, ikke dampet grønt.",
        "prepTime": "PT15M",
        "cookTime": "PT18M",
        "totalTime": "PT33M",
        "servings": 4,
        "difficulty": "nem",
        "tags": [
            "blomkål",
            "tahin",
            "granatæble",
            "vegetar",
            "hverdag",
            "mellemøstlig",
            "efterår",
            "vinter",
        ],
        "relatedGrej": ["airfryer-tilbehoer"],
        "imageAlt": "Ristet blomkål med tahin-dressing, granatæblekerner og persille",
        "ingredients": [
            "1 stort blomkålshoved, i buketter",
            "2 spsk olivenolie",
            "1 tsk spidskommen",
            "Flagesalt og peber",
            "Dressing: 3 spsk [tahin-dressing](/opskrifter/dips/tahin-dressing) eller 3 spsk tahin + 2 spsk citron + 1 fed hvidløg + vand til konsistens",
            "½ granatæble, kerner",
            "Frisk persille",
        ],
        "steps": [
            "Vend blomkålsbuketter med olie, spidskommen, salt og peber.",
            "Airfry 200 °C i 15–18 minutter, ryst halvvejs, til kanterne er dybt brune — ikke blege.",
            "Rør dressingen. Den skal kunne dryppe, ikke klumpe.",
            "Anret blomkål. Dryp tahin. Drys granatæble og persille. Server lun.",
        ],
        "faq": [
            {
                "question": "Forskel på [brændt blomkålssalat](/opskrifter/airfryer/braendt-blomkaalssalat-hasselnodder)?",
                "answer": "Den er hasselnødder og syre. Her er tahin og granatæble — cremet og sødsyrlig.",
            },
            {
                "question": "Blomkålen bliver dampet?",
                "answer": "Kurven er for fuld. Ét lag. To hold er bedre end grød.",
            },
            {
                "question": "Uden granatæble?",
                "answer": "Tørrede tranebær eller finthakkede æbler. Granatæble er bedst til knas og syre.",
            },
            {
                "question": "Hovedret?",
                "answer": "Med kikærter i kurven de sidste 8 minutter, eller quinoa ved siden af.",
            },
        ],
        "body": "Ristet blomkål med tahin er Maillard, ikke skolemad: høj varme, brune kanter, cremet dressing, granatæble der popper.\n\nDamp er fjenden. Brun er målet.",
        "tip": "Tør blomkålen efter vask. Våde buketter damper sig selv bløde.",
    },
    {
        "title": "Hjemmelavede forårsruller i airfryer",
        "slug": "hjemmelavede-foraarsruller-airfryer",
        "description": "Hjemmelavede forårsruller i airfryer — sprød wrap uden frituregryde, klar som party-snack på under 30 minutter.",
        "prepTime": "PT25M",
        "cookTime": "PT12M",
        "totalTime": "PT37M",
        "servings": 4,
        "difficulty": "mellem",
        "tags": [
            "forårsruller",
            "party",
            "snack",
            "asiatisk",
            "sprød",
            "hjemmelavet",
            "fyld",
        ],
        "relatedGrej": ["airfryer-tilbehoer", "oliesprayflasker-airfryer"],
        "imageAlt": "Sprøde hjemmelavede forårsruller fra airfryeren med dip",
        "ingredients": [
            "12 forårsrulle-wrappers (frosne, tøet)",
            "Fyld: 200 g hakket kylling eller rejer, 150 g hvidkål finthakket, 1 gulerod julienne, 2 forårsløg, 1 fed hvidløg, 1 tsk ingefær, 1 spsk soja, peber",
            "1 æg til at limme kanterne",
            "Oliespray eller 1 spsk olie til pensling",
            "Dip: sojasauce, chili, lime — eller sød chilisauce",
        ],
        "steps": [
            "Svits hvidløg og ingefær kort. Tilsæt kød/rejer, kål, gulerod og forårsløg. Soja. Steg til fyldet er tørt — vådt fyld ødelægger wrap. Køl.",
            "Læg wrapper som ruder. 1–2 spsk fyld. Fold sider ind, rull stramt. Pensl kant med æg.",
            "Pensl eller spray let med olie. Airfry 190 °C i 10–12 minutter, vend halvvejs, til dybt gyldne.",
            "Server med det samme med dip.",
        ],
        "faq": [
            {
                "question": "Frosne færdigruller?",
                "answer": "Se [frosne forårsruller](/opskrifter/airfryer/frosne-foraarsruller). Her er fyldet dit — og knaset tættere.",
            },
            {
                "question": "Vegetarisk fyld?",
                "answer": "Shiitake, kål, gulerod, glasnudler. Steg fugten væk først.",
            },
            {
                "question": "Wrappers sprækker?",
                "answer": "De er for tørre. Dæk med fugtig klud mens du ruller. Ikke for meget fyld.",
            },
            {
                "question": "Rispapir i stedet?",
                "answer": "Anden teknik — se [crispy rispapir-dumplings](/opskrifter/airfryer/crispy-rispapir-dumplings).",
            },
        ],
        "body": "Hjemmelavede forårsruller i airfryer er party uden oliebad: stram rulle, let olie, høj varme.\n\nFyldet skal være tørt. Wrap'en skal være stram. Resten er knas.",
        "tip": "Køl fyldet før du ruller. Varmt fyld damper wrappers bløde indefra.",
    },
    {
        "title": "Wonton-chips i airfryer",
        "slug": "wontonchips-airfryer",
        "description": "Sprøde wonton-chips i airfryer på få minutter — party-snack eller knasende base til tun- og laksetatar.",
        "prepTime": "PT5M",
        "cookTime": "PT5M",
        "totalTime": "PT10M",
        "servings": 4,
        "difficulty": "nem",
        "tags": [
            "wonton",
            "chips",
            "snack",
            "party",
            "tatar",
            "sprød",
            "tilbehør",
            "antipasti",
        ],
        "relatedGrej": ["airfryer-tilbehoer", "oliesprayflasker-airfryer"],
        "imageAlt": "Gyldne wonton-chips med flagesalt fra airfryeren",
        "ingredients": [
            "20 wonton-skaller (firkantede)",
            "1–2 spsk neutral olie eller oliespray",
            "Flagesalt",
            "Valgfrit: sesamfrø, chili-flager, fem-krydderi",
        ],
        "steps": [
            "Skær skallerne i trekanter eller strimler. Pensl eller spray let med olie på begge sider.",
            "Læg i ét lag i kurven. Drys flagesalt.",
            "Airfry 160 °C i 3–5 minutter, til de er oppustede og gyldne. Hold øje — de går fra perfekt til brændt på 30 sekunder.",
            "Køl på rist. Server til [tun-tatar med sriracha](/opskrifter/antipasti/tuntatar-sriracha-mayo-sesam) eller [laksetatar](/opskrifter/airfryer/laksetatar-rugbroedschips-airfryer).",
        ],
        "faq": [
            {
                "question": "Rispapir i stedet?",
                "answer": "Ja — samme metode, ofte 1 minut kortere. Wonton er tykkere og mere cracker-agtig.",
            },
            {
                "question": "Til dip?",
                "answer": "Ja. Chili-mayo, [aioli](/opskrifter/dips/aioli) eller soya-ingefær. Eller bare salt.",
            },
            {
                "question": "Holder de?",
                "answer": "Lufttæt dåse 1–2 dage. Genopfrisk 1 minut ved 150 °C.",
            },
            {
                "question": "For brune?",
                "answer": "For høj varme eller for lang tid. 160 °C. Første batch er din kalibrering.",
            },
        ],
        "body": "Wonton-chips er sprødhed uden friture: olie, salt, 4 minutter.\n\nTil tatar. Til dip. Til øl.",
        "tip": "Ét lag. Stablede wrappers limer sig sammen og bliver sej midt i.",
    },
    {
        "title": "Æble- og kanelsnegle i airfryer",
        "slug": "aeblesnegle-airfryer",
        "description": "Saftige æble-kanelsnegle bagt i airfryer-bageform — gærbage med æblefyld, uden at tænde den store ovn.",
        "prepTime": "PT1H15M",
        "cookTime": "PT18M",
        "totalTime": "PT1H35M",
        "servings": 8,
        "difficulty": "mellem",
        "tags": [
            "æblesnegle",
            "kanelsnegle",
            "bagværk",
            "æble",
            "kanel",
            "gær",
            "efterår",
            "kaffe",
        ],
        "relatedGrej": ["airfryer-tilbehoer", "bagestaal-til-airfryer"],
        "imageAlt": "Æble-kanelsnegle i bageform fra airfryeren med glasur",
        "ingredients": [
            "Dej: 2 dl lunken mælk, 25 g frisk gær, 50 g sukker, 1 æg, ½ tsk salt, 75 g blødt smør, 400 g hvedemel",
            "Fyld: 60 g blødt smør, 80 g brun farin, 2 spsk kanel, 2 syrlige æbler i små tern (tørret af), 1 knivspids salt",
            "1 lille smurt bageform eller ovnfast fad der passer i airfryeren (ca. 18–20 cm)",
            "Glasur: 6 spsk flormelis + 1–2 tsk æblesaft eller citron",
        ],
        "steps": [
            "Rør gær ud i mælk med sukker. Tilsæt æg, salt, smør og mel. Ælt blød dej. Hæv tildækket 45–60 minutter.",
            "Rul ud til ca. 30×40 cm. Smør med smør. Fordel farin, kanel og æbletern. Rul stramt. Skær 8 snegle.",
            "Læg sneglerne tæt i den smurte form. Efterhæv 15 minutter. Forvarm airfryer til 160 °C.",
            "Bag formen 15–18 minutter, til midten er gennembagt. Dæk med folie hvis toppen bruner for hurtigt. Glasur på lunkne snegle.",
        ],
        "faq": [
            {
                "question": "Forskel på [kanelsnegle](/opskrifter/airfryer/kanelsnegle)?",
                "answer": "Klassiske kanelsnegle er kanel-farin. Her er æbletern i fyldet, og de bages samlet i form — mere saftig, mere kageagtig.",
            },
            {
                "question": "Uden form?",
                "answer": "Læg 3–4 snegle på bagepapir med plads — som klassiske kanelsnegle. Formen giver blødere sider.",
            },
            {
                "question": "Æblerne gør dejen våd?",
                "answer": "Dup ternene tørre. Syrlige æbler (Ingrid Marie, Granny). Undgå store stykker.",
            },
            {
                "question": "Færdigdej?",
                "answer": "Ja — rul [færdig kanelsnegle-dej](/opskrifter/airfryer/kanelsnegle-faerdigdej) ud, tilsæt æble, form. Hurtigere, mindre hæve-flex.",
            },
        ],
        "body": "Æble-kanelsnegle i airfryer er gærbage til kaffebordet: smør, kanel, æble, form.\n\nIkke bare kanelsnegle med pynt. Æblet er fyldet.",
        "tip": "Formen skal kunne stå frit i kurven. Mål din airfryer, før du smører fadet.",
    },
]


def yaml_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def to_mdx(d: dict) -> str:
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
category: {CAT}
description: {yaml_str(d["description"])}
prepTime: "{d["prepTime"]}"
cookTime: "{d["cookTime"]}"
totalTime: "{d["totalTime"]}"
servings: {d["servings"]}
difficulty: {d["difficulty"]}
tags:
{tags}
{grej}image: /recipes/{CAT}/{slug}.jpg
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
    assert len(RECIPES) == 9, f"expected 9 recipes, got {len(RECIPES)}"
    slugs = [r["slug"] for r in RECIPES]
    assert len(slugs) == len(set(slugs)), "duplicate slugs"

    out = ROOT / CAT
    out.mkdir(parents=True, exist_ok=True)
    (PUBLIC / CAT).mkdir(parents=True, exist_ok=True)

    written = []
    for d in RECIPES:
        assert len(d["faq"]) >= 3, d["slug"]
        assert d.get("tip")
        assert len(d["ingredients"]) >= 3
        assert len(d["steps"]) >= 3
        path = out / f"{d['slug']}.mdx"
        if path.exists():
            raise SystemExit(f"slug collision: {path}")
        path.write_text(to_mdx(d), encoding="utf-8")
        written.append(d["slug"])
        print("wrote", f"{CAT}/{path.name}")

    print(f"done: {len(written)} recipes")


if __name__ == "__main__":
    main()
