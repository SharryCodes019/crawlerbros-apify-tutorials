# Medium Article Scraper Tutorial: Run This Apify Actor with Python

Scrape Medium articles by tag/topic, user, publication, or search query. Extracts title, author, tags, preview text, reading time, publish date, and paywall status all via public RSS feeds and metadata.

This repository shows how to run [Medium Article Scraper](https://apify.com/crawlerbros/medium-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/medium-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/medium-scraper](https://apify.com/crawlerbros/medium-scraper)
- **SEO title:** Medium Article Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Medium articles by tag/topic, user, publication, or search query. Extracts title, author, tags, preview text, reading time, publish date, and paywall status all via public RSS feeds and metadata.

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

# Medium Article Scraper

Scrape articles from [Medium](https://medium.com) by tag/topic, author, publication, keyword search, or a single article URL — all without authentication.

## Features

- **By Tag** — fetch latest articles for any Medium topic (programming, data-science, AI, and 16+ built-in tags, or any custom slug)
- **By User** — fetch all articles published by a Medium username
- **By Publication** — fetch articles from any Medium publication (e.g. `better-programming`, `towards-data-science`)
- **Search** — search Medium by keyword; supplements with tag-feed results for broader coverage
- **By URL** — extract metadata from a single Medium article URL
- Filter results by publish date, keyword match, and paywall status
- Detects member-only (paywalled) articles — never bypasses the paywall

## Output Fields

| Field | Type | Description |
|-------|------|-------------|
| `articleId` | string | Unique Medium article ID extracted from URL |
| `title` | string | Article title |
| `previewText` | string | First 300 chars of article preview/description |
| `authorName` | string | Author's display name |
| `authorUsername` | string | Medium username (without @) |
| `publicationName` | string | Publication name (if published under one) |
| `publicationSlug` | string | Publication URL slug |
| `publishedDate` | string | ISO-8601 publish date |
| `tags` | array | Article tags/categories |
| `readingTimeMinutes` | integer | Estimated reading time in minutes |
| `articleUrl` | string | Full article URL |
| `canonicalUrl` | string | Canonical URL (if different from articleUrl) |
| `isPaywalled` | boolean | Whether the article is member-only |
| `recordType` | string | Always `"article"` |
| `siteName` | string | Always `"Medium"` |
| `scrapedAt` | string | ISO-8601 scrape timestamp |

## Input Options

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `mode` | select | `byTag` | What to scrape: `byTag`, `byUser`, `byPublication`, `search`, `byUrl` |
| `tag` | select | `programming` | Tag slug for `byTag` mode (choose from 20 built-in tags or type custom) |
| `username` | string | — | Medium username for `byUser` mode |
| `publication` | string | — | Publication slug for `byPublication` mode |
| `query` | string | — | Search terms for `search` mode |
| `articleUrl` | string | — | Article URL for `byUrl` mode |
| `fromDate` | string | — | Only articles published on/after this date (ISO-8601) |
| `containsKeyword` | string | — | Case-insensitive keyword filter on title/preview |
| `excludePaywalled` | boolean | `false` | Skip member-only articles |
| `maxItems` | integer | `20` | Maximum articles to return (1–1000) |

## Example Use Cases

**Get latest programming articles:**
```json
{"mode": "byTag", "tag": "programming", "maxItems": 20}
```

**Get articles by a specific author:**
```json
{"mode": "byUser", "username": "towardsdatascience", "maxItems": 50}
```

**Get free articles about Python published in 2025:**
```json
{"mode": "byTag", "tag": "python", "fromDate": "2025-01-01", "excludePaywalled": true}
```

**Search for AI articles:**
```json
{"mode": "search", "query": "artificial intelligence", "maxItems": 30}
```

## FAQs

**Does this scrape paywalled article content?**
No. This actor only collects publicly available metadata (title, author, tags, preview text). Full article content for member-only posts is never extracted. Use `isPaywalled` to identify and filter such articles.

**How many articles are returned per tag/user?**
Medium RSS feeds typically return the latest 10–25 items. For more results, use the `search` mode which supplements with tag feed data.

**Why does search mode return fewer results than expected?**
Medium's public search does not expose a paginated JSON API. The actor uses HTML and tag feed supplementation to maximize results within Medium's public data surface.

**Is a Medium account required?**
No authentication or cookies are required.

**What tags are available in the dropdown?**
20 popular tags are in the dropdown (programming, data-science, AI, python, javascript, startup, etc.). You can also type any custom tag slug directly.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/medium-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
