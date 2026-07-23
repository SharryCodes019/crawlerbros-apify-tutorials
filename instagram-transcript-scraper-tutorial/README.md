# Instagram Transcript Scraper Tutorial: Run This Apify Actor with Python

Extract transcripts from Instagram videos and reels using auto-generated captions or AI-powered speech-to-text. Returns clean, timestamped transcript segments with full video metadata.

This repository shows how to run [Instagram Transcript Scraper](https://apify.com/crawlerbros/instagram-transcript-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/instagram-transcript-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/instagram-transcript-scraper](https://apify.com/crawlerbros/instagram-transcript-scraper)
- **SEO title:** Instagram Transcript Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract transcripts from Instagram videos and reels using auto-generated captions or AI-powered speech-to-text. Returns clean, timestamped transcript segments with full video metadata.

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

# Instagram Transcript Scraper

Extract spoken transcripts from Instagram videos and reels — automatically and at scale. Supports `/reel/`, `/p/`, and `/tv/` URL formats, produces full-text transcripts and optional per-phrase timestamps, and covers 30+ languages with automatic language detection.

## What this actor does

- **Auto transcription** — tries Instagram's native captions first, then falls back to Whisper AI automatically
- **Native captions** — reads Instagram's own auto-generated captions directly; instant when available
- **Whisper AI** — runs local AI speech-to-text on any video with speech, regardless of caption availability
- **Timestamped segments** — optionally outputs per-phrase start/end times alongside the full transcript
- **30+ languages** — automatic language detection or explicit language override for best accuracy
- **Multiple videos** — process a batch of video URLs in a single run
- **Reliable** — built-in retry logic and automatic managed session rotation

## Authentication

This actor requires Instagram session cookies to access video data (Instagram does not expose video content to logged-out users). You can either:

1. **Paste your own cookies** — export from a logged-in browser session using a tool such as [Cookie-Editor](https://cookie-editor.cgagnier.ca/) and paste the JSON into the `cookies` field.
2. **Leave the cookies field blank** — the actor will automatically use a managed pool of shared Instagram sessions. This is the recommended option for most users.

If your cookies expire mid-run, re-export them from your browser and restart the actor.

## Output per video record

**Always present**

- `postUrl` — canonical Instagram URL of the video
- `shortCode` — Instagram shortcode (unique identifier)
- `pk` — Instagram internal numeric media ID
- `id` — combined media ID in `pk_userId` format
- `postDescription` — video caption text
- `thumbnailUrl` — CDN URL of the video thumbnail (time-limited; download promptly)
- `videoUrl` — direct CDN URL to the highest-quality MP4 (time-limited; download promptly)
- `pubDate` — post creation time in ISO 8601 UTC format (e.g. `2025-05-10T14:32:03Z`)
- `likeCount` — number of likes at scrape time
- `commentCount` — number of comments at scrape time
- `userId` — creator's numeric Instagram user ID
- `userName` — creator's Instagram handle
- `userFullName` — creator's display name
- `avatarUri` — CDN URL of the creator's profile picture
- `fullText` — complete transcript of the video as a single string
- `transcriptionMethod` — `native` or `whisper`, indicating how the transcript was produced
- `createdAt` — ISO 8601 UTC timestamp of when this record was scraped

**Present only when `includeSegments` is `true`**

- `audioUrl` — direct CDN URL to the audio-only track (omitted when unavailable)
- `segments` — array of timestamped transcript segments, each containing:
  - `index` — zero-based position of this segment
  - `start` — segment start time in seconds
  - `end` — segment end time in seconds
  - `text` — transcript text for this segment

**Present only on failed records**

- `errMsg` — error description (private post, deleted video, or unsupported media type)

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `videoUrls` | array | required | One or more Instagram video or reel URLs to transcribe. Supports `/p/`, `/reel/`, and `/tv/` formats |
| `transcriptionMethod` | string | `auto` | `auto` — tries native captions then Whisper; `native` — native captions only; `whisper` — Whisper AI always |
| `whisperModel` | string | `base` | Whisper model size: `tiny` (fastest), `base` (balanced), or `small` (most accurate) |
| `language` | string | — | Language code (e.g. `en`, `es`, `fr`). Leave blank for automatic detection. Only active when Whisper is used |
| `includeSegments` | boolean | `false` | When `true`, adds a `segments` array with per-phrase timestamps to each result |
| `cookies` | string | — | Instagram session cookies in JSON format. Leave blank to use the managed session pool |

### Example: transcribe a single reel

```json
{
  "videoUrls": ["https://www.instagram.com/reel/DV29mBcMQwp/"],
  "transcriptionMethod": "auto",
  "whisperModel": "base"
}
```

### Example: multiple videos with timestamped segments

```json
{
  "videoUrls": [
    "https://www.instagram.com/reel/DV29mBcMQwp/",
    "https://www.instagram.com/p/DULBkEngpxg/"
  ],
  "transcriptionMethod": "auto",
  "includeSegments": true
}
```

### Example: force Whisper AI with explicit language and your own cookies

```json
{
  "videoUrls": ["https://www.instagram.com/reel/DV29mBcMQwp/"],
  "transcriptionMethod": "whisper",
  "whisperModel": "small",
  "language": "es",
  "cookies": "[{\"name\":\"sessionid\",\"value\":\"YOUR_SESSION_ID\",\"domain\":\".instagram.com\"}]"
}
```

## Example output

```json
{
  "postUrl": "https://www.instagram.com/p/DV29mBcMQwp/",
  "shortCode": "DV29mBcMQwp",
  "pk": "3852537424986049577",
  "id": "3852537424986049577_16278726",
  "postDescription": "On Friday, US President Donald Trump claimed Iran's air force is \"no longer\"...",
  "thumbnailUrl": "https://scontent-iad6-1.cdninstagram.com/v/thumbnail.jpg",
  "videoUrl": "https://scontent-iad6-1.cdninstagram.com/v/video.mp4",
  "pubDate": "2025-05-11T05:12:03Z",
  "likeCount": 16799,
  "commentCount": 1159,
  "userId": "16278726",
  "userName": "bbcnews",
  "userFullName": "BBC News",
  "avatarUri": "https://scontent-iad3-1.cdninstagram.com/v/avatar.jpg",
  "fullText": "On Friday, U.S. President Donald Trump claimed Iran's Air Force is no longer, as a result of military action...",
  "transcriptionMethod": "whisper",
  "createdAt": "2026-06-08T06:09:05.841Z"
}
```

## Transcription methods

### Auto (recommended)

Tries Instagram's native captions first. Falls back to Whisper AI automatically when native captions are unavailable. Best balance of speed and coverage for most workloads.

### Native captions only

Reads Instagram's built-in auto-generated captions. Fastest option — no audio download needed. May not be available on older posts, non-Reel content, or videos without speech.

### Whisper AI

Always downloads the video and runs local AI speech-to-text. Consistent coverage for any video with speech, independent of Instagram's captioning availability.

| Model | Size | Speed | Accuracy | Best for |
|---|---|---|---|---|
| `tiny` | 39 MB | Fastest | Basic | Quick previews, speed-critical pipelines |
| `base` | 74 MB | Fast | Good | Most use cases |
| `small` | 244 MB | Moderate | Very good | Accented speech, technical or specialized content |

## Instagram CDN URLs expire

The `videoUrl`, `audioUrl`, `thumbnailUrl`, and `avatarUri` fields contain time-limited CDN links that expire within hours to days of the scrape. Download or store any media you need during the run — do not treat these as permanent URLs.

## Known limitations

- **Public videos only** — private accounts, restricted posts, and login-gated content cannot be scraped.
- **Audio quality matters** — Whisper accuracy degrades on videos with heavy background music, multiple overlapping speakers, or very low recording quality.
- **Native captions not always available** — Instagram does not generate captions for all videos. Short clips, older posts, or music-only audio fall back to Whisper automatically in `auto` mode.

## Use cases

- **AI agents and LLM pipelines** — feed Instagram video speech into RAG systems, summarizers, or classifiers
- **Content research** — extract and analyze what creators are saying across a topic or niche
- **Social media monitoring** — capture spoken claims in video content for brand or news tracking
- **Subtitle generation** — produce timestamped captions for repurposed video content
- **Competitive intelligence** — batch-transcribe competitor or industry video content
- **Multilingual analysis** — transcribe non-English video content with automatic language detection
- **Accessibility** — build searchable archives of spoken video content

## FAQ

**Do I need an Instagram account to use this actor?**
No. The actor uses a managed pool of shared Instagram sessions automatically. You can optionally paste your own cookies into the `cookies` field for more reliable access.

**Will this work on private accounts?**
No. Private account videos are not accessible without following the account. Only publicly available videos can be transcribed.

**Can I process multiple videos in one run?**
Yes. Provide as many URLs as you need in the `videoUrls` array. The actor processes them sequentially with automatic pauses between requests.

**What if a video has no speech (music only or silent)?**
Whisper will return an empty or near-empty transcript. Native captions will not exist. The actor returns the record with an empty `fullText` field.

**How accurate is the Whisper transcription?**
The `base` model works well for clear, single-speaker audio. For accented speech, fast speech, or specialized vocabulary, use `small`. Setting the `language` field explicitly improves accuracy for non-English content.

**Are the video and audio URLs in the output permanent?**
No. Instagram CDN URLs are signed and expire within hours or days. Download media during the run if you need to store it.

**How fresh is the data?**
Data is scraped live at the time of the run. Transcripts and metadata reflect the current state of each video at the moment of scraping.

**Is this actor affiliated with Instagram or Meta?**
No. This is an independent third-party tool that automates interaction with the public Instagram website. It is not endorsed by or affiliated with Meta Platforms, Inc.

## Other Instagram Scrapers

Want to get other data from Instagram? Check out our complete suite of Instagram scrapers:

| Actor | Description |
|---|---|
| [Instagram Post Scraper](https://apify.com/crawlerbros/instagram-post-scraper) | Scrape public posts, reels, IGTV, and carousel posts from direct URLs — no login or cookies required |
| [Instagram Comment Scraper](https://apify.com/crawlerbros/instagram-comment-scraper) | Scrape comments from any Instagram post or reel |
| [Instagram Profile Scraper](https://apify.com/crawlerbros/instagram-profile-scraper) | Extract profile data, bio, follower counts, and more |
| [Instagram Followers & Following Scraper](https://apify.com/crawlerbros/instagram-follower-scraper) | Scrape followers and following lists from any profile |
| [Instagram Tagged Posts Scraper](https://apify.com/crawlerbros/instagram-tagged-posts-scraper) | Collect posts where a user has been tagged |
| [Instagram Hashtag Scraper](https://apify.com/crawlerbros/instagram-hashtag-scraper) | Scrape posts and profiles by hashtag |
| [Instagram Story Downloader](https://apify.com/crawlerbros/instagram-story-downloader) | Download stories from Instagram profiles |
| [Instagram Downloader API](https://apify.com/crawlerbros/instagram-downloader-api) | Download photos, videos, and reels from Instagram |
| [Instagram Keyword Scraper](https://apify.com/crawlerbros/instagram-keyword-scraper) | Search and scrape posts by keyword |
| [Instagram Keyword Search Scraper](https://apify.com/crawlerbros/instagram-keyword-search-scraper) | Search Instagram accounts and posts by keyword |

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/instagram-transcript-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
