#!/usr/bin/env python3
"""Inject img/*.jpg as base64 data URIs into kalpa_tpl3.html -> kalpa.html"""
import base64, pathlib

root = pathlib.Path(__file__).parent
MAP = {
    "__JAR__": "jar_blank_ng.jpg",
    "__HERO__": "hero_ng.jpg",
    "__SEEDS__": "seeds_ng.jpg",
    "__ORCHARD__": "orchard_ng.jpg",
    "__RUNNER__": "runner_ng.jpg",
    "__LAB__": "lab_ng.jpg",
    "__JARMACRO__": "jarm_blank_ng.jpg",
    "__POUCH__": "pouch_blank_ng.jpg",
    "__CARTON__": "carton_blank.jpg",
    "__TRIO__": "trio_blank_ng.jpg",
}
html = (root / "kalpa_tpl3.html").read_text(encoding="utf-8")
for token, fname in MAP.items():
    data = base64.b64encode((root / "img" / fname).read_bytes()).decode()
    html = html.replace(token, f"data:image/jpeg;base64,{data}")
out = root / "kalpa.html"
out.write_text(html, encoding="utf-8")
print(f"built {out} ({out.stat().st_size/1e6:.2f} MB)")
