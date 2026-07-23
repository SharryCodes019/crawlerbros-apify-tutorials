# Kleinanzeigen Scraper Tutorial: Run This Apify Actor with Python

Scrape classified listings from Kleinanzeigen.de (formerly eBay Kleinanzeigen). Extract listing details including title, price, description, location, seller info, images, and category-specific attributes.

This repository shows how to run [Kleinanzeigen Scraper](https://apify.com/crawlerbros/kleinanzeigen-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/kleinanzeigen-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/kleinanzeigen-scraper](https://apify.com/crawlerbros/kleinanzeigen-scraper)
- **SEO title:** Kleinanzeigen Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape classified listings from Kleinanzeigen.de (formerly eBay Kleinanzeigen). Extract listing details including title, price, description, location, seller info, images, and category-specific attributes.

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

# Kleinanzeigen.de Scraper

Scrape classified listings from **Kleinanzeigen.de** (formerly eBay Kleinanzeigen), Germany's largest classifieds marketplace. Extract detailed information including prices, descriptions, images, seller details, and more.

## Features

- **Search Results Scraping**: Scrape any search URL with automatic pagination
- **Detail Page Extraction**: Get full descriptions, all images, and seller info
- **All Categories Supported**: Cars, electronics, real estate, furniture, jobs, etc.
- **German Format Handling**: Correctly parses German prices (1.990 €) and dates
- **Price & Seller Filters**: Filter by price range or seller type (private/commercial)
- **Anti-Detection**: Stealth scripts, rate limiting, and proxy support
- **Cookie Consent Handling**: Automatically handles GDPR popups

## Important: Proxy Required

**Kleinanzeigen.de blocks datacenter IPs.** You must use **Residential proxies with German IPs** for reliable scraping.

Recommended proxy configuration:
```json
{
    "useApifyProxy": true,
    "apifyProxyGroups": ["RESIDENTIAL"],
    "apifyProxyCountry": "DE"
}
```

## Input Examples

### Scrape Cars Category
```json
{
    "searchUrls": ["https://www.kleinanzeigen.de/s-autos/k0c216"],
    "maxListings": 100,
    "scrapeDetails": true,
    "proxyConfiguration": {
        "useApifyProxy": true,
        "apifyProxyGroups": ["RESIDENTIAL"],
        "apifyProxyCountry": "DE"
    }
}
```

### Scrape with Price Filter
```json
{
    "searchUrls": ["https://www.kleinanzeigen.de/s-elektronik/k0c161"],
    "maxListings": 50,
    "minPrice": 100,
    "maxPrice": 500,
    "sellerType": "private",
    "proxyConfiguration": {
        "useApifyProxy": true,
        "apifyProxyGroups": ["RESIDENTIAL"],
        "apifyProxyCountry": "DE"
    }
}
```

### Scrape Specific Listings
```json
{
    "listingUrls": [
        "https://www.kleinanzeigen.de/s-anzeige/example/123456-216"
    ],
    "proxyConfiguration": {
        "useApifyProxy": true,
        "apifyProxyGroups": ["RESIDENTIAL"],
        "apifyProxyCountry": "DE"
    }
}
```

## Output Schema

Each listing contains the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `listingId` | string | Unique listing identifier |
| `listingUrl` | string | Full URL to the listing |
| `title` | string | Listing title |
| `description` | string | Full description (with detail scraping) |
| `price` | number | Price in EUR (numeric) |
| `priceText` | string | Original price text (e.g., "1.990 € VB") |
| `priceType` | string | FIXED, NEGOTIABLE, FREE, or ON_REQUEST |
| `isNegotiable` | boolean | Whether price is negotiable (VB) |
| `isFree` | boolean | Whether item is free |
| `postalCode` | string | Postal code |
| `city` | string | City/location name |
| `region` | string | Region/state (Bundesland) |
| `locationText` | string | Full location text |
| `category` | string | Category name |
| `categoryPath` | string | Full category path |
| `categoryId` | string | Category ID |
| `sellerId` | string | Seller's user ID |
| `sellerName` | string | Seller's display name |
| `sellerType` | string | PRIVATE or COMMERCIAL |
| `sellerProfileUrl` | string | URL to seller's profile |
| `sellerMemberSince` | string | Date the seller joined Kleinanzeigen |
| `images` | array | List of image URLs |
| `thumbnailUrl` | string | Thumbnail image URL |
| `imageCount` | number | Number of images |
| `datePosted` | string | Original posting date |
| `datePostedISO` | string | ISO formatted date |
| `lastModified` | string | Last modification date |
| `scrapedAt` | string | Timestamp of scraping |
| `isActive` | boolean | Whether listing is active |
| `isTopAd` | boolean | Whether it's a promoted listing |
| `shippingAvailable` | boolean | Whether shipping is offered |
| `shippingCost` | string | Shipping cost if specified |
| `viewCount` | number | Number of listing views (if available) |
| `attributes` | object | Category-specific attributes (e.g., mileage, condition) |
| `searchUrl` | string | The search URL this listing was found from |
| `position` | number | Position in search results |

## Sample Output

```json
{
    "listingId": "3232063424",
    "listingUrl": "https://www.kleinanzeigen.de/s-anzeige/bmw-116i-74-000km-/3232063424-216-1914",
    "title": "BMW 116i 74.000KM!",
    "description": "Biete hier meinen fast ungenutzten BMW an...",
    "price": 6500,
    "priceText": "6.500 € VB",
    "priceType": "NEGOTIABLE",
    "isNegotiable": true,
    "isFree": false,
    "postalCode": "49479",
    "city": "Nordrhein-Westfalen - Ibbenbüren",
    "locationText": "49479 Nordrhein-Westfalen - Ibbenbüren",
    "category": "Kleinanzeigen Auto, Rad & Boot Autos",
    "sellerId": "22181186",
    "sellerName": "Kevin",
    "sellerType": "PRIVATE",
    "sellerProfileUrl": "https://www.kleinanzeigen.de/s-bestandsliste.html?userId=22181186",
    "images": [
        "https://img.kleinanzeigen.de/api/v1/prod-ads/images/26/26c18b06-2d56-47be-ade3-9dbdcdccbc49",
        "..."
    ],
    "imageCount": 12,
    "datePosted": "31.10.2025",
    "datePostedISO": "2025-10-31T00:00:00",
    "scrapedAt": "2026-01-23T08:14:45.375276",
    "isActive": true,
    "isTopAd": false,
    "shippingAvailable": false
}
```

## Supported Categories

You can scrape any category on Kleinanzeigen.de:

- **Autos** (`/s-autos/k0c216`)
- **Electronics** (`/s-elektronik/k0c161`)
- **Real Estate** (`/s-immobilien/k0c195`)
- **Jobs** (`/s-jobs/k0c102`)
- **Furniture** (`/s-moebel/k0c86`)
- **Fashion** (`/s-mode/k0c153`)
- **Pets** (`/s-haustiere/k0c130`)
- And many more...

## Tips for Best Results

1. **Use Residential Proxies**: Datacenter IPs are blocked
2. **Use German IPs**: Set `apifyProxyCountry: "DE"` for best success rate
3. **Enable Detail Scraping**: Set `scrapeDetails: true` for complete data
4. **Reasonable Rate Limits**: Keep `rateLimitDelay` at 2-3 seconds
5. **Handle Failures**: Some residential IPs may still be blocked; the scraper will retry automatically

## Limitations

- Requires residential proxies (additional cost)
- Some residential IPs may be blocked; success rate varies
- Rate limited to avoid detection
- Detail scraping is slower but provides complete data

## FAQ

**Do I need to log in to scrape Kleinanzeigen.de?**
No. All public listings are accessible without an account. The scraper handles cookie consent popups automatically.

**Why are residential proxies required?**
Kleinanzeigen.de blocks datacenter IP ranges. You must use residential proxies with German IPs (`apifyProxyCountry: "DE"`) for reliable access.

**What is the difference between `searchUrls` and `listingUrls`?**
`searchUrls` are search results pages (the scraper paginates through them and collects all matching listings). `listingUrls` are direct links to individual listings — the scraper fetches each one without searching.

**Does `scrapeDetails: false` save time?**
Yes. When `scrapeDetails` is disabled, the scraper collects data only from the search result cards, which is faster but yields fewer fields (no full description, fewer images, limited seller info).

**Can I filter by price or seller type?**
Yes — use `minPrice`, `maxPrice`, and `sellerType` input fields. `sellerType` accepts `private`, `commercial`, or leave empty for both.

**How many listings can I scrape?**
Up to 1,000 listings per search URL (`maxListings`), across up to 50 pages (`maxPages`). Each search results page contains approximately 25 listings.

**What categories are supported?**
All Kleinanzeigen.de categories are supported. Copy the URL of any search results page from the website and use it as a `searchUrls` entry.

## Support

If you encounter issues:
1. Ensure you're using Residential proxies with German IPs
2. Try increasing `rateLimitDelay` to 3-4 seconds
3. Check the run logs for specific error messages

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/kleinanzeigen-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
