# Tiktok Profile Mention Scraper Tutorial: Run This Apify Actor with Python

Scrape TikTok videos that mention specific usernames (@mentions) without cookies. Extracts video metadata (views, likes, comments, shares), author info, music metadata, and more.

This repository shows how to run [Tiktok Profile Mention Scraper](https://apify.com/crawlerbros/tiktok-profile-mention-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tiktok-profile-mention-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/tiktok-profile-mention-scraper](https://apify.com/crawlerbros/tiktok-profile-mention-scraper)
- **SEO title:** Tiktok Profile Mention Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape TikTok videos that mention specific usernames (@mentions) without cookies. Extracts video metadata (views, likes, comments, shares), author info, music metadata, and more.

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

# TikTok Profile Mention Scraper

Find all TikTok posts that formally @mention a specific creator or brand account. The actor searches TikTok for each username and then validates each result against TikTok's `textExtra` array to confirm a real tagged mention — not just a caption text match. No TikTok account or cookies are required.

## What this actor does

- Accepts TikTok usernames (bare, @-prefixed, or as full profile URLs)
- Searches TikTok for posts mentioning each username
- Validates each result: checks whether the `textExtra` array contains a confirmed type=0 mention tag for the username
- Reports `isMentionConfirmed` (boolean) and the exact `mentionEntry` with character start/end offsets within the caption
- Extracts full post metadata: caption, engagement stats, author info, music, video details, hashtags, and all @mentions
- `confirmedMentionsOnly` filter lets you choose whether to return only validated mentions or all search results
- Empty fields are omitted

## Output per post

- `postId` — unique TikTok post ID
- `postUrl` — canonical post URL
- `caption` — post caption text
- `targetUsername` — the username being monitored
- `isMentionConfirmed` — `true` if a `textExtra` type=0 tag matching the username was found
- `mentionEntry.username` — username from the confirmed textExtra tag
- `mentionEntry.secUid` — secUid from the confirmed textExtra tag
- `mentionEntry.start` — character offset where the @mention begins in the caption
- `mentionEntry.end` — character offset where the @mention ends in the caption
- `author.id` — post author's TikTok user ID
- `author.username` — post author's @handle
- `author.displayName` — post author's display name
- `author.verified` — post author's verification status
- `author.avatarUrl` — post author's avatar URL
- `likeCount` — total likes on the post
- `commentCount` — total comments
- `shareCount` — total shares
- `playCount` — total views
- `createTime` — Unix publication timestamp
- `hashtags` — array of `{id, name}` hashtag objects
- `mentions` — array of all `{username, start, end}` @mention objects in the caption
- `scrapedAt` — ISO 8601 scrape timestamp

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `usernames` | array | — | TikTok usernames to monitor for @mentions |
| `profileUrls` | array | — | Full TikTok profile URLs as alternative or additional input |
| `maxResultsPerProfile` | integer | `50` | Maximum posts to collect per username (1–500) |
| `confirmedMentionsOnly` | boolean | `false` | When `true`, only emit posts with a verified textExtra mention tag |

### Example: Monitor a brand account for confirmed @mentions

```json
{
  "usernames": ["natgeo"],
  "maxResultsPerProfile": 50,
  "confirmedMentionsOnly": true
}
```

### Example: Monitor multiple influencers — all search results

```json
{
  "usernames": ["khaby.lame", "charlidamelio"],
  "maxResultsPerProfile": 100,
  "confirmedMentionsOnly": false
}
```

### Example: Monitor via profile URLs

```json
{
  "profileUrls": ["https://www.tiktok.com/@nike", "https://www.tiktok.com/@adidas"],
  "maxResultsPerProfile": 50,
  "confirmedMentionsOnly": true
}
```

### Example: High-volume mention audit

```json
{
  "usernames": ["natgeo"],
  "maxResultsPerProfile": 500,
  "confirmedMentionsOnly": false
}
```

## Use cases

- **Creator reputation monitoring** — discover who is tagging your TikTok account and what they are saying
- **Brand @mention tracking** — distinguish confirmed textExtra tags from posts that merely contain the brand name string
- **Influencer collaboration discovery** — find creators who actively tag a specific influencer, indicating organic affinity
- **Competitor monitoring** — track who is @mentioning a competitor brand account and the sentiment of those posts
- **Fan community analysis** — understand the community creating @mention content about a creator or artist
- **Campaign attribution** — verify which posts formally @mentioned your account during a specific campaign period

## FAQ

**Do I need a TikTok account or cookies?**
No. The actor uses TikTok's public search API available to anonymous visitors.

**What is a "confirmed @mention"?**
When a TikTok user types `@username` in a caption and TikTok resolves it to a real account, TikTok creates a `textExtra` entry of `type=0` with character offsets. This is more reliable than searching for the username string — a caption could say "not like @reply khaby.lame" where the username appears in text without a formal mention tag.

**What does `isMentionConfirmed: false` mean?**
The post appeared in TikTok's search results for the username but no matching `textExtra` type=0 entry was found. The username may appear as plain text in the caption, or TikTok may have returned the result based on engagement signals rather than an exact text match.

**What is `mentionEntry`?**
The matching `textExtra` object: `{username, secUid, start, end}` where `start` and `end` are character offsets within the caption string.

**How is this different from TikTok Mention Scraper?**
Mention Scraper accepts any keyword (brand names, product names, phrases). This actor is purpose-built for @username tracking and adds the extra validation step against `textExtra` to confirm formal mention tags.

**What does `confirmedMentionsOnly: false` do?**
Returns all search results regardless of textExtra validation, but still sets `isMentionConfirmed` accurately for each row. Useful when you want maximum coverage and will filter yourself downstream.

**How many results can I get?**
Up to 500 per username. With `confirmedMentionsOnly: true` the actual count may be lower since some search results lack formal mention tags.

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

- [Run this actor on Apify](https://apify.com/crawlerbros/tiktok-profile-mention-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
