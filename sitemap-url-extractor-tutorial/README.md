# Sitemap URL Extractor Tutorial: Run This Apify Actor with Python

Extract every URL from any site's sitemap.xml with handles sitemap index files (nested sitemaps), gzipped sitemaps, and robots.txt discovery. Returns URL, lastmod, changefreq, priority, and optional image/video/alternate-language fields. No proxy, no cookies, no login.

This repository shows how to run [Sitemap URL Extractor](https://apify.com/crawlerbros/sitemap-url-extractor) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/sitemap-url-extractor`
- **Apify Store:** [https://apify.com/crawlerbros/sitemap-url-extractor](https://apify.com/crawlerbros/sitemap-url-extractor)
- **SEO title:** Sitemap URL Extractor Tutorial: Run This Apify Actor with Python
- **Description:** Extract every URL from any site's sitemap.xml with handles sitemap index files (nested sitemaps), gzipped sitemaps, and robots.txt discovery. Returns URL, lastmod, changefreq, priority, and optional image/video/alternate-language fields. No proxy, no cookies, no login.

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

# Sitemap URL Extractor — Pull Every URL From Any Website's Sitemap

Extract the complete URL inventory of any website in seconds — straight from its XML sitemap, no proxy or login required.

## What this actor does

Point this actor at a website and it returns every page URL that site publishes in its sitemap. You can pass a direct sitemap URL (`https://example.com/sitemap.xml`), a gzipped sitemap (`https://example.com/sitemap.xml.gz`), a sitemap index file that points at dozens of child sitemaps, or just a bare domain (`https://example.com`) and the actor will discover the sitemap for you via `robots.txt` and common fallback paths.

Behind the scenes the actor performs pure XML parsing over standard HTTP. It walks nested sitemap index files to any depth, decompresses gzipped sitemaps automatically, and preserves per-URL metadata such as last-modified dates, change frequency, priority, and image/video/hreflang annotations whenever the source sitemap includes them. Include and exclude regex filters let you narrow the output to just the section of the site you care about (e.g. only product pages, only blog posts).

Because sitemaps are public endpoints designed to be consumed by search engines, this actor runs without cookies, without proxies, and without any authentication — making it one of the cheapest and fastest ways to map a website end-to-end.

## Key features

- **Bare-domain auto-discovery** — pass `https://example.com` and the actor finds the sitemap via `robots.txt` and common paths (`/sitemap.xml`, `/sitemap_index.xml`).
- **Gzipped sitemap support** — `.xml.gz` files are decompressed transparently.
- **Recursive sitemap index walking** — nested sitemap trees are fetched and merged into a single flat list.
- **Image sitemap extraction** — preserves image URLs, captions, titles when the sitemap contains them.
- **Video & hreflang annotations** — kept per URL whenever the source exposes them.
- **Regex include / exclude filters** — trim the output to a specific section of the site.
- **Max URL cap** — stop early once you have enough data.
- **Public data only** — no proxy, no cookies, no login.

## Input

| Field | Type | Description |
|---|---|---|
| `startUrls` | array | One or more sitemap URLs, sitemap index URLs, `.xml.gz` URLs, or bare domains. |
| `maxUrls` | integer | Upper bound on total URLs returned. `0` means unlimited. |
| `followSitemapIndexes` | boolean | When true (default), nested sitemap index files are expanded recursively. |
| `urlFilterInclude` | string | Optional regex. Only URLs matching this pattern are kept. |
| `urlFilterExclude` | string | Optional regex. URLs matching this pattern are dropped. |

**Example input**

```json
{
  "startUrls": [
    { "url": "https://www.nytimes.com" },
    { "url": "https://example.com/sitemap.xml" }
  ],
  "maxUrls": 5000,
  "followSitemapIndexes": true,
  "urlFilterInclude": "/202[4-6]/",
  "urlFilterExclude": "/tag/|/category/"
}
```

## Output

Each dataset record represents one URL found in a sitemap:

```json
{
  "url": "https://example.com/products/red-shoes",
  "lastmod": "2026-03-12T08:14:00+00:00",
  "changefreq": "weekly",
  "priority": 0.8,
  "source": "https://example.com/sitemap-products.xml",
  "images": [
    { "loc": "https://example.com/img/red-shoes.jpg", "title": "Red Shoes" }
  ],
  "alternates": [
    { "hreflang": "de", "href": "https://example.com/de/schuhe-rot" }
  ]
}
```

**Field descriptions**

- `url` — the page URL listed in the sitemap.
- `lastmod` — last-modified timestamp reported by the sitemap, if present.
- `changefreq` — publisher-declared change frequency (`daily`, `weekly`, `monthly`, …).
- `priority` — publisher-declared priority hint (0.0–1.0).
- `source` — the sitemap file this URL was extracted from (useful with nested indexes).
- `images` — image sitemap entries attached to the URL (when present).
- `videos` — video sitemap entries attached to the URL (when present).
- `alternates` — `hreflang` alternate-language URLs (when present).

Empty or missing fields are omitted rather than emitted as `null`, so records stay compact.

## Use cases

- **SEO audits** — pull every indexable URL a site exposes, then cross-check against Google Search Console coverage.
- **Site migrations** — generate a full URL inventory before cutover to build redirect maps.
- **Competitive research** — map a competitor's product catalog, blog, or news archive.
- **Content crawling seed list** — feed the extracted URLs into a downstream scraper or LLM ingestion pipeline.
- **Broken-link discovery** — pair the URL list with a link checker to find 404s across large sites.

## FAQ

**Do I need a proxy?**
No. Sitemap endpoints are public and designed for consumption by search engines, so they do not gate by IP or require cookies.

**What if I only have a domain and don't know the sitemap URL?**
Pass the bare domain (`https://example.com`). The actor reads `robots.txt`, falls back to common sitemap paths, and walks any index files it finds.

**How does it handle very large sitemaps?**
Each sitemap file is streamed and parsed as it's received. Use `maxUrls` to cap the output when you do not need the entire site.

**Does it follow nested sitemap index files?**
Yes, by default. Set `followSitemapIndexes` to `false` to stop at the first level and receive only index entries.

**Can it extract images from image sitemaps?**
Yes. If the sitemap uses the `<image:image>` extension, the image entries are preserved on the per-URL record.

**Why is `lastmod` missing on some records?**
Sitemap fields are optional. If the publisher did not include a last-modified date for a URL, it is omitted from the output instead of padded with a placeholder.

**What happens if the sitemap URL returns a 404 or HTML page?**
The actor emits a compact error record describing the failure and continues with any other inputs. Your dataset is never silently empty.

## Known limitations

- **HTML-only websites with no sitemap** cannot be mapped. If `robots.txt` does not declare a sitemap and common fallback paths are empty, the actor has nothing to parse. Use a full crawler for those cases.
- **JavaScript-built sitemap pages** (rare — some single-page apps render `/sitemap` as HTML) are not XML and are not supported.
- **Extremely deep nested indexes** — sitemap trees are expanded recursively, but the total URL count is still bounded by `maxUrls` to keep runs predictable.
- **Sitemap accuracy depends on the publisher** — if the site forgets to list a URL in its sitemap, this actor cannot discover it (there is no HTML fallback crawling here by design).

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/sitemap-url-extractor)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
