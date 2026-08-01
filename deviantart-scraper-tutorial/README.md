# DeviantArt Scraper Tutorial: Run This Apify Actor with Python

Scrape DeviantArt - the world's largest online art community. Search deviations by keyword, browse popular artworks, or scrape a user's gallery.

This repository shows how to run [DeviantArt Scraper](https://apify.com/crawlerbros/deviantart-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/deviantart-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/deviantart-scraper](https://apify.com/crawlerbros/deviantart-scraper)
- **SEO title:** DeviantArt Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape DeviantArt - the world's largest online art community. Search deviations by keyword, browse popular artworks, or scrape a user's gallery.

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

﻿# DeviantArt Scraper

Extract data from [DeviantArt.com](https://www.deviantart.com) — Extract artwork, journals, literature, and user profiles from DeviantArt — the world's largest online social community for artists and art enthusiasts.

## What Does It Do?

This actor scrapes DeviantArt.com to retrieve product listings, artwork details, prices, and metadata.

## Input

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `mode` | Select | search, user, trending | first mode |
| `searchQuery` | String | Search keywords | — |
| `maxItems` | Integer | Maximum items to return (1–500) | 50 |

**Example Input**
```json
{
  "mode": "search",
  "searchQuery": "example query",
  "maxItems": 50
}
```

## Output

Key fields per record: deviationId,title,authorName,category,imageUrl,deviationUrl,publishedAt, `scrapedAt`

## FAQs

**Is this free to use?**  
Yes. This actor accesses only publicly available pages — no account or API key required.

**The actor uses DeviantArt's public RSS feed to bypass login requirements.**

**How often is the data updated?**  
Each run fetches live data. Schedule daily runs for fresh results.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/deviantart-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
