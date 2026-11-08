#!/usr/bin/env python3
"""Build the run.co clickable prototype from the design source.

Reads design/*.dc.html (one file per screen, exported from the design canvas)
and design/canvas.json (screen order and flow sections), and writes:
  index.html        every screen as a <section>, linked with hash routes
  styles/runco.css  the design system, with asset URLs made local

Run:  python3 tools/build.py
"""
import json, re, pathlib, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
DESIGN = ROOT / "design"

BLOBS = {
    "/_blob/dd73ac5ec881c3ac37f1c72d80232d5c": "assets/blr-map.svg",
    "/_blob/f0cf5ae2192bfe31eea4c6db6c8264db": "assets/turf-hex.svg",
}
FONT_IMPORT = '@import url("https://api.fontshare.com/v2/css?f[]=satoshi@500,700,900&display=swap");\n'


def build_css():
    css = (DESIGN / "runco.css").read_text()
    css = re.sub(r"@font-face\{[^}]*\}\n?", "", css)
    for blob, path in BLOBS.items():
        css = css.replace(blob, "../" + path)
    out = ROOT / "styles" / "runco.css"
    out.parent.mkdir(exist_ok=True)
    out.write_text(FONT_IMPORT + css)


def screen_markup(name):
    src = (DESIGN / f"{name}.dc.html").read_text()
    body = src.split("</helmet>", 1)[1].split("</x-dc>", 1)[0].strip()
    title = re.search(r"<title>(.*?)</title>", src).group(1)
    body = re.sub(r'href="([A-Za-z0-9_]+)\.dc\.html"', r'href="#\1"', body)
    for blob, path in BLOBS.items():
        body = body.replace(blob, path)
    return title, body


def main():
    canvas = json.loads((DESIGN / "canvas.json").read_text())
    order = [f[:-len(".dc.html")] for f in canvas["order"]]
    boards = canvas["boards"]
    notes = sorted(canvas["notes"].values(), key=lambda n: n["y"])

    sections, nav = [], []
    for note in notes:
        row = [n for n in order if 0 <= boards[n + ".dc.html"]["y"] - note["y"] < 600]
        nav.append(f'<h3>{html.escape(note["text"])}</h3><ol>')
        for n in row:
            label = boards[n + ".dc.html"].get("title", n)
            nav.append(f'<li><a href="#{n}">{html.escape(label)}</a></li>')
        nav.append("</ol>")
    for n in order:
        title, body = screen_markup(n)
        sections.append(f'<section class="screen" id="{n}" aria-label="{html.escape(title)}" hidden>\n{body}\n</section>')

    page = TEMPLATE.replace("{{NAV}}", "\n".join(nav)).replace("{{SCREENS}}", "\n".join(sections))
    (ROOT / "index.html").write_text(page)
    build_css()
    print(f"built {len(order)} screens")


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0E0E10">
<title>run.co · prototype</title>
<link rel="stylesheet" href="styles/runco.css">
<link rel="stylesheet" href="styles/shell.css">
</head>
<body>
<aside class="flow" aria-label="All screens">
<div class="flow-head"><span class="wordmark">run<i>.</i>co</span><span>Clickable prototype · Bengaluru</span></div>
{{NAV}}
</aside>
<main class="device">
{{SCREENS}}
</main>
<script src="app.js"></script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
