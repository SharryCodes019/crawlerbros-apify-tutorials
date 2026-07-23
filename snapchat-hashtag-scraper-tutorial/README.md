# Snapchat Hashtag Scraper Tutorial: Run This Apify Actor with Python

Scrape Snapchat Spotlight videos by hashtag. Extracts video metadata, engagement stats (views, likes, shares, comments), creator info, and download URLs.

This repository shows how to run [Snapchat Hashtag Scraper](https://apify.com/crawlerbros/snapchat-hashtag-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/snapchat-hashtag-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/snapchat-hashtag-scraper](https://apify.com/crawlerbros/snapchat-hashtag-scraper)
- **SEO title:** Snapchat Hashtag Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Snapchat Spotlight videos by hashtag. Extracts video metadata, engagement stats (views, likes, shares, comments), creator info, and download URLs.

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

# Snapchat Hashtag Scraper

Scrape Snapchat Spotlight videos by hashtag. Extracts video metadata, engagement statistics (views, likes, shares, comments), creator info, keywords, and video download URLs from public Snapchat pages.

No login or cookies required. Uses a fast HTTP-only approach.

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| Hashtags | string[] | Yes | - | Hashtags to scrape (with or without #) |
| Results Per Hashtag | integer | No | 30 | Max videos per hashtag (up to 50) |
| Include Video URLs | boolean | No | true | Include direct video download URLs |

### Example Input

```json
{
    "hashtags": ["food", "travel", "fitness"],
    "resultsPerHashtag": 20,
    "includeVideoUrls": true
}
```

## Output

Each result is a flat JSON object representing one Spotlight video:

```json
{
    "snap_id": "W7_EDlXWTBiXAEEniNoMPwAAY...",
    "story_id": "35::3e890222746020bc...",
    "snap_url": "https://www.snapchat.com/spotlight/W7_EDl...",
    "video_url": "https://cf-st.sc-cdn.net/d/...",
    "thumbnail_url": "https://cf-st.sc-cdn.net/d/...",
    "duration_seconds": 10.4,
    "width": 540,
    "height": 960,
    "creator_username": "secretcookshow",
    "creator_display_name": "Secret Cook",
    "creator_profile_url": "https://www.snapchat.com/@secretcookshow",
    "view_count": 3562939,
    "like_count": 12654,
    "share_count": 211,
    "comment_count": 111,
    "remix_count": 0,
    "description": "#asmr #food #cooking",
    "caption": "",
    "keywords": ["easy way to peel pears", "kitchen gadget review"],
    "upload_date": "2026-02-08T12:30:00+00:00",
    "searched_hashtag": "food",
    "scraped_at": "2026-02-20T10:00:00+00:00"
}
```

## Output Fields

| Field | Description |
|-------|-------------|
| snap_id | Unique Snapchat snap identifier |
| story_id | Story identifier |
| snap_url | URL to view the snap on Snapchat |
| video_url | Direct video download URL (watermarked) |
| video_url_unwatermarked | Unwatermarked video URL (when available) |
| thumbnail_url | Video thumbnail image URL |
| duration_seconds | Video duration in seconds |
| width / height | Video dimensions in pixels |
| creator_username | Creator's Snapchat username |
| creator_display_name | Creator's display name |
| creator_profile_url | Link to creator's profile |
| view_count | Number of views |
| like_count | Number of likes/boosts |
| share_count | Number of shares |
| comment_count | Number of comments |
| remix_count | Number of remixes |
| description | Video description text |
| caption | Caption overlay text |
| keywords | Related keywords/tags |
| upload_date | When the video was uploaded (ISO 8601) |
| searched_hashtag | The hashtag used to find this video |
| scraped_at | When the data was scraped (ISO 8601) |

## Tips

- Snapchat returns approximately 24-32 Spotlight videos per hashtag
- Video download URLs contain expiring tokens - download promptly
- Works without proxy, but proxy can help with rate limiting
- Some creators may have empty usernames due to privacy settings

## Limitations

- Maximum ~32 videos per hashtag (server-side rendering limit)
- No pagination support (single page of results)
- Video URLs expire after some time
- Content may vary based on geographic location of the server

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/snapchat-hashtag-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
