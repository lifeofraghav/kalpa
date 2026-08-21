#!/usr/bin/env python3
"""Inject img/*.jpg as base64 data URIs into kalpa_tpl3.html -> kalpa.html"""
import base64, pathlib

root = pathlib.Path(__file__).parent
MAP = {
    "__JAR__": "jar.jpg",
    "__HERO__": "hero.jpg",
    "__SEEDS__": "seeds.jpg",
    "__ORCHARD__": "orchard.jpg",
    "__RUNNER__": "runner.jpg",
    "__LAB__": "lab.jpg",
    "__JARMACRO__": "jarm_card.jpg",
    "__POUCH__": "pouch_card.jpg",
    "__CARTON__": "carton_card.jpg",
    "__TRIO__": "trio_card.jpg",
}
html = (root / "kalpa_tpl3.html").read_text(encoding="utf-8")
for token, fname in MAP.items():
    data = base64.b64encode((root / "img" / fname).read_bytes()).decode()
    html = html.replace(token, f"data:image/jpeg;base64,{data}")
out = root / "kalpa.html"
out.write_text(html, encoding="utf-8")
print(f"built {out} ({out.stat().st_size/1e6:.2f} MB)")
