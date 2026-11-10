"""Render a Tech Tales carousel from a post JSON file to 1080x1350 PNGs.

Usage (from repo root): python3 engine/render.py posts/YYYY/MM/YYYY-MM-DD-slug/post.json
Writes slides/slide-01.png ... next to the JSON. Settings live in engine/config.json.
"""
import json, sys, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).parent.resolve()
CFG = json.loads((ROOT / "config.json").read_text())


def slide_html(slide, i, n, post):
    frac = (i + 1) / n
    trace = f'<div class="trace"><i style="height:{frac*100:.1f}%"></i><b style="top:calc({frac*100:.1f}% - 6px)"></b></div>'
    return f'''<section class="slide {slide.get("theme","light")}">{trace}
<div class="inner">
  <div class="meta"><span class="tag">{slide.get("tag", post["pillar"])}</span><span>{i+1:02d} / {n:02d}</span></div>
  <div class="body" style="margin-top:{slide.get("offset", 120)}px">{slide["html"]}</div>
  <div class="foot"><span>{CFG["handle"]}</span><span>{slide.get("footnote", "")}</span></div>
</div></section>'''


def main(path):
    post_path = pathlib.Path(path).resolve()
    post = json.loads(post_path.read_text())
    slides = post["slides"]
    n = len(slides)
    css = (ROOT / "brand.css").read_text()
    out = post_path.parent / "slides"
    out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CFG["chrome_path"])
        pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for i, s in enumerate(slides):
            doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{slide_html(s, i, n, post)}</body></html>'
            tmp = ROOT / "_render.html"
            tmp.write_text(doc)
            pg.goto(tmp.as_uri())
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(150)
            pg.locator(".slide").screenshot(path=str(out / f"slide-{i+1:02d}.png"))
        b.close()
    print(f"rendered {n} slides to {out}")


if __name__ == "__main__":
    main(sys.argv[1])
