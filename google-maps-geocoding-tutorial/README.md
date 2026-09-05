# Google Maps Geocoding Scraper Tutorial: Run This Apify Actor with Python

Bidirectional geocoding via Google Maps: convert addresses to coordinates (forward) or coordinates to addresses (reverse). Batch input supported with structured address components, place IDs, plus codes, and place categories.

This repository shows how to run [Google Maps Geocoding Scraper](https://apify.com/crawlerbros/google-maps-geocoding) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-maps-geocoding`
- **Apify Store:** [https://apify.com/crawlerbros/google-maps-geocoding](https://apify.com/crawlerbros/google-maps-geocoding)
- **SEO title:** Google Maps Geocoding Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Bidirectional geocoding via Google Maps: convert addresses to coordinates (forward) or coordinates to addresses (reverse). Batch input supported with structured address components, place IDs, plus codes, and place categories.

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

# Google Maps Geocoding Scraper

Bidirectional geocoding via Google Maps. Convert street addresses into latitude/longitude coordinates (forward geocoding), or convert coordinates back into a human-readable address (reverse geocoding). Supports batch input, multiple languages, and country bias for ambiguous queries.

## What it does

- **Forward geocoding** — given an address, returns the resolved coordinates, place ID, structured address components, plus code, and a stable Google Maps URL.
- **Reverse geocoding** — given a `{lat, lng}` pair, returns the nearest matched place name and address.

Each input produces exactly one record in the dataset. Inputs that Google cannot resolve are still recorded (`"resolved": false`) so you can audit failures.

## Input

| Field | Type | Description |
|---|---|---|
| `mode` | enum (`forward` \| `reverse`) | Which direction to geocode. Default: `forward`. |
| `address` | string | A single address (forward mode). |
| `addresses` | array of strings | Batch of addresses (forward mode). |
| `location` | object `{lat, lng}` | A single coordinate (reverse mode). |
| `locations` | array of `{lat, lng}` | Batch of coordinates (reverse mode). |
| `language` | enum | Interface language (`en`, `es`, `fr`, `de`, `it`, `pt`, `ja`, `ko`, `zh`, `ar`, `ru`). Default: `en`. |
| `country` | string | Optional ISO 3166-1 alpha-2 code (e.g. `US`, `GB`) used to bias results when an address is ambiguous. |
| `proxyConfiguration` | proxy | Optional. By default the scraper runs without a proxy because Apify proxy frequently routes through regions that trigger Google's consent flow. |

### Example inputs

**Forward (single):**
```json
{
  "mode": "forward",
  "address": "1600 Amphitheatre Parkway, Mountain View, CA",
  "language": "en"
}
```

**Forward (batch):**
```json
{
  "mode": "forward",
  "addresses": [
    "Eiffel Tower, Paris",
    "Big Ben, London",
    "Tokyo Tower, Tokyo"
  ],
  "language": "en"
}
```

**Reverse (single):**
```json
{
  "mode": "reverse",
  "location": {"lat": 40.7579, "lng": -73.9855}
}
```

**Reverse (batch):**
```json
{
  "mode": "reverse",
  "locations": [
    {"lat": 48.8584, "lng": 2.2945},
    {"lat": 35.6586, "lng": 139.7454},
    {"lat": -33.8568, "lng": 151.2153}
  ]
}
```

## Output

Each dataset record contains a subset of these fields (empty fields are omitted):

| Field | Type | Description |
|---|---|---|
| `mode` | string | `"forward"` or `"reverse"`. |
| `inputAddress` | string | Original address (forward mode only). |
| `inputLocation` | object | Original coordinates (reverse mode only). |
| `resolved` | boolean | Whether Google resolved the input to a place. |
| `name` | string | Place name (h1 on the place page); often blank for pure street addresses. |
| `formattedAddress` | string | Full address as Google formats it. |
| `location` | object | `{lat, lng}` of the resolved place. |
| `placeId` | string | Google's internal feature ID (hex:hex format). |
| `plusCode` | string | Open Location Code if present. |
| `addressComponents` | object | Structured `{streetNumber, street, city, state, postalCode, country, countryCode}`. |
| `categoryName` | string | Google's category label when the resolved place is a business. |
| `googleMapsUrl` | string | Stable `/maps/place/` URL. |
| `scrapedAt` | string | UTC ISO-8601 timestamp. |
| `error` | string | Present only when scraping failed. |

### Example output

```json
{
  "mode": "forward",
  "inputAddress": "1600 Amphitheatre Parkway, Mountain View, CA",
  "resolved": true,
  "name": "Google Building 41",
  "formattedAddress": "1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA",
  "location": {"lat": 37.4224864, "lng": -122.0855962},
  "placeId": "0x808fba02f1822489:0x37a9269fbae1c4f7",
  "plusCode": "CWC8+W4 Mountain View, California",
  "addressComponents": {
    "streetNumber": "1600",
    "street": "Amphitheatre Pkwy",
    "city": "Mountain View",
    "state": "CA",
    "postalCode": "94043",
    "country": "USA",
    "countryCode": "US"
  },
  "categoryName": "Corporate office",
  "googleMapsUrl": "https://www.google.com/maps/place/...",
  "scrapedAt": "2026-06-16T12:00:00+00:00"
}
```

## FAQs

**Q: Do I need an API key?**
No. This scraper uses the public Google Maps web interface — no API key, no quota, no billing.

**Q: How many results does it return per input?**
One record per input. If an address is ambiguous, Google picks the highest-confidence match (the same one you would see at the top of `maps.google.com`).

**Q: How accurate are the coordinates?**
Coordinates are extracted directly from Google's resolved `/maps/place/…` URL with full precision (often 7 decimal places, sub-centimetre accuracy).

**Q: Why does my batch of 10 addresses take 1–2 minutes?**
The scraper navigates a real browser for each address with a small polite delay between requests to avoid rate-limiting. Throughput is roughly 5–8 addresses per minute.

**Q: Should I use a proxy?**
Usually no. The default no-proxy path is the most reliable because Apify proxy often routes through EU regions that trigger Google's consent screen. Use the optional `proxyConfiguration` only if you hit rate-limits.

**Q: What languages are supported?**
The `language` input controls the Google Maps interface language and the format of the returned address (e.g. street names, country names in the target language). Currently exposed: English, Spanish, French, German, Italian, Portuguese, Japanese, Korean, Chinese, Arabic, Russian.

**Q: Can I bias results to a specific country?**
Yes. Set `country` to an ISO 3166-1 alpha-2 code (e.g. `US`, `GB`, `FR`). The scraper appends the country name to ambiguous queries (e.g. `Big Ben` → `Big Ben, UK`).

**Q: What happens for unresolvable inputs?**
A record is still pushed with `"resolved": false` and the original input echoed back in `inputAddress` / `inputLocation`, so you can audit failures.

## Use cases

- Convert a CSV of customer addresses to coordinates for mapping.
- Enrich event logs with city/state/country from raw GPS pings.
- Validate user-submitted addresses against Google's canonical form.
- Reverse-geocode IoT device locations or photo EXIF coordinates.
- Compare address-component parsing across multiple countries.

## Data source

This actor scrapes Google Maps directly. It does not call the Google Maps Geocoding API, so no Google Cloud project, billing account, or API key is required.

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
| 🧭 [Google Maps Directions Scraper](https://apify.com/crawlerbros/google-maps-directions) | A→B routing — distance, duration, traffic, route alternatives for driving/walking/transit |
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

- [Run this actor on Apify](https://apify.com/crawlerbros/google-maps-geocoding)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
