# Tiktok Downloader Api Tutorial: Run This Apify Actor with Python

Download TikTok videos and their cover thumbnails by URL. Give the actor a list of TikTok post links and it will return direct download URLs for both the video file and the cover image - stored in Apify's Key-Value Store and ready to use immediately.

This repository shows how to run [Tiktok Downloader Api](https://apify.com/crawlerbros/tiktok-downloader-api) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tiktok-downloader-api`
- **Apify Store:** [https://apify.com/crawlerbros/tiktok-downloader-api](https://apify.com/crawlerbros/tiktok-downloader-api)
- **SEO title:** Tiktok Downloader Api Tutorial: Run This Apify Actor with Python
- **Description:** Download TikTok videos and their cover thumbnails by URL. Give the actor a list of TikTok post links and it will return direct download URLs for both the video file and the cover image - stored in Apify's Key-Value Store and ready to use immediately.

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

# TikTok Downloader

Download TikTok video files, cover thumbnails, background audio, and slideshow images by URL. The actor stores each file in Apify's Key-Value Store and returns a stable download URL per asset. Supports quality selection (best, 720p, 540p, 360p, smallest) and a configurable filename template. No TikTok account or cookies are required.

## What this actor does

- Accepts TikTok video URLs or bare numeric post IDs as input
- Downloads the selected asset types (video, cover image, audio, slideshow frames) per post
- Stores each file in Apify's Key-Value Store and emits one dataset row per downloaded asset
- Supports quality selection for video downloads: best, 720p, 540p, 360p, or smallest
- Returns file metadata including dimensions, byte size, codec, and bitrate where available
- Allows a custom filename template with `{postId}`, `{type}`, `{ordinal}`, and `{ext}` placeholders
- Processes each URL sequentially to avoid rate limiting
- Empty fields are omitted

## Output per asset

- `postId` — unique TikTok video ID
- `postUrl` — canonical TikTok post URL
- `assetType` — type of asset: `video`, `cover`, `audio`, or `image`
- `ordinal` — index of the asset within its type (useful for slideshow images)
- `kvsKey` — Key-Value Store key used to store the file
- `kvsUrl` — stable Apify Key-Value Store URL to download the file
- `mimeType` — MIME type of the file (e.g. `video/mp4`, `image/jpeg`)
- `byteSize` — file size in bytes
- `width` — pixel width (video and image assets)
- `height` — pixel height (video and image assets)
- `duration` — duration in seconds (video assets)
- `codecType` — video codec identifier (e.g. `h264`)
- `bitrate` — video bitrate in bps
- `gearName` — TikTok quality tier label (e.g. `normal`, `adapt`)
- `downloadedAt` — ISO 8601 timestamp when the file was saved to the store
- `scrapedAt` — ISO 8601 timestamp when the row was emitted

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `postUrls` | array of strings | — | TikTok post URLs to download. Accepts full URLs, short share links, and bare numeric IDs. |
| `postIds` | array of strings | — | Numeric TikTok post IDs (alternative to `postUrls`). |
| `assetTypes` | array of strings | `["video", "cover"]` | Asset types to download per post: `video`, `images` (slideshow frames), `audio`, `cover`. |
| `preferredQuality` | string | `"best"` | Target video quality: `best`, `720p`, `540p`, `360p`, or `smallest`. |
| `filenameTemplate` | string | `"{postId}_{type}_{ordinal}.{ext}"` | Template for Key-Value Store keys. Placeholders: `{postId}`, `{type}`, `{ordinal}`, `{ext}`. |

### Example: Download video and cover thumbnail

```json
{
  "postUrls": ["https://www.tiktok.com/@khaby.lame/video/7574844184952081686"],
  "assetTypes": ["video", "cover"],
  "preferredQuality": "best"
}
```

### Example: Cover thumbnails only (lightweight)

```json
{
  "postUrls": [
    "https://www.tiktok.com/@khaby.lame/video/7574844184952081686",
    "https://www.tiktok.com/@natgeo/video/7341234567890123456"
  ],
  "assetTypes": ["cover"]
}
```

### Example: Download at 540p to save storage

```json
{
  "postUrls": ["https://www.tiktok.com/@bbcnews/video/7395279524742083872"],
  "assetTypes": ["video"],
  "preferredQuality": "540p",
  "filenameTemplate": "{postId}_video_{ordinal}.{ext}"
}
```

### Example: Download slideshow images and audio

```json
{
  "postUrls": ["https://www.tiktok.com/@somecreator/video/7123456789012345678"],
  "assetTypes": ["images", "audio"]
}
```

## Use cases

- **Content archiving** — preserve brand or creator content before it is deleted or made private
- **Ad creative libraries** — download competitor or inspiration videos for internal review and benchmarking
- **Thumbnail pipelines** — bulk-collect cover images for visual classification, brand consistency audits, or moderation workflows
- **Media production** — pull background music tracks (`audio` asset type) from viral TikTok sounds for licensing research
- **Dataset building** — compile labeled video/image datasets for computer vision or multimodal ML training

## FAQ

**Q: Do I need a TikTok account or cookies?**  
A: No. The actor downloads publicly available TikTok videos without any authentication.

**Q: How long are the download URLs valid?**  
A: Files are stored in Apify's Key-Value Store. The `kvsUrl` remains valid as long as the run's storage is retained (default 7 days on the Apify platform). Download the files to your own storage if you need them beyond that window.

**Q: What is the difference between `video` and `images` asset types?**  
A: `video` downloads the standard MP4 file for regular video posts. `images` downloads individual frames from TikTok slideshow (photo carousel) posts, one row per frame. Regular video posts do not produce `image` rows.

**Q: What does `preferredQuality` do exactly?**  
A: The actor picks the bitrate entry from TikTok's `bitrateInfo` list that best matches the requested quality tier. If the exact resolution is not available, it selects the closest available option. `best` always picks the highest bitrate.

**Q: What if a URL fails to download?**  
A: Failed downloads do not block other URLs. Each failed asset produces a dataset row with an error message so you can identify and retry specific posts.

**Q: Are short TikTok URLs (vm.tiktok.com, vt.tiktok.com) supported?**  
A: Yes. The actor resolves short links before downloading.

**Q: Can I download multiple posts in one run?**  
A: Yes. Pass as many URLs as needed in the `postUrls` array. Posts are processed sequentially.

**Q: What filename template should I use for slideshow images?**  
A: Use `{postId}_image_{ordinal}.{ext}` so each frame gets a unique, ordered filename.

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
| TikTok Playlist Scraper | https://apify.com/crawlerbros/tiktok-playlist-scraper |
| TikTok Explore Scraper | https://apify.com/crawlerbros/tiktok-explore-scraper |
| TikTok For You Scraper | https://apify.com/crawlerbros/tiktok-for-you-scraper |
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

- [Run this actor on Apify](https://apify.com/crawlerbros/tiktok-downloader-api)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
