# Shrimad Rajchandraji — Lifetime Places

An interactive map of every place Param Krupalu Dev is documented to have visited, stayed in or
lived in during His lifetime (1867–1901).

## What's here

    index.html            The map. Self-contained — double-click it, or push it to GitHub Pages.
    review.html           Generated. The reviewer's sheet — print it, or send the file.
    not-found.md          Generated. Everything still unplaced, and what has been tried.
    not-found.html        Generated. The same list, laid out to print.
    build.py              Rebuilds everything below from the two CSVs.
    data/places.csv       The research source. Edit this.
    data/sites.csv        Individual sites within each place, with survival status. Edit this.
    data/register.json    The disputed and candidate entries. Edit this.
    data/images.csv       Pictures keyed to a place or site, with their credits. Edit this.
    images/               The picture files.
    data/places.json      Generated. The same data as one document.
    data/places.geojson   Generated. Standard GeoJSON, if you want to load it into anything else.

`index.html` carries its own copy of the data so that it works as a single file, with no server
and no fetch. That copy is generated too.

## Editing

Edit a CSV, then run:

    python build.py

That rewrites `data/places.json`, `data/places.geojson`, `review.html`, `not-found.md`,
`not-found.html` and the `const DATA = {...};` block inside `index.html`, and refuses to write anything if a row is malformed — an unknown life phase or
survival status, a latitude without a longitude, a place with no sites, a site pointing at a place
that does not exist. `python build.py --check` reports whether the generated files are current
without touching them, which is worth running before a commit.

It also refuses a site pinned more than 25 km from its own town, which is what a transposed or
mistyped coordinate looks like. That guard exists because site pins now arrive in batches from
research passes rather than one at a time.

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
says so in as many words rather than letting the reader assume the dot is the doorway. 14 of the
89 sites are pinned; the rest still show their town.

Each pin carries its own confidence — `Building`, `Street-level`, `Locality` — and the panel prints
it beside the coordinate, because "we know the lane" and "we know the door" are different promises
to a pilgrim.

Where the body that runs a site publishes a postal address, that address is recorded against it
and shown in the panel. An address is not a coordinate, but it is what a pilgrim actually
navigates by, and unlike a pin inferred from a neighbouring building it is sourced. Six sites
carry one so far.

## Pictures

8 places and sites carry a photograph. Every one is freely licensed — all of them from Wikimedia
Commons — and `build.py` refuses to build if any lacks a credit or a licence, because a photograph
is publishable only on its licence's terms. Nothing is taken from the trusts' own websites.

Captions say what the picture actually shows. A general view of Idar's hills is captioned as the
range and not as Ghantiya Pahad; the Dharampur photograph is captioned as the modern complex and
not the lifetime retreat. The same standard that governs a pin governs a picture.

To add one: put the file in `images/`, add a row to `data/images.csv` naming the place or site it
belongs to along with its credit, licence and source, and rebuild.

## The extent of the map

He never left Gujarat and Bombay, so neither does the map. It opens framed on the places
themselves, will not zoom out past the region and will not pan away from it. Left unfenced, a
reader can drift into the Arabian Sea or zoom out until thirty-four dots are one speck over western
India, and nothing on the screen tells them they have gone wrong.

The fence is computed from the data, not written down, so adding a place widens it by itself. It is
also re-measured once the webfonts have loaded and on every resize: the header is set in a webfont
and is a different height before and after it arrives, and a map framed against the earlier height
put Mumbai — the southernmost place He reached — just below the bottom edge.

## Using the map

**All places** opens a searchable index of every place, grouped by life phase, showing each one's
district, how many sites it holds and whether it is located at all. Thirty-five dots on a map is
not a way to find a named village.

Each entry has its own link — `index.html#uttarsanda`, `#vavania`, `#hadmatiya` — so a particular
place can be sent to someone or cited from the reviewer's sheet, and the back button walks through
the entries you have opened. Markers are reachable by Tab and open with Enter or Space; Escape, a
click on the map, or the × closes the panel.

Long provenance folds away behind a disclosure rather than being cut. The claim and the first
sentence of its reasoning stay in the open; *how we know* opens the rest. Research passes make
these notes grow, and an entry that is thorough should not become an entry nobody reads.

The two documented-but-unlocated places, Hadmatiya and Rajpur, have no marker to click, so they are
links in the footer. Their entries carry the longest research notes in the data and were previously
unreadable.

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
2. **Still outstanding.** Have someone who reads Gujarati and someone connected to one of the
   trusts read the entries.
   `review.html` is built for exactly this: every claim with its evidence and its source, a box
   to tick against each, and a line for the source of any correction. It prints cleanly, and it
   is a single file, so it can simply be emailed. The two readings are independent and can go to
   two people at once. This one cannot be done from the sources — it needs the readers.

## Research passes

Locations are found in passes and folded in through the CSVs, each pin keeping the source that
produced it. The standing brief handed to each pass, and the draft letters to the three trusts,
are kept in `working/` beside this repository rather than inside it — they are correspondence and
working notes, not part of the published map. The brief points each new pass at `not-found.md`,
which is generated here and is always current.

**Pass 2 — Gujarati search and the trusts' own prose, 16 September 2026.** Two advances and one
correction. SRMD states that its Rachnabhoomi memorial stands *on* the site where the Atmasiddhi
Shastra was composed, and the Trust states that its Idar ashram sits *on* the rock He sat on — a
source saying a memorial occupies the spot is the one case where a memorial's location is the
spot's, so both are pinned as buildings. The correction was to pass 1: the Uttarsanda pin cannot be
told apart from a lake memorial 500 m away, so its confidence dropped from building to locality.
Most usefully, it closed a door — the Khambhat, Kavitha, Bharuch and Vaso sites are described by the
trusts in prose with no street, pol or landmark at all, so they will not be found in anything
published.

**Pass 1 — Google Maps and Places, 14 September 2026.** The avenue the brief predicted would pay,
and it did: Google's user-contributed places carry Indian temples, ashrams and even individual
houses that OpenStreetMap does not have at all. It pinned thirteen sites, several with reviews
independently corroborating the association, and located Rajpur. It also correctly declined the
Dharampur trap — the modern ashram campus is not the 1890s forest tract — and flagged three
contradictions rather than smoothing them over. Still untried: Gujarati-language search,
yatra blogs and video, Wikimapia, Bhuvan, census records, and OCR of the full biographies —
jainqq.org has no fetchable full-text search and serves page images, so that one is a
download-and-search job rather than a browsing one.

## Still open

- Which of the Gujarat villages named Hadmatiya is the one in the VS 1951 route. OpenStreetMap
  holds only three of the name, and the census count is far higher; the coordinates of all three
  are recorded in the entry's caution note as a starting point, not as an answer. Pass 1 found no
  source naming the district.
- Which of Nadiad's two Kumbhnath temples bore the name in 1896. The composition site itself is
  settled — SRMD places it where its Rachnabhoomi stands — so a pilgrim can be sent to the right
  ground; only the building is still unidentified.
- Ambalalbhai's house at Khambhat and the Dhaneshwari Bungalow at Uttarsanda — the only two
  buildings the Trust calls original, and neither is located. Khambhat has a candidate in a listing
  named Raj Chhaya, in the right quarter of the old city but not named for Ambalalbhai in any
  source found. At Uttarsanda the Trust names the bungalow and publishes no address, and the pin
  found there belongs to one of two other nearby sites.
- A precise pin for the Sir Framji Cawasji Institute, Mumbai — site of the Shatavadhan. Narrowed
  from the Zaveri Bazaar anchor about 1 km away to a street-level pin on Anandilal Podar Marg,
  Dhobi Talao, where the building survives as Framji Cowasji Hall. The entrance itself is still
  unverified.
- Whether the Aga Khan bungalow in Ahmedabad still stands, and where it is. The Trust's own
  register attests the VS 1957 stay and publishes no address; nothing independent was found.
- Site-level coordinates generally: 73 of the 89 sites still inherit their town's pin.
  OpenStreetMap is a dead end for these — it holds two Rajchandra-named features in all of
  Gujarat, both hospitals — but Google Places is not, and further passes should keep going there
  and into Gujarati-language sources. Where a body publishes an address it is recorded, and where
  only a neighbouring campus building can be found — the Dharampur hospital, the Sayla eye
  hospital — that is noted as a navigation aid rather than promoted to a pin.
  `python build.py --unlocated` reprints what is still missing, grouped by which body would know.
- The named Kavitha landmarks — three banyans, a well, a field — are oral and local rather than
  indexed anywhere, and will not be found by searching maps in English. They need a yatra account
  or someone who has walked the village.

## Making a PDF of what is missing

`not-found.html` is styled to print. Any browser's print-to-PDF will do it, or from the command
line:

    chrome --headless=new --no-pdf-header-footer --print-to-pdf=still-not-found.pdf not-found.html

Gujarati needs a browser that has the font, which any current one does. The PDF is not kept in the
repository, because it is generated from files that are.

Full reasoning, sources and the disputed register are in the Research Edition 2 PDF.
