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
    review.html         the reviewer's sheet, for the Gujarati and trust readings

Run:  python build.py         rebuild
      python build.py --check verify the generated files are up to date
"""

import csv, json, re, sys, pathlib

ROOT   = pathlib.Path(__file__).parent
DATA   = ROOT / "data"
INDEX  = ROOT / "index.html"
REVIEW = ROOT / "review.html"

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
        # a published postal address, where the body that runs the site gives one
        address = (row.get("address") or "").strip()
        if address:
            site["addr"] = address
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


STATUS_LABEL = {"ORIG": "Original survives", "MEM": "Later memorial",
                "GONE": "Altered", "UNID": "Not located"}

REVIEW_CSS = """
:root{--ink:#1a1a1a;--muted:#666;--line:#ccc;--rule:#e6e2d8}
*{box-sizing:border-box}
body{margin:0 auto;padding:28px 26px 60px;max-width:52em;color:var(--ink);background:#fff;
     font:15px/1.5 "Source Serif 4",Georgia,serif}
h1{font-size:22px;margin:0 0 4px}
h2{font-size:13px;letter-spacing:.6px;text-transform:uppercase;color:var(--muted);
   margin:26px 0 8px;font-weight:600}
.lede{color:var(--muted);font-size:13.5px;line-height:1.6;margin:0 0 18px}
.how{border:1px solid var(--line);border-radius:6px;padding:14px 16px;margin:0 0 26px;
     font-size:13.5px;line-height:1.6;background:#faf9f6}
.how p{margin:0 0 8px}
.how p:last-child{margin:0}
.place{border-top:2px solid var(--ink);padding-top:12px;margin-top:30px;break-inside:avoid}
.pname{font-size:18px;font-weight:600;margin:0}
.pgu{font-family:"Noto Serif Gujarati",serif;font-size:15px;color:var(--muted);margin:1px 0 6px}
.meta{font:12px/1.55 system-ui,sans-serif;color:var(--muted);margin:0 0 9px}
.ev{font-size:14px;line-height:1.55;margin:0 0 9px}
.warn{border-left:3px solid #8c2f22;background:#fbf3ef;padding:8px 11px;font-size:12.5px;
      line-height:1.5;margin:0 0 9px}
.q{font:12.5px/1.9 system-ui,sans-serif;margin:9px 0 4px}
.q span{display:inline-block;min-width:20.5em}
.box{display:inline-block;width:13px;height:13px;border:1px solid #888;vertical-align:-2px;
     margin:0 4px 0 9px}
.fill{display:inline-block;border-bottom:1px solid var(--line);min-width:15em;margin-left:8px}
table{width:100%;border-collapse:collapse;margin:8px 0 0;font-size:12.5px}
th{text-align:left;font:600 10px/1.4 system-ui,sans-serif;letter-spacing:.5px;
   text-transform:uppercase;color:var(--muted);border-bottom:1px solid var(--ink);padding:0 6px 4px 0}
td{border-bottom:1px solid var(--rule);padding:7px 6px 7px 0;vertical-align:top;line-height:1.45}
td.st{white-space:nowrap;font:600 9.5px/1.4 system-ui,sans-serif;letter-spacing:.4px;
      text-transform:uppercase;color:var(--muted)}
td.mark,th.mark{width:6.5em;white-space:nowrap;text-align:right;padding-right:0}
td.mark .box{margin:0 0 0 8px}
.note{color:var(--muted);font-size:11.5px;display:block;margin-top:2px}
.addr{font:600 11px/1.4 system-ui,sans-serif;display:block;margin-top:2px}
.open{background:#fffbe9;border:1px dashed #c9a227;border-radius:5px;padding:9px 11px;
      font-size:12.5px;line-height:1.5;margin:9px 0 0}
.src{font-size:11px;color:var(--muted);font-style:italic;margin:8px 0 0}
footer{margin-top:40px;border-top:1px solid var(--line);padding-top:12px;
       font:11.5px/1.6 system-ui,sans-serif;color:var(--muted)}
@media print{
  body{padding:0;font-size:11.5pt;max-width:none}
  .place{break-inside:avoid;page-break-inside:avoid}
  .how{break-after:page}
  a{text-decoration:none;color:inherit}
}
"""


def render_review(data):
    """A sheet the Gujarati reader and the trust reader can work through on paper.

    Every claim the map makes appears here with its evidence and its source, and
    nothing else — the point is to make each one easy to affirm or overturn, not
    to persuade anyone of it.
    """
    from html import escape as e

    phases = {p[0]: p[1] for p in data["phases"]}
    out = []
    add = out.append

    add("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">")
    add("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
    add("<title>Lifetime Places — reviewer's sheet</title>")
    add("<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css2?"
        "family=Noto+Serif+Gujarati:wght@400;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap\">")
    add("<style>" + REVIEW_CSS + "</style>\n</head>\n<body>")

    pinned = [p for p in data["places"] if p["lat"] is not None]
    sites = [s for p in data["places"] for s in p["sites"]]
    add("<h1>Shrimad Rajchandraji — Lifetime Places</h1>")
    add('<p class="lede">Reviewer\'s sheet &middot; {} places, {} sites &middot; '
        '{} places pinned, {} documented but not located</p>'.format(
            len(data["places"]), len(sites), len(pinned), len(data["places"]) - len(pinned)))

    add('<div class="how">')
    add("<p><strong>What this is.</strong> Every claim the map makes, with the evidence and the "
        "source behind it. It is compiled independently by a devotee and is not an official "
        "publication of SRMD, the Shrimad Rajchandra Trust, Raj Saubhag Satsang Mandal or any "
        "other body.</p>")
    add("<p><strong>What is being asked.</strong> Two readings, and they can be done by two "
        "different people. The first is the Gujarati reading: are the names, the spellings and "
        "the Vikram Samvat dates right? The second is the reading by someone connected to one of "
        "the trusts: is the visit real, is the site the right one, and does the building still "
        "stand as described?</p>")
    add("<p><strong>How to mark it.</strong> Tick a box only where you are confident. Where a "
        "claim is wrong, strike it and write what is right, and — this matters more than the "
        "correction itself — name the source, a book and page or a Trust page. An entry with no "
        "source cannot be used, however certain it feels.</p>")
    add("<p><strong>Leaving something unmarked is useful.</strong> It tells the compiler the "
        "claim has not been checked, which is different from it being right.</p>")
    add("</div>")

    for p in data["places"]:
        add('<div class="place">')
        add('<p class="pname">{}. {}</p>'.format(p["id"], e(p["en"])))
        if p["gu"]:
            add('<p class="pgu">{}</p>'.format(e(p["gu"])))
        loc = "{}, {}".format(e(p["district"]), e(p["state"]))
        if p["alt"]:
            loc += " &middot; also " + e(p["alt"])
        pin = ("{:.5f}, {:.5f} (pin confidence: {})".format(p["lat"], p["lng"], e(p["pin"]))
               if p["lat"] is not None else "<strong>not located</strong>")
        add('<p class="meta">{}<br>{}<br>{} &middot; {}</p>'.format(
            loc, pin, e(p["period"]), e(phases[p["phase"]])))
        if p["work"]:
            add('<p class="ev"><strong>{}</strong></p>'.format(e(p["work"])))
        add('<p class="ev">{}</p>'.format(e(p["evidence"])))
        if p["warn"]:
            add('<div class="warn"><strong>Caution as published.</strong> {}</div>'.format(e(p["warn"])))

        for label in ("Gujarati name and spelling correct?",
                      "Visit documented, and in this period?",
                      "Town pin in the right place?" if p["lat"] is not None
                      else "Can you identify which village this is?"):
            add('<p class="q"><span>{}</span>yes<i class="box"></i>no<i class="box"></i>'
                '<i class="fill"></i></p>'.format(label))

        add("<table><tr><th>Status as published</th><th>Site</th>"
            "<th class=\"mark\">Right? yes&nbsp;/&nbsp;no</th></tr>")
        for s in p["sites"]:
            note = '<span class="note">{}</span>'.format(e(s["note"])) if s["note"] else ""
            addr = '<span class="addr">{}</span>'.format(e(s["addr"])) if s.get("addr") else ""
            pinned_at = ('<span class="note">pinned at {:.5f}, {:.5f}</span>'.format(s["lat"], s["lng"])
                         if "lat" in s else "")
            add("<tr><td class=\"st\">{}</td><td>{}{}{}{}</td>"
                "<td class=\"mark\"><i class=\"box\"></i><i class=\"box\"></i></td></tr>".format(
                    e(STATUS_LABEL[s["status"]]), e(s["name"]), addr, note, pinned_at))
        add("</table>")

        unpinned = sum(1 for s in p["sites"] if "lat" not in s)
        if unpinned:
            add('<div class="open">{} of these sites have no coordinates of their own and are '
                'shown at the town pin. If you know where any of them stands, that is the single '
                'most useful thing you can add.</div>'.format(unpinned))

        add('<p class="src">Sources as published: {}</p>'.format(e(p["src"])))
        add("</div>")

    add('<h2>Entries held back</h2>')
    add('<p class="lede">These are not on the map. Each needs a source before it could be, or a '
        'reason to drop it for good.</p>')
    for d in data["disputed"]:
        add('<div class="place"><p class="pname">{}</p><p class="ev">{}</p>'.format(
            e(d["name"]), e(d["detail"])))
        add('<p class="q"><span>Can you settle this either way?</span><i class="fill"></i></p></div>')
    c = data["candidate"]
    add('<div class="place"><p class="pname">{} (candidate)</p><p class="ev">{}</p>'.format(
        e(c["name"]), e(c["detail"])))
    add('<p class="q"><span>Is there a second source?</span><i class="fill"></i></p></div>')

    add("<footer>Reviewer: <i class=\"fill\"></i> &nbsp; Date: <i class=\"fill\"></i><br>"
        "Return marked copies to the compiler. Generated by build.py from data/places.csv and "
        "data/sites.csv — do not edit this file directly.</footer>")
    add("</body>\n</html>")
    return "\n".join(out) + "\n"


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
        REVIEW:                  render_review(data),
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
