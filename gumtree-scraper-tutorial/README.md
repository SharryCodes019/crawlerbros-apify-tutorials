# Gumtree Scraper Tutorial: Run This Apify Actor with Python

Scrape listings from Gumtree Australia (.com.au), Gumtree UK (.com), and Gumtree South Africa (.co.za). Extract titles, prices, descriptions, images, seller info, location, and more from search results and individual listing pages.

This repository shows how to run [Gumtree Scraper](https://apify.com/crawlerbros/gumtree-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/gumtree-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/gumtree-scraper](https://apify.com/crawlerbros/gumtree-scraper)
- **SEO title:** Gumtree Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape listings from Gumtree Australia (.com.au), Gumtree UK (.com), and Gumtree South Africa (.co.za). Extract titles, prices, descriptions, images, seller info, location, and more from search results and individual listing pages.

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

# Gumtree Scraper

Scrape listings from **Gumtree Australia** (.com.au), **Gumtree UK** (.com), and **Gumtree South Africa** (.co.za). Extract structured data including titles, prices, descriptions, images, seller information, location, attributes, and more from search results and individual listing pages.

## Features

- Scrapes **3 Gumtree domains**: Australia, UK, and South Africa
- Extracts data from **search result pages** and **individual listing pages**
- Supports **pagination** — automatically follows multiple pages up to your limit
- Extracts **rich listing details** including descriptions, all images, seller info, and category-specific attributes
- **No browser required** — uses lightweight HTTP requests for fast, cost-effective scraping
- Handles **rate limiting** and retries automatically

## Supported Domains

| Domain | URL Pattern | Example |
|--------|-------------|---------|
| Gumtree Australia | `gumtree.com.au` | `https://www.gumtree.com.au/s-cars-vans-utes/c18320` |
| Gumtree UK | `gumtree.com` | `https://www.gumtree.com/search?q=laptop` |
| Gumtree South Africa | `gumtree.co.za` | `https://www.gumtree.co.za/s-cars-bakkies/v1c9077p1` |

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `startUrls` | Array | **Yes** | — | URLs to scrape. Can be search result pages or individual listing pages from any supported Gumtree domain. |
| `maxItems` | Integer | No | `100` | Maximum number of listings to scrape per start URL. |
| `includeListingDetails` | Boolean | No | `true` | Whether to visit each listing page for full details (description, all images, seller info). Disable for faster but less detailed scraping. |
| `cookies` | Array | No | `[]` | Browser cookies (EditThisCookie format) for Gumtree Australia bypass. Required for AU due to Akamai bot protection. |
| `proxy` | Object | No | Apify Residential | Proxy configuration. Residential proxies are required for Australian domain. |

## Architecture

The scraper automatically detects the domain from your URL and routes requests accordingly:

- **UK (.com) and ZA (.co.za)** → Fast HTTP requests with httpx (no browser needed)
- **AU (.com.au)** → Browser-fingerprinted requests with impit, falling back to Playwright with stealth

This hybrid approach keeps costs low for UK/ZA while providing browser emulation where needed for AU.

## Input Example

```json
{
    "startUrls": [
        { "url": "https://www.gumtree.com/search?q=bicycle" },
        { "url": "https://www.gumtree.co.za/s-cars-bakkies/v1c9077p1" }
    ],
    "maxItems": 50,
    "includeListingDetails": true,
    "proxy": {
        "useApifyProxy": true
    }
}
```

## Output Fields

| Field | Type | Description |
|-------|------|-------------|
| `adId` | String | Unique listing identifier |
| `title` | String | Listing title |
| `description` | String | Full listing description (text only) |
| `price` | String | Price amount |
| `currency` | String | Currency code (GBP, AUD, ZAR) |
| `priceType` | String | Price type (FIXED, NEGOTIABLE, CONTACT_ME, MAKE_OFFER) |
| `location` | String | Location name |
| `latitude` | Number | GPS latitude (when available) |
| `longitude` | Number | GPS longitude (when available) |
| `category` | String | Listing category |
| `imageUrl` | String | Primary image URL |
| `images` | Array | All image URLs |
| `sellerName` | String | Seller/dealer name |
| `sellerType` | String | Seller type (Private, Trade, Dealer) |
| `postedDate` | String | When the listing was posted |
| `attributes` | Object | Category-specific attributes (e.g., car make, year, mileage, condition) |
| `link` | String | Direct URL to the listing |
| `sourceUrl` | String | The start URL this listing was found from |
| `domain` | String | Domain identifier (au, uk, za) |
| `extractedAt` | String | ISO timestamp of when data was extracted |

## Output Example

```json
{
    "adId": "1511110656",
    "title": "HP i7 32GB Ram 2TB SSD High Spec Laptop NVIDIA RTX 4GB",
    "description": "HP ZBook Studio i7 11th Gen...",
    "price": "650.00",
    "currency": "GBP",
    "priceType": "",
    "location": "Sunderland, Tyne and Wear",
    "latitude": null,
    "longitude": null,
    "category": "PC Laptops & Netbooks",
    "imageUrl": "https://img.gumtree.com/...",
    "images": ["https://img.gumtree.com/..."],
    "sellerName": "JUNIOR",
    "sellerType": "Trade",
    "postedDate": "13 days",
    "attributes": {
        "Condition": "As good as new"
    },
    "link": "https://www.gumtree.com/p/laptops/hp-i7-laptop/1511110656",
    "sourceUrl": "https://www.gumtree.com/search?q=laptop",
    "domain": "uk",
    "extractedAt": "2026-04-04T06:40:25.164694+00:00"
}
```

## How to Use

1. **Go to the Gumtree Scraper** actor page on Apify
2. **Add Start URLs** — paste one or more Gumtree search or listing URLs
3. **Set Max Items** — choose how many listings you want per URL
4. **Run the actor** — results appear in the Dataset tab
5. **Export data** — download as JSON, CSV, Excel, or connect via API

## URL Types

### Search URLs
Navigate to any Gumtree search page and copy the URL:
- **UK**: `https://www.gumtree.com/search?q=laptop&max_price=500`
- **AU**: `https://www.gumtree.com.au/s-cars-vans-utes/perth/c18320l3008303`
- **ZA**: `https://www.gumtree.co.za/s-cars-bakkies/v1c9077p1`

### Individual Listing URLs
Copy the URL of any individual listing:
- **UK**: `https://www.gumtree.com/p/laptops/my-laptop/1511110656`
- **AU**: `https://www.gumtree.com.au/s-ad/sydney/cars/my-car/1341427739`
- **ZA**: `https://www.gumtree.co.za/a-cars/pretoria/my-car/10013428956741013052980009`

## Proxy Configuration

- **UK and ZA** domains work reliably with standard Apify proxy (or without proxy)
- **AU domain** requires residential proxies and may need user-provided session cookies due to Akamai Bot Manager protection

### How to get AU cookies (optional but recommended)

1. Open Gumtree Australia in your browser: https://www.gumtree.com.au
2. Install the [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg) Chrome extension
3. Click the extension icon and click "Export"
4. Paste the JSON cookies array into the `cookies` input field

## FAQ

**Q: Which Gumtree domains are supported?**
A: Gumtree Australia (.com.au), Gumtree UK (.com), and Gumtree South Africa (.co.za).

**Q: Can I scrape multiple domains in one run?**
A: Yes! Add URLs from different domains to the Start URLs array. The scraper automatically detects the domain.

**Q: Why are some fields empty?**
A: Field availability varies by domain and listing type. UK listings may not have latitude/longitude. Some sellers don't provide all details. Setting `includeListingDetails: true` maximizes data completeness.

**Q: How fast is the scraper?**
A: The scraper uses HTTP requests (no browser), making it very fast. With `includeListingDetails: false`, it can process hundreds of listings per minute. With details enabled, it's limited by the 1-second delay between detail page requests.

**Q: Do I need a proxy?**
A: For UK and South Africa, the scraper works without proxy. Australia has strong anti-bot protection and may not work with HTTP-only requests — a browser-based approach may be needed for AU.

**Q: What is the `attributes` field?**
A: This contains category-specific details. For cars, it may include Year, Mileage, Fuel Type, etc. For electronics, it may include Condition, Brand, etc. The available attributes depend on the listing category.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/gumtree-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
