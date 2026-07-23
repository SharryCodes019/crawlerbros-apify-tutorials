# Facebook Search Scraper Tutorial: Run This Apify Actor with Python

Search Facebook for pages and people by keyword. Extract structured data including page/profile details, engagement metrics, and contact information.

This repository shows how to run [Facebook Search Scraper](https://apify.com/crawlerbros/facebook-search-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/facebook-search-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/facebook-search-scraper](https://apify.com/crawlerbros/facebook-search-scraper)
- **SEO title:** Facebook Search Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Search Facebook for pages and people by keyword. Extract structured data including page/profile details, engagement metrics, and contact information.

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

# Facebook Search Scraper

Search Facebook by keyword and extract structured data from pages, posts, or people. Get page details, post content, engagement metrics, and profile information.

## What does Facebook Search Scraper do?

Facebook Search Scraper performs keyword searches on Facebook and extracts structured data from the results. It supports three search types: Pages, Posts, and People.

## Why use Facebook Search Scraper?

- **Lead generation** — Find businesses and pages matching your target keywords
- **Market research** — Discover competitors and industry players on Facebook
- **Content monitoring** — Track posts mentioning specific topics or brands
- **People search** — Find profiles matching specific criteria
- **Location-based discovery** — Search for businesses in specific areas

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| **searchQueries** | Array | Yes | — | Search keywords (e.g., "coffee shop", "dentist") |
| **searchType** | String | No | "pages" | Type of results: "pages", "posts", or "people" |
| **maxResults** | Integer | No | 50 | Maximum results per query (1-500) |

### Input example

```json
{
    "searchQueries": ["coffee shop", "restaurant"],
    "searchType": "pages",
    "maxResults": 20
}
```

## Output

### Pages search output

| Field | Type | Description |
|-------|------|-------------|
| **facebookUrl** | String | Facebook page URL |
| **pageName** | String | Name of the page |
| **pageId** | String | Facebook page ID |
| **category** | String | Page category |
| **description** | String | Page description |
| **followerCount** | Integer | Number of followers |
| **likeCount** | Integer | Number of likes |
| **ratingValue** | String | Page rating (if available) |
| **ratingCount** | Integer | Number of ratings |
| **phone** | String | Contact phone number |
| **email** | String | Contact email |
| **website** | String | External website URL |
| **address** | String | Physical address |
| **profileImageUrl** | String | Profile picture URL |
| **searchQuery** | String | The search query used |
| **scrapedAt** | String | When data was collected |

### Posts search output

| Field | Type | Description |
|-------|------|-------------|
| **postUrl** | String | Direct link to the post |
| **postText** | String | Post content text |
| **authorName** | String | Author name |
| **authorUrl** | String | Author profile URL |
| **likesCount** | Integer | Number of reactions |
| **commentsCount** | Integer | Number of comments |
| **date** | String | Post date (ISO 8601) |
| **searchQuery** | String | The search query used |
| **scrapedAt** | String | When data was collected |

### People search output

| Field | Type | Description |
|-------|------|-------------|
| **profileUrl** | String | Profile URL |
| **profileName** | String | Person's name |
| **profileId** | String | Profile ID |
| **profilePicture** | String | Profile picture URL |
| **subtitle** | String | Profile subtitle/description |
| **searchQuery** | String | The search query used |
| **scrapedAt** | String | When data was collected |

## How many results can I get?

The scraper can extract up to 500 results per search query. The actual number depends on how many results Facebook returns for your search terms.

## Is it legal to search Facebook?

This scraper only accesses publicly available search results that anyone can view without logging in. Always review Facebook's Terms of Service for your use case.

## Frequently Asked Questions

### Do I need a Facebook account?

No. The scraper works without any login credentials and only accesses public data.

### Can I search for specific locations?

Include the location in your search query (e.g., "coffee shop New York" or "dentist Berlin").

### How long does it take?

Typically 1-3 minutes per query depending on the number of results requested.

### Can I export the data?

Yes. Export in JSON, CSV, Excel, XML, HTML and other formats from the Apify platform.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/facebook-search-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
