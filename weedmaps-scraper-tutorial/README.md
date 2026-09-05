# Weedmaps Scraper — Cannabis Dispensaries & Products Tutorial: Run This Apify Actor with Python

Scrape Weedmaps.com for cannabis dispensaries, products, and deals. Filter by state, city, dispensary type, product category, strain type, and more. Returns ratings, hours, menus, THC/CBD content, pricing and availability.

This repository shows how to run [Weedmaps Scraper — Cannabis Dispensaries & Products](https://apify.com/crawlerbros/weedmaps-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/weedmaps-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/weedmaps-scraper](https://apify.com/crawlerbros/weedmaps-scraper)
- **SEO title:** Weedmaps Scraper — Cannabis Dispensaries & Products Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Weedmaps.com for cannabis dispensaries, products, and deals. Filter by state, city, dispensary type, product category, strain type, and more. Returns ratings, hours, menus, THC/CBD content, pricing and availability.

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

# Weedmaps Scraper — Cannabis Dispensaries, Products & Deals

Scrape Weedmaps.com for cannabis dispensaries, delivery services, products, and deals. Filter by state, city, dispensary type, product category, strain type, rating, and more. Returns comprehensive data including ratings, hours, menus, THC/CBD content, pricing, and availability.

## What it does

- **Dispensaries** — search storefronts, delivery services, and medical marijuana doctors by state/city
- **Products** — search cannabis products (flower, edibles, concentrates, vapes, etc.) with strain type, THC/CBD levels, and pricing
- **Deals** — find current dispensary promotions and discounts by state

No API key or account required. Uses Weedmaps' public discovery API.

## Input

| Field | Type | Description |
|---|---|---|
| `mode` | select | `dispensaries` (default), `products`, `deals` |
| `stateSlug` | select | US state or Canadian province (e.g., `california`, `colorado`) |
| `citySlug` | string | City slug for narrower search (e.g., `los-angeles`, `denver`) |
| `dispensaryType` | select | `dispensary`, `delivery`, or `doctor` |
| `productCategory` | select | Product category: flower, edible, concentrate, vape, etc. |
| `searchQuery` | string | Free-text product search (mode=products) |
| `strainType` | select | `indica`, `sativa`, `hybrid`, `cbd` |
| `licenseType` | select | `recreational`, `medical`, or `hybrid` |
| `isVerified` | boolean | Verified listings only |
| `hasDelivery` | boolean | Only dispensaries with delivery |
| `hasPickup` | boolean | Only dispensaries with pickup |
| `isOpenNow` | boolean | Only currently open dispensaries |
| `minRating` | number | Minimum star rating (0–5) |
| `maxItems` | integer | Max results (1–500, default 20) |

### Example inputs

**California dispensaries:**
```json
{
  "mode": "dispensaries",
  "stateSlug": "california",
  "maxItems": 20
}
```

**Flower products in Colorado:**
```json
{
  "mode": "products",
  "stateSlug": "colorado",
  "productCategory": "flower",
  "strainType": "sativa",
  "maxItems": 30
}
```

**Deals in Los Angeles:**
```json
{
  "mode": "deals",
  "stateSlug": "california",
  "citySlug": "los-angeles",
  "maxItems": 25
}
```

**Delivery services in Denver:**
```json
{
  "mode": "dispensaries",
  "stateSlug": "colorado",
  "citySlug": "denver",
  "dispensaryType": "delivery",
  "hasDelivery": true,
  "maxItems": 20
}
```

## Output — Dispensary records

| Field | Description |
|---|---|
| `name` | Dispensary name |
| `slug` | URL slug |
| `url` | Weedmaps listing URL |
| `wmid` | Weedmaps' internal numeric dispensary ID |
| `type` | Type: `dispensary`, `delivery`, or `doctor` |
| `address` | Street address |
| `city` | City |
| `state` | State name |
| `zipCode` | ZIP/postal code |
| `country` | Country |
| `lat` | Latitude |
| `lng` | Longitude |
| `phone` | Phone number |
| `email` | Email address |
| `licenseType` | License type: `recreational`, `medical`, `hybrid` |
| `rating` | Star rating (0–5) |
| `reviewCount` | Number of reviews |
| `isOpen` | Currently open (boolean) |
| `todaysHours` | Today's hours string |
| `timezone` | Timezone |
| `services` | Available services list |
| `hasDelivery` | Offers delivery (boolean) |
| `hasPickup` | Offers pickup (boolean) |
| `hasCurbsidePickup` | Offers curbside pickup |
| `paymentMethods` | Accepted payments |
| `avatarUrl` | Logo/avatar image URL |
| `menuItemsCount` | Total menu item count |
| `hasFeaturedDeal` | Has active featured deal |
| `hasSaleItems` | Has at least one item currently on sale (boolean) |
| `closesInMinutes` | Minutes until closing (when open) |
| `hasAgeGate` | Requires an age-verification gate to view the menu (boolean) |
| `minAge` | Minimum age required, when `hasAgeGate` is true |
| `endorsementBadgeCount` | Number of customer endorsement badges |
| `promoCode` | Active storewide promo code, when available (`code`, `title`, `discount`, `discountType`, `appliesTo`) |
| `verifiedMenuItemsCount` | Number of menu items with a verified license match |
| `bestOfWeedmaps` | Holds a "Best of Weedmaps" award (boolean) |
| `socialEquity` | Registered social-equity business (boolean) |
| `packageLevel` | Weedmaps listing/subscription tier (e.g. `listing_plus`) |
| `regionId` | Weedmaps' internal numeric region ID |
| `description` | Business description |
| `sourceUrl` | Source URL |
| `scrapedAt` | UTC timestamp |
| `recordType` | Always `dispensary` |

## Output — Product records

| Field | Description |
|---|---|
| `name` | Product name |
| `url` | Weedmaps product URL |
| `category` | Category (Indica, Sativa, Flower, Edible, etc.) |
| `strainType` | Strain type (Indica/Sativa/Hybrid/CBD) |
| `brand` | Brand name |
| `price` | Price in USD |
| `onSale` | Whether on sale |
| `originalPrice` | Original price if on sale |
| `pricesByWeight` | Price per weight (eighth, quarter, half, ounce) |
| `thcContent` | THC percentage |
| `cbdContent` | CBD percentage |
| `cannabinoids` | Full cannabinoid data |
| `effects` | Effects list |
| `flavors` | Flavor list |
| `rating` | Product rating |
| `reviewCount` | Number of reviews |
| `imageUrl` | Product image URL |
| `isOnlineOrderable` | Orderable online |
| `createdAt` | When this product was added to the menu (ISO timestamp) |
| `updatedAt` | When the menu item was last updated (ISO timestamp) |
| `currentDealTitle` | Active deal summary for this product, e.g. `"10+ deals available"` (omitted when there's no active deal) |
| `discountLabel` | Discount badge when on sale (e.g. `-35%`) |
| `productId` | Weedmaps' internal numeric product ID |
| `menuId` | Menu-item ID for this product at the dispensary |
| `slug` | Product URL slug |
| `brandSlug` | Brand URL slug |
| `topCategory` | Top-level category (e.g. `Flower`) |
| `subCategory` | Sub-category (e.g. `Big Buds`) |
| `strains` | Strain name(s) list |
| `licenseType` | License type of the offering dispensary (`recreational`, `medical`, `hybrid`) |
| `priceLabel` | Human-readable price unit label (e.g. `each`) |
| `priceUnit` | Price unit code (e.g. `unit`, `gram`) |
| `thcUnit` | Unit for `thcContent` (e.g. `%`, `mg`) |
| `cbdUnit` | Unit for `cbdContent` (e.g. `%`, `mg`) |
| `isBadged` | Whether the product carries a Weedmaps badge (boolean) |
| `sourceUrl` | Source URL |
| `scrapedAt` | UTC timestamp |
| `recordType` | Always `product` |

## Output — Deal records

| Field | Description |
|---|---|
| `title` | Deal title |
| `body` | Deal description |
| `dealType` | Type of deal |
| `categories` | Deal category tag(s), e.g. `["Flower"]`, `["Edibles"]` |
| `productCategories` | Product category name(s) the deal applies to, e.g. `["Edible"]` |
| `isStorewide` | Applies storewide |
| `isFirstTimeCustomer` | First-time customer deal |
| `dispensaryName` | Offering dispensary name |
| `dispensaryCity` | Dispensary city |
| `dispensaryState` | Dispensary state |
| `dispensaryUrl` | Dispensary Weedmaps URL |
| `dispensaryWmid` | Offering dispensary's Weedmaps ID |
| `dispensaryType` | Dispensary type (`dispensary`, `delivery`, `doctor`) |
| `dispensaryRating` | Dispensary star rating |
| `dispensaryLicenseType` | Dispensary license type |
| `dispensaryHasDelivery` | Dispensary offers delivery (boolean) |
| `dispensaryHasPickup` | Dispensary offers pickup (boolean) |
| `imageUrl` | Deal image URL |
| `dealId` | Weedmaps' internal numeric deal ID |
| `slug` | Deal URL slug |
| `claimedCount` | Number of times the deal has been claimed |
| `likes` | Number of likes on the deal |
| `expiresIn` | Seconds until the deal expires |
| `sourceUrl` | Source URL |
| `scrapedAt` | UTC timestamp |
| `recordType` | Always `deal` |

## Supported states

All major US cannabis markets: California, Colorado, Washington, Oregon, Nevada, Arizona, Michigan, Illinois, Massachusetts, New York, New Jersey, New Mexico, Connecticut, Maryland, and more. Canadian provinces: British Columbia, Alberta, Ontario, Quebec.

## Frequently Asked Questions

**Do I need an account or API key?**
No. This actor uses Weedmaps' public discovery API, which requires no authentication.

**Can I filter by city?**
Yes — use the `citySlug` field with the city name in slug format: `los-angeles`, `san-francisco`, `denver`, `chicago`, etc.

**What product categories are available?**
flower, pre-roll, edible, concentrate, vape, tincture, topical, gear, clone, seed

**How accurate are the hours?**
The `isOpen` field and `todaysHours` reflect real-time data from Weedmaps at the time of scraping.

**Can I get delivery services only?**
Yes — set `dispensaryType` to `delivery` and `hasDelivery` to `true`.

**What's the THC/CBD data from?**
Cannabis product potency data is self-reported by dispensaries or from lab test results (where `is_badged` is true).

**How do I get the most local results?**
Combine `stateSlug` + `citySlug` for the most relevant results. Leave `citySlug` empty for statewide results.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/weedmaps-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
