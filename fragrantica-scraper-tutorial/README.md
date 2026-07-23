# Fragrantica Perfume Scraper Tutorial: Run This Apify Actor with Python

Extract perfume data from Fragrantica.com like name, brand, year, perfumer, fragrance pyramid (top/middle/base notes), main accords, ratings, and reviews. No proxy required.

This repository shows how to run [Fragrantica Perfume Scraper](https://apify.com/crawlerbros/fragrantica-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/fragrantica-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/fragrantica-scraper](https://apify.com/crawlerbros/fragrantica-scraper)
- **SEO title:** Fragrantica Perfume Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract perfume data from Fragrantica.com like name, brand, year, perfumer, fragrance pyramid (top/middle/base notes), main accords, ratings, and reviews. No proxy required.

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

# Fragrantica Perfume Scraper

Extract perfume data from **Fragrantica.com** — the world's largest perfume database. Returns name, brand, year, perfumer, full fragrance pyramid (top/middle/base notes), main accords, and aggregated ratings.

## Features

- **17 output fields** per perfume — flat schema with typed defaults (zero nulls)
- **Two input modes** — direct perfume URLs, or designer pages (auto-expanded)
- **Full fragrance pyramid** — top notes, middle/heart notes, base notes
- **Main accords** with rankings
- **Ratings** — average value + total count
- **Perfumer (nose) names** extracted from the description
- **Launch year**
- **Gender classification** (for women / for men / unisex)
- **DataDome bypass** via curl_cffi Chrome 131 + RESIDENTIAL/US proxy (hardcoded, applied automatically). Sessions rotate on failure.

## Input

| Field | Type | Description |
|---|---|---|
| `perfumeUrls` | Array | Direct perfume URLs (e.g., `https://www.fragrantica.com/perfume/Chanel/Coco-Mademoiselle-611.html`) |
| `designerUrls` | Array | Designer/brand pages (e.g., `https://www.fragrantica.com/designers/Chanel.html`) — automatically expanded to all perfumes from that brand |
| `maxItems` | Integer | Maximum perfumes to return (default 20, max 500) |

### Example Input

Single perfume:
```json
{
    "perfumeUrls": [
        "https://www.fragrantica.com/perfume/Chanel/Coco-Mademoiselle-611.html"
    ],
    "maxItems": 1
}
```

Brand catalog:
```json
{
    "designerUrls": [
        "https://www.fragrantica.com/designers/Tom-Ford.html"
    ],
    "maxItems": 50
}
```

## Output

Each perfume has **17 fields**. All fields are always present — empty strings, zero, or empty array as typed defaults, never `null`.

### Identity
| Field | Type | Description |
|---|---|---|
| `id` | Integer | Fragrantica perfume ID |
| `url` | String | Perfume page URL |
| `name` | String | Perfume name |
| `brand` | String | Brand / designer |
| `fullName` | String | Full title (Name + Brand + gender) |
| `gender` | String | `for women`, `for men`, or `for women and men` |
| `year` | Integer | Launch year |

### Composition
| Field | Type | Description |
|---|---|---|
| `perfumers` | Array | Perfumer / nose names |
| `topNotes` | Array | Top notes |
| `middleNotes` | Array | Middle / heart notes |
| `baseNotes` | Array | Base notes |
| `allNotes` | Array | All notes combined |
| `mainAccords` | Array | Main accord names (e.g., `floral`, `woody`, `citrus`) |

### Ratings & Media
| Field | Type | Description |
|---|---|---|
| `ratingValue` | Number | Average user rating (1-5 scale) |
| `ratingCount` | Integer | Total number of ratings |
| `imageUrl` | String | Cover image URL |

### Metadata
| Field | Type | Description |
|---|---|---|
| `scrapedAt` | String | ISO 8601 scrape timestamp |

## FAQ

**Q: Do I need a proxy?**
No configuration needed — a US residential proxy is hardcoded and applied automatically. Fragrantica is fronted by DataDome which blocks Apify datacenter IPs with `403`. The scraper combines RESIDENTIAL/US traffic with curl_cffi Chrome 131 TLS impersonation, with automatic session rotation on each failed attempt (up to 5 retries per URL).

**Q: How do I find a designer URL?**
The format is `https://www.fragrantica.com/designers/{Brand-Name}.html` (e.g., `Chanel.html`, `Tom-Ford.html`, `Dior.html`). Spaces become hyphens.

**Q: How many perfumes per brand?**
Major brands like Chanel and Dior have 150-300 perfumes. The scraper expands the designer page and scrapes up to `maxItems` perfumes.

**Q: How fresh is the data?**
Fragrantica updates ratings and reviews continuously — new data is reflected within hours.

## Use Cases

- **Perfume market research** — track new launches by brand or accord
- **E-commerce enrichment** — pull perfume metadata for product catalogs
- **Accord analysis** — find perfumes with specific note combinations
- **Rating aggregation** — compare brands by average ratings
- **Recommendation systems** — match perfumes by shared notes / perfumers

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/fragrantica-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
