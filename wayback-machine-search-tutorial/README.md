# Wayback Machine Search Tutorial: Run This Apify Actor with Python

Query Internet Archive's Wayback Machine for historical snapshots of any URL or domain. Filter by date, HTTP status, MIME type, and deduplicate. Optionally fetch the archived page text. Free public CDX API, no authentication.

This repository shows how to run [Wayback Machine Search](https://apify.com/crawlerbros/wayback-machine-search) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/wayback-machine-search`
- **Apify Store:** [https://apify.com/crawlerbros/wayback-machine-search](https://apify.com/crawlerbros/wayback-machine-search)
- **SEO title:** Wayback Machine Search Tutorial: Run This Apify Actor with Python
- **Description:** Query Internet Archive's Wayback Machine for historical snapshots of any URL or domain. Filter by date, HTTP status, MIME type, and deduplicate. Optionally fetch the archived page text. Free public CDX API, no authentication.

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

# Wayback Machine Search

Query the Internet Archive's Wayback Machine for historical snapshots of any URL or domain — with flexible match modes, date and status filtering, content deduplication, and optional archived-text retrieval.

## What this actor does

The Internet Archive's Wayback Machine has captured trillions of web pages since 1996. This actor uses the Wayback Machine's free, public search API to enumerate every archived capture of a given URL or domain and return it as structured data — something the Wayback Machine's own browser UI can't easily do at scale.

You give the actor a URL and a match mode (exact URL, path prefix, full host, or entire domain) and it returns a row per archived snapshot with the capture timestamp, playback URL, HTTP status, MIME type, and content fingerprint. You can filter by date range, by HTTP status (e.g. find every archived 404 on a site), or by MIME type (e.g. enumerate every archived PDF). And because many pages are captured hundreds of times with identical content, the actor can deduplicate by content fingerprint so you get one row per *actual change*.

For historical-content research, the actor can optionally download each snapshot and extract the readable text of the archived page, giving you the raw material for diffs, longitudinal SEO studies, or training datasets.

## Key features

- Four URL match modes: `exact`, `prefix`, `host`, `domain`
- Date-range filtering (`YYYY`, `YYYYMM`, or `YYYYMMDD` precision)
- HTTP-status filtering — find every archived 200, 301, 404, etc.
- MIME-type filtering — restrict to `text/html`, `application/pdf`, images, and so on
- Content deduplication by fingerprint, or time-bucketing (one snapshot per month / day / hour)
- Optional archived-text retrieval — pull the readable text of selected snapshots
- No API key, no login, no proxy — the Wayback Machine's public search API is free and open
- Zero-null output — empty fields are omitted from each record

## Input

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `url` | string | — | **Required.** The URL or domain to look up (e.g. `apify.com`, `https://nytimes.com/2024/01/15/story.html`). |
| `matchType` | enum | `exact` | How to match the URL: `exact` (this URL only), `prefix` (URL and anything beneath it), `host` (same hostname only), `domain` (host plus all subdomains). |
| `dateFrom` | string | — | Earliest snapshot date, inclusive. Accepts `YYYY`, `YYYYMM`, or `YYYYMMDD`. |
| `dateTo` | string | — | Latest snapshot date, inclusive. Same formats. |
| `statusFilter` | string | — | Keep only snapshots with this HTTP status (e.g. `200`, `404`). |
| `mimeFilter` | string | — | Keep only snapshots with this MIME type (e.g. `text/html`, `application/pdf`). |
| `collapseBy` | enum | `digest` | `digest` (drop adjacent duplicates by content fingerprint), `monthly`, `daily`, `hourly`, or `none`. |
| `maxResults` | integer | `500` | Maximum snapshot records to return (1-10000). |
| `includeContent` | boolean | `false` | If `true`, download each snapshot and extract its readable text. |
| `maxContentFetch` | integer | `10` | When `includeContent` is on, cap the number of snapshots to download (0-500). |

**Example input — every HTML page ever archived under a domain, deduplicated**

```json
{
  "url": "example.com",
  "matchType": "domain",
  "mimeFilter": "text/html",
  "statusFilter": "200",
  "collapseBy": "digest",
  "maxResults": 2000
}
```

**Example input — track a single page through 2024 with monthly granularity**

```json
{
  "url": "https://news.ycombinator.com/",
  "matchType": "exact",
  "dateFrom": "2024",
  "dateTo": "2024",
  "collapseBy": "monthly"
}
```

**Example input — archive the readable text of a page across changes**

```json
{
  "url": "apify.com",
  "matchType": "exact",
  "includeContent": true,
  "maxContentFetch": 20,
  "collapseBy": "digest"
}
```

## Output

One record per snapshot:

```json
{
  "originalUrl": "https://apify.com/",
  "timestamp": "20240115123045",
  "archiveDate": "2024-01-15T12:30:45+00:00",
  "archiveUrl": "https://web.archive.org/web/20240115123045/https://apify.com/",
  "mimeType": "text/html",
  "statusCode": 200,
  "contentDigest": "SHA1:ABC123...",
  "contentLength": 45678,
  "content": "Apify is the platform where developers build, deploy, and publish...",
  "scrapedAt": "2026-04-24T12:00:00+00:00"
}
```

**Field descriptions**

- **`originalUrl`** — the URL that was archived
- **`timestamp`** — the Wayback Machine's raw capture timestamp (`YYYYMMDDHHMMSS`)
- **`archiveDate`** — ISO-8601 UTC rendering of `timestamp` for convenience
- **`archiveUrl`** — direct playback URL in the Wayback Machine viewer
- **`mimeType`** — MIME type reported when the snapshot was captured
- **`statusCode`** — HTTP status code at capture time
- **`contentDigest`** — content fingerprint (used for deduplication)
- **`contentLength`** — response body size in bytes
- **`content`** — extracted readable page text (only when `includeContent=true` and fetch succeeded; capped at 500 KB)
- **`scrapedAt`** — ISO timestamp of this run

If no snapshots match, a single diagnostic record is emitted with `type: "wayback_search_error"` and a `reason` of `no_snapshots`, `cdx_fetch_failed`, or `invalid_input`.

## Use cases

- **Content audit / SEO** — recover every historical version of a site's pages to diff copy, titles, or schema changes over time
- **Broken-link recovery** — enumerate every archived 404 on your domain so you can redirect or restore the missing URLs
- **Competitive intelligence** — see how a competitor's landing page, pricing, or product catalogue has evolved month by month
- **Journalism and due diligence** — reconstruct a web page, press release, or statement as it existed on a specific date
- **Training-data curation** — pull the text of older captures of reference sites for ML datasets

## FAQ

**Do I need a Wayback Machine account or API key?**
No. The Wayback Machine's search API is a free public endpoint. The actor uses no credentials.

**Does it use proxies?**
No. The search API works fine from Apify's datacenter IPs.

**What's the difference between `matchType=host` and `matchType=domain`?**
`host` matches one exact hostname — `www.example.com` won't return `blog.example.com`. `domain` matches that host *and* all of its subdomains (`blog.example.com`, `api.example.com`, and so on).

**Why is `collapseBy=digest` the default?**
Most pages are captured many times with identical content. Collapsing by fingerprint drops those duplicates so you get one record per *actual change* rather than hundreds of identical captures.

**When should I use the time-bucket collapses (`monthly` / `daily` / `hourly`)?**
Use these when you want an evenly-spaced sample over time — one snapshot per month is great for a long-term trend, one per day for detailed change tracking.

**Why does my record sometimes lack a `content` field?**
Either `includeContent` was off, `maxContentFetch` was exhausted, or the archived page replayed with a non-200 status. The actor never emits an empty `content` field.

**What are the rate limits?**
The Wayback Machine's search API doesn't publish a hard limit. The actor retries transient 429 / 5xx responses and paces archived-page downloads with a small polite delay.

**Can I search by keyword or full-text?**
No. The Wayback Machine's public search API works by URL, not full-text. Use the `includeContent` option to retrieve page text and then filter downstream.

## Known limitations

- **URL-based search only.** You can't query by keyword — only by URL, host, or domain.
- **Archive coverage is not complete.** Not every page on the internet is captured, and capture frequency varies wildly by site popularity.
- **`maxResults` is capped at 10,000.** For very large domains, narrow the scope with a date range or use more specific match types.
- **Archived text extraction** captures readable text only — not images, interactive widgets, or JavaScript-rendered content that wasn't present in the stored HTML.
- **Content is capped at 500 KB** per archived page to keep dataset rows manageable; anything longer is truncated.
- **Playback occasionally redirects.** When the Wayback Machine redirects a playback URL to a different snapshot, the `statusCode` field reflects the original capture status, not the redirect chain.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/wayback-machine-search)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
