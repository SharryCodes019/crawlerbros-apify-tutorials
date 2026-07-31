# Tumblr Posts Scraper Tutorial: Run This Apify Actor with Python

Scrape public Tumblr posts from any blog URL, search query, or tag. Returns blog name, post URL, date, tags, content text, note count, like/reblog counts, and media URLs. HTTP-only, no cookies, no login, no API key.

This repository shows how to run [Tumblr Posts Scraper](https://apify.com/crawlerbros/tumblr-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tumblr-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/tumblr-scraper](https://apify.com/crawlerbros/tumblr-scraper)
- **SEO title:** Tumblr Posts Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape public Tumblr posts from any blog URL, search query, or tag. Returns blog name, post URL, date, tags, content text, note count, like/reblog counts, and media URLs. HTTP-only, no cookies, no login, no API key.

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

# Tumblr Posts Scraper

Scrape public posts from any Tumblr blog, tag, or search page. HTTP-only — no cookies, no login, no API key input, no proxy required.

## What this actor does

Given a list of Tumblr URLs or a tag query, this actor extracts public post data including:

- Blog name, title, description, URL
- Post ID, URL, slug, post type
- Publish date (ISO-8601) and Unix timestamp
- Tags
- Note count (engagement)
- Content text (HTML stripped)
- Per-type fields: title + body (text), image URLs (photo), video source (video), quote text + source (quote), link URL (link), audio player (audio)
- Scrape timestamp

## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `startUrls` | string[] | At least one input required | Any mix of: `https://<blog>.tumblr.com`, `https://www.tumblr.com/<blog>`, `https://www.tumblr.com/tagged/<tag>`, `https://www.tumblr.com/search/<query>`, `https://<blog>.tumblr.com/tagged/<tag>`. |
| `searchQuery` | string | Optional | A tag or search term. Uses Tumblr's public tagged feed. Can be combined with `startUrls`. |
| `postType` | enum | No (default `any`) | Filter by post type: `any`, `text`, `photo`, `video`, `quote`, `link`, `audio`. Applies to blog URL scrapes. |
| `maxItems` | integer | No (default 50) | Maximum posts across all inputs (1-1000). |
| `country` | enum | No (default `us`) | Accept-Language hint (`us`, `gb`, `de`, `jp`). |

You must provide at least one of `startUrls` or `searchQuery`.

## Output

Every record is one post with at minimum:

- `type`: always `"tumblr_post"`
- `blogName`, `blogUrl`
- `postId`, `postUrl`, `postType`
- `date` (ISO-8601), `timestamp`
- `tags` (array, may be empty)
- `noteCount` (integer)
- `contentText` (stripped HTML, may be empty string for media-only posts)
- `scrapedAt`

Type-specific fields (emitted only when present): `title`, `bodyHtml`, `imageUrls`, `photoLinkUrl`, `videoSource`, `videoPlayer`, `quoteText`, `quoteSource`, `linkUrl`, `linkText`, `audioPlayer`, `question`.

## How it works (high level)

- **Blog URLs** hit Tumblr's legacy `/api/read/json` endpoint directly on the blog subdomain. No API key, no rate limit issues.
- **Tag / search queries** use Tumblr's public `api.tumblr.com/v2/tagged` endpoint with the official Tumblr demo API key.
- Requests impersonate Chrome TLS fingerprint via `curl_cffi` to avoid false-positive anti-bot blocks.

## FAQ

**Do I need a Tumblr API key?** No. The actor uses Tumblr's own published demo key, which is rate-limited but sufficient for typical search usage. For blog URLs the key is not used at all.

**Do I need a proxy?** No. Tumblr does not block datacenter IPs for these endpoints.

**Why does `maxItems` sometimes return fewer posts?** Some blogs have fewer posts than the requested limit, or the tag search hits its server-side cap before reaching your limit.

**Custom-domain blogs** (e.g. `humansofnewyork.com`) are not supported — Tumblr does not route their URL through the standard subdomain API. Use the underlying `<blog>.tumblr.com` form.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/tumblr-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
