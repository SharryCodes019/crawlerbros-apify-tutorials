# OpenTable + Resy Scraper Tutorial: Run This Apify Actor with Python

Scrape restaurant data from OpenTable and Resy in a single actor. Search by city/cuisine, look up specific restaurants by URL or slug, fetch reviews, and check Resy availability. No login required for either platform.

This repository shows how to run [OpenTable + Resy Scraper](https://apify.com/crawlerbros/opentable-resy-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/opentable-resy-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/opentable-resy-scraper](https://apify.com/crawlerbros/opentable-resy-scraper)
- **SEO title:** OpenTable + Resy Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape restaurant data from OpenTable and Resy in a single actor. Search by city/cuisine, look up specific restaurants by URL or slug, fetch reviews, and check Resy availability. No login required for either platform.

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

# OpenTable + Resy Scraper

A single Apify actor that scrapes restaurant data from both **OpenTable** and **Resy**. Switch between platforms with the `platform` input. Find restaurants by city or cuisine, look up specific venues by URL or slug, and (on Resy) check live reservation availability.

No login required for either platform.

## Features

- **Two platforms in one actor** — `platform` input picks OpenTable or Resy.
- **Five modes per platform**: search, by-restaurant, by-cuisine, by-city, by-URL.
- **Rich record fields** — name, cuisine, price range, neighborhood, address, coordinates, rating, photos, contact info, and full-text reviews (OpenTable detail pages).
- **Resy availability** (optional) — append live reservation slots from Resy's `/4/find` API.
- **Cuisine taxonomy** — 50-entry curated dropdown maps to OpenTable + Resy search terms.
- **Country filter** — drop records outside a target ISO country.
- **Price-range filter** — `$` through `$$$$`, mapped to each platform's price-band IDs.
- **Auto-escalation** — TLS-impersonated `curl_cffi` first; auto-switches to Apify Proxy (datacenter, then residential) on `403` / `429`.

## Sample input

```json
{
  "platform": "opentable",
  "mode": "search",
  "city": "New York",
  "cuisine": "italian",
  "partySize": 2,
  "maxItems": 10
}
```

```json
{
  "platform": "resy",
  "mode": "byRestaurant",
  "urls": ["https://resy.com/cities/ny/venues/carbone"],
  "includeAvailability": true,
  "day": "2026-07-15"
}
```

## Modes

| Mode | OpenTable | Resy |
|---|---|---|
| `search` | `/s/?term=...&metroId=...` — extracts `multiSearch.restaurants[]` from the SSR window-vars JSON. | `POST /3/venuesearch/search` with geo + query. |
| `byRestaurant` / `byUrl` | Detail page `/{slug}` — extracts `restaurantProfile.restaurant` + `reviewsData`. | `GET /3/venue?url_slug=...&location=...` — full venue detail. |
| `byCuisine` | Search with cuisine as the search term. | Search with cuisine as the query. |
| `byCity` | Search with city / metroId only. | Search by geo coordinates. |

## Output (per platform)

Both platforms expose a unified `entityId` (string) for cross-platform joins. The platform-specific `restaurantId` (OpenTable) and `venueId` (Resy) are still emitted alongside `entityId` for backwards compatibility.

### OpenTable

```json
{
  "platform": "opentable",
  "entityId": "96577",
  "restaurantId": "96577",
  "name": "Sistina",
  "url": "https://www.opentable.com/sistina",
  "primaryCuisine": "Italian",
  "priceBand": "$31 to $50",
  "priceBandId": 3,
  "priceLabel": "$$$",
  "currencySymbol": "$",
  "neighborhood": "Upper East Side",
  "address": {"line1": "24 E 81st Street", "city": "New York", "state": "NY", "postCode": "10028", "country": "United States"},
  "coordinates": {"latitude": 40.776, "longitude": -73.962},
  "totalReviews": 1894,
  "overallRating": 4.7,
  "isInstantBookable": true,
  "hasPrivateDining": true,
  "coverImageUrl": "https://resizer.otstatic.com/...",
  "recordType": "restaurant",
  "scrapedAt": "..."
}
```

In `byRestaurant` mode the record additionally includes `recentReviews[]`, `hoursOfOperation[]`, `cuisines[]`, `contact`, `executiveChef`, `dressCode`, `paymentOptions`, `parkingDetails`, etc.

### Resy

```json
{
  "platform": "resy",
  "entityId": "6194",
  "venueId": 6194,
  "name": "Carbone",
  "urlSlug": "carbone",
  "url": "https://resy.com/cities/ny/venues/carbone",
  "cuisine": ["Italian"],
  "neighborhood": "Greenwich Village",
  "priceRangeId": 4,
  "priceLabel": "$$$$",
  "currencySymbol": "$",
  "coordinates": {"latitude": 40.728, "longitude": -74.000},
  "rating": {"average": 4.74, "count": 31498},
  "address": {"line1": "181 Thompson Street", "city": "New York", "state": "NY", "country": "United States", "countryIso": "US"},
  "isGlobalDiningAccess": true,
  "coverImageUrl": "https://image.resy.com/...",
  "recordType": "restaurant",
  "scrapedAt": "..."
}
```

With `includeAvailability=true` (byRestaurant mode), each Resy record gains:

```json
"availability": {
  "day": "2026-07-15",
  "partySize": 2,
  "slotCount": 6,
  "slots": [{"start": "...", "type": "Dining Room", "id": "..."}]
}
```

## High-churn output fields

Some fields evolve rapidly between runs and should be treated as snapshot-in-time:

- **Resy `availability.slots[]` and `availability.slotCount`** — Resy slots change every few minutes as bookings fill up; the same `(venue, day, partySize)` query can return different counts on consecutive runs. Compare across the timestamp captured in `scrapedAt`, not against historical exports.
- **OpenTable `recentReservationCount`** — daily booking counter; rolls over each midnight in the venue's local timezone.
- **`overallRating`, `totalReviews`, Resy `rating.average`/`rating.count`** — providers' aggregate review stats update as new reviews are posted; expect minor drift on each run.
- **`recentReviews[]` (OpenTable)** — most-recent review window changes daily; absent from a run does not mean the venue lost reviews.
- **Photos and `coverImageUrl`** — CDN URLs may rotate; the resource itself is usually stable but the URL string can change.

Stable fields safe for diff/dedup: `restaurantId`/`venueId`, `entityId`, `name`, `url`, `address`, `coordinates`, `priceBand`/`priceRangeId`, `cuisines`/`primaryCuisine`.

## Limitations

- **Resy reviews are not exposed** in the public API — only aggregate rating + count. Use OpenTable for full review text.
- **OpenTable detail URL has two forms**: `/{slug}` (legacy) and `/r/{slug}` (newer). Only one form returns a populated SSR page per restaurant; the actor probes the user-supplied form first, then auto-falls back to the alternate.
- **OpenTable search returns ~50 restaurants per page** — beyond that, paginate by changing `metroId` or `cuisine`.
- **Resy availability requires a `day` parameter** — the actor defaults to 14 days from today; override via the `day` input. Dates farther than 365 days in the future are rejected.
- The Resy widget `api_key` may rotate; the actor harvests a fresh one from `resy.com/modules/app.*.js` at startup if the bundled key fails.

## FAQ

**Do I need login cookies?** No. Both APIs are public, served from datacenter IPs.

**Does it support international markets?** Yes — OpenTable covers 25+ countries (US, CA, UK, France, Germany, Italy, Spain, Australia, Mexico, etc.). Resy covers US, UK, Mexico, Australia, France, and a handful of other markets. Use the `country` filter to scope output.

**Can I scrape both platforms in one run?** Not in a single call — run the actor twice with `platform=opentable` and `platform=resy` and merge the datasets downstream.

**Why does my run keep getting 403?** OpenTable is fronted by Akamai BMP. The actor auto-escalates to Apify Proxy (datacenter, then residential) on 403/429 if `autoEscalateOnBlock=true`.

**Is this legal?** This actor only fetches public, unauthenticated restaurant directory data (names, addresses, cuisines, public reviews) — the same data any visitor sees on the website. No reservations are placed and no user data is collected. You are responsible for complying with each platform's Terms of Service in your jurisdiction.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/opentable-resy-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
