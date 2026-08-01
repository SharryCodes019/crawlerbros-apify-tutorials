# Bing Search Scraper Tutorial: Run This Apify Actor with Python

Scrape Bing search results. Extract titles, URLs, descriptions, and snippets for any search query with market/language targeting.

This repository shows how to run [Bing Search Scraper](https://apify.com/crawlerbros/bing-search-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/bing-search-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/bing-search-scraper](https://apify.com/crawlerbros/bing-search-scraper)
- **SEO title:** Bing Search Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Bing search results. Extract titles, URLs, descriptions, and snippets for any search query with market/language targeting.

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

# Bing Search Scraper

Extract organic search results from Bing for any query. Get titles, URLs, descriptions, and snippets with support for 40+ markets and languages.

## Features

- Extract organic search results from Bing
- Get title, URL, description, and display URL for each result
- Support for 40+ markets/languages (en-US, fr-FR, de-DE, etc.)
- Configurable results per query (up to 100)
- Automatic pagination across multiple result pages
- No proxy required by default
- Fast HTTP-based extraction (no browser overhead)

## Input

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `queries` | Array | Required | Search queries to look up on Bing |
| `maxResultsPerQuery` | Integer | 10 | Max results per query (1-100) |
| `market` | String | "en-US" | Bing market code (e.g., "en-US", "fr-FR") |
| `proxyConfiguration` | Object | No proxy | Proxy configuration |

### Example Input

```json
{
    "queries": ["best restaurants NYC", "python web frameworks"],
    "maxResultsPerQuery": 20,
    "market": "en-US"
}
```

## Output

| Field | Type | Description |
|-------|------|-------------|
| `query` | String | Search query used |
| `position` | Integer | Position in results (1-based) |
| `title` | String | Result title |
| `url` | String | Result URL |
| `displayUrl` | String | Displayed URL text |
| `description` | String | Result snippet/description |
| `searchUrl` | String | Bing search URL used |
| `scrapedAt` | String | ISO timestamp when scraped |

## Use Cases

- **SEO monitoring** — track your website's ranking on Bing for target keywords
- **Competitor analysis** — discover who ranks for industry keywords
- **Content research** — find top-performing content for any topic
- **Market research** — analyze search landscapes across different markets
- **Lead generation** — find businesses and websites in specific niches

## FAQ

### Is a proxy required?

No. The scraper works without proxy by default. Enable proxy only if you experience rate limiting on high-volume runs.

### What markets are supported?

Bing supports 40+ market codes. Common ones: en-US, en-GB, fr-FR, de-DE, es-ES, it-IT, ja-JP, pt-BR, zh-CN, ko-KR, nl-NL, ru-RU, ar-SA.

### How many results can I get?

Up to 100 results per query with automatic pagination (10 results per page).

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/bing-search-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
