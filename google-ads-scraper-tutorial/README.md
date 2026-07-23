# Google Ads Scraper Tutorial: Run This Apify Actor with Python

Extract ads from Google Ads Transparency Center. Get text, image and video ad details, advertiser info, dates, and preview URLs.

This repository shows how to run [Google Ads Scraper](https://apify.com/crawlerbros/google-ads-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-ads-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/google-ads-scraper](https://apify.com/crawlerbros/google-ads-scraper)
- **SEO title:** Google Ads Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract ads from Google Ads Transparency Center. Get text, image and video ad details, advertiser info, dates, and preview URLs.

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

# Google Ads Scraper

Extract ads from the **Google Ads Transparency Center** — get text, image, and video ad details along with advertiser info, dates, and preview URLs.

## What is Google Ads Scraper?

A fast and efficient tool that extracts advertising data from the official [Google Ads Transparency Center](https://adstransparency.google.com/). Search by advertiser name, domain, or use direct Transparency Center URLs to collect ad creatives and their details.

## What data can you extract?

**Ad details:**
- Ad format (TEXT, IMAGE, VIDEO)
- Preview URL, image URL, video URL
- First shown and last shown dates
- Creative ID and advertiser ID

**Advertiser info:**
- Advertiser name
- Advertiser ID
- Google Ads Transparency Center URL

## Input

### Start URLs

Provide direct Google Ads Transparency Center advertiser URLs. Navigate to [adstransparency.google.com](https://adstransparency.google.com/), find an advertiser, and copy the URL.

**Example:** `https://adstransparency.google.com/advertiser/AR08888592736429539329?region=ES`

### Search Terms

Alternatively, search by advertiser name or domain:

```json
{
    "searchTerms": ["Google LLC", "nike.com", "Amazon"]
}
```

### Options

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| startUrls | array | — | Direct Transparency Center advertiser URLs |
| searchTerms | array | — | Advertiser names or domains to search |
| region | string | `"anywhere"` | Filter by country (select from dropdown) |
| resultsLimit | integer | `50` | Max ads per advertiser (up to 1000) |
| skipDetails | boolean | `false` | Skip full ad details for faster scraping |

At least one of `startUrls` or `searchTerms` must be provided.

## Output

Each item in the dataset represents one ad:

```json
{
    "advertiserId": "AR08888592736429539329",
    "advertiserName": "Niantic, Inc.",
    "creativeId": "CR08436770543486631937",
    "format": "IMAGE",
    "firstShown": "2023-07-04",
    "lastShown": "2024-05-17",
    "previewUrl": "https://tpc.googlesyndication.com/archive/simgad/12683072185372151324",
    "imageUrl": "https://tpc.googlesyndication.com/archive/simgad/12683072185372151324",
    "videoUrl": null,
    "adLibraryUrl": "https://adstransparency.google.com/advertiser/AR08888592736429539329/creative/CR08436770543486631937",
    "startUrl": "https://adstransparency.google.com/advertiser/AR08888592736429539329?region=ES",
    "searchTerm": null,
    "scrapedAt": "2025-03-16T12:00:00.000000+00:00"
}
```

### Output Fields

| Field | Type | Description |
|-------|------|-------------|
| advertiserId | string | Unique advertiser identifier |
| advertiserName | string | Name of the advertiser |
| creativeId | string | Unique creative/ad identifier |
| format | string | Ad format: TEXT, IMAGE, or VIDEO |
| firstShown | string | Date ad was first shown (YYYY-MM-DD) |
| lastShown | string | Date ad was last shown (YYYY-MM-DD) |
| previewUrl | string | URL to preview the ad creative |
| imageUrl | string | Direct image URL (for IMAGE ads) |
| videoUrl | string | Direct video URL (for VIDEO ads with YouTube-hosted content) |
| adLibraryUrl | string | Direct link to ad in Transparency Center |
| startUrl | string | Input URL that generated this result |
| searchTerm | string | Search term that generated this result |
| scrapedAt | string | ISO 8601 timestamp of when data was scraped |

## How to use

### Option 1: Search by advertiser name

1. Enter advertiser names in the **Search Terms** field
2. Set your desired **Results Limit**
3. Optionally filter by **Region**
4. Click **Save & Start**

### Option 2: Use direct URLs

1. Go to [Google Ads Transparency Center](https://adstransparency.google.com/)
2. Search for an advertiser and select them
3. Copy the browser URL
4. Paste into the **Start URLs** field
5. Click **Save & Start**

### Tips for faster scraping

- Enable **Skip Details** to scrape up to 4x faster (returns less data per ad)
- Use **Results Limit** to control how many ads you need per advertiser
- Process multiple advertisers in a single run by adding multiple search terms or URLs

## Frequently Asked Questions

### What types of ads does this scraper extract?

All ad formats supported by the Google Ads Transparency Center: text ads, image ads, and video ads.

### Can I filter ads by country?

Yes. Use the **Region** dropdown to select a country and see only ads shown in that region.

### What is the difference between Start URLs and Search Terms?

**Start URLs** are direct links to a specific advertiser's page on the Transparency Center. **Search Terms** let you search by advertiser name or domain — the scraper automatically finds the matching advertiser.

### Why are some fields null?

- `imageUrl` is only available for IMAGE format ads with direct image URLs
- `videoUrl` is only available for VIDEO format ads with YouTube-hosted content
- When **Skip Details** is enabled, some fields will be null (only IDs and URLs are returned)

### Is it legal to scrape Google Ads data?

The Google Ads Transparency Center is a public resource. Scraping is legal as long as you comply with applicable laws regarding data collection and usage. Consult legal counsel if unsure about your specific use case.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-ads-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
