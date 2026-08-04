# CruiseMapper Cruises Scraper Tutorial: Run This Apify Actor with Python

Search CruiseMapper.com for cruise itineraries by destination, ship, cruise line, departure port, length, and date. Returns ship name, dates, route, duration, and starting price per cruise.

This repository shows how to run [CruiseMapper Cruises Scraper](https://apify.com/crawlerbros/cruisemapper-cruises-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/cruisemapper-cruises-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/cruisemapper-cruises-scraper](https://apify.com/crawlerbros/cruisemapper-cruises-scraper)
- **SEO title:** CruiseMapper Cruises Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Search CruiseMapper.com for cruise itineraries by destination, ship, cruise line, departure port, length, and date. Returns ship name, dates, route, duration, and starting price per cruise.

## Run Locally

```bash
python -m pip install -r requirements.txt
cp .env.example .env
cp input.example.json input.json
python main.py
```

Set `APIFY_TOKEN` in `.env`, then edit `input.json` according to the actor README below. The script calls the actor and prints JSON results from the default dataset.

## Actor README

The following README is copied from the Apify actor page/source and should be treated as the source of truth.

# CruiseMapper Cruises Scraper

Search [CruiseMapper.com](https://www.cruisemapper.com) — the largest free public cruise database — by destination, ship, cruise line, length, type, and date. Returns one structured record per cruise with departure date, ship, duration, route, title, and starting price. HTTP-only — no proxy, no cookies, no API key.

## What it does

You set any combination of filters; the actor:

1. Submits the search to `cruisemapper.com/cruise-search` with your filters mapped to the site's form params.
2. Walks paginated result pages (15 cruises per page) until `maxResults` is reached.
3. Parses each result row into a flat record with date, ship, duration, route type, title, price, and ship-detail URL.
4. Optionally narrows results by an `endDate` upper bound and `cruiseLength` bucket (client-side validation).

Empty fields are omitted (no nulls). Cruises without a published price still emit a record with `priceFrom`/`currency` absent.

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `departureFrom` | string | – | Earliest cruise departure date `YYYY-MM-DD`. Empty = no lower bound. |
| `endDate` | string | – | Latest cruise departure date `YYYY-MM-DD`. Empty = no upper bound. Client-side filter. |
| `cruiseLength` | enum | `any` | One of `any`, `1-2`, `3-5`, `6-10`, `11-14`, `15+`. |
| `destination` | enum | `any` | Cruise region (e.g. `alaska`, `mediterranean-black-sea`, `bahamas-caribbean-bermuda`, `nile-river`, `arctic-antarctica`, `asia`). 24 regions supported. |
| `cruiseType` | enum | `any` | Theme / category (e.g. `transatlantic`, `christmas`, `food-wine`, `northern-lights`, `panama-canal`, `world`). 25 types supported. |
| `shipName` | string | – | Substring match against the ship name (e.g. `Symphony of the Seas`). |
| `cruiseLine` | string | – | Filter by cruise line (e.g. `Royal Caribbean`, `Carnival`). |
| `departurePort` | string | – | Filter by embarkation port (e.g. `Miami`, `Barcelona`). |
| `portOfCall` | string | – | Filter by intermediate port-of-call (e.g. `Cozumel`). |
| `maxPrice` | integer | `10000` (100–100000) | Drop cruises with starting price above this USD amount. |
| `maxResults` | integer | `50` (1–500) | Hard cap on records emitted across all pages. |
| `enrichWithShipData` | boolean | `false` | When true, fetch the ship-detail page for each unique ship and add a `shipDetails` block (year built, builder, gross tonnage, passenger capacity, length, decks, cabins). Adds ~1 extra HTTP request per unique ship. |
| `startUrls` | array of strings | `[]` | Paste full CruiseMapper search URLs (e.g. `https://www.cruisemapper.com/cruise-search?finder=cruise&portRegion=22`). Each URL's query params become a search; results merge + dedup with the main filter inputs. |
| `pageConcurrency` | integer | `1` (1–10) | Number of pages to fetch in parallel per query. Higher values speed up bulk runs; may trigger rate-limits. |

### Example input

```json
{
  "departureFrom": "2026-06-01",
  "endDate": "2026-09-30",
  "cruiseLength": "6-10",
  "destination": "alaska",
  "cruiseType": "any",
  "maxResults": 100
}
```

## Output

One record per cruise. Empty fields are omitted (no nulls).

```json
{
  "departureDate": "2026-06-15",
  "departureDateText": "2026 Jun 15",
  "daysUntilDeparture": 14,
  "shipName": "AmaLilia",
  "shipUrl": "https://www.cruisemapper.com/ships/AmaLilia-1340",
  "duration": 11,
  "routeType": "round-trip",
  "title": "Secrets of Egypt the Nile",
  "priceFrom": 6334,
  "currency": "USD",
  "shipDetails": {
    "yearBuilt": 2024,
    "builder": "Maasara Shipyard (Cairo, Egypt)",
    "shipClass": "Nile River cruiser",
    "speed": "9 kn / 17 km/h / 10 mph",
    "lengthMeters": 72,
    "beamMeters": 13,
    "passengerCapacity": 68,
    "crewCount": 62,
    "deckCount": 5,
    "cabinCount": 34
  },
  "scrapedAt": "2024-12-16T14:23:11+00:00"
}
```

### Output fields

- **`departureDate`** — ISO date `YYYY-MM-DD` of departure (parsed from the table's free-form text).
- **`departureDateText`** — original date string from the page (e.g. `"2026 Apr 27"`) — useful for QA / verification.
- **`daysUntilDeparture`** — derived integer: days from now (UTC) to `departureDate`. Negative for departures in the past.
- **`shipName`** — vessel name as listed by CruiseMapper.
- **`shipUrl`** — direct link to the ship's CruiseMapper detail page (deck plans, photos, cabin info).
- **`duration`** — cruise length in days (parsed from `"N days, ..."`).
- **`routeType`** — `round-trip`, `one-way`, `open-jaw`, or `transatlantic` when present in the title prefix.
- **`title`** — cruise itinerary title (e.g. `"Secrets of Egypt the Nile"`, `"Western Caribbean"`).
- **`priceFrom`** — starting USD price as integer; absent when CruiseMapper doesn't publish a price for the cruise.
- **`currency`** — `USD` / `EUR` / `GBP`; absent when `priceFrom` is absent.
- **`shipDetails`** — (only when `enrichWithShipData: true`) flat dict with `yearBuilt`, `builder`, `shipClass`, `flagState`, `speed`, `lengthMeters`, `beamMeters`, `draftMeters`, `grossTonnage`, `passengerCapacity`, `crewCount`, `deckCount`, `cabinCount`, `decksWithCabins`, `engines`, etc. Each ship is fetched once per run and cached.
- **`scrapedAt`** — ISO-8601 UTC timestamp.

## Use cases

- **Travel-planning aggregation** — feed your travel app with fresh CruiseMapper inventory.
- **Price-monitoring** — track starting-price trends for specific ships / cruise lines / destinations over time.
- **Competitive research** — see what competitors are pricing for the same routes.
- **Content / editorial** — generate weekly "Cruises departing this month from Miami" digests.
- **Inventory enrichment** — combine with a cruise-line site scraper to triangulate pricing across sources.

## FAQ

**Does it need a proxy or cookies?**
No. CruiseMapper search results are public and the actor connects directly with a Chrome-impersonated TLS fingerprint.

**Why is `priceFrom` missing on some records?**
Roughly 30–40% of CruiseMapper listings don't publish a starting price (they require contacting the cruise line). The actor follows an omit-empty contract — fields not present on the source are simply absent from the record (no nulls).

**Are the date / duration filters server-side or client-side?**
Mixed. `departureFrom`, `cruiseLength`, `destination`, `cruiseType`, `shipName`, `cruiseLine`, `departurePort`, `portOfCall`, and `maxPrice` are submitted as form params (server-side). `endDate` and the duration-bucket boundary check are applied client-side after parsing each result row, since CruiseMapper's form has no end-date field.

**How many results can I get in one run?**
Up to `maxResults` (max 500). CruiseMapper paginates ~15 cruises per page; 500 records ≈ 34 pages × ~1.5s = under a minute on a clean run.

**Can I scrape ship-detail pages too?**
This actor focuses on the search results table. Use the `shipUrl` field with a downstream actor (or a follow-up run) for ship deck plans, cabin layouts, and photos.

**What if my filters return zero cruises?**
You get a single sentinel record `{type: "cruisemapper_scraper_error", reason: "no_results"}`. The run still completes successfully — empty datasets aren't treated as failures.

**Why is the route type sometimes empty?**
CruiseMapper only embeds `round-trip`/`one-way`/`open-jaw`/`transatlantic` in the title for ~70% of cruises. When the title doesn't start with a known route-type prefix, the field is omitted.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/cruisemapper-cruises-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
