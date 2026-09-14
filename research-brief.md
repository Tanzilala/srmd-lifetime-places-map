# Research brief — locating the sites

Paste everything below the line into Cowork as a single prompt. It is written to stand on its own:
it does not assume any earlier conversation, and it states what has already been ruled out so the
effort is not spent twice.

---

You are helping locate historical sites for a reference map, and the discipline of the task matters
more than its completeness. Read the whole brief before starting.

## The project

An independently compiled map of every place Shrimad Rajchandraji (Param Krupalu Dev, 1867–1901,
Jain mystic and poet, teacher of Mahatma Gandhi) is documented to have visited, stayed in or lived
in. It is not an official publication of any religious body. The repository is a private GitHub
repo, `Tanzilala/srmd-lifetime-places-map`; if you have it, run `python build.py --unlocated` for
the current list. If you do not, the priority list is at the foot of this brief.

Each place has a town-level pin. Within a place are **sites** — a house, a stepwell, a banyan tree,
a cremation ground. 87 of the 88 sites have no location of their own and are drawn at the centre of
their town, so a pilgrim who arrives still has to ask in the street which building is meant.

**Your task: find locations for as many of those sites as the evidence honestly allows.**

## The standard, which is the whole point

This project's governing rule is that **a plausible answer is worse than no answer.** A pilgrim who
is told "we do not know" can ask someone. A pilgrim sent to the wrong building by a confident pin
does not find out they were misled. The map already says "not located" in 40-odd places and is not
embarrassed about it.

So:

- **Never infer a pin from a neighbouring building.** A worked example of what not to do: the map
  has a site "Shrimad Rajchandra Ashram, Dharampur." OpenStreetMap has a "Shrimad Rajchandra
  Hospital" node at 20.53771, 73.16970, which is the hospital on that ashram's campus. That is
  *not* the ashram, and it was deliberately recorded as a navigation aid rather than promoted to a
  pin. Do the same wherever you find something adjacent rather than the thing itself.
- **A modern centre bearing His name is not evidence He was there.** Many trusts have built temples
  and ashrams named after Him in the last century. Those are already in the data, correctly, as
  "later memorial." Do not treat a memorial's location as the location of a lifetime site unless a
  source says the memorial stands on the documented spot.
- **Distinguish what you found from what you concluded.** Every answer must carry the URL or
  publication it came from. An answer whose provenance you cannot state is not an answer.
- **"Not found" is a first-class result.** Report it explicitly and say where you looked. That is
  genuinely useful — it stops the next person repeating the search.
- **Do not contact any of the trusts, ashrams or missions.** Not by email, not by contact form, not
  by phone. This is a research task only. The owner has decided against approaching them.

## What has already been tried, and failed

Do not repeat these:

- **OpenStreetMap and Overpass.** Exhaustively queried. OSM holds exactly two Rajchandra-named
  features in the whole of Gujarat, both hospitals. None of the ashrams, temples, houses, stepwells
  or banyans is mapped. Nominatim returns nothing for these site names.
- **The trusts' own websites.** shrimadrajchandratrust.org, srmd.org and rajsaubhag.org publish
  postal addresses for a handful of sites — already recorded — and no coordinates anywhere.
- **English-language web search** for the four named open questions below. Exhausted.

## What has not been tried, and should be

In rough order of expected yield:

1. **Google Maps / Google Places.** This is the significant untried avenue. Indian temples, ashrams,
   upashrays and even individual heritage houses are very often present as user-contributed places
   in Google Maps when they are entirely absent from OpenStreetMap. Search the site names, in both
   English and Gujarati. Where you find one, capture the coordinates, the plus code, and the
   reviews and photos, which frequently confirm the identification.
2. **Gujarati-language search.** Most of what exists on these sites was never written in English.
   Search the Gujarati names — શ્રીમદ્ રાજચંદ્ર, વવાણિયા, ઉત્તરસંડા, ખંભાત, કાવીઠા, વડવા, ઈડર — and
   Gujarati words for the site types: વાવ (stepwell), ઉપાશ્રય (upashray), દેરાસર (temple),
   સ્મશાન (cremation ground), વડ (banyan).
3. **jainqq.org full texts.** It hosts scanned and romanised Jain literature including the
   Ardhashatabdi Smarak Granth and Sachitra Jivan Darshan. These are the primary biographical
   sources and are likely to describe locations in terms of landmarks.
4. **Yatra accounts.** Devotees post detailed trip reports, photographs and video of these pilgrimage
   routes on blogs, YouTube and Instagram. A video walking from a bus stand to a house is often
   enough to identify the building on satellite imagery. Photographs sometimes carry EXIF
   coordinates.
5. **Wikimapia and Bhuvan (ISRO).** Both have Indian coverage that OSM lacks. Wikimapia in
   particular has user-drawn outlines for many Gujarat villages.
6. **Village and census records.** For Rajpur and Hadmatiya below, census village codes and
   panchayat rosters may give a location where gazetteers do not.

## The four standing questions

Beyond the site list, these are open and each is worth more than any single pin:

1. **Hadmatiya.** Named in the VS 1951 travel entry between Sayla and Dharmaj. At least fifteen
   census villages in Gujarat carry this name; OpenStreetMap holds three (22.43352/70.48005 in
   Paddhari taluka, Rajkot — which also has a railway station of that name; 24.64183/72.68557; and a
   Hadmatia locality at 20.71343/70.87421). None is attested. **Which one is His?** Only a source
   naming the district will settle it.
2. **Rajpur, Khambhat taluka, Anand district.** Confirmed to exist — about 9 km from Khambhat,
   pincode 388640, 2,444.88 hectares, in the 'Ralaj-Rajpura' gram panchayat alongside Ralej and
   Metpur. No published coordinate found. **Where is it?**
3. **Ghantiya Pahad, at Barvav near Idar.** The Shrimad Rajchandra Trust gives its Idar ashram's
   address as "Ghantiya Pahad, Idar 383430" and describes the hill as about 2 km from Idar town.
   Neither the hill nor Barvav village is in OpenStreetMap. **Where is the hill?**
4. **The Aga Khan's bungalow, Ahmedabad.** The Trust's own register states that in VS 1957 (1900–01)
   He stayed there with His mother and wife, and publishes no address. Nothing independent has been
   found. **Does the building still stand, and where was it?** Late-19th-century Ismaili property
   records or Ahmedabad heritage surveys may be the route.

## How to report what you find

For each site, give exactly this, as a row:

    site name | place | latitude | longitude | confidence | source URL or publication | what convinced you

On **confidence**, use one of these words and mean it:

- `Building` — you have identified the specific structure
- `Street-level` — you have the right street or lane, not the building
- `Locality` — you have the right neighbourhood or village quarter
- `Not found` — say where you looked

Give coordinates to five decimal places. If you have a Google plus code but not decimal
coordinates, give the plus code and say so rather than converting it loosely.

Where you find a **postal address but no coordinate**, report the address — that is a real result
and the project records addresses separately from pins.

Finally, please report your failures as carefully as your successes, and flag anything where the
sources disagree with each other. The map has a "caution" field for exactly that, and a documented
contradiction is more valuable than a smoothed-over guess.

## Priority list — the 38 sites that still stand

These are the sites recorded as surviving from His lifetime, so they are the ones a pilgrim can
actually visit, and they matter most. (A further 49 sites are memorials or unidentified; the
repository's `--unlocated` output has the full list.)

- **Vavania** (town pin 23.00552, 70.61034) — Crematorium / lake area of the jatismaran-jnan
- **Rajkot** (22.30000, 70.78330) — Narmada Mansion / Samadhi Bhavan *(the house where He died,
  9 April 1901 — the single highest-value pin on this list)*
- **Mumbai** (18.95181, 72.83070) — Zaveri Bazaar / Bhuleshwar business quarter
- **Ahmedabad** (23.02250, 72.57139) — Residence of Shri Jesangbhai Sheth; Hathising ni Vaadi, the
  small room above the main gate; Building in Ghanchi's Pol, old city; Saraspur Upashray
- **Bharuch** (21.71200, 72.99300) — Residence of Shri Anupchand Malukchand; the crematory He used
  for meditation; Shri Samali Vihar Jinmandir
- **Khambhat** (22.31670, 72.62430) — Shri Ambalalbhai's house and room *(one of only two buildings
  the Trust explicitly calls original)*; Shri Subodhak Pustakalay; Sthanakvasi Upashray, third
  floor; Jain temple near Ambalalbhai's house
- **Ralej** (22.29988, 72.68147) — the banyan and lakeshore where He sat
- **Kavitha** (22.44165, 72.87206) — Residence of Shri Zaverchand Sheth; Gamot Vad (banyan); Vijali
  Mata no Vad (banyan); Dhainia no Vad (banyan); Mithuji no Kuvo (well); Shamal Dosa nu Khetar
  (field)
- **Vadva, Metpur, Khambhat 388620** (22.31050, 72.63590) — the room beside the stepwell; the Vaav
  (stepwell) itself; the Vad (banyan) where He preached
- **Nadiad** (22.69000, 72.86000) — Nana Kumbhdev Mahadev *(the Atmasiddhi Shastra was composed at
  Nadiad on 22 October 1896 — arguably the most significant single location of His life)*
- **Idar, Ghantiya Pahad 383430** (23.83900, 73.00200) — Pudhavi Sheela (the rock); Bhurabawa ni
  Gufa (cave); the Shwetambar and Digambar hill temples; Ghantiya Pahad itself
- **Naroda** (23.08300, 72.66700) — the lake at Naroda
- **Dharampur, Shrimad Rajchandra Marg 396050** (20.53000, 73.18000) — the forest and hill retreat
  landscape
- **Tithal** (20.58800, 72.90100) — Tithal Bungalow
- **Uttarsanda** (22.65778, 72.89806) — Dhaneshwari Bungalow *(the other building the Trust
  explicitly calls original)*
- **Vaso** (22.66000, 72.75000) — Navlakha nu Dehlu; Mahadev Temple; the old crematorium; Digambar
  temple; Shwetambar temple
