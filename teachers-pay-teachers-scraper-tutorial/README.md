# Teachers Pay Teachers Store & Product Scraper Tutorial: Run This Apify Actor with Python

Scrape Teachers Pay Teachers (TpT) with search educational resources by keyword, grade, subject, or format. Get product details with price, rating, seller info, and more. Also scrape entire teacher stores.

This repository shows how to run [Teachers Pay Teachers Store & Product Scraper](https://apify.com/crawlerbros/teachers-pay-teachers-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/teachers-pay-teachers-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/teachers-pay-teachers-scraper](https://apify.com/crawlerbros/teachers-pay-teachers-scraper)
- **SEO title:** Teachers Pay Teachers Store & Product Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Teachers Pay Teachers (TpT) with search educational resources by keyword, grade, subject, or format. Get product details with price, rating, seller info, and more. Also scrape entire teacher stores.

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

# Teachers Pay Teachers Store & Product Scraper

Scrape educational resources from **Teachers Pay Teachers** (TPT) — the world's largest marketplace for teacher-created educational materials. Extract product details including price, rating, seller information, grade levels, and more — no account required.

## What This Actor Does

- **Search resources** by keyword with optional grade, subject, and format filters
- **Browse by grade** — Pre-K through 12th grade, Higher Education, Homeschool
- **Browse by subject** — Math, ELA, Science, Social Studies, Arts, and more
- **Fetch specific product details** from TpT product URLs
- **Scrape entire teacher stores** — get all products from any teacher's store page

## Input

| Field | Type | Description |
|-------|------|-------------|
| `mode` | Select | `search`, `byGrade`, `bySubject`, `getProduct`, `getStore` |
| `searchQuery` | Text | Keyword search (mode=search) |
| `startUrls` | List | TpT product or store URLs (getProduct/getStore) |
| `grade` | Select | Grade level filter (also required for byGrade mode) |
| `subject` | Select | Subject area filter (required for bySubject mode) |
| `format` | Select | Resource format (PDF, Google Apps, PowerPoint, etc.) |
| `isFree` | Boolean | Only return free resources |
| `minRating` | Number | Minimum average rating (1–5 star scale) |
| `minReviews` | Integer | Minimum number of ratings/reviews |
| `maxItems` | Integer | Maximum records to return (default: 24) |

### Grade Options
Pre-K, Kindergarten, 1st–12th Grade, Higher Education, Adult Education, Homeschool, Not Grade Specific

### Subject Options
Arts & Music, English Language Arts, Foreign Language, Math, Science, Social Studies - History, Special Education, Holidays/Seasonal

### Format Options
PDF, Google Apps, PowerPoint, Word Document, Excel Spreadsheets, Easel Activity, Interactive Notebooks, Lesson Plans, Task Cards, Tests, Worksheets, Workbooks

## Output

| Field | Type | Description |
|-------|------|-------------|
| `productId` | String | TpT numeric product ID |
| `title` | String | Resource title |
| `description` | String | Product description |
| `price` | Number | Price in USD (0.0 = free) |
| `isFree` | Boolean | Whether the resource is free |
| `rating` | Number | Average rating (1–5 scale) |
| `ratingCount` | Integer | Number of ratings |
| `seller` | String | Teacher/seller display name |
| `sellerUrl` | String | Seller's TpT store URL |
| `thumbnailUrl` | String | Product preview image URL |
| `url` | String | Product page URL |
| `releaseDate` | String | Date product was listed |
| `currency` | String | Currency code (USD) |
| `grades` | Array | Grade levels (when available) |
| `subjects` | Array | Subject areas (when available) |
| `formats` | Array | Resource formats (when available) |
| `recordType` | String | Always "product" |
| `scrapedAt` | String | ISO timestamp |

## Example Output

```json
{
  "productId": "4061393",
  "title": "Multiplication Color By Number Worksheets - Fact Fluency",
  "price": 3.50,
  "isFree": false,
  "rating": 4.8,
  "ratingCount": 1250,
  "seller": "Games 4 Learning",
  "sellerUrl": "https://www.teacherspayteachers.com/Store/Games-4-Learning",
  "thumbnailUrl": "https://ecdn.teacherspayteachers.com/thumbitem/...",
  "url": "https://www.teacherspayteachers.com/Product/Multiplication-Color-By-Number-Worksheets-Fact-Fluency-4061393",
  "currency": "USD",
  "recordType": "product",
  "scrapedAt": "2026-05-17T07:00:00+00:00"
}
```

## Modes

### `search` — Search by keyword
Searches TpT's browse page with optional filters.
```json
{"mode": "search", "searchQuery": "multiplication worksheets", "grade": "3rd", "maxItems": 24}
```

### `byGrade` — Browse by grade level
Returns resources for a specific grade.
```json
{"mode": "byGrade", "grade": "Kindergarten", "maxItems": 50}
```

### `bySubject` — Browse by subject
Returns resources for a specific subject area.
```json
{"mode": "bySubject", "subject": "Math", "grade": "5th", "maxItems": 50}
```

### `getProduct` — Fetch specific product(s)
Returns full details for specific product URLs.
```json
{
  "mode": "getProduct",
  "startUrls": [
    "https://www.teacherspayteachers.com/Product/Multiplication-Color-By-Number-Worksheets-4061393"
  ]
}
```

### `getStore` — Scrape a teacher's store
Returns all products from a teacher's store.
```json
{
  "mode": "getStore",
  "startUrls": ["https://www.teacherspayteachers.com/Store/Games-4-Learning"],
  "maxItems": 100
}
```

## FAQ

**Does this require a TpT account?**
No. All product listings and details scraped are publicly accessible without login.

**Does TpT use Algolia for search?**
TpT uses Algolia internally for its search infrastructure, but the search results are delivered as server-rendered HTML. This actor scrapes the HTML results pages and individual product pages to extract structured data (including JSON-LD) without needing Algolia credentials.

**How do I get grades, subjects, and formats for a product?**
These fields are best populated by fetching product detail pages (all modes except search/byGrade/bySubject). Use `mode=getProduct` or `mode=getStore` for richest data.

**What is the rating scale?**
TpT uses a standard 1–5 star rating scale. The JSON-LD on product pages includes `ratingValue` on this scale.

**How many products can I scrape?**
Set `maxItems` up to 5000. TpT has millions of resources.

**Why might some product records have fewer fields?**
Listing pages provide only the product URL and title. Full details (price, rating, seller, thumbnail) require fetching individual product pages, which is done automatically by the actor.

**Can I scrape an entire teacher's store?**
Yes — use `mode=getStore` with the store URL. The actor paginates through all store pages automatically.

## Limitations

- TpT's browse page may require a brief delay between requests to avoid rate limiting
- Some product fields (grades, subjects, formats) may not always be available on listing pages and require fetching the product detail page
- Product pages blocked by TpT's anti-bot systems will be skipped with a warning; try reducing request frequency if many pages fail
- Preview/download files are not accessible without a TpT account

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/teachers-pay-teachers-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
