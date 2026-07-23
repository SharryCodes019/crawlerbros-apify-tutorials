# Website Image Scraper Tutorial: Run This Apify Actor with Python

Extract every image URL from a website. Crawls the start page (and optionally internal links up to a configurable depth), parses `<img>` tags, `<picture>`/`<source>`, `srcset` candidates, and CSS `background-image` declarations. HTTP-only, no proxy or browser needed.

This repository shows how to run [Website Image Scraper](https://apify.com/crawlerbros/website-image-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/website-image-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/website-image-scraper](https://apify.com/crawlerbros/website-image-scraper)
- **SEO title:** Website Image Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract every image URL from a website. Crawls the start page (and optionally internal links up to a configurable depth), parses `<img>` tags, `<picture>`/`<source>`, `srcset` candidates, and CSS `background-image` declarations. HTTP-only, no proxy or browser needed.

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

# Website Image Scraper

Extract every image URL from a website. Crawls the start page (and optionally internal links up to a configurable depth), then parses `<img>` tags, `<picture>`/`<source>`, `srcset` candidates, `<link rel="icon">`, and CSS `background-image` declarations. HTTP-only — no browser, no proxy, no API key.

## What it does

- **Pull every image URL referenced on a page** — `<img src>`, lazy-loaded `data-src`, srcset candidates, picture sources, favicons, inline `style="background-image: url(...)"`.
- **Crawl deeper** — follow internal links up to `maxCrawlDepth` (same host only) to grab images from linked pages too.
- **Filter by format** — restrict to specific extensions (e.g. only SVG, only WebP/AVIF).
- **Bounded** — `maxImagesPerPage` and `maxTotalImages` keep runs cost-predictable on large galleries.

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `startUrl` | string (required) | `https://apify.com` | Page to start crawling. Must be `http://` or `https://`. |
| `maxCrawlDepth` | integer | `1` (0–5) | 0 = only the start URL; 1+ = follow internal links one level (same host only). |
| `maxImagesPerPage` | integer | `200` (1–5000) | Cap per page — keeps pathological galleries bounded. |
| `maxTotalImages` | integer | `1000` (1–50000) | Hard cap on total images emitted across the whole run. |
| `imageExtensions` | array | `[jpg, jpeg, png, gif, webp, svg, avif, bmp, ico]` | Only URLs whose path ends in one of these are kept. |
| `includeBackgroundImages` | boolean | `true` | Also extract from inline `style="background-image: url(...)"`. |
| `userAgent` | string | (Chrome 131) | Optional UA override. |

### Example input

```json
{
  "startUrl": "https://apify.com",
  "maxCrawlDepth": 1,
  "maxImagesPerPage": 200,
  "maxTotalImages": 500,
  "imageExtensions": ["jpg", "png", "webp", "svg"],
  "includeBackgroundImages": true
}
```

## Output

One record per unique image URL. Empty fields are omitted (no nulls).

```json
{
  "url": "https://apify.com/static/hero.jpg",
  "sourcePage": "https://apify.com/",
  "pageTitle": "Apify · The full-stack web-scraping & automation platform",
  "alt": "Apify hero image",
  "hasAltText": true,
  "title": "Apify",
  "width": 1200,
  "height": 600,
  "extension": "jpg",
  "discoveredVia": "img-tag",
  "mimeTypeHint": "image/jpeg",
  "crawlDepth": 0,
  "scrapedAt": "2024-12-16T14:23:11+00:00"
}
```

### Output fields

- **`url`** — absolute URL of the image (data: URIs and javascript: pseudo-URLs are filtered out).
- **`sourcePage`** — the page where the image was discovered.
- **`pageTitle`** — `<title>` of the page where the image was found (handy for grouping the dataset by page name).
- **`alt`** — `alt` attribute of the `<img>` tag (when present).
- **`hasAltText`** — derived boolean: `true` when `alt` is present and non-empty. Lets you filter accessibility issues without testing for field presence.
- **`title`** — `title` attribute (when present).
- **`width`** / **`height`** — explicit pixel dimensions from the tag (only emitted when numeric).
- **`extension`** — lowercase file extension parsed from the URL path (e.g. `"jpg"`, `"svg"`, `"webp"`). Useful for format-bucket aggregations.
- **`discoveredVia`** — one of `img-tag`, `srcset`, `picture-source`, `link-icon`, `css-background`.
- **`mimeTypeHint`** — derived from the file extension (e.g. `image/png`, `image/svg+xml`).
- **`crawlDepth`** — depth at which the page was crawled (0 = startUrl).
- **`scrapedAt`** — ISO-8601 timestamp.

## Use cases

- **Content audits** — see every image a website serves up, broken down by source (img tag vs CSS background).
- **Asset inventory** — pull all logos, hero images, and icons from a competitor or brand site.
- **Format migration** — find every JPEG/PNG to convert to WebP/AVIF, or every PNG to convert to SVG.
- **SEO / accessibility** — list images with `hasAltText: false` to flag accessibility issues at a glance.

## FAQ

**Does it download the image binaries?**
No. The actor only collects URLs and metadata. Combine with a separate downloader (or pipe URLs into Apify's standard "URL list" actor) if you need the bytes.

**Does it work on JavaScript-rendered pages?**
Mostly no. This scraper is HTTP-only — it sees the server-rendered HTML, not what runs after the page boots. If a site lazy-loads images via React/Vue, you may only see fallback / placeholder images. For SPA-rendered content, use a Playwright-based actor instead.

**Can I limit it to a single page?**
Set `maxCrawlDepth: 0`. Only the start URL is fetched.

**Does it follow external links?**
No. Internal-link crawling only follows links to the same host as `startUrl` to keep cost and scope bounded.

**What if the site has no images at all?**
You get a single sentinel record `{"type": "website_image_scraper_error", "reason": "no_images_found"}` so the dataset is non-empty. The run still completes successfully.

**How does it deduplicate?**
By absolute URL. The same image referenced from multiple pages produces one record (the first-seen page is recorded as `sourcePage`).

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/website-image-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
