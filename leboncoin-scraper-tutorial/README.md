# Leboncoin Classifieds Scraper Tutorial: Run This Apify Actor with Python

Extract classified ads from leboncoin.fr with title, price, location, images, attributes, owner type. Supports all categories (real estate, vehicles, jobs, services, etc.) with filter URL pass-through.

This repository shows how to run [Leboncoin Classifieds Scraper](https://apify.com/crawlerbros/leboncoin-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/leboncoin-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/leboncoin-scraper](https://apify.com/crawlerbros/leboncoin-scraper)
- **SEO title:** Leboncoin Classifieds Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract classified ads from leboncoin.fr with title, price, location, images, attributes, owner type. Supports all categories (real estate, vehicles, jobs, services, etc.) with filter URL pass-through.

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

# Leboncoin Classifieds Scraper

Extract classified ads from **leboncoin.fr** — France's largest classifieds platform. Returns title, description, price, location, images, owner info, and category-specific attributes (real estate specs, vehicle specs, job details, etc.).

## Features

- **30 output fields** per ad — flat schema with typed defaults (zero nulls)
- **All categories supported** — real estate (rentals + sales), vehicles, jobs, services, electronics, fashion, etc.
- **Filter by category, keyword, location, price** — via Leboncoin URL parameters
- **Owner type** (`private` vs `pro`) for lead segmentation
- **Geocoordinates** for every ad
- **Image gallery** with multiple resolutions
- **Generic attributes** (real estate type, surface, rooms, energy class, etc.) flattened into a single dict
- **DataDome bypass** via Camoufox (patched Firefox with built-in fingerprint spoofing) + RESIDENTIAL/FR proxy (hardcoded, applied automatically)
- **Pagination** via `?page=N` (35 ads per page)

## Input

| Field | Type | Description |
|---|---|---|
| `startUrls` | Array | Leboncoin search URLs (e.g., `https://www.leboncoin.fr/recherche?category=10&locations=Paris`) |
| `category` | Integer | Category ID when no startUrls. Verified: 9=real estate sales, 10=rentals, 2=cars, 6=auto equipment, 17=phones, 33=jobs. For other categories, find the ID in any leboncoin.fr search URL. |
| `search` | String | Free-text keyword (combined with category) |
| `maxItems` | Integer | Maximum ads to return (default 50, max 1000) |

### Example Input

```json
{
    "startUrls": [
        "https://www.leboncoin.fr/recherche?category=10&locations=Paris&price=min-2000"
    ],
    "maxItems": 100
}
```

Or filter mode:

```json
{
    "category": 2,
    "search": "Tesla",
    "maxItems": 50
}
```

## Output

Each ad has **30 fields**. All fields are always present — empty strings, zero, `false`, or empty array as typed defaults, never `null`.

### Identity
| Field | Type | Description |
|---|---|---|
| `id` | Integer | Leboncoin `list_id` |
| `url` | String | Ad URL |
| `subject` | String | Ad title |
| `body` | String | Description text (truncated to 2,000 chars) |
| `categoryId` | String | Category ID |
| `categoryName` | String | Category name |
| `adType` | String | `offer` / `demand` |
| `status` | String | `active` / `expired` / `sold` |

### Price
| Field | Type | Description |
|---|---|---|
| `price` | Integer | Price in EUR |

### Location
| Field | Type | Description |
|---|---|---|
| `city` | String | City |
| `zipcode` | String | Postal code |
| `department` | String | Department name |
| `region` | String | Region name |
| `country` | String | Country code (`FR`) |
| `latitude` | Number | Latitude |
| `longitude` | Number | Longitude |

### Owner
| Field | Type | Description |
|---|---|---|
| `ownerName` | String | Seller display name |
| `ownerType` | String | `private` or `pro` |
| `ownerId` | String | Seller user ID |
| `ownerStoreId` | String | Pro store ID (if pro) |
| `hasPhone` | Boolean | Whether phone number is exposed |

### Media & Attributes
| Field | Type | Description |
|---|---|---|
| `imageCount` | Integer | Number of images |
| `imageUrls` | Array | All large image URLs |
| `thumbnail` | String | Thumbnail URL |
| `attributes` | Object | Generic attributes (e.g., `{"real_estate_type": "Appartement", "square": "60 m²", "rooms": "2"}`) |

### Dates & Flags
| Field | Type | Description |
|---|---|---|
| `publishedDate` | String | First publication date |
| `expirationDate` | String | Expiration date |
| `isUrgent` | Boolean | Urgent ad flag |
| `isHighlighted` | Boolean | Highlighted ad flag |
| `scrapedAt` | String | ISO 8601 scrape timestamp |

## FAQ

**Q: Do I need a proxy?**
No configuration needed — a French residential proxy is hardcoded and applied automatically. Leboncoin's DataDome anti-bot blocks Apify datacenter IPs with a CAPTCHA challenge, so the scraper uses Camoufox (a fingerprint-spoofing Firefox browser) combined with `RESIDENTIAL/FR` proxy traffic. Sessions are rotated automatically on failure.

**Q: How do I find the category ID?**
Browse to leboncoin.fr, apply filters, then look at the URL: `?category=10` is rentals, `?category=9` is real estate sales, `?category=2` is vehicles. The full list is on Leboncoin's category page.

**Q: How many results per page?**
35 ads per page. The scraper paginates via `?page=N` until `maxItems` is reached.

**Q: Are pro and private ads both included?**
Yes. The `ownerType` field tells you which. You can filter post-scrape if you only want one type.

**Q: How fresh is the data?**
Leboncoin's `__NEXT_DATA__` contains the live search results — same data as their website at the moment of fetch.

## Use Cases

- **Real estate market research** — track rental and sale prices by city / region
- **Vehicle pricing intelligence** — monitor used-car markets across France
- **Lead generation** — discover pro sellers with mailing addresses (via owner data)
- **Job market analysis** — extract job postings by region and category
- **Price monitoring** — daily runs to detect price changes
- **Competitor analysis** — track listings from specific stores

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/leboncoin-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
