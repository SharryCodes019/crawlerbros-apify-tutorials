# Reddit Video Downloader Tutorial: Run This Apify Actor with Python

Download videos from Reddit posts, subreddits, or user profiles. Supports Reddit-hosted videos, YouTube embeds, Streamable, and other video hosts. Extracts metadata including resolution, duration, codec, and filesize. Stores downloaded videos in Apify key-value store with direct download URLs.

This repository shows how to run [Reddit Video Downloader](https://apify.com/crawlerbros/reddit-video-downloader) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/reddit-video-downloader`
- **Apify Store:** [https://apify.com/crawlerbros/reddit-video-downloader](https://apify.com/crawlerbros/reddit-video-downloader)
- **SEO title:** Reddit Video Downloader Tutorial: Run This Apify Actor with Python
- **Description:** Download videos from Reddit posts, subreddits, or user profiles. Supports Reddit-hosted videos, YouTube embeds, Streamable, and other video hosts. Extracts metadata including resolution, duration, codec, and filesize. Stores downloaded videos in Apify key-value store with direct download URLs.

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

# Reddit Video Downloader

Download videos from Reddit posts or entire subreddits. Supports Reddit-hosted videos (v.redd.it) with full audio, plus external video hosts. Extracts comprehensive metadata and provides direct download links for every video.

## Use Cases

### Content Archiving

Bulk download videos from any subreddit for backup or offline viewing. Preserve content before it gets removed or deleted.

### Research & Analysis

Collect video metadata (resolution, duration, engagement metrics) at scale for social media research, trend analysis, or academic studies.

### Content Pipelines

Feed downloaded videos into automated workflows — transcription, AI analysis, content moderation, or media aggregation.

### Trend Monitoring

Track trending video content across subreddits by sorting and filtering posts by time period and popularity.

## Input

| Parameter      | Type    | Default | Description                                                                            |
| -------------- | ------- | ------- | -------------------------------------------------------------------------------------- |
| `postUrls`     | Array   | `[]`    | Direct Reddit post URLs to download videos from                                        |
| `subreddits`   | Array   | `[]`    | Subreddit names to scan for video posts (without `r/` prefix)                          |
| `maxVideos`    | Integer | `10`    | Maximum videos to download per subreddit (1–100)                                       |
| `sort`         | String  | `hot`   | Sort method: `hot`, `new`, `top`, `rising`, `controversial`                            |
| `timeFilter`   | String  | `week`  | Time filter for `top` / `controversial`: `hour`, `day`, `week`, `month`, `year`, `all` |
| `quality`      | String  | `best`  | Video quality: `best`, `1080`, `720`, `480`, `360`, `worst`                            |
| `includeAudio` | Boolean | `true`  | Merge audio track with Reddit-hosted videos                                            |

### Example Input — Download from Post URLs

```json
{
  "postUrls": [
    "https://www.reddit.com/r/HPVictus/comments/1r62x2u/whatchall_think/"
  ],
  "quality": "best",
  "includeAudio": true
}
```

### Example Input — Scan a Subreddit

```json
{
  "subreddits": ["funny", "videos"],
  "maxVideos": 5,
  "sort": "top",
  "timeFilter": "week",
  "quality": "720"
}
```

## Output

Each downloaded video produces a structured JSON object with post metadata, video details, and a direct download link.

```json
{
  "post_id": "1r5zfwr",
  "title": "A Better Answer",
  "author": "PhoenixPhenomenonX",
  "subreddit": "funny",
  "subreddit_prefixed": "r/funny",
  "score": 3117,
  "num_comments": 67,
  "post_url": "https://www.reddit.com/r/funny/comments/1r5zfwr/a_better_answer/",
  "old_reddit_url": "https://old.reddit.com/r/funny/comments/1r5zfwr/a_better_answer/",
  "video_source_url": "https://v.redd.it/hux845hl6sjg1/HLSPlaylist.m3u8",
  "video_source": "reddit",
  "resolution": "720x1266",
  "download_status": "finished",
  "downloaded_at": "2026-02-16T07:09:23.309706+00:00",
  "download_url": "https://api.apify.com/v2/key-value-stores/.../records/video_1r5zfwr.mp4",
  "filename": "1r5zfwr.mp4",
  "storage_key": "video_1r5zfwr.mp4",
  "video_meta": {
    "width": 720,
    "height": 1266,
    "duration": 21.03,
    "fps": 30,
    "video_codec": "h264",
    "audio_codec": "aac",
    "ext": "mp4",
    "filesize_bytes": 6320220,
    "total_bitrate_kbps": 2404.27,
    "aspect_ratio": 0.57
  }
}
```

### Output Fields

| Field                | Type    | Description                                         |
| -------------------- | ------- | --------------------------------------------------- |
| `post_id`            | String  | Unique Reddit post identifier                       |
| `title`              | String  | Post title                                          |
| `author`             | String  | Reddit username of the poster                       |
| `subreddit`          | String  | Subreddit name                                      |
| `subreddit_prefixed` | String  | Subreddit with `r/` prefix                          |
| `score`              | Integer | Post score (upvotes minus downvotes)                |
| `num_comments`       | Integer | Number of comments on the post                      |
| `post_url`           | String  | Full URL to the Reddit post                         |
| `old_reddit_url`     | String  | Old Reddit URL for the post                         |
| `video_source_url`   | String  | Direct URL of the video source                      |
| `video_source`       | String  | Source type: `reddit`, `external`, or `fallback`    |
| `resolution`         | String  | Video resolution (e.g., `720x1266`)                 |
| `download_status`    | String  | Download result: `finished`, `failed`, or `error`   |
| `downloaded_at`      | String  | ISO 8601 timestamp of when the video was downloaded |
| `download_url`       | String  | Direct download link from Apify key-value store     |
| `filename`           | String  | Name of the downloaded video file                   |
| `storage_key`        | String  | Key-value store record key                          |
| `video_meta`         | Object  | Video metadata (see below)                          |

### Video Metadata (`video_meta`)

| Field                | Type    | Description                |
| -------------------- | ------- | -------------------------- |
| `width`              | Integer | Video width in pixels      |
| `height`             | Integer | Video height in pixels     |
| `duration`           | Float   | Duration in seconds        |
| `fps`                | Float   | Frames per second          |
| `video_codec`        | String  | Video codec (e.g., `h264`) |
| `audio_codec`        | String  | Audio codec (e.g., `aac`)  |
| `ext`                | String  | File extension             |
| `filesize_bytes`     | Integer | File size in bytes         |
| `total_bitrate_kbps` | Float   | Total bitrate in kbps      |
| `aspect_ratio`       | Float   | Width-to-height ratio      |

## Tips

- Start with 1–2 videos to verify your setup before scaling up
- Use `quality: "720"` or `"480"` for faster downloads and lower storage usage
- When scanning subreddits, combine `sort: "top"` with a `timeFilter` to find the most popular videos
- Each downloaded video is stored in the Apify key-value store and accessible via the `download_url` field

## Limitations

- Reddit may rate-limit or block automated access during high-volume scraping
- Some external video hosts (e.g., YouTube) may block downloads from datacenter IPs
- Video quality depends on what the original uploader provided
- Large videos consume Apify key-value store quota

## Support

For issues or feature requests, please reach out via the Apify platform.

---

**Built by [CrawlerBros](https://apify.com/crawlerbros)**

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/reddit-video-downloader)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
