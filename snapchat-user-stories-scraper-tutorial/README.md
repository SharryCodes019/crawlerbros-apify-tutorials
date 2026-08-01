# Snapchat User Stories Scraper Tutorial: Run This Apify Actor with Python

Scrape curated highlight stories from public Snapchat profiles. Provide usernames or profile URLs and get direct media URLs, thumbnails, story titles, and creator metadata with one record per snap.

This repository shows how to run [Snapchat User Stories Scraper](https://apify.com/crawlerbros/snapchat-user-stories-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/snapchat-user-stories-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/snapchat-user-stories-scraper](https://apify.com/crawlerbros/snapchat-user-stories-scraper)
- **SEO title:** Snapchat User Stories Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape curated highlight stories from public Snapchat profiles. Provide usernames or profile URLs and get direct media URLs, thumbnails, story titles, and creator metadata with one record per snap.

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

# Snapchat User Stories Scraper

Extract individual snaps from Snapchat users' curated highlight albums and active public stories — no login, no cookies, no API key required. Provide any username or profile URL and get direct media URLs, story titles, post timestamps, geolocation, and full creator metadata, one flat record per snap.

Ideal for content archiving, influencer monitoring, media research, brand tracking, and social media analytics.

---

## What You Get

- Individual snap records from saved highlight albums (permanent, creator-curated content)
- Individual snap records from active public stories (ephemeral, refreshes every 24 hours)
- Direct media URLs (video and image) ready for download
- Preview image URLs for each snap
- Post timestamps, geolocation coordinates, and sponsorship flags
- Creator metadata merged into every record: display name, subscriber count, bio, profile picture
- Clear `storySource` field on every record indicating whether it came from a highlight or live story
- Works on all public Snapchat profiles — no account or session required

---

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `usernames` | string[] | Yes | — | Snapchat usernames or profile URLs. Accepts: bare username (`djkhaled`), `@djkhaled`, `https://www.snapchat.com/add/djkhaled`, or `https://www.snapchat.com/@djkhaled` |
| `maxSnapsPerUser` | integer | No | `50` | Maximum number of snaps to extract per user across all selected sources (1–500) |
| `sources` | string[] | No | `["curatedHighlights", "activeStory"]` | Which story sources to extract. `curatedHighlights` = saved highlight albums; `activeStory` = current ephemeral public story |
| `proxyConfiguration` | object | No | — | Apify proxy settings. Public profiles work without proxy; use for resilience at scale |

### Example Input

```json
{
  "usernames": ["djkhaled", "khaby.lame", "https://www.snapchat.com/@brentrivera"],
  "maxSnapsPerUser": 50,
  "sources": ["curatedHighlights", "activeStory"]
}
```

---

## Output

One record is produced per snap. Creator metadata is merged into every record so the dataset is self-contained and ready for analysis without joining.

### Per-Snap Output Fields

| Field | Type | Description |
|-------|------|-------------|
| `username` | string | Creator's Snapchat username |
| `displayName` | string | Creator's display name |
| `isVerified` | boolean | Whether the creator has a verification badge |
| `subscriberCount` | integer | Creator's total subscriber / follower count |
| `bio` | string | Creator's profile bio text |
| `profileUrl` | string | Creator's full Snapchat profile URL |
| `profilePictureUrl` | string | Creator's profile picture URL |
| `storySource` | string | `"curatedHighlight"` or `"activeStory"` — indicates the origin of this snap |
| `highlightId` | string | ID of the highlight album or story this snap belongs to |
| `storyTitle` | string | Title of the highlight album or story |
| `highlightThumbnailUrl` | string | Thumbnail image URL for the parent highlight or story |
| `snapIndex` | integer | Position of this snap within its highlight or story (0-based) |
| `snapId` | string | Unique snap ID (may be absent for some curated highlights) |
| `mediaUrl` | string | Direct media URL — video or image file ready for download |
| `mediaPreviewUrl` | string | Low-resolution preview image URL |
| `mediaType` | string | `"video"` or `"image"` |
| `postedAt` | string | Snap post timestamp (ISO 8601 UTC) |
| `snapTitle` | string | Snap title or caption text |
| `snapSubtitles` | array | Subtitle/caption objects overlaid on the snap |
| `lat` | number | Latitude coordinate (if the snap is geotagged) |
| `lng` | number | Longitude coordinate (if the snap is geotagged) |
| `hasAttachment` | boolean | Whether the snap has an external link attachment |
| `audioTranscriptionObjectUrl` | string | URL to an audio transcription file (sparse) |
| `isSponsored` | boolean | Whether the snap is marked as sponsored content |
| `scrapedAt` | string | Scrape timestamp (ISO 8601 UTC) |

### Active Story Extras

When `storySource` is `"activeStory"`, the following additional story-level fields may appear if present on the profile:

| Field | Type | Description |
|-------|------|-------------|
| `storySubtitle` | string | Story subtitle text |
| `storyShareId` | string | Share ID for the story |
| `emoji` | string | Story emoji indicator |
| `storyTapId` | string | Internal tap ID |
| `canonicalUrlSuffix` | string | Canonical URL suffix for the story |
| `videoTrackUrl` | string | URL to the video track manifest |
| `isAttributed` | boolean | Whether the story is attributed to an event or campaign |

### Error Records

When a username cannot be fetched or has no public content, an error record is pushed instead of crashing the run.

| Field | Type | Description |
|-------|------|-------------|
| `inputUsername` | string | The original input value that failed |
| `error` | string | Human-readable error description |
| `scrapedAt` | string | Timestamp of the failed attempt (ISO 8601 UTC) |

---

## Example Output

```json
{
  "username": "djkhaled",
  "displayName": "DJ Khaled",
  "isVerified": true,
  "subscriberCount": 8500000,
  "bio": "Father, DJ, producer, mogul, lover of life.",
  "profileUrl": "https://www.snapchat.com/@djkhaled",
  "profilePictureUrl": "https://cf-st.sc-cdn.net/img/dr/djkhaled.jpg",
  "storySource": "curatedHighlight",
  "highlightId": "hl-abc123",
  "storyTitle": "Behind The Scenes",
  "highlightThumbnailUrl": "https://cf-st.sc-cdn.net/thumb/bts.jpg",
  "snapIndex": 0,
  "snapId": "snap-001xyz",
  "mediaUrl": "https://cf-st.sc-cdn.net/video/bts_snap1.mp4",
  "mediaPreviewUrl": "https://cf-st.sc-cdn.net/preview/bts_snap1.jpg",
  "mediaType": "video",
  "postedAt": "2026-06-20T16:45:00+00:00",
  "snapTitle": "Studio session with the squad",
  "hasAttachment": false,
  "isSponsored": false,
  "scrapedAt": "2026-06-28T12:00:00+00:00"
}
```

---

## FAQ

**Do I need a Snapchat account or cookies?**
No. The scraper accesses only public Snapchat profile pages using standard HTTP requests. No login or session cookies are needed.

**What is the difference between `curatedHighlights` and `activeStory`?**
Curated highlights are permanent story albums that creators manually save and organise — they persist indefinitely. Active stories are ephemeral 24-hour public stories that change frequently. Both sources are selected by default; use the `sources` field to restrict to one or the other.

**How do I know which source each snap came from?**
Every record has a `storySource` field set to either `"curatedHighlight"` or `"activeStory"`. This makes it straightforward to filter or group by source in your downstream pipeline.

**What happens if a profile has no public content?**
If a profile is private, has no highlights, and has no active story, the scraper pushes an error record with a descriptive message and moves on to the next username. The run does not fail.

**How many snaps can I get per user?**
`maxSnapsPerUser` caps the total across both sources combined. The default is 50 and the maximum is 500. Snaps from `curatedHighlights` are counted first, then `activeStory` snaps fill the remainder up to the cap.

**Are media URLs permanent?**
Highlight media URLs are generally stable for weeks or months. Active story URLs contain short-lived CDN tokens that expire within hours. Download media promptly if you need to preserve active story content.

**Can I scrape only curated highlights or only active stories?**
Yes. Set `sources` to `["curatedHighlights"]` to skip active stories entirely, or `["activeStory"]` to skip highlights. Both are included by default.

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

- [Run this actor on Apify](https://apify.com/crawlerbros/snapchat-user-stories-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
