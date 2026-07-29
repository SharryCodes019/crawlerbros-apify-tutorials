# Amazon Product Scraper Tutorial: Run This Apify Actor with Python

Scrapes Amazon product data including prices, reviews, seller info, variants, and delivery details. Supports multiple Amazon domains and languages.

This repository shows how to run [Amazon Product Scraper](https://apify.com/crawlerbros/amazon-product-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/amazon-product-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/amazon-product-scraper](https://apify.com/crawlerbros/amazon-product-scraper)
- **SEO title:** Amazon Product Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrapes Amazon product data including prices, reviews, seller info, variants, and delivery details. Supports multiple Amazon domains and languages.

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

# Amazon Product Scraper

Extract product data from any Amazon domain including prices, reviews, ratings, seller info, and more.

## Supported Amazon Domains

| Domain | Country |
|--------|---------|
| amazon.com | United States |
| amazon.co.uk | United Kingdom |
| amazon.de | Germany |
| amazon.fr | France |
| amazon.it | Italy |
| amazon.es | Spain |
| amazon.ca | Canada |
| amazon.co.jp | Japan |
| amazon.in | India |
| amazon.com.au | Australia |
| amazon.com.br | Brazil |
| amazon.com.mx | Mexico |

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `productUrls` | array | Yes | - | Amazon product URLs to scrape (e.g., `amazon.com/dp/ASIN`) |
| `proxyCountry` | string | No | AUTO | Proxy country code (AUTO selects based on domain) |
| `rateLimitDelay` | integer | No | 2 | Delay between requests in seconds (1-30) |

## Input Examples

### Single Product
```json
{
  "productUrls": ["https://www.amazon.com/dp/B09X7MPX8L"]
}
```

### Multiple Products
```json
{
  "productUrls": [
    "https://www.amazon.com/dp/B09X7MPX8L",
    "https://www.amazon.com/dp/B08N5WRWNW",
    "https://www.amazon.com/dp/B09V3KXJPB"
  ]
}
```

### Multiple Domains
```json
{
  "productUrls": [
    "https://www.amazon.com/dp/B09X7MPX8L",
    "https://www.amazon.co.uk/dp/B09X7MPX8L",
    "https://www.amazon.de/dp/B09X7MPX8L"
  ]
}
```

### With Custom Settings
```json
{
  "productUrls": ["https://www.amazon.com/dp/B09X7MPX8L"],
  "proxyCountry": "US",
  "rateLimitDelay": 3
}
```

## Output Fields

| Field | Type | Description |
|-------|------|-------------|
| `title` | string | Product title |
| `url` | string | Product page URL |
| `asin` | string | Amazon Standard Identification Number |
| `inStock` | boolean | Whether product is in stock |
| `inStockText` | string | Stock availability text |
| `brand` | string | Product brand name |
| `price` | object | Current price (`value`, `currency`) |
| `listPrice` | object | Original price if discounted |
| `shippingPrice` | object | Shipping cost |
| `stars` | number | Average rating (0-5) |
| `reviewsCount` | number | Total number of reviews |
| `breadCrumbs` | string | Category path |
| `thumbnailImage` | string | Main product image URL |
| `description` | string | Product description text |
| `features` | array | Bullet point features list |
| `variantAsins` | array | Related variant product ASINs |
| `reviewsLink` | string | URL to reviews page |
| `delivery` | string | Delivery information |
| `fastestDelivery` | string | Fastest delivery option |
| `seller` | object | Seller information (`name`, `id`, `url`) |
| `bestsellerRanks` | array | Bestseller rankings |
| `scrapedAt` | string | Timestamp when data was scraped |

## Output Example

```json
{
  "title": "SanDisk 1TB Extreme microSDXC UHS-I Memory Card",
  "url": "https://www.amazon.com/dp/B09X7MPX8L",
  "asin": "B09X7MPX8L",
  "inStock": true,
  "inStockText": "In Stock",
  "brand": "SanDisk",
  "price": {
    "value": 99.99,
    "currency": "$"
  },
  "stars": 4.8,
  "reviewsCount": 137947,
  "breadCrumbs": "Electronics > Computers & Accessories > Memory Cards > Micro SD Cards",
  "thumbnailImage": "https://m.media-amazon.com/images/I/716kSUlHouL._AC_SX466_.jpg",
  "description": "The SanDisk Extreme microSDXC memory card...",
  "features": [
    "Save time with card offload speeds of up to 190MB/s",
    "Up to 130MB/s write speeds for fast shooting",
    "4K UHD-ready with UHS Speed Class 3 (U3)"
  ],
  "variantAsins": ["B09X7C2GBC", "B09X7C7LL1", "B09X7BK27V"],
  "seller": {
    "name": "Amazon.com",
    "id": "ATVPDKIKX0DER",
    "url": "/gp/help/seller/..."
  },
  "bestsellerRanks": [
    {
      "rank": 3,
      "category": "Micro SD Memory Cards"
    }
  ],
  "scrapedAt": "2026-01-21T12:30:00.000Z"
}
```

## Tips

- Use direct product URLs (`/dp/ASIN` format) for best results
- Increase `rateLimitDelay` to 3-5 seconds if experiencing blocks
- Proxy country is auto-selected based on Amazon domain for best results
- Empty/null fields are dropped at push time, so the dataset only carries
  fields that were actually populated for a given product

## Limitations

- A residential Apify proxy is required; datacenter IPs are challenged
  almost immediately. The actor exits cleanly with a typed status
  message if no proxy is configured.
- Bot-check (CAPTCHA) pages occasionally appear; the actor automatically
  bypasses the simple "Continue shopping" button and skips ASINs that
  hit a hard image CAPTCHA.
- A small number of fields (e.g. `priceVariants`) may be omitted on
  products with no variant matrix.

## FAQs

**Which Amazon domains are supported?**
All major country domains: amazon.com, .co.uk, .de, .fr, .es, .it, .ca,
.com.au, .co.jp, .in, .com.br, .com.mx and more. Mix domains freely in
one run; the actor groups URLs by domain and routes proxy traffic per
TLD.

**Is the actor compliant with Amazon's robots.txt?**
Yes. It only fetches `/dp/{ASIN}` product pages, which Amazon's
`robots.txt` does not disallow for `User-agent: *`. There is no
`Crawl-delay` directive on amazon.com; the actor paces requests via the
`rateLimitDelay` input.

**Why is a residential proxy required?**
Amazon aggressively challenges anonymous datacenter IPs within seconds.
A residential proxy is the only stable way to reach product pages for an
end-to-end run.

**What happens if a CAPTCHA appears?**
The actor first attempts a soft bypass (clicking the "Continue
shopping" button on the simple bot-check page). If a hard image CAPTCHA
is detected, the ASIN is skipped and the run continues with the next
URL.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/amazon-product-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
