# DoorDash Restaurant Scraper Tutorial: Run This Apify Actor with Python

Extract restaurant info + complete menus from DoorDash store pages like name, address, cuisine, breadcrumbs, FAQ, and full menu sections with item names, descriptions, and prices.

This repository shows how to run [DoorDash Restaurant Scraper](https://apify.com/crawlerbros/doordash-restaurant-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/doordash-restaurant-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/doordash-restaurant-scraper](https://apify.com/crawlerbros/doordash-restaurant-scraper)
- **SEO title:** DoorDash Restaurant Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract restaurant info + complete menus from DoorDash store pages like name, address, cuisine, breadcrumbs, FAQ, and full menu sections with item names, descriptions, and prices.

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

# DoorDash Restaurant Scraper

Extract restaurant info + complete menus from **DoorDash** store pages — restaurant name, address, city, cuisine breadcrumbs, FAQ, and full menu sections with item names, descriptions, and prices.

## Features

- **16 output fields** per restaurant — flat schema with typed defaults (zero nulls)
- **Complete menu extraction** — every section + item with name, description, and price
- **FAQ extraction** — questions and answers about the restaurant
- **Breadcrumb extraction** — cuisine type and neighborhood
- **Cloudflare bypass** via Patchright Chromium + RESIDENTIAL US proxy (typically clears in 2–15 seconds)
- **Hardcoded RESIDENTIAL US proxy** — required, applied automatically

## Input

| Field | Type | Description |
|---|---|---|
| `storeUrls` | Array | DoorDash store URLs (e.g., `https://www.doordash.com/store/15034`) |
| `maxItems` | Integer | Maximum restaurants to scrape (default 10, max 100) |

### Example Input

```json
{
    "storeUrls": [
        "https://www.doordash.com/store/15034",
        "https://www.doordash.com/store/6422"
    ],
    "maxItems": 10
}
```

## Output

Each restaurant has **16 fields**. All fields are always present — empty strings, zero, or empty array as typed defaults, never `null`.

### Identity
| Field | Type | Description |
|---|---|---|
| `storeId` | String | DoorDash store ID (from URL) |
| `storeName` | String | Restaurant name |
| `storeUrl` | String | Store page URL |
| `title` | String | Page title |
| `description` | String | Meta description |

### Location
| Field | Type | Description |
|---|---|---|
| `address` | String | Street address |
| `city` | String | City |
| `state` | String | State / region code |

### Categorization
| Field | Type | Description |
|---|---|---|
| `breadcrumbs` | Array | Page breadcrumb names (e.g., `["Home", "Boston", "Burgers", "UBURGER"]`) — last is restaurant, second-to-last is cuisine |

### Menu
| Field | Type | Description |
|---|---|---|
| `menuSections` | Array | Section names (e.g., `["Salads", "Burgers", "Drinks"]`) |
| `menuSectionCount` | Integer | Number of menu sections |
| `menuItems` | Array | Flat list of items: `[{section, name, description, price}, ...]` |
| `menuItemCount` | Integer | Total items across all sections |

### FAQ
| Field | Type | Description |
|---|---|---|
| `faq` | Array | List of `{question, answer}` pairs from the FAQ section |
| `faqCount` | Integer | Number of FAQ entries |

### Metadata
| Field | Type | Description |
|---|---|---|
| `scrapedAt` | String | ISO 8601 scrape timestamp |

### Example Output

```json
{
    "storeId": "15034",
    "storeName": "UBURGER",
    "storeUrl": "https://www.doordash.com/store/15034",
    "address": "636 Beacon Street",
    "city": "Boston",
    "state": "MA",
    "breadcrumbs": ["Home", "Boston", "Burgers", "UBURGER"],
    "menuSectionCount": 11,
    "menuItemCount": 37,
    "menuSections": ["Usalads", "Burgers", "Sandwiches", "Sides"],
    "menuItems": [
        {"section": "Usalads", "name": "Greek Salad", "description": "Romaine lettuce, cherry tomatoes, ...", "price": "$8.50"}
    ],
    "faqCount": 3,
    "faq": [
        {"question": "How can I order from UBURGER on DoorDash?", "answer": "..."}
    ],
    "scrapedAt": "2026-04-13T05:55:00+00:00"
}
```

## FAQ

**Q: Why doesn't this scrape user reviews?**
DoorDash removed user-facing reviews from store pages and now only shows aggregate ratings via menu items. The reference actor labeled "DoorDash Reviews Scraper" is misleading — there are no individual reviews to extract. This actor instead extracts everything DoorDash actually exposes: menu, address, FAQ, and breadcrumbs.

**Q: Why is a RESIDENTIAL proxy required?**
DoorDash's `www.doordash.com/store/*` paths are protected by Cloudflare which blocks Apify datacenter IPs with `403 Just a moment...`. A real Chrome browser (Patchright) on a US residential IP solves the Cloudflare challenge automatically in 2–15 seconds. The proxy is hardcoded and applied automatically — no configuration needed.

**Q: How long does each restaurant take?**
Roughly 15–25 seconds per restaurant (Cloudflare solve + page load + JSON-LD parse). Limited by the browser session, not by network throughput.

**Q: Can I get prices in dollars (not strings)?**
Prices are kept as strings (`"$8.50"`) because DoorDash sometimes uses ranges or currency symbols. Cast to float in your downstream pipeline if you need numerics: `float(price.replace("$", "").split("-")[0])`.

**Q: Will this work for all DoorDash stores?**
Yes for restaurants with a published menu schema. About 40% of DoorDash stores don't expose a Menu JSON-LD on their store page (closed restaurants, brand aggregators like ezCater, certain catering platforms). For those stores the scraper still returns full restaurant info, FAQ, breadcrumbs and address — but `menuSections` and `menuItems` come back as empty arrays. Convenience-store / grocery URLs (e.g., `/store/cvs`, `/store/walgreens`) have a different page structure and may return fewer fields.

## Use Cases

- **Restaurant menu intelligence** — track competitor pricing across markets
- **Cuisine analysis** — group restaurants by breadcrumb cuisine tag
- **Market research** — identify chains operating in specific cities
- **Menu engineering** — see which items / sections are common across restaurants
- **Lead generation** — find independent restaurants by city + cuisine

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/doordash-restaurant-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
