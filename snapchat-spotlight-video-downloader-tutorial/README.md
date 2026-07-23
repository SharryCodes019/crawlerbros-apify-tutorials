# Snapchat Spotlight Video Downloader Tutorial: Run This Apify Actor with Python

Download Snapchat Spotlight videos. Provide one or more Spotlight URLs and get direct CDN video links, thumbnails, captions, creator info, and engagement stats.

This repository shows how to run [Snapchat Spotlight Video Downloader](https://apify.com/crawlerbros/snapchat-spotlight-video-downloader) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/snapchat-spotlight-video-downloader`
- **Apify Store:** [https://apify.com/crawlerbros/snapchat-spotlight-video-downloader](https://apify.com/crawlerbros/snapchat-spotlight-video-downloader)
- **SEO title:** Snapchat Spotlight Video Downloader Tutorial: Run This Apify Actor with Python
- **Description:** Download Snapchat Spotlight videos. Provide one or more Spotlight URLs and get direct CDN video links, thumbnails, captions, creator info, and engagement stats.

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

# Snapchat Spotlight Video Downloader

Extract direct video URLs, engagement stats, AI-generated metadata, transcripts, and comment threads from Snapchat Spotlight posts — no login or cookies required.

Paste one or more Spotlight URLs and get back the CDN video link, thumbnail, creator info, view/like/comment counts, captions, LLM-generated descriptions, WebVTT transcripts, and up to 24 related videos per post. All data comes from public Snapchat pages.

## What You Get

- **Direct CDN video URL** ready to download or embed
- **Full engagement stats** — shares, likes, comments, recommendations
- **AI metadata** — LLM title, description, keywords, detected languages, context cards
- **WebVTT transcript** parsed into timestamped segments
- **Comment threads** with reaction counts and commenter info
- **Up to 24 related Spotlight stories** from the same feed
- No Snapchat account, no cookies, no proxy required

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `spotlightUrls` | string[] | Yes | — | One or more Snapchat Spotlight URLs to process |
| `includeTranscript` | boolean | No | `true` | Parse WebVTT transcript into timestamped segments |
| `includeAiMetadata` | boolean | No | `true` | Include LLM title, description, keywords, context cards, detected languages |
| `includeComments` | boolean | No | `false` | Decode comment threads from the page |
| `includeRelatedStories` | boolean | No | `false` | Include up to 24 related Spotlight stories |
| `proxyConfiguration` | object | No | — | Optional proxy settings |

### Supported URL Formats

```
https://www.snapchat.com/spotlight/{id}
https://www.snapchat.com/@{username}/spotlight/{id}
https://t.snapchat.com/{id}
```

Short links (`t.snapchat.com`) are resolved automatically before scraping.

## Output Fields

### Core Fields (always present on success)

| Field | Type | Description |
|-------|------|-------------|
| `snapId` | string | Unique Spotlight snap identifier |
| `inputUrl` | string | The URL you provided as input |
| `videoUrl` | string | Direct CDN video URL (expires — download promptly) |
| `thumbnailUrl` | string | Thumbnail image URL |
| `caption` | string | Caption or description text on the snap |
| `creatorUsername` | string | Creator's Snapchat username |
| `profileUrl` | string | Full profile URL (`snapchat.com/@username`) |
| `creatorDisplayName` | string | Creator's display name |
| `durationSeconds` | number | Video duration in seconds |
| `uploadedAt` | string | ISO 8601 upload timestamp |
| `scrapedAt` | string | ISO 8601 timestamp of when this record was collected |
| `shareCount` | integer | Number of times the video was shared |
| `commentCount` | integer | Number of comments |
| `likeCount` | integer | Number of likes (boosts) |
| `recommendCount` | integer | Number of recommendations |
| `mediaPreviewUrl` | string | Preview/thumbnail variant URL |
| `width` | integer | Video width in pixels (video snaps only) |
| `height` | integer | Video height in pixels (video snaps only) |
| `restricted` | boolean | Whether the content is age-restricted |
| `isAttributed` | boolean | Whether the snap is attributed to Snapchat's own feed |

> `viewCount` is omitted for very recent videos — Snapchat returns -1 as a sentinel value for posts still accumulating views.

### AI Metadata (when `includeAiMetadata: true`)

| Field | Type | Description |
|-------|------|-------------|
| `llmTitle` | string | LLM-generated title for the video |
| `llmDescription` | string | LLM-generated description of the video content |
| `llmKeywords` | string[] | LLM-generated keyword tags |
| `textMetadataKeywords` | string[] | Text-based keyword tags extracted from metadata |
| `hashtags` | string[] | Hashtags associated with the snap |
| `contextCards` | object[] | Context cards shown on the snap (sound info, creator card, etc.) |
| `detectedLanguages` | object[] | Detected languages with confidence scores (`languageCode`, `score`) |

### Transcript (when `includeTranscript: true`)

| Field | Type | Description |
|-------|------|-------------|
| `transcript` | object[] | Array of `{startTime, endTime, text}` WebVTT segments |
| `transcriptUrl` | string | URL of the raw WebVTT transcript file |

### Comments (when `includeComments: true`)

Each item in `comments[]`:

| Field | Type | Description |
|-------|------|-------------|
| `commentId` | string | Unique comment identifier |
| `snapId` | string | ID of the snap this comment belongs to |
| `replyText` | string | Comment text |
| `reactionCounts` | object[] | Array of `{reactTypeId, count}` reaction tallies |
| `commenterDisplayName` | string | Commenter's display name |
| `approvalState` | any | Moderation approval state |
| `postedAt` | string | ISO 8601 timestamp when the comment was posted |

### Related Stories (when `includeRelatedStories: true`)

Each item in `relatedStories[]`:

| Field | Type | Description |
|-------|------|-------------|
| `thumbnailUrl` | string | Thumbnail URL of the related story |
| `storyPageUrl` | string | Full Spotlight URL of the related story |
| `durationSeconds` | number | Duration of the related story in seconds |
| `creatorUsername` | string | Creator's username |

### Error Records

If a URL fails, an error record is saved instead of a video record:

| Field | Type | Description |
|-------|------|-------------|
| `inputUrl` | string | The URL that failed |
| `snapId` | string | Snap ID if it could be extracted |
| `error` | string | Human-readable error message |
| `scrapedAt` | string | ISO 8601 timestamp |

## Example Input

```json
{
  "spotlightUrls": [
    "https://www.snapchat.com/spotlight/W7_EDlXWTBiXAEEniNoMPwAAYZmRwYmVqcm5wAZ8Kxg_vAZ8Kxgn9AAAAAQ",
    "https://www.snapchat.com/spotlight/W7_EDlXWTBiXAEEniNoMPwAAYZG5iaHJuY2phAZ8KF10GAZ8KETc1AAAAAQ"
  ],
  "includeTranscript": true,
  "includeAiMetadata": true,
  "includeComments": false,
  "includeRelatedStories": false
}
```

## Example Output

```json
{
  "snapId": "W7_EDlXWTBiXAEEniNoMPwAAYZG5iaHJuY2phAZ8KF10GAZ8KETc1AAAAAQ",
  "inputUrl": "https://www.snapchat.com/spotlight/W7_EDlXWTBiXAEEniNoMPwAAYZG5iaHJuY2phAZ8KF10GAZ8KETc1AAAAAQ",
  "videoUrl": "https://bolt-gcdn.sc-cdn.net/v/udlVbjK0wdjHbPx1FRph0.27.IRZXSOY?...",
  "thumbnailUrl": "https://bolt-gcdn.sc-cdn.net/v/udlVbjK0wdjHbPx1FRph0.256.IRZXSOY?...",
  "caption": "Another Spotlight Snap brought to you by Snapchat",
  "creatorUsername": "waqarzaka",
  "profileUrl": "https://www.snapchat.com/@waqarzaka",
  "creatorDisplayName": "Waqar Zaka",
  "durationSeconds": 130.23,
  "width": 540,
  "height": 960,
  "shareCount": 0,
  "likeCount": 3,
  "commentCount": 0,
  "recommendCount": 0,
  "uploadedAt": "2026-06-27T17:12:08.245000+00:00",
  "scrapedAt": "2026-06-28T06:43:34.588497+00:00",
  "isAttributed": true,
  "textMetadataKeywords": ["bitcoin", "hacker", "crypto", "cryptocurrency", "blockchain"],
  "contextCards": [
    {
      "contextType": 3,
      "title": "Waqar Zaka",
      "subtitle": "waqarzaka",
      "url": "https://www.snapchat.com/@waqarzaka",
      "thumbnailType": 0,
      "hasBadge": true,
      "id": "36d0088b-39d5-4765-a237-bb147a292272"
    }
  ],
  "detectedLanguages": [
    { "languageCode": "hi", "score": 0.910262405872345 }
  ]
}
```

## FAQ

**Does this require a Snapchat account or cookies?**
No. All data is extracted from public Snapchat Spotlight pages. No login, no cookies, and no proxy are required in most regions.

**Do video URLs expire?**
Yes. Snapchat CDN URLs include signed tokens that expire after a short period. Download the video as soon as the actor completes — do not store the URL and try to fetch it later.

**Why is `viewCount` missing from some records?**
Snapchat returns -1 as a sentinel for videos that are too new to have an accurate view count. The actor omits this field rather than storing a misleading -1.

**Are `width` and `height` always present?**
Only for video snaps. Some Spotlight posts are images or have incomplete metadata, in which case these fields are absent.

**Can I scrape a large batch of URLs at once?**
Yes. Provide all URLs in the `spotlightUrls` array. The actor processes them sequentially with a short delay between requests to stay respectful of rate limits.

**What is the `isAttributed` flag?**
When `true`, Snapchat itself attributed the snap to its own Discover/Spotlight feed rather than to a specific creator account.

**Can I get comments from all videos?**
Set `includeComments: true`. Comments are decoded from data embedded in the page, so availability depends on what Snapchat includes per snap.

---

## Other Snapchat Scrapers

Explore the full Snapchat scraper suite on Apify:

| Actor | Description |
|-------|-------------|
| [Snapchat Profile Scraper](https://apify.com/crawlerbros/snapchat-profile-scraper) | Full profile metadata, highlights, lenses, and spotlight data |
| [Snapchat Hashtag Scraper](https://apify.com/crawlerbros/snapchat-hashtag-scraper) | Spotlight videos by hashtag or topic with AI metadata |
| [Snapchat User Stories Scraper](https://apify.com/crawlerbros/snapchat-user-stories-scraper) | Curated highlights and active story snaps |
| [Snapchat Spotlight Video Downloader](https://apify.com/crawlerbros/snapchat-spotlight-video-downloader) | Download Spotlight videos with AI metadata, transcripts, and comments |
| [Snapchat Search Scraper](https://apify.com/crawlerbros/snapchat-search-scraper) | Search across videos, lenses, users, places, and shows |
| [Snapchat Lens Scraper](https://apify.com/crawlerbros/snapchat-lens-scraper) | AR lens metadata, trending lenses, and creator info |
| [Snapchat Publisher Scraper](https://apify.com/crawlerbros/snapchat-publisher-scraper) | Discover publisher pages, shows, episodes, and spotlights |
| [Snapchat Ads Gallery Scraper](https://apify.com/crawlerbros/snapchat-ads-gallery-scraper) | EU/UK ad transparency library — ads and sponsored content |
| [Snapchat Spotlight Comments Scraper](https://apify.com/crawlerbros/snapchat-spotlight-comments-scraper) | Comment threads from Spotlight videos |
| [Snapchat Topic Scraper](https://apify.com/crawlerbros/snapchat-topic-scraper) | Spotlight videos by topic with related tags |
| [Snapchat Snapcode Scraper](https://apify.com/crawlerbros/snapchat-snapcode-scraper) | Download Snapcode images (SVG/PNG) for any username |
| [Snapchat Snap Map Scraper](https://apify.com/crawlerbros/snapchat-snap-map-scraper) | Public Snap Map places and their latest snaps |
| [Snapchat Discover Scraper](https://apify.com/crawlerbros/snapchat-discover-scraper) | Shows and stories from Snapchat's Discover feed |

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/snapchat-spotlight-video-downloader)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
