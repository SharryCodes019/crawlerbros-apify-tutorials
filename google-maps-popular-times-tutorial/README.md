# Google Maps Popular Times Scraper Tutorial: Run This Apify Actor with Python

Extract popular times busy-hours histograms and live busyness data from Google Maps places - all 7 days with hourly percentages, current busyness, and typical time spent.

This repository shows how to run [Google Maps Popular Times Scraper](https://apify.com/crawlerbros/google-maps-popular-times) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-maps-popular-times`
- **Apify Store:** [https://apify.com/crawlerbros/google-maps-popular-times](https://apify.com/crawlerbros/google-maps-popular-times)
- **SEO title:** Google Maps Popular Times Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract popular times busy-hours histograms and live busyness data from Google Maps places - all 7 days with hourly percentages, current busyness, and typical time spent.

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

# Google Maps Popular Times Scraper

Extract the **Popular Times** histogram for any Google Maps place — the busy-hours bar chart that Google shows on most restaurants, shops, gyms, and tourist attractions. Get hourly busyness percentages for all 7 days of the week, plus the live "current busyness" reading and typical visit duration.

## What It Does

Give this actor a Google Maps place URL and it returns:

- **Per-day hourly busyness** (0–100%) for Monday through Sunday — a full week of data in one request
- **Peak hour** and **peak busyness percentage** for each day
- **Quietest hour** for each day
- **Live busyness** reading at the moment of scraping (e.g. *"As busy as it gets"*, *"A little busy"*)
- **Typical time spent** at the place (e.g. *"People typically spend 30 min to 1 hour here"*)
- **Business name + Place ID** for cross-referencing with the Google Maps API
- **Location** (lat/lng) and place URL echoed on every record so datasets stay joinable

## Use Cases

- Plan field operations and logistics around quietest hours
- Find optimal times to visit popular tourist attractions
- Build foot-traffic dashboards for retail, restaurants, and gyms
- Inform staffing decisions for franchise networks
- Power "when to go" recommendations in travel apps

## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `placeUrls` | Array of strings | Yes | One or more Google Maps place URLs |

### Example input — single place

```json
{
  "placeUrls": [
    "https://www.google.com/maps/place/McDonald%27s/@40.7577297,-73.9853627,17z/"
  ]
}
```

### Example input — batch

```json
{
  "placeUrls": [
    "https://www.google.com/maps/place/Starbucks/@40.7127281,-74.0060152,17z/",
    "https://www.google.com/maps/place/McDonald%27s/@40.7577297,-73.9853627,17z/",
    "https://www.google.com/maps/place/Whole+Foods+Market/@40.7561,-73.9903,17z/"
  ]
}
```

## Output

One record per place:

```json
{
  "businessName": "McDonald's",
  "placeId": "0x89c2597777397641:0x4387a82ee10d3e3b",
  "placeUrl": "https://www.google.com/maps/place/McDonald%27s/...",
  "location": {"lat": 40.7577297, "lng": -73.9853627},
  "liveBusyness": "A little busy",
  "typicalTimeSpent": "People typically spend 15-30 min here",
  "popularTimes": {
    "monday":    [{"hour": 6, "busyness": 12}, {"hour": 7, "busyness": 38}, "..."],
    "tuesday":   [{"hour": 6, "busyness": 14}, "..."],
    "wednesday": [{"hour": 6, "busyness": 11}, "..."],
    "thursday":  [{"hour": 6, "busyness": 13}, "..."],
    "friday":    [{"hour": 6, "busyness": 16}, "..."],
    "saturday":  [{"hour": 7, "busyness": 22}, "..."],
    "sunday":    [{"hour": 7, "busyness": 18}, "..."]
  },
  "peakHours": {
    "monday":    {"hour": 12, "busyness": 89},
    "tuesday":   {"hour": 12, "busyness": 84},
    "wednesday": {"hour": 13, "busyness": 91},
    "thursday":  {"hour": 12, "busyness": 87},
    "friday":    {"hour": 18, "busyness": 96},
    "saturday":  {"hour": 14, "busyness": 78},
    "sunday":    {"hour": 13, "busyness": 71}
  },
  "scrapedAt": "2026-06-16T18:23:11+00:00"
}
```

Empty / unavailable fields are omitted from the record — no `null` values appear in the dataset.

### Hourly busyness format

Each day in `popularTimes` is an array of `{hour, busyness}` pairs:

- `hour` — 0–23 (local time at the business)
- `busyness` — integer 0–100 (Google's relative busyness percentage; 100 = peak for that place)

Hours with no data (e.g. while the place is closed) are omitted from the array.

## FAQ

**Which places have Popular Times data?**
Restaurants, cafés, retail stores, gyms, grocery stores, and major tourist attractions almost always have it. Small businesses, services without foot traffic, and very new listings often do not.

**Why is `liveBusyness` sometimes missing?**
Google only shows live data while the place is currently open and has enough recent visits to compute it. When the place is closed or hasn't reached the data threshold, the field is omitted.

**How is `busyness` measured?**
Google reports it as a percentage of peak for that specific place. `100` means "as busy as this place ever gets". The values are derived from aggregated, anonymised Google location-history data.

**Do I need a proxy or cookies?**
No login required. A proxy is not necessary for typical runs; Google Maps serves Popular Times without restriction from datacenter IPs.

**Can I scrape hundreds of places in one run?**
Yes — pass them as `placeUrls`. The actor processes places sequentially with a polite delay between requests. For very large batches, split into multiple runs.

**Does this scrape the Google Places API?**
No. It loads the public-facing Google Maps web page (Playwright + Chromium) and extracts the embedded data block, so no API key, no billing, no quota.

## Data Source

Public Google Maps web UI (`google.com/maps`). No Google API key or login is required.

## 🗺️ Complete Google Maps Scraper Suite

This actor is part of a comprehensive Google Maps data extraction toolkit by **crawlerbros**. All actors run on the free Apify plan, use no proxy by default, and return clean, structured data.

| Actor | What it does |
|---|---|
| 🏢 [Google Maps Business Scraper](https://apify.com/crawlerbros/google-maps-scraper) | Extract business data — name, address, phone, website, rating, reviews, hours, amenities |
| ⭐ [Google Maps Reviews Scraper](https://apify.com/crawlerbros/google-maps-reviews-scraper) | Scrape reviews with reviewer Local Guide level, photos, mentioned items, owner replies |
| 📸 [Google Maps Photos Scraper](https://apify.com/crawlerbros/google-maps-photos) | Extract all photos from any place — max-resolution URLs, contributor info, categories |
| 🕐 [Google Maps Business Hours Scraper](https://apify.com/crawlerbros/google-maps-business-hours) | Full 7-day hours, timezone, current local time, next open/close, holiday hours |
| 📧 [Google Maps Email Extractor](https://apify.com/crawlerbros/google-maps-email-extractor) | Find business emails + social media links by crawling websites |
| 🗺️ [Google Maps Area Scanner](https://apify.com/crawlerbros/google-maps-area-scanner) | Geographic grid scanning — bypass the 120-place limit with bounding box / circle / polygon |
| 💼 [Google Maps Leads Scraper](https://apify.com/crawlerbros/google-maps-leads) | B2B lead generation with email + phone enrichment, US states + global countries |
| 🤖 [Google Maps MCP Server](https://apify.com/crawlerbros/google-maps-mcp) | Unified MCP server combining search + reviews for AI assistants |
| 🧭 [Google Maps Directions Scraper](https://apify.com/crawlerbros/google-maps-directions) | A→B routing — distance, duration, traffic, route alternatives for driving/walking/transit |
| 📍 [Google Maps Geocoding Scraper](https://apify.com/crawlerbros/google-maps-geocoding) | Bidirectional geocoding — address ↔ coordinates, with address components |
| 🔗 [Google Maps Similar Places Scraper](https://apify.com/crawlerbros/google-maps-similar-places) | "People also search for" / related place discovery — competitor & alternative finder |
| 🍽️ [Google Maps Menu Scraper](https://apify.com/crawlerbros/google-maps-menu) | Restaurant menu items, prices, descriptions, photos |
| 📌 [Google Maps Nearby Scraper](https://apify.com/crawlerbros/google-maps-nearby) | Find places near a coordinate point — lightweight POI search by category |
| 📋 [Google Maps Place List Scraper](https://apify.com/crawlerbros/google-maps-place-list) | Extract Google's curated "Top X in Y" lists — best hotels/restaurants/things to do |
| 🌍 [Google Maps Timezone Scraper](https://apify.com/crawlerbros/google-maps-timezone) | IANA timezone + current local time from coordinates |

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-maps-popular-times)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
