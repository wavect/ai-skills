"""Regenerate the raw-file discovery index and check packaged references."""
import argparse
import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.json"
RAW = "https://raw.githubusercontent.com/wavect/ai-skills/main/"
FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}


def build(index, site):
    seen = set()
    for entry in index["skills"]:
        name = entry["name"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64 or name in seen:
            raise ValueError(f"Invalid or duplicate skill name: {name}")
        seen.add(name)
        folder = ROOT / name
        path = folder / "SKILL.md"
        data = path.read_bytes()
        markdown = data.decode().splitlines(keepends=True)
        if not markdown or markdown[0].rstrip() != "---":
            raise ValueError(f"{path}: missing frontmatter")
        end = next((i for i, line in enumerate(markdown[1:], 1) if line.rstrip() == "---"), None)
        if end is None:
            raise ValueError(f"{path}: unclosed frontmatter")
        head, body = "".join(markdown[1:end]), "".join(markdown[end + 1:])
        meta = yaml.safe_load(head)
        if not isinstance(meta, dict) or meta.get("name") != name or set(meta) - FIELDS:
            raise ValueError(f"{path}: invalid frontmatter")
        desc = meta.get("description")
        if not isinstance(desc, str) or not desc.strip() or len(desc) > 1024:
            raise ValueError(f"{path}: invalid description")
        metadata = meta.get("metadata", {})
        if not isinstance(metadata, dict) or not all(isinstance(v, str) for v in metadata.values()):
            raise ValueError(f"{path}: metadata values must be strings")
        refs = {folder / link for link in re.findall(r"\]\((reference/[^)]+)\)", body)}
        if refs != set((folder / "reference").glob("*.md")):
            raise ValueError(f"{path}: missing or unlinked reference")
        if site:
            mirror = site / "themes/raditiy/static/.well-known/agent-skills" / name
            if {p.name for p in (mirror / "reference").glob("*.md")} != {p.name for p in refs}:
                raise ValueError(f"{name}: website reference membership differs")
            for file in [path, *refs]:
                if (mirror / file.relative_to(folder)).read_bytes() != file.read_bytes():
                    raise ValueError(f"Website copy differs: {file.relative_to(ROOT)}")
        entry.update(type="skill-md", description=desc, url=f"{RAW}{name}/SKILL.md",
                     digest="sha256:" + hashlib.sha256(data).hexdigest())
    if seen != {p.parent.name for p in ROOT.glob("*/SKILL.md")}:
        raise ValueError("Published skill directories and index membership differ")
    return json.dumps(index, indent=2, ensure_ascii=False) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if index.json is stale")
    parser.add_argument("--site-root", type=Path, help="also compare with this homepage checkout")
    args = parser.parse_args()
    current = INDEX.read_text()
    generated = build(json.loads(current), args.site_root)
    if args.check and generated != current:
        raise SystemExit("Stale index.json. Run python3 scripts/registry.py")
    if not args.check:
        INDEX.write_text(generated)
    print("Skill directories, metadata, references and registry checked.")
