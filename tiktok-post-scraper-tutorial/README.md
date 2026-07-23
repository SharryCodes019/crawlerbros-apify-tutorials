# Tiktok Post Scraper Tutorial: Run This Apify Actor with Python

Scrape TikTok posts by URL and extract comprehensive video metadata including engagement stats, author information, music details, and hashtags.

This repository shows how to run [Tiktok Post Scraper](https://apify.com/crawlerbros/tiktok-post-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tiktok-post-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/tiktok-post-scraper](https://apify.com/crawlerbros/tiktok-post-scraper)
- **SEO title:** Tiktok Post Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape TikTok posts by URL and extract comprehensive video metadata including engagement stats, author information, music details, and hashtags.

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

# TikTok Post Scraper

Scrape any TikTok video or slideshow post by URL or numeric ID. The actor uses a two-step extraction — embed API then `/api/item/detail/` — to return complete post metadata including engagement stats (from statsV2), full author snapshots, music details, hashtags, @mentions, and signed media URLs with expiry timestamps. No TikTok account or cookies are required.

## What this actor does

- Accepts TikTok post URLs (standard `/@user/video/ID` or `/@user/photo/ID` format) and/or raw post IDs
- Returns engagement stats from statsV2 (playCount, likeCount, commentCount, shareCount, collectCount, repostCount) to avoid integer overflow on viral posts
- Extracts full author snapshots including follower/following/heart/video counts
- Parses music details (title, artist, copyright status, play URL, cover URL)
- Extracts hashtags and @mentions with character-level offsets from textExtra
- Provides signed video/cover/music play URLs plus a `mediaUrlExpiresAt` timestamp
- Handles both video and slideshow (photo carousel) post types
- Empty fields are omitted

## Output per post

- `postId` — unique TikTok post ID
- `postUrl` — canonical post URL
- `postType` — `"video"` or `"slideshow"`
- `caption` — full post caption text
- `createTime` — Unix timestamp of publication
- `createdAt` — ISO 8601 publication date
- `locationCreated` — location tag if set by creator
- `playCount` — total play/view count (from statsV2)
- `likeCount` — total like count (from statsV2)
- `commentCount` — total comment count (from statsV2)
- `shareCount` — total share count (from statsV2)
- `collectCount` — total saves/bookmarks (from statsV2)
- `repostCount` — total reposts (from statsV2)
- `isAd` — whether the post is a paid advertisement
- `isAigc` — whether the post is AI-generated content
- `stitchEnabled` — whether stitching is allowed
- `duetEnabled` — whether duets are allowed
- `shareEnabled` — whether sharing is allowed
- `author.id` — author's TikTok user ID
- `author.secUid` — author's secUid for API calls
- `author.username` — author's @handle
- `author.displayName` — author's display name
- `author.verified` — whether the author has a verified badge
- `author.private` — whether the author's account is private
- `author.bio` — author's profile bio
- `author.avatarUrl` — author's avatar image URL
- `author.followerCount` — author's follower count
- `author.followingCount` — number of accounts the author follows
- `author.heartCount` — total likes received by the author
- `author.videoCount` — number of public videos by the author
- `music.id` — music ID
- `music.title` — music/sound name
- `music.authorName` — music artist name
- `music.original` — whether this is original audio created for the post
- `music.duration` — music clip duration in seconds
- `music.isCopyrighted` — copyright flag
- `music.playUrl` — signed audio stream URL
- `music.coverUrl` — music cover art URL
- `video.width` — video width in pixels
- `video.height` — video height in pixels
- `video.duration` — video duration in seconds
- `video.ratio` — aspect ratio string (e.g. `"540p"`)
- `video.definition` — quality label (e.g. `"720p"`)
- `video.bitrate` — video bitrate in bps
- `video.format` — container format (e.g. `"mp4"`)
- `video.playUrl` — signed video stream URL
- `video.downloadAddr` — signed download URL
- `video.cover` — static cover image URL
- `video.dynamicCover` — animated cover image URL
- `mediaUrlExpiresAt` — ISO 8601 expiry time for all signed URLs
- `hashtags` — array of `{id, name}` hashtag objects
- `mentions` — array of `{username, start, end}` @mention objects
- `subtitleInfos` — subtitle track array (when `includeSubtitles` is true)
- `slideshow` — array of media objects for photo carousel posts
- `scrapedAt` — ISO 8601 timestamp when the record was collected

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `postUrls` | array | — | TikTok post URLs (`/@user/video/ID` or `/@user/photo/ID` format) |
| `postIds` | array | — | Numeric post IDs (15–20 digit strings) as alternative to URLs |
| `includeMediaUrls` | boolean | `true` | Include signed video, cover, and music URLs in output |
| `validateMediaUrls` | boolean | `false` | Probe each media URL with a HEAD request to confirm accessibility |
| `includeAuthorStats` | boolean | `true` | Include follower/following/heart/video counts in the author object |
| `includeSubtitles` | boolean | `false` | Include subtitleInfos, bitrateInfo, and volumeInfo arrays |
| `includeHashtags` | boolean | `true` | Include hashtags array extracted from textExtra |
| `includeMentions` | boolean | `true` | Include @mentions array extracted from textExtra with offsets |
| `includeEffectStickers` | boolean | `false` | Include effectStickers and stickersOnItem arrays |

### Example: Scrape a single video post

```json
{
  "postUrls": ["https://www.tiktok.com/@khaby.lame/video/7574844184952081686"],
  "includeMediaUrls": true,
  "includeAuthorStats": true,
  "includeHashtags": true,
  "includeMentions": true
}
```

### Example: Scrape multiple posts by ID

```json
{
  "postIds": ["7574844184952081686", "7640880319159094559"],
  "includeMediaUrls": false,
  "includeAuthorStats": true
}
```

### Example: Scrape a photo carousel (slideshow) post

```json
{
  "postUrls": ["https://www.tiktok.com/@natgeo/photo/7650496998889573645"],
  "includeMediaUrls": true,
  "includeAuthorStats": true
}
```

### Example: Minimal fields — engagement only

```json
{
  "postUrls": [
    "https://www.tiktok.com/@khaby.lame/video/7574844184952081686",
    "https://www.tiktok.com/@natgeo/video/7640880319159094559"
  ],
  "includeMediaUrls": false,
  "includeAuthorStats": false,
  "includeHashtags": false,
  "includeMentions": false
}
```

## Use cases

- **Influencer marketing** — pull full post metrics, author stats, and music details for campaign reporting and ROI measurement
- **Trend research** — monitor engagement velocity on viral posts to identify emerging trends before they peak
- **Content competitive analysis** — benchmark your own posts against competitors by extracting their engagement stats and content metadata
- **Media asset collection** — obtain signed video and cover image URLs for archival or content moderation workflows
- **Brand safety monitoring** — audit posts by a creator before partnering to verify content type flags (isAd, isAigc) and sharing settings
- **Academic research** — build structured datasets of TikTok video metadata for social media studies

## FAQ

**Do I need a TikTok account or cookies?**
No. The actor uses TikTok's public embed API and item detail endpoint. No login is required.

**How long do signed media URLs last?**
Signed video and audio URLs typically expire within 24 hours. The `mediaUrlExpiresAt` field tells you exactly when. Download any media you need promptly after scraping.

**What is the difference between `postUrls` and `postIds`?**
They are two ways to identify the same posts. `postUrls` accepts the standard TikTok URL format; `postIds` accepts the 15–20 digit numeric ID directly. You can provide either or both in the same run.

**Does this work on slideshow (photo carousel) posts?**
Yes. Photo carousels are detected automatically (`postType: "slideshow"`) and the individual image URLs are returned in the `slideshow` array.

**What does `validateMediaUrls` do?**
When enabled, the actor sends a HEAD request to each signed video URL to confirm it is accessible before including it in output. This adds latency but ensures the URLs are valid at the time of scraping.

**Why are engagement stats from statsV2?**
TikTok's legacy `stats` object uses a 32-bit integer for `diggCount`, which overflows to a negative number for posts with more than 2 billion likes. statsV2 returns these as strings and never overflows.

**Can I scrape private or deleted videos?**
No. Private videos and deleted posts return an error from TikTok's API and are skipped.

**Is there a rate limit?**
The actor handles pacing automatically. You can scrape hundreds of posts in a single run without manual delay configuration.

## Related TikTok Scrapers

Build a complete TikTok data pipeline with our full suite:

| Scraper | URL |
|---|---|
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

- [Run this actor on Apify](https://apify.com/crawlerbros/tiktok-post-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
