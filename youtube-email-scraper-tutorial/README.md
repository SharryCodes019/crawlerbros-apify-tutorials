# YouTube Email Scraper Tutorial: Run This Apify Actor with Python

Extract emails from YouTube channels without CAPTCHA bypass. Scans channel About descriptions and follows Instagram, TikTok and Linktree profiles linked from the channel. HTTP-only, no cookies, no API keys.

This repository shows how to run [YouTube Email Scraper](https://apify.com/crawlerbros/youtube-email-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/youtube-email-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/youtube-email-scraper](https://apify.com/crawlerbros/youtube-email-scraper)
- **SEO title:** YouTube Email Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract emails from YouTube channels without CAPTCHA bypass. Scans channel About descriptions and follows Instagram, TikTok and Linktree profiles linked from the channel. HTTP-only, no cookies, no API keys.

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

# YouTube Email Scraper

Extract verified contact emails from any YouTube channel — including the emails hidden in the creator's Instagram, TikTok, or Linktree bios.

## What this actor does

Give the scraper a list of YouTube channel URLs and it returns every public email address the creator advertises. The scraper opens each channel's public About page, pulls channel metadata (name, handle, channel ID, description, subscriber count), and harvests every email literal it finds — including obfuscated variants like `contact [at] example [dot] com`, which are automatically normalised to proper addresses.

Because creators often hide their business email on Instagram or TikTok rather than on YouTube itself, the scraper also follows every Instagram, TikTok, and Linktree link it finds on the channel page and scans those bios for additional addresses. Every email is tagged with its source so you can tell a YouTube-advertised address apart from one picked up on Instagram.

The result is a clean dataset of one record per channel, with all emails deduplicated, fully qualified, and traceable back to the exact page they were found on.

## Key features

- Accepts every YouTube URL format: `@handle`, `/channel/UC...`, `/c/name`, `/user/name`, or a bare `@handle` string
- Harvests emails from the About description, advertised hyperlinks, and `mailto:` anchors
- Follows Instagram, TikTok, and Linktree links and extracts emails from their bios
- Deobfuscates common anti-scraper patterns: `[at]`, `(at)`, ` AT `, `[dot]`, `(dot)`, ` DOT `
- Per-email source attribution — see exactly where each address came from
- Case-insensitive deduplication with stable ordering
- Transparent residential-proxy fallback — direct requests first, proxy only when blocked
- No cookies, no login, no API keys required
- Zero-null output — empty fields are omitted rather than filled with placeholders

## Input

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `channelUrls` | array of strings | — | **Required.** YouTube channel URLs in any supported shape. |
| `followExternalProfiles` | boolean | `true` | Follow Instagram / TikTok / Linktree links discovered on the channel. |
| `maxExternalPerChannel` | integer | `3` | Cap on external profiles fetched per channel (0-20). |
| `autoProxyFallback` | boolean | `true` | Automatically retry through Apify residential proxy when a page looks blocked. |

**Example input**

```json
{
  "channelUrls": [
    "https://www.youtube.com/@Apify",
    "https://www.youtube.com/@MrBeast",
    "@MKBHD"
  ],
  "followExternalProfiles": true,
  "maxExternalPerChannel": 3,
  "autoProxyFallback": true
}
```

## Output

One record per channel. Fields with no value are omitted.

```json
{
  "channelUrl": "https://www.youtube.com/@Apify/about",
  "channelId": "UCx...",
  "channelHandle": "@Apify",
  "channelName": "Apify",
  "channelDescription": "We help businesses extract data from the web...",
  "subscriberCount": 12500,
  "emails": ["hello@apify.com", "press@apify.com"],
  "sources": [
    {"email": "hello@apify.com", "sourceUrl": "https://www.youtube.com/@Apify/about", "sourceType": "channel_description"},
    {"email": "press@apify.com", "sourceUrl": "https://www.instagram.com/apify/", "sourceType": "instagram_bio"}
  ],
  "externalLinks": [
    "https://apify.com",
    "https://www.instagram.com/apify/",
    "https://twitter.com/apify"
  ],
  "scrapedAt": "2026-04-24T12:00:00+00:00"
}
```

**Field descriptions**

- **`channelUrl`** — canonical URL of the scraped About page
- **`channelId`** — YouTube's stable channel identifier (`UC...`)
- **`channelHandle`** — the `@handle` form of the channel
- **`channelName`** — human-readable channel title
- **`channelDescription`** — full About description text
- **`subscriberCount`** — resolved subscriber count (matches YouTube's on-screen value)
- **`emails`** — deduplicated list of every email discovered for the channel
- **`sources`** — one entry per email with the exact URL and source type
- **`externalLinks`** — advertised links from the About page (not all are crawled)
- **`scrapedAt`** — ISO-8601 timestamp of this run

**Source types**

| `sourceType` | Where the email came from |
| --- | --- |
| `channel_description` | The channel's About description. |
| `channel_external_link` | An email embedded directly in an advertised link. |
| `instagram_bio` | Creator's Instagram profile (bio text or metadata). |
| `tiktok_bio` | Creator's TikTok profile. |
| `linktree` | A Linktree hub linked from the channel. |

**Error record** — emitted when a channel can't be parsed, so the run never fails entirely:

```json
{
  "type": "youtube_email_scraper_error",
  "reason": "fetch_failed",
  "message": "Could not fetch About page (blocked / offline / not found).",
  "channelUrl": "https://www.youtube.com/@SomeClosedChannel/about",
  "scrapedAt": "2026-04-24T12:00:00+00:00"
}
```

## Use cases

- **Influencer outreach** — build a ranked contact list for a shortlist of creators in a niche
- **Brand partnership research** — harvest business emails from your competitor's sponsored-creator roster
- **Agency sourcing** — quickly see which creators publish a reachable inbox vs. hide behind management
- **PR and press** — find the right email for an interview, quote, or product-review request
- **CRM enrichment** — keep your creator-contacts database synced with the emails currently advertised publicly

## FAQ

**Does this scraper bypass CAPTCHAs?**
No. The actor uses only the public About page and the public profile pages of Instagram, TikTok, and Linktree. When a page is fully blocked, the scraper emits an error record for that channel and moves on.

**Do I need cookies, a login, or a YouTube API key?**
No. The scraper is unauthenticated and reads only publicly available data.

**Will it find every email on a channel?**
It finds every email advertised in plain text, as a `mailto:` link, with common obfuscation (`[at]` / `[dot]`), and on linked Instagram / TikTok / Linktree bios. It cannot extract emails hidden behind YouTube's "View email address" click-to-reveal button — that gate requires a logged-in account and is not supported.

**Does it follow every external link on a channel?**
No — only Instagram, TikTok, and Linktree, because those are where creators most often advertise a contact address. All external links are still listed in `externalLinks` so you can follow them downstream if you wish.

**What if a channel has no public emails?**
The channel record is still emitted, just without the `emails` and `sources` fields. You can filter on the presence of `emails` in post-processing.

**How does the proxy fallback work?**
If a direct request returns a suspiciously small response or a known block page, the scraper transparently retries through Apify residential proxy. Set `autoProxyFallback: false` to skip the retry.

**How fast is it?**
Each channel typically takes under a second. Following external profiles adds one HTTP round-trip per profile (capped by `maxExternalPerChannel`).

## Known limitations

- **Click-to-reveal emails on YouTube are not supported.** YouTube's "View email address" button requires a logged-in session; this actor is login-free by design.
- **Instagram login walls** occasionally show for certain regions or IP ranges. When this happens the scraper skips that bio and keeps the emails it already found elsewhere.
- **TikTok region restrictions** can replace a profile with an interstitial page; the scraper still extracts whatever metadata the interstitial exposes.
- **Channels without a public About page** (some custom-branding and music-artist channels) return a `parse_failed` error record.
- **Subscriber counts** reflect YouTube's publicly displayed rounded value (e.g. `12K` → `12000`). Exact counts below YouTube's display threshold are not available.

## YouTube Scraper Suite

This actor is part of a complete YouTube data extraction toolkit. Explore the full suite:

| Actor | Description |
|-------|-------------|
| [YouTube Channel Scraper](https://apify.com/crawlerbros/youtube-channel-scraper) | Channel metadata, subscriber counts, and full video catalogs |
| [YouTube Channel Scraper Fast](https://apify.com/crawlerbros/youtube-channel-scraper-fast) | Streamlined channel scraper for high-volume and speed-sensitive workflows |
| [YouTube Comment Scraper](https://apify.com/crawlerbros/youtube-comment-scraper) | Comments, replies, likes, author info, and pinned/hearted status |
| [YouTube Email Scraper](https://apify.com/crawlerbros/youtube-email-scraper) | Creator contact emails from channel pages, Instagram, TikTok, and Linktree |
| [YouTube Hashtag Scraper](https://apify.com/crawlerbros/youtube-hashtag-scraper) | Videos and Shorts tagged with specific hashtags |
| [YouTube Playlist Scraper](https://apify.com/crawlerbros/youtube-playlist-scraper) | All videos and metadata from any YouTube playlist |
| [YouTube Search Scraper](https://apify.com/crawlerbros/youtube-search-scraper) | Search results including videos, channels, and playlists |
| [YouTube Shorts Scraper](https://apify.com/crawlerbros/youtube-shorts-scraper) | Shorts from channels or hashtags with full view and like metadata |
| [YouTube Transcript Scraper](https://apify.com/crawlerbros/youtube-transcript-scraper) | Timed transcripts and captions with optional Whisper AI fallback |
| [YouTube Trending Scraper](https://apify.com/crawlerbros/youtube-trending-scraper) | Ranked trending videos by category — Gaming, Music, News, Movies |
| [YouTube Video Details Scraper](https://apify.com/crawlerbros/youtube-video-details-scraper) | Comprehensive video metadata, chapters, endscreen, captions, and comments |
| [YouTube Video Downloader](https://apify.com/crawlerbros/youtube-video-downloader) | Download videos, playlists, and channels in any quality with metadata |

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/youtube-email-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
