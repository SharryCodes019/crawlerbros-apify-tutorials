# Bluesky Scraper Tutorial: Run This Apify Actor with Python

Scrape Bluesky (AT Protocol) using search posts by keyword or hashtag, fetch user timelines, look up profiles, search for accounts, and pull custom feeds. Pure HTTP, no login required, no proxy needed.

This repository shows how to run [Bluesky Scraper](https://apify.com/crawlerbros/bluesky-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/bluesky-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/bluesky-scraper](https://apify.com/crawlerbros/bluesky-scraper)
- **SEO title:** Bluesky Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Bluesky (AT Protocol) using search posts by keyword or hashtag, fetch user timelines, look up profiles, search for accounts, and pull custom feeds. Pure HTTP, no login required, no proxy needed.

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

# Bluesky Scraper

Scrape **Bluesky** (the AT Protocol social network) — full-text search by keyword or hashtag, fetch user timelines, look up profiles, search for accounts, and pull custom feeds. Pure HTTP, no login, no cookies, no proxy required.

Bluesky's public XRPC endpoints serve every read operation without authentication, so the actor runs straight from datacenter IPs.

## What you get

### Post records (`recordType=post`)

| Field | Description |
| --- | --- |
| `uri` | Canonical AT URI (`at://did:plc:.../app.bsky.feed.post/...`) |
| `cid` | Content ID |
| `url` | Public `bsky.app` URL (derived from `uri` + author handle) |
| `text` | Post text |
| `createdAt` | ISO 8601 timestamp |
| `indexedAt` | When Bluesky indexed the post |
| `language` | ISO 639-1 language code |
| `replyCount` | Reply count |
| `repostCount` | Repost count |
| `likeCount` | Like count |
| `quoteCount` | Quote-post count |
| `bookmarkCount` | Bookmark count |
| `inReplyToUri` | AT URI of parent post (when reply) |
| `inReplyToCid` | CID of parent post (when reply) |
| `isRepost` | `true` if surfaced via repost reason |
| `repostedBy` | Handle that reposted (when `isRepost=true`) |
| `mentions` | Array of mentioned DIDs (extracted from facets) |
| `tags` | Array of hashtags used (lowercase, extracted from facets) |
| `urls` | Array of external URLs in the post (extracted from facets) |
| `mediaAttachments` | Array of `{type, url, previewUrl, description}` for images/videos/external |
| `quotedPost` | Embedded quoted post `{uri, cid, text, authorHandle, authorDid}` |
| `author` | Author summary `{did, handle, displayName, avatar}` |
| `authorHandle` | Author handle (top-level convenience field) |
| `scrapedAt` | ISO 8601 UTC timestamp of extraction |

### Account records (`recordType=account`)

| Field | Description |
| --- | --- |
| `did` | DID (decentralised identifier) |
| `handle` | Bluesky handle (e.g. `bsky.app`) |
| `displayName` | Display name |
| `description` | Bio |
| `avatar` | Avatar URL |
| `banner` | Banner URL |
| `followersCount`, `followsCount`, `postsCount` | Stats |
| `createdAt` | Account creation timestamp |
| `indexedAt` | When Bluesky last reindexed the profile |
| `url` | Public profile URL |

Empty fields are dropped from every record at every depth — the dataset never contains nulls.

## Input

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `mode` | Enum | `search` | `search` / `profile` / `actorSearch` / `feed` / `postThread` / `urlFetch` / `getPosts` / `follows` / `followers` / `getLikes` / `getActorLikes` / `getList` / `getStarterPack` / `feedGeneratorsDiscovery` |
| `searchQuery` | String | `bluesky` | Free-text query (used by `search` and `actorSearch`); also acts as a query keyword for `feedGeneratorsDiscovery` |
| `searchSort` | Enum | `top` | `top` (engagement) or `latest` (recency) — applies to `mode=search` |
| `actor` | String | `bsky.app` | Handle (`bsky.app`) or DID. Used by `profile` / `follows` / `followers` / `getActorLikes` |
| `postUri` | String | — | Full AT URI of a post — used by `mode=postThread` and `mode=getLikes` |
| `postUris` | Array | — | Up to 25 AT URIs to batch-hydrate — used by `mode=getPosts` |
| `postUrls` | Array | — | Public bsky.app post URLs to expand — used by `mode=urlFetch` |
| `listUri` | String | — | AT URI of a Bluesky list — used by `mode=getList` |
| `starterPackUri` | String | — | AT URI of a starter pack — used by `mode=getStarterPack` |
| `feedPreset` | Enum | — | Built-in feed preset — `whats-hot`, `discover`, `mutuals`, `bsky-team`, `hot-classic`, `popular-with-friends`, `for-you`, `news`, `trending-videos`, `quiet-posters`. Overrides `feedUri` when set. |
| `feedUri` | String | — | Custom AT feed URI for `mode=feed` (used when no preset is selected) |
| `language` | Enum | — | ISO 639-1 dropdown (top 30 codes) — drops posts not in this language |
| `excludeReplies` | Boolean | `false` | Drop reply posts |
| `excludeReposts` | Boolean | `false` | Drop reposts |
| `mediaOnly` | Boolean | `false` | Only emit posts with at least one media attachment |
| `minLikes` | Integer | — | Drop posts with fewer likes |
| `minReposts` | Integer | — | Drop posts with fewer reposts |
| `since` | String | — | `YYYY-MM-DD` — earliest post date (search mode) |
| `until` | String | — | `YYYY-MM-DD` — latest post date (search mode) |
| `fromUser` | String | — | Restrict search to a specific author handle / DID |
| `maxItems` | Integer | `40` | Hard cap on emitted records (1-5000) |

### Example input — keyword search

```json
{
  "mode": "search",
  "searchQuery": "AI",
  "language": "en",
  "minLikes": 50,
  "maxItems": 100
}
```

### Example input — hashtag search

```json
{
  "mode": "search",
  "searchQuery": "#python",
  "since": "2026-01-01",
  "maxItems": 200
}
```

### Example input — user profile

```json
{
  "mode": "profile",
  "actor": "bsky.app",
  "maxItems": 50,
  "excludeReplies": true
}
```

### Example input — account search

```json
{
  "mode": "actorSearch",
  "searchQuery": "rust",
  "maxItems": 25
}
```

### Example input — custom feed

```json
{
  "mode": "feed",
  "feedPreset": "whats-hot",
  "maxItems": 100
}
```

### Example input — post thread (post + replies)

```json
{
  "mode": "postThread",
  "postUri": "at://did:plc:z72i7hdynmk6r22z27h6tvur/app.bsky.feed.post/3kxxxx",
  "maxItems": 200
}
```

### Example input — expand post URLs

```json
{
  "mode": "urlFetch",
  "postUrls": [
    "https://bsky.app/profile/bsky.app/post/3kxxxx",
    "https://bsky.app/profile/jay.bsky.team/post/3kyyyy"
  ]
}
```

### Example input — followers / follows

```json
{
  "mode": "followers",
  "actor": "bsky.app",
  "maxItems": 200
}
```

### Example input — likes on a post

```json
{
  "mode": "getLikes",
  "postUri": "at://did:plc:z72i7hdynmk6r22z27h6tvur/app.bsky.feed.post/3kxxxx",
  "maxItems": 100
}
```

### Example input — discover popular feed generators

```json
{
  "mode": "feedGeneratorsDiscovery",
  "searchQuery": "news",
  "maxItems": 50
}
```

### Example input — author + keyword

```json
{
  "mode": "search",
  "searchQuery": "release",
  "fromUser": "bsky.app",
  "maxItems": 50
}
```

## Example output

```json
{
  "recordType": "post",
  "uri": "at://did:plc:z72i7hdynmk6r22z27h6tvur/app.bsky.feed.post/3ml54ry2iwc2x",
  "cid": "bafyreidwzz...",
  "url": "https://bsky.app/profile/bsky.app/post/3ml54ry2iwc2x",
  "text": "Keep it private! We're adding more ways to connect…",
  "createdAt": "2026-04-23T17:06:32.796Z",
  "language": "en",
  "replyCount": 123,
  "repostCount": 255,
  "likeCount": 1509,
  "quoteCount": 47,
  "tags": ["bluesky"],
  "mentions": [],
  "urls": [],
  "mediaAttachments": [
    { "type": "image", "url": "https://cdn.bsky.app/img/feed_fullsize/.../photo.jpg", "previewUrl": "https://cdn.bsky.app/img/feed_thumbnail/.../photo.jpg", "description": "Demonstration of …" }
  ],
  "author": {
    "did": "did:plc:z72i7hdynmk6r22z27h6tvur",
    "handle": "bsky.app",
    "displayName": "Bluesky",
    "avatar": "https://cdn.bsky.app/img/avatar/plain/.../jpeg"
  },
  "authorHandle": "bsky.app",
  "scrapedAt": "2026-05-06T05:24:18Z"
}
```

## Use cases

- **Social listening / brand monitoring** — Track mentions of your brand or product on Bluesky in real time.
- **Trend research** — Pull `mode=feed` "What's Hot" for a daily snapshot of viral content.
- **Influencer discovery** — Combine `actorSearch` + `minLikes` filters to surface high-impact accounts in any niche.
- **Academic research** — Snapshot public conversations on the AT Protocol, with full media + facet provenance.
- **Cross-platform social monitoring** — Pair with our Mastodon / Twitter / Reddit scrapers for full coverage of post-X social media.
- **Content discovery** — Surface high-engagement posts on a specific hashtag for content curation.
- **Competitor tracking** — Use `fromUser` + keyword to monitor what specific competitors post about specific topics.

## FAQ

**Do I need a Bluesky account or login?**
No. Every endpoint this actor uses (`searchPosts`, `getProfile`, `getAuthorFeed`, `searchActors`, `getFeed`) is part of Bluesky's public AppView and serves anonymous traffic.

**How does Bluesky's search work?**
Bluesky supports its standard search operators in the `searchQuery`:
- `from:handle` — posts by a specific user
- `since:YYYY-MM-DD` / `until:YYYY-MM-DD` — date range
- `lang:en` — language filter
- `#hashtag` — exact hashtag match

The actor also exposes `since`, `until`, `fromUser`, and `language` as dedicated input fields that get folded into the query.

**What's the difference between `mode=search` and `mode=actorSearch`?**
- `mode=search` runs full-text search across **posts**.
- `mode=actorSearch` runs typeahead-style search across **accounts** (handles + display names + bios).

**What's a "feed" and which shortnames are supported?**
A feed is a curated post stream produced by a feed-generator service. Built-in shortnames: `whats-hot` / `discover` (Bluesky's official trending feed), `bsky-team`, `mutuals`. Pass any AT URI directly via `feedUri` to scrape custom feeds.

**How are reposts handled?**
A repost surfaced via `getAuthorFeed` is emitted as one record with `isRepost=true` and `repostedBy=<handle>`, with the underlying post's text/media/counts preserved. Use `excludeReposts=true` to drop these.

**How are quoted posts handled?**
A quote-post is emitted as one record with the quoter's text in `text` and the quoted post's metadata in `quotedPost: {uri, cid, text, authorHandle, authorDid}`.

**How current is the data?**
Live — every run hits Bluesky's AppView at request time. Schedule the actor for hourly / daily refreshes.

**Do I need a proxy?**
No. The Bluesky AppView is happy to serve datacenter IPs. The actor sets a polite User-Agent and stays well under any rate limit.

## Limitations

- **`mode=search` is capped at ~100 posts per query.** Bluesky's AppView blocks unauthenticated cursor pagination on `searchPosts` (HTTP 403 from page 2 onward). Each query returns one page of up to 100 posts. To get more results, run multiple queries with different keywords or use `fromUser` + date filters to narrow.
- `mode=profile`, `mode=actorSearch`, and `mode=feed` paginate normally and can return thousands of records.
- Bluesky search is recency-weighted and does not index every post — very old or low-engagement posts may not surface in `searchPosts`.
- Custom feeds depend on third-party feed-generator services; if a generator is offline, the feed returns empty.
- The actor only reads public data — it cannot access private follower lists or DMs.
- Bluesky's AT Protocol is still evolving; field names and embed types may shift between major releases.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/bluesky-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
