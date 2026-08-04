# UberEats Menu Scraper Tutorial: Run This Apify Actor with Python

Scrape full restaurant menus from UberEats. Extract restaurant info, all menu sections, items with prices, descriptions, and images.

This repository shows how to run [UberEats Menu Scraper](https://apify.com/crawlerbros/ubereats-menu-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/ubereats-menu-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/ubereats-menu-scraper](https://apify.com/crawlerbros/ubereats-menu-scraper)
- **SEO title:** UberEats Menu Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape full restaurant menus from UberEats. Extract restaurant info, all menu sections, items with prices, descriptions, and images.

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

# UberEats Menu Scraper

Extract complete restaurant menus from UberEats — including every section, item, price, description, and image. Get restaurant details like rating, delivery fee, address, and cuisine types in seconds. Built for market research, menu databases, price monitoring, and competitor analysis.

---

## What data does it extract?

| Field | Description |
|-------|-------------|
| `restaurantId` | UberEats unique store ID |
| `restaurantName` | Restaurant display name |
| `restaurantUrl` | Direct link to the restaurant on UberEats |
| `heroImageUrl` | Restaurant banner image URL |
| `rating` | Average star rating |
| `ratingCount` | Number of customer ratings |
| `priceRange` | Price tier (`$`, `$$`, `$$$`) |
| `cuisines` | Cuisine category tags (e.g. `["Burgers", "Fast Food"]`) |
| `isOpen` | Whether currently open for delivery |
| `address` | Street address |
| `city` | City |
| `deliveryFee` | Delivery fee (e.g. `Free`, `$0.49`) |
| `estimatedDeliveryTime` | Estimated delivery time (e.g. `15–25 min`) |
| `menu` | Full nested menu: sections → items |
| `menu[].sectionName` | Section name (e.g. `Burgers`, `Drinks`, `Sides`) |
| `menu[].items[].name` | Item name |
| `menu[].items[].description` | Item description (when available) |
| `menu[].items[].price` | Price in local currency (e.g. `5.99`) |
| `menu[].items[].currency` | ISO currency code (e.g. `USD`, `GBP`) |
| `menu[].items[].imageUrl` | Item photo URL |
| `menu[].items[].isAvailable` | Whether currently available |
| `menuSectionCount` | Total number of menu sections |
| `menuItemCount` | Total number of menu items |
| `itemsWithImageCount` | Number of items that have a photo |
| `itemsWithDescCount` | Number of items that have a description |
| `scrapedAt` | UTC timestamp of when data was collected |

---

## How to use

1. Open [UberEats](https://www.ubereats.com) and navigate to a restaurant page
2. Copy the URL from your browser's address bar (e.g. `https://www.ubereats.com/store/mcdonalds-fillmore/P21H_Lf3Se2wSmjGHfoFcQ`)
3. Paste the URL into the **Restaurant URLs** input field
4. Select the **Country** that matches the restaurant's location
5. Set **Max Items Per Restaurant** if you want to limit results
6. Click **Start** — your menu data appears in the dataset within seconds

---

## Input parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `restaurantUrls` | List of URLs | Yes | — | UberEats restaurant page URLs to scrape |
| `maxItemsPerRestaurant` | Integer | No | `200` | Maximum menu items extracted per restaurant (1–2000) |
| `country` | Select | No | `us` | Country context for the delivery API (`us`, `gb`, `au`, `ca`, `in`) |

---

## Example output

```json
{
  "restaurantId": "3f6d47fc-b7f7-49ed-b04a-68c61dfa0571",
  "restaurantName": "McDonald's® (Fillmore)",
  "restaurantUrl": "https://www.ubereats.com/store/mcdonalds-fillmore/P21H_Lf3Se2wSmjGHfoFcQ",
  "heroImageUrl": "https://d3i4yxtzktqr9n.cloudfront.net/...",
  "rating": 4.5,
  "ratingCount": "15000+",
  "priceRange": "$",
  "cuisines": ["American", "Burgers", "Fast Food"],
  "isOpen": true,
  "address": "1100 Fillmore St, San Francisco, CA 94115",
  "city": "San Francisco",
  "deliveryFee": "Free",
  "estimatedDeliveryTime": "15–25 min",
  "menuSectionCount": 8,
  "menuItemCount": 52,
  "itemsWithImageCount": 52,
  "itemsWithDescCount": 0,
  "menu": [
    {
      "sectionName": "Burgers",
      "items": [
        {
          "itemId": "abc-uuid",
          "name": "Big Mac",
          "price": 5.99,
          "currency": "USD",
          "imageUrl": "https://d3i4yxtzktqr9n.cloudfront.net/...",
          "isAvailable": true
        }
      ]
    }
  ],
  "scrapedAt": "2026-04-14T10:00:00Z"
}
```

---

## Use cases

- **Competitive intelligence** — Monitor competitor menus and pricing across cities
- **Menu database** — Build a structured database of restaurant menus at scale
- **Price monitoring** — Track price changes over time with scheduled daily runs
- **Market analysis** — Analyse cuisine trends and menu composition by region
- **Restaurant onboarding** — Import menu data into your own ordering or review platform
- **Food tech research** — Study menu diversity, item availability, and pricing patterns

---

## FAQ

**Which countries are supported?**  
United States (`us`), United Kingdom (`gb`), Australia (`au`), Canada (`ca`), and India (`in`). Always select the country that matches the restaurant's physical location for best results.

**Can I scrape multiple restaurants at once?**  
Yes — add as many URLs as you need to the `restaurantUrls` list. Each restaurant produces one output record. Restaurants are processed one at a time with a short polite delay between requests.

**How do I find a restaurant's URL?**  
Go to [ubereats.com](https://www.ubereats.com), search for the restaurant, open its page, and copy the URL from your browser's address bar. The URL will look like: `https://www.ubereats.com/store/<name>/<id>`.

**Are item descriptions always available?**  
No — UberEats restaurants often omit item descriptions. The `itemsWithDescCount` field tells you how many items in a restaurant's menu include descriptions. Images are much more commonly available.

**How fresh is the data?**  
Data is fetched live from UberEats at the time the actor runs. Use Apify's scheduling feature to run it daily for up-to-date menu and pricing data.

**Does this require a proxy or login?**  
No. The actor uses UberEats' public API with no authentication, login, or proxy required.

---

## Legal

This actor is for informational and research purposes only. Use in compliance with UberEats [Terms of Service](https://www.ubereats.com/legal/terms-of-use) and all applicable laws. Do not use to harm UberEats, its restaurant partners, or for unauthorized commercial data resale.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/ubereats-menu-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
