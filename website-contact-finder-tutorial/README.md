# Website Contact Finder Tutorial: Run This Apify Actor with Python

Crawl any website and extract emails, phone numbers, and social media profiles. Smart prioritisation of /contact, /about, /team pages. HTTP-only, no browser.

This repository shows how to run [Website Contact Finder](https://apify.com/crawlerbros/website-contact-finder) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/website-contact-finder`
- **Apify Store:** [https://apify.com/crawlerbros/website-contact-finder](https://apify.com/crawlerbros/website-contact-finder)
- **SEO title:** Website Contact Finder Tutorial: Run This Apify Actor with Python
- **Description:** Crawl any website and extract emails, phone numbers, and social media profiles. Smart prioritisation of /contact, /about, /team pages. HTTP-only, no browser.

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

# Website Contact Finder

Crawl any website and extract **emails**, **phone numbers**, and **social media profiles** (Facebook, Instagram, LinkedIn, Twitter/X, YouTube, TikTok, GitHub, Pinterest). HTTP-only — no browser, no login.

## What this actor extracts

- `websiteUrl` — normalised URL
- `emails` — unique list (placeholder / noreply / blacklisted domains filtered)
- `phones` — unique list (international-format filtered for noise)
- `socialLinks` — object with the first profile URL per platform
- `contactPageUrl` — direct link to the discovered contact page (if any)
- `pagesCrawled` — number of pages fetched
- `crawledAt` — ISO timestamp

## Input

| Field | Type | Description |
|---|---|---|
| `urls` | string[] | Sites to scan. Required. |
| `maxPagesPerSite` | integer | 1–200 (default 20). |
| `maxConcurrency` | integer | 1–20 parallel page fetches (default 5). |
| `requestTimeoutSecs` | integer | 5–60 per-page timeout (default 15). |
| `useProxy` | boolean | Toggle Apify RESIDENTIAL proxy for sites that block datacenter IPs. Default off. |
| `smartPrioritise` | boolean | Crawl `/contact`, `/about`, `/team` first. Default on. |

## How it works

1. Normalise each URL (`https://` prefix if missing).
2. Fetch the homepage via `curl_cffi` (Chrome-131 TLS fingerprint).
3. Extract `mailto:` + `tel:` + plain-text emails/phones + social-profile links.
4. Discover internal links; prioritise contact/about/team pages.
5. Continue fetching up to `maxPagesPerSite`, gathering data from each page.
6. Return one record per input URL with deduplicated results.

## Filters and quality

- Emails: blacklists placeholder domains (`example.com`, `yoursite.com`, etc.), known noreply locals, and file-like extensions (`.png@x2`, `.jpg`…).
- Phones: requires 7–20 digits, prefers international format.
- Socials: drops platform homepages, sharer links, and intent URLs.

## FAQ

**Do I need a proxy?** No — leave `useProxy=false`. Enable only for sites that serve 403 to datacenter IPs.
**Does it render JavaScript?** No — pure HTTP. Extract target info from server-rendered HTML / mailto-tel links.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/website-contact-finder)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
