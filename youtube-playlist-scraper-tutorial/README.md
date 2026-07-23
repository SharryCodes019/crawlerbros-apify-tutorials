# Youtube Playlist Scraper Tutorial: Run This Apify Actor with Python

Scrape all videos from YouTube playlists. Get playlist metadata and complete video listings including titles, durations, thumbnails, and position in playlist.

This repository shows how to run [Youtube Playlist Scraper](https://apify.com/crawlerbros/youtube-playlist-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/youtube-playlist-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/youtube-playlist-scraper](https://apify.com/crawlerbros/youtube-playlist-scraper)
- **SEO title:** Youtube Playlist Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape all videos from YouTube playlists. Get playlist metadata and complete video listings including titles, durations, thumbnails, and position in playlist.

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

# YouTube Playlist Scraper

Scrape all videos from YouTube playlists. Get playlist metadata and complete video listings including titles, durations, thumbnails, and position in playlist.

## Features

- Extract all videos from any public YouTube playlist
- Playlist metadata (title, owner, description, video count)
- Video details (title, duration, channel, thumbnail, availability)
- Handles large playlists with automatic pagination
- Detects deleted/private videos
- HTTP-first approach (fast, no browser needed) with Playwright fallback

## Supported URL Formats

| Format | Example |
|--------|---------|
| Full playlist URL | `https://www.youtube.com/playlist?list=PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf` |
| Watch URL with list | `https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf` |
| Bare playlist ID | `PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf` |

Supported playlist ID prefixes: `PL`, `RD`, `UU`, `OL`, `LL`, `FL`, `WL`.

## Input

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `playlistUrls` | `string[]` | YouTube playlist URLs or IDs (required) | — |
| `maxVideos` | `integer` | Max videos per playlist (0 = all) | `0` |

## Output

Each row represents one video in the playlist:

| Field | Type | Description |
|-------|------|-------------|
| `position` | `number` | Position in playlist (1-based) |
| `videoId` | `string` | YouTube video ID |
| `title` | `string` | Video title |
| `url` | `string` | Full video URL with playlist context |
| `thumbnailUrl` | `string` | Highest resolution thumbnail |
| `duration` | `string` | Duration as "H:MM:SS" or "M:SS" |
| `durationSeconds` | `number` | Duration in seconds |
| `isAvailable` | `boolean` | Whether the video is playable |
| `videoChannelName` | `string` | Video uploader channel name |
| `videoChannelId` | `string` | Video uploader channel ID |
| `videoChannelUrl` | `string` | Video uploader channel URL |
| `playlistId` | `string` | Playlist ID |
| `playlistTitle` | `string` | Playlist title |
| `playlistUrl` | `string` | Full playlist URL |
| `playlistVideoCount` | `number` | Total videos in playlist |
| `playlistOwner` | `string` | Playlist creator name |
| `playlistDescription` | `string` | Playlist description |
| `scrapedAt` | `string` | ISO 8601 timestamp |

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/youtube-playlist-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
