# Youtube Search Scraper Tutorial: Run This Apify Actor with Python

Scrape YouTube search results without cookies. Extracts video metadata (title, views, duration, channel info), channel profiles, and playlists. Supports all YouTube search filters (sort, upload date, type, duration, features).

This repository shows how to run [Youtube Search Scraper](https://apify.com/crawlerbros/youtube-search-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/youtube-search-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/youtube-search-scraper](https://apify.com/crawlerbros/youtube-search-scraper)
- **SEO title:** Youtube Search Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape YouTube search results without cookies. Extracts video metadata (title, views, duration, channel info), channel profiles, and playlists. Supports all YouTube search filters (sort, upload date, type, duration, features).

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

# YouTube Search Scraper

Scrape YouTube search results without needing cookies or a YouTube account. Get video metadata, channel profiles, and playlists from any search query — with full support for YouTube's search filters.

## What it does

Enter one or more search queries and the scraper returns structured data for each result, just like you'd see on YouTube's search page. Results include videos, channels, and playlists depending on your filters.

## Input

| Field | Required | Default | Description |
|-------|----------|---------|-------------|
| **Search Queries** | Yes | — | One or more YouTube search terms |
| Max Results Per Query | No | 20 | How many results to return per query (1–200) |
| Sort By | No | Relevance | Relevance, Upload Date, View Count, or Rating |
| Upload Date | No | Any time | Last hour, Today, This week, This month, This year |
| Result Type | No | All | Video, Channel, or Playlist |
| Duration | No | Any | Under 4 min, 4–20 min, Over 20 min |
| Features | No | None | HD, Subtitles, CC (alias for Subtitles), Creative Commons, Live, 4K, HDR, 360, VR180, Location, Purchased, 3D |
| Market | No | US | Country/region for localized results. One of: `US`, `GB`, `DE`, `IN`, `JP`, `BR`, `FR`, `ES`, `KR`, `RU` |

### Example input

```json
{
  "searchQueries": ["web scraping tutorial", "python automation"],
  "maxResults": 30,
  "sortBy": "view_count",
  "uploadDate": "this_year",
  "type": "video"
}
```

## Output

### Video results

| Field | Example |
|-------|---------|
| videoId | `"dQw4w9WgXcQ"` |
| title | `"Never Gonna Give You Up"` |
| url | `"https://www.youtube.com/watch?v=dQw4w9WgXcQ"` |
| description | `"The official video for..."` |
| channelName | `"Rick Astley"` |
| channelUrl | `"https://www.youtube.com/@RickAstley"` |
| channelId | `"UCuAXFkgsw1L7..."` |
| viewCount | `1500000000` |
| viewCountText | `"1.5B views"` |
| publishedTimeText | `"15 years ago"` |
| duration | `"3:33"` |
| durationSeconds | `213` |
| thumbnails | Array of `{url, width, height}` |
| richThumbnailUrl | Animated preview URL (or null) |
| badges | `["CC", "4K"]` |
| isLive | `false` |
| estimatedResults | `1234567` |
| searchQuery | `"web scraping tutorial"` |
| scrapedAt | `"2026-02-10T12:00:00+00:00"` |

### Channel results

| Field | Example |
|-------|---------|
| channelId | `"UCxxxxxx"` |
| channelName | `"Python Programmer"` |
| channelUrl | `"https://www.youtube.com/@gilesmcmullen"` |
| handle | `"@gilesmcmullen"` |
| description | `"Hi I'm Giles..."` |
| subscriberCount | `782000` |
| subscriberCountText | `"782K subscribers"` |
| thumbnails | Array of `{url, width, height}` |
| channelThumbnailUrl | Single highest-res channel avatar URL |
| verified | `true` |

### Playlist results

| Field | Example |
|-------|---------|
| playlistId | `"PLxxxxxxx"` |
| title | `"Python Full Course"` |
| url | `"https://www.youtube.com/playlist?list=PLxxxxxxx"` |
| channelName | `"CodeWithHarry"` |
| ownerName | `"CodeWithHarry"` (alias for channelName) |
| channelUrl | `"https://www.youtube.com/@CodeWithHarry"` |
| channelId | `"UCxxxxxx"` |
| firstVideoId | `"dQw4w9WgXcQ"` (first video in the playlist) |
| videoCount | `100` |
| videoCountText | `"100 lessons"` |
| thumbnails | Array of `{url, width, height}` |

## Limitations

- YouTube returns approximately 20 results per page. For larger result counts, the scraper automatically paginates.
- Some filters may return fewer results than requested if YouTube doesn't have enough matching content.
- No authentication or cookies are required — the scraper works with publicly available search results only.

## Use Cases

- **Market research** — find top-performing videos in any niche by view count or upload date
- **SEO analysis** — track which channels rank for specific keywords
- **Competitor monitoring** — see what your competitors are posting and how videos perform
- **Content ideation** — find trending topics by sorting by view count
- **Influencer discovery** — use channel search to find YouTubers in any niche
- **Academic research** — systematic collection of videos for corpus building

## YouTube Scraper Suite

This actor is part of a complete YouTube data extraction toolkit. Explore the full suite:

| Actor | Description |
|-------|-------------|
| [YouTube Channel Scraper](https://apify.com/crawlerbros/youtube-channel-scraper) | Channel metadata, subscriber counts, and full video catalogs |
| [YouTube Channel Scraper Fast](https://apify.com/crawlerbros/youtube-channel-scraper-fast) | Streamlined channel scraper for high-volume and speed-sensitive workflows |
| [YouTube Comment Scraper](https://apify.com/crawlerbros/youtube-comment-scraper) | Comments, replies, likes, author info, and pinned/hearted status |
| [YouTube Email Scraper](https://apify.com/crawlerbros/youtube-email-scraper) | Creator contact emails from channel pages, Instagram, TikTok, and Linktree |
| [YouTube Hashtag Scraper](https://apify.com/crawlerbros/youtube-hashtag-scraper) | Videos and Shorts tagged with specific hashtags |
| [YouTube Playlist Scraper](https://apify.com/crawlerbros/youtube-playlist-scraper) | All videos and metadata from any YouTube playlist |
| [YouTube Search Scraper](https://apify.com/crawlerbros/youtube-search-scraper) | Search results including videos, channels, and playlists |
| [YouTube Shorts Scraper](https://apify.com/crawlerbros/youtube-shorts-scraper) | Shorts from channels or hashtags with full view and like metadata |
| [YouTube Transcript Scraper](https://apify.com/crawlerbros/youtube-transcript-scraper) | Timed transcripts and captions with optional Whisper AI fallback |
| [YouTube Trending Scraper](https://apify.com/crawlerbros/youtube-trending-scraper) | Ranked trending videos by category — Gaming, Music, News, Movies |
| [YouTube Video Details Scraper](https://apify.com/crawlerbros/youtube-video-details-scraper) | Comprehensive video metadata, chapters, endscreen, captions, and comments |
| [YouTube Video Downloader](https://apify.com/crawlerbros/youtube-video-downloader) | Download videos, playlists, and channels in any quality with metadata |

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/youtube-search-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
