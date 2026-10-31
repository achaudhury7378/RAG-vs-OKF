"""Generate data/okf_bundle/index.md from each concept file's frontmatter."""
from pathlib import Path

from common import BUNDLE_DIR, parse_frontmatter

lines = ["---", "type: index", "title: EY Supply Chain Interview Notes", "---", "",
         "Knowledge bundle for supply chain interview prep. One concept per file.", ""]
for path in sorted(BUNDLE_DIR.glob("*.md")):
    if path.name == "index.md":
        continue
    meta, _ = parse_frontmatter(path.read_text())
    lines.append(f"- [{meta['title']}]({path.name}) ({meta['type']}): {meta['description']}")
(BUNDLE_DIR / "index.md").write_text("\n".join(lines) + "\n")
print(f"indexed {len(lines) - 6} concepts")
