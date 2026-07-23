# GetYourGuide Tours & Activities Scraper Tutorial: Run This Apify Actor with Python

Scrape tours, activities, and experiences from GetYourGuide.com by search query or direct URL. Extracts title, price, rating, reviews, images, highlights, duration, cancellation policy, and more. HTTP-only, no cookies or proxy required.

This repository shows how to run [GetYourGuide Tours & Activities Scraper](https://apify.com/crawlerbros/getyourguide-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/getyourguide-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/getyourguide-scraper](https://apify.com/crawlerbros/getyourguide-scraper)
- **SEO title:** GetYourGuide Tours & Activities Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape tours, activities, and experiences from GetYourGuide.com by search query or direct URL. Extracts title, price, rating, reviews, images, highlights, duration, cancellation policy, and more. HTTP-only, no cookies or proxy required.

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

# GetYourGuide Tours & Activities Scraper

Scrape tours, activities, and experiences from **GetYourGuide.com** by search query or direct URL. Get structured data for cities worldwide — titles, prices, ratings, reviews, images, highlights, durations, cancellation policies, and more. Ideal for travel price monitoring, competitive research, experience aggregation, and affiliate content.

Fast HTTP-only scraper (no cookies, no login) with sensible defaults. Works out of the box without proxy on most regions.

## Features

- Search any city, destination, or activity keyword (e.g. "rome", "paris", "eiffel tower")
- Pass direct GetYourGuide activity, search, or city URLs via `startUrls`
- Extracts 15+ structured fields per activity
- Graceful handling of rate limits via session rotation + exponential backoff
- HTTP-only — fast, cheap, reliable

## Input

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `query` | string | no | Search query (city, destination, or activity). Defaults to `"rome"`. Ignored when `startUrls` are provided. |
| `startUrls` | array of strings | no | Direct GetYourGuide URLs — search pages, activity pages, or city pages. Overrides `query`. |
| `maxItems` | integer | no | Maximum activities to return (1–500). Default `3`. |
| `proxyConfiguration` | object | no | Optional Apify Proxy. GetYourGuide typically works without proxy; enable only if you hit rate limits. |

### Example input

```json
{
    "query": "rome",
    "maxItems": 5
}
```

### Example with startUrls

```json
{
    "startUrls": [
        "https://www.getyourguide.com/rome-l33/rome-colosseum-arena-floor-palatine-forum-guided-tour-t217332/",
        "https://www.getyourguide.com/s/?q=paris"
    ],
    "maxItems": 10
}
```

## Output

Each activity record (`type: "gyg_activity"`) has the following shape:

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | GetYourGuide activity ID. |
| `url` | string | Canonical URL of the activity. |
| `title` | string | Activity title. |
| `shortDescription` | string | Marketing description. |
| `city` | string | City where the activity takes place. |
| `country` | string | Country where the activity takes place. |
| `price` | number | Starting price. |
| `currency` | string | Currency code (e.g. `USD`, `EUR`). |
| `rating` | number | Average star rating (0–5). |
| `reviewCount` | integer | Number of user reviews. |
| `duration` | string | Human-readable duration (e.g. `"2.5 - 3 hours"`). |
| `category` | string | Activity category (e.g. `guidedTour`, `ticket`). |
| `language` | string | Page locale (e.g. `en-US`). |
| `images` | array of strings | Image URLs. |
| `highlights` | array of strings | Bullet-point highlights. |
| `cancellationPolicy` | string | Cancellation policy summary. |
| `scrapedAt` | string | ISO-8601 UTC timestamp. |

### Example output

```json
{
    "type": "gyg_activity",
    "id": "217332",
    "url": "https://www.getyourguide.com/rome-l33/rome-colosseum-arena-floor-palatine-forum-guided-tour-t217332/",
    "title": "Rome: Colosseum Arena Floor, Palatine & Forum Guided Tour",
    "shortDescription": "Experience special access to the Colosseum, Roman Forum, and Palatine Hill on a guided tour...",
    "city": "Rome",
    "country": "Italy",
    "price": 69.26,
    "currency": "USD",
    "rating": 4.51,
    "reviewCount": 21807,
    "duration": "2.5 - 3 hours",
    "category": "guidedTour",
    "language": "en-US",
    "images": ["https://cdn.getyourguide.com/img/tour/..."],
    "highlights": ["Skip the ticket line", "Enter the Colosseum arena floor", "..."],
    "cancellationPolicy": "Free cancellation up to 24 hours before the activity starts for a full refund.",
    "scrapedAt": "2026-04-20T10:30:00Z"
}
```

## Sentinel record

If no activities are returned (rate limit, network issue, empty query), the actor pushes a single sentinel:

```json
{
    "type": "gyg_blocked",
    "reason": "listing_empty_or_blocked",
    "query": "rome",
    "scrapedAt": "2026-04-20T10:30:00Z"
}
```

This keeps daily test runs green without failing the actor.

## FAQs

**Does this scraper need cookies or login?**
No. GetYourGuide search and activity pages are publicly accessible.

**Do I need a proxy?**
Usually no. If you hit rate limits (403/429), enable `proxyConfiguration` in the UI.

**What search queries work?**
Any city, destination, or activity keyword — e.g. `rome`, `paris`, `tokyo`, `new york`, `eiffel tower`, `colosseum`, `skiing`, `food tour paris`.

**How fresh is the data?**
Each run fetches live data at request time — never cached.

**Can I scrape a single activity page?**
Yes — pass its URL in `startUrls`.

**What's the maximum items per run?**
500. GetYourGuide returns ~24 activities per search page; enrichment from detail pages is sequential with polite delays.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/getyourguide-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
