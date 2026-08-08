# Twitch Scraper Tutorial: Run This Apify Actor with Python

Scrape Twitch, search channels/categories/videos/clips, fetch top live streams, channel info, top games, VOD metadata, and clip details. No login or API key required.

This repository shows how to run [Twitch Scraper](https://apify.com/crawlerbros/twitch-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/twitch-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/twitch-scraper](https://apify.com/crawlerbros/twitch-scraper)
- **SEO title:** Twitch Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Twitch, search channels/categories/videos/clips, fetch top live streams, channel info, top games, VOD metadata, and clip details. No login or API key required.

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

# Twitch Scraper

Scrape Twitch — top live streams, channel info, recent VODs, top clips, and game (category) directories. Pure HTTP via Twitch's public GraphQL endpoint. **No login or API key required.**

## What this actor does

Twitch's public website is powered by a GraphQL API at `gql.twitch.tv`. This actor talks to that API directly using the public web `Client-ID`, the same identifier the Twitch web frontend uses for unauthenticated browsing. That means the actor can pull:

- The current top live streams across Twitch (filterable by language)
- The top games/categories on Twitch right now
- Live streams within a single category
- Channel profile + recent VODs + top clips for any channel
- Top clips for a specific category over a chosen time window
- Single VODs by video ID
- Single clips by slug
- Full search across channels, categories, and videos
- Anything you can identify by a Twitch URL (channel, video, clip, or category page)

All output records are flat JSON with snake-case-style camelCase keys, omit-empty (no `null`/`""`/`[]`/`{}` anywhere in the dataset).

## Modes

| Mode | What you get |
|---|---|
| **Top live streams** (`topStreams`) | The most-viewed live streams across Twitch right now, with broadcaster, game, viewer count, language, tags, and preview thumbnail. Optional language filter. |
| **Top games / categories** (`topGames`) | The top categories on Twitch right now — sorted by current viewer count — with box art, follower counts, and broadcaster counts. |
| **Search Twitch** (`search`) | Free-text search across channels (users), games (categories), and videos. Restrict by `searchType` to `channel`, `game`, or `video` only. |
| **Channel info + VODs + clips** (`byChannel`) | Channel profile (followers, partner status, current live state, last broadcast, banner / profile / offline images) plus recent VODs and top clips. |
| **Browse a category** (`byCategory`) | Live streams currently broadcasting in a given category — filterable by language. |
| **Top clips for a category** (`topClips`) | Top clips for a category over a configurable time window (last day / week / month / all time). |
| **Lookup VOD by ID** (`byVideo`) | Full metadata for a single VOD — title, length, views, owner, game, broadcast type, language. |
| **Lookup clip by slug** (`byClip`) | Full metadata for a single clip — broadcaster, curator, source video, view count, embed URL. |
| **Resolve a Twitch URL** (`byUrl`) | Paste any list of Twitch URLs and the actor resolves each one to the right query (channel / VOD / clip / category page). |

## Filters

All filters apply across modes wherever the field exists. Records that don't have the field pass through (filter is opt-in, not opt-out).

- **Broadcast language** — restrict live streams and search to `EN` / `ES` / `DE` / `FR` / `PT` / `RU` / `JA` / `KO` / `ZH` / `IT` / `TR` / `PL` / `AR` / `TH` / `ID` / `VI` / `NL` / `SV` / `FI` / `DA` / `NO` / `CS` / `HU` / `EL` / `RO` / `BG` / `UK` / `HE` / `MS` / `TL` / `ASL` / `OTHER` (or `(any)` for no filter).
- **Min concurrent viewers** — drop live streams below this count.
- **Min total views** — drop VODs / clips below this view count.
- **Title contains keyword** — case-insensitive substring match against stream / video / clip titles.
- **VOD type** (`byChannel`) — `ARCHIVE`, `HIGHLIGHT`, `UPLOAD`, `PAST_PREMIERE`, `PREMIERE_UPLOAD`.
- **Video sort** (`byChannel`) — `TIME` (most recent first) or `VIEWS` (most-viewed first).
- **Clip time window** — `LAST_DAY`, `LAST_WEEK`, `LAST_MONTH`, or `ALL_TIME`.

## Output fields (per record)

Every record includes a `recordType` discriminator (`stream`, `channel`, `video`, `clip`, `game`, or `error`) and a `scrapedAt` ISO-8601 timestamp.

### Live stream (`recordType: "stream"`)
`streamId`, `title`, `viewersCount`, `streamType`, `language`, `startedAt`, `previewImageURL`, `channelId`, `channelName`, `displayName`, `gameId`, `gameName`, `gameSlug`, `tags`, `broadcaster` (sub-object: `id`/`login`/`displayName`/`profileImageURL`/`primaryColorHex`), `game` (sub-object), `url`.

### Channel (`recordType: "channel"`)
`channelId`, `channelName`, `displayName`, `description`, `createdAt`, `profileImageURL`, `bannerImageURL`, `offlineImageURL`, `primaryColorHex`, `isPartner`, `isAffiliate`, `isStaff`, `followersCount`, `streamTitle`, `currentGame` (sub-object), `liveStream` (sub-object — only present when live), `isLive`, `lastBroadcast` (sub-object), `url`.

### VOD (`recordType: "video"`)
`videoId`, `title`, `description`, `lengthSeconds`, `viewCount`, `createdAt`, `publishedAt`, `previewImageURL`, `broadcastType`, `language`, `gameId`, `gameName`, `gameSlug`, `game` (sub-object), `channelId`, `channelName`, `displayName`, `owner` (sub-object), `url`.

### Clip (`recordType: "clip"`)
`clipId`, `slug`, `title`, `viewCount`, `durationSeconds`, `createdAt`, `language`, `thumbnailURL`, `embedURL`, `videoOffsetSeconds`, `gameId`, `gameName`, `gameSlug`, `game` (sub-object), `channelId`, `channelName`, `displayName`, `broadcaster` (sub-object), `curator` (sub-object), `sourceVideo` (sub-object), `url`.

### Game / category (`recordType: "game"`)
`gameId`, `name`, `displayName`, `slug`, `viewersCount`, `followersCount`, `broadcastersCount`, `boxArtURL`, `avatarURL`, `description`, `url`.

## Default daily-test prefill

The actor's saved prefill is `mode=topStreams, language=EN, maxItems=10`. This always returns ≥1 record because Twitch is always live somewhere — a strong daily-test default.

## FAQ

**Do I need a Twitch account or API key?**
No. The actor uses the public web `Client-ID` (the same one the Twitch site sends from incognito). Optional `authToken` input is supported for higher rate limits, but is never required.

**Why don't I see subscriber counts?**
Subscriber counts and a few other fields are gated by Twitch behind a logged-in OAuth token. Provide an `authToken` (the value of your `auth-token` cookie on twitch.tv) to unlock them, but they are not returned in default unauthenticated mode.

**Why does the actor sometimes engage Apify proxy automatically?**
Twitch's GraphQL endpoint occasionally rate-limits aggressive datacenter IPs. If the first attempt returns 0 records (e.g., 429 / 403), the actor lazily acquires an Apify proxy session and retries. Setting `useApifyProxy=true` up-front avoids the warmup hit.

**Can I scrape chat history?**
No. Chat (IRC / EventSub) is a separate live-streaming surface and out of scope for this actor.

**What's the difference between `byCategory` and `topClips`?**
`byCategory` returns *currently-live streams* in a category (use it to find people streaming a game right now). `topClips` returns *top clips* in that category over a chosen time window.

**How do I find a category slug?**
Open `https://www.twitch.tv/directory/category/<slug>` — for example `just-chatting`, `league-of-legends`, `valorant`. Or use the actor's `topGames` mode and read the `slug` field.

## Limitations

- Twitch's GraphQL endpoint may rotate persisted-query hashes; this actor side-steps that by sending **raw** GraphQL queries (no `persistedQuery` extension), so hash rotation can never break it. The schema itself is stable.
- Subscriber counts, paid emote slots, and other partner-only fields require an `authToken`.
- Per-clip exact rendering URLs (`.mp4` files) require a `gqlClipsAccessToken` separate flow that's beyond the scope of this actor; we surface the official embed URL instead.

## Pricing

Pricing is configured on the Apify platform. There is no charging logic in the actor code itself.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/twitch-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
