# Google Scholar Scraper Tutorial: Run This Apify Actor with Python

Scrape academic papers, articles, and citations from Google Scholar. Search by keywords with filters for year range, document type, sort order, and article type. Extract titles, authors, citations, links, and more.

This repository shows how to run [Google Scholar Scraper](https://apify.com/crawlerbros/google-scholar-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-scholar-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/google-scholar-scraper](https://apify.com/crawlerbros/google-scholar-scraper)
- **SEO title:** Google Scholar Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape academic papers, articles, and citations from Google Scholar. Search by keywords with filters for year range, document type, sort order, and article type. Extract titles, authors, citations, links, and more.

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

# Google Scholar Scraper

Extract academic papers, research articles, and citation data from Google Scholar. Search by keywords with filters for year range, document type, sort order, and article type — no login or API key required. A powerful Google Scholar API alternative for researchers, academics, and data analysts.

## What can this scraper do?

- **Search by keywords** — Enter any research topic and get structured data for each result
- **Filter by year range** — Limit results to specific publication years
- **Sort by relevance or date** — Choose how results are ordered
- **Filter by document type** — Get only PDF or HTML documents
- **Filter by article type** — Search for review articles specifically
- **Extract citation data** — Get citation counts with links to citing articles
- **Pagination support** — Automatically fetch multiple pages of results

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| **Search Queries** | string[] | Yes | — | Keywords to search on Google Scholar |
| Max Results | integer | No | 100 | Maximum articles per query (1–1,000) |
| Sort By | enum | No | Relevance | Sort by relevance or publication date |
| Document Format | enum | No | All | Filter: all formats, PDF only, or HTML only |
| Article Type | enum | No | Any | Filter: all types or review articles only |
| Published After | integer | No | — | Only articles from this year onward |
| Published Before | integer | No | — | Only articles up to this year |
| Proxy Configuration | object | No | — | Proxy settings (often not needed) |

### Example input

```json
{
    "queries": ["machine learning", "deep learning"],
    "maxItems": 50,
    "sortBy": "relevance",
    "newerThan": 2020
}
```

```json
{
    "queries": ["cancer treatment review"],
    "maxItems": 30,
    "articleType": "review",
    "filter": "pdfOnly"
}
```

## Output

Each row in the dataset represents one academic article or paper found in search results.

### Output fields

| Field | Type | Example |
|-------|------|---------|
| `title` | string | `"Deep Learning"` |
| `link` | string | `"https://link.springer.com/article/..."` |
| `documentLink` | string | `"https://example.com/paper.pdf"` |
| `documentType` | string | `"PDF"`, `"HTML"`, or empty |
| `authors` | string | `"Y LeCun, Y Bengio, G Hinton"` |
| `publication` | string | `"Nature"` |
| `year` | integer | `2015` |
| `source` | string | `"springer.com"` |
| `fullAttribution` | string | `"Y LeCun, Y Bengio, G Hinton - Nature, 2015 - springer.com"` |
| `searchMatch` | string | Snippet or excerpt from the article |
| `citations` | integer | `65432` |
| `citationsLink` | string | Link to view all citing articles |
| `relatedArticlesLink` | string | Link to related articles on Scholar |
| `versions` | integer | `12` |
| `versionsLink` | string | Link to all versions of this article |
| `type` | string | `"ARTICLE"` or `"CITATION"` |
| `resultIndex` | integer | `0` (position in results) |
| `searchQuery` | string | `"deep learning"` |
| `scrapeTimestamp` | string | `"2026-03-09T12:00:00+00:00"` |

### Sample output

```json
{
    "title": "Deep Learning",
    "link": "https://www.nature.com/articles/nature14539",
    "documentLink": "https://creativecoding.soe.ucsc.edu/courses/cs523/slides/week3/DeepLearning_LeCun.pdf",
    "documentType": "PDF",
    "authors": "Y LeCun, Y Bengio, G Hinton",
    "publication": "Nature",
    "year": 2015,
    "source": "nature.com",
    "fullAttribution": "Y LeCun, Y Bengio, G Hinton - Nature, 2015 - nature.com",
    "searchMatch": "Deep learning allows computational models composed of multiple processing layers to learn representations of data...",
    "citations": 65432,
    "citationsLink": "https://scholar.google.com/scholar?cites=...",
    "relatedArticlesLink": "https://scholar.google.com/scholar?q=related:...",
    "versions": 12,
    "versionsLink": "https://scholar.google.com/scholar?cluster=...",
    "type": "ARTICLE",
    "resultIndex": 0,
    "searchQuery": "deep learning",
    "scrapeTimestamp": "2026-03-09T12:00:00+00:00"
}
```

## FAQs

### Do I need a Google Scholar account?

No. Google Scholar is publicly accessible and the scraper works without any authentication.

### Do I need a proxy?

Often not. Google Scholar is more accessible than regular Google Search from datacenter IPs. Try running without a proxy first. If you get blocked (CAPTCHA), enable Apify proxy.

### How many results can I get?

Up to 1,000 results per search query. Google Scholar shows 10 results per page, and the scraper automatically paginates through multiple pages.

### Can I filter by publication year?

Yes. Use the **Published After** and **Published Before** fields to limit results to a specific year range. For example, set "Published After" to 2020 to get only recent articles.

### What is the difference between "link" and "documentLink"?

- **link** is the main article URL (journal page, abstract, etc.)
- **documentLink** is a direct link to the document file (PDF or HTML) when available

### What does the "citations" field contain?

The number of times this article has been cited by other papers, as reported by Google Scholar. The `citationsLink` field provides a direct link to see all citing articles.

### Can I search for review articles only?

Yes. Set the **Article Type** to "Review articles only" to filter results to review papers.

### What is the "type" field?

Results are either `"ARTICLE"` (full papers with links) or `"CITATION"` (references without direct links, typically older works only available as citations).

## Limitations

- Google Scholar may show CAPTCHA for high-volume requests from datacenter IPs — use proxy if this happens
- Maximum 1,000 results per query (Google Scholar pagination limit)
- Year filters are not effective when sorting by date
- Citation counts and version numbers are as reported by Google Scholar and may not be perfectly up-to-date
- The scraper extracts publicly visible search results only

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-scholar-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
