from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).parent
TEMPLATE = ROOT / "template.html"
CONTENT = ROOT / "content"
DIST = ROOT / "dist"

def render_markdown(path: Path) -> str:
    result = subprocess.run(
        ["pandoc", "--from=gfm", "--to=html5", "--wrap=none"],
        input=path.read_text(encoding="utf-8"),
        text=True, capture_output=True, check=True,
    ).stdout
    # The page masthead shows the document title; omit the duplicated first heading.
    result = re.sub(r"^<h1\b[^>]*>.*?</h1>\s*", "", result, count=1, flags=re.S)
    return result.strip()

page = TEMPLATE.read_text(encoding="utf-8")
page = page.replace("__EN_CONTENT__", render_markdown(CONTENT / "en.md"))
page = page.replace("__RO_CONTENT__", render_markdown(CONTENT / "ro.md"))
DIST.mkdir(exist_ok=True)
(DIST / "index.html").write_text(page, encoding="utf-8")
print(f"Built {DIST / 'index.html'}")
