# Shrimad Rajchandraji — Lifetime Places

An interactive map of every place Param Krupalu Dev is documented to have visited, stayed in or
lived in during His lifetime (1867–1901).

## What's here

    index.html            The map. Self-contained — double-click it, or push it to GitHub Pages.
    review.html           Generated. The reviewer's sheet — print it, or send the file.
    outreach.md           Draft letters to the three trusts, asking where the sites are.
    build.py              Rebuilds everything below from the two CSVs.
    data/places.csv       The research source. Edit this.
    data/sites.csv        Individual sites within each place, with survival status. Edit this.
    data/register.json    The disputed and candidate entries. Edit this.
    data/places.json      Generated. The same data as one document.
    data/places.geojson   Generated. Standard GeoJSON, if you want to load it into anything else.

`index.html` carries its own copy of the data so that it works as a single file, with no server
and no fetch. That copy is generated too.

## Editing

Edit a CSV, then run:

    python build.py

That rewrites `data/places.json`, `data/places.geojson`, `review.html` and the `const DATA = {...};`
block inside `index.html`, and refuses to write anything if a row is malformed — an unknown life phase or
survival status, a latitude without a longitude, a place with no sites, a site pointing at a place
that does not exist. `python build.py --check` reports whether the generated files are current
without touching them, which is worth running before a commit.

Nothing outside the `const DATA` block is touched, so the page can be edited by hand freely.

## Inclusion standard

A place appears only where a published biographical, SRMD or Shrimad Rajchandra Trust source
explicitly places Him there during His lifetime. A modern centre bearing His name is never
treated as proof of a visit. Where the visit is documented but the exact building is not
identified, that is shown as an open question rather than filled in with a plausible address.

## Survival status

Each site carries one of four values, because a pilgrim needs to know what they will actually find:

- **Original survives** — the structure or natural feature from His lifetime still stands
- **Later memorial** — a building raised afterwards on the documented spot
- **Altered** — the place is located, the original structure has been converted or replaced
- **Not located** — the visit is documented, the exact site is not

Note that the Trust states originality explicitly for only two buildings in its whole register:
Ambalalbhai's house at Khambhat and the Dhaneshwari Bungalow at Uttarsanda. Everything else in
the "original" class is read from the site being a pre-existing building or a natural feature.

## Coordinates

A place carries a town-level pin and a stated confidence. A site carries its own pin only where
one has actually been sourced; where it has not, the site inherits the town pin, and the panel
says so in as many words rather than letting the reader assume the dot is the doorway. One site
is pinned at present — see "Still open" below.

Where the body that runs a site publishes a postal address, that address is recorded against it
and shown in the panel. An address is not a coordinate, but it is what a pilgrim actually
navigates by, and unlike a pin inferred from a neighbouring building it is sourced. Six sites
carry one so far.

## Corrections

Open `index.html` and set `CORRECTIONS` near the top of the page script:

    const CORRECTIONS = {email: "you@example.org", url: ""};

An email address opens the reader's mail client with the entry already quoted and a prompt for the
published source. A `url` instead points at a form, and takes precedence. Leave both blank and the
panel says corrections are welcome without offering a link that goes nowhere.

## Deploying

    git add -A && git commit -m "Update"
    # push to a GitHub repo, then Settings → Pages → deploy from main branch, root

The page loads Leaflet from a CDN and map tiles from OpenStreetMap. No API key, no billing.

It used CARTO's Voyager basemap until CARTO began burning an "API KEY REQUIRED" watermark into
tiles served to unregistered sites. If you would rather have Voyager's quieter palette back,
register for a CARTO key and restore the tile URL noted in the comment above `L.tileLayer`.
OpenStreetMap's own [tile usage policy](https://operations.osmfoundation.org/policies/tiles/)
covers the tiles this now uses; a map of this size sits comfortably inside it.

## Before sharing widely

1. ~~Replace the "Tell us" link with a real correction form or email address.~~ The mechanism is
   built; set `CORRECTIONS` as above to turn it on.
2. Have someone who reads Gujarati and someone connected to one of the trusts read the entries.
   `review.html` is built for exactly this: every claim with its evidence and its source, a box
   to tick against each, and a line for the source of any correction. It prints cleanly, and it
   is a single file, so it can simply be emailed. The two readings are independent and can go to
   two people at once. This one cannot be done from the sources — it needs the readers.

## Still open

- Which of the Gujarat villages named Hadmatiya is the one in the VS 1951 route. OpenStreetMap
  holds only three of the name, and the census count is far higher; the coordinates of all three
  are recorded in the entry's caution note as a starting point, not as an answer.
- Coordinates for Rajpur (Khambhat taluka) and Ghantiya Pahad (Barvav, near Idar). Both are now
  described tightly enough to be found on the ground — Rajpur about 9 km from Khambhat, pincode
  388640, 2,444.88 ha; Ghantiya Pahad about 2 km from Idar town at Barvav — but neither appears in
  OpenStreetMap or any gazetteer that publishes a coordinate, so neither is pinned.
- A precise pin for the Sir Framji Cawasji Institute, Mumbai — site of the Shatavadhan. Narrowed
  from the Zaveri Bazaar anchor about 1 km away to a street-level pin on Anandilal Podar Marg,
  Dhobi Talao, where the building survives as Framji Cowasji Hall. The entrance itself is still
  unverified.
- Whether the Aga Khan bungalow in Ahmedabad still stands, and where it is. The Trust's own
  register attests the VS 1957 stay and publishes no address; nothing independent was found.
- Site-level coordinates generally: 87 of the 88 sites still inherit their town's pin. Open
  geodata is a dead end here — OpenStreetMap holds two Rajchandra-named features in all of
  Gujarat, both hospitals, and none of the ashrams, temples or houses. The trusts hold these
  addresses; asking them is the route, and the last question on every page of `review.html` asks
  it, and `outreach.md` holds a draft letter to each of the three. Where a trust publishes an
  address it is now recorded, and where OpenStreetMap has a neighbouring campus building — the
  Dharampur hospital, the Sayla eye hospital — that is noted as a navigation aid rather than
  promoted to a pin. `python build.py --unlocated` reprints what is still missing, grouped by
  which body would know.

Full reasoning, sources and the disputed register are in the Research Edition 2 PDF.
