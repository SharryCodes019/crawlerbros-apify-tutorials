# Youtube Video Details Scraper Tutorial: Run This Apify Actor with Python

Extract comprehensive details from YouTube videos including metadata, channel information, transcripts, comments, and engagement metrics.

This repository shows how to run [Youtube Video Details Scraper](https://apify.com/crawlerbros/youtube-video-details-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/youtube-video-details-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/youtube-video-details-scraper](https://apify.com/crawlerbros/youtube-video-details-scraper)
- **SEO title:** Youtube Video Details Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract comprehensive details from YouTube videos including metadata, channel information, transcripts, comments, and engagement metrics.

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

# YouTube Video Details Scraper

Scrape comprehensive YouTube video details including metadata, channel info, transcripts, comments, and engagement metrics. HTTP-first approach with automatic Playwright fallback for maximum reliability.

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `videoUrls` | string[] | Yes | - | YouTube video URLs, short links (youtu.be), shorts URLs, or plain video IDs |
| `maxComments` | integer | No | 0 | Max comments to extract per video (0-1000). Set to 0 to skip comments |

### Supported URL formats

- `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- `https://youtu.be/dQw4w9WgXcQ`
- `https://www.youtube.com/shorts/dQw4w9WgXcQ`
- `https://www.youtube.com/embed/dQw4w9WgXcQ`
- `https://www.youtube.com/v/dQw4w9WgXcQ`
- `dQw4w9WgXcQ` (bare video ID)

### Example input

```json
{
  "videoUrls": [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://youtu.be/VIDEO_ID_2"
  ],
  "maxComments": 100
}
```

## Output

Each row in the dataset represents one video with full metadata, channel info, transcript, and optionally comments.

### Video fields

| Field | Type | Example |
|-------|------|---------|
| `type` | string | `"video"` |
| `video_id` | string | `"dQw4w9WgXcQ"` |
| `title` | string | `"Rick Astley - Never Gonna Give You Up"` |
| `description` | string | Full video description |
| `channel_id` | string | `"UCuAXFkgsw1L7xaCfnd5JJOw"` |
| `channel_name` | string | `"Rick Astley"` |
| `published_date` | string | `"2009-10-25"` |
| `duration_seconds` | integer | `212` |
| `views` | integer | `1234567890` |
| `likes` | integer | `15000000` |
| `comment_count` | integer | `500000` |
| `tags` | array | `["rick astley", "never gonna give you up"]` |
| `thumbnails` | object | `{"default": "...", "medium": "...", "high": "..."}` |
| `category` | string | `"Music"` |
| `language` | string | `"en"` |
| `live_status` | string | `"none"`, `"live_now"`, `"was_live"`, or `"upcoming"` |
| `engagement_rate` | float | `0.0162` |
| `hashtags` | array | `["#rickastley", "#nevergonnagiveyouup"]` |
| `upload_type` | string | `"normal"`, `"live"`, `"was_live"`, `"premiere"`, or `"short"` |
| `resolution` | string | `"1080p"` |
| `is_family_safe` | boolean | `true` |
| `available_countries` | array | `["US", "GB", "CA", ...]` |
| `success` | boolean | `true` |
| `scrapedAt` | string | `"2026-02-10T12:00:00.000000+00:00"` |

### Channel info (embedded in `channel` object)

| Field | Type | Example |
|-------|------|---------|
| `id` | string | `"UCuAXFkgsw1L7xaCfnd5JJOw"` |
| `name` | string | `"Rick Astley"` |
| `handle` | string | `"@rickastley"` |
| `url` | string | `"https://www.youtube.com/@rickastley"` |
| `subscriberCount` | integer | `2500000` |
| `subscriberCountText` | string | `"2.5M subscribers"` |
| `logo` | string | Channel avatar URL |
| `badges` | array | `["Verified"]` |

### Transcript (embedded in `transcript` array)

| Field | Type | Example |
|-------|------|---------|
| `start` | string | `"0.000"` |
| `dur` | string | `"3.500"` |
| `text` | string | `"We're no strangers to love"` |

### Comments (embedded in `comments` array, when `maxComments > 0`)

| Field | Type | Example |
|-------|------|---------|
| `commentId` | string | `"abc123"` |
| `text` | string | `"This song is timeless!"` |
| `author` | string | `"MusicFan"` |
| `authorChannelId` | string | `"UC..."` |
| `authorThumbnail` | string | Profile image URL |
| `publishedTime` | string | `"2 years ago"` |
| `likes` | string | `"1.2K"` |
| `isHearted` | boolean | `false` |
| `isPinned` | boolean | `false` |

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/youtube-video-details-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
