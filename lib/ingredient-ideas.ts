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
  ideas: readonly IngredientIdea[];
}

export const INGREDIENT_IDEAS: readonly IngredientIdeasEntry[] = [
  {
    slug: "spidskaal",
    blurb:
      "Spidskål er mildere og hurtigere at tilberede end hvidkål, hvilket gør den ideel til travle hverdage.",
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
    ],
  },
  {
    slug: "rosenkaal",
    blurb:
      "Rosenkål har fået en renæssance og er oplagt i efterårs- og vinterhalvåret, især når de tilberedes ved høj varme.",
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
    ],
  },
  {
    slug: "hokkaido",
    blurb:
      "Hokkaido-græskar er taknemmeligt at arbejde med, fordi skrællen kan spises, og det har en lang holdbarhed.",
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
    ],
  },
  {
    slug: "rucola",
    blurb:
      "Rucola mister hurtigt sin sprødhed i køleskabet, så opskrifter der bruger en hel bakke eller redder slatten rucola er meget værdifulde.",
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
    ],
  },
  {
    slug: "purloeg",
    blurb:
      "Purløg bruges ofte kun som drys, så brugerne mangler ofte idéer til at få brugt et helt bundt op.",
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
    ],
  },
  {
    slug: "aerter",
    blurb:
      "Friske ærter er en kort sommerfavorit, mens frosne ærter er en uundværlig basisvare i fryseren året rundt.",
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
