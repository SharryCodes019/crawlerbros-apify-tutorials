# TikTok Playlist Scraper Tutorial: Run This Apify Actor with Python

Scrape TikTok playlists - discover all playlists for a profile, get playlist metadata, and extract all videos. Supports playlist URLs, IDs, and profile URLs. No cookies required.

This repository shows how to run [TikTok Playlist Scraper](https://apify.com/crawlerbros/tiktok-playlist-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tiktok-playlist-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/tiktok-playlist-scraper](https://apify.com/crawlerbros/tiktok-playlist-scraper)
- **SEO title:** TikTok Playlist Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape TikTok playlists - discover all playlists for a profile, get playlist metadata, and extract all videos. Supports playlist URLs, IDs, and profile URLs. No cookies required.

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

# TikTok Playlist Scraper

Scrape TikTok playlists (called "mixes" in the API) by providing playlist URLs, playlist IDs, profile URLs, or plain usernames. The actor discovers all playlists for a profile or targets specific playlists directly, then returns playlist metadata rows and video post rows with each video's position in the playlist. No login or cookies required.

## What this actor does

- Accepts playlist URLs, raw playlist IDs, profile URLs, or usernames — any combination of these inputs
- Discovers all playlists for a given profile and scrapes each one up to a configurable limit
- Emits a metadata row per playlist with name, video count, creator info, cover thumbnail, and share metadata
- Emits a post row for every video in each playlist, including the video's position within the playlist
- Supports three modes: `metadata` (playlist info only), `posts` (videos only), and `both`
- Empty fields are omitted

## Output per playlist metadata record

- `rowType` — always `"playlist"`
- `playlistId` — unique playlist/mix ID
- `playlistName` — playlist name as set by the creator
- `videoCount` — total number of videos in the playlist
- `playlistUrl` — full URL to the playlist page
- `creatorId` — creator's TikTok user ID
- `creatorUsername` — creator handle
- `creatorDisplayName` — creator display name
- `creatorVerified` — whether the creator is verified
- `coverPostId` — ID of the video used as the playlist cover
- `coverThumbnailUrl` — thumbnail image URL of the cover video
- `shareMeta.title` — share title text
- `shareMeta.desc` — share description text
- `scrapedAt` — ISO 8601 timestamp of when the record was collected

## Output per post record

- `rowType` — always `"post"`
- `playlistId` — ID of the playlist this post belongs to
- `playlistName` — name of the playlist
- `positionInPlaylist` — zero-based position of this video within the playlist
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
- `music.id` — sound ID
- `music.title` — sound title
- `music.authorName` — sound creator name
- `video.width` — video width in pixels
- `video.height` — video height in pixels
- `video.duration` — video duration in seconds
- `video.playUrl` — streamable video URL (expires)
- `video.cover` — cover/thumbnail image URL
- `hashtags` — array of hashtag names parsed from caption
- `scrapedAt` — ISO 8601 timestamp of when the record was collected

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `playlistUrls` | string[] | — | Full TikTok playlist URLs. Example: `https://www.tiktok.com/@natgeo/playlist/Cinematic-7509464647364283178` |
| `playlistIds` | string[] | — | Raw numeric playlist/mix IDs (15–20 digits). |
| `profileUrls` | string[] | — | Profile URLs — all playlists for each user will be discovered and scraped. |
| `usernames` | string[] | — | TikTok usernames (with or without `@`) — all playlists will be discovered and scraped. |
| `mode` | string | `"both"` | `"both"` returns metadata + posts. `"metadata"` returns playlist info only. `"posts"` returns videos only. |
| `maxPostsPerPlaylist` | integer | 100 | Maximum videos to fetch per playlist (1–5000). |
| `maxPlaylistsPerProfile` | integer | 20 | Maximum playlists to scrape per profile when discovering from a username or profile URL (1–100). |

### Example: discover playlists by username (metadata only)

```json
{
  "usernames": ["natgeo"],
  "mode": "metadata",
  "maxPlaylistsPerProfile": 5
}
```

### Example: scrape a specific playlist by URL

```json
{
  "playlistUrls": ["https://www.tiktok.com/@natgeo/playlist/Cinematic-7509464647364283178"],
  "mode": "both",
  "maxPostsPerPlaylist": 50
}
```

### Example: multiple profiles — full video archive

```json
{
  "usernames": ["natgeo", "nasa"],
  "mode": "both",
  "maxPostsPerPlaylist": 500,
  "maxPlaylistsPerProfile": 20
}
```

### Example: bare playlist IDs

```json
{
  "playlistIds": ["7509464647364283178", "7501234567890123456"],
  "mode": "posts",
  "maxPostsPerPlaylist": 100
}
```

## Use cases

- **Content archivists** backing up all videos from a creator's curated playlists before content is deleted
- **Media researchers** studying how creators organize their content into thematic series or collections
- **Brand teams** auditing playlist-organized product review or tutorial content from influencers
- **Talent managers** tracking playlist growth and video count over time to measure creator output
- **Developers** building structured content libraries from TikTok playlist data for client apps
- **E-learning platforms** collecting structured educational video series from knowledge-creator playlists

## FAQ

**Q: Do I need login or cookies?**  
A: No. The actor works without any credentials.

**Q: How many playlists can a creator have?**  
A: TikTok allows creators to have multiple playlists (called "mixes"). The `maxPlaylistsPerProfile` setting controls how many are scraped per profile.

**Q: What is `mode: "metadata"` useful for?**  
A: It fetches only playlist names, video counts, and creator info without loading any videos. This is the fastest way to audit which playlists a creator has and how large they are.

**Q: What does `positionInPlaylist` mean?**  
A: It is the zero-based index of the video within the playlist as returned by TikTok's API. Position 0 is the first video in the playlist.

**Q: What if a playlist has no public videos?**  
A: Playlists with no accessible videos return only a metadata row (when mode includes metadata) with `videoCount: 0` and no post rows.

**Q: Are video URLs permanent?**  
A: No. TikTok's video play and cover image URLs are signed and expire after several hours. Use `postUrl` as the stable reference.

**Q: Can I mix different input types in one run?**  
A: Yes. You can combine `playlistUrls`, `playlistIds`, `profileUrls`, and `usernames` in a single run. All are processed together.

**Q: How many videos can I get per playlist?**  
A: Up to 5,000 per playlist via the `maxPostsPerPlaylist` setting.

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
| TikTok Profile Mention Scraper | https://apify.com/crawlerbros/tiktok-profile-mention-scraper |
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

- [Run this actor on Apify](https://apify.com/crawlerbros/tiktok-playlist-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
