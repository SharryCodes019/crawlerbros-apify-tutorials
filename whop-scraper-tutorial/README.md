# Whop.com Scraper Tutorial: Run This Apify Actor with Python

Scrape Whop.com community listings by search query, category, or URL. Extracts id, title, route, verified, member count, reviews, creator pitch, owner, images. HTTP-only, no proxy.

This repository shows how to run [Whop.com Scraper](https://apify.com/crawlerbros/whop-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/whop-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/whop-scraper](https://apify.com/crawlerbros/whop-scraper)
- **SEO title:** Whop.com Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Whop.com community listings by search query, category, or URL. Extracts id, title, route, verified, member count, reviews, creator pitch, owner, images. HTTP-only, no proxy.

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

# Whop.com Scraper

Scrape public Whop.com community listings via search, category, or direct URL. HTTP-only — no cookies, no login, no proxy required.

## What this actor extracts

Per community:

- `id`, `title`, `route`, `url`
- `verified` status
- `memberCount`, `reviewsCount`, `reviewsAverage`
- `totalViews`
- `creatorPitch` (creator-written description)
- `createdAt`
- `logoUrl`, `bannerUrl`
- `owner` (id, username, name, avatarUrl)
- `scrapedAt`

## Input

| Field | Type | Description |
|---|---|---|
| `searchQueries` | string[] | List of search keywords. Each query returns up to 20 results (Whop server cap). |
| `startUrls` | string[] | Whop URLs: search pages, category pages, or direct community pages. |
| `category` | enum | Optional category (`trading`, `fitness`, `gaming`, etc.). When set, is added as an extra search query. |
| `maxItems` | integer | Maximum records across all inputs (default 50, cap 500). |

At least one of `searchQueries`, `startUrls`, or non-`any` `category` is required.

## How it works

Whop.com runs on Next.js 14 App Router with React Server Components (RSC). Passing the `rsc: 1` header to any page URL returns a `text/x-component` streaming response that contains server-rendered JSON for the page. We parse those line-by-line and collect community objects.

## Limitations

- **20 results per search query** — Whop's search endpoint server-renders only the first page. To get more results, use multiple search queries covering related terms.
- **Discover homepage / category pages with no query** return nothing server-side (they're client-side hydrated). The actor maps categories to search queries internally.
- **Custom domain communities** (e.g. third-party storefronts) are not supported.

## FAQ

**Do I need cookies / login?** No.

**Do I need a proxy?** No — the actor hardcodes Apify's RESIDENTIAL US proxy pool with per-request session rotation. Vercel rate-limits datacenter IPs so residential is mandatory and baked into the actor. No user configuration needed.

**Why only 20 per query?** Whop's frontend loads additional results via client-side XHR after hydration. A server-side scraper only gets the server-rendered batch.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/whop-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
