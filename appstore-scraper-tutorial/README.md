# App Store Scraper Tutorial: Run This Apify Actor with Python

Scrape Apple App Store search results and app details using the public iTunes API. Extract app name, rating, reviews, price, developer info, screenshots, and more.

This repository shows how to run [App Store Scraper](https://apify.com/crawlerbros/appstore-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/appstore-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/appstore-scraper](https://apify.com/crawlerbros/appstore-scraper)
- **SEO title:** App Store Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Apple App Store search results and app details using the public iTunes API. Extract app name, rating, reviews, price, developer info, screenshots, and more.

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

# App Store Scraper

Scrape Apple App Store search results and app details at scale. Extract comprehensive app data including name, rating, reviews, price, developer info, screenshots, and more using the public iTunes Search API.

## What does App Store Scraper do?

App Store Scraper lets you extract structured data from the Apple App Store without any authentication, proxies, or browser automation. It uses Apple's official public iTunes Search API to retrieve app metadata quickly and reliably.

Use it to:

- **Search for apps** by keyword and get detailed results
- **Look up specific apps** by their App Store ID
- **Monitor competitors** by tracking ratings, reviews, and pricing
- **Analyze app categories** and market trends
- **Track app updates** and version history

## Input

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `searchTerms` | Array of strings | Keywords to search for on the App Store | `[]` |
| `appIds` | Array of strings | Specific App Store IDs to look up (e.g., `"544007664"` for YouTube) | `[]` |
| `country` | String | Two-letter ISO country code (e.g., `us`, `gb`, `de`, `jp`) | `"us"` |
| `maxResults` | Integer | Maximum number of apps to return (1-200) | `50` |

You must provide at least one of `searchTerms` or `appIds`.

### Input example

```json
{
  "searchTerms": ["photo editor", "fitness tracker"],
  "appIds": ["544007664"],
  "country": "us",
  "maxResults": 50
}
```

## Output

Each app in the output dataset contains the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `appId` | String | Unique Apple App Store ID |
| `name` | String | App name |
| `url` | String | Direct App Store URL |
| `developer` | String | Developer or seller name |
| `developerId` | String | Developer's Apple artist ID |
| `developerUrl` | String | Developer's App Store page URL |
| `developerWebsite` | String | Developer's external website |
| `price` | Number | Price in local currency (0 for free apps) |
| `formattedPrice` | String | Human-readable price (e.g., "Free", "$4.99") |
| `currency` | String | Currency code (USD, EUR, GBP, etc.) |
| `rating` | Number | Average user rating across all versions (0-5) |
| `ratingCount` | Integer | Total number of user ratings |
| `currentVersionRating` | Number | Average rating for current version |
| `currentVersionRatingCount` | Integer | Number of ratings for current version |
| `description` | String | Full app description |
| `releaseNotes` | String | Latest version release notes |
| `version` | String | Current version number |
| `releaseDate` | String | Original release date (ISO 8601) |
| `lastUpdated` | String | Latest version release date (ISO 8601) |
| `category` | String | Primary genre/category |
| `genres` | Array | All genres/categories |
| `contentRating` | String | Age rating (e.g., "4+", "12+", "17+") |
| `bundleId` | String | App bundle identifier |
| `minimumOs` | String | Minimum required iOS version |
| `fileSize` | String | File size in bytes |
| `icon` | String | App icon URL |
| `screenshots` | Array | iPhone screenshot URLs |
| `ipadScreenshots` | Array | iPad screenshot URLs |
| `languages` | Array | Supported language codes |
| `scrapedAt` | String | Scraping timestamp (ISO 8601) |

### Output example

```json
{
  "appId": "544007664",
  "name": "YouTube: Watch, Listen, Stream",
  "url": "https://apps.apple.com/us/app/youtube-watch-listen-stream/id544007664",
  "developer": "Google LLC",
  "developerId": "544007664",
  "developerUrl": "https://apps.apple.com/us/developer/google-llc/id281956209",
  "developerWebsite": "https://www.youtube.com/",
  "price": 0,
  "formattedPrice": "Free",
  "currency": "USD",
  "rating": 4.69,
  "ratingCount": 16853204,
  "currentVersionRating": 4.69,
  "currentVersionRatingCount": 16853204,
  "description": "Watch your favorite videos, music and more...",
  "releaseNotes": "Bug fixes and stability improvements.",
  "version": "19.50.2",
  "releaseDate": "2012-09-11T07:00:00Z",
  "lastUpdated": "2024-12-16T08:00:00Z",
  "category": "Photo & Video",
  "genres": ["Photo & Video", "Entertainment"],
  "contentRating": "17+",
  "bundleId": "com.google.ios.youtube",
  "minimumOs": "16.0",
  "fileSize": "290816000",
  "icon": "https://is1-ssl.mzstatic.com/image/thumb/...",
  "screenshots": ["https://is1-ssl.mzstatic.com/image/..."],
  "ipadScreenshots": ["https://is1-ssl.mzstatic.com/image/..."],
  "languages": ["EN", "ES", "FR", "DE", "JA"],
  "scrapedAt": "2024-12-20T10:30:00.000000+00:00"
}
```

## How much does it cost to use App Store Scraper?

This scraper uses Apple's free public iTunes Search API, which requires:

- **No proxy** - Direct API calls without any proxy costs
- **No browser** - Pure HTTP requests, minimal compute usage
- **No authentication** - No cookies or login required

The cost is determined only by Apify platform compute units, which are minimal since this actor uses lightweight HTTP requests only.

## Supported countries

The scraper supports all App Store regions. Use the standard two-letter ISO 3166-1 alpha-2 country codes:

| Code | Country | Code | Country |
|------|---------|------|---------|
| `us` | United States | `gb` | United Kingdom |
| `ca` | Canada | `au` | Australia |
| `de` | Germany | `fr` | France |
| `jp` | Japan | `kr` | South Korea |
| `cn` | China | `in` | India |
| `br` | Brazil | `mx` | Mexico |

And many more. See the full list of [ISO 3166-1 alpha-2 codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

## Tips and limitations

- The iTunes Search API returns a maximum of 200 results per search term. Use multiple specific search terms for broader coverage.
- Some fields like `developerWebsite` or `releaseNotes` may be empty if the developer hasn't provided them.
- Results may vary by country due to regional app availability and localization.
- A 3-second delay is applied between API calls to respect rate limits.
- Duplicate apps across multiple search terms are automatically deduplicated.

## FAQ

**Can I scrape any app from the App Store?**
Yes, any app publicly listed on the App Store can be scraped. You can search by keyword or look up specific apps by their App Store ID.

**Where do I find an app's App Store ID?**
Open the app in a browser at `apps.apple.com`. The numeric ID is in the URL, e.g., `https://apps.apple.com/us/app/youtube/id544007664` -- the ID is `544007664`.

**How often is the data updated?**
The iTunes API returns real-time data from Apple's servers. Ratings, prices, and other metadata reflect the current state of the App Store.

**Can I get user reviews?**
This scraper focuses on app metadata (ratings, descriptions, pricing). Individual user reviews are not available through the iTunes Search API.

**Is there a rate limit?**
Apple's iTunes API has undocumented rate limits. This scraper includes built-in delays (3 seconds between requests) to stay within safe limits.

**Can I use this for market research?**
Absolutely. The structured output is ideal for competitive analysis, market sizing, pricing research, and tracking app category trends.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/appstore-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
