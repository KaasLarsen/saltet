import { INGREDIENT_NAV } from "@/lib/ingredient-nav";

/** Kuraterede opskriftsidéer til udvalgte råvaresider. */

export interface IngredientIdea {
  title: string;
  description: string;
  /** Link til eksisterende opskrift, når der er et tæt match. */
  recipeHref?: string;
}

export interface IngredientIdeasEntry {
  slug: string;
  blurb: string;
  /** Foto til forside-teaser (gerne en opskrift hvor råvaren er synlig). */
  image: string;
  imageAlt: string;
  ideas: readonly IngredientIdea[];
}

export const INGREDIENT_IDEAS: readonly IngredientIdeasEntry[] = [
  {
    slug: "spidskaal",
    blurb:
      "Spidskål er mildere og hurtigere at tilberede end hvidkål, hvilket gør den ideel til travle hverdage.",
    image: "/recipes/airfryer/spidskaal.jpg",
    imageAlt: "Stegt spidskål i airfryer",
    ideas: [
      {
        title: "Stegt spidskål med brunet smør, hasselnødder og citron",
        description:
          "En enkel og smagfuld tilbehørsret, hvor den søde nøddeagtige smag fra smørret fremhæver kålen.",
        recipeHref:
          "/opskrifter/grill/grillet-spidskaal-brunet-smoer-hasselnodder",
      },
      {
        title: "Spidskålssalat med æble, dild og sennepsdressing",
        description:
          "En frisk, sprød salat, der passer perfekt til fisk, fjerkræ eller frikadeller.",
        recipeHref: "/opskrifter/palaeg/spidskaal-aeble-salat",
      },
      {
        title: "Lynstegt spidskål i wok med kylling, ingefær og soja",
        description:
          "En hurtig hverdagsret, hvor et halvt spidskål nemt kan bruges op.",
      },
      {
        title: "Bagte spidskålsbåde med tahindressing og sesam",
        description:
          "Halve eller kvarte spidskål bagt møre i ovnen, toppet med en cremet tahindressing og ristede sesamfrø.",
      },
      {
        title: "Spidskålswrap med krydret hakket oksekød og avocado",
        description:
          "Brug de store yderblade fra spidskålet som sprøde, sunde wraps i stedet for tortillapandekager.",
        recipeHref: "/opskrifter/airfryer/spidskaals-tacoskaller",
      },
      {
        title: "Flødestuvet spidskål med muskatnød og persille",
        description:
          "En hurtig, moderne udgave af den klassiske stuvede hvidkål, der passer godt til frikadeller eller medister.",
        recipeHref: "/opskrifter/gryde/one-pot-floede-spidskaal-bacon",
      },
      {
        title: "Spidskålstacos med stegt fisk eller kikærter",
        description:
          "Fintsnittet spidskål vendt med lime og koriander fungerer som et sprødt og friskt fyld i tacos.",
      },
      {
        title: "Spidskåls-okonomiyaki (japansk kålpandekage)",
        description:
          "En smart måde at få brugt et halvt eller helt spidskål på ved at stege det sammen med æg, mel og forårsløg som en mættende madpandekage.",
        recipeHref: "/opskrifter/plancha/japansk-okonomiyaki",
      },
      {
        title: "Simreret spidskål med pølser og sennep i én gryde",
        description:
          "Groftsnittet spidskål der falder sammen i en cremet bouillon- og sennepssauce med stegte pølseskiver.",
      },
    ],
  },
  {
    slug: "rosenkaal",
    blurb:
      "Rosenkål har fået en renæssance og er oplagt i efterårs- og vinterhalvåret, især når de tilberedes ved høj varme.",
    image: "/recipes/airfryer/rosenkaal-balsamico.jpg",
    imageAlt: "Rosenkål med balsamico",
    ideas: [
      {
        title: "Bagte rosenkål med bacon, balsamico og parmesan",
        description:
          "Tilberedning i ovn gør rosenkålene sprøde og søde i stedet for bitre.",
        recipeHref: "/opskrifter/airfryer/rosenkaal-baconfedt-parmesan",
      },
      {
        title: "Rå rosenkålssalat med granatæble, appelsin og valnødder",
        description:
          "Fintsnittede rosenkål giver masser af bid og fungerer rigtig godt som vintersalat eller julesalat.",
      },
      {
        title: "Cremet pasta med rosenkål, hvidløg, citron og timian",
        description:
          "En nem vegetarisk ret, hvor kålen steges gylden på panden før den vendes i saucen.",
      },
      {
        title: "Rosenkål på pande med æbler, sennep og timian",
        description:
          "Halverede rosenkål stegt hårdt på panden sammen med æbletern og vendt i en grov sennepsglasering.",
      },
      {
        title: "Gratin med rosenkål, porre og cheddar",
        description:
          "En varm og mættende vinterret, hvor rosenkålene bages i en cremet ostesauce med sprødt rasp på toppen.",
      },
      {
        title: "Lynstegt rosenkål med chili, hvidløg og honning",
        description:
          "Et smagfuldt og let stærkt tilbehør, der gør rosenkål spændende selv for skeptikere.",
      },
      {
        title: "Rosenkåls-chips med flagesalt og parmesan",
        description:
          "Løse blade fra rosenkål vendt i lidt olie og bagt helt sprøde i ovnen eller airfryeren som en sund snack eller sprød topping.",
      },
      {
        title: "Lynstegt rosenkål med chorizo og hvide bønner",
        description:
          "En rustik, smagfuld hverdagsret på 15 minutter, hvor den krydrede chorizo giver masser af smag til kålen.",
      },
      {
        title: "Tærte med karamelliserede løg, rosenkål og gedeost",
        description:
          "En mættende efterårs- og vintertærte, hvor rosenkålene bages møre i æggemassen.",
      },
    ],
  },
  {
    slug: "hokkaido",
    blurb:
      "Hokkaido-græskar er taknemmeligt at arbejde med, fordi skrællen kan spises, og det har en lang holdbarhed.",
    image: "/recipes/gryde/hokkaido-graeskarsuppe-ingefaer.jpg",
    imageAlt: "Hokkaido-græskarsuppe med ingefær",
    ideas: [
      {
        title: "Cremet hokkaidosuppe med ingefær, kokosmælk og ristede kerner",
        description:
          "En klassiker, der er nem at lave i stor portion og fryse ned.",
        recipeHref: "/opskrifter/gryde/hokkaido-graeskarsuppe-ingefaer",
      },
      {
        title: "Bagte hokkaidobåde med feta, honning og timian",
        description:
          "Skåret i både og bagt i ovnen fungerer det både som tilbehør og som base i en lun salat.",
        recipeHref: "/opskrifter/ovn/bagte-graeskarbade-hokkaido-chili-feta",
      },
      {
        title: "Svampet hokkaidokage med kanel og flødeostecreme",
        description:
          "En oplagt måde at bruge en rest græskarpuré på i det søde køkken.",
      },
      {
        title: "Hokkaidopure med smør, salvie og hvidløg",
        description:
          "Et farverigt og sødmefuldt alternativ til kartoffelmos, der passer perfekt til efterårets gryderetter og stegt kød.",
      },
      {
        title: "Fyldt hokkaido med linser, feta og valnødder",
        description:
          "Et halvt udhulet græskar bagt i ovnen med et krydret vegetarisk fyld — en flot servering til gæster.",
        recipeHref: "/opskrifter/ovn/fyldte-hokkaido-halvdele",
      },
      {
        title: "Hokkaidoboller med græskarkerner",
        description:
          "Revet eller bagt hokkaido i bolledejen gør brødet ekstra saftigt og giver en flot gylden krumme.",
      },
      {
        title: "Hokkaidokarry med kikærter og spinat",
        description:
          "En varmende vegetarisk gryderet, hvor tern af hokkaido koger møre i kokosmælk og karry og giver en naturlig cremet konsistens.",
      },
      {
        title: "Ristede græskarkerner med paprika og salt",
        description:
          'En klassisk "red min mad"-opskrift, der lærer brugerne at udnytte kernerne i stedet for at smide dem ud.',
        recipeHref: "/opskrifter/ovn/ristede-graeskarkerner-roget-paprika",
      },
      {
        title: "Hokkaidorisotto med salvie og parmesan",
        description:
          "Revet eller ternet hokkaido kogt med i risottoen giver en smuk, gylden farve og en mild sødme.",
        recipeHref: "/opskrifter/gryde/graeskar-risotto-parmesan",
      },
    ],
  },
  {
    slug: "rucola",
    blurb:
      "Rucola mister hurtigt sin sprødhed i køleskabet, så opskrifter der bruger en hel bakke eller redder slatten rucola er meget værdifulde.",
    image: "/recipes/dips/rucolapesto.jpg",
    imageAlt: "Rucolapesto",
    ideas: [
      {
        title: "Rucolapesto med mandler, hvidløg og parmesan",
        description:
          'En genial "red min mad"-opskrift, der forlænger holdbarheden på en bakke rucola markant.',
        recipeHref: "/opskrifter/dips/rucolapesto",
      },
      {
        title: "Kartoffelpizza med rosmarin, mozzarella og frisk rucola",
        description:
          "En klassisk kombination, hvor rucolaen kommes på lige inden servering.",
      },
      {
        title: "Pastasalat med rucola, soltørrede tomater, feta og pinjekerner",
        description:
          "En fyldig salat til madpakken eller som tilbehør til grillmad.",
      },
      {
        title: "Omelet eller frittata med rucola, kartoffel og gedeost",
        description:
          "En nem måde at få brugt både en rest kogte kartofler og en pose rucola, der er ved at miste pusten.",
      },
      {
        title: "Rucolasmør med citron og hvidløg",
        description:
          "Finthakket rucola rørt i blødt smør — perfekt til at smelte oven på en varm bøf, grillede grøntsager eller nybagt brød.",
      },
      {
        title: "Rugbrødssandwich med parmaskinke, mozzarella og rucola",
        description:
          "En hurtig frokostklassiker, hvor rucolaens pebrede smag giver modspil til den fede ost og salte skinke.",
      },
      {
        title: "Rucola- og kartoffelsuppe",
        description:
          "En grøn, let pebret kartoffelsuppe, hvor en hel bakke rucola blendes i til sidst for at give farve, smag og redde slatne blade.",
      },
      {
        title: "Grillet sandwich med cheddar, æble og rucola",
        description:
          "Varm toast hvor den friske rucola kommes i lige inden servering for at give sprødhed til den smeltede ost.",
      },
      {
        title: "Focaccia med rucola, cherrytomater og oliven",
        description:
          "Bagt direkte oven på dejen eller lagt på det lune brød med god olivenolie og flagesalt.",
        recipeHref:
          "/opskrifter/pizzaovn/focaccia-rosmarin-cherrytomater-pizzaovn",
      },
    ],
  },
  {
    slug: "purloeg",
    blurb:
      "Purløg bruges ofte kun som drys, så brugerne mangler ofte idéer til at få brugt et helt bundt op.",
    image: "/recipes/palaeg/kartoffelsalat.jpg",
    imageAlt: "Kartoffelsalat med purløg",
    ideas: [
      {
        title: "Purløgsolie",
        description:
          "Blendet purløg og neutral olie giver en smuk, grøn krydderolie, der holder sig længe og løfter supper, fisk og kartofler.",
      },
      {
        title: "Æggesalat med masser af purløg, skyr og sennep",
        description:
          "En klassiker til frokostbordet eller madpakken, hvor man sagtens kan bruge et stort bundt.",
      },
      {
        title: "Kartoffelsalat med purløg, radiser og creme fraiche-dressing",
        description:
          "En sommerfavorit, hvor purløg spiller hovedrollen i smagen.",
      },
      {
        title: "Purløgsflødeost eller rygeostecreme",
        description:
          "Finthakket purløg rørt i flødeost med lidt citron og peber — oplagt som dip, på bagels eller til røget laks.",
        recipeHref: "/opskrifter/palaeg/floedeost-urter",
      },
      {
        title: "Ostepandekager eller vafler med purløg",
        description:
          "Kom masser af friskklippet purløg direkte i dejen til salte madpandekager eller kartoffelvafler.",
      },
      {
        title: "Smørrebrød med æggestand og purløg",
        description:
          "En klassisk, dansk frokostfavorit, hvor purløg udgør et generøst grønt lag på toppen.",
      },
      {
        title: "Purløgssmør til majs, kartofler eller brød",
        description:
          "Et nemt kryddersmør med masser af frisk purløg og lidt citronskal, som kan rulles til en pølse og fryses ned i skiver.",
        recipeHref: "/opskrifter/roeremaskine/kryddersmoer-roeremaskine",
      },
      {
        title: "Røræg eller omeletsandwich med masser af purløg",
        description:
          "En simpel morgenmads- eller frokostopskrift, hvor purløg bruges i rigelige mængder frem for blot som pynt.",
        recipeHref: "/opskrifter/pande/aeggekage-bacon-purloeg",
      },
      {
        title: "Kold agurke- og yoghurtsuppe med purløg og dild",
        description:
          "En forfriskende sommersuppe eller forret, hvor krydderurterne giver hele karakteren.",
      },
    ],
  },
  {
    slug: "aerter",
    blurb:
      "Friske ærter er en kort sommerfavorit, mens frosne ærter er en uundværlig basisvare i fryseren året rundt.",
    image: "/recipes/dehydrator/wasabi-aerter-dehydrator.jpg",
    imageAlt: "Sprøde wasabi-ærter",
    ideas: [
      {
        title: "Ærtepure med mynte, citron og olivenolie",
        description:
          "Hurtigt tilbehør til laks eller kylling, som også fungerer godt som smørepålæg på ristet brød.",
      },
      {
        title: "Risotto med ærter, asparges og parmesan",
        description:
          "En frisk forårs- og sommerret, hvor ærterne giver både sødme og farve.",
      },
      {
        title: "Ærtesuppe med sprød bacon og cremefraiche",
        description:
          "En budgetvenlig og lynhurtig hverdagssuppe, der kan laves på under 20 minutter.",
      },
      {
        title: "Ærtehummus med tahin, hvidløg og spidskommen",
        description:
          "En frisk, lysegrøn dip til grøntsagsstave, pita eller som smørelse i sandwiches.",
      },
      {
        title: "Pasta med ærter, bacon, fløde og parmesan",
        description:
          "En cremet hverdagsfavorit, hvor de frosne ærter blot vendes i saucen de sidste to minutter.",
      },
      {
        title: "Ærtefrikadeller med feta og mynte",
        description:
          "Grønne vegetarfrikadeller lavet på blendede ærter, æg og havregryn — gode både varme til aftensmad og kolde i madpakken.",
      },
      {
        title: "Kold ærte- og myntesuppe med rygeost",
        description:
          "En hurtig, grøn sommersuppe på frosne eller friske ærter, der serveres kold med en skefuld rygeost i midten.",
      },
      {
        title: "Gnocchi med ærter, citron, smør og parmesan",
        description:
          "En 10-minutters hverdagsret på én pande, hvor søde ærter og frisk citron balancerer den salte ost.",
      },
      {
        title: "Kartoffel- og ærtecurry (Aloo Matar)",
        description:
          "En krydret, budgetvenlig indisk-inspireret gryderet baseret på to råvarer, de fleste allerede har i køkkenet.",
      },
    ],
  },
  {
    slug: "persillerod",
    blurb:
      "Persillerod er en overset dansk vinterrodfrugt, der ofte forveksles med pastinak, men har en fin, nøddeagtig smag af persille.",
    image: "/recipes/airfryer/pastinak-persillerod-fritter.jpg",
    imageAlt: "Pastinak- og persillerodsfritter fra airfryeren",
    ideas: [
      {
        title: "Bagte persillerødder med honning, timian og hasselnødder",
        description:
          "Enkel tilbehørsret, hvor rodfrugterne karamelliserer i ovnen.",
      },
      {
        title: "Cremet persillerodssuppe med sprød bacon og æbletern",
        description:
          "En fløjlsblød vintersuppe, hvor syren fra æblet balancerer den søde rod.",
      },
      {
        title: "Persillerodsmos med brunet smør",
        description:
          "Et smagfuldt alternativ til almindelig kartoffelmos til efterårets og vinterens simreretter.",
      },
    ],
  },
  {
    slug: "quinoa",
    blurb:
      "Quinoa er en proteinrig og glutenfri basisvare, som mange bruger i salater og som sundt alternativ til ris og pasta.",
    image: "/recipes/ovn/bagt-feta-quinoa-oliven.jpg",
    imageAlt: "Bagt feta med cherrytomater, oliven og quinoa",
    ideas: [
      {
        title:
          "Quinoasalat med bagt græskar, feta, granatæble og græskarkerner",
        description:
          "En mættende efterårs- og vintersalat, der holder sig god i flere dage.",
        recipeHref: "/opskrifter/ovn/bagt-feta-quinoa-oliven",
      },
      {
        title: "Quinoadeller med gulerod, forårsløg og spidskommen",
        description:
          "Sprøde vegetarfrikadeller, som fungerer godt både til aftensmad og i madpakken.",
      },
      {
        title: "One-pot quinoa med kylling, tomat og spinat",
        description:
          "En nem hverdagsret, hvor quinoaen koger direkte i saucen og suger masser af smag.",
      },
    ],
  },
  {
    slug: "hytteost",
    blurb:
      "Hytteost er en af de mest søgte ingredienser lige nu — især til proteinrige morgenmåltider, madpakker og bagværk.",
    image: "/recipes/ovn/hytteost-madboller-havregryn.jpg",
    imageAlt: "Hytteost-madboller med havregryn",
    ideas: [
      {
        title: "Hytteostboller med havregryn og kerner",
        description:
          "Hurtige, saftige boller uden hævetid, som er blevet en fast hverdagsfavorit hos mange.",
        recipeHref: "/opskrifter/ovn/hytteost-madboller-havregryn",
      },
      {
        title: "Vafler eller pandekager med hytteost og banan",
        description:
          "Mættende morgenmad, hvor hytteosten gør dejen ekstra svampet.",
        recipeHref: "/opskrifter/pande/proteinpandekager-hytteost",
      },
      {
        title: "Pisket hytteost med urter, citron og hvidløg",
        description:
          "En cremet og proteinrig dip eller smørelse til sandwich og rugbrød.",
        recipeHref: "/opskrifter/dips/hytteost-obatzda",
      },
    ],
  },
  {
    slug: "burrata",
    blurb:
      "Burrata er en cremet italiensk ost, der hurtigt løfter en simpel ret til gæstemad — populær i både salater og pastaretter.",
    image: "/recipes/antipasti/burrata-rucola-troeffelolie.jpg",
    imageAlt: "Burrata på rucola med trøffelolie",
    ideas: [
      {
        title: "Tomatsalat med burrata, basilikum og balsamico",
        description:
          "En sommerklassiker, der kræver minimal tilberedning.",
        recipeHref: "/opskrifter/antipasti/burrata-rucola-troeffelolie",
      },
      {
        title:
          "Pasta med bagte cherrytomater, hvidløg og hel burrata på toppen",
        description:
          "Når den kolde ost skæres op over den varme pasta, fungerer den som en cremet sauce.",
      },
      {
        title: "Bruschetta med grillet brød, parmaskinke, figner og burrata",
        description:
          "En oplagt forret eller tapasret med kontrast mellem sprødt, salt, sødt og cremet.",
        recipeHref:
          "/opskrifter/pizzaovn/bruschetta-hvidloeg-burrata-pizzaovn",
      },
    ],
  },
  {
    slug: "chorizo",
    blurb:
      "Chorizo er en krydret pølse med lang holdbarhed, der fungerer som en genial smagsgiver i alt fra gryderetter til tapas.",
    image: "/recipes/stobejern/shakshuka-chorizo.jpg",
    imageAlt: "Shakshuka med chorizo",
    ideas: [
      {
        title: "Pastaret med chorizo, peberfrugt, fløde og parmesan",
        description:
          "En hurtig hverdagsret på 20 minutter med masser af dybde fra pølsens krydderier.",
        recipeHref: "/opskrifter/stobejern/one-pot-pasta-chorizo",
      },
      {
        title: "Bagte kartofler eller kartoffelfad med chorizo, løg og rosmarin",
        description:
          "Pølsens paprikaolie giver smag og farve til kartoflerne i ovnen.",
      },
      {
        title: "Shakshuka med chorizo, hakkede tomater og pocherede æg",
        description:
          "En varmende brunch- eller aftensmadsklassiker på én pande.",
        recipeHref: "/opskrifter/stobejern/shakshuka-chorizo",
      },
    ],
  },
  {
    slug: "roedloeg",
    blurb:
      "Rødløg søges ofte specifikt — især til syltning, salater og ovnretter — selvom almindelige løg allerede er i indekset.",
    image: "/recipes/sylte/syltede-roedloeg.jpg",
    imageAlt: "Syltede rødløg",
    ideas: [
      {
        title: "Syltede rødløg",
        description:
          "En uundværlig basisopskrift til burgere, tacos, smørrebrød og salater.",
        recipeHref: "/opskrifter/sylte/syltede-roedloeg",
      },
      {
        title: "Tærte med karamelliserede rødløg, gedeost og timian",
        description:
          "En smuk og smagfuld tærte, hvor rødløgene bliver helt søde.",
        recipeHref: "/opskrifter/ovn/viral-upside-down-butterdejstaerter",
      },
      {
        title: "Rødløgskompot med rødvin og balsamico",
        description:
          "Perfekt tilbehør til ostebordet, stegt and eller en god bøf.",
      },
    ],
  },
];

const ideasBySlug = new Map(
  INGREDIENT_IDEAS.map((entry) => [entry.slug, entry])
);

export function getIngredientIdeas(
  slug: string
): IngredientIdeasEntry | undefined {
  return ideasBySlug.get(slug);
}

/** Råvarer med kuraterede idéer, filtreret til en sæson. */
export function getSeasonalProduceForSeason(
  seasonSlug: string
): IngredientIdeasEntry[] {
  return INGREDIENT_IDEAS.filter((entry) => {
    const nav = INGREDIENT_NAV.find((item) => item.slug === entry.slug);
    return nav?.seasonSlugs?.includes(seasonSlug) ?? false;
  });
}
