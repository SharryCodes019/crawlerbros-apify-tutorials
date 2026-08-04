# TikTok Music/Sound Scraper Tutorial: Run This Apify Actor with Python

Scrape TikTok music/sound metadata and the posts that use a particular sound. Input music URLs or IDs. No cookies required.

This repository shows how to run [TikTok Music/Sound Scraper](https://apify.com/crawlerbros/tiktok-music-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tiktok-music-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/tiktok-music-scraper](https://apify.com/crawlerbros/tiktok-music-scraper)
- **SEO title:** TikTok Music/Sound Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape TikTok music/sound metadata and the posts that use a particular sound. Input music URLs or IDs. No cookies required.

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

# TikTok Music Scraper

Scrape TikTok sound and music pages to collect track metadata and the full list of videos that use a given sound. Accepts music page URLs or bare numeric IDs and returns a metadata row per sound followed by post rows for every video using that sound. No login or cookies required.

## What this actor does

- Accepts TikTok music page URLs or raw numeric sound IDs as input
- Emits a metadata row per sound with title, author, duration, cover images, video count, copyright flags, and DSP streaming links (Spotify, Apple Music, etc.)
- Paginates the sound's video list and emits a post row for each video using the sound
- Captures full post metadata: caption, author profile, engagement stats, hashtags, and video details
- Supports toggling metadata rows and post rows independently so you can fetch just stats or just videos
- Empty fields are omitted

## Output per music metadata record

- `rowType` — always `"music"`
- `musicId` — unique TikTok sound ID
- `musicTitle` — sound/track title
- `authorName` — creator display name
- `duration` — duration in seconds
- `isCopyrighted` — whether the sound has a copyright restriction
- `isCommerceMusic` — whether this is a licensed commercial track
- `isOriginal` — whether this is a user-created original sound
- `videoCount` — total videos using this sound on TikTok
- `playUrl` — streamable audio URL (expires)
- `coverLarge` — large cover image URL
- `coverMedium` — medium cover image URL
- `album` — album name (when present, for commercial tracks)
- `tt2dsp` — object with links to Spotify, Apple Music, and other streaming platforms (when present)
- `author.id` — creator's TikTok user ID
- `author.username` — creator handle
- `author.displayName` — creator display name
- `author.verified` — verification status
- `author.avatarUrl` — creator profile image URL
- `author.followerCount` — creator follower count
- `shareMeta.title` — share title text
- `shareMeta.desc` — share description text
- `scrapedAt` — ISO 8601 timestamp of when the record was collected

## Output per post record

- `rowType` — always `"post"`
- `matchedMusicId` — the sound ID this video is associated with
- `postId` — unique TikTok video ID
- `postUrl` — direct URL to the video
- `caption` — full caption text
- `likeCount` — total likes
- `commentCount` — total comments
- `shareCount` — total shares
- `playCount` — total plays/views
- `author.id` — author's TikTok user ID
- `author.username` — author handle
- `author.displayName` — author display name
- `author.verified` — verification status
- `author.avatarUrl` — author profile image URL
- `hashtags` — array of hashtag names parsed from caption
- `scrapedAt` — ISO 8601 timestamp of when the record was collected

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `musicUrls` | string[] | — | TikTok music page URLs. Example: `https://www.tiktok.com/music/original-sound-7595604258835401494` |
| `musicIds` | string[] | — | Bare numeric sound IDs (15–20 digits). Alternative to full URLs. |
| `maxPostsPerSound` | integer | 30 | Maximum videos to collect per sound (0–500). Set to 0 to skip post rows. |
| `includeMusicMetadata` | boolean | `true` | Emit a metadata row per sound with title, stats, cover images, and DSP links. |
| `includePosts` | boolean | `true` | Emit post rows for videos using each sound. |

### Example: single sound by URL

```json
{
  "musicUrls": ["https://www.tiktok.com/music/original-sound-7595604258835401494"],
  "maxPostsPerSound": 30,
  "includeMusicMetadata": true,
  "includePosts": true
}
```

### Example: multiple sounds by ID

```json
{
  "musicIds": ["7595604258835401494", "7234567890123456789"],
  "maxPostsPerSound": 50,
  "includeMusicMetadata": true,
  "includePosts": true
}
```

### Example: metadata-only (no video scraping)

```json
{
  "musicIds": ["7595604258835401494"],
  "includeMusicMetadata": true,
  "includePosts": false
}
```

### Example: large-scale video collection for a viral sound

```json
{
  "musicUrls": ["https://www.tiktok.com/music/original-sound-7595604258835401494"],
  "maxPostsPerSound": 500,
  "includeMusicMetadata": false,
  "includePosts": true
}
```

## Use cases

- **Music labels and A&R teams** tracking how often a track is being used on TikTok and which creators are driving virality
- **Content marketers** identifying trending sounds to incorporate into brand video campaigns
- **UGC researchers** collecting all videos using a specific sound for trend analysis or sentiment studies
- **Podcast and media teams** monitoring original sounds tied to news events or cultural moments
- **Influencer platforms** discovering creators building audiences around a particular music niche
- **Rights management teams** auditing the spread of copyrighted audio across user-generated content

## FAQ

**Q: Do I need a TikTok account, login, or cookies?**  
A: No. The actor uses TikTok's public music API without authentication.

**Q: How do I find a sound's numeric ID?**  
A: Open any TikTok music page in a browser. The URL format is `/music/sound-name-XXXXXXXXXXXXXXXXX` — the final numeric segment is the ID. You can pass the full URL or just the ID.

**Q: How many videos can I collect per sound?**  
A: Up to 500 per sound. TikTok returns approximately 30 videos per page and the actor paginates automatically.

**Q: Do video and audio play URLs expire?**  
A: Yes. TikTok signs all media CDN URLs with a short-lived token. Download or cache media within a few hours of scraping. The `mediaUrlExpiresAt` field indicates when signed URLs expire.

**Q: What are the DSP links in `tt2dsp`?**  
A: DSP stands for Digital Service Provider. These are links to Spotify, Apple Music, and similar streaming platforms. They only appear for licensed commercial tracks; user-created original sounds do not have DSP links.

**Q: Can I get only the sound stats without scraping videos?**  
A: Yes. Set `includePosts: false` and `includeMusicMetadata: true` to get only the metadata row for each sound.

**Q: What does `isOriginal` mean?**  
A: When `isOriginal` is `true`, the sound was recorded by a TikTok user rather than uploaded from a commercial music catalog.

## Related TikTok Scrapers

Build a complete TikTok data pipeline with our full suite:

| Scraper | URL |
|---|---|
| TikTok Post Scraper | https://apify.com/crawlerbros/tiktok-post-scraper |
| TikTok Profile Scraper | https://apify.com/crawlerbros/tiktok-profile-scraper |
| TikTok Comments Scraper | https://apify.com/crawlerbros/tiktok-comments-scraper |
| TikTok Search Scraper | https://apify.com/crawlerbros/tiktok-search-scraper |
| TikTok Hashtag Scraper | https://apify.com/crawlerbros/tiktok-hashtag-scraper |
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

- [Run this actor on Apify](https://apify.com/crawlerbros/tiktok-music-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
