# Pinterest Media Downloader Tutorial: Run This Apify Actor with Python

Download images and videos from Pinterest pins in bulk. Provide Pinterest pin URLs or search keywords to save all media files directly to your storage with download links.

This repository shows how to run [Pinterest Media Downloader](https://apify.com/crawlerbros/pinterest-media-downloader) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/pinterest-media-downloader`
- **Apify Store:** [https://apify.com/crawlerbros/pinterest-media-downloader](https://apify.com/crawlerbros/pinterest-media-downloader)
- **SEO title:** Pinterest Media Downloader Tutorial: Run This Apify Actor with Python
- **Description:** Download images and videos from Pinterest pins in bulk. Provide Pinterest pin URLs or search keywords to save all media files directly to your storage with download links.

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

# Pinterest Media Downloader

Download images and videos from Pinterest pins in bulk. Provide Pinterest pin URLs or search keywords to save all media files directly to your storage with download links.

## What does Pinterest Media Downloader do?

Pinterest Media Downloader lets you bulk download images and videos from Pinterest. It supports two input modes:

- **Pinterest URLs** - Provide direct pin URLs to download specific images or videos
- **Search Terms** - Enter keywords to search Pinterest and download media from all matching pins

All downloaded media files (images and videos) are stored in the Apify Key-Value Store. Each file gets a direct download URL in the dataset output, so you can easily access or integrate them into your workflow.

## Input

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `pinterestUrls` | Array of strings | List of Pinterest pin URLs to download media from | - |
| `searchTerms` | Array of strings | Keywords to search on Pinterest and download media | - |
| `maxItems` | Integer | Maximum number of media items to download per search term (0 = unlimited) | 50 |
| `proxy` | Object | Optional proxy configuration | - |

At least one of `pinterestUrls` or `searchTerms` must be provided.

### Input example

```json
{
    "pinterestUrls": [
        "https://www.pinterest.com/pin/123456789/",
        "https://www.pinterest.com/pin/987654321/"
    ],
    "searchTerms": [
        "aesthetic wallpapers",
        "cute cats"
    ],
    "maxItems": 50
}
```

## Output

Each downloaded media item produces a dataset entry with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `pinterest_url` | String | Original Pinterest pin URL |
| `media_type` | String | Type of media - `image` or `video` |
| `saved_as` | String | Filename in the Key-Value Store |
| `download_url` | String | Direct URL to download the media file from the API |

### Output example

```json
{
    "pinterest_url": "https://www.pinterest.com/pin/123456789/",
    "media_type": "image",
    "saved_as": "123456789.jpg",
    "download_url": "https://api.apify.com/v2/key-value-stores/<store-id>/records/123456789.jpg"
}
```

```json
{
    "pinterest_url": "https://www.pinterest.com/pin/987654321/",
    "media_type": "video",
    "saved_as": "987654321.mp4",
    "download_url": "https://api.apify.com/v2/key-value-stores/<store-id>/records/987654321.mp4"
}
```

## How to download Pinterest images

1. Go to [Pinterest Media Downloader](https://apify.com/valuable_harmonium/pinterest-media-downloader) on Apify
2. Add Pinterest pin URLs or enter search terms in the input
3. Click **Start** to run the actor
4. Once finished, download your media files from the **Key-Value Store** tab or use the direct download links provided in the dataset

## How to download Pinterest videos

The actor automatically detects whether a Pinterest pin contains a video or an image. Videos are downloaded in MP4 format at the highest available quality (up to 720p). Images are saved in their original format (typically JPG or PNG). Simply provide the pin URL and the actor handles the rest.

## How to bulk download Pinterest media by keyword

Enter one or more keywords in the `searchTerms` input field. The actor searches Pinterest for matching pins and downloads all images and videos from the results. Use `maxItems` to control how many items are downloaded per search term.

## Supported Pinterest URL formats

The actor supports standard Pinterest pin URLs including:
- `https://www.pinterest.com/pin/123456789/`
- `https://pinterest.com/pin/123456789/`
- Country-specific domains like `https://uk.pinterest.com/pin/123456789/`, `https://de.pinterest.com/pin/123456789/`

## Proxy configuration

This actor works without a proxy from datacenter IPs. If you experience rate limiting, you can configure Apify Proxy or custom proxies in the input settings.

## Integrations

Pinterest Media Downloader can be connected with other apps and services using Apify integrations. You can integrate with Make, Zapier, Slack, Airbyte, GitHub, Google Sheets, Google Drive, and many more. You can also use webhooks to trigger actions when the actor finishes running.

## FAQ

### Can I download both images and videos?
Yes, the actor automatically detects the media type for each pin and downloads both images and videos. Videos are saved as MP4 files and images in their original format (JPG, PNG).

### What image quality is downloaded?
The actor downloads the highest resolution available for each pin, typically the original upload resolution.

### What video quality is downloaded?
Videos are downloaded at the best available direct quality, typically 720p MP4. The actor prioritizes downloadable MP4 files over streaming formats.

### How many Pinterest images can I download at once?
You can download as many images as needed. Use the `maxItems` setting to control the number of downloads per search term. Set it to 0 for unlimited downloads.

### Where are the downloaded files stored?
All media files are stored in the Apify Key-Value Store associated with the actor run. Each file gets a direct download URL accessible via the Apify API or Console. Files are named using the Pinterest pin ID (e.g., `123456789.jpg` or `987654321.mp4`).

### Can I search for specific types of content?
Yes, use the `searchTerms` input to search for any keyword on Pinterest. You can provide multiple search terms to download media from different searches in a single run.

### Do I need a Pinterest account?
No, this actor works without any Pinterest account or login credentials. It only accesses publicly available content.

### Is there a limit on file size?
There is no specific file size limit. The actor downloads the full original media file for each pin, whether it's a small image or a large video.

### Can I use this actor with the Apify API?
Yes, you can start runs, retrieve datasets, and download individual media files from the Key-Value Store using the Apify API. Each dataset entry includes a `download_url` field for direct API access to the media file.

### What happens with NSFW content?
Pinterest enforces SafeSearch by default for unauthenticated access. Explicit search terms will return no results as Pinterest filters this content at the platform level.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/pinterest-media-downloader)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
