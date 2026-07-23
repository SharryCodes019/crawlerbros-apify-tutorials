# Facebook Ads Library Scraper Tutorial: Run This Apify Actor with Python

Scrape ads from Facebook Ad Library without cookies or authentication. Search by keywords or page names, filter by country, ad status, ad type, and media type. Extracts ad text, page info, media URLs, dates, CTA, landing page links, and more.

This repository shows how to run [Facebook Ads Library Scraper](https://apify.com/crawlerbros/facebook-ads-library-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/facebook-ads-library-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/facebook-ads-library-scraper](https://apify.com/crawlerbros/facebook-ads-library-scraper)
- **SEO title:** Facebook Ads Library Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape ads from Facebook Ad Library without cookies or authentication. Search by keywords or page names, filter by country, ad status, ad type, and media type. Extracts ad text, page info, media URLs, dates, CTA, landing page links, and more.

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

# Facebook Ads Library Scraper

Scrape ads from the [Facebook Ad Library](https://www.facebook.com/ads/library/) without cookies or authentication.

## Features

- Search by keywords or page names
- Filter by country, ad status, ad type, and media type
- Extracts ad text, page info, media URLs, dates, platforms, and more
- No login or cookies required
- Residential proxy support for best results

## Input

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `searchTerms` | array | Keywords or page names to search | (required) |
| `country` | string | Country code (e.g., "US", "GB") or "ALL" | "ALL" |
| `adActiveStatus` | string | "all", "active", or "inactive" | "active" |
| `adType` | string | "all", "political_and_issue_ads", "housing", "employment", "credit" | "all" |
| `mediaType` | string | "all", "image", "video", "meme", "none" | "all" |
| `resultsPerSearch` | integer | Max ads per search term (1-500) | 50 |
| `proxyConfiguration` | object | Proxy settings (residential recommended) | Apify residential |

## Output

Each ad in the dataset contains:

| Field | Description |
|-------|-------------|
| `ad_id` | Unique Facebook ad archive ID |
| `page_name` | Name of the Facebook page running the ad |
| `page_id` | Facebook page ID |
| `ad_text` | Ad creative text/copy |
| `ad_snapshot_url` | URL to view the ad in Facebook Ad Library |
| `start_date` | When the ad started running |
| `end_date` | When the ad stopped (if inactive) |
| `status` | Active or inactive |
| `platforms` | Platforms where the ad runs (Facebook, Instagram, etc.) |
| `media_type` | Type of media (image, video, none) |
| `media_url` | URL to the ad media |
| `cta_text` | Call-to-action button text |
| `link_url` | Destination URL of the ad |
| `search_term` | The search term that found this ad |
| `scraped_at` | Timestamp when the data was scraped |

## Example Input

```json
{
    "searchTerms": ["nike", "adidas"],
    "country": "US",
    "adActiveStatus": "active",
    "resultsPerSearch": 20
}
```

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/facebook-ads-library-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
