# Groupon Coupons Scraper Tutorial: Run This Apify Actor with Python

Scrape Groupon Coupons - one of the largest coupon aggregators with 10,000+ brands. Fetch coupons by store name, browse by category, or get popular deals. Extracts coupon codes, discount values, verified status, usage counts, and more. No proxy required.

This repository shows how to run [Groupon Coupons Scraper](https://apify.com/crawlerbros/groupon-coupons-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/groupon-coupons-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/groupon-coupons-scraper](https://apify.com/crawlerbros/groupon-coupons-scraper)
- **SEO title:** Groupon Coupons Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Groupon Coupons - one of the largest coupon aggregators with 10,000+ brands. Fetch coupons by store name, browse by category, or get popular deals. Extracts coupon codes, discount values, verified status, usage counts, and more. No proxy required.

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

# Groupon Coupons Scraper

Scrape coupon codes, promo deals, and discount offers from **Groupon Coupons** — one of the largest coupon aggregators in the US, featuring 10,000+ brands and stores.

## What You Can Scrape

- Coupon codes ready to use at checkout
- Deals and reward offers with no code required
- Discount value (%, $, free shipping, BOGO)
- Verified status — manually checked by Groupon editors
- Usage counts (how many people used a coupon today)
- Expiry information

## Modes

| Mode | Description |
|------|-------------|
| **byStore** | Fetch all coupons from one or more specific stores (e.g. amazon, nike, doordash) |
| **byCategory** | Browse coupons by category (electronics, travel, food-drink, etc.) |
| **popular** | Get today's popular and featured deals from the Groupon homepage |

## Input

| Field | Type | Description |
|-------|------|-------------|
| `mode` | Select | `byStore` / `byCategory` / `popular` |
| `storeNames` | String List | Store slugs to scrape (e.g. `amazon`, `nike`). Used in `byStore` mode. |
| `category` | Select | Category to browse. Used in `byCategory` mode. |
| `couponTypeFilter` | Select | Filter by type: Code, Deal, or Reward |
| `verifiedOnly` | Boolean | Only return Groupon-verified coupons |
| `maxItems` | Integer | Maximum coupons to return (1–500, default: 50) |

### Store Slugs

Store slugs match the URL on Groupon: `https://www.groupon.com/coupons/<slug>`. Examples:

- `amazon` → amazon.com
- `nike` → Nike
- `target` → Target
- `doordash` → DoorDash
- `best-buy` → Best Buy
- `sams-club` → Sam's Club

### Available Categories

`food-drink`, `attractions`, `entertainment`, `womens-clothing`, `mens-clothing`, `health-beauty`, `travel`, `gifts`, `electronics`, `sports-outdoors`, `home-garden`, `auto`, `department-stores`, `office-supplies`, `kids-baby`, `pets`, `seasonal`

## Output

Each record contains:

```json
{
  "couponId": "3468551",
  "storeName": "Amazon",
  "storeUrl": "https://www.groupon.com/coupons/amazon",
  "couponTitle": "30% Off Subscribe & Save with Amazon Promo Code",
  "couponDescription": "Subscribe for auto-delivery and save up to 30% off your next delivery.",
  "couponCode": "CLIPCOUPON",
  "couponType": "Code",
  "discountValue": "30% Off",
  "discountType": "Percent",
  "isVerified": true,
  "usedToday": 2881,
  "expiresAt": "2026-07-03T05:00:00.0000000Z",
  "url": "https://www.groupon.com/coupons/article/3468551",
  "sourceUrl": "https://www.groupon.com/coupons/amazon",
  "recordType": "coupon",
  "scrapedAt": "2026-06-30T10:00:00+00:00"
}
```

## Technical Details

- **No proxy required** — works on the free Apify plan with datacenter IPs
- **Memory**: 1024 MB
- **Anti-bot tier**: curl_cffi Chrome 131 TLS impersonation (Tier 2)
- **Data source**: [groupon.com/coupons](https://www.groupon.com/coupons)

## FAQs

**Do I need a proxy or API key?**
No. This actor works without any proxy configuration or credentials on the free Apify plan.

**How many coupons can I get?**
Each store page typically has 10–50 active coupons. The `maxItems` limit caps total output.

**Are the coupon codes visible?**
Yes — Groupon shows coupon codes directly in the HTML (no click required to reveal them).

**How often are coupons updated?**
Groupon updates their coupons daily. Run this actor daily to get fresh data.

**What does `isVerified` mean?**
Groupon's editorial team manually tests and marks coupons as "Verified" when confirmed working.

**Can I scrape all stores?**
Use `byCategory` mode to get coupons from stores in a specific category, or use `popular` mode for trending deals. For specific stores, use `byStore` with a list of store slugs.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/groupon-coupons-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
