# Website Content Crawler Tutorial: Run This Apify Actor with Python

Crawls websites and extracts clean text, markdown, or HTML content. Ideal for LLM training data, RAG pipelines, and knowledge base building.

This repository shows how to run [Website Content Crawler](https://apify.com/crawlerbros/website-content-crawler) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/website-content-crawler`
- **Apify Store:** [https://apify.com/crawlerbros/website-content-crawler](https://apify.com/crawlerbros/website-content-crawler)
- **SEO title:** Website Content Crawler Tutorial: Run This Apify Actor with Python
- **Description:** Crawls websites and extracts clean text, markdown, or HTML content. Ideal for LLM training data, RAG pipelines, and knowledge base building.

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

# Website Content Crawler

Crawl any website and extract clean **text**, **markdown**, or **HTML** content. Built for feeding data into LLMs, building RAG pipelines, creating knowledge bases, and powering AI-driven search.

## What does Website Content Crawler do?

This actor takes one or more URLs and crawls entire websites by following links. It extracts clean, readable content from every page — stripping navigation, scripts, footers, and other non-content elements. The output is optimized for use with large language models (LLMs) and retrieval-augmented generation (RAG) systems.

## Features

- **Deep website crawling** — Follows links across pages up to a configurable depth
- **Multiple output formats** — Get content as Markdown, plain text, or cleaned HTML
- **Smart content extraction** — Automatically removes navigation, scripts, footers, cookie banners, and other boilerplate
- **URL filtering** — Include or exclude pages using glob patterns (e.g., `https://example.com/blog/**`)
- **Configurable limits** — Control max pages, crawl depth, and concurrency
- **JavaScript rendering** — Uses a headless browser (Chromium or Firefox) to handle dynamic websites
- **Fast HTTP mode** — Optional raw HTTP mode for static sites that don't need JavaScript
- **No login required** — Works with publicly accessible pages

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `startUrls` | Array of URLs | Yes | — | One or more URLs to begin crawling from |
| `crawlerType` | String | No | `playwright:chromium` | Crawler engine: `playwright:chromium`, `playwright:firefox`, or `http` |
| `maxCrawlDepth` | Integer | No | 10 | Maximum link-following depth (0 = start URLs only) |
| `maxCrawlPages` | Integer | No | 100 | Total page limit |
| `maxConcurrency` | Integer | No | 5 | Number of pages loaded in parallel |
| `includeUrlGlobs` | Array of strings | No | [] | Only crawl URLs matching these glob patterns |
| `excludeUrlGlobs` | Array of strings | No | [] | Skip URLs matching these glob patterns |
| `outputFormat` | String | No | `markdown` | Output format: `markdown`, `text`, or `html` |
| `proxyConfiguration` | Object | No | — | Optional proxy settings |

### Example Input

```json
{
    "startUrls": [
        { "url": "https://docs.apify.com" }
    ],
    "maxCrawlPages": 50,
    "maxCrawlDepth": 3,
    "outputFormat": "markdown"
}
```

### URL Filtering Example

```json
{
    "startUrls": [
        { "url": "https://example.com" }
    ],
    "includeUrlGlobs": ["https://example.com/blog/**"],
    "excludeUrlGlobs": ["**login**", "**signup**"]
}
```

## Output

Each crawled page produces a result with the following fields.

| Field | Type | Description |
|-------|------|-------------|
| `url` | String | Original URL that was requested |
| `loadedUrl` | String | Final URL after any redirects |
| `title` | String | Page title |
| `description` | String | Meta description of the page |
| `languageCode` | String | Language code from the HTML lang attribute |
| `text` | String | Clean plain text extracted from the page |
| `markdown` | String | Page content converted to Markdown |
| `html` | String | Cleaned HTML content (when output format is HTML) |
| `depth` | Integer | Crawl depth (0 = start URL) |
| `httpStatusCode` | Integer | HTTP response status code |
| `loadedTime` | String | ISO 8601 timestamp when the page was loaded |
| `referrerUrl` | String | URL of the page that linked to this one |

### Example Output

```json
{
    "url": "https://docs.apify.com/academy/web-scraping-for-beginners",
    "loadedUrl": "https://docs.apify.com/academy/web-scraping-for-beginners",
    "title": "Web scraping for beginners | Apify Documentation",
    "description": "Learn how to build web scrapers from scratch.",
    "languageCode": "en",
    "text": "Web scraping for beginners\n\nThis course teaches you the basics of web scraping...",
    "markdown": "# Web scraping for beginners\n\nThis course teaches you the basics of web scraping...",
    "html": "",
    "depth": 1,
    "httpStatusCode": 200,
    "loadedTime": "2025-01-15T10:30:00.000Z",
    "referrerUrl": "https://docs.apify.com"
}
```

## Use Cases

- **LLM Training Data** — Crawl documentation sites, blogs, or knowledge bases to build training datasets
- **RAG Pipelines** — Extract and index website content for retrieval-augmented generation
- **Knowledge Base Building** — Convert entire websites into structured, searchable content
- **Content Migration** — Export website content as Markdown for migration to a new platform
- **Competitive Analysis** — Extract and compare content across competitor websites
- **SEO Auditing** — Crawl your site to analyze content, titles, and meta descriptions
- **Documentation Archival** — Create offline copies of documentation in clean text format

## FAQ

### What output format should I use for LLMs?

**Markdown** is the recommended format for LLM use cases. It preserves document structure (headings, lists, links) while remaining clean and readable. Use **text** if you need the simplest possible format with no formatting.

### How many pages can I crawl?

You can crawl up to 100,000 pages per run. The default limit is 100 pages. Adjust the `maxCrawlPages` setting based on your needs and available compute.

### What's the difference between Chromium and HTTP mode?

**Chromium** (default) uses a headless browser that renders JavaScript, making it work with modern dynamic websites. **HTTP mode** fetches raw HTML without running JavaScript — it's much faster but only works with static (server-rendered) pages.

### Does the crawler follow links to other domains?

No. The crawler only follows links within the same domain as the start URL. This prevents accidentally crawling the entire internet.

### How does URL filtering work?

Use **includeUrlGlobs** to restrict crawling to specific sections of a site (e.g., `https://example.com/docs/**`). Use **excludeUrlGlobs** to skip certain pages (e.g., `**login**`, `**.pdf`). Glob patterns use standard wildcard matching where `*` matches anything within a path segment and `**` matches across segments.

### Does it handle JavaScript-rendered content?

Yes. The default Chromium mode renders JavaScript before extracting content. This means Single Page Applications (SPAs), React sites, and other dynamic pages are fully supported.

### How clean is the extracted content?

The crawler automatically removes navigation menus, headers, footers, scripts, styles, cookie banners, and other non-content elements. The resulting text or markdown contains only the main page content.

### Can I crawl password-protected pages?

No. This crawler works with publicly accessible pages only. It does not support login or authentication.

### What happens if a page fails to load?

Failed pages are logged and skipped. The crawler continues with the remaining URLs. Check the run log for details on any failures.

### Does the crawler respect robots.txt?

The headless browser mode does not explicitly check robots.txt. If you need to respect robots.txt restrictions, review the site's rules before crawling.

### What output formats are available for export?

Results can be exported as JSON, CSV, Excel (XLSX), HTML, RSS, or XML directly from the Apify platform.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/website-content-crawler)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
