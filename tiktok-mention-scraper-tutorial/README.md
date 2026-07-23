# Tiktok Mention Scraper Tutorial: Run This Apify Actor with Python

Scrape TikTok videos that mention specific usernames (@mentions) without cookies. Extracts video metadata (views, likes, comments, shares), author info, music metadata, and more. Features anti-bot detection, residential proxy support, and human-like browsing behavior.

This repository shows how to run [Tiktok Mention Scraper](https://apify.com/crawlerbros/tiktok-mention-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tiktok-mention-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/tiktok-mention-scraper](https://apify.com/crawlerbros/tiktok-mention-scraper)
- **SEO title:** Tiktok Mention Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape TikTok videos that mention specific usernames (@mentions) without cookies. Extracts video metadata (views, likes, comments, shares), author info, music metadata, and more. Features anti-bot detection, residential proxy support, and human-like browsing behavior.

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

# TikTok Mention Scraper

Brand monitoring tool — find all TikTok posts that mention any keyword, @handle, or phrase. Uses TikTok's general search API to return matching posts with full engagement stats, author info, hashtag and @mention arrays, and a `mentionInCaption` flag that tells you whether the keyword actually appears in the post caption. No TikTok account or cookies required.

## What this actor does

- Accepts one or more keywords, brand names, @handles, or phrases
- Searches TikTok for each keyword using the public search API
- Reports `mentionInCaption` — a boolean flag indicating the keyword appears in the caption text
- Extracts `mentions[]` from TikTok's `textExtra` array with character-level offsets (confirmed tagged @mentions)
- Returns full engagement stats: views, likes, comments, shares, saves, reposts
- Includes author snapshots with username, display name, follower count, and verification status
- Includes music metadata and video technical details for each post
- Empty fields are omitted

## Output per post

- `postId` — unique TikTok post ID
- `postUrl` — canonical post URL
- `caption` — full post caption text
- `keyword` — the keyword that produced this result
- `rank` — zero-based position in TikTok's search results for this keyword
- `mentionInCaption` — `true` if the keyword string appears in the caption (case-insensitive)
- `author.id` — author's TikTok user ID
- `author.username` — author's @handle
- `author.displayName` — author's display name
- `author.verified` — whether the author has a verified badge
- `author.avatarUrl` — author's avatar image URL
- `author.followerCount` — author's follower count
- `likeCount` — total likes
- `commentCount` — total comments
- `shareCount` — total shares
- `playCount` — total views
- `collectCount` — total saves/bookmarks
- `createTime` — Unix publication timestamp
- `hashtags` — array of `{id, name}` hashtag objects
- `mentions` — array of `{username, start, end}` confirmed textExtra @mention objects
- `music.id` — music ID
- `music.title` — music name
- `music.authorName` — music artist
- `scrapedAt` — ISO 8601 timestamp when the record was collected

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `keywords` | array | — | Keywords, brand names, or @handles to monitor (required) |
| `maxResultsPerKeyword` | integer | `50` | Maximum posts to collect per keyword (1–500) |

### Example: Brand name monitoring

```json
{
  "keywords": ["natgeo", "national geographic"],
  "maxResultsPerKeyword": 100
}
```

### Example: @handle monitoring

```json
{
  "keywords": ["@khaby.lame", "@natgeo"],
  "maxResultsPerKeyword": 50
}
```

### Example: Product launch tracking

```json
{
  "keywords": ["apple vision pro", "visionpro", "apple vr"],
  "maxResultsPerKeyword": 200
}
```

### Example: Multi-keyword competitive analysis

```json
{
  "keywords": ["nike shoes", "adidas shoes", "puma shoes"],
  "maxResultsPerKeyword": 100
}
```

## Use cases

- **Brand monitoring** — track every TikTok post that mentions your brand name, product line, or campaign hashtag
- **Competitor monitoring** — monitor competitor mentions and measure their share of organic TikTok conversation
- **Influencer analysis** — find which creators mention a specific @handle and assess their audience alignment
- **Campaign tracking** — measure reach of a product launch keyword or sponsored event phrase across all creators
- **Crisis management** — rapidly surface negative mentions of a brand name during a PR incident
- **Market research** — discover how consumers naturally talk about a product category or trend

## FAQ

**Do I need a TikTok account or cookies?**
No. The actor uses TikTok's public search API available to anonymous visitors.

**What does `mentionInCaption` mean?**
It is `true` when the keyword string (case-insensitive) appears anywhere in the post caption. For @username keywords it checks for both `@username` and the bare `username` form.

**What is the difference between `mentionInCaption` and `mentions[]`?**
`mentionInCaption` is a simple text search result for the keyword you provided. `mentions[]` contains all formally tagged @mentions parsed from TikTok's `textExtra` array — these are confirmed account tags with character offsets, not just text strings.

**How is this different from TikTok Profile Mention Scraper?**
This actor monitors any keyword, including brand names and phrases that contain no @ symbol. The Profile Mention Scraper is purpose-built for @username tracking and adds a validation step against TikTok's textExtra array to confirm formal tagged mentions.

**How many results can I get per keyword?**
Up to 500. TikTok's search has a finite result set per keyword (typically 50–200 unique posts). The actor stops when TikTok returns `has_more: false`.

**Why might I get fewer results than `maxResultsPerKeyword`?**
TikTok's search exhausts its result set for some keywords quickly, especially niche terms. The actor returns everything available and stops early.

**Can I search in other languages?**
Yes. Enter your keyword in any language. TikTok's search is language-aware and will return locally relevant content.

**Are results sorted by relevance or recency?**
TikTok's default search ranking blends relevance, recency, and engagement. The `rank` field in the output reflects TikTok's result ordering.

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
| TikTok Profile Mention Scraper | https://apify.com/crawlerbros/tiktok-profile-mention-scraper |
| TikTok Playlist Scraper | https://apify.com/crawlerbros/tiktok-playlist-scraper |
| TikTok Explore Scraper | https://apify.com/crawlerbros/tiktok-explore-scraper |
| TikTok For You Scraper | https://apify.com/crawlerbros/tiktok-for-you-scraper |
| TikTok Downloader | https://apify.com/crawlerbros/tiktok-downloader-api |
| TikTok Ads Library Scraper | https://apify.com/crawlerbros/tiktok-ads-library-scraper-pro |
| TikTok Top Ads Scraper | https://apify.com/crawlerbros/tiktok-top-ads-scraper |
| TikTok Hashtag Trends Scraper | https://apify.com/crawlerbros/tiktok-hashtag-trends-scraper |
| TikTok LIVE Scraper | https://apify.com/crawlerbros/tiktok-live-scraper |

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/tiktok-mention-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
