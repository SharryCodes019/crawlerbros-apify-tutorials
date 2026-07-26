# Google Maps Leads Scraper Tutorial: Run This Apify Actor with Python

Scrape business leads from Google Maps. Search by query and extract business name, category, address, phone, website, rating, review count, place ID, and coordinates. Optionally enrich with emails, phone numbers, and social links crawled from each business's website.

This repository shows how to run [Google Maps Leads Scraper](https://apify.com/crawlerbros/google-maps-leads) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-maps-leads`
- **Apify Store:** [https://apify.com/crawlerbros/google-maps-leads](https://apify.com/crawlerbros/google-maps-leads)
- **SEO title:** Google Maps Leads Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape business leads from Google Maps. Search by query and extract business name, category, address, phone, website, rating, review count, place ID, and coordinates. Optionally enrich with emails, phone numbers, and social links crawled from each business's website.

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

# Google Maps Leads Scraper

Extract business leads from Google Maps at scale. Enrich each lead with emails,
phone numbers, and social media links crawled directly from the business website.

## Features

- Search Google Maps by any query ("restaurants in Brooklyn", "dentists Berlin")
- Extract name, category, address, phone, website, rating, reviews, place ID, coordinates
- Optional website crawl: emails, additional phones, Facebook / Instagram / LinkedIn / X / YouTube / TikTok
- Global — works for any country/language via the `language` input

## Input

| Field | Type | Description |
|------|------|-------------|
| `searchQueries` | array | Google Maps queries, e.g. `["coffee shops in Brooklyn"]` |
| `maxPlacesPerSearch` | int | Cap per query (default 20, max 200) |
| `language` | string | Two-letter language code (default `en`) |
| `enrichWithWebsite` | bool | Crawl each business website for contact info (default `true`) |
| `maxPagesPerWebsite` | int | Pages per site when enrichment on (default 3) |

## Output

One dataset record per business with only the fields we could populate:
`title`, `categoryName`, `address`, `phone`, `website`, `totalScore`,
`reviewsCount`, `placeId`, `url`, `location`, `emails`, `websitePhones`,
`socialLinks`, `contactPageUrl`, `scrapedAt`.

## FAQ

**Q: Do I need a proxy?**
A: Not for most searches. The actor retries with Apify Residential automatically
if the first attempt fails.

**Q: Why are some fields missing?**
A: We omit fields we couldn't populate rather than emit `null`. Every field
in your record has real data.

**Q: Does enrichment slow things down?**
A: Website crawl adds ~1-3s per business. Disable `enrichWithWebsite` for a
Maps-only run.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-maps-leads)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
