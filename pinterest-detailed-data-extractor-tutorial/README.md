# Pinterest Detailed Data Extractor Tutorial: Run This Apify Actor with Python

Scrape Pinterest pins, profiles, boards, search results, and comments. Extract images, videos, metadata, and engagement stats using Pinterest's internal API.

This repository shows how to run [Pinterest Detailed Data Extractor](https://apify.com/crawlerbros/pinterest-detailed-data-extractor) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/pinterest-detailed-data-extractor`
- **Apify Store:** [https://apify.com/crawlerbros/pinterest-detailed-data-extractor](https://apify.com/crawlerbros/pinterest-detailed-data-extractor)
- **SEO title:** Pinterest Detailed Data Extractor Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Pinterest pins, profiles, boards, search results, and comments. Extract images, videos, metadata, and engagement stats using Pinterest's internal API.

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

# Pinterest Data Extractor

Scrape Pinterest pins, profiles, boards, and search results. Extract images, videos, metadata, and engagement stats.

## What it does

This actor extracts data from Pinterest by keyword search or direct URLs. It supports:

- **Search** - Find pins by keyword
- **Pin URLs** - Get detailed data for specific pins
- **Profile URLs** - Get user info and their pins
- **Board URLs** - Get all pins from a board

## Input

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `search` | string | Keyword to search on Pinterest | - |
| `startUrls` | array | List of Pinterest URLs to scrape | - |
| `maxItems` | integer | Maximum number of items to scrape (0 = unlimited) | 50 |
| `endPage` | integer | Maximum pages to paginate (0 = unlimited) | 0 |
| `proxy` | object | Proxy configuration | Apify Proxy |

At least one of `search` or `startUrls` must be provided.

### Supported URL formats

- `https://www.pinterest.com/pin/123456/` - Single pin
- `https://www.pinterest.com/username/` - User profile + pins
- `https://www.pinterest.com/username/board-name/` - Board pins
- `https://www.pinterest.com/search/pins/?q=query` - Search results

### Example input

```json
{
    "search": "minimalist interior design",
    "maxItems": 50,
    "proxy": { "useApifyProxy": true }
}
```

```json
{
    "startUrls": [
        "https://www.pinterest.com/pin/292452569572809169/",
        "https://www.pinterest.com/welovehomeblog/",
        "https://www.pinterest.com/welovehomeblog/interior-design-ideas/"
    ],
    "maxItems": 100,
    "proxy": { "useApifyProxy": true }
}
```

## Output

### Pin data

Each pin includes the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Pin ID |
| `url` | string | Pinterest pin URL |
| `title` | string | Pin title |
| `description` | string | Pin description |
| `created_at` | string | Creation timestamp |
| `images` | object | Image URLs at multiple resolutions (236x, 474x, 736x, orig) |
| `dominant_color` | string | Dominant hex color of the image |
| `link` | string | Source/destination URL |
| `pinner_id` | string | Creator's user ID |
| `pinner_username` | string | Creator's username |
| `pinner_name` | string | Creator's display name |
| `pinner_followers` | integer | Creator's follower count |
| `board_id` | string | Board ID |
| `board_name` | string | Board name |
| `board_url` | string | Board URL |
| `save_count` | integer | Number of saves/repins |
| `comment_count` | integer | Number of comments |
| `is_video` | boolean | Whether the pin is a video |
| `video_url` | string | Video URL (HLS stream) if applicable |

### User profile data

When scraping a profile URL, the first item in the dataset is the user's profile:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Always `"user"` |
| `id` | string | User ID |
| `username` | string | Username |
| `full_name` | string | Display name |
| `bio` | string | Profile bio |
| `follower_count` | integer | Number of followers |
| `following_count` | integer | Number of accounts followed |
| `pin_count` | integer | Total pins |
| `board_count` | integer | Total boards |
| `image_url` | string | Profile image URL |
| `website_url` | string | Website URL |
| `is_verified` | boolean | Verified merchant status |
| `profile_url` | string | Pinterest profile URL |

### Example output

```json
{
    "id": "292452569572809169",
    "url": "https://www.pinterest.com/pin/292452569572809169/",
    "title": "",
    "description": "THIS MAKES ME CRY...",
    "created_at": "Mon, 03 Nov 2025 07:46:12 +0000",
    "images": {
        "170x": "https://i.pinimg.com/236x/0b/d6/e9/0bd6e9...jpg",
        "236x": "https://i.pinimg.com/236x/0b/d6/e9/0bd6e9...jpg",
        "474x": "https://i.pinimg.com/474x/0b/d6/e9/0bd6e9...jpg",
        "736x": "https://i.pinimg.com/736x/0b/d6/e9/0bd6e9...jpg",
        "orig": "https://i.pinimg.com/originals/0b/d6/e9/0bd6e9...jpg"
    },
    "dominant_color": "#6c5d56",
    "link": "https://www.instagram.com/reel/DMPX6u3pAN0/",
    "pinner_id": "292452706960849245",
    "pinner_username": "dalilacristina1",
    "pinner_name": "Dalila Cristina",
    "pinner_followers": 11,
    "board_id": "292452638242391545",
    "board_name": "Devocional 2025",
    "board_url": "https://www.pinterest.com/dalilacristina1/devocional-2025/",
    "save_count": 316,
    "comment_count": 0,
    "is_video": true,
    "video_url": "https://v1.pinimg.com/videos/iht/hls/8f/03/99/8f0399...m3u8"
}
```

## Limitations

- Board scraping extracts the initial set of pins from the page (~15-25 pins). Full board pagination requires authentication.
- Pin detail pages may not include the pinner's display name (relay response limitation).
- No login/cookie support — only public data is accessible.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/pinterest-detailed-data-extractor)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
