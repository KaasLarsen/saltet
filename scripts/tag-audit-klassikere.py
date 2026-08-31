#!/usr/bin/env python3
"""Tag-audit — berig eksisterende opskrifter med dansk-klassiker tags (aug 2026)."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent / "content/recipes"

UPDATES: dict[str, list[str]] = {
    "gryde/boller-i-karry.mdx": ["dansk-klassiker"],
    "airfryer/stegt-flaesk.mdx": ["dansk klassiker", "dansk-klassiker"],
    "pande/stegt-flaesk-pande.mdx": ["dansk-klassiker"],
    "pande/frikadeller-pande.mdx": ["dansk klassiker", "dansk-klassiker"],
    "airfryer/frikadeller.mdx": ["dansk-klassiker"],
    "pande/krebinetter.mdx": ["dansk-klassiker"],
    "gryde/millionboef.mdx": ["dansk klassiker", "dansk-klassiker"],
    "pande/millionboef-pande.mdx": ["dansk-klassiker"],
    "trykkoger/millionboef-trykkoger.mdx": ["dansk-klassiker"],
    "gryde/forloren-hare-gryde.mdx": ["dansk-klassiker"],
    "ovn/forloren-hare-bacon-floedesovs.mdx": ["dansk klassiker", "dansk-klassiker"],
    "trykkoger/forloren-hare-trykkoger.mdx": ["dansk-klassiker"],
    "pande/stjerneskud.mdx": ["dansk-klassiker"],
    "gryde/skipperlabskovs.mdx": ["dansk klassiker", "dansk-klassiker"],
    "trykkoger/skipperlabskovs-trykkoger.mdx": ["dansk-klassiker"],
    "gryde/klassisk-risengrod.mdx": ["dansk-klassiker"],
    "pande/aeggekage-bacon-purloeg.mdx": ["dansk klassiker", "dansk-klassiker"],
    "airfryer/aeggekage.mdx": ["dansk-klassiker"],
    "airfryer/tarteletter-hoens-asparges.mdx": ["dansk-klassiker"],
    "pande/tarteletfyld-kylling-asparges.mdx": ["dansk-klassiker"],
    "pande/tykke-moerbradboeffer-bloede-loeg.mdx": ["dansk klassiker", "dansk-klassiker"],
    "palaeg/leverpostej.mdx": ["dansk-klassiker"],
    "palaeg/julesylte.mdx": ["dansk-klassiker"],
    "gryde/hjerter-i-floedesovs.mdx": ["dansk-klassiker"],
    "pande/biksemad-spejlaeg.mdx": ["dansk klassiker", "dansk-klassiker"],
    "airfryer/biksemad-spejlaeg.mdx": ["dansk-klassiker"],
}


def quote_tag(tag: str) -> str:
    if re.search(r'[:#\[\]{}]', tag) or tag.startswith(("-", " ")):
        return f'"{tag}"'
    return tag


def parse_tags(content: str) -> tuple[re.Match[str] | None, list[str], str]:
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
