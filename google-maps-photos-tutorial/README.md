# Google Maps Photos Scraper Tutorial: Run This Apify Actor with Python

Extract photos from any Google Maps place - carousel scraping with max-resolution URLs, contributor info, and category metadata.

This repository shows how to run [Google Maps Photos Scraper](https://apify.com/crawlerbros/google-maps-photos) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-maps-photos`
- **Apify Store:** [https://apify.com/crawlerbros/google-maps-photos](https://apify.com/crawlerbros/google-maps-photos)
- **SEO title:** Google Maps Photos Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract photos from any Google Maps place - carousel scraping with max-resolution URLs, contributor info, and category metadata.

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

# Google Maps Photos Scraper

Extract every photo from any Google Maps place — including max-resolution image URLs, contributor names, upload dates, captions, and category tabs (Food & Drink, Indoor, Outdoor, Menu, Videos, etc.).

## What It Does

Give this actor a Google Maps place URL and it returns up to 5,000 photos for that place. For each photo you get:

- **Max-resolution photo URL** (full-size, not thumbnail)
- **Photo category** — All Photos, By Owner, By Visitors, Food & Drink, Outdoor, Indoor, Menu, Videos
- **Contributor name** and profile URL (when available)
- **Upload date** as a relative string (e.g. "2 months ago")
- **Original dimensions** + aspect ratio + orientation
- **Caption** and tags (when published by the contributor)
- **Video flag** — distinguishes photos from short clips
- **Business context** — `businessName`, `placeId`, `placeUrl` echoed on every record so the dataset stays joinable

## Use Cases

- Build a visual asset library for restaurants, hotels, and venues
- Track menu / interior photo updates over time
- Source UGC photography for travel and food blogs
- Power "what does this place look like" previews in custom apps
- Enrich lead-generation pipelines with visual context

## Input

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `placeUrl` | String | Yes | — | Google Maps place URL |
| `maxPhotos` | Integer | No | `100` | Maximum number of photos to extract (1–5000) |
| `photoCategory` | Enum | No | `all` | Filter by tab: `all`, `by_owner`, `by_visitors`, `food_and_drink`, `outdoor`, `indoor`, `menu`, `videos` |
| `enrichDetails` | Boolean | No | `true` | Visit each photo individually to capture contributor, date, dimensions, tags. Disable for ~3–5x faster runs that only return thumbnail-level data. |
| `proxyConfiguration` | Object | No | Apify Proxy | Optional proxy settings |

### Example input

```json
{
  "placeUrl": "https://www.google.com/maps/place/Empire+State+Building/@40.7484405,-73.9878584,17z/",
  "maxPhotos": 50,
  "photoCategory": "all",
  "enrichDetails": true
}
```

## Output

One record per photo:

```json
{
  "photoId": "AF1QipP...XYZ",
  "photoUrl": "https://lh3.googleusercontent.com/p/AF1QipP...XYZ=s0",
  "category": "by_visitors",
  "contributorName": "Jane Smith",
  "contributorUrl": "https://maps.google.com/maps/contrib/123...",
  "uploadDate": "2 months ago",
  "caption": "Sunset view from the observation deck",
  "width": 4032,
  "height": 3024,
  "aspectRatio": 1.33,
  "orientation": "landscape",
  "isVideo": false,
  "tags": ["sunset", "view", "observation deck"],
  "businessName": "Empire State Building",
  "placeId": "0x89c259a9b3117469:0xd134e199a405a163",
  "placeUrl": "https://www.google.com/maps/place/Empire+State+Building/...",
  "rank": 1,
  "scrapedAt": "2026-06-16T12:00:00+00:00"
}
```

Empty fields are omitted automatically — no `null` values in the dataset.

## FAQ

**Does it need a proxy or cookies?**
No login or cookies. A proxy is recommended for large runs to avoid rate limiting, and Apify Proxy is enabled by default.

**Which categories does Google show?**
Every place is different. Restaurants typically have Food & Drink + Menu, hotels have Indoor + Outdoor, and landmarks usually have a single "All Photos" tab. Selecting a category that doesn't exist for a place yields the All tab automatically.

**What does `enrichDetails` actually do?**
With enrichment on, the actor walks through every photo (one network request per photo) to capture contributor and upload metadata. With it off, only thumbnail-level fields (photoUrl, category, businessName) are returned — much faster but less detail.

**Are video clips supported?**
Yes — short video clips on Google Maps are included when `photoCategory` is `all` or `videos`, with `isVideo: true` on the record.

**How many photos can I get per place?**
Google Maps caps each photo tab at ~5,000 — the same limit this actor exposes.

## Data Source

Public Google Maps web UI. No Google API key required.

## 🗺️ Complete Google Maps Scraper Suite

This actor is part of a comprehensive Google Maps data extraction toolkit by **crawlerbros**. All actors run on the free Apify plan, use no proxy by default, and return clean, structured data.

| Actor | What it does |
|---|---|
| 🏢 [Google Maps Business Scraper](https://apify.com/crawlerbros/google-maps-scraper) | Extract business data — name, address, phone, website, rating, reviews, hours, amenities |
| ⭐ [Google Maps Reviews Scraper](https://apify.com/crawlerbros/google-maps-reviews-scraper) | Scrape reviews with reviewer Local Guide level, photos, mentioned items, owner replies |
| 🕐 [Google Maps Business Hours Scraper](https://apify.com/crawlerbros/google-maps-business-hours) | Full 7-day hours, timezone, current local time, next open/close, holiday hours |
| 📊 [Google Maps Popular Times Scraper](https://apify.com/crawlerbros/google-maps-popular-times) | Busy hours histogram for all 7 days + current busyness + typical visit time |
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

- [Run this actor on Apify](https://apify.com/crawlerbros/google-maps-photos)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
