# Tiktok Hashtag Scraper Tutorial: Run This Apify Actor with Python

Scrape TikTok videos by hashtag without cookies. Extracts video metadata (views, likes, comments, shares), author info, music metadata, and more. Features anti-bot detection, residential proxy support, and human-like browsing behavior.

This repository shows how to run [Tiktok Hashtag Scraper](https://apify.com/crawlerbros/tiktok-hashtag-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tiktok-hashtag-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/tiktok-hashtag-scraper](https://apify.com/crawlerbros/tiktok-hashtag-scraper)
- **SEO title:** Tiktok Hashtag Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape TikTok videos by hashtag without cookies. Extracts video metadata (views, likes, comments, shares), author info, music metadata, and more. Features anti-bot detection, residential proxy support, and human-like browsing behavior.

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

# TikTok Hashtag Scraper

Scrape TikTok hashtag pages to collect metadata statistics and the videos posted under any hashtag. Three flexible modes let you pull only the hashtag stats, only the video feed, or both in a single run — all without cookies or login.

## What this actor does

- Accepts one or more hashtags (with or without the `#` symbol) and scrapes each one
- Retrieves hashtag metadata from TikTok's challenge stats: view count, video count, description, and cover images
- Fetches the paginated video feed for each hashtag and returns full post rows with engagement stats
- Supports four modes: `metadata` (stats only, always reliable), `posts` (video feed), `topPosts` (search-based fallback), and `auto` (tries posts, falls back gracefully)
- Automatically falls back to metadata-only when TikTok blocks the post feed, ensuring at least one record per hashtag
- Empty fields are omitted

## Output per hashtag metadata record

- `rowType` — always `"hashtag_metadata"`
- `hashtagId` — unique TikTok challenge/hashtag ID
- `hashtagName` — normalized hashtag name without `#`
- `desc` — hashtag description text
- `videoCount` — total number of videos using this hashtag
- `viewCount` — total view count across all videos using this hashtag
- `isCommerce` — whether this is a branded/commercial hashtag
- `profileLarger` — large cover image URL (when present)
- `profileMedium` — medium cover image URL (when present)
- `shareMeta.title` — share title
- `shareMeta.desc` — share description

## Output per post record

- `postId` — unique TikTok video ID
- `postUrl` — direct URL to the video
- `caption` — full caption text
- `searchedHashtag` — the hashtag used to find this post
- `author.id` — author's TikTok user ID
- `author.secUid` — author's secondary unique ID
- `author.username` — author handle
- `author.displayName` — author display name
- `author.verified` — verification status
- `author.avatarUrl` — author profile image URL
- `likeCount` — total likes
- `commentCount` — total comments
- `shareCount` — total shares
- `playCount` — total plays/views
- `music.id` — sound ID
- `music.title` — sound title
- `music.authorName` — sound creator name
- `music.original` — whether it is an original sound
- `hashtags` — array of hashtag names parsed from caption
- `scrapedAt` — ISO 8601 timestamp of when the record was collected

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `hashtags` | string[] | — | Hashtags to scrape (with or without `#`). Required, minimum 1. |
| `mode` | string | `"auto"` | Scrape mode: `auto`, `metadata`, `posts`, or `topPosts`. |
| `maxPostsPerHashtag` | integer | 50 | Maximum videos to collect per hashtag when mode includes posts (0–500). |
| `includeHashtagMetadata` | boolean | `true` | Emit a metadata stats row for each hashtag in addition to post rows. |

### Example: hashtag stats only (lightest run)

```json
{
  "hashtags": ["fyp", "trending", "viral"],
  "mode": "metadata"
}
```

### Example: posts with metadata

```json
{
  "hashtags": ["cooking"],
  "mode": "auto",
  "maxPostsPerHashtag": 100,
  "includeHashtagMetadata": true
}
```

### Example: competitor hashtag research

```json
{
  "hashtags": ["nikerunning", "adidasoriginals"],
  "mode": "posts",
  "maxPostsPerHashtag": 200,
  "includeHashtagMetadata": false
}
```

### Example: trend monitoring

```json
{
  "hashtags": ["summerfashion", "ootd", "streetstyle"],
  "mode": "auto",
  "maxPostsPerHashtag": 50,
  "includeHashtagMetadata": true
}
```

## Use cases

- **Social media managers** tracking hashtag performance and video count growth over time
- **Brand marketing teams** monitoring branded hashtag campaigns and measuring reach via view count
- **Content creators** identifying high-volume hashtags to include in their posts for discoverability
- **Market researchers** collecting video datasets around industry-specific hashtags for sentiment analysis
- **Agencies** auditing competitor hashtag strategies to benchmark engagement and volume
- **Journalists** monitoring event or news hashtags in real time for content discovery

## FAQ

**Q: Do I need a TikTok account or cookies?**  
A: No. Metadata mode works without any authentication. Post scraping uses TikTok's public API, though success rates vary by IP and session.

**Q: What is the difference between `posts` and `topPosts` mode?**  
A: `posts` mode uses TikTok's paginated hashtag video feed. `topPosts` uses a search-based approach as a fallback when the feed is blocked. `auto` mode tries both in sequence and falls back to metadata-only if needed.

**Q: Why might I get fewer posts than `maxPostsPerHashtag`?**  
A: TikTok limits how many posts are exposed via the hashtag feed API, typically 400–800 videos per hashtag. The actor stops when TikTok returns no more results.

**Q: What does `viewCount` on the metadata row represent?**  
A: It is TikTok's aggregate view count across all videos ever posted under that hashtag, not just the videos you scraped in this run.

**Q: Can I scrape multiple hashtags in one run?**  
A: Yes. Pass multiple values in the `hashtags` array. Each is processed in sequence with the same mode and limit settings.

**Q: Is the `#` symbol required in the input?**  
A: No. The actor normalizes the input and strips any leading `#` characters automatically.

**Q: What does `isCommerce` mean in the metadata row?**  
A: TikTok marks certain hashtags as commercial or branded challenges. This field reflects TikTok's own classification.

## Related TikTok Scrapers

Build a complete TikTok data pipeline with our full suite:

| Scraper | URL |
|---|---|
| TikTok Post Scraper | https://apify.com/crawlerbros/tiktok-post-scraper |
| TikTok Profile Scraper | https://apify.com/crawlerbros/tiktok-profile-scraper |
| TikTok Comments Scraper | https://apify.com/crawlerbros/tiktok-comments-scraper |
| TikTok Search Scraper | https://apify.com/crawlerbros/tiktok-search-scraper |
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

- [Run this actor on Apify](https://apify.com/crawlerbros/tiktok-hashtag-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
