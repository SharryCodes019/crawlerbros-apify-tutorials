# Zillow Open Houses Scraper Tutorial: Run This Apify Actor with Python

Scrape upcoming open house events from Zillow by location. Returns date, time, address, price, beds/baths, agent, and full property details for each scheduled open house.

This repository shows how to run [Zillow Open Houses Scraper](https://apify.com/crawlerbros/zillow-open-houses-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/zillow-open-houses-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/zillow-open-houses-scraper](https://apify.com/crawlerbros/zillow-open-houses-scraper)
- **SEO title:** Zillow Open Houses Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape upcoming open house events from Zillow by location. Returns date, time, address, price, beds/baths, agent, and full property details for each scheduled open house.

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

# Zillow Open Houses Scraper

Scrape upcoming open house events from Zillow by location. Get date, time, address, price, beds/baths, full property details, and the hosting agent — all in one structured dataset.

## What you get

Each result contains:
- **Open house schedule** — all upcoming events with start/end times and type (in-person or virtual)
- **Property details** — address, price, beds, baths, sqft, year built, lot size, HOA fee
- **Agent info** — listing agent name, phone, and brokerage
- **Photos** — array of property photo URLs
- **Convenience field** — `nextOpenHouse` points to the soonest upcoming event

## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `search` | string | one of search/startUrls | Free-text location: city, ZIP code, neighborhood (e.g. `Austin, TX`, `90210`) |
| `startUrls` | array | one of search/startUrls | Zillow search or open-house URLs — the open house filter is added automatically |
| `dateFrom` | string | no | Only include events on or after this date (`YYYY-MM-DD`) |
| `dateTo` | string | no | Only include events on or before this date (`YYYY-MM-DD`) |
| `maxItems` | integer | no | Maximum listings to return (1–500, default: 100) |
| `scrapeDetails` | boolean | no | Fetch full property details — sqft, photos, agent info (default: true) |

## Output

One record per property. Open house events are nested under `openHouses`.

```json
{
  "url": "https://www.zillow.com/homedetails/123-main-st/12345678_zpid/",
  "zpid": 12345678,
  "status": "FOR_SALE",
  "address": "123 Main St",
  "city": "Austin",
  "state": "TX",
  "zipCode": "78701",
  "latitude": 30.2672,
  "longitude": -97.7431,
  "price": 450000,
  "zestimate": 455000,
  "beds": 3,
  "baths": 2,
  "sqft": 1850,
  "yearBuilt": 2005,
  "propertyType": "SINGLE_FAMILY",
  "hoaFee": 150,
  "agentName": "Jane Smith",
  "agentPhone": "512-555-0100",
  "brokerName": "Realty Austin",
  "photos": ["https://photos.zillowstatic.com/fp/abc123.jpg"],
  "openHouses": [
    {
      "startDateTime": "2026-05-03T13:00:00",
      "endDateTime": "2026-05-03T15:00:00",
      "openHouseType": "INPERSON"
    }
  ],
  "nextOpenHouse": {
    "startDateTime": "2026-05-03T13:00:00",
    "endDateTime": "2026-05-03T15:00:00",
    "openHouseType": "INPERSON"
  },
  "scrapedAt": "2026-04-30T10:00:00Z"
}
```

## Use cases

- **Home buyers** — build a weekend open house calendar for a target neighborhood or ZIP code
- **Real estate agents** — monitor competitor open house activity in your market
- **Market researchers** — track open house frequency and pricing by area over time
- **Lead generation** — identify active listings with upcoming open houses

## Examples

**Open houses this weekend in Austin:**
```json
{
  "search": "Austin, TX",
  "dateFrom": "2026-05-04",
  "dateTo": "2026-05-05",
  "maxItems": 100
}
```

**All upcoming open houses in a single ZIP, with full property detail:**
```json
{
  "search": "78704",
  "scrapeDetails": true,
  "maxItems": 50
}
```

**Pull from a Zillow search URL directly:**
```json
{
  "startUrls": [
    "https://www.zillow.com/austin-tx/open-houses/"
  ]
}
```

## FAQ

**How many open houses can I scrape?**
Up to 500 per run (set via `maxItems`). Run multiple times with different locations or date ranges to collect more.

**Can I filter by date?**
Yes. Use `dateFrom` and `dateTo` (format: `YYYY-MM-DD`) to get only open houses within a date range. Both fields are optional — you can set just one.

**What is `nextOpenHouse`?**
A convenience field containing the soonest upcoming open house event for the property. It always equals `openHouses[0]` (events are sorted chronologically).

**What does `openHouseType` mean?**
Either `INPERSON` (on-site visit) or `VIRTUAL` (online showing).

**Can I use Zillow URLs directly?**
Yes. Paste any Zillow search or property URL into `startUrls`. The open house filter is injected automatically if not already present.

**Does it work for all US markets?**
Yes. Any location searchable on Zillow works — city names, ZIP codes, neighborhoods, or full addresses.

**How fresh is the data?**
The scraper fetches live data from Zillow at the time of each run. Open house schedules are time-sensitive, so run it close to when you plan to use the results.

**Why are some fields missing from certain records?**
Empty, null, and zero-value fields are omitted to keep output clean. Fields like `sqft` or `hoaFee` may not be available for every listing.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/zillow-open-houses-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
