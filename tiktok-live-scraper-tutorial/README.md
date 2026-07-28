# TikTok LIVE Event Stream Scraper Tutorial: Run This Apify Actor with Python

Capture real-time events from TikTok LIVE streams including chat messages, gifts, likes, joins, shares, and viewer stats. Requires the broadcaster to be live at runtime.

This repository shows how to run [TikTok LIVE Event Stream Scraper](https://apify.com/crawlerbros/tiktok-live-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tiktok-live-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/tiktok-live-scraper](https://apify.com/crawlerbros/tiktok-live-scraper)
- **SEO title:** TikTok LIVE Event Stream Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Capture real-time events from TikTok LIVE streams including chat messages, gifts, likes, joins, shares, and viewer stats. Requires the broadcaster to be live at runtime.

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

# TikTok LIVE Scraper

Capture real-time events from TikTok LIVE streams. Two modes: Mode A (room metadata — no cookie required, always works if the broadcaster is currently live) retrieves roomId, viewerCount, likeCount, title, stream URLs, and host profile in a single dataset row. Mode B (event stream — requires a sessionid cookie) captures timestamped chat messages, gifts, likes, joins, shares, and stats updates as individual rows. The actor exits cleanly with zero rows and no error when the broadcaster is not currently live.

## What this actor does

- Monitors one or more TikTok usernames or live URLs for active LIVE sessions
- Mode A (no cookie): emits one room-metadata row per live user with title, viewer count, like count, stream URLs, and host profile
- Mode B (sessionid cookie): connects to the LIVE event stream and captures every chat message, gift, like, join, share, and stats update as a separate row
- Stops cleanly after `connectionDuration` seconds or after `eventCap` events — whichever comes first
- Supports an optional `eventTypes` filter to capture only specific event categories
- Exits cleanly with zero rows and a log message when a broadcaster is not live — this is correct behavior, not a failure
- Empty fields are omitted

## Output per room-metadata row (Mode A)

- `roomId` — unique TikTok LIVE room identifier
- `username` — broadcaster's TikTok username
- `displayName` — broadcaster's display name
- `title` — current LIVE stream title
- `viewerCount` — current live viewer count
- `likeCount` — cumulative like count for the stream
- `startTime` — ISO 8601 timestamp when the stream started
- `hostUserId` — broadcaster's TikTok user ID
- `hostAvatarUrl` — broadcaster's avatar image URL
- `streamUrl` — HLS or FLV stream URL (when available)
- `status` — stream status string
- `scrapedAt` — ISO 8601 timestamp of collection

## Output per event row (Mode B)

- `roomId` — unique TikTok LIVE room identifier
- `eventType` — event category: `chat`, `gift`, `like`, `join`, `share`, `follow`, `stats`, or `unknown`
- `timestamp` — ISO 8601 UTC timestamp when the event was received
- `user.id` — sender's TikTok user ID
- `user.username` — sender's TikTok username
- `user.displayName` — sender's display name
- `user.avatarUrl` — sender's avatar image URL
- `payload.text` — chat message text (chat events)
- `payload.giftId` — gift identifier (gift events)
- `payload.count` — gift quantity or like count (gift and like events)

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `usernames` | array of strings | — | TikTok usernames to monitor for LIVE sessions (without the `@` symbol). |
| `liveUrls` | array of strings | — | Direct TikTok LIVE URLs (e.g. `https://www.tiktok.com/@username/live`). Alternative to `usernames`. |
| `connectionDuration` | integer | `60` | Seconds to stay connected per stream (10–3600). The actor disconnects cleanly after this window. |
| `eventCap` | integer | `500` | Stop collecting events from a stream after this many rows (1–10000). |
| `eventTypes` | array of strings | `["all"]` | Filter to specific event types: `chat`, `gift`, `like`, `follow`, `share`, `join`, `stats`, `all`. |
| `sessionCookie` | string (secret) | — | Your TikTok `sessionid` cookie value. Required for Mode B (event stream). Without it, the actor runs in Mode A (room metadata only). |

### Example: Mode A — room metadata, no cookie

```json
{
  "usernames": ["natgeo"],
  "connectionDuration": 10
}
```

### Example: Mode B — event stream with cookie

```json
{
  "usernames": ["khaby.lame"],
  "connectionDuration": 120,
  "eventCap": 1000,
  "eventTypes": ["chat", "gift", "stats"],
  "sessionCookie": "your_sessionid_value_here"
}
```

### Example: Monitor multiple accounts simultaneously

```json
{
  "usernames": ["natgeo", "bbcnews", "cnn"],
  "connectionDuration": 60
}
```

### Example: Monitor a specific live URL

```json
{
  "liveUrls": ["https://www.tiktok.com/@natgeo/live"],
  "connectionDuration": 30
}
```

## Use cases

- **Community management** — monitor chat messages and viewer reactions during your own brand's live events in real time
- **Influencer research** — capture viewership counts, like velocity, and gift activity for live-streaming creators to gauge audience engagement
- **Event coverage** — archive the complete chat and event stream from a product launch, sports event, or music performance broadcast on TikTok
- **Competitive analysis** — track how frequently competitor brands go live and compare peak viewer counts over time
- **Content moderation** — scan live chat streams for spam, harmful keywords, or policy violations during high-traffic events

## FAQ

**Q: What happens if the broadcaster is not live when the actor runs?**  
A: The actor logs a message and exits cleanly with zero dataset rows. This is expected behavior. Schedule the actor during the creator's typical streaming hours for best results.

**Q: Does Mode A require a cookie?**  
A: No. Mode A (room metadata) works without any authentication. It retrieves title, viewer count, like count, stream URLs, and host profile for any broadcaster who is currently live.

**Q: How do I get my sessionid cookie for Mode B?**  
A: Install the Cookie-Editor browser extension, log into TikTok in your browser, open Cookie-Editor, find the cookie named `sessionid`, and copy its value. Paste it into the `sessionCookie` input field.

**Q: Is the sessionid cookie stored or logged?**  
A: No. The cookie is used only to authenticate the WebSocket connection within the actor run and is not persisted or logged anywhere.

**Q: What does `connectionDuration` control?**  
A: It sets how many seconds the actor stays connected to each LIVE stream. A 60-second window typically captures hundreds of chat events during an active stream. Increase it to archive longer sessions.

**Q: Can I monitor multiple users in one run?**  
A: Yes. Add multiple usernames to the `usernames` array. The actor processes each one sequentially — connecting, collecting events for `connectionDuration` seconds, then moving to the next.

**Q: What is the `unknown` event type?**  
A: TikTok sends some event types not yet mapped to a named category. The actor preserves the raw frame method name and payload size as `rawMethod` and `payloadSize` for debugging purposes.

**Q: What stream formats does Mode A return in `streamUrl`?**  
A: When available, the actor captures HLS (m3u8) and FLV stream URLs at resolutions including 360p, 720p, 720p60, and 1080p60.

## Related TikTok Scrapers

Build a complete TikTok data pipeline with our full suite:

| Scraper | URL |
|---|---|
| TikTok Post Scraper | https://apify.com/crawlerbros/tiktok-post-scraper |
| TikTok Profile Scraper | https://apify.com/crawlerbros/tiktok-profile-scraper |
| TikTok Comments Scraper | https://apify.com/crawlerbros/tiktok-comments-scraper |
| TikTok Search Scraper | https://apify.com/crawlerbros/tiktok-search-scraper |
| TikTok Hashtag Scraper | https://apify.com/crawlerbros/tiktok-hashtag-scraper |
| TikTok Music Scraper | https://apify.com/crawlerbros/tiktok-music-scraper |
| TikTok Transcript Scraper | https://apify.com/crawlerbros/tiktok-transcript-scraper |
| TikTok Followers Scraper | https://apify.com/crawlerbros/tiktok-followers-scraper |
| TikTok Mention Scraper | https://apify.com/crawlerbros/tiktok-mention-scraper |
| TikTok Profile Mention Scraper | https://apify.com/crawlerbros/tiktok-profile-mention-scraper |
| TikTok Playlist Scraper | https://apify.com/crawlerbros/tiktok-playlist-scraper |
| TikTok Explore Scraper | https://apify.com/crawlerbros/tiktok-explore-scraper |
| TikTok For You Scraper | https://apify.com/crawlerbros/tiktok-for-you-scraper |
| TikTok Downloader | https://apify.com/crawlerbros/tiktok-downloader-api |
| TikTok Ads Library Scraper | https://apify.com/crawlerbros/tiktok-ads-library-scraper-pro |
| TikTok Top Ads Scraper | https://apify.com/crawlerbros/tiktok-top-ads-scraper |
| TikTok Hashtag Trends Scraper | https://apify.com/crawlerbros/tiktok-hashtag-trends-scraper |

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/tiktok-live-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
