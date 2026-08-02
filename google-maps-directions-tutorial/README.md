# Google Maps Directions Scraper Tutorial: Run This Apify Actor with Python

Extract driving, walking, bicycling, and transit directions between any two locations from Google Maps - distance, duration, traffic, route alternatives, and turn-by-turn steps.

This repository shows how to run [Google Maps Directions Scraper](https://apify.com/crawlerbros/google-maps-directions) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-maps-directions`
- **Apify Store:** [https://apify.com/crawlerbros/google-maps-directions](https://apify.com/crawlerbros/google-maps-directions)
- **SEO title:** Google Maps Directions Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract driving, walking, bicycling, and transit directions between any two locations from Google Maps - distance, duration, traffic, route alternatives, and turn-by-turn steps.

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

# Google Maps Directions Scraper

Extract driving, walking, bicycling, and transit directions between any two locations from Google Maps — including distance, duration, traffic conditions, route alternatives, and turn-by-turn steps.

## What It Does

Provide an origin and a destination (as addresses, place names, or `lat,lng` coordinates), and this actor returns:

- **All route alternatives** Google Maps offers (up to 5)
- **Distance** in both human-readable form (`"1.2 mi"`) and integer meters
- **Duration** in human-readable form (`"8 min"`) and integer seconds
- **"via" road** for each route (e.g. `"via Broadway"`)
- **Traffic condition** notes when available (e.g. `"Moderate traffic"`)
- **Turn-by-turn step instructions** for the primary route (best-effort)
- **Resolved origin and destination** strings (what Google actually matched)
- **The final Google Maps directions URL** you can share or open in a browser

## Use Cases

- ETA calculators, courier and logistics planning, dispatch dashboards
- Travel-time monitoring between business locations
- Field-service routing and territory planning
- Sales and customer-visit scheduling
- Real-estate commute analyses
- Tourism / transit research

## Input

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `origin` | String | yes | — | Starting location (address, place name, or `lat,lng`) |
| `destination` | String | yes | — | Ending location (address, place name, or `lat,lng`) |
| `travelMode` | Enum | no | `driving` | One of `driving`, `walking`, `bicycling`, `transit` |
| `language` | Enum | no | `en` | UI language (affects instruction text) |
| `units` | Enum | no | `metric` | `metric` or `imperial` distance preference |
| `avoidTolls` | Boolean | no | `false` | Driving mode — avoid toll roads |
| `avoidHighways` | Boolean | no | `false` | Driving mode — avoid highways/motorways |
| `avoidFerries` | Boolean | no | `false` | Driving mode — avoid ferry routes |
| `departureTime` | String | no | — | Optional ISO 8601 datetime for transit routing |
| `proxyConfiguration` | Object | no | — | Optional Apify proxy (used only as a fallback) |

**Example input:**

```json
{
  "origin": "Times Square, New York, NY",
  "destination": "Central Park, New York, NY",
  "travelMode": "driving"
}
```

**Walking directions:**

```json
{
  "origin": "Eiffel Tower, Paris",
  "destination": "Louvre Museum, Paris",
  "travelMode": "walking",
  "language": "en"
}
```

## Output

Each route alternative produces one dataset record:

```json
{
  "origin": "Times Square, New York, NY",
  "destination": "Central Park, New York, NY",
  "originResolved": "Times Square",
  "destinationResolved": "Central Park",
  "midpointLocation": { "lat": 40.7700, "lng": -73.9758 },
  "travelMode": "driving",
  "language": "en",
  "units": "metric",
  "routeIndex": 0,
  "distance": "1.2 mi",
  "distanceMeters": 1931,
  "duration": "8 min",
  "durationSeconds": 480,
  "via": "via Broadway",
  "trafficCondition": "Moderate traffic",
  "steps": [
    { "instruction": "Head north on Broadway", "distance": "0.3 mi" }
  ],
  "googleMapsUrl": "https://www.google.com/maps/dir/Times+Square/Central+Park/?hl=en&travelmode=driving",
  "scrapedAt": "2026-06-16T10:30:00+00:00"
}
```

Empty fields are omitted from the record.

## How It Works

- Loads the canonical Google Maps directions URL in a stealth Chromium browser
- Waits for route alternatives to render, then extracts them from the DOM
- Distance and duration strings are also normalised to integer meters / seconds for downstream analytics

## FAQ

**How many routes are returned per run?**
Up to 5 alternatives, in the order Google Maps shows them. `routeIndex: 0` is Google's recommended route.

**Why does Google sometimes resolve my origin/destination differently?**
Google Maps performs its own geocoding and may match the closest known place. The `originResolved` and `destinationResolved` fields show what it actually matched.

**Can I use coordinates instead of addresses?**
Yes — pass `"40.7580,-73.9855"` (or similar) as origin/destination and the actor will route between the exact points.

**Does this actor use cookies or login?**
No. Google Maps directions are public and require no authentication.

**Is a proxy needed?**
Usually not. The actor first attempts the run without a proxy, which is the most reliable approach for Google Maps. If you configure a proxy, it is used only as a fallback.

**What if Google Maps cannot find a route (e.g. between two continents for driving)?**
The actor will report no routes found and fail the run gracefully so you can see the issue in the status message.

## 🗺️ Complete Google Maps Scraper Suite

This actor is part of a comprehensive Google Maps data extraction toolkit by **crawlerbros**. All actors run on the free Apify plan, use no proxy by default, and return clean, structured data.

| Actor | What it does |
|---|---|
| 🏢 [Google Maps Business Scraper](https://apify.com/crawlerbros/google-maps-scraper) | Extract business data — name, address, phone, website, rating, reviews, hours, amenities |
| ⭐ [Google Maps Reviews Scraper](https://apify.com/crawlerbros/google-maps-reviews-scraper) | Scrape reviews with reviewer Local Guide level, photos, mentioned items, owner replies |
| 📸 [Google Maps Photos Scraper](https://apify.com/crawlerbros/google-maps-photos) | Extract all photos from any place — max-resolution URLs, contributor info, categories |
| 🕐 [Google Maps Business Hours Scraper](https://apify.com/crawlerbros/google-maps-business-hours) | Full 7-day hours, timezone, current local time, next open/close, holiday hours |
| 📊 [Google Maps Popular Times Scraper](https://apify.com/crawlerbros/google-maps-popular-times) | Busy hours histogram for all 7 days + current busyness + typical visit time |
| 📧 [Google Maps Email Extractor](https://apify.com/crawlerbros/google-maps-email-extractor) | Find business emails + social media links by crawling websites |
| 🗺️ [Google Maps Area Scanner](https://apify.com/crawlerbros/google-maps-area-scanner) | Geographic grid scanning — bypass the 120-place limit with bounding box / circle / polygon |
| 💼 [Google Maps Leads Scraper](https://apify.com/crawlerbros/google-maps-leads) | B2B lead generation with email + phone enrichment, US states + global countries |
| 🤖 [Google Maps MCP Server](https://apify.com/crawlerbros/google-maps-mcp) | Unified MCP server combining search + reviews for AI assistants |
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

- [Run this actor on Apify](https://apify.com/crawlerbros/google-maps-directions)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
