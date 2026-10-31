# Koik Family Atlas

An animated map of where the ancestors in four family branches lived and moved, 1480 to today: **Koik** (with Leoke), **Rodilitz** (with Zaslow), **Goundrey** and **Romegialli**. Each branch has one main colour that fades as the tree reaches further back.

Open `index.html` in a browser. It is a single self-contained page; d3 and topojson-client load from public CDNs.

## Data

- Koik, Leoke and Rodilitz–Zaslow people and places are hand-entered in `build/manual.py` from the family research of October 2026.
- Goundrey and Romegialli come from the Ancestry tree export of 31 October 2026 (GEDCOM). The GEDCOM itself is **not** in this repository because it includes living people; put it at `build/tree.ged` to rebuild.
- Place coordinates are in `build/places.py` (farm sites in Estonia are approximate). Living people are not shown.

## Rebuild

```
cd geo && npm install && cd ..
cd build && python3 parse_ged.py && python3 build.py && cd ..
python3 build/make_page.py
```

`parse_ged.py` and `build.py` run from `build/` (they read `tree.ged` and write `data.json`); `make_page.py` runs from the repo root and writes `index.html`.

Search engines and AI crawlers are asked not to index the page (`robots.txt` and a robots meta tag).
