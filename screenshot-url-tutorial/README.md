# Website Screenshot Generator Tutorial: Run This Apify Actor with Python

Capture full-page screenshots of any website as PNG images or PDF documents. Supports custom viewport, scroll-to-bottom, element hiding, and configurable wait conditions.

This repository shows how to run [Website Screenshot Generator](https://apify.com/crawlerbros/screenshot-url) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/screenshot-url`
- **Apify Store:** [https://apify.com/crawlerbros/screenshot-url](https://apify.com/crawlerbros/screenshot-url)
- **SEO title:** Website Screenshot Generator Tutorial: Run This Apify Actor with Python
- **Description:** Capture full-page screenshots of any website as PNG images or PDF documents. Supports custom viewport, scroll-to-bottom, element hiding, and configurable wait conditions.

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

# Screenshot URL

Capture full-page screenshots of any website as PNG images or PDF documents. Supports custom viewport sizes, scroll-to-bottom for lazy-loaded content, element hiding, and configurable wait conditions.

## What can this actor do?

- **Full-page screenshots** -- Capture entire web pages as PNG images or PDF documents
- **Custom viewport** -- Set browser width from 100px to 3840px to test responsive layouts
- **Scroll to bottom** -- Trigger lazy-loaded images and infinite scroll content before capturing
- **Hide elements** -- Remove cookie banners, popups, and ads using CSS selectors
- **Wait conditions** -- Wait for page load, DOM ready, or network idle before capturing
- **Custom delay** -- Add delay after page load for animations or dynamic content
- **Redirect tracking** -- Records the final URL after any redirects
- **Bulk capture** -- Process multiple URLs in a single run
- **PDF export** -- Generate printable PDF documents from web pages

## Use cases

- **Website monitoring** -- Schedule regular screenshots to track visual changes over time
- **Quality assurance** -- Verify website appearance across different viewport widths
- **Archiving** -- Save snapshots of web pages for records or compliance
- **Competitive analysis** -- Capture competitor websites for design comparison
- **Bug reporting** -- Generate visual evidence of display issues
- **Content verification** -- Confirm that published content appears correctly

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `urls` | URL[] | Yes | -- | Web page URLs to screenshot |
| `format` | string | No | `png` | Output format: `png` or `pdf` |
| `waitUntil` | string | No | `load` | Page load event: `load`, `domcontentloaded`, or `networkidle` |
| `delay` | integer | No | 0 | Delay before screenshot in milliseconds (0--3,600,000) |
| `viewportWidth` | integer | No | 1280 | Browser viewport width in pixels (100--3,840) |
| `scrollToBottom` | boolean | No | false | Scroll to bottom before screenshot |
| `delayAfterScrolling` | integer | No | 2500 | Delay after scrolling in milliseconds (0--3,600,000) |
| `waitUntilNetworkIdleAfterScroll` | boolean | No | false | Wait for network idle after scrolling |
| `waitUntilNetworkIdleAfterScrollTimeout` | integer | No | 30000 | Network idle timeout in milliseconds (1,000--3,600,000) |
| `proxyConfiguration` | object | No | -- | Proxy settings (optional) |
| `selectorsToHide` | string | No | -- | CSS selectors to hide before screenshot (comma-separated) |

### Example input

```json
{
    "urls": [
        {"url": "https://www.example.com"},
        {"url": "https://news.ycombinator.com"}
    ],
    "format": "png",
    "waitUntil": "networkidle",
    "viewportWidth": 1920
}
```

```json
{
    "urls": [
        {"url": "https://www.wikipedia.org"}
    ],
    "format": "pdf",
    "scrollToBottom": true,
    "selectorsToHide": ".cookie-banner, #popup"
}
```

## Output

Each URL produces one row in the dataset with a link to the screenshot file stored in the key-value store.

| Field | Type | Description |
|-------|------|-------------|
| `startUrl` | string | The original URL provided as input |
| `url` | string | The final URL after any redirects |
| `screenshotUrl` | string | Public URL to download the screenshot file |
| `screenshotKey` | string | Key name in the key-value store |
| `format` | string | Screenshot format (`png` or `pdf`) |
| `status` | string | `success` or error description |
| `timestamp` | string | ISO 8601 timestamp |

### Sample output

```json
{
    "startUrl": "https://www.example.com",
    "url": "https://www.example.com/",
    "screenshotUrl": "https://api.apify.com/v2/key-value-stores/STORE_ID/records/screenshot_https___www_example_com__abc123.png",
    "screenshotKey": "screenshot_https___www_example_com__abc123.png",
    "format": "png",
    "status": "success",
    "timestamp": "2026-03-23T12:00:00.000000+00:00"
}
```

## How it works

1. Launches a Chromium browser with the configured viewport width
2. Navigates to each URL and waits for the specified load condition
3. Optionally scrolls to the bottom to trigger lazy-loaded content
4. Optionally hides specified elements (cookie banners, popups, ads)
5. Captures a full-page screenshot as PNG or generates a PDF document
6. Stores the screenshot file in the key-value store with a public download URL
7. Records the result in the dataset with the original URL, final URL, and screenshot link

## Tips for best results

- Use `networkidle` for `waitUntil` on pages with heavy JavaScript rendering
- Enable `scrollToBottom` for pages with lazy-loaded images or infinite scroll
- Use `selectorsToHide` to remove cookie consent banners and popups: `.cookie-banner, #consent-popup, .ad-wrapper`
- Set a `delay` of 1000-3000ms for pages with entrance animations
- Use wider `viewportWidth` (1920) for desktop-optimized pages, or 375 for mobile views
- The actor works without proxy for most websites; enable proxy only if needed

## Limitations

- Some websites may block screenshots from datacenter IPs. Use proxy configuration for these sites
- Very long pages may produce large PNG files. Consider using PDF format for document-heavy pages
- JavaScript-heavy single-page applications may need `networkidle` wait condition and additional delay
- The actor cannot log into websites or handle authentication
- PDF format uses the browser's print layout, which may differ from the visual page appearance

## Frequently Asked Questions

**Do I need a proxy?**
No. The actor works without proxy for most publicly accessible websites. Only enable proxy if the target site blocks datacenter IPs.

**What is the difference between PNG and PDF?**
PNG captures a full-page screenshot as an image, including everything visible when scrolled. PDF generates a printable document using the browser's print functionality, which may paginate content differently.

**How do I hide cookie banners?**
Use the `selectorsToHide` field with CSS selectors. For example: `.cookie-banner, #gdpr-consent, [class*="cookie"]`.

**What viewport height is used?**
The viewport height is fixed at 1080px. The screenshot captures the full page length regardless of viewport height.

**How does scroll-to-bottom work?**
The actor scrolls the page in 250px increments, triggering lazy-loaded images and content. After scrolling, it waits for the configured delay or network idle before taking the screenshot.

**Can I screenshot multiple pages in one run?**
Yes. Add multiple URLs to the input. Each URL produces a separate screenshot and dataset row.

**Where are the screenshot files stored?**
Screenshots are stored in the run's key-value store. Each dataset row includes a `screenshotUrl` field with a direct download link.

**Can I take mobile screenshots?**
Yes. Set `viewportWidth` to a mobile width like 375 or 390 to simulate a mobile browser viewport.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/screenshot-url)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
