from pathlib import Path
import re

# writes to _data/porfolio_order.yml
# go into that file to modify the order afterward

# Directory THIS SCRIPT lives in (_portfolio/)
SCRIPT_DIR = Path(__file__).resolve().parent

# Project root (parent of _portfolio)
PROJECT_ROOT = SCRIPT_DIR.parent

# Portfolio entries directory
PORTFOLIO_DIR = SCRIPT_DIR / "entries"

# Output file: _data/portfolio_order.yml
OUTPUT_FILE = PROJECT_ROOT / "_data" / "portfolio_order.yml"

pattern = re.compile(r"^\s*include_on_website\s*:\s*true\s*$", re.MULTILINE)

results = []

for md_file in sorted(PORTFOLIO_DIR.glob("*.md")):
    text = md_file.read_text(encoding="utf-8", errors="ignore")
    if pattern.search(text):
        results.append(md_file.stem)

# Ensure _data exists
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

# Write the YAML
with OUTPUT_FILE.open("w", encoding="utf-8") as f:
    for name in results:
        f.write(f"- {name}\n")

print(f"Wrote {len(results)} entries to {OUTPUT_FILE.resolve()}")
