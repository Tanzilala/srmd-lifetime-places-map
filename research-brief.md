# Research brief — locating the sites

Paste everything below the line into Cowork as one prompt, **and attach `not-found.md`** (or the
PDF printed from `not-found.html`). The brief holds the standing rules; the attachment holds the
current list of what is missing and what has already been tried. Keeping them apart is deliberate —
the list changes every pass, and a brief that repeats it goes stale and starts sending people after
things that were found two passes ago.

---

You are helping locate historical sites for a reference map, and the discipline of the task matters
more than how much of it you finish. Read the whole brief before starting.

## The project

An independently compiled map of every place Shrimad Rajchandraji (Param Krupalu Dev, 1867–1901,
Jain mystic and poet, teacher of Mahatma Gandhi) is documented to have visited, stayed in or lived
in. It is not an official publication of any religious body.

Each place carries a town-level pin. Within a place are **sites** — a house, a stepwell, a banyan
tree, a cremation ground. Most sites have no location of their own and are drawn at the centre of
their town, so a pilgrim who arrives still has to ask in the street which building is meant.

**Your task: find locations for as many of those sites as the evidence honestly allows.**

The attached `not-found.md` lists every unplaced site grouped by town, with its survival status and
what is known about it, and ends with what has already been tried and what has not. Work from that
list. Everything in its "already tried" section is closed — do not repeat it.

## The standard, which is the whole point

The governing rule is that **a plausible answer is worse than no answer.** A pilgrim told "we do not
know" can ask someone. A pilgrim sent to the wrong building by a confident pin never finds out they
were misled. The map says "not located" in dozens of places and is not embarrassed about it.

So:

- **Never infer a pin from a neighbouring building.** A worked example of what not to do: the map
  has a site "Shrimad Rajchandra Ashram, Dharampur." OpenStreetMap has a "Shrimad Rajchandra
  Hospital" node at 20.53771, 73.16970, which is the hospital on that ashram's campus. That is *not*
  the ashram, and it is recorded as a navigation aid rather than promoted to a pin. Do the same
  wherever you find something adjacent rather than the thing itself.
- **A modern centre bearing His name is not evidence He was there.** Many trusts built temples and
  ashrams named after Him in the last century. Those are in the data already, correctly, as "later
  memorial."
  *The one exception, and it is a real one:* where a source states that a memorial stands **on** the
  documented spot, the memorial's location is the spot's location. That is how Nadiad and the Idar
  rock were settled — SRMD says its Rachnabhoomi occupies the site of the Atmasiddhi Shastra's
  composition, and the Trust says its Idar ashram sits on the rock He sat on. A source has to say
  so; proximity is not enough.
- **Distinguish what you found from what you concluded.** Every answer carries the URL or
  publication it came from. An answer whose provenance you cannot state is not an answer.
- **Say which of two things a pin is, or say you cannot.** A pass-1 finding at Uttarsanda was
  recorded as a specific building; pass 2 showed the source separates three things there and the pin
  could be either of two of them. That correction cost nothing because the confidence was recorded.
  Guessing would have cost the entry's credibility.
- **"Not found" is a first-class result.** Report it explicitly and say where you looked. It stops
  the next person repeating the search, which is worth as much as a pin.
- **Do not contact any of the trusts, ashrams or missions.** Not by email, not by contact form, not
  by phone. This is a research task only. The owner has decided against approaching them.

## Two method notes that will save you a pass

- **jainqq.org has no usable search.** It exposes no full-text search URL a fetch tool can query —
  the obvious `/search?q=` pattern 404s — and serves its books as per-page scanned images, so
  fetching a page helps only if you already know which page holds the answer. To get value from
  these texts, download the PDFs — several, including a 400-page biography, are mirrored on
  archive.org — and search them locally. This is the single most promising untried avenue, and it
  is a download-and-OCR job rather than a browsing job. Budget for that.
- **The trusts' own prose is exhausted.** Their place-by-place pages have been crawled. The
  Khambhat, Kavitha, Bharuch and Vaso sites are described in devotional language with no street, pol
  name or landmark whatsoever. That is settled: those sites will not be located from anything the
  trusts have published, and re-reading those pages will produce nothing.

## The questions still open

1. **Hadmatiya** — the only place on the map that cannot be placed at all. Named in the VS 1951
   travel entry between Sayla and Dharmaj. At least fifteen census villages in Gujarat carry the
   name; OpenStreetMap holds three (22.43352/70.48005 in Paddhari taluka, Rajkot, which also has a
   railway station of that name; 24.64183/72.68557; and a Hadmatia locality at 20.71343/70.87421).
   None is attested. **Only a source naming the district will settle it.** Census and panchayat
   records, and the local-text OCR above, are the routes left.
2. **The Dhaneshwari Bungalow, Uttarsanda, and Ambalalbhai's house, Khambhat** — the only two
   buildings the Trust explicitly calls original, and neither is located. Khambhat has a candidate:
   a listing named "Shrimad Rajchandra Raj Chhaya" at 3 Pirajpal Rd, Chudiwaal Chakla (22.31758,
   72.61853), in the right quarter of the old city but not named for Ambalalbhai in any source
   found. **Is Raj Chhaya his house?** And **where is the Dhaneshwari Bungalow?**
3. **The Aga Khan's bungalow, Ahmedabad.** The Trust's register states He stayed there with His
   mother and wife in VS 1957 and publishes no address. Ahmedabad's municipal heritage register
   lists no Aga Khan property at all. **Does the building still stand, and where was it?**
   Late-19th-century Ismaili property records are the remaining route.
4. **Which Kumbhnath temple at Nadiad.** The composition site itself is now settled, but no source
   says whether the "Nana Kumbhdev Mahadev" of 1896 is the Nana or the Mota Kumbhnath temple
   standing today. Lower stakes than the others, since a pilgrim can already be sent to the right
   ground.

## How to report what you find

For each site, give exactly this, as a row:

    site name | place | latitude | longitude | confidence | source URL or publication | what convinced you

On **confidence**, use one of these and mean it:

- `Building` — you have identified the specific structure
- `Street-level` — the right street or lane, not the building
- `Locality` — the right neighbourhood, hill or village quarter
- `Not found` — say where you looked

Give coordinates to five decimal places. If you have a Google plus code but no decimal coordinate,
give the plus code and say so rather than converting it loosely — short plus codes need
nearest-cell recovery against a reference point, and taking the reference's own prefix puts the
result tens of kilometres out.

Where you find a **postal address but no coordinate**, report the address. That is a real result;
the map records addresses separately from pins.

Report your failures as carefully as your successes, and flag anything where sources disagree. The
map has a field for exactly that, and a documented contradiction is worth more than a smoothed-over
guess.
