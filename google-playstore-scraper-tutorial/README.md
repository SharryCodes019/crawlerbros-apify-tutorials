# Google Play Store Scraper Tutorial: Run This Apify Actor with Python

Scrape Google Play Store app data including ratings, reviews, installs, pricing, developer info, and screenshots. Search by keyword or look up apps by package ID.

This repository shows how to run [Google Play Store Scraper](https://apify.com/crawlerbros/google-playstore-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-playstore-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/google-playstore-scraper](https://apify.com/crawlerbros/google-playstore-scraper)
- **SEO title:** Google Play Store Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Google Play Store app data including ratings, reviews, installs, pricing, developer info, and screenshots. Search by keyword or look up apps by package ID.

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

# Google Play Store Scraper

Extract detailed app data from Google Play Store. Search by keyword or look up specific apps by package ID. Get ratings, reviews, install counts, developer info, screenshots, and 30+ data fields for each app.

## What does Google Play Store Scraper do?

This scraper collects comprehensive data from the Google Play Store. It supports two modes of operation:

- **Search mode** - Enter search keywords (e.g., "calculator", "fitness tracker") to discover and scrape matching apps
- **Direct lookup mode** - Provide specific app package IDs (e.g., "com.whatsapp") to scrape exact apps

For each app, the scraper extracts over 30 data points including ratings, reviews, install counts, pricing, developer contact information, screenshots, and more.

## Features

- Search Google Play Store by keyword
- Look up specific apps by package ID
- Extract 30+ fields per app including all metadata
- Optionally fetch user reviews with ratings and reply data
- Support for any country and language
- No proxy or authentication required
- Lightweight and fast

## Input

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| searchTerms | array | Search keywords to find apps | - |
| appIds | array | Direct app package IDs for lookup | - |
| country | string | Two-letter country code (e.g., "us", "gb", "de") | "us" |
| language | string | Two-letter language code (e.g., "en", "es", "fr") | "en" |
| maxResults | integer | Maximum number of apps to scrape | 50 |
| includeReviews | boolean | Fetch user reviews for each app | false |
| reviewCount | integer | Number of reviews per app (1-200) | 20 |

You must provide at least one search term or app ID.

### Input example

```json
{
    "searchTerms": ["photo editor", "calculator"],
    "country": "us",
    "language": "en",
    "maxResults": 10,
    "includeReviews": true,
    "reviewCount": 5
}
```

### Direct app lookup example

```json
{
    "appIds": ["com.whatsapp", "com.google.android.calculator"],
    "country": "us",
    "language": "en"
}
```

## Output

Each app in the dataset contains the following fields:

| Field | Type | Description |
|-------|------|-------------|
| appId | string | Package ID (e.g., com.whatsapp) |
| title | string | App name |
| url | string | Google Play Store URL |
| developer | string | Developer name |
| developerId | string | Developer ID on Google Play |
| developerEmail | string | Developer contact email |
| developerWebsite | string | Developer website URL |
| developerAddress | string | Developer physical address |
| score | number | Average rating (0-5) |
| ratings | integer | Total number of ratings |
| reviewCount | integer | Total number of reviews |
| histogram | array | Rating distribution [1-star through 5-star counts] |
| installs | string | Install count display text (e.g., "1,000,000+") |
| minInstalls | integer | Minimum install threshold |
| realInstalls | integer | Estimated real install count |
| price | number | App price (0 for free) |
| free | boolean | Whether the app is free |
| currency | string | Price currency code |
| genre | string | App category (e.g., Tools, Games) |
| genreId | string | Genre identifier |
| categories | array | List of categories |
| icon | string | App icon URL |
| headerImage | string | Feature/header image URL |
| screenshots | array | Screenshot image URLs |
| video | string | Promo video URL |
| contentRating | string | Content rating (e.g., Everyone, Teen) |
| adSupported | boolean | Whether app shows ads |
| containsAds | boolean | Marked as containing ads |
| released | string | Original release date |
| lastUpdated | string | Date of last update |
| version | string | Current version number |
| description | string | Full app description |
| recentChanges | string | Latest changelog / what's new |
| privacyPolicy | string | Privacy policy URL |
| reviews | array | User reviews (when includeReviews is enabled) |
| scrapedAt | string | ISO 8601 scrape timestamp |

### Review fields (when includeReviews is enabled)

Each review object contains:

| Field | Type | Description |
|-------|------|-------------|
| reviewId | string | Unique review identifier |
| userName | string | Reviewer's display name |
| userImage | string | Reviewer's profile image URL |
| score | integer | Rating given (1-5) |
| content | string | Review text |
| thumbsUpCount | integer | Number of helpful votes |
| date | string | Date the review was posted |
| replyContent | string | Developer's reply text |
| repliedAt | string | Date of developer's reply |
| appVersion | string | App version the review was written for |

### Output example

```json
{
    "appId": "com.google.android.calculator",
    "title": "Calculator",
    "url": "https://play.google.com/store/apps/details?id=com.google.android.calculator",
    "developer": "Google LLC",
    "developerId": "5700313618786177705",
    "developerEmail": "apps-help@google.com",
    "developerWebsite": "https://support.google.com/calculator",
    "developerAddress": "1600 Amphitheatre Parkway, Mountain View 94043",
    "score": 4.32,
    "ratings": 1234567,
    "reviewCount": 98765,
    "histogram": [50000, 30000, 40000, 150000, 964567],
    "installs": "1,000,000,000+",
    "minInstalls": 1000000000,
    "realInstalls": 1523456789,
    "price": 0,
    "free": true,
    "currency": "USD",
    "genre": "Tools",
    "genreId": "TOOLS",
    "categories": [{"name": "Tools", "id": "TOOLS"}],
    "icon": "https://play-lh.googleusercontent.com/...",
    "headerImage": "https://play-lh.googleusercontent.com/...",
    "screenshots": ["https://play-lh.googleusercontent.com/..."],
    "video": "",
    "contentRating": "Everyone",
    "adSupported": false,
    "containsAds": false,
    "released": "Oct 22, 2014",
    "lastUpdated": "2025-01-15 00:00:00",
    "version": "8.8",
    "description": "A simple calculator app...",
    "recentChanges": "Bug fixes and performance improvements",
    "privacyPolicy": "https://policies.google.com/privacy",
    "reviews": [],
    "scrapedAt": "2025-06-15T12:00:00+00:00"
}
```

## How much does it cost to use Google Play Store Scraper?

This scraper is lightweight and efficient. It uses pure HTTP requests with no browser automation, which keeps costs minimal.

| Apps | Approx. time | Approx. cost |
|------|-------------|-------------|
| 10 apps | ~30 seconds | < $0.01 |
| 50 apps | ~2 minutes | < $0.05 |
| 50 apps + reviews | ~4 minutes | < $0.10 |

No proxy is required, further reducing operational costs.

## Tips and best practices

- **Start small** - Use a low `maxResults` value (5-10) for initial testing before scaling up
- **Country matters** - Some apps are only available in specific countries. Set the `country` field accordingly
- **Reviews add time** - Enabling reviews increases run time. Use `reviewCount` to limit how many reviews per app
- **Combine modes** - You can use both `searchTerms` and `appIds` in the same run
- **Rate limiting** - The scraper automatically manages request pacing to avoid being blocked

## Frequently Asked Questions

### Can I scrape any app on Google Play Store?
Yes, any publicly listed app on Google Play Store can be scraped. Apps that are region-restricted will only appear when using the appropriate country code.

### Do I need a Google account or API key?
No. This scraper works without any authentication, API keys, or cookies.

### Do I need a proxy?
No. The scraper works reliably without a proxy from any IP address.

### How many apps can I scrape in one run?
You can scrape up to 250 apps per run. Each search term returns up to 50 results from Google Play.

### Can I get reviews for all apps?
Yes, enable the `includeReviews` option and set `reviewCount` to the number of reviews you want per app (up to 200).

### What countries and languages are supported?
All countries and languages supported by Google Play Store are available. Use standard two-letter codes (e.g., "us", "gb", "de" for countries; "en", "es", "fr" for languages).

### How often is the data updated?
The scraper fetches live data directly from Google Play Store on each run. Data is always current at the time of scraping.

### Why are some fields empty for certain apps?
Some apps may not have all fields populated on Google Play Store (e.g., no promo video, no developer address). The scraper returns empty strings or empty arrays for unavailable fields.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-playstore-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
