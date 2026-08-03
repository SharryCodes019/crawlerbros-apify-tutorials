# Crunchbase News Scraper Tutorial: Run This Apify Actor with Python

Extract startup, funding, M&A, and tech news articles from news.crunchbase.com like title, content, author, date, categories, tags, featured image. Uses the public WordPress REST API. No proxy required.

This repository shows how to run [Crunchbase News Scraper](https://apify.com/crawlerbros/crunchbase-news-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/crunchbase-news-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/crunchbase-news-scraper](https://apify.com/crawlerbros/crunchbase-news-scraper)
- **SEO title:** Crunchbase News Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract startup, funding, M&A, and tech news articles from news.crunchbase.com like title, content, author, date, categories, tags, featured image. Uses the public WordPress REST API. No proxy required.

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

# Crunchbase News Scraper

Extract startup, funding, M&A, and tech news articles from **news.crunchbase.com** — Crunchbase's editorial news site with **8,500+ articles** covering venture capital, AI, startups, IPOs, and more. Returns full content, author, date, categories, tags, and featured image.

## Features

- **16 output fields** per article — flat schema with typed defaults (zero nulls)
- **8,500+ articles indexed** — going back years
- **Filter by keyword, category, or date**
- **Public WordPress REST API** — no authentication, no proxy, no cookies
- **Pagination** — walks pages until `maxItems` reached (100 per page)
- **Pre-resolved category and tag names** (not just IDs)

## Note on Crunchbase Data

The main `crunchbase.com` site (organization profiles, funding rounds, search) is gated behind login + Cloudflare and cannot be scraped without authenticated session cookies. This scraper instead targets `news.crunchbase.com`, which runs WordPress and exposes its content via the public REST API. The news site covers most of the same topics (funding rounds, M&A, IPOs, market analysis) as the gated database, just in editorial article form.

## Input

| Field | Type | Description |
|---|---|---|
| `search` | String | Free-text keyword (searches title + content) |
| `category` | String | Category slug to filter by (e.g., `venture`, `startups`, `ai`, `crypto`, `cybersecurity`, `ipo`, `ma`, `web3`, `saas`). Friendly aliases like `artificial-intelligence` → `ai` and `fintech` → `fintech-ecommerce` are also accepted. |
| `after` | String | Only articles published after this date (`YYYY-MM-DD` or ISO 8601) |
| `maxItems` | Integer | Maximum articles to return (default 50, max 1000) |

### Example Input

```json
{
    "search": "Series A",
    "category": "artificial-intelligence",
    "after": "2026-01-01",
    "maxItems": 100
}
```

## Output

Each article has **16 fields**. All fields are always present — empty strings, zero, or empty array as typed defaults, never `null`.

### Identity
| Field | Type | Description |
|---|---|---|
| `id` | Integer | Article ID |
| `url` | String | Full article URL |
| `slug` | String | URL slug |
| `title` | String | Article title (HTML stripped) |

### Content
| Field | Type | Description |
|---|---|---|
| `excerpt` | String | Short summary (HTML stripped, ~500 chars) |
| `content` | String | Full article content (HTML stripped, truncated to 5,000 chars) |

### Dates
| Field | Type | Description |
|---|---|---|
| `publishedDate` | String | Publication date (ISO 8601) |
| `modifiedDate` | String | Last modified date (ISO 8601) |

### Author & Taxonomy
| Field | Type | Description |
|---|---|---|
| `authorId` | Integer | Primary author ID |
| `authorName` | String | Primary author name |
| `categoryNames` | Array | Category names (e.g., `["AI", "Business"]`) |
| `categoryIds` | Array | Category IDs |
| `tagNames` | Array | Tag names |

### Media
| Field | Type | Description |
|---|---|---|
| `featuredImageUrl` | String | Featured image URL |
| `featuredImageId` | Integer | Featured image ID |

### Metadata
| Field | Type | Description |
|---|---|---|
| `scrapedAt` | String | ISO 8601 scrape timestamp |

## FAQ

**Q: Do I need a proxy?**
No. news.crunchbase.com runs WordPress and exposes its REST API publicly at `/wp-json/wp/v2/posts`. Works directly from datacenter IPs.

**Q: How many articles per page?**
100 (the WordPress API maximum). The scraper paginates automatically.

**Q: How do I find category slugs?**
Browse to news.crunchbase.com, click any category, and the URL is `/category/{slug}/`. Verified working slugs (by article volume): `venture`, `startups`, `business`, `ai`, `public`, `fintech-ecommerce`, `health-wellness-biotech`, `cybersecurity`, `transportation`, `clean-tech-and-energy`, `crypto`, `ma`, `data`, `liquidity`, `ipo`, `media-entertainment`, `seed`, `enterprise`, `agtech-foodtech`, `web3`, `real-estate-property-tech`, `semiconductors-and-5g`, `robotics`, `retail`, `saas`. Friendly aliases (`artificial-intelligence`, `fintech`, `health`, `m&a`, etc.) are auto-mapped to the canonical slug.

**Q: Can I get organization data (logos, funding rounds, etc.)?**
Not from this scraper. The main crunchbase.com database is gated. This actor scrapes the news site only. Use it when you need editorial commentary, market analysis, and funding-round summaries.

**Q: How fresh is the data?**
news.crunchbase.com publishes new articles daily. The WordPress API serves the live database — new articles appear within minutes of publication.

## Use Cases

- **Funding round monitoring** — track new VC deals via news coverage
- **Market analysis** — extract content from sector reports (AI, fintech, climate)
- **Competitive intelligence** — search for mentions of competitors / partners
- **Content syndication** — feed Crunchbase News into your own newsroom
- **Trend tracking** — aggregate by tag/category to identify rising topics

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/crunchbase-news-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
