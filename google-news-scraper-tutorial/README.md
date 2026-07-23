# Google News Scraper Tutorial: Run This Apify Actor with Python

Scrape Google News in real-time. Supports keyword search, date filters, full-text article extraction, and image extraction.

This repository shows how to run [Google News Scraper](https://apify.com/crawlerbros/google-news-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-news-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/google-news-scraper](https://apify.com/crawlerbros/google-news-scraper)
- **SEO title:** Google News Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Google News in real-time. Supports keyword search, date filters, full-text article extraction, and image extraction.

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

# Google News Scraper

Scrape Google News articles by keyword in real-time. Get headlines, full article text, images, and author information — all structured and ready to use. No proxy needed.

## What does Google News Scraper do?

This actor searches Google News for your keywords and returns structured article data. It resolves the actual article URLs (not Google redirect links), and can optionally extract the full article text and images from each page.

You can run multiple search queries in a single run. Results are automatically deduplicated across queries, so you never get the same article twice.

## What data can you extract?

| Field         | Description                                            |
| ------------- | ------------------------------------------------------ |
| `title`       | Article headline                                       |
| `url`         | Direct link to the article (resolved from Google News) |
| `source`      | Publisher name (e.g. BBC, Reuters, CNN)                |
| `domain`      | Publisher domain (e.g. bbc.com)                        |
| `publishedAt` | Publication date and time                              |
| `snippet`     | Short summary from Google News                         |
| `fullText`    | Full article body text (optional)                      |
| `imageUrl`    | Article hero image URL (optional)                      |
| `author`      | Article author name (optional)                         |
| `language`    | Language code used for the search                      |

## Use cases

- **Media monitoring** — Track news coverage of your brand, competitors, or industry topics across thousands of sources
- **Market research** — Collect news about specific markets, companies, or trends for analysis
- **Content aggregation** — Build news feeds or newsletters from curated topics and sources
- **Sentiment analysis** — Feed article text into NLP pipelines to gauge public sentiment on any topic
- **Academic research** — Gather news datasets filtered by date, region, and topic for studies
- **AI/LLM training data** — Extract full article text at scale for language model fine-tuning

## How to use it

1. **Add your search queries** — Enter one or more keywords (e.g. "artificial intelligence", "climate change")
2. **Set your filters** — Choose date range, language, country, or restrict to a specific site
3. **Choose what to extract** — Enable full-text extraction and/or image extraction if needed
4. **Run the actor** — Results appear in the dataset, ready to download as JSON, CSV, or Excel

## Input

| Field                | Type     | Default    | Description                                                     |
| -------------------- | -------- | ---------- | --------------------------------------------------------------- |
| `queries`            | string[] | _required_ | Search keywords — each query is processed separately            |
| `maxResultsPerQuery` | integer  | 20         | Maximum articles to return per query (1–100)                    |
| `language`           | string   | `en`       | Language code (e.g. `en`, `de`, `fr`, `es`, `ja`)               |
| `country`            | string   | `US`       | Country code (e.g. `US`, `GB`, `DE`, `IN`)                      |
| `dateRange`          | string   | `any`      | Filter by recency: `1h`, `6h`, `1d`, `7d`, `1m`, `1y`, or `any` |
| `dateFrom`           | string   | —          | Start date `YYYY-MM-DD` (overrides dateRange)                   |
| `dateTo`             | string   | —          | End date `YYYY-MM-DD`                                           |
| `siteFilter`         | string   | —          | Restrict to a domain (e.g. `reuters.com`, `bbc.com`)            |
| `excludeWords`       | string[] | `[]`       | Words or phrases to exclude from results                        |
| `extractFullText`    | boolean  | `false`    | Extract the full article body text                              |
| `includeImages`      | boolean  | `false`    | Extract the article's main image URL                            |
| `maxConcurrency`     | integer  | 5          | Parallel browser pages (1–20). Higher = faster but more memory  |

## Output example

Each item in the dataset represents one article:

```json
{
  "query": "artificial intelligence",
  "title": "AI Achieves New Milestone in Scientific Research",
  "url": "https://www.nature.com/articles/d41586-026-00123-4",
  "source": "Nature",
  "domain": "nature.com",
  "publishedAt": "2026-03-03T09:15:00+00:00",
  "snippet": "Researchers at MIT report a new breakthrough in machine learning...",
  "fullText": "Full article body text here...",
  "imageUrl": "https://nature.com/images/article-hero.jpg",
  "author": "Dr. Jane Smith",
  "language": "en",
  "scrapedAt": "2026-03-03T12:00:00.000000+00:00"
}
```

`fullText`, `imageUrl`, and `author` are `null` unless `extractFullText` / `includeImages` are enabled.

## Input examples

### Headlines only — quick scan of today's news

```json
{
  "queries": ["artificial intelligence", "climate change"],
  "maxResultsPerQuery": 20,
  "dateRange": "1d"
}
```

### Full articles with images

```json
{
  "queries": ["renewable energy"],
  "maxResultsPerQuery": 10,
  "extractFullText": true,
  "includeImages": true
}
```

### News from a specific site

```json
{
  "queries": ["technology"],
  "siteFilter": "bbc.com",
  "maxResultsPerQuery": 20
}
```

### Custom date range with exclusions

```json
{
  "queries": ["elections"],
  "dateFrom": "2026-01-01",
  "dateTo": "2026-02-28",
  "excludeWords": ["opinion", "editorial"],
  "maxResultsPerQuery": 50
}
```

### Non-English news

```json
{
  "queries": ["Nachrichten"],
  "language": "de",
  "country": "DE",
  "maxResultsPerQuery": 10
}
```

## Limitations

- **Paywalled articles** — Full-text extraction returns `null` for sites behind paywalls (e.g. NYTimes, WSJ)

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-news-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
