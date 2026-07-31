# AllTrails Scraper Tutorial: Run This Apify Actor with Python

Scrape AllTrails, the world's largest hiking, biking, and running trail database. Search trails by keyword/location; fetch full trail detail (difficulty, distance, elevation, GPS coordinates, photos, recent reviews); browse trails by park, city, or country.

This repository shows how to run [AllTrails Scraper](https://apify.com/crawlerbros/alltrails-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/alltrails-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/alltrails-scraper](https://apify.com/crawlerbros/alltrails-scraper)
- **SEO title:** AllTrails Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape AllTrails, the world's largest hiking, biking, and running trail database. Search trails by keyword/location; fetch full trail detail (difficulty, distance, elevation, GPS coordinates, photos, recent reviews); browse trails by park, city, or country.

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

# AllTrails Scraper

Scrape **AllTrails** — the world's largest hiking, biking, and running trail database — for trail detail, location-based browse, or keyword search. Returns full structured data including difficulty, distance, elevation profile, GPS coordinates, photos, ratings, and recent reviews.

## What this actor extracts

For every emitted trail record:

- `name`, `slug`, `url`, `trailId`, `mapId`
- `overview` — long-form trail description
- Geometry: `lengthMeters`, `lengthKm`, `lengthMiles`, `elevationGainMeters`, `elevationGainFeet`, `elevationStartMeters`, `elevationMaxMeters`
- Difficulty: `difficulty` (`easy`/`moderate`/`hard`), `difficultyScore` (1-7)
- `routeType` (`out_and_back`/`loop`/`point_to_point`)
- Location: `latitude`, `longitude`, `city`, `state`, `stateCode`, `country`, `countryCode`, `areaName`, `areaSlug`
- Ratings: `avgRating`, `reviewCount`, `ratingsBreakdown` (per-star counts), `popularity`, `visitorUsage`
- Counts: `photoCount`, `trackCount`, `completedCount`
- `activities[]` — primary activity slugs (hiking, mountain-biking, etc.)
- `features[]` — trail attributes (Forests, Rivers, Views, Waterfalls, etc.)
- `seasonStartMonth`, `seasonEndMonth`
- `coverPhoto` — `{id, url, title, username}` and top-level `coverUrl`
- `recentReviews[]` — recent review excerpts (rating, author, text, date) when available from the trail page

## Modes

| Mode                  | Input                                                  | Output |
|-----------------------|--------------------------------------------------------|--------|
| `byTrail`             | `url` or `country` + `state` + `trailSlug`             | One full trail record |
| `byUrl`               | `url` or `urls[]` — any alltrails.com URL              | Auto-routed (trail/park/city/country/search) |
| `searchTrails`        | `query` + optional `country`                           | Trails matching the query (Algolia API) |
| `byPark`              | `url` or `country` + `state` + `parkSlug`              | Trails inside a park (with detail) |
| `byCity`              | `url` or `country` + `state` + `city`                  | Popular trails near a city |
| `topTrailsByCountry`  | `url` or `country`                                     | Curated trail list for a country page |

## Filters

| Filter           | Description |
|------------------|-------------|
| `difficulty`     | `easy` / `moderate` / `hard` |
| `routeType`      | `out_and_back` / `loop` / `point_to_point` |
| `activity`       | One of 23 activity slugs (hiking, mountain-biking, …) |
| `minRating`      | Drop trails below this avgRating (0-5) |
| `minLengthKm`    | Drop trails shorter than this (km) |
| `maxLengthKm`    | Drop trails longer than this (km) |
| `maxItems`       | Hard cap on emitted records (1-1000) |

## Reliability

- HTTP-first via `curl_cffi` with **Safari iOS** TLS fingerprint (this is the only impersonation that bypasses AllTrails' Cloudflare-edge filter — Chrome/Firefox impersonations get 403'd).
- Auto-escalates to **Apify residential proxy** on 403 / 429 / Cloudflare-challenge if `autoEscalateOnBlock=true` (default).
- Retries with exponential backoff up to 4 attempts.
- Algolia search uses AllTrails' public client-facing keys — no auth gymnastics required.

## Multi-country support

The `country` enum exposes 48 of the most-trafficked AllTrails country slugs. Search uses the matching localized Algolia index when one exists (e.g. `germany` → `alltrails_primary_de-DE`). For all other countries, the global English index is used.

## FAQ

**Do I need an account or login?**
No. AllTrails' trail pages, park pages, country pages, and search index are all publicly accessible.

**Why is `recentReviews` shorter than `reviewCount`?**
AllTrails' trail page only embeds the most-recent ~5-10 reviews server-side; the rest are loaded client-side via API. To pull large review sets, use the `byTrail` mode with the canonical URL — the actor returns whatever the page exposes.

**Are GPX track files included?**
No — the actor focuses on trail metadata. GPX/KML downloads are paywalled by AllTrails.

**Do I get photos?**
Yes — the cover photo URL is included as `coverUrl`. AllTrails CDN images are publicly accessible without referer headers.

**Can I scrape user profiles or saved lists?**
Not in v1 — those routes are mostly login-walled.

## Limitations

- AllTrails Pro-only fields (downloadable maps, real-time conditions API) are not exposed.
- Search results sometimes return `area` records (parks/regions) before trails; we filter to `type=trail` only.
- A handful of country slugs return 403 from datacenter IPs — auto-escalation kicks in transparently.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/alltrails-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
