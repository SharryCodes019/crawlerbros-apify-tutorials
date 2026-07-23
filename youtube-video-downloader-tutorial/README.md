# Youtube Video Downloader Tutorial: Run This Apify Actor with Python

Download YouTube videos, playlists, and entire channels in your preferred quality from 360p all the way up to the best available resolution. Each downloaded video is automatically stored with a shareable public link and comes with rich metadata including title, description, view counts, thumbnails.

This repository shows how to run [Youtube Video Downloader](https://apify.com/crawlerbros/youtube-video-downloader) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/youtube-video-downloader`
- **Apify Store:** [https://apify.com/crawlerbros/youtube-video-downloader](https://apify.com/crawlerbros/youtube-video-downloader)
- **SEO title:** Youtube Video Downloader Tutorial: Run This Apify Actor with Python
- **Description:** Download YouTube videos, playlists, and entire channels in your preferred quality from 360p all the way up to the best available resolution. Each downloaded video is automatically stored with a shareable public link and comes with rich metadata including title, description, view counts, thumbnails.

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

# YouTube Video Downloader

Download YouTube videos, playlists, and entire channels in your preferred quality — from 360p all the way up to the best available resolution. Each downloaded video is automatically stored with a shareable public link and comes with rich metadata including title, description, view counts, thumbnails, and more.

## What can this actor do?

- **Download single or multiple videos** — paste one or more YouTube video URLs and get the video files with full metadata.
- **Download entire playlists** — provide a playlist URL and the actor downloads every video in it (up to your configured limit).
- **Download from channels** — provide a channel URL (e.g. `youtube.com/@ChannelName`) to grab the latest videos.
- **Choose your quality** — pick from Best Available, 1080p, 720p, 480p, 360p, Audio Only, or Lowest quality.
- **Extract audio only** — download just the audio track without the video.
- **Download subtitles** — grab caption files alongside your videos.
- **Get metadata without downloading** — retrieve video title, description, view count, likes, tags, and more without downloading the actual video file.
- **Geo-unblock videos** — select a proxy country to access region-restricted content.

## How to use

1. **Add your YouTube URLs** — paste video URLs, playlist URLs, or channel URLs into the corresponding input fields.
2. **Choose video quality** — select your preferred resolution from the dropdown (defaults to 720p).
3. **Configure options** — optionally enable subtitle downloads, set a max video limit for playlists/channels, or change the proxy country.
4. **Run the actor** — click Start and the actor will process each video, downloading and storing the files.
5. **Access your results** — find all downloaded videos and metadata in the dataset. Each successfully downloaded video includes a public download link.

## Input

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| **Video URLs** | `string[]` | `[]` | Direct YouTube video URLs to download |
| **Playlist URLs** | `string[]` | `[]` | YouTube playlist URLs — all videos in the playlist will be downloaded |
| **Channel URLs** | `string[]` | `[]` | YouTube channel URLs (e.g. `https://www.youtube.com/@ChannelName`) |
| **Video Quality** | `string` | `720p` | Preferred resolution: Best Available, 1080p, 720p, 480p, 360p, Audio Only, or Lowest |
| **Download Subtitles** | `boolean` | `false` | Download subtitle / caption files alongside the video |
| **Max Videos Per Playlist / Channel** | `integer` | `10` | Maximum number of videos to download per playlist or channel (1–500) |
| **Proxy Country** | `string` | `US` | Country for the proxy IP — change this if a video is geo-blocked in the default country |

### Example input

```json
{
    "videoUrls": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "videoQuality": "720p",
    "downloadSubtitles": false,
    "maxVideosPerInput": 10,
    "proxyCountry": "US"
}
```

## Output

Each video produces one record in the output dataset. Here is an example of a single output record:

```json
{
    "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "video_id": "dQw4w9WgXcQ",
    "title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
    "description": "The official video for Never Gonna Give You Up by Rick Astley...",
    "uploader": "Rick Astley",
    "uploader_id": "@RickAstleyYT",
    "uploader_url": "https://www.youtube.com/@RickAstleyYT",
    "upload_date": "2009-10-25",
    "duration_seconds": 212.0,
    "view_count": 1400000000,
    "like_count": 16000000,
    "comment_count": 2200000,
    "thumbnail": "https://api.apify.com/v2/key-value-stores/.../records/yt_dQw4w9WgXcQ_thumb.jpg",
    "tags": ["rick astley", "never gonna give you up", "80s"],
    "categories": ["Music"],
    "resolution": "1280x720",
    "filesize_bytes": 28491776,
    "download_status": "success",
    "download_url": "https://api.apify.com/v2/key-value-stores/.../records/yt_dQw4w9WgXcQ.mp4",
    "storage_key": "yt_dQw4w9WgXcQ.mp4",
    "subtitle_files": [],
    "subtitle_urls": [],
    "error": null,
    "downloaded_at": "2026-02-23T10:00:00Z"
}
```

### Output fields

| Field | Description |
| --- | --- |
| `video_url` | URL of the YouTube video |
| `video_id` | YouTube video ID |
| `title` | Title of the video |
| `description` | Video description (up to 2000 characters) |
| `uploader` | Channel or uploader name |
| `uploader_id` | Channel or uploader ID |
| `uploader_url` | URL of the uploader's channel |
| `upload_date` | Upload date (YYYY-MM-DD) |
| `duration_seconds` | Duration of the video in seconds |
| `view_count` | Number of views |
| `like_count` | Number of likes |
| `comment_count` | Number of comments |
| `thumbnail` | URL of the video thumbnail |
| `tags` | Tags associated with the video |
| `categories` | Categories associated with the video |
| `resolution` | Resolution of the downloaded video (e.g. 1920x1080) |
| `filesize_bytes` | File size of the downloaded video in bytes |
| `download_status` | Status: `success`, `failed`, or `metadata_only` |
| `download_url` | Public URL to download the video file |
| `storage_key` | Key of the video file in storage |
| `subtitle_files` | List of subtitle file keys |
| `subtitle_urls` | List of public URLs for subtitle files |
| `error` | Error message if the download failed |
| `downloaded_at` | Timestamp of when the download was processed |

## Use cases

- **Content archival** — back up your favorite YouTube videos or entire channels before they disappear.
- **Research and analysis** — collect video metadata (titles, descriptions, view counts, tags) at scale for content research, trend analysis, or competitive intelligence.
- **Media production** — download source material for editing, compilation, or repurposing (always respect copyright).
- **Subtitle extraction** — grab caption files for translation, accessibility, or content repurposing workflows.
- **Audio extraction** — download podcast episodes, music, or audio content from YouTube without the video.
- **Dataset building** — build structured datasets of YouTube video metadata for machine learning or analytics projects.

## FAQ

### How do I download a single YouTube video?

Paste the video URL into the **Video URLs** field and click Start. The actor will download the video and provide a public link to the file along with all available metadata.

### Can I download an entire YouTube playlist?

Yes. Paste the playlist URL into the **Playlist URLs** field. The actor will automatically expand the playlist and download each video. Use **Max Videos Per Playlist / Channel** to limit the number of videos.

### Can I download videos from a YouTube channel?

Yes. Paste the channel URL (e.g. `https://www.youtube.com/@ChannelName`) into the **Channel URLs** field. The actor will fetch the latest videos from that channel.

### What video qualities are available?

You can choose from: Best Available, 1080p, 720p, 480p, 360p, Audio Only (no video), or Lowest (fastest download). If the selected quality is not available for a particular video, the actor automatically falls back to the best available option.

### Can I download just the audio from a YouTube video?

Yes. Set the **Video Quality** to "Audio Only" and the actor will download only the audio track.

### Can I download subtitles?

Yes. Enable the **Download Subtitles** option and the actor will download available caption files alongside the video. Subtitle files are stored separately with their own public URLs.

### What if a video is geo-blocked in my region?

Change the **Proxy Country** setting to a country where the video is available. Supported countries include the United States, United Kingdom, Germany, France, Canada, Australia, Japan, India, Brazil, and Singapore.

### Where are the downloaded files stored?

Downloaded video files are uploaded to the Apify Key-Value Store. Each successfully downloaded video includes a `download_url` field in the output — this is a public link you can use to access the file directly.

### What happens if a download fails?

The output record for that video will have a `download_status` of `failed` along with an `error` field explaining what went wrong. The actor will continue processing the remaining videos.

### Can I get video metadata without downloading the actual file?

Yes. The actor always returns rich metadata for every video (title, description, view counts, likes, tags, upload date, etc.) regardless of whether the download succeeds or not.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/youtube-video-downloader)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
