# Flickr Scraper Tutorial: Run This Apify Actor with Python

Scrape Flickr public photo search results - extract photo metadata including title, owner, tags, views, and image URLs. No API key required.

This repository shows how to run [Flickr Scraper](https://apify.com/crawlerbros/flickr-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/flickr-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/flickr-scraper](https://apify.com/crawlerbros/flickr-scraper)
- **SEO title:** Flickr Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Flickr public photo search results - extract photo metadata including title, owner, tags, views, and image URLs. No API key required.

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

# Flickr Scraper

Scrape **Flickr** � Flickr public photos. 

---

## Features

- Browse and search Flickr data
- Filter by photos by keyword and sort order
- Output: `photoId, title, ownerName, tags, views, imageUrl, photoUrl`
- No API key required
- Daily test runs for reliability

---

## Input

| Parameter | Type | Description |
|---|---|---|
| `mode` | select | What to fetch |
| `maxItems` | integer | Maximum records to return (default: 50) |

**Example input:**
```json
{
  "mode": "search",
  "maxItems": 10
}
```

---

## Output

Each record contains: `photoId, title, ownerName, tags, views, imageUrl, photoUrl`

**Example record:**
```json
{
  "recordType": "record",
  "scrapedAt": "2024-01-15T10:30:00+00:00"
}
```

---

## FAQ

**Is this free to use?**
Yes � this actor uses only public APIs and requires no authentication.

**How often is data updated?**
Data is fetched live on every run from Flickr.

**What is the daily test run?**
This actor runs automatically every day to verify it still works correctly.

---

## Data Source

Data is sourced from **Flickr** public API/website.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/flickr-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
