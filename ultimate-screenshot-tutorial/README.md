# Ultimate Website Screenshot / PDF / Video Tutorial: Run This Apify Actor with Python

Capture JPEG/PNG screenshots, PDFs, GIFs and MP4s of any website. 12+ device presets, full-page, custom viewport, scroll-to-bottom, cookie injection, proxy support.

This repository shows how to run [Ultimate Website Screenshot / PDF / Video](https://apify.com/crawlerbros/ultimate-screenshot) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/ultimate-screenshot`
- **Apify Store:** [https://apify.com/crawlerbros/ultimate-screenshot](https://apify.com/crawlerbros/ultimate-screenshot)
- **SEO title:** Ultimate Website Screenshot / PDF / Video Tutorial: Run This Apify Actor with Python
- **Description:** Capture JPEG/PNG screenshots, PDFs, GIFs and MP4s of any website. 12+ device presets, full-page, custom viewport, scroll-to-bottom, cookie injection, proxy support.

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

# Ultimate Website Screenshot, PDF, GIF and Video Capture

Capture any web page as a pixel-perfect **JPEG**, **PNG**, **PDF document**, animated **GIF**, or **MP4 video** — all from a single Apify actor, with 31 real device presets out of the box.

## What this actor does

Feed this actor one or more URLs and it loads each page in a real browser at the device and viewport you choose, then produces the capture in the format you need. Assets are stored in the run's key-value store and referenced in the dataset via a direct download link — ready to embed in reports, pipe into a CDN, or attach to a ticket.

It supports full-page captures that stitch the entire scrollable height (for images and PDFs), animated captures that scroll the page across frames (for GIF/MP4), and **31 device presets** covering everything from a 4K desktop monitor to an iPhone 15 Pro Max and a foldable Surface Duo. A custom viewport is also available if none of the presets match. Anti-bot resilience is built in: when a target page responds with a block/challenge page, the actor's **auto proxy fallback** detects it and silently retries the capture through a residential proxy session, so you get a real screenshot instead of a CAPTCHA image.

Everything is configurable — JPEG quality, PDF paper size and margins, navigation wait strategy, post-load delay, scroll-to-bottom behavior, cookie injection for session-walled pages, and MP4/GIF frame timing. The result is one consistent tool that replaces half a dozen specialized screenshot services.

## Key features

- **Five output formats** — JPEG, PNG, PDF, GIF, MP4.
- **31 device presets** — desktop monitors (1080p, 1440p, 4K), MacBook Pro 14/16, iPhone 13/14/15 families, Pixel phones, Galaxy phones, iPad Pro/Mini, Surface Duo, plus a Custom viewport option.
- **Full-page capture** that stitches the entire scrollable height for images and PDFs.
- **Animated captures** — GIF and MP4 with configurable frame count, interval, FPS, and scroll step per frame.
- **Scroll-to-bottom trigger** to force lazy-loaded images and content to render before capture.
- **Auto proxy fallback** — detects block/challenge pages and silently retries through a residential proxy so the run still produces a usable asset.
- **Cookie injection** for pages behind simple session walls.
- **Proxy support** (Apify Proxy or custom proxy URLs) for geo-specific or blocked pages.
- **Configurable waits** — `load`, `domcontentloaded`, or `networkidle`, plus a user-defined delay.
- **PDF controls** — A4 / Letter / Legal paper size, millimeter margins, background printing toggle.
- **Graceful degradation** — if MP4 encoding fails at runtime the actor falls back to a JPEG of the target page so your dataset is never empty.

## Input

| Field | Description |
|---|---|
| `linkUrls` | One or more `http`/`https` URLs to capture. |
| `outputFormat` | `jpeg`, `png`, `pdf`, `gif`, or `mp4`. |
| `device` | Any of the 31 presets, or `Custom` to use your own viewport. |
| `windowWidth` / `windowHeight` | Viewport size when `device` is `Custom`. |
| `fullPage` | Capture the entire scrollable page (applies to images + PDF). |
| `waitUntil` | Navigation wait strategy: `load`, `domcontentloaded`, or `networkidle`. |
| `timeoutSeconds` | Navigation timeout in seconds (1–120). |
| `delayBeforeScreenshotMs` | Extra wait after page load, in milliseconds (0–30000). |
| `scrollToBottom` | Scroll the page before capture to trigger lazy content. |
| `jpegQuality` | JPEG quality (1–100). |
| `pdfFormat` / `pdfPrintBackground` / `pdfMargin*` | Paper size, background toggle, margins (mm). |
| `videoFrameCount`, `videoFrameIntervalMs`, `videoFps`, `videoScrollStepPx` | Control GIF/MP4 length, timing, and scroll-per-frame. |
| `cookies` | Array of `{name, value, domain?}` cookies injected into the browser. |
| `enableSSL` | When `false` (default), invalid HTTPS certificates are ignored. |
| `autoProxyFallback` | When true (default), detect block/challenge pages and retry via residential proxy. |
| `proxyConfiguration` | Apify Proxy or custom proxy URLs. |

**Example input**

```json
{
  "linkUrls": [
    { "url": "https://news.ycombinator.com" },
    { "url": "https://example.com/pricing" }
  ],
  "outputFormat": "png",
  "device": "Desktop 1920x1080",
  "fullPage": true,
  "scrollToBottom": true,
  "waitUntil": "networkidle",
  "delayBeforeScreenshotMs": 1500,
  "autoProxyFallback": true
}
```

## Output

Each capture produces one dataset record:

```json
{
  "linkUrl": "https://example.com/pricing",
  "screenshotUrl": "https://api.apify.com/v2/key-value-stores/.../records/example-pricing.png",
  "storageKey": "example-pricing.png",
  "contentType": "image/png",
  "fileSizeBytes": 428913,
  "device": "Desktop 1920x1080",
  "viewportWidth": 1920,
  "viewportHeight": 1080,
  "format": "png",
  "capturedAtUTC": "2026-04-24T10:15:00+00:00"
}
```

**Field descriptions**

- `linkUrl` — the URL that was captured.
- `screenshotUrl` — direct download link to the captured asset in the run's key-value store.
- `storageKey` — key inside the run's key-value store (useful when referencing assets by convention).
- `contentType` — MIME type of the asset (`image/jpeg`, `image/png`, `application/pdf`, `image/gif`, `video/mp4`).
- `fileSizeBytes` — size of the stored asset in bytes.
- `device` — the device preset used (or `Custom`).
- `viewportWidth` / `viewportHeight` — actual viewport dimensions used for the capture.
- `format` — final format saved. May differ from the requested format if the MP4 fallback engaged.
- `capturedAtUTC` — ISO 8601 UTC timestamp of capture.

If a URL cannot be captured at all, a compact error record is written in its place with `type: screenshot_error` and a human-readable `message`, so your dataset is never silently empty.

## Use cases

- **Automated QA & visual regression** — screenshot every critical page in your marketing site across desktop + mobile presets on every deploy.
- **Archiving & compliance** — snapshot competitor pricing pages, regulated content, or legal notices as dated PDFs for record keeping.
- **Social media & preview cards** — generate high-DPI screenshots of pages to embed in blog posts, Slack threads, and Notion docs.
- **Marketing demos** — record short MP4/GIF walkthroughs of a web app scrolling through its home page for pitch decks and ads.
- **Accessibility & cross-device review** — compare how the same page renders across iPhone 15 Pro Max, Pixel 8, and a 4K desktop without owning the hardware.

## FAQ

**Can it capture sites that block bots?**
Yes in most cases. The actor uses a real browser with a realistic user agent and respects the `waitUntil` and `delayBeforeScreenshotMs` settings so content renders before capture. When a target page responds with a block/challenge page, `autoProxyFallback` (on by default) retries the capture through a residential proxy session automatically.

**How do I capture pages behind a login?**
Paste your session cookies as an array of `{name, value, domain?}` objects into the `cookies` field. If `domain` is omitted, the page's host is used.

**Does full-page capture work for every format?**
Full-page applies to image (JPEG/PNG) and PDF formats. GIF and MP4 capture the current viewport across a sequence of frames while scrolling, so they reflect real on-screen animation.

**What if MP4 encoding fails at runtime?**
The actor falls back to a JPEG of the target page and marks `format: "jpeg"` in the dataset record so your run still produces usable output rather than an error.

**What's the difference between `load`, `domcontentloaded`, and `networkidle`?**
`domcontentloaded` is fastest (fires once the HTML is parsed), `load` waits for images and subresources, and `networkidle` waits until there are no network requests for 500ms — best for JS-heavy apps but slowest.

**Will it capture every pixel of an infinite-scroll page?**
No tool can — infinite scroll has no end. Use `scrollToBottom` to trigger lazy-loading and set a reasonable page height cap via `videoFrameCount` (for MP4/GIF) to control how far the capture scrolls.

**Do I pay per screenshot?**
Pricing is set in the Apify UI, separate from the actor itself. Costs depend on run duration, compute, and whether you use residential proxy.

## Known limitations

- **Infinite-scroll feeds** (Twitter, TikTok) cannot be fully captured — full-page stitches only the currently-loaded DOM, not content that requires scrolling to materialize indefinitely.
- **DRM-protected video** (Netflix, DRM-locked streaming) cannot be recorded in MP4 captures — the browser blacks out protected frames.
- **CAPTCHA gates** that block all browser traffic (including real users) cannot be bypassed; those pages will be captured as-is or emit an error record.
- **Fixed-position headers/footers** can appear duplicated in full-page stitched screenshots on some sites — this is a common browser rendering limitation across all screenshot tools.
- **Large MP4 captures** (high frame count at high resolution) produce large files. Use reasonable `videoFrameCount` and `videoFps` values to keep storage manageable.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/ultimate-screenshot)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
