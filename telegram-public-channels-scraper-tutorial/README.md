# Telegram Public Channels Scraper Tutorial: Run This Apify Actor with Python

Scrape Telegram public channels via the web preview (t.me/s/{channel}) with channel metadata + recent posts with text, media URLs, view counts, and forwarded-from attribution. No login, no Telegram app, no proxy required.

This repository shows how to run [Telegram Public Channels Scraper](https://apify.com/crawlerbros/telegram-public-channels-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/telegram-public-channels-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/telegram-public-channels-scraper](https://apify.com/crawlerbros/telegram-public-channels-scraper)
- **SEO title:** Telegram Public Channels Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Telegram public channels via the web preview (t.me/s/{channel}) with channel metadata + recent posts with text, media URLs, view counts, and forwarded-from attribution. No login, no Telegram app, no proxy required.

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

# Telegram Public Channels Scraper

Scrape any **public Telegram channel** via the web preview at `t.me/s/{channel}`. Pull channel metadata (title, bio, subscriber count, photo/video counts) plus recent posts with text, media URLs, view counts, and forwarded-from attribution. No login, no Telegram app, no proxy — datacenter IPs work fine.

Built for OSINT research, news monitoring, crypto-community tracking, and any analytics workflow that needs structured data from public Telegram channels.

## What you get

### Channel records (`recordType=channel`)

| Field | Description |
| --- | --- |
| `channel` | Channel handle (without `@`) |
| `id` | Same as `channel` (handle is canonical ID) |
| `url` | Public Telegram URL (`https://t.me/{channel}`) |
| `title` | Channel display name |
| `description` | Channel bio |
| `avatarUrl` | Channel avatar URL |
| `subscribersCount` | Subscriber count (parsed from `1.2M` / `12K` short form) |
| `photosCount` | Total photo count |
| `videosCount` | Total video count |
| `filesCount` | Total file/document count |
| `linksCount` | Total external-link count |
| `verified` | `true` for verified channels |

### Post records (`recordType=post`)

| Field | Description |
| --- | --- |
| `id` | Post message ID (channel-relative) |
| `channel` | Source channel handle |
| `url` | Direct post URL (`https://t.me/{channel}/{id}`) |
| `publishedAt` | ISO 8601 timestamp |
| `text` | Plain-text post body (newlines preserved) |
| `viewCount` | View count (parsed from `1.2K` / `99M` short form) |
| `mediaAttachments` | Array of `{type, url, [thumbnailUrl, title]}` for photo / video / document |
| `isForwarded` | `true` if the post was forwarded from another channel |
| `forwardedFrom` | Source channel handle (when `isForwarded=true`) |
| `inReplyToUrl` | Permalink of the post being replied to |
| `scrapedAt` | ISO 8601 UTC timestamp |

Empty fields are dropped from every record at every depth.

## Input

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `mode` | Enum | `channels` | `channels` (channel metadata + recent posts) or `singlePost` (one post by URL) |
| `channels` | Array | `["durov"]` | Channel handles (without `@`) or `t.me/{channel}` URLs (mode=channels) |
| `postUrls` | Array | — | `t.me/<channel>/<post_id>` URLs to fetch one-by-one (mode=singlePost) |
| `searchQuery` | String | — | Keyword search within each channel's history (mode=channels) — uses `t.me/s/<channel>?q=…` |
| `since` | String | — | Earliest post date (`YYYY-MM-DD` or ISO 8601). Pagination stops once the page is older than this. |
| `until` | String | — | Latest post date (`YYYY-MM-DD` or ISO 8601). Posts newer than this are dropped. |
| `maxPostsPerChannel` | Integer | `50` | Hard cap on posts per channel (1-1000) |
| `includeChannelMeta` | Boolean | `true` | Emit a separate `channel` record for each channel |
| `mediaOnly` | Boolean | `false` | Drop posts without any media attachment |
| `minViews` | Integer | — | Drop posts with fewer views than this |
| `excludeForwarded` | Boolean | `false` | Drop forwarded posts |
| `maxItems` | Integer | `100` | Hard cap on total emitted records |

**Album / grouped posts**: when a post contains multiple images (a Telegram "album"), the actor emits **all** image URLs in `mediaAttachments`, sets `isAlbum: true`, and (when present) sets `albumId` to Telegram's `data-grouped-id`.

### Example input — single channel

```json
{
  "mode": "channels",
  "channels": ["durov"],
  "maxPostsPerChannel": 50
}
```

### Example input — keyword search within channels

```json
{
  "mode": "channels",
  "channels": ["telegram", "tginfo"],
  "searchQuery": "feature",
  "maxPostsPerChannel": 100
}
```

### Example input — date window

```json
{
  "mode": "channels",
  "channels": ["durov"],
  "since": "2026-01-01",
  "until": "2026-04-30",
  "maxPostsPerChannel": 500
}
```

### Example input — single post by URL

```json
{
  "mode": "singlePost",
  "postUrls": [
    "https://t.me/durov/100",
    "https://t.me/telegram/300"
  ]
}
```

### Example input — multiple channels, posts only

```json
{
  "channels": ["durov", "telegram", "tginfo"],
  "includeChannelMeta": false,
  "maxPostsPerChannel": 30
}
```

### Example input — high-engagement filter

```json
{
  "channels": ["breakingnews"],
  "minViews": 10000,
  "excludeForwarded": true,
  "maxPostsPerChannel": 200
}
```

### Example input — media tracking

```json
{
  "channels": ["spacepictures"],
  "mediaOnly": true,
  "maxPostsPerChannel": 100
}
```

## Example output

```json
{
  "recordType": "channel",
  "channel": "durov",
  "id": "durov",
  "url": "https://t.me/durov",
  "title": "Pavel Durov",
  "description": "Founder of Telegram. Building a platform for free communication.",
  "avatarUrl": "https://cdn.telegram.org/photo/durov.jpg",
  "subscribersCount": 12600000,
  "photosCount": 523,
  "videosCount": 42,
  "scrapedAt": "2026-05-06T06:42:18Z"
}
```

```json
{
  "recordType": "post",
  "id": "100",
  "channel": "durov",
  "url": "https://t.me/durov/100",
  "publishedAt": "2026-04-15T14:32:00+00:00",
  "text": "Big announcement coming next week.",
  "viewCount": 1200000,
  "mediaAttachments": [
    { "type": "photo", "url": "https://cdn.telegram.org/photo/abc.jpg" }
  ],
  "scrapedAt": "2026-05-06T06:42:18Z"
}
```

## Use cases

- **OSINT / intelligence research** — Snapshot public Telegram channels of interest (geopolitical, journalism, dissident communities).
- **Crypto / market monitoring** — Many trading communities publish first on Telegram; monitor for signals.
- **News monitoring** — Track breaking-news channels for headlines as they post.
- **Brand monitoring** — Track mentions of your brand or product in Telegram channels.
- **Compliance / regulatory** — Monitor channels for misuse of trademarks or copyrighted material.
- **Academic research** — Bulk-collect public discourse on Telegram for sociological / linguistic analysis.

## FAQ

**Do I need a Telegram account or the Telegram app?**
No. The actor uses Telegram's official **web preview** at `t.me/s/{channel}` — fully public, no login. Works against any "public" channel (the kind that has a `t.me/` URL).

**What about private / invite-only channels?**
Private channels (those joined via invite links and without a public `t.me/` handle) are **not accessible** without a logged-in Telegram account, and this actor doesn't support that.

**How many posts can I get per channel?**
Up to 1000 per channel via `maxPostsPerChannel`. The web preview returns ~16-20 posts per page; the actor paginates via `?before=N` cursors to reach further back. Performance: ~1-2 seconds per page.

**How does pagination work?**
The actor reads the smallest message ID on each page and uses it as `?before=` cursor for the next page. This is the standard `t.me/s/` pagination pattern.

**How current is the data?**
Live — every run hits Telegram's web preview at request time. Schedule the actor for hourly / daily refreshes on watchlist channels.

**Do I need a proxy?**
Usually no — `t.me/s/` works from datacenter IPs out of the box. If you scrape from a region where Telegram is blocked at the network level (e.g. some corporate networks), enable proxy via Apify's platform-level config.

**Are comments / reactions included?**
Comments and reaction counts aren't exposed on the public web preview (Telegram surfaces them only inside the app or via the Bot API). The actor returns post text, view count, and media — these are everything `t.me/s/` publishes.

**What about NSFW / sensitive channels?**
The actor returns whatever `t.me/s/` serves. Telegram itself flags certain channels as sensitive; in those cases the page renders a warning shell with no posts, and the actor returns an empty result with a clear status message.

## Limitations

- Comments, reactions, and detailed engagement metrics aren't on the web preview (Telegram exposes those only in-app or via the Bot API with admin auth).
- Voice/video notes don't have direct download URLs in the web preview.
- Some country-blocked channels may not render outside their target region.
- Telegram's `t.me/s/` only shows the latest few thousand messages; very old archives are not paginatable indefinitely.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/telegram-public-channels-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
