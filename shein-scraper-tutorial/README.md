# Shein Product Scraper Tutorial: Run This Apify Actor with Python

Scrape product details from Shein (us.shein.com) by direct product URL. Returns SKU, product ID, title, price, sale price, images, sizes, colors, and rating.

This repository shows how to run [Shein Product Scraper](https://apify.com/crawlerbros/shein-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/shein-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/shein-scraper](https://apify.com/crawlerbros/shein-scraper)
- **SEO title:** Shein Product Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape product details from Shein (us.shein.com) by direct product URL. Returns SKU, product ID, title, price, sale price, images, sizes, colors, and rating.

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

# Shein Featured Products Scraper

Scrape featured products from **[Shein](https://shein.com)** regional homepages across **22 countries**. Returns product ID, title, URL, sale and retail prices with formatted currency text, discount %, category, and images — all in local currency.

## What it does

- Fetches the Shein homepage for the selected country
- Parses ~6–16 server-rendered featured products from the embedded `productList` JSON (varies by country and session)
- Bracket-counted JSON extraction tolerates non-JSON fragments in the surrounding page
- Returns prices in local currency with sale/retail/discount and formatted symbol text
- Hardcoded residential proxy (Shein blocks all datacenter IPs)

## Scope note

**This scraper returns *currently-featured* Shein homepage products, not a keyword/URL-based catalog lookup.** Shein's category (`/dress-c-1727.html`) and product detail (`/...-p-39521541.html`) pages redirect every anonymous session to `/risk/challenge?captcha_type=903`. Only the root homepage is reachable without cookies, so the scraper extracts the featured products from the homepage server-side render.

The featured set rotates per session ID, so each run can return different products. Run the scraper multiple times to accumulate variety.

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `country` | enum | `US` | Shein regional homepage (see supported countries below) |
| `maxItems` | integer | `30` | Maximum featured products to return (1–200) |

### Supported countries

| Code | Country | Currency |
|---|---|---|
| `US` | United States | USD |
| `UK` | United Kingdom | GBP |
| `DE` | Germany | EUR |
| `FR` | France | EUR |
| `ES` | Spain | EUR |
| `IT` | Italy | EUR |
| `AU` | Australia | AUD |
| `BR` | Brazil | BRL |
| `CA` | Canada | CAD |
| `MX` | Mexico | MXN |
| `NL` | Netherlands | EUR |
| `SE` | Sweden | SEK |
| `PL` | Poland | PLN |
| `CH` | Switzerland | CHF |
| `PT` | Portugal | EUR |
| `AT` | Austria | EUR |
| `IL` | Israel | ILS |
| `PH` | Philippines | PHP |
| `SG` | Singapore | SGD |
| `MY` | Malaysia | MYR |
| `NZ` | New Zealand | NZD |
| `ZA` | South Africa | ZAR |

### Example input

```json
{
    "country": "DE",
    "maxItems": 20
}
```

## Output

Each product is a JSON record. Fields are omitted when not present — no field is ever `null`.

| Field | Type | Always present | Description |
|---|---|---|---|
| `productId` | string | ✓ | Shein goods_id |
| `title` | string | ✓ | Product name |
| `url` | string | ✓ | Product page URL |
| `countryCode` | string | ✓ | 2-letter country code |
| `scrapedAt` | string | ✓ | UTC ISO 8601 scrape timestamp |
| `mainImage` | string | ✓ | Main product image URL |
| `currency` | string | ✓ | Local currency code |
| `salePrice` | number | ✓ | Current sale price (numeric) |
| `salePriceText` | string | ✓ | Formatted sale price with symbol (e.g. `$18.23`) |
| `retailPrice` | number | ✓ | Original retail price (numeric) |
| `retailPriceText` | string | ✓ | Formatted retail price with symbol (e.g. `$26.39`) |
| `discountPercentage` | integer | — | Discount % off retail (present on ~95% of products) |
| `catId` | string | — | Shein category ID (present on ~96% of products) |
| `images` | array | — | Additional product image URLs (present on ~99% of products) |

### Sample output

```json
{
    "productId": "410596328",
    "title": "Aloruh Women's Beaded Floral Loose Halter Neck Top",
    "url": "https://us.shein.com/-p-410596328.html",
    "countryCode": "US",
    "mainImage": "https://img.ltwebstatic.com/v4/j/pi/2026/03/16/ea/1773668717f1aeb4cce6f077e48c10775ec0127141_thumbnail_405x552.jpg",
    "currency": "USD",
    "salePrice": 13.33,
    "salePriceText": "$13.33",
    "retailPrice": 20.49,
    "retailPriceText": "$20.49",
    "discountPercentage": 35,
    "catId": "2223",
    "images": [
        "https://img.ltwebstatic.com/v4/j/pi/2026/02/28/3b/1772264392b9902f7c9c914bac00c237fb58631ada_thumbnail_405x552.jpg",
        "https://img.ltwebstatic.com/v4/j/pi/2026/03/16/72/177366871989f4c9815bf2e1e447c739a678fb483d_thumbnail_405x552.jpg"
    ],
    "scrapedAt": "2026-05-15T16:34:10Z"
}
```

## FAQ

**Do I need a proxy?**
No configuration needed — a residential proxy is hardcoded and applied automatically. Shein blocks all direct datacenter access.

**Why featured products only, not keyword search?**
Shein blocks category and product detail pages with a `/risk/challenge?captcha_type=903` redirect for anonymous sessions. Only the root homepage is reachable without pre-seeded cookies or a captcha-solver.

**How many products per run?**
The server-rendered homepage typically contains 6–16 featured products depending on country and session. `maxItems` caps the output (default 30, max 200), but you will rarely exceed ~16 per run.

**Do different countries return different products?**
Yes. Each regional site has its own featured set with local pricing, currency, and products.

**Is the data fresh?**
Every run fetches the live homepage. The featured set rotates per session, so repeated runs build up a rolling catalog.

## Use cases

- **Daily trending monitor** — track what Shein is featuring on each regional homepage
- **Price sampling** — accumulate a rolling catalog of Shein prices across 22 markets
- **Market research** — monitor product themes, categories, and promotions globally
- **Cross-market comparison** — compare US vs EU featured picks, pricing, or discount levels
- **Competitive intelligence** — track which products Shein promotes in emerging markets

## Notes

- Pricing is configured in the Apify UI (pay-per-result).
- The daily Apify test run uses `country=US`, `maxItems=5`.
- Parser: `_iter_product_blocks` walks every `{"goods_id":"..."}` object with a bracket counter + `json.loads`, tolerant of nested JSON fragments in the enclosing array.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/shein-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
