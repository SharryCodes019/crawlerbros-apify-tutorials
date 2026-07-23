# Traffic Generator Tutorial: Run This Apify Actor with Python

Generate realistic website traffic with human-like behavior simulation. Supports any website.

This repository shows how to run [Traffic Generator](https://apify.com/crawlerbros/traffic-generator) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/traffic-generator`
- **Apify Store:** [https://apify.com/crawlerbros/traffic-generator](https://apify.com/crawlerbros/traffic-generator)
- **SEO title:** Traffic Generator Tutorial: Run This Apify Actor with Python
- **Description:** Generate realistic website traffic with human-like behavior simulation. Supports any website.

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

# Traffic Generator

Generate realistic website traffic with human-like behavior simulation. Drive pageviews to any website, YouTube video, Etsy shop, or Behance profile. Each visit includes natural scrolling, mouse movements, variable dwell times, and browser fingerprint randomization to appear as genuine user traffic.

## What can this traffic generator do?

- **Simulate real traffic** -- Visit any URL with human-like browsing behavior including scrolling, mouse movements, and idle time
- **YouTube video views** -- Play YouTube videos with realistic viewing behavior and configurable watch duration
- **Crawl and browse** -- Follow links on target pages to simulate deeper browsing sessions across multiple pages
- **Fingerprint randomization** -- Each session uses a different browser fingerprint (user agent, viewport, timezone, WebGL parameters)
- **Stress testing** -- Rapid request mode for load testing your own websites
- **Resource blocking** -- Block ads and trackers for faster page loads and reduced bandwidth
- **Kill switch** -- Automatically stop after a set time limit to control costs
- **Detailed logging** -- Track every page visit with load times, scroll depth, and interaction metrics

## Use cases

- **SEO and analytics** -- Increase website traffic metrics for testing and validation
- **Load testing** -- Test how your website handles traffic using stress mode
- **YouTube creators** -- Generate views on YouTube videos
- **Etsy shop owners** -- Drive traffic to your Etsy shop listings
- **Behance designers** -- Increase portfolio views
- **Campaign testing** -- Verify analytics tracking is working before launching campaigns
- **Website monitoring** -- Regularly visit pages to check availability and performance

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `startUrls` | URL[] | Yes | -- | Target URLs to visit |
| `mode` | string | No | PAGEVIEW | PAGEVIEW (human simulation) or STRESS (rapid requests) |
| `enableCrawling` | boolean | No | false | Follow links on visited pages for deeper sessions |
| `crawlingLinkSelector` | string | No | `a[href]` | CSS selector for links to follow when crawling |
| `maxPagesPerUrl` | integer | No | 10 | Max pages per start URL when crawling (1-1,000) |
| `waitOnPage` | integer | No | 30 | Seconds to spend on each page (0-600, varies +/-20%) |
| `endAfterSeconds` | integer | No | 300 | Stop after N seconds (0 = unlimited) |
| `enableYoutube` | boolean | No | false | Enable YouTube video playback simulation |
| `blockResources` | string[] | No | -- | Additional URL patterns to block |
| `enableAdvancedFingerprinting` | boolean | No | true | Randomize browser fingerprint per session |
| `proxyConfiguration` | object | No | -- | Optional proxy settings for geographic targeting |

### Example input

```json
{
    "startUrls": [
        { "url": "https://example.com" },
        { "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ" }
    ],
    "mode": "PAGEVIEW",
    "waitOnPage": 30,
    "endAfterSeconds": 300,
    "enableCrawling": true,
    "maxPagesPerUrl": 5,
    "enableYoutube": true
}
```

```json
{
    "startUrls": [
        { "url": "https://www.etsy.com/shop/YourShopName" }
    ],
    "waitOnPage": 45,
    "endAfterSeconds": 600,
    "enableCrawling": true,
    "maxPagesPerUrl": 10
}
```

## Output

Each page visit produces a record in the dataset with these fields:

| Field | Type | Description |
|-------|------|-------------|
| `url` | string | URL of the visited page |
| `status` | string | Visit result: success, failed, blocked, or timeout |
| `pageTitle` | string | HTML title of the page |
| `loadTimeMs` | number | Page load time in milliseconds |
| `timeOnPageSec` | number | Seconds spent on the page |
| `scrollDepthPercent` | number | How far the page was scrolled (0-100) |
| `linksFound` | number | Links found on the page |
| `linksFollowed` | number | Links followed from this page |
| `referrer` | string | Previous page URL (empty for start URLs) |
| `userAgent` | string | User agent used for this visit |
| `viewport` | string | Viewport dimensions (e.g., 1920x1080) |
| `timestamp` | string | ISO 8601 timestamp of the visit |

### Sample output

```json
{
    "url": "https://example.com",
    "status": "success",
    "pageTitle": "Example Domain",
    "loadTimeMs": 342,
    "timeOnPageSec": 28.5,
    "scrollDepthPercent": 85,
    "linksFound": 1,
    "linksFollowed": 0,
    "referrer": "",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "viewport": "1920x1080",
    "timestamp": "2026-03-23T10:30:00.000000+00:00"
}
```

## How it works

1. Launches a real Chromium browser with stealth technology to avoid bot detection
2. Creates a unique browser fingerprint for each start URL (user agent, viewport, timezone, WebGL)
3. Visits each target URL and simulates human behavior: scrolling, mouse movements, link hovering
4. Spends the configured amount of time on each page with natural variation
5. Optionally follows links to simulate deeper browsing sessions
6. Records detailed metrics for every page visited
7. Stops automatically when the kill switch timer expires

## Tips for best results

- Start with a small number of URLs and short `endAfterSeconds` to test
- Use PAGEVIEW mode for realistic traffic; STRESS mode for load testing only
- Enable crawling to increase total page visits per start URL
- Adjust `waitOnPage` based on your needs: 10-30s for quick traffic, 60-120s for deep engagement
- Use proxy for websites that block datacenter IPs or for traffic from specific locations
- YouTube mode works best with `waitOnPage` set to the approximate video duration
- Block additional resources to speed up page loads when images and scripts are not needed

## Limitations

- The actor uses a real browser, so it consumes more compute than HTTP-only tools
- Some websites with advanced bot detection may still block visits
- YouTube view counting has anti-fraud systems; views may not always register in YouTube analytics
- Stress mode may trigger rate limiting on target websites
- The actor cannot solve CAPTCHAs

## Frequently Asked Questions

**Do I need a proxy?**
No. The actor works without proxy for most websites. Use proxy when target websites block datacenter IPs or when you need traffic from specific geographic locations.

**How many pages can it visit?**
In PAGEVIEW mode with 30-second dwell time, approximately 2 pages per minute per start URL. With crawling enabled and 10 maxPagesPerUrl, one start URL generates up to 10 page visits. In STRESS mode, it can process 50+ pages per minute.

**Does it work with YouTube?**
Yes. Enable the YouTube mode and set `waitOnPage` to the desired viewing duration. The actor plays the video and simulates watching behavior.

**Can I use it for Etsy?**
Yes. Provide your Etsy shop or listing URL as a start URL. Enable crawling to visit multiple product pages.

**What is the kill switch?**
The `endAfterSeconds` parameter automatically stops the actor after the specified time. This prevents runaway costs. Set to 0 for unlimited runtime (the actor will stop after processing all URLs).

**Does it store output data?**
Yes. Every page visit is recorded in the dataset with detailed metrics including load time, scroll depth, and interaction data.

**How is the human behavior simulated?**
Each visit includes random mouse movements, variable-speed scrolling to random depths, link hovering, and idle periods that simulate reading. Timing varies randomly so no two visits look identical.

**Can it follow links on the target website?**
Yes. Enable crawling mode to follow links on visited pages. You can specify a CSS selector to target specific links (e.g., `a.product-link`). Only same-domain links are followed.

**What is the difference between PAGEVIEW and STRESS mode?**
PAGEVIEW mode simulates realistic human browsing with scrolling, mouse movements, and dwell time. STRESS mode sends rapid requests with minimal delay, useful for load testing your own websites.

**Can I run multiple instances?**
Yes. You can start multiple runs of this actor simultaneously from the Apify platform to multiply traffic volume.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/traffic-generator)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
