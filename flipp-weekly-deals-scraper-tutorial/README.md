# Flipp Weekly Deals & Grocery Ad Scraper Tutorial: Run This Apify Actor with Python

Scrape Flipp - the #1 grocery deals platform used by Walmart, Lidl, Costco, Target, Kroger, and 2000+ US retailers. Get current weekly flyer items with prices, discounts, and validity dates. Search by keyword or browse specific store weekly ads.

This repository shows how to run [Flipp Weekly Deals & Grocery Ad Scraper](https://apify.com/crawlerbros/flipp-weekly-deals-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/flipp-weekly-deals-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/flipp-weekly-deals-scraper](https://apify.com/crawlerbros/flipp-weekly-deals-scraper)
- **SEO title:** Flipp Weekly Deals & Grocery Ad Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Flipp - the #1 grocery deals platform used by Walmart, Lidl, Costco, Target, Kroger, and 2000+ US retailers. Get current weekly flyer items with prices, discounts, and validity dates. Search by keyword or browse specific store weekly ads.

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

# Flipp Weekly Deals & Grocery Ad Scraper

Scrape [Flipp](https://flipp.com) — the #1 grocery deals platform in North America, featuring weekly ads from Walmart, Lidl, Costco, Target, Kroger, CVS, Walgreens, and 2,000+ US retailers. Get real-time weekly flyer items with prices, discounts, sale badges, and validity dates. No login or API key required.

## What data do you get?

Each deal record includes:

| Field | Description |
|---|---|
| `productId` | Flipp deal item ID |
| `name` | Product name |
| `merchantName` | Store/retailer name |
| `merchantId` | Flipp numeric merchant ID (region-specific) |
| `currentPrice` | Current sale price (USD) |
| `originalPrice` | Original price before discount (if available) |
| `discount` | Savings amount in USD |
| `discountPercent` | Percentage saved |
| `pricePrefix` | Price prefix text (e.g., "From") |
| `priceSuffix` | Price suffix text (e.g., "ea.", "/lb") |
| `saleBadge` | Sale badge text (e.g., "Buy 1 Get 1 Free", "Save 25%") |
| `category` | L1 product category |
| `subcategory` | L2 product subcategory |
| `validFrom` | Deal start date (ISO 8601) |
| `validTo` | Deal end date (ISO 8601) |
| `flyerId` | Flipp flyer ID |
| `flyerName` | Name of the flyer the deal belongs to (flyer-based modes) |
| `flyerValidFrom` | Flyer start date, ISO 8601 (flyer-based modes) |
| `flyerValidTo` | Flyer end date, ISO 8601 (flyer-based modes) |
| `imageUrl` | Product image URL |
| `merchantLogoUrl` | Store logo URL |
| `isPremium` | Whether this is a premium/sponsored placement |
| `sourceUrl` | Direct link to deal on Flipp |
| `recordType` | Always `"deal"` |
| `scrapedAt` | ISO timestamp of scrape |

## Modes

### Weekly deals (`mode=weeklyDeals`)
Get all items from the current weekly flyer of a specific store. Perfect for tracking Lidl, Walmart, or any retailer's weekly specials.

**Input:**
```json
{
  "mode": "weeklyDeals",
  "merchant": "Lidl",
  "postalCode": "10001",
  "maxItems": 100
}
```

### Search deals (`mode=search`)
Search across all stores by keyword to find the best deals on a specific product.

**Input:**
```json
{
  "mode": "search",
  "searchQuery": "chicken breast",
  "postalCode": "10001",
  "category": "Groceries",
  "maxItems": 50
}
```

### By merchant (`mode=byMerchant`)
List all current active flyers for a specific retailer.

**Input:**
```json
{
  "mode": "byMerchant",
  "merchant": "Lidl",
  "postalCode": "22201",
  "maxItems": 10
}
```

Each flyer record (`recordType: "flyer"`) includes `flyerId`, `flyerName`, `merchantName`, `merchantId`, `merchantLogoUrl`, `validFrom`/`validTo` (when the flyer's deals are active), `availableFrom`/`availableTo` (when the flyer itself is browsable — sometimes a day or two earlier than `validFrom`), `isPremium` (sponsored flyer flag), `thumbnailUrl`, `categories`, and `sourceUrl`.

## Supported stores

Lidl, Walmart, Target, Kroger, Costco, Aldi, CVS Pharmacy, Walgreens, Safeway, Publix, Whole Foods Market, Dollar General, Dollar Tree, Food Lion, Harris Teeter, Meijer, Giant Food, Stop & Shop, ShopRite, H-E-B, Weis Markets, Winn-Dixie, Rite Aid, Albertsons

## Sample output record

```json
{
  "productId": "1020582129",
  "name": "Crystal Geyser® Sparkling Water",
  "merchantName": "Lidl",
  "currentPrice": 2.19,
  "priceSuffix": "ea.",
  "category": "Food, Beverages & Tobacco",
  "subcategory": "Beverages",
  "validFrom": "2026-06-24T04:00:00+00:00",
  "validTo": "2026-07-01T03:59:59+00:00",
  "flyerId": 7985465,
  "imageUrl": "https://f.wishabi.net/page_items/424025910/1781586849/extra_large.jpg",
  "isPremium": false,
  "sourceUrl": "https://flipp.com/flyers/lidl/7985465/items/1020582129",
  "recordType": "deal",
  "scrapedAt": "2026-06-30T12:00:00+00:00"
}
```

## Use cases

- Track grocery prices and deals across multiple stores
- Build price comparison tools for budget shoppers
- Monitor competitor pricing for retail market intelligence
- Find the best deals on specific products in your area
- Automate weekly deal newsletters or savings alerts
- Analyze promotional patterns by retailer or category

## FAQ

**How often does data update?**
Flipp flyers update weekly — most stores publish new ads on Wednesday for the following week. This scraper always fetches the currently active flyer.

**Why do I need a postal code?**
Flipp flyers are location-specific — store availability and prices can vary by region. The default postal code (10001 = New York City) works for most major national chains.

**Does this require login?**
No — Flipp's deal data is publicly accessible without authentication.

**What if my merchant isn't in the list?**
The dropdown shows the most common US retailers. If your store is not listed, you can still use `mode=search` to search across all available stores.

**Are prices in USD?**
Yes — this scraper targets the US Flipp platform. Prices are in USD.

**Data source**
[Flipp](https://flipp.com) — powered by Wishabi's flyer platform. Data is publicly accessible weekly ad content from participating US retailers.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/flipp-weekly-deals-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
