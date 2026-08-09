# Tiktok Profile Scraper Tutorial: Run This Apify Actor with Python

Scrape TikTok profiles and their video or repost history.

This repository shows how to run [Tiktok Profile Scraper](https://apify.com/crawlerbros/tiktok-profile-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tiktok-profile-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/tiktok-profile-scraper](https://apify.com/crawlerbros/tiktok-profile-scraper)
- **SEO title:** Tiktok Profile Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape TikTok profiles and their video or repost history.

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

# TikTok Profile Scraper

Scrape TikTok profiles and their video or repost history. The actor emits a profile row (rowType=profile) with full account metadata and then individual post rows (rowType=video or rowType=repost) for each piece of content. Without a session cookie the actor returns profile info plus approximately 14 recent videos from search; with a sessionCookie it can retrieve the full video history up to 500 posts. Reposts are available without a cookie.

## What this actor does

- Accepts TikTok usernames (with or without @) and/or full profile URLs
- Emits a dedicated profile row per account with follower/following/like/video counts and account settings
- Emits separate post rows for each video or repost, selectable via `contentTypes`
- Retrieves up to ~14 recent videos without authentication via search fallback
- With a `sessionCookie` or full `cookies` export, retrieves the complete video history (up to 500 posts)
- Reposts (videos the user has shared from other creators) are extracted without a cookie
- Empty fields are omitted

## Output per profile row

- `rowType` — always `"profile"` for profile rows
- `userId` — TikTok user ID
- `secUid` — TikTok secUid
- `username` — @handle
- `displayName` — display name / nickname
- `verified` — verification badge status
- `privateAccount` — whether the account is private
- `bio` — profile bio text
- `bioLink` — clickable link in bio (if set)
- `followerCount` — total followers
- `followingCount` — total accounts followed
- `heartCount` — total likes received across all videos
- `videoCount` — number of public videos
- `avatarLarger` — large avatar image URL
- `avatarMedium` — medium avatar image URL
- `createTime` — account creation Unix timestamp
- `commentSetting` — comment permission setting
- `duetSetting` — duet permission setting
- `stitchSetting` — stitch permission setting
- `profileUrl` — canonical TikTok profile URL
- `scrapedAt` — ISO 8601 scrape timestamp

## Output per video/repost row

- `rowType` — `"video"` or `"repost"`
- `contentKind` — same as rowType for filtering convenience
- `postId` — unique post ID
- `postUrl` — canonical post URL
- `caption` — post caption text
- `createTime` — Unix publication timestamp
- `likeCount` — total likes
- `commentCount` — total comments
- `shareCount` — total shares
- `playCount` — total plays/views
- `author.id` — video author's user ID
- `author.username` — video author's @handle
- `author.displayName` — video author's display name
- `author.verified` — author verification status
- `music.id` — music ID
- `music.title` — music name
- `music.authorName` — music artist
- `video.width` — video width
- `video.height` — video height
- `video.duration` — video duration in seconds
- `hashtags` — array of `{id, name}` hashtag objects
- `profileUsername` — the queried username that produced this row
- `scrapedAt` — ISO 8601 scrape timestamp

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `usernames` | array | — | TikTok usernames to scrape (with or without @) |
| `profileUrls` | array | — | Full TikTok profile URLs as alternative or additional input |
| `contentTypes` | array | `["profile","videos"]` | Which rows to emit: any combination of `"profile"`, `"videos"`, `"reposts"` |
| `maxPostsPerProfile` | integer | `30` | Maximum post rows per profile (0 = skip posts) |
| `includeProfileInfo` | boolean | `true` | Include profile metadata in the profile row |
| `sessionCookie` | string | — | TikTok `sessionid` cookie value — required for full video history |
| `cookies` | array | — | Full browser cookie export as JSON array (Cookie-Editor format) |
| `ttwid` | string | — | TikTok `ttwid` device cookie — enables immediate video listing |

### Example: Profile info and recent videos (no cookie)

```json
{
  "usernames": ["natgeo"],
  "contentTypes": ["profile", "videos"],
  "maxPostsPerProfile": 10
}
```

### Example: Reposts only

```json
{
  "usernames": ["khaby.lame", "charlidamelio"],
  "contentTypes": ["reposts"],
  "maxPostsPerProfile": 50
}
```

### Example: Full video history with session cookie

```json
{
  "usernames": ["natgeo"],
  "contentTypes": ["profile", "videos"],
  "maxPostsPerProfile": 200,
  "sessionCookie": "your_sessionid_value_here"
}
```

### Example: Multiple profiles — profile metadata only

```json
{
  "usernames": ["natgeo", "bbcnews", "cnn"],
  "contentTypes": ["profile"],
  "maxPostsPerProfile": 0
}
```

## Use cases

- **Influencer research** — pull profile stats and recent video performance for creator discovery and vetting
- **Competitive benchmarking** — track a competitor brand account's posting frequency and engagement trends over time
- **Audience and content auditing** — export a creator's complete video history for content strategy or brand safety review
- **Repost tracking** — identify what external content a creator is amplifying through reposts
- **Social media archival** — build structured archives of public TikTok accounts for research or compliance purposes
- **Agency reporting** — collect cross-account profile snapshots for client portfolio dashboards

## FAQ

**Do I need a TikTok account or cookies?**
Not for profile metadata or reposts. For the complete video list you need a `sessionCookie` or full `cookies` export, because TikTok's video listing API blocks unauthenticated datacenter requests.

**How many videos can I get without a cookie?**
Approximately 14 recent videos are available via TikTok's public search fallback. For full history, provide a `sessionCookie`.

**How do I get my sessionCookie?**
Install the Cookie-Editor browser extension, log into TikTok, click the icon, find the cookie named `sessionid`, and copy its value. Paste that value into the `sessionCookie` field.

**What is the difference between `sessionCookie` and `cookies`?**
`sessionCookie` accepts only the `sessionid` value and is sufficient for follower/repost mode. `cookies` accepts the full browser cookie export (Cookie-Editor JSON format) and provides the complete session context including `msToken` and `ttwid` — this gives the most reliable video list retrieval.

**What is `ttwid`?**
A non-personal device tracking cookie from TikTok. Providing your browser's `ttwid` value lets the actor bypass the typical 7-day device-aging period that TikTok applies to new (unknown) devices. Find it in browser DevTools under Application → Cookies → tiktok.com.

**What is a repost?**
A video from another creator that the profile owner has re-shared to their own followers using TikTok's repost feature. The original author and post ID are preserved in the output.

**What does `includeProfileInfo: false` do?**
The profile row is still emitted but without the detailed metadata fields (follower counts, bio, settings). Useful when you only want the post rows.

**Can I scrape private accounts?**
Profile metadata for private accounts is visible, but their video grid is not accessible without being an approved follower.

## Related TikTok Scrapers

Build a complete TikTok data pipeline with our full suite:

| Scraper | URL |
|---|---|
| TikTok Post Scraper | https://apify.com/crawlerbros/tiktok-post-scraper |
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

- [Run this actor on Apify](https://apify.com/crawlerbros/tiktok-profile-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
