#!/usr/bin/env python3
"""Rebuild every derived file from the research sources.

Sources of truth (edit these):
    data/places.csv     one row per place
    data/sites.csv      one row per site within a place
    data/register.json  the disputed and candidate entries

Generated (do not edit by hand):
    data/places.json    the same data as one document
    data/places.geojson standard GeoJSON, pinned places only
    index.html          the `const DATA = {...};` block is rewritten in place

Run:  python build.py         rebuild
      python build.py --check verify the generated files are up to date
"""

import csv, json, re, sys, pathlib

ROOT   = pathlib.Path(__file__).parent
DATA   = ROOT / "data"
INDEX  = ROOT / "index.html"

PHASES = [
    ["childhood", "Vavania & childhood",       "1867–1883", "#6b5b95", "Childhood"],
    ["avadhan",   "The avadhan years",         "1883–1887", "#2e6f9e", "Avadhan"],
    ["business",  "Mumbai & the travel years", "1888–1894", "#1f7a5a", "Travel years"],
    ["retreat",   "The years of retreat",      "1895–1899", "#b07d2b", "Retreat"],
    ["final",     "Final illness & Rajkot",    "1900–1901", "#8c2f22", "Final"],
]
PHASE_KEYS = {p[0] for p in PHASES}
STATUSES   = {"ORIG", "MEM", "GONE", "UNID"}

# places.csv column -> key in the generated JSON
PLACE_COLS = [
    ("place_id", "id", int), ("name_en", "en", str), ("name_gu", "gu", str),
    ("alt_spellings", "alt", str), ("district_taluka", "district", str),
    ("state", "state", str), ("lat", "lat", float), ("lng", "lng", float),
    ("pin_confidence", "pin", str), ("period_label", "period", str),
    ("ce_from", "from", int), ("ce_to", "to", int), ("life_phase", "phase", str),
    ("evidence", "evidence", str), ("caution", "warn", str),
    ("sources", "src", str), ("work", "work", str),
]


def read_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def build():
    errors = []

    sites_by_place = {}
    for row in read_csv(DATA / "sites.csv"):
        pid = int(row["place_id"])
        status = row["structure_status"].strip()
        if status not in STATUSES:
            errors.append(f"site {row['site_id']}: unknown status {status!r}")
        site = {
            "name":   row["site_name_en"].strip(),
            "status": status,
            "note":   row["evidence_note"].strip(),
        }
        # a site carries its own pin only where one has actually been sourced;
        # otherwise it inherits the town pin, and says so in the panel
        lat, lng = row.get("lat", "").strip(), row.get("lng", "").strip()
        if lat and lng:
            site["lat"], site["lng"] = float(lat), float(lng)
            site["pin"] = row.get("pin_confidence", "").strip()
        elif lat or lng:
            errors.append(f"site {row['site_id']}: only one of lat/lng given")
        sites_by_place.setdefault(pid, []).append(site)

    places = []
    for row in read_csv(DATA / "places.csv"):
        place = {}
        for col, key, cast in PLACE_COLS:
            raw = (row.get(col) or "").strip()
            if cast is str:
                place[key] = raw
            elif raw == "":
                place[key] = None
            else:
                place[key] = cast(raw)
        pid = place["id"]
        if place["phase"] not in PHASE_KEYS:
            errors.append(f"place {pid}: unknown life_phase {place['phase']!r}")
        if (place["lat"] is None) != (place["lng"] is None):
            errors.append(f"place {pid}: only one of lat/lng given")
        if place["lat"] is not None and not (-90 <= place["lat"] <= 90 and -180 <= place["lng"] <= 180):
            errors.append(f"place {pid}: coordinates out of range")
        if pid not in sites_by_place:
            errors.append(f"place {pid} ({place['en']}): no rows in sites.csv")
        place["sites"] = sites_by_place.pop(pid, [])
        places.append(place)

    for orphan in sites_by_place:
        errors.append(f"sites.csv references place_id {orphan}, which is not in places.csv")

    if errors:
        for e in errors:
            print("ERROR:", e, file=sys.stderr)
        sys.exit(1)

    register = json.loads((DATA / "register.json").read_text(encoding="utf-8"))
    data = {"phases": PHASES, "places": places,
            "disputed": register["disputed"], "candidate": register["candidate"]}

    geojson = {"type": "FeatureCollection", "features": [
        {"type": "Feature",
         "geometry": {"type": "Point", "coordinates": [p["lng"], p["lat"]]},
         "properties": {k: v for k, v in p.items() if k not in ("lat", "lng")}}
        for p in places if p["lat"] is not None
    ]}

    return data, geojson


def rendered(data, geojson):
    """The exact bytes each generated file should contain."""
    plain = {"phases": data["phases"], "places": data["places"]}
    html = INDEX.read_text(encoding="utf-8")
    blob = json.dumps(data, ensure_ascii=False, separators=(", ", ": "))
    html, n = re.subn(r"const DATA = \{.*?\};\n", "const DATA = " + blob.replace("\\", "\\\\") + ";\n",
                      html, count=1, flags=re.S)
    if n != 1:
        print("ERROR: could not find the `const DATA = {...};` block in index.html", file=sys.stderr)
        sys.exit(1)
    return {
        DATA / "places.json":    json.dumps(plain, ensure_ascii=False, indent=1) + "\n",
        DATA / "places.geojson": json.dumps(geojson, ensure_ascii=False, indent=1) + "\n",
        INDEX:                   html,
    }


if __name__ == "__main__":
    files = rendered(*build())
    check = "--check" in sys.argv
    stale = []
    for path, text in files.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == text:
            continue
        stale.append(path.name)
        if not check:
            path.write_text(text, encoding="utf-8", newline="")
    if check:
        print("stale:", ", ".join(stale) if stale else "nothing — all generated files are current")
        sys.exit(1 if stale else 0)
    print("rebuilt:", ", ".join(stale) if stale else "nothing changed")
