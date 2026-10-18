#!/usr/bin/env python3
"""Build draft.pdf from chapters/*.md: pandoc -> HTML -> WeasyPrint.

Requires pandoc and weasyprint on PATH (e.g. `pipx install weasyprint`).
"""
import pathlib
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent
chapters = sorted((ROOT / "chapters").glob("*.md"))

with tempfile.TemporaryDirectory() as tmp:
    html = pathlib.Path(tmp) / "book.html"
    subprocess.run(
        ["pandoc", *map(str, chapters), "-f", "markdown", "-t", "html5", "-s",
         "--metadata", "pagetitle=Felhasználókutatás", "--metadata", "lang=hu",
         "--css", "style.css", "-o", str(html)],
        cwd=ROOT, check=True,
    )
    subprocess.run(
        ["weasyprint", "--base-url", str(ROOT), str(html), str(ROOT / "draft.pdf")],
        cwd=ROOT, check=True,
    )
print("wrote", ROOT / "draft.pdf")
