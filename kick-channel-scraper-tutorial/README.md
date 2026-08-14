# Kick Channel Scraper Tutorial: Run This Apify Actor with Python

Scrape Kick.com streamer channels - profile info, follower counts, live status, VODs, clips, gift leaderboards, custom emotes, and the full category/subcategory taxonomy. No login, no proxy, public JSON API.

This repository shows how to run [Kick Channel Scraper](https://apify.com/crawlerbros/kick-channel-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/kick-channel-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/kick-channel-scraper](https://apify.com/crawlerbros/kick-channel-scraper)
- **SEO title:** Kick Channel Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Kick.com streamer channels - profile info, follower counts, live status, VODs, clips, gift leaderboards, custom emotes, and the full category/subcategory taxonomy. No login, no proxy, public JSON API.

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

# Kick Channel Scraper

Scrape Kick.com — the live-streaming platform — for streamer channel profiles, follower counts, live status, past broadcasts (VODs), clips, gift leaderboards, custom emotes, and the site-wide category/subcategory taxonomy. Uses Kick's public JSON API directly. No login, no cookies, no proxy required.

## What this actor does

- **Channel profiles** — follower count, live status, bio, social links, subscriber badges, chatroom settings, recent categories
- **VODs (past broadcasts)** — title, duration, views, thumbnail, stream categories, per-video playback URL
- **Clips** — either a specific channel's clips or site-wide trending clips, with sort/period/category filters
- **Gift leaderboards** — top gifters per channel, all-time / weekly / monthly
- **Category taxonomy** — browse subcategories (games, IRL activities, etc.), optionally filtered to one of Kick's 6 top-level categories, plus the 6 top-level categories themselves
- **Channel emotes** — a channel's own custom emote set (name, subscriber-only flag, full-size image URL)

## Modes

| Mode | Description | Requires |
|---|---|---|
| `channel` | One channel's profile + live status | `channelSlug` |
| `videos` | A channel's recent VODs | `channelSlug` |
| `clips` | A channel's clips, or global trending clips if `channelSlug` is omitted | — |
| `subcategories` | Browse the subcategory list | — |
| `leaderboard` | A channel's top-gifter leaderboard | `channelSlug` |
| `categories` | The 6 fixed top-level categories | — |
| `emotes` | A channel's own custom emote set | `channelSlug` |

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | string | `categories` (shown as `channel` in the Console) | `channel` / `videos` / `clips` / `subcategories` / `leaderboard` / `categories` / `emotes` |
| `channelSlug` | string | – (shown as `xqc` in the Console) | Kick username, e.g. `xqc`, `adinross` |
| `clipSort` | string | `date` | `date` (newest) or `view` (most viewed) — global clips only |
| `clipPeriod` | string | `all` | `day` / `week` / `month` / `all` — global clips only |
| `clipCategory` | string | – | Restrict global trending clips to one top-level category |
| `subcategoryCategory` | string | – | Restrict subcategory browsing to one top-level category |
| `maxItems` | integer | `20` | Cap on emitted records (1–2000); ignored by `channel` (always 1 record) |

**Note on defaults vs. Console prefill:** `mode`'s underlying schema default is `categories` (Kick's fixed, always-available 6-category list) so that any API/integration call that omits `mode` and `channelSlug` entirely still gets real data back deterministically. The Console UI shows `channel` + `channelSlug=xqc` pre-filled as a friendlier starting point for manual runs — clicking "Start" without editing anything runs the channel-profile example above. `channelSlug` itself has no default (only a Console prefill) so that a `mode=clips` call which omits `channelSlug` correctly falls through to global trending clips instead of silently being scoped to `xqc`.

### Example: channel profile

```json
{ "mode": "channel", "channelSlug": "xqc" }
```

### Example: a channel's recent VODs

```json
{ "mode": "videos", "channelSlug": "adinross", "maxItems": 10 }
```

### Example: global trending clips this week, gambling category

```json
{ "mode": "clips", "clipSort": "view", "clipPeriod": "week", "clipCategory": "gambling", "maxItems": 50 }
```

### Example: a channel's own clips

```json
{ "mode": "clips", "channelSlug": "trainwreckstv", "maxItems": 30 }
```

### Example: browse subcategories under "Games"

```json
{ "mode": "subcategories", "subcategoryCategory": "games", "maxItems": 100 }
```

### Example: top gifters for a channel

```json
{ "mode": "leaderboard", "channelSlug": "xqc" }
```

### Example: the 6 top-level categories

```json
{ "mode": "categories" }
```

### Example: a channel's custom emotes

```json
{ "mode": "emotes", "channelSlug": "xqc" }
```

## Output

Fields vary by `recordType` (`channel`, `video`, `clip`, `subcategory`, `leaderboardEntry`, `category`, `emote`). Empty/unavailable fields are omitted rather than emitted as null.

**Channel:** `slug`, `channelId`, `username`, `bio`, `profilePicUrl`, `followersCount`, `verified`, `isAffiliate`, `isBanned`, `vodEnabled`, `subscriptionEnabled`, `socials` (instagram/twitter/youtube/discord/tiktok/facebook), `bannerUrl`, `chatroom` (chatMode, slowMode, followersMode, subscribersMode, emotesMode), `recentCategories[]`, `isLive`, `streamTitle`, `viewerCount`, `startTime`, `streamThumbnailUrl`, `liveCategories[]`, `kickUrl`

**Video (VOD):** `videoId`, `channelSlug`, `title`, `language`, `isMature`, `durationSeconds`, `views`, `viewerCount`, `createdAt`, `startTime`, `tags[]`, `thumbnailUrl`, `streamUrl`, `videoStatus`, `categories[]`, `videoUrl`

**Clip:** `clipId`, `title`, `isMature`, `privacy`, `durationSeconds`, `views`, `likes`, `createdAt`, `clipUrl`, `thumbnailUrl`, `channelSlug`, `channelUsername`, `channelProfilePicUrl`, `creatorUsername`, `creatorSlug`, `category` (id/name/slug), `parentCategory`, `kickUrl`

**Subcategory:** `subcategoryId`, `name`, `slug`, `tags[]`, `description`, `isMature`, `isPromoted`, `viewers`, `bannerUrl`, `parentCategory` (id/name/slug), `kickUrl`

**Leaderboard entry:** `channelSlug`, `period` (`allTime`/`week`/`month`), `rank`, `username`, `userId`, `quantity`, `kickUrl`

**Category (top-level):** `categoryId`, `name`, `slug`, `icon`, `kickUrl`

**Emote:** `emoteId`, `name`, `channelSlug`, `subscribersOnly`, `emoteUrl`, `kickUrl`

## Use cases

- **Streamer analytics** — track a creator's follower growth, live status, and VOD/clip performance over time
- **Talent scouting / esports** — discover trending clips per game category to spot rising streamers
- **Content aggregation** — pull recent VODs and clips for a highlight roundup
- **Creator-economy research** — analyze gift-leaderboard data to study viewer spending behavior
- **Category/tag discovery** — enumerate Kick's full subcategory taxonomy for content classification
- **Emote/brand asset collection** — pull a streamer's custom emote set and image URLs for chat overlays, merch, or Discord servers

## FAQ

**Do I need a Kick account or API key?** No. Every mode uses Kick's public JSON endpoints, the same ones the kick.com website itself calls.

**Why is `isLive` sometimes `false` with no other live fields?** Kick only returns live-stream data (title, viewer count, thumbnail) while the channel is actually broadcasting. Offline channels still return their full profile — follower count, bio, socials, etc.

**Why does `videos` mode return at most ~18-20 items?** Kick's public VOD endpoint returns only the most recent broadcasts per channel and doesn't paginate further; this actor surfaces everything the API exposes.

**What are the 6 top-level categories?** Games, IRL, Music, Gambling, Creative, Alternative — used to filter global trending clips and the subcategory browser.

**Why does `subcategories` mode return at most ~200 records (per `subcategoryCategory` filter or overall)?** Kick's subcategory-browse endpoint reports a much larger `total`/`last_page`, but silently caps real pagination at an internal ceiling (page 20 of 10 items each) — requesting a page past that ceiling just re-serves the same last page instead of erroring or returning empty. This actor detects the ceiling via the endpoint's own `current_page` field and stops there, so it never fabricates duplicate or phantom records; ~200 is the genuine amount Kick exposes per query through this endpoint.

**Why is `clips` mode slower for some `clipCategory` values than others?** Kick's global clips endpoint silently ignores the `category` query parameter server-side, so this actor filters client-side against each clip's own category instead. Popular categories (`games`, `gambling`, `irl`) are common in the trending feed and fill `maxItems` quickly; niche categories (`music`, `creative`, `alternative`) are genuinely rarer in the feed, so reaching a large `maxItems` for one of those can require scanning many more pages and take noticeably longer. This is an upstream data-distribution characteristic, not a bug — the actor always returns only correctly-matching records, just at different speeds per category.

**Why doesn't `emotes` mode return Kick's global/emoji emotes too?** Kick's emotes endpoint returns 3 sets per request: the channel's own custom set, plus a site-wide "Global" set and an "Emoji" set that are identical for every channel. Only the channel-specific set is returned so the output actually reflects the requested `channelSlug` — the Global/Emoji sets would otherwise look like a bug (same records for every channel).

**Is there a search mode?** Not currently. Kick's search endpoints require an unpublished parameter format that returns `400` for every guessed name; a client-rendered `kick.com/search` page was the only route that returned data, and no public JSON endpoint could be confirmed to back it reliably. Adding search would risk shipping a mode that silently breaks, so it's left out until a stable public endpoint is found.

**How fresh is the data?** Real-time — every request hits Kick's live API directly.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/kick-channel-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
