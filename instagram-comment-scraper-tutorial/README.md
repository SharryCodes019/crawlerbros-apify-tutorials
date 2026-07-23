# Instagram Comment Scraper Tutorial: Run This Apify Actor with Python

Extract comments from Instagram posts and reels with complete metadata including replies, likes, and author details. Features smart pagination, reply threading, and safe browser automation.

This repository shows how to run [Instagram Comment Scraper](https://apify.com/crawlerbros/instagram-comment-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/instagram-comment-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/instagram-comment-scraper](https://apify.com/crawlerbros/instagram-comment-scraper)
- **SEO title:** Instagram Comment Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract comments from Instagram posts and reels with complete metadata including replies, likes, and author details. Features smart pagination, reply threading, and safe browser automation.

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

# Instagram Comment Scraper

Extract comments from Instagram posts and reels with complete metadata (author, likes, replies, timestamps).

## Features

- **Complete Data**: Extracts text, author info, likes, replies, and timestamps.
- **Reply Threading**: Automatically expands and captures nested replies.
- **Smart Pagination**: Handles "Load More" buttons to get as many comments as possible.
- **Safe & Reliable**: Uses browser automation with built-in rate limiting.

## Setup & Authentication

This scraper requires Instagram cookies to work.

1.  **Get your cookies**:
    *   Log into Instagram.com in your browser.
    *   Open Developer Tools (F12) -> Application -> Cookies.
    *   Copy the cookies for `https://www.instagram.com`.
    *   Format them as a JSON array (or use a browser extension like "EditThisCookie" to export as JSON).

2.  **Provide cookies**:
    *   **Option A (Recommended)**: Paste the JSON array into the `cookies` input field.

## How to Run

### Input Configuration

Example input configuration:

```json
{
  "postUrls": [
    "https://www.instagram.com/p/C4g4BqBPrXx/"
  ],
  "maxCommentsPerPost": 100,
  "includeReplies": true,
  "maxRepliesPerComment": 20
}
```

### Parameters

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `postUrls` | Array | `[]` | List of Instagram post/reel URLs. |
| `maxCommentsPerPost` | Integer | `100` | Max comments to scrape per post. Set to `0` for unlimited. |
| `includeReplies` | Boolean | `true` | Whether to expand and scrape replies. |
| `cookies` | Array | `[]` | Your Instagram cookies (JSON format). |

## Output

The scraper produces a dataset where each item represents a comment:

```json
{
  "comment_id": "1798...",
  "comment_text": "Great post!",
  "author_username": "user123",
  "likes_count": 42,
  "is_reply": false,
  "created_at": "2024-03-20T10:00:00"
}
```

## Troubleshooting

-   **No comments extracted?** Check if your cookies are valid and not expired. Try logging out and back in to refresh them.
-   **"Login required"?** Your cookies might be invalid. Update them.
-   **Missing comments?** For posts with thousands of comments, the scraper extracts the most recent/relevant ones first (typically ~30-50).

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/instagram-comment-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
