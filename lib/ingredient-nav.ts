/** Client-safe råvare-meta (ingen fs / recipes-import). */

export interface IngredientNavItem {
  slug: string;
  name: string;
  /** Aliases/ordstammer matched mod normaliserede ingredienslinjer. */
  match: readonly string[];
  /** Valgfri sæson-slugs (foraar/sommer/efteraar/vinter) til senere hints. */
  seasonSlugs?: readonly string[];
}

/**
 * Kurateret råvarekatalog til /raavare-indeks.
 * Match kun konkrete aliases — undgå generisk «olie», «salt», «peber», «vand».
 */
export const INGREDIENT_NAV: readonly IngredientNavItem[] = [
  // A
  {
    slug: "agurk",
    name: "Agurk",
    match: ["agurk", "agurker", "agurkesalat"],
    seasonSlugs: ["sommer"],
  },
  {
    slug: "ananas",
    name: "Ananas",
    match: ["ananas"],
  },
  {
    slug: "and",
    name: "And",
    match: ["and", "andesteg", "andebryst", "andeoverlår", "andeoverlaar", "andefedt"],
  },
  {
    slug: "appelsin",
    name: "Appelsin",
    match: ["appelsin", "appelsiner", "appelsinsaft", "appelsinskal"],
    seasonSlugs: ["vinter"],
  },
  {
    slug: "asparges",
    name: "Asparges",
    match: ["asparges", "aspargesbundt"],
    seasonSlugs: ["foraar"],
  },
  {
    slug: "aubergine",
    name: "Aubergine",
    match: ["aubergine", "auberginer"],
    seasonSlugs: ["sommer"],
  },
  {
    slug: "avocado",
    name: "Avocado",
    match: ["avocado", "avocadoer", "avokado", "avokadoer"],
  },
  {
    slug: "aeble",
    name: "Æble",
    match: ["æble", "æbler", "aeble", "aebler", "æblemos", "æbleeddike"],
    seasonSlugs: ["efteraar"],
  },
  {
    slug: "aeg",
    name: "Æg",
    match: ["æg", "aeg", "æggeblomme", "æggehvide", "æggeblommer", "æggehvider"],
  },
  {
    slug: "aerter",
    name: "Ærter",
    match: [
      "ærter",
      "aerter",
      "grønne ærter",
      "frosne ærter",
      "ærtepure",
      "aertepure",
    ],
    seasonSlugs: ["foraar", "sommer"],
  },

  // B
  {
    slug: "bacon",
    name: "Bacon",
    match: ["bacon", "bacontern", "baconskiver"],
  },
  {
    slug: "banan",
    name: "Banan",
    match: ["banan", "bananer"],
  },
  {
    slug: "basilikum",
    name: "Basilikum",
    match: ["basilikum"],
    seasonSlugs: ["sommer"],
  },
  {
    slug: "blaabaer",
    name: "Blåbær",
    match: ["blåbær", "blaabaer"],
    seasonSlugs: ["sommer"],
  },
  {
    slug: "bladselleri",
    name: "Bladselleri",
    match: ["bladselleri"],
  },
  {
    slug: "blomkaal",
    name: "Blomkål",
    match: ["blomkål", "blomkaal"],
    seasonSlugs: ["efteraar", "vinter"],
  },
  {
    slug: "broccoli",
    name: "Broccoli",
    match: ["broccoli"],
    seasonSlugs: ["sommer", "efteraar"],
  },
  {
    slug: "brombaer",
    name: "Brombær",
    match: ["brombær", "brombaer"],
    seasonSlugs: ["sommer", "efteraar"],
  },
  {
    slug: "butternut",
    name: "Butternut",
    match: ["butternut", "butternutsquash"],
    seasonSlugs: ["efteraar"],
  },
  {
    slug: "boenner",
    name: "Bønner",
    match: [
      "bønner",
      "boenner",
      "hvide bønner",
      "sorte bønner",
      "kidneybønner",
      "kidney bønner",
      "grønne bønner",
      "haricots verts",
      "edamame",
      "edamamebønner",
    ],
  },

  // C
  {
    slug: "cashew",
    name: "Cashewnødder",
    match: ["cashew", "cashewnødder", "cashewnoedder", "cashewnød"],
  },
  {
    slug: "champignon",
    name: "Champignon",
    match: ["champignon", "champignoner", "svampe", "svamp", "shiitake", "portobello"],
    seasonSlugs: ["efteraar"],
  },
  {
    slug: "chili",
    name: "Chili",
    match: ["chili", "chilier", "chiliflager", "chilipulver", "frisk chili"],
  },
  {
    slug: "chokolade",
    name: "Chokolade",
    match: ["chokolade", "mørk chokolade", "mork chokolade", "hvid chokolade", "kakao"],
  },
  {
    slug: "citron",
    name: "Citron",
    match: ["citron", "citroner", "citronsaft", "citronskal"],
  },

  // D
  {
    slug: "dadler",
    name: "Dadler",
    match: ["dadler", "dadel"],
  },
  {
    slug: "dild",
    name: "Dild",
    match: ["dild"],
    seasonSlugs: ["sommer"],
  },

  // F
  {
    slug: "fennikel",
    name: "Fennikel",
    match: ["fennikel"],
    seasonSlugs: ["efteraar"],
  },
  {
    slug: "feta",
    name: "Feta",
    match: ["feta", "fetaost"],
  },
  {
    slug: "figen",
    name: "Figen",
    match: ["figen", "figner", "figenmarmelade"],
    seasonSlugs: ["efteraar"],
  },
  {
    slug: "fisk",
    name: "Fisk",
    match: ["fisk", "fiskefilet", "fiskefileter", "hvidfisk"],
  },
  {
    slug: "floede",
    name: "Fløde",
    match: ["fløde", "floede", "piskefløde", "piskefloede", "madlavningsfløde"],
  },
  {
    slug: "floedeost",
    name: "Flødeost",
    match: ["flødeost", "floedeost"],
  },
  {
    slug: "foraarsloeg",
    name: "Forårsløg",
    match: ["forårsløg", "foraarsloeg"],
    seasonSlugs: ["foraar", "sommer"],
  },

  // G
  {
    slug: "gedeost",
    name: "Gedeost",
    match: ["gedeost", "gedemælksost"],
  },
  {
    slug: "granataeble",
    name: "Granatæble",
    match: ["granatæble", "granataeble", "granatæbler", "granatæblekerner"],
    seasonSlugs: ["efteraar", "vinter"],
  },
  {
    slug: "graeskar",
    name: "Græskar",
    match: ["græskar", "graeskar", "græskarkerner"],
    seasonSlugs: ["efteraar"],
  },
  {
    slug: "groenkaal",
    name: "Grønkål",
    match: ["grønkål", "groenkaal"],
    seasonSlugs: ["efteraar", "vinter"],
  },
  {
    slug: "gulerod",
    name: "Gulerod",
    match: ["gulerod", "gulerødder", "guleroedder"],
    seasonSlugs: ["efteraar", "vinter"],
  },

  // H
  {
    slug: "hakket-koed",
    name: "Hakket kød",
    match: [
      "hakket kød",
      "hakket koed",
      "hakket oksekød",
      "hakket oksekoed",
      "hakket svinekød",
      "hakket svinekoed",
      "hakket kalv",
      "hakket kylling",
      "blandet hakket",
    ],
  },
  {
    slug: "halloumi",
    name: "Halloumi",
    match: ["halloumi"],
  },
  {
    slug: "hasselnodder",
    name: "Hasselnødder",
    match: ["hasselnødder", "hasselnodder", "hasselnød", "hasselnod"],
  },
  {
    slug: "havregryn",
    name: "Havregryn",
    match: ["havregryn"],
  },
  {
    slug: "havtorn",
    name: "Havtorn",
    match: ["havtorn"],
    seasonSlugs: ["efteraar"],
  },
  {
    slug: "hindbaer",
    name: "Hindbær",
    match: ["hindbær", "hindbaer"],
    seasonSlugs: ["sommer"],
  },
  {
    slug: "honning",
    name: "Honning",
    match: ["honning", "hot honey"],
  },
  {
    slug: "hokkaido",
    name: "Hokkaido",
    match: ["hokkaido"],
    seasonSlugs: ["efteraar"],
  },
  {
    slug: "hvidkaal",
    name: "Hvidkål",
    match: ["hvidkål", "hvidkaal"],
    seasonSlugs: ["efteraar", "vinter"],
  },
  {
    slug: "hvidloeg",
    name: "Hvidløg",
    match: ["hvidløg", "hvidloeg", "hvidløgsfed", "hvidløgspulver"],
  },

  // I
  {
    slug: "ingefaer",
    name: "Ingefær",
    match: ["ingefær", "ingefaer"],
  },

  // J
  {
    slug: "jordbaer",
    name: "Jordbær",
    match: ["jordbær", "jordbaer"],
    seasonSlugs: ["sommer"],
  },
  {
    slug: "jordskok",
    name: "Jordskok",
    match: ["jordskok", "jordskokker"],
    seasonSlugs: ["efteraar", "vinter"],
  },

  // K
  {
    slug: "kalkun",
    name: "Kalkun",
    match: ["kalkun", "kalkunbryst", "kalkunkød"],
  },
  {
    slug: "kanel",
    name: "Kanel",
    match: ["kanel", "kanelstang", "kanelstænger"],
  },
  {
    slug: "kantarel",
    name: "Kantarel",
    match: ["kantarel", "kantareller"],
    seasonSlugs: ["efteraar"],
  },
  {
    slug: "kapers",
    name: "Kapers",
    match: ["kapers"],
  },
  {
    slug: "kardemomme",
    name: "Kardemomme",
    match: ["kardemomme"],
  },
  {
    slug: "kartoffel",
    name: "Kartoffel",
    match: [
      "kartoffel",
      "kartofler",
      "kartoffelmos",
      "bagekartoffel",
      "bagekartofler",
      "nye kartofler",
    ],
    seasonSlugs: ["sommer", "efteraar"],
  },
  {
    slug: "kikaerter",
    name: "Kikærter",
    match: ["kikærter", "kikaerter", "kikært"],
  },
  {
    slug: "kirsebaer",
    name: "Kirsebær",
    match: ["kirsebær", "kirsebaer"],
    seasonSlugs: ["sommer"],
  },
  {
    slug: "knoldselleri",
    name: "Knoldselleri",
    match: ["knoldselleri"],
    seasonSlugs: ["efteraar", "vinter"],
  },
  {
    slug: "kokos",
    name: "Kokos",
    match: ["kokos", "kokosmælk", "kokosmaelk", "kokosmel", "kokosolie", "kokosflager"],
  },
  {
    slug: "kylling",
    name: "Kylling",
    match: [
      "kylling",
      "kyllingebryst",
      "kyllingelår",
      "kyllingelaar",
      "hel kylling",
      "kyllingevinger",
      "kyllingefars",
    ],
  },

  // L
  {
    slug: "laks",
    name: "Laks",
    match: ["laks", "laksefilet", "lakseside", "røget laks", "roget laks"],
  },
  {
    slug: "lam",
    name: "Lam",
    match: ["lam", "lammekød", "lammekoed", "lammesteg", "lammekoteletter"],
  },
  {
    slug: "laurbaerblad",
    name: "Laurbærblad",
    match: ["laurbærblad", "laurbaerblad", "laurbærblade", "laurbaerblade"],
  },
  {
    slug: "lime",
    name: "Lime",
    match: ["lime", "limer", "limesaft", "limeskal"],
  },
  {
    slug: "linser",
    name: "Linser",
    match: ["linser", "røde linser", "grønne linser", "belugalinser"],
  },
  {
    slug: "loeg",
    name: "Løg",
    match: ["løg", "loeg", "skalotteløg", "skalotteloeg", "rødløg", "roedloeg"],
  },

  // M
  {
    slug: "majs",
    name: "Majs",
    match: ["majs", "majskolbe", "majskolber"],
    seasonSlugs: ["sommer"],
  },
  {
    slug: "makrel",
    name: "Makrel",
    match: ["makrel", "røget makrel", "roget makrel"],
  },
  {
    slug: "mandler",
    name: "Mandler",
    match: ["mandler", "mandel", "mandelmel", "mandelmælk", "flagerede mandler"],
  },
  {
    slug: "mango",
    name: "Mango",
    match: ["mango", "mangoer"],
  },
  {
    slug: "mascarpone",
    name: "Mascarpone",
    match: ["mascarpone"],
  },
  {
    slug: "maelk",
    name: "Mælk",
    match: ["mælk", "maelk", "kærnemælk", "kaernemaelk"],
  },
  {
    slug: "melon",
    name: "Melon",
    match: ["melon", "vandmelon", "honningmelon", "cantaloupe"],
    seasonSlugs: ["sommer"],
  },
  {
    slug: "mozzarella",
    name: "Mozzarella",
    match: ["mozzarella"],
  },
  {
    slug: "muskatnoed",
    name: "Muskatnød",
    match: ["muskatnød", "muskatnoed", "muskat"],
  },
  {
    slug: "muslinger",
    name: "Muslinger",
    match: ["muslinger", "blåmuslinger", "blaamuslinger"],
  },
  {
    slug: "mynte",
    name: "Mynte",
    match: ["mynte", "frisk mynte"],
    seasonSlugs: ["sommer"],
  },

  // N
  {
    slug: "nelliker",
    name: "Nelliker",
    match: ["nelliker", "nellike"],
  },

  // O
  {
    slug: "oksekoed",
    name: "Oksekød",
    match: [
      "oksekød",
      "oksekoed",
      "oksemørbrad",
      "oksemoerbrad",
      "oksecuvette",
      "oksebryst",
      "entrecote",
      "ribeye",
      "hamburgerbøf",
      "hamburgerboef",
    ],
  },
  {
    slug: "oliven",
    name: "Oliven",
    match: ["oliven", "sorte oliven", "grønne oliven", "olivenolie"],
  },
  {
    slug: "oregano",
    name: "Oregano",
    match: ["oregano"],
  },

  // P
  {
    slug: "parmaskinke",
    name: "Parmaskinke",
    match: ["parmaskinke", "prosciutto"],
  },
  {
    slug: "parmesan",
    name: "Parmesan",
    match: ["parmesan", "parmigiano"],
  },
  {
    slug: "pastinak",
    name: "Pastinak",
    match: ["pastinak", "pastinakker"],
    seasonSlugs: ["efteraar", "vinter"],
  },
  {
    slug: "paere",
    name: "Pære",
    match: ["pære", "paere", "pærer", "paerer"],
    seasonSlugs: ["efteraar"],
  },
  {
    slug: "peberfrugt",
    name: "Peberfrugt",
    match: ["peberfrugt", "peberfrugter"],
    seasonSlugs: ["sommer"],
  },
  {
    slug: "peberrod",
    name: "Peberrod",
    match: ["peberrod"],
  },
  {
    slug: "persille",
    name: "Persille",
    match: ["persille", "bredbladet persille", "kruspersille"],
  },
  {
    slug: "persillerod",
    name: "Persillerod",
    match: ["persillerod", "persillerødder", "persillerodder"],
    seasonSlugs: ["efteraar", "vinter"],
  },
  {
    slug: "pinjekerner",
    name: "Pinjekerner",
    match: ["pinjekerner", "pinjekerne"],
  },
  {
    slug: "pistacie",
    name: "Pistacie",
    match: ["pistacie", "pistacier", "pistacienødder"],
  },
  {
    slug: "porre",
    name: "Porre",
    match: ["porre", "porrer"],
    seasonSlugs: ["efteraar", "vinter"],
  },
  {
    slug: "purloeg",
    name: "Purløg",
    match: ["purløg", "purloeg"],
    seasonSlugs: ["sommer"],
  },

  // R
  {
    slug: "rabarber",
    name: "Rabarber",
    match: ["rabarber"],
    seasonSlugs: ["foraar"],
  },
  {
    slug: "radiser",
    name: "Radiser",
    match: ["radise", "radiser"],
    seasonSlugs: ["foraar", "sommer"],
  },
  {
    slug: "ramslog",
    name: "Ramsløg",
    match: ["ramsløg", "ramslog", "ramsløgssalt"],
    seasonSlugs: ["foraar"],
  },
  {
    slug: "rejer",
    name: "Rejer",
    match: ["rejer", "rejefars", "scampi", "kæmpe rejer"],
  },
  {
    slug: "ribs",
    name: "Ribs",
    match: ["ribs", "ribsaft", "solbærsaft"],
    seasonSlugs: ["sommer"],
  },
  {
    slug: "ris",
    name: "Ris",
    match: ["ris", "grødris", "groedris", "jasminris", "basmatiris", "arborio", "risotto"],
  },
  {
    slug: "rosenkaal",
    name: "Rosenkål",
    match: ["rosenkål", "rosenkaal", "rosenkålene", "rosenkaalene"],
    seasonSlugs: ["efteraar", "vinter"],
  },
  {
    slug: "rosmarin",
    name: "Rosmarin",
    match: ["rosmarin"],
  },
  {
    slug: "roedbeder",
    name: "Rødbeder",
    match: ["rødbede", "roedbede", "rødbeder", "roedbeder"],
    seasonSlugs: ["efteraar"],
  },
  {
    slug: "roedkaal",
    name: "Rødkål",
    match: ["rødkål", "roedkaal"],
    seasonSlugs: ["efteraar", "vinter"],
  },
  {
    slug: "roedvin",
    name: "Rødvin",
    match: ["rødvin", "roedvin", "rødvinseddike"],
  },

  // S
  {
    slug: "rucola",
    name: "Rucola",
    match: ["rucola"],
    seasonSlugs: ["sommer"],
  },
  {
    slug: "salat",
    name: "Salat",
    match: ["salat", "hovedsalat", "romainesalat", "spinatsalat"],
    seasonSlugs: ["sommer"],
  },
  {
    slug: "salvie",
    name: "Salvie",
    match: ["salvie"],
  },
  {
    slug: "sennep",
    name: "Sennep",
    match: ["sennep", "dijonsennep", "grov sennep"],
  },
  {
    slug: "sesam",
    name: "Sesam",
    match: ["sesam", "sesamfrø", "sesamfro"],
  },
  {
    slug: "sild",
    name: "Sild",
    match: ["sild", "marinerede sild", "kryddersild"],
  },
  {
    slug: "skyr",
    name: "Skyr",
    match: ["skyr"],
  },
  {
    slug: "smoer",
    name: "Smør",
    match: ["smør", "smoer", "brunet smør", "clarified butter"],
  },
  {
    slug: "soede-kartofler",
    name: "Søde kartofler",
    match: ["søde kartofler", "soede kartofler", "sød kartoffel", "batat"],
  },
  {
    slug: "spidskaal",
    name: "Spidskål",
    match: ["spidskål", "spidskaal", "spids kål"],
    seasonSlugs: ["efteraar", "vinter"],
  },
  {
    slug: "spinat",
    name: "Spinat",
    match: ["spinat", "babyspinat"],
    seasonSlugs: ["foraar", "sommer"],
  },
  {
    slug: "squash",
    name: "Squash",
    match: ["squash", "zucchini"],
    seasonSlugs: ["sommer"],
  },
  {
    slug: "svinekoed",
    name: "Svinekød",
    match: [
      "svinekød",
      "svinekoed",
      "svinemørbrad",
      "svinemoerbrad",
      "svinekam",
      "svinebryst",
      "flæskesteg",
      "flaeskesteg",
      "koteletter",
      "nakkekoteletter",
    ],
  },

  // T
  {
    slug: "tahin",
    name: "Tahin",
    match: ["tahin", "tahini"],
  },
  {
    slug: "timian",
    name: "Timian",
    match: ["timian"],
  },
  {
    slug: "tomat",
    name: "Tomat",
    match: [
      "tomat",
      "tomater",
      "cherrytomater",
      "hakkede tomater",
      "tomatpuré",
      "tomatpure",
      "passata",
      "soltørrede tomater",
      "soltorrede tomater",
    ],
    seasonSlugs: ["sommer"],
  },
  {
    slug: "torsk",
    name: "Torsk",
    match: ["torsk", "torskefilet", "torskerogn"],
  },
  {
    slug: "tranebaer",
    name: "Tranebær",
    match: ["tranebær", "tranebaer"],
  },
  {
    slug: "tun",
    name: "Tun",
    match: ["tun", "tunfilet", "dåsetun", "dassetun"],
  },

  // V
  {
    slug: "valnoedder",
    name: "Valnødder",
    match: ["valnødder", "valnoedder", "valnød"],
  },
  {
    slug: "vanilje",
    name: "Vanilje",
    match: ["vanilje", "vaniljestang", "vaniljesukker", "vaniljeekstrakt"],
  },

  // Y
  {
    slug: "yoghurt",
    name: "Yoghurt",
    match: ["yoghurt", "græsk yoghurt", "graesk yoghurt", "tykmælk", "tykmaelk", "ymer"],
  },
];

export function getIngredientNav(): readonly IngredientNavItem[] {
  return INGREDIENT_NAV;
}

export function ingredientNavBySlug(
  slug: string
): IngredientNavItem | undefined {
  return INGREDIENT_NAV.find((item) => item.slug === slug);
}
