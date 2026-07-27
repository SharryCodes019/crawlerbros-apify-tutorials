# Chrome Extensions Scraper Pro Tutorial: Run This Apify Actor with Python

Scrape any Chrome Web Store extension by URL, ID, category, search query, or top-charts. Pulls name, developer, ratings, install count, version, manifest, supported locales, related extensions. Pro filters: minRating, minInstalls, verifiedOnly, developerNameContains.

This repository shows how to run [Chrome Extensions Scraper Pro](https://apify.com/crawlerbros/chrome-extensions-scraper-pro) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/chrome-extensions-scraper-pro`
- **Apify Store:** [https://apify.com/crawlerbros/chrome-extensions-scraper-pro](https://apify.com/crawlerbros/chrome-extensions-scraper-pro)
- **SEO title:** Chrome Extensions Scraper Pro Tutorial: Run This Apify Actor with Python
- **Description:** Scrape any Chrome Web Store extension by URL, ID, category, search query, or top-charts. Pulls name, developer, ratings, install count, version, manifest, supported locales, related extensions. Pro filters: minRating, minInstalls, verifiedOnly, developerNameContains.

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

# Chrome Extensions Scraper Pro

Scrape any Chrome Web Store extension by URL, ID, category, search query, or top-charts category. Pulls every public field including ratings, install count, version, manifest details, supported locales, screenshots, and related extensions. Pro filters narrow the result set to exactly what you need.

## What it scrapes

For each Chrome Web Store extension the actor returns a clean record with:

- `extension_id`, `name`, `version`, `package_size`, `min_chrome_version`
- `rating` (0–5, four decimals), `rating_count`, `install_count`
- `category`, `category_group`
- `short_description`, `long_description`
- `developer`, `developer_email`, `verified_developer` (bool — D-U-N-S-verified business)
- `featured` (bool — Chrome Web Store "Featured" badge)
- `website_url` — developer's homepage (when listed)
- `manifest_version`, `permissions[]`, `host_permissions[]`
- `supported_languages[]` (display names), `supported_locales[]` (codes)
- `icon_url`, `cover_url`, `screenshots[]` (carousel image URLs)
- `bug_tracker_url`, `privacy_policy_url`
- `last_updated_at` (ISO 8601 UTC)
- `related_extensions[]` (id + name + icon, full list)
- `relatedExtensionIds[]` (flat ID list, capped at 10)

No null fields — only what the Chrome Web Store actually exposes for that extension.

## Input

| Field | Type | Description |
|---|---|---|
| `mode` | enum | `urls` (direct), `category` (walk a category page), `search` (search query), `topCharts` (popular by category) |
| `extensionUrls` | array | When `mode=urls`. Accepts full Chrome Web Store URLs or 32-char extension IDs. |
| `categoryUrls` | array | When `mode=category`. |
| `searchQuery` | string | When `mode=search`. |
| `topChartsCategory` | string | When `mode=topCharts`. Use the schema slug such as `productivity/tools`, `productivity/developer_tools`, `make_chrome_yours/accessibility`, or leave empty for the global top list. |
| `maxItems` | int | Cap on emitted records (1-5000, default 50). |
| `minRating` | number | Drop extensions with average rating below this value (0.0–5.0, e.g. `4.5`). |
| `minInstalls` | int | Drop extensions with fewer installs. |
| `verifiedOnly` | bool | Only emit extensions whose developer has the verified badge. |
| `developerNameContains` | string | Substring filter on developer name (case-insensitive). |

## Sample input

```json
{
  "mode": "urls",
  "extensionUrls": [
    "https://chromewebstore.google.com/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh"
  ],
  "maxItems": 1
}
```

## Sample output

```json
{
  "recordType": "extension",
  "extension_id": "ddkjiahejlhfcafbddmgiahcphecmpfh",
  "name": "uBlock Origin Lite",
  "version": "2024.10.30.1156",
  "rating": 4.4948,
  "rating_count": 2955,
  "install_count": 17000000,
  "developer": "Raymond Hill (gorhill)",
  "developer_email": "ubo@raymondhill.net",
  "category": "privacy",
  "category_group": "make_chrome_yours",
  "package_size": "9.17MiB",
  "min_chrome_version": "122.0",
  "manifest_version": 3,
  "permissions": ["activeTab", "declarativeNetRequest", "offscreen", "scripting", "storage", "userScripts"],
  "host_permissions": ["<all_urls>"],
  "supported_languages": ["English", "Deutsch", "Español", "..."],
  "supported_locales": ["en", "de", "es", "..."],
  "url": "https://chromewebstore.google.com/detail/ddkjiahejlhfcafbddmgiahcphecmpfh",
  "scrapedAt": "2026-04-29T12:00:00+00:00"
}
```

## Use cases

- **Competitive analysis** — pull all extensions in a category to study install + rating distribution
- **App-store optimisation** — track your competitor's version + manifest changes over time
- **Permissions audit** — list every extension whose `host_permissions` include `<all_urls>`
- **Developer outreach** — filter by `developerNameContains` to build a contact list
- **Install-leader research** — `minInstalls=1000000` to surface the top-tier extensions

## FAQ

**Does it require a login or cookie?** No. The Chrome Web Store is public and the actor uses HTTP-only requests.

**Is a proxy needed?** No. The actor runs from datacenter IPs without issue.

**What happens when an extension ID isn't found?** The actor skips it and finishes cleanly. If no extensions are found at all, the run status message explains what happened.

**What if all my Pro filters reject every result?** The run finishes without fake rows and sets a status message so you can loosen the filters.

**Can I scrape extensions by exact text in their description?** Use `mode: "search"` with the text as the query — Chrome's own search will rank by relevance.

**What does `topChartsCategory` expect?** Use the exact schema slug, not a human label. For example: `productivity/tools`, `productivity/communication`, or `make_chrome_yours/themes`.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/chrome-extensions-scraper-pro)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
