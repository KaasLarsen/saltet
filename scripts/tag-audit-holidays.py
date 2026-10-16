#!/usr/bin/env python3
"""Tag-audit — berig eksisterende opskrifter med højtid-tags (aug 2026)."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"

UPDATES: dict[str, list[str]] = {
    "airfryer/and.mdx": ["Mortensaften", "jul"],
    "ovn/spraengt-andebryst-roedkaal.mdx": ["Mortensaften"],
    "ovn/andelaar-i-fad-rodfrugter.mdx": ["Mortensaften", "jul"],
    "sous-vide/andebryst-sous-vide.mdx": ["Mortensaften"],
    "sous-vide/andelaar-sous-vide.mdx": ["Mortensaften", "jul"],
    "stobejern/stegte-andebryster-sproedt-skind.mdx": ["Mortensaften"],
    "stobejern/confiterede-andelaar.mdx": ["Mortensaften"],
    "trykkoger/roedkaal-trykkoger.mdx": ["Mortensaften", "jul"],
    "sylte/klassisk-roedkaal-andefedt.mdx": ["Mortensaften"],
    "grill/grillede-aebler-svesker.mdx": ["Mortensaften", "jul"],
    "ovn/gammeldags-flaeskesteg-sproede-svaer.mdx": ["jul"],
    "grill/kamsteg-sproed-svaer.mdx": ["jul"],
    "grill/flaeskesteg-porchetta-rotisseri.mdx": ["jul"],
    "grill/gaas-paa-grill.mdx": ["jul"],
    "grill/julegaas-rotisseri.mdx": ["jul"],
    "gryde/klassisk-risengrod.mdx": ["jul"],
    "trykkoger/risengrod-trykkoger.mdx": ["jul"],
    "pande/varme-aebleskiver-pande.mdx": ["jul"],
    "airfryer/norske-klejner.mdx": ["jul"],
    "airfryer/flaeskestegssandwich.mdx": ["jul"],
    "sous-vide/flaeskesteg-sous-vide.mdx": ["jul"],
    "palaeg/leverpostej.mdx": ["jul"],
    "palaeg/leverpostej-vildt.mdx": ["jul"],
    "palaeg/rullepoelse.mdx": ["jul", "påske"],
    "palaeg/kryddersild.mdx": ["jul", "påske"],
    "palaeg/karrysild.mdx": ["jul", "påske"],
    "palaeg/dildsild.mdx": ["jul"],
    "palaeg/sildesalat.mdx": ["jul"],
    "palaeg/sennepssalat.mdx": ["jul"],
    "palaeg/tomatsild.mdx": ["jul"],
    "sylte/klassiske-kryddersild.mdx": ["jul", "påske"],
    "sylte/roedvins-sild.mdx": ["jul"],
    "sylte/syltede-sild.mdx": ["jul", "påske"],
    "fermentering/fermenteret-roedkaal.mdx": ["jul"],
    "grill/tomahawk-steak.mdx": ["nytår"],
    "grill/cote-de-boeuf.mdx": ["nytår"],
    "grill/oksemoerbrad-paa-grill.mdx": ["nytår"],
    "grill/grillet-hummerhale.mdx": ["nytår"],
    "grill/grillede-jomfruhummere.mdx": ["nytår"],
    "plancha/jomfruhummere-paa-plancha.mdx": ["nytår"],
    "dips/champagnesauce.mdx": ["nytår"],
    "dips/troeffelmayo.mdx": ["nytår"],
    "roeg/koldroget-laks.mdx": ["nytår", "påske"],
    "palaeg/skaldyrssalat.mdx": ["nytår", "jul"],
    "grill/lammekoelle-rotisseri.mdx": ["påske"],
    "grill/grillede-lammeracks-sennep-urtekrust.mdx": ["påske"],
    "stobejern/langtidsstegt-lammekoelle.mdx": ["påske"],
    "sous-vide/lammekrone-sous-vide.mdx": ["påske"],
    "sous-vide/lammekoelle-sous-vide.mdx": ["påske"],
}


def quote_tag(tag: str) -> str:
    if re.search(r'[:#\[\]{}]', tag) or tag.startswith(("-", " ")):
        return f'"{tag}"'
    return tag


def parse_tags(content: str) -> tuple[re.Match[str] | None, list[str], str]:
    """Return match, tags, format ('list' | 'inline')."""
    m = re.search(r"^tags:\s*\n((?:  - .+\n)+)", content, re.MULTILINE)
    if m:
        tags = []
        for line in m.group(1).strip().split("\n"):
            val = line[4:].strip().strip('"').strip("'")
            tags.append(val)
        return m, tags, "list"
    m2 = re.search(r"^tags:\s*\[(.+)\]\s*$", content, re.MULTILINE)
    if m2:
        inner = m2.group(1)
        tags = [t.strip().strip('"').strip("'") for t in inner.split(",")]
        return m2, tags, "inline"
    return None, [], ""


def format_tags(tags: list[str], fmt: str) -> str:
    if fmt == "inline":
        inner = ", ".join(quote_tag(t) for t in tags)
        return f"tags: [{inner}]"
    lines = "\n".join(f"  - {quote_tag(t)}" for t in tags)
    return f"tags:\n{lines}\n"


def add_tags(content: str, new_tags: list[str]) -> tuple[str, bool]:
    m, existing, fmt = parse_tags(content)
    if m is None:
        return content, False
    merged = existing[:]
    changed = False
    for t in new_tags:
        if t not in merged:
            merged.append(t)
            changed = True
    if not changed:
        return content, False
    replacement = format_tags(merged, fmt)
    new_content = content[: m.start()] + replacement + content[m.end() :]
    return new_content, True


def main() -> None:
    updated = 0
    for rel, tags in UPDATES.items():
        path = ROOT / rel
        if not path.exists():
            print("skip missing", rel)
            continue
        content = path.read_text(encoding="utf-8")
        new_content, changed = add_tags(content, tags)
        if changed:
            path.write_text(new_content, encoding="utf-8")
            print("updated", rel)
            updated += 1
        else:
            print("ok", rel)
    print(f"done: {updated} files updated")


if __name__ == "__main__":
    main()
