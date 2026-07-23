# Instagram Downloader Api Tutorial: Run This Apify Actor with Python

Download photos, videos, reels, and carousels from Instagram posts. Extracts detailed metadata for videos and images.

This repository shows how to run [Instagram Downloader Api](https://apify.com/crawlerbros/instagram-downloader-api) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/instagram-downloader-api`
- **Apify Store:** [https://apify.com/crawlerbros/instagram-downloader-api](https://apify.com/crawlerbros/instagram-downloader-api)
- **SEO title:** Instagram Downloader Api Tutorial: Run This Apify Actor with Python
- **Description:** Download photos, videos, reels, and carousels from Instagram posts. Extracts detailed metadata for videos and images.

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

# Instagram Downloader API

Download photos, videos, reels, and carousel posts from Instagram with full technical metadata. Supply direct post URLs or Instagram usernames and receive media files saved to Apify's key-value store alongside structured dataset records with resolution, duration, file size, and source post details.

## What this actor does

- **Download from post URLs** — provide direct `/p/`, `/reel/`, or `/tv/` links to download specific posts
- **Scrape by username** — supply Instagram handles to automatically discover and download recent posts
- **Carousel support** — downloads every image in a multi-photo post as separate files
- **Video metadata** — captures resolution, duration, FPS, codec, bitrate, and file size for each video
- **Image metadata** — captures dimensions, file extension, and file size for each image
- **Cloud storage** — media is uploaded to Apify's key-value store with a public download URL returned in the dataset
- **Reliable** — built-in retry logic and automatic managed session rotation

## Authentication

This actor requires Instagram session cookies to access post media. Authentication is handled automatically using a managed pool of shared Instagram sessions — no credentials or configuration are required from the user.

## Output per media file

One dataset record is created per downloaded media file. A carousel post with 5 images produces 5 records.

**Always present**

- `filename` — saved file name including extension (e.g. `3918833148741120108.jpg`)
- `post_url` — source Instagram post URL
- `username` — Instagram handle of the post creator
- `type` — `image` or `video`
- `download_status` — `finished` when the file was successfully downloaded and stored
- `downloaded_at` — ISO 8601 timestamp of when the file was downloaded
- `storage_key` — key name used in Apify's key-value store
- `download_url` — public URL to access or download the file from Apify's key-value store
- `media_meta_data` — object containing technical file details (see below)

**Fields inside `media_meta_data` — always present**

- `width` — media width in pixels
- `height` — media height in pixels
- `ext` — file extension (`jpg`, `mp4`, etc.)
- `filesize_bytes` — file size in bytes
- `aspect_ratio` — width-to-height ratio (rounded to 2 decimal places)

**Fields inside `media_meta_data` — present only for videos**

- `fps` — frames per second
- `duration` — video length in seconds
- `video_codec` — codec identifier (e.g. `avc1`)
- `total_bitrate_kbps` — total bitrate in kilobits per second

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `postUrls` | array | — | Direct Instagram post, reel, or IGTV URLs to download. Supports `/p/`, `/reel/`, and `/tv/` formats |
| `usernames` | array | — | Instagram handles whose recent posts should be downloaded (e.g. `leomessi`, `natgeo`) |
| `maxPosts_per_username` | integer | `10` | Maximum number of recent posts to download per username. Range 1–100 |

At least one of `postUrls` or `usernames` must be provided.

### Example: download specific posts by URL

```json
{
  "postUrls": [
    "https://www.instagram.com/leomessi/p/DZifppZj_cB/",
    "https://www.instagram.com/natgeo/reel/DYhkH24lf3j/"
  ]
}
```

### Example: download recent posts from usernames

```json
{
  "usernames": ["natgeo", "leomessi"],
  "maxPosts_per_username": 5
}
```

### Example: combine direct URLs with username scraping

```json
{
  "postUrls": ["https://www.instagram.com/leomessi/p/DZifppZj_cB/"],
  "usernames": ["natgeo"],
  "maxPosts_per_username": 3
}
```

## Example output

```json
{
  "filename": "3918833148741120108.jpg",
  "post_url": "https://www.instagram.com/leomessi/p/DZifppZj_cB/",
  "username": "leomessi",
  "type": "image",
  "download_status": "finished",
  "downloaded_at": "2026-07-02T18:46:36.768000",
  "storage_key": "3918833148741120108.jpg",
  "download_url": "https://api.apify.com/v2/key-value-stores/abc123/records/3918833148741120108.jpg",
  "media_meta_data": {
    "width": 1080,
    "height": 1350,
    "ext": "jpg",
    "filesize_bytes": 284672,
    "aspect_ratio": 0.8
  }
}
```

## Known limitations

- **Public posts only** — private account posts are not accessible. The actor detects private profiles and skips them with an error record.
- **Stories not supported** — only permanent posts, reels, and IGTV are downloaded. Stories are excluded.
- **Download URLs are temporary** — files in Apify's key-value store follow standard Apify dataset retention. Export files before they expire if you need permanent storage.
- **Username post discovery** — post discovery from a profile scrolls up to 100 posts; the exact number available depends on how many posts Instagram surfaces in the feed.

## Use cases

- **Content archiving** — save a creator's posts offline or back them up before deletion
- **Brand monitoring** — download posts from competitors or partners for analysis and reporting
- **Social media research** — collect video and image datasets from specific accounts for AI training or analysis
- **Marketing asset collection** — pull media from user-generated content campaigns for review
- **Influencer analysis** — download recent posts to assess visual content quality and engagement patterns
- **Bulk media export** — migrate Instagram media libraries to other platforms or storage systems

## FAQ

**Do I need an Instagram account or cookies to use this actor?**
No. Authentication is handled automatically using a managed pool of shared Instagram sessions. No credentials or configuration are required.

**Can I download from private accounts?**
No. Private account posts are not publicly accessible. The actor detects private profiles and outputs an error record with the profile metadata instead of downloading media.

**How many posts can I download per run?**
There is no hard cap on the number of post URLs you can supply directly. For username-based scraping, the `maxPosts_per_username` field controls how many recent posts are fetched per profile (up to 100).

**Are carousel posts (multiple images) supported?**
Yes. Each image in a carousel is downloaded as a separate file and produces its own dataset record. A 5-image carousel produces 5 records and 5 key-value store entries.

**How long are the downloaded files available?**
Files are stored in Apify's key-value store and follow standard Apify dataset retention policies. Export them before they expire if you need permanent storage.

**How fresh is the data?**
Data is scraped live at the time of the run. Media files and metadata reflect the current state of each post at the moment of scraping.

**Is this actor affiliated with Instagram or Meta?**
No. This is an independent third-party tool that automates interaction with the public Instagram website. It is not endorsed by or affiliated with Meta Platforms, Inc.

## Other Instagram Scrapers

Want to get other data from Instagram? Check out our complete suite of Instagram scrapers:

| Actor | Description |
|---|---|
| [Instagram Post Scraper](https://apify.com/crawlerbros/instagram-post-scraper) | Scrape public posts, reels, IGTV, and carousel posts from direct URLs — no login or cookies required |
| [Instagram Comment Scraper](https://apify.com/crawlerbros/instagram-comment-scraper) | Scrape comments from any Instagram post or reel |
| [Instagram Profile Scraper](https://apify.com/crawlerbros/instagram-profile-scraper) | Extract profile data, bio, follower counts, and more |
| [Instagram Followers & Following Scraper](https://apify.com/crawlerbros/instagram-follower-scraper) | Scrape followers and following lists from any profile |
| [Instagram Tagged Posts Scraper](https://apify.com/crawlerbros/instagram-tagged-posts-scraper) | Collect posts where a user has been tagged |
| [Instagram Hashtag Scraper](https://apify.com/crawlerbros/instagram-hashtag-scraper) | Scrape posts and profiles by hashtag |
| [Instagram Story Downloader](https://apify.com/crawlerbros/instagram-story-downloader) | Download stories from Instagram profiles |
| [Instagram Keyword Scraper](https://apify.com/crawlerbros/instagram-keyword-scraper) | Search and scrape posts by keyword |
| [Instagram Keyword Search Scraper](https://apify.com/crawlerbros/instagram-keyword-search-scraper) | Search Instagram accounts and posts by keyword |
| [Instagram Transcript Scraper](https://apify.com/crawlerbros/instagram-transcript-scraper) | Extract transcripts from Instagram video content |

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/instagram-downloader-api)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
