#!/usr/bin/env python3
"""Tilføj affiliateProduct + relatedGrej på danske-klassikere batch (aug 2026)."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"
GUIDE = Path(__file__).resolve().parent.parent / "content/guides/danske-klassikere-guide.mdx"

# affiliateProduct + relatedGrej per opskrift
PATCHES: dict[str, dict[str, str | list[str]]] = {
    "gryde/boller-i-karry.mdx": {
        "relatedGrej": ["kobbergryder", "multihakker-loegsnitter"],
    },
    "gryde/klassisk-rodgroed.mdx": {
        "relatedGrej": ["kobbergryder"],
    },
    "gryde/koldskal.mdx": {
        "relatedGrej": ["kobbergryder"],
    },
    "trykkoger/boller-i-karry-trykkoger.mdx": {
        "affiliateProduct": "kitchenone-instant-pot",
        "relatedGrej": ["trykkoger-vs-slowcooker"],
    },
    "trykkoger/hjerter-i-floedesovs-trykkoger.mdx": {
        "affiliateProduct": "kitchenone-instant-pot",
        "relatedGrej": ["trykkoger-vs-slowcooker"],
    },
    "airfryer/stegt-flaesk.mdx": {
        "affiliateProduct": "homeshop-airfryer",
        "relatedGrej": ["airfryer-vs-ovn-opgoer", "oliesprayflasker-airfryer"],
    },
    "airfryer/stjerneskud-airfryer.mdx": {
        "affiliateProduct": "homeshop-airfryer",
        "relatedGrej": ["airfryer-vs-ovn-opgoer"],
    },
    "airfryer/krebinetter-airfryer.mdx": {
        "affiliateProduct": "homeshop-airfryer",
        "relatedGrej": ["airfryer-vs-ovn-opgoer"],
    },
    "airfryer/moerbradboeffer-airfryer.mdx": {
        "affiliateProduct": "homeshop-airfryer",
        "relatedGrej": ["airfryer-vs-ovn-opgoer", "instant-read-vs-bluetooth-termometer"],
    },
    "grill/stegt-flaesk-grill.mdx": {
        "affiliateProduct": "meater-plus",
        "relatedGrej": ["tradlost-stegetermometer", "traekul-og-briketter-i-indkoebskurven"],
    },
    "grill/moerbradboeffer-grill.mdx": {
        "affiliateProduct": "meater-plus",
        "relatedGrej": ["tradlost-stegetermometer", "instant-read-vs-bluetooth-termometer"],
    },
    "stobejern/forloren-hare-stobejern.mdx": {
        "affiliateProduct": "lodge-dutch-oven",
        "relatedGrej": ["stoebjernsgryde-storrelsesguide", "stoebjern-rene-skole"],
    },
    "stobejern/skipperlabskovs-stobejern.mdx": {
        "affiliateProduct": "lodge-dutch-oven",
        "relatedGrej": ["stoebjernsgryde-storrelsesguide"],
    },
    "pande/blodpoelse-pande.mdx": {
        "affiliateProduct": "boligcenter-stegepande",
        "relatedGrej": ["belaegning-teflon-keramik-staal"],
    },
    "ovn/stegt-flaesk-ovn.mdx": {
        "relatedGrej": ["bagestaal-vs-bagesten", "koedsnore-og-koednaale"],
    },
    "ovn/klassisk-aeblekage.mdx": {
        "relatedGrej": ["koekkenvaegt-vs-maalebaeger", "bagestaal-vs-bagesten"],
    },
    "ovn/karamelrand.mdx": {
        "relatedGrej": ["koekkenvaegt-vs-maalebaeger"],
    },
    "ovn/hjemmelavet-leverpostej.mdx": {
        "relatedGrej": ["koedhakkere", "palaegsmaskine-pro-vs-billig"],
    },
    "ovn/tarteletter-ovn.mdx": {
        "relatedGrej": ["tarteletjern-vs-koebte-skaller"],
    },
    "ovn/aeggekage-ovn.mdx": {
        "relatedGrej": ["bagestaal-vs-bagesten"],
    },
    # Basis-opskrifter (guide + emne)
    "pande/stjerneskud.mdx": {
        "affiliateProduct": "boligcenter-stegepande",
        "relatedGrej": ["belaegning-teflon-keramik-staal", "tangsaet-pincet-grilltang"],
    },
    "pande/krebinetter.mdx": {
        "affiliateProduct": "boligcenter-stegepande",
        "relatedGrej": ["belaegning-teflon-keramik-staal"],
    },
    "pande/tykke-moerbradboeffer-bloede-loeg.mdx": {
        "affiliateProduct": "boligcenter-stegepande",
        "relatedGrej": ["instant-read-vs-bluetooth-termometer"],
    },
    "gryde/hjerter-i-floedesovs.mdx": {
        "relatedGrej": ["kobbergryder", "koekkensakse-fjerkrae-saks"],
    },
    "gryde/forloren-hare-gryde.mdx": {
        "relatedGrej": ["kobbergryder"],
    },
    "gryde/skipperlabskovs.mdx": {
        "relatedGrej": ["kobbergryder", "stoebjernsgryde-storrelsesguide"],
    },
    "palaeg/leverpostej.mdx": {
        "relatedGrej": ["palaegsmaskine-pro-vs-billig", "elektrisk-palaegskniv"],
    },
    "dips/persillesovs.mdx": {
        "affiliateProduct": "boligcenter-saucegryde",
        "relatedGrej": ["kobbergryder"],
    },
}

GUIDE_GREJ = [
    "trykkoger-vs-slowcooker",
    "stoebjernsgryde-storrelsesguide",
    "tradlost-stegetermometer",
    "airfryer-vs-ovn-opgoer",
    "kobbergryder",
    "tarteletjern-vs-koebte-skaller",
    "koedhakkere",
    "belaegning-teflon-keramik-staal",
]


def parse_list_block(content: str, key: str) -> tuple[re.Match[str] | None, list[str]]:
    m = re.search(rf"^{key}:\s*\n((?:  - .+\n)+)", content, re.MULTILINE)
    if not m:
        return None, []
    items = []
    for line in m.group(1).strip().split("\n"):
        items.append(line[4:].strip().strip('"').strip("'"))
    return m, items


def merge_list(content: str, key: str, new_items: list[str]) -> tuple[str, bool]:
    m, existing = parse_list_block(content, key)
    merged = existing[:]
    changed = False
    for item in new_items:
        if item not in merged:
            merged.append(item)
            changed = True
    if not changed:
        return content, False
    if m:
        block = f"{key}:\n" + "\n".join(f"  - {x}" for x in merged) + "\n"
        return content[: m.start()] + block + content[m.end() :], True
    # insert after publishedAt or featured
    insert_after = re.search(r"^(publishedAt: .+\n|featured: .+\n)", content, re.MULTILINE)
    if not insert_after:
        insert_after = re.search(r"^tags:\s*\n(?:  - .+\n)+", content, re.MULTILINE)
    block = f"{key}:\n" + "\n".join(f"  - {x}" for x in merged) + "\n"
    if insert_after:
        pos = insert_after.end()
        return content[:pos] + block + content[pos:], True
    return content, False


def patch_recipe(rel: str, data: dict[str, str | list[str]]) -> bool:
    path = ROOT / rel
    if not path.exists():
        print("skip missing", rel)
        return False
    content = path.read_text(encoding="utf-8")
    changed = False

    product = data.get("affiliateProduct")
    if product and "affiliateProduct:" not in content:
        m = re.search(r"^(publishedAt: .+\n|featured: .+\n)", content, re.MULTILINE)
        line = f"affiliateProduct: {product}\n"
        if m:
            content = content[: m.end()] + line + content[m.end() :]
        else:
            content = content.replace("---\n", f"---\n{line}", 1)
        changed = True

    grej = data.get("relatedGrej", [])
    if grej:
        content, c = merge_list(content, "relatedGrej", grej)
        changed = changed or c

    if changed:
        path.write_text(content, encoding="utf-8")
        print("updated", rel)
    else:
        print("ok", rel)
    return changed


def patch_guide() -> bool:
    content = GUIDE.read_text(encoding="utf-8")
    if "relatedGrej:" in content:
        content, changed = merge_list(content, "relatedGrej", GUIDE_GREJ)
    else:
        m = re.search(r"^relatedGuides:\s*\n(?:  - .+\n)+", content, re.MULTILINE)
        block = "relatedGrej:\n" + "\n".join(f"  - {x}" for x in GUIDE_GREJ) + "\n"
        if m:
            content = content[: m.end()] + block + content[m.end() :]
            changed = True
        else:
            changed = False
    if changed:
        GUIDE.write_text(content, encoding="utf-8")
        print("updated guide relatedGrej")
    return changed


def main() -> None:
    n = sum(1 for rel, data in PATCHES.items() if patch_recipe(rel, data))
    patch_guide()
    print(f"done: {n} recipes patched")


if __name__ == "__main__":
    main()
