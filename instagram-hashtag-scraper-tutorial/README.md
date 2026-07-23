# Instagram Hashtag Scraper Tutorial: Run This Apify Actor with Python

Extract posts from Instagram hashtags with complete metadata including engagement metrics, captions, media info, and author details. Features smart pagination, anti-block strategies, and multiple scraping approaches.

This repository shows how to run [Instagram Hashtag Scraper](https://apify.com/crawlerbros/instagram-hashtag-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/instagram-hashtag-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/instagram-hashtag-scraper](https://apify.com/crawlerbros/instagram-hashtag-scraper)
- **SEO title:** Instagram Hashtag Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract posts from Instagram hashtags with complete metadata including engagement metrics, captions, media info, and author details. Features smart pagination, anti-block strategies, and multiple scraping approaches.

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

# Instagram Hashtag Scraper

A robust Instagram hashtag scraper built for Apify that extracts posts from Instagram hashtags with complete metadata including engagement metrics, captions, media info, and author details.

## Features

- **Multiple Hashtag Support**: Scrape posts from one or multiple hashtags in a single run
- **Smart Pagination**: Automatically scrolls and loads more content
- **Anti-Block Strategies**:
  - Cookie rotation via MongoDB
  - Smart delays with jitter
  - Human-like behavior simulation
  - Stealth browser configuration
  - Automatic retry with exponential backoff
- **Multiple Data Extraction Methods**:
  - GraphQL API interception
  - Direct API calls
  - HTML parsing with embedded JSON
  - DOM-based fallback extraction
- **Comprehensive Data Output**: Extracts all available post metadata

## Input Parameters

| Parameter                 | Type    | Default           | Description                                    |
| ------------------------- | ------- | ----------------- | ---------------------------------------------- |
| `hashtags`                | array   | required          | List of hashtags to scrape (with or without #) |
| `maxPostsPerHashtag`      | integer | 50                | Maximum posts to extract per hashtag           |
| `scrapeMode`              | string  | "recent"          | "recent", "top", or "both"                     |
| `minDelayBetweenRequests` | integer | 2                 | Minimum delay in seconds                       |
| `maxDelayBetweenRequests` | integer | 5                 | Maximum delay in seconds                       |
| `humanizeBehavior`        | boolean | true              | Enable human-like behavior                     |
| `cookies`                 | string  | null              | Instagram cookies in JSON format               |
| `sessionName`             | string  | "default_session" | Session name for cookie storage                |
| `useGraphQLApi`           | boolean | true              | Try GraphQL API first                          |
| `proxyConfiguration`      | object  | null              | Proxy settings                                 |

## Output Data Structure

Each post in the output dataset contains:

```json
{
  "post_id": "1234567890",
  "shortcode": "ABC123xyz",
  "post_url": "https://www.instagram.com/p/ABC123xyz/",
  "username": "example_user",
  "user_id": "987654321",
  "user_url": "https://www.instagram.com/example_user/",
  "full_name": "Example User",
  "is_verified": false,
  "profile_pic_url": "https://...",
  "caption": "Amazing sunset! #travel #photography",
  "posted_date": "2024-01-15T18:30:00",
  "timestamp": 1705340400,
  "location": "Bali, Indonesia",
  "location_id": "123456",
  "media_type": "image",
  "media_count": 1,
  "thumbnail_url": "https://...",
  "display_url": "https://...",
  "media_urls": ["https://..."],
  "video_url": null,
  "is_video": false,
  "video_view_count": 0,
  "hashtags": ["travel", "photography"],
  "mentions": ["friend_account"],
  "likes_count": 1234,
  "comments_count": 56,
  "is_ad": false,
  "is_carousel": false,
  "search_hashtag": "travel",
  "scraped_at": "2024-01-20T10:00:00",
  "source": "instagram_hashtag_scraper"
}
```

## Cookie Setup

Instagram requires authentication for hashtag scraping. You have several options:

### Option 1: Provide cookies directly in input

1. Install a browser extension like "EditThisCookie" or "Cookie-Editor"
2. Log into Instagram in your browser
3. Export the cookies as JSON
4. Paste the JSON string in the `cookies` input field

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/instagram-hashtag-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
