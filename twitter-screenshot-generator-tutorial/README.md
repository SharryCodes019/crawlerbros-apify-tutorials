# Twitter Screenshot Generator Tutorial: Run This Apify Actor with Python

Take clean, high-quality screenshots of any public Twitter/X post. Just paste the post URLs, choose dark or light theme, and get back pixel-perfect PNG screenshots with direct download links - no login required.

This repository shows how to run [Twitter Screenshot Generator](https://apify.com/crawlerbros/twitter-screenshot-generator) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/twitter-screenshot-generator`
- **Apify Store:** [https://apify.com/crawlerbros/twitter-screenshot-generator](https://apify.com/crawlerbros/twitter-screenshot-generator)
- **SEO title:** Twitter Screenshot Generator Tutorial: Run This Apify Actor with Python
- **Description:** Take clean, high-quality screenshots of any public Twitter/X post. Just paste the post URLs, choose dark or light theme, and get back pixel-perfect PNG screenshots with direct download links - no login required.

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

# Twitter Screenshot Generator

Take clean, high-quality screenshots of any public Twitter/X post. Just paste the post URLs, choose dark or light theme, and get back pixel-perfect PNG screenshots with direct download links — no login required.

## What does Twitter Screenshot Generator do?

Twitter Screenshot Generator captures clean screenshots of tweets by opening each post in a browser, waiting for all media (images and videos) to fully load, hiding UI clutter like headers, login prompts, and community notes, then screenshotting just the tweet itself. You get a distraction-free image of the tweet at Full HD quality.

## Why use Twitter Screenshot Generator?

- **Save tweets as images** — Archive tweets before they get deleted or accounts go private
- **Content creation** — Embed tweet screenshots in presentations, blog posts, or videos
- **Social media management** — Capture competitor posts, track campaigns, or document conversations
- **Research & journalism** — Preserve tweets as visual evidence for reports and articles
- **No login needed** — Works with any public tweet without requiring a Twitter/X account

## Features

- Screenshot any public Twitter/X post
- Dark mode and light mode support
- Automatically hides UI overlays (headers, bottom bars, login prompts)
- Removes "Readers added context" community notes
- Waits for video media to fully load before capturing
- Automatically retries if media fails to load (clicks "Reload" button)
- Screenshots the tweet element only — no surrounding page clutter
- Full HD resolution (1920x1080 viewport)
- Direct download URLs for each screenshot via Apify key-value store

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `post_urls` | array of strings | Yes | - | List of Twitter/X post URLs to screenshot |
| `theme` | string | No | `"dark"` | Theme for screenshots: `"dark"` or `"light"` |

### Example Input

```json
{
    "post_urls": [
        "https://x.com/FCBarcelona/status/2031865446224261132",
        "https://x.com/TouchlineX/status/2031853496517943760"
    ],
    "theme": "dark"
}
```

Both `twitter.com` and `x.com` URLs are supported and automatically normalized.

## Output

Results are pushed to the default dataset. Each entry contains:

| Field | Type | Description |
|-------|------|-------------|
| `post_url` | string | The Twitter/X post URL that was processed |
| `status` | string | `"success"` or error details |
| `screenshot_key` | string | Filename of the screenshot in the key-value store |
| `download_url` | string | Direct URL to download the screenshot PNG |
| `scraped_at` | string | ISO timestamp of when the screenshot was taken |

### Example Output

```json
{
    "post_url": "https://x.com/FCBarcelona/status/2031865446224261132",
    "status": "success",
    "screenshot_key": "screenshot_2031865446224261132.png",
    "download_url": "https://api.apify.com/v2/key-value-stores/<store_id>/records/screenshot_2031865446224261132.png",
    "scraped_at": "2026-03-18T10:30:00.000000"
}
```

Screenshots are stored as PNG files in the Actor's default key-value store and can be downloaded via the `download_url` field.

## How much does it cost to use Twitter Screenshot Generator?

Twitter Screenshot Generator uses minimal compute and is very affordable to run on the Apify platform. The Actor processes each tweet sequentially with short delays between requests, so a typical run with a handful of tweets completes in under a minute.

## Is it legal to screenshot tweets?

Screenshotting publicly available tweets is generally considered fair use for personal, educational, journalistic, and research purposes. The Actor only accesses public posts — no login, scraping of private data, or terms-of-service circumvention is involved. Always check your local laws and Twitter/X's terms of service for your specific use case.

## FAQ

**Can I screenshot tweets from private accounts?**
No. This Actor only works with public tweets. Private or protected tweets are not accessible.

**Does it support tweet threads?**
Each URL is screenshotted individually. To capture a full thread, provide each tweet URL in the thread as a separate entry in `post_urls`.

**What happens if a tweet contains a video?**
The Actor waits for the video to fully load, then pauses it at the first frame to capture a clean thumbnail in the screenshot.

**What if the media fails to load?**
The Actor automatically detects and clicks the "Reload" button if media fails to load, then waits for the content to render before taking the screenshot.

**What resolution are the screenshots?**
Screenshots are taken at a 1920x1080 Full HD viewport. The actual image dimensions match the tweet element size, which varies depending on the tweet content.

**Can I use both twitter.com and x.com URLs?**
Yes. Both URL formats are supported and automatically normalized to x.com.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/twitter-screenshot-generator)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
