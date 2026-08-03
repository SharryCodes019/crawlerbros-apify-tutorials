# RAG Web Browser Tutorial: Run This Apify Actor with Python

Search the web or fetch direct URLs and return clean markdown for LLM/RAG pipelines. filters: domainAllowlist/Blocklist, minTextLength, keywordsAnyOf. No login, no cookies.

This repository shows how to run [RAG Web Browser](https://apify.com/crawlerbros/rag-web-browser) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/rag-web-browser`
- **Apify Store:** [https://apify.com/crawlerbros/rag-web-browser](https://apify.com/crawlerbros/rag-web-browser)
- **SEO title:** RAG Web Browser Tutorial: Run This Apify Actor with Python
- **Description:** Search the web or fetch direct URLs and return clean markdown for LLM/RAG pipelines. filters: domainAllowlist/Blocklist, minTextLength, keywordsAnyOf. No login, no cookies.

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

# RAG Web Browser

Search the web (or fetch direct URLs) and return clean markdown ready for LLM/RAG pipelines. HTTP-first with `chrome131` TLS impersonation; Playwright fallback when needed. Pro filters narrow the result set to exactly what your retrieval index needs.

## What this actor does

- Sends a query to Google → extracts top organic results → fetches each → cleans HTML → emits structured records
- Or fetches direct URLs (`startUrls`) and skips Google entirely
- Strips boilerplate (nav, footer, ads, scripts) before extracting the main article
- Outputs `markdown` (default), plain `text`, and/or raw `html` per page
- Returns one clean record per page with title, description, language, word count, reading time

## Output per page

- `url`, `loadedUrl`, `domain`
- `title`, `description`, `languageCode`
- `text` (plain text) — when requested
- `markdown` (LLM-ready) — when requested
- `html` (raw cleaned HTML) — when requested
- `wordCount`, `readingTimeMinutes` (220 wpm)
- `httpStatusCode`, `loadedTime` (seconds)
- `searchRank` (1-based — when the URL came from Google search)
- `recordType: "page"`, `scrapedAt`

Empty fields are omitted from the output (no nulls).

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `query` | string | `"what is retrieval augmented generation"` | Search query OR a single URL |
| `startUrls` | array | `[]` | Direct URLs to fetch (skips Google search) |
| `maxResults` | int | `3` | Number of top organic Google results to fetch (1–100) |
| `outputFormats` | array | `["markdown"]` | Any combination of `markdown`, `text`, `html` |
| `requestTimeoutSecs` | int | `40` | Per-page HTTP timeout (1–300s) |
| `scrapingTool` | enum | `raw-http` | `raw-http` (curl_cffi) or `browser-playwright` |
| `removeElementsCssSelector` | string | nav/footer/aside/script/... | CSS selector(s) to strip before extraction |
| `htmlTransformer` | enum | `readable-text` | `readable-text` (main article) or `none` |
| `desiredConcurrency` | int | `5` | Parallel fetches (0 = auto) |
| `maxRequestRetries` | int | `2` | Retries on transient HTTP failures |
| `dynamicContentWaitSecs` | int | `5` | Wait time for JS content (browser mode only) |
| `removeCookieWarnings` | bool | `true` | Dismiss cookie/consent dialogs (browser mode) |
| `useApifyProxy` | bool | `true` | Route requests through Apify proxy |
| `domainAllowlist` | array | `[]` | Only emit pages whose host contains one of these substrings |
| `domainBlocklist` | array | `[]` | Drop pages whose host contains one of these substrings |
| `minTextLength` | int | – | Drop pages with fewer than N characters of extracted text |
| `excludeContentSelectors` | array | `[]` | Additional CSS selectors to strip |
| `keywordsAnyOf` | array | `[]` | Only emit pages containing at least one of these keywords |

### Example: search query

```json
{
  "query": "best vector database for RAG 2024",
  "maxResults": 5,
  "outputFormats": ["markdown"],
  "minTextLength": 500,
  "domainBlocklist": ["pinterest.com", "youtube.com"]
}
```

### Example: direct URLs

```json
{
  "startUrls": [
    "https://en.wikipedia.org/wiki/Retrieval-augmented_generation",
    "https://docs.langchain.com/docs/use-cases/qa/"
  ],
  "outputFormats": ["markdown", "text"],
  "htmlTransformer": "readable-text"
}
```

### Example: filter for relevance

```json
{
  "query": "vector embeddings tutorial",
  "maxResults": 10,
  "keywordsAnyOf": ["embedding", "vector", "similarity"],
  "minTextLength": 1000,
  "outputFormats": ["markdown"]
}
```

## Use cases

- **RAG ingestion** — pull fresh top-N Google results for a topic, hand markdown to your embedder
- **News briefings** — daily query like "AI news today", filter by `minTextLength` to drop SEO thin pages
- **Competitive monitoring** — `domainAllowlist` of competitor domains, scrape their blogs weekly
- **Reference enrichment** — feed each citation URL from a paper into the actor for clean text extraction
- **LLM context** — give an LLM the cleaned markdown of pages, not raw HTML, to save tokens

## FAQ

**Does it require a login or cookies?**  No. All fetches are anonymous.

**Is a proxy needed?**  Apify proxy is enabled by default to avoid Google rate-limits and unblock some target sites. You can disable it with `useApifyProxy: false`.

**What's the difference between `raw-http` and `browser-playwright`?**  Raw HTTP uses curl_cffi with chrome131 TLS impersonation — fast and works on ~80% of sites. Browser mode runs headless Chromium, waits for JS, and dismisses cookie banners — slower but handles SPAs.

**Why is `description` missing on some pages?**  Some pages don't expose a `<meta name="description">` or `og:description`. The omit-empty contract drops missing fields rather than emit nulls.

**Why does `markdown` look stripped down?**  We intentionally output simple markdown (headings, lists, links, emphasis, code) — RAG embedders strip most formatting anyway, and simpler markdown reduces token bloat.

**What if all my filters reject every result?**  The actor finishes cleanly with a status message instead of pushing placeholder rows.

**How do I use this with my LLM/RAG pipeline?**  Trigger this actor from your indexing job, read the dataset (each record has `url` + `markdown`), embed the markdown, store in your vector DB.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/rag-web-browser)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
