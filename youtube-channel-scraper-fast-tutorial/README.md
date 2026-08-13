# Youtube Channel Scraper Fast Tutorial: Run This Apify Actor with Python

Scrape YouTube channel info and video listings. Get channel metadata, subscriber counts, and complete video catalogs from any YouTube channel.

This repository shows how to run [Youtube Channel Scraper Fast](https://apify.com/crawlerbros/youtube-channel-scraper-fast) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/youtube-channel-scraper-fast`
- **Apify Store:** [https://apify.com/crawlerbros/youtube-channel-scraper-fast](https://apify.com/crawlerbros/youtube-channel-scraper-fast)
- **SEO title:** Youtube Channel Scraper Fast Tutorial: Run This Apify Actor with Python
- **Description:** Scrape YouTube channel info and video listings. Get channel metadata, subscriber counts, and complete video catalogs from any YouTube channel.

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

# YouTube Channel Scraper

Scrape YouTube channel info and video listings. Get channel metadata (subscribers, description, links, verified status) and a complete video catalog from any YouTube channel.

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `channelUrls` | string[] | Yes | - | YouTube channel URLs, handles, or channel IDs |
| `maxVideos` | integer | No | 50 | Max videos per channel (0-2000). Set to 0 for channel info only |
| `sortVideosBy` | string | No | `"newest"` | Sort order: `"newest"`, `"popular"`, or `"oldest"` |

### Supported URL formats

- `@MrBeast` — handle
- `https://www.youtube.com/@MrBeast` — full URL
- `https://www.youtube.com/channel/UCX6OQ3DkcsbYNE6H8uQQuVA` — channel ID URL
- `UCX6OQ3DkcsbYNE6H8uQQuVA` — raw channel ID
- `MrBeast` — plain name (treated as handle)

### Example input

```json
{
  "channelUrls": ["@MrBeast", "@mkbhd"],
  "maxVideos": 100,
  "sortVideosBy": "popular"
}
```

## Output

Every row in the dataset has the same schema. Each row represents a video with an embedded `authorMetadata` object containing full channel details.

When `maxVideos` is set to 0, a single row is returned with video fields set to `null` and `authorMetadata` populated.

### Row fields

| Field | Type | Example |
|-------|------|---------|
| `videoId` | string | `"0e3GPea1Tyg"` |
| `title` | string | `"$456,000 Squid Game In Real Life!"` |
| `url` | string | `"https://www.youtube.com/watch?v=0e3GPea1Tyg"` |
| `viewCount` | integer | `905688793` |
| `viewCountText` | string | `"905,688,793 views"` |
| `publishedTimeText` | string | `"4 years ago"` |
| `duration` | string | `"25:42"` |
| `durationSeconds` | integer | `1542` |
| `thumbnailUrl` | string | URL to video thumbnail |
| `description` | string | Video description snippet |
| `isLive` | boolean | `false` |
| `isShort` | boolean | `false` |
| `authorMetadata` | object | Channel details (see below) |
| `scrapedAt` | string | `"2026-02-10T12:00:00+00:00"` |

### `authorMetadata` fields

| Field | Type | Example |
|-------|------|---------|
| `channelId` | string | `"UCX6OQ3DkcsbYNE6H8uQQuVA"` |
| `channelName` | string | `"MrBeast"` |
| `handle` | string | `"@MrBeast"` |
| `channelUrl` | string | `"https://www.youtube.com/@MrBeast"` |
| `description` | string | `"SUBSCRIBE FOR A COOKIE!..."` |
| `subscriberCount` | integer | `466000000` |
| `subscriberCountText` | string | `"466M subscribers"` |
| `videoCount` | integer | `948` |
| `videoCountText` | string | `"948 videos"` |
| `country` | string | `"US"` |
| `avatarUrl` | string | URL to channel avatar |
| `bannerUrl` | string | URL to channel banner |
| `isVerified` | boolean | `true` |
| `keywords` | array | `["mrbeast", "challenge"]` |
| `channelLinks` | array | `[{"title": "linktr.ee/...", "url": "https://..."}]` |

## Cost

The scraper uses HTTP requests instead of a browser, making it very cost-efficient. A typical run with 50 videos from one channel costs under $0.001 in Apify platform credits (256 MB memory, ~3 seconds).

Larger runs with pagination (e.g., 500+ videos) or multiple channels scale linearly. Browser fallback activates only when HTTP requests are blocked, which increases cost slightly.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/youtube-channel-scraper-fast)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
