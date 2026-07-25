# Yandex Search Scraper Tutorial: Run This Apify Actor with Python

Scrape Yandex search results including organic results, ads, knowledge graph, inline images, and videos. Supports 17 regional domains, multiple languages, pagination, and time filters.

This repository shows how to run [Yandex Search Scraper](https://apify.com/crawlerbros/yandex-search-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/yandex-search-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/yandex-search-scraper](https://apify.com/crawlerbros/yandex-search-scraper)
- **SEO title:** Yandex Search Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Yandex search results including organic results, ads, knowledge graph, inline images, and videos. Supports 17 regional domains, multiple languages, pagination, and time filters.

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

# Yandex Search Scraper

Scrape Yandex search results across 17 regional domains. Returns structured data for organic results, ads, knowledge graph, inline images, videos, and related searches.

## What it does

Enter one or more search queries and the scraper returns full SERP data from Yandex, including organic results with positions, snippets, and thumbnails. Supports all major Yandex regional domains (Russia, Turkey, Germany, France, and 13 more), language settings, time filters, and pagination.

When a regional domain is blocked by SmartCaptcha (common on datacenter IPs), the scraper automatically falls back to a captcha-free domain while preserving regional targeting via Yandex's `lr` parameter.

## Input

| Field | Required | Default | Description |
|-------|----------|---------|-------------|
| **Search Queries** | Yes | - | One or more search terms to look up on Yandex |
| Yandex Domain | No | `yandex.com` | Regional domain (e.g. `yandex.ru`, `yandex.com.tr`, `yandex.de`) |
| Language | No | `en` | UI language code (e.g. `en`, `ru`, `tr`, `de`) |
| Region | No | - | Region filter: named shortcut (`ru`, `moscow`, `us`) or numeric Yandex region ID |
| Max Pages | No | 3 | Number of SERP pages to scrape per query (1-10) |
| Results Per Page | No | 10 | Organic results per page (10, 20, 30, or 50) |
| Time Filter | No | Any time | Filter by recency: Past day, week, month, or year |
| Disable Spell Correction | No | `false` | Prevent Yandex from auto-correcting your query |
| Proxy Configuration | No | Residential | Residential proxies recommended to avoid SmartCaptcha |

### Supported domains

| Domain | Region |
|--------|--------|
| `yandex.com` | International |
| `yandex.ru` | Russia |
| `yandex.com.tr` | Turkey |
| `yandex.by` | Belarus |
| `yandex.kz` | Kazakhstan |
| `yandex.uz` | Uzbekistan |
| `yandex.ua` | Ukraine |
| `yandex.fr` | France |
| `yandex.de` | Germany |
| `yandex.com.ge` | Georgia |
| `yandex.am` | Armenia |
| `yandex.az` | Azerbaijan |
| `yandex.md` | Moldova |
| `yandex.tj` | Tajikistan |
| `yandex.lt` | Lithuania |
| `yandex.lv` | Latvia |
| `yandex.ee` | Estonia |

### Example input

```json
{
    "searchQueries": ["machine learning", "python programming"],
    "yandexDomain": "yandex.com",
    "lang": "en",
    "maxPages": 2,
    "resultsPerPage": 10,
    "timeFilter": "any"
}
```

## Output

One dataset record is created per SERP page per query. Each record contains:

| Field | Description |
|-------|-------------|
| `query` | The search query |
| `page` | Page number (1-indexed) |
| `url` | The Yandex search URL used |
| `domain` | The actual domain used (may differ from requested if fallback occurred) |
| `lang` | Language code |
| `total_results_text` | Yandex's total result count text |
| `organic_results` | Array of organic search results |
| `ads_results` | Array of sponsored/ad results |
| `knowledge_graph` | Knowledge graph card (or `null`) |
| `inline_images` | Array of inline image thumbnails |
| `inline_videos` | Array of inline video cards |
| `related_searches` | Array of related search suggestions |
| `search_metadata` | Metadata about domain, language, and fallback status |
| `pagination_info` | Current page, has next page, results per page |
| `scraped_at` | ISO 8601 timestamp |

### Organic result fields

| Field | Example |
|-------|---------|
| `position` | `1` |
| `title` | `"Artificial Intelligence - Wikipedia"` |
| `link` | `"https://en.wikipedia.org/wiki/Artificial_intelligence"` |
| `displayed_link` | `"Wikipedia.org"` |
| `snippet` | `"AI is the simulation of human intelligence..."` |
| `favicon_url` | `"https://favicon.yandex.net/favicon/en.wikipedia.org"` |
| `date` | `"2025-12-01"` (or empty) |
| `thumbnail` | Image URL (or `null`) |
| `sitelinks` | Array of `{title, link}` sub-links |

### Ad result fields

| Field | Example |
|-------|---------|
| `position` | `1` |
| `title` | `"Best AI Course - Learn Now"` |
| `link` | `"https://example.com/ai-course"` |
| `displayed_link` | `"example.com"` |
| `snippet` | `"Start your AI journey today..."` |

### Knowledge graph fields

| Field | Example |
|-------|---------|
| `title` | `"Albert Einstein"` |
| `description` | `"German-born theoretical physicist..."` |
| `image_url` | `"https://avatars.mds.yandex.net/..."` |
| `source_url` | `"https://en.wikipedia.org/wiki/Albert_Einstein"` |
| `attributes` | `{"Born": "14 March 1879", "Died": "18 April 1955"}` |

### Related search fields

| Field | Example |
|-------|---------|
| `query` | `"machine learning vs deep learning"` |
| `link` | `"https://yandex.com.tr/search/?text=machine+learning+vs+deep+learning&noreask=1"` |

### Example output

```json
{
    "query": "artificial intelligence",
    "page": 1,
    "url": "https://yandex.com.tr/search/?text=artificial+intelligence&lang=en&numdoc=10",
    "domain": "yandex.com.tr",
    "lang": "en",
    "total_results_text": "182 bin sonuç bulundu",
    "organic_results": [
        {
            "position": 1,
            "title": "Artificial Intelligence - Wikipedia",
            "link": "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "displayed_link": "Wikipedia.org",
            "snippet": "Artificial intelligence is used in astronomy to analyze...",
            "favicon_url": "https://favicon.yandex.net/favicon/en.wikipedia.org",
            "date": "",
            "thumbnail": null,
            "sitelinks": []
        }
    ],
    "ads_results": [],
    "knowledge_graph": null,
    "inline_images": [],
    "inline_videos": [],
    "related_searches": [],
    "search_metadata": {
        "yandex_domain": "yandex.com",
        "domain_description": "International / English",
        "language": "en",
        "results_per_page": 10,
        "max_pages": 2,
        "fallback_domain": "yandex.com.tr"
    },
    "pagination_info": {
        "current_page": 1,
        "max_pages_set": 2,
        "has_next_page": true,
        "results_per_page": 10
    },
    "scraped_at": "2026-03-02T08:32:57.904000+00:00"
}
```

## Cost

This scraper uses Playwright (headless Chromium) to render Yandex search pages. A typical run with 2 queries and 3 pages each takes about 90 seconds and costs ~$0.03 in platform credits.

## Limitations

- **SmartCaptcha**: Yandex blocks most regional domains from datacenter IPs. The scraper automatically falls back to captcha-free domains (`yandex.com.tr`, `yandex.uz`) with region targeting. Residential proxies bypass this entirely.
- **Inline images/videos**: Yandex serves dedicated image and video wizard blocks inconsistently across domains and queries. These fields may be empty for some searches.
- **Results per page**: While the input accepts 10-50, Yandex may not honor values above 10 on all domains.
- **Rate limiting**: The scraper includes random delays between pages (2-4s) and queries (3-7s) to avoid triggering additional captchas.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/yandex-search-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
