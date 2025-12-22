from pathlib import Path
import re

# Directory THIS SCRIPT lives in
SCRIPT_DIR = Path(__file__).resolve().parent

# Portfolio directory (adjust if needed)
PORTFOLIO_DIR = SCRIPT_DIR / "entries"

# Output file: SAME directory as this script
OUTPUT_FILE = SCRIPT_DIR / "portfolio_order.yml"

pattern = re.compile(r"^\s*include_on_website\s*:\s*true\s*$", re.MULTILINE)

results = []

for md_file in sorted(PORTFOLIO_DIR.glob("*.md")):
    text = md_file.read_text(encoding="utf-8", errors="ignore")
    if pattern.search(text):
        results.append(md_file.stem)

# Write directly to portfolio_order.yml
with OUTPUT_FILE.open("w", encoding="utf-8") as f:
    for name in results:
        f.write(f"- {name}\n")

print(f"Wrote {len(results)} entries to {OUTPUT_FILE.resolve()}")
