# Amazon Bestseller Scraper Tutorial: Run This Apify Actor with Python

Scrapes Amazon Best Sellers, Movers and Shakers, New Releases, Most Wished For, and Most Gifted product lists. Extracts product details including name, price, URL, thumbnail, and position. Supports multiple Amazon domains: US, UK, DE, FR, ES, and IT

This repository shows how to run [Amazon Bestseller Scraper](https://apify.com/crawlerbros/amazon-bestseller-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/amazon-bestseller-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/amazon-bestseller-scraper](https://apify.com/crawlerbros/amazon-bestseller-scraper)
- **SEO title:** Amazon Bestseller Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrapes Amazon Best Sellers, Movers and Shakers, New Releases, Most Wished For, and Most Gifted product lists. Extracts product details including name, price, URL, thumbnail, and position. Supports multiple Amazon domains: US, UK, DE, FR, ES, and IT

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

# Amazon Best Sellers Scraper

Scrape Amazon Best Sellers, Movers and Shakers, New Releases, Most Wished For, and Most Gifted product lists. Extract up to 100 top-selling items per category with product details including name, price, URL, and thumbnail image.

## ⭐️ What is Amazon Best Sellers Scraper?

This Amazon Best Sellers Scraper allows you to scrape the top-selling items on Amazon. It extracts data from Amazon Best Sellers pages in structured formats such as JSON, XML, CSV, or Excel.

### Features

- Extract data from multiple Amazon domains: US (.com), UK (.co.uk), DE (.de), FR (.fr), ES (.es), and IT (.it)
- Extract all Best Seller product details: name, price, URL, thumbnail image, rating, and reviews count
- Scrape Amazon Best Seller categories and subcategories
- Support for multiple Amazon list types:
  - **Best Sellers** - Top selling products
  - **Movers and Shakers** - Biggest gainers in sales rank
  - **New Releases** - Best selling new and future releases
  - **Most Wished For** - Most added to wishlists and registries
  - **Most Gifted** - Most gifted products

## Supported Amazon Domains

| Domain       | Country        |
| ------------ | -------------- |
| amazon.com   | United States  |
| amazon.co.uk | United Kingdom |
| amazon.de    | Germany        |
| amazon.fr    | France         |
| amazon.it    | Italy          |
| amazon.es    | Spain          |

## 📚 How to Scrape Amazon Best Sellers

1. Create a free Apify account using your email
2. Open Amazon Best Sellers Scraper
3. Add one or more Amazon category URLs to scrape
4. Click "Start" and wait for the data to be extracted
5. Download your data in JSON, XML, CSV, Excel, or HTML

## Input Parameters

| Parameter             | Type    | Required | Default | Description                            |
| --------------------- | ------- | -------- | ------- | -------------------------------------- |
| `categoryUrls`        | array   | Yes      | -       | Amazon Best Sellers URLs to scrape     |
| `maxItems`            | integer | No       | 100     | Maximum items per category (max 100)   |
| `scrapeSubcategories` | boolean | No       | false   | Also scrape subcategories              |
| `maxSubcategoryDepth` | integer | No       | 1       | How deep to crawl subcategories (1-3)  |
| `proxyCountry`        | string  | No       | AUTO    | Proxy country (AUTO selects by domain) |
| `rateLimitDelay`      | integer | No       | 2       | Delay between requests in seconds      |

## ⬇️ Input Examples

### Best Sellers Category

```json
{
  "categoryUrls": [
    "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/"
  ]
}
```

### Multiple Categories

```json
{
  "categoryUrls": [
    "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/",
    "https://www.amazon.com/Best-Sellers-Books/zgbs/books/",
    "https://www.amazon.com/Best-Sellers-Home-Kitchen/zgbs/home-garden/"
  ]
}
```

### Different List Types

```json
{
  "categoryUrls": [
    "https://www.amazon.com/Best-Sellers-Appliances/zgbs/appliances/",
    "https://www.amazon.de/-/en/gp/movers-and-shakers/garden/",
    "https://www.amazon.co.uk/gp/new-releases/",
    "https://www.amazon.es/gp/most-wished-for/",
    "https://www.amazon.fr/gp/most-gifted/books/"
  ]
}
```

### With Subcategories

```json
{
  "categoryUrls": [
    "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/"
  ],
  "scrapeSubcategories": true,
  "maxSubcategoryDepth": 2,
  "maxItems": 50
}
```

### Multiple Domains

```json
{
  "categoryUrls": [
    "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/",
    "https://www.amazon.co.uk/Best-Sellers-Electronics/zgbs/electronics/",
    "https://www.amazon.de/gp/bestsellers/ce-de/"
  ],
  "proxyCountry": "AUTO"
}
```

## ⬆️ Output Fields

| Field            | Type   | Description                                  |
| ---------------- | ------ | -------------------------------------------- |
| `position`       | number | Rank/position in the bestseller list (1-100) |
| `category`       | string | Category name with list type prefix          |
| `categoryUrl`    | string | URL of the category page                     |
| `name`           | string | Product name/title                           |
| `asin`           | string | Amazon Standard Identification Number        |
| `price`          | number | Product price (numeric value)                |
| `currency`       | string | Currency symbol ($, £, €, etc.)              |
| `numberOfOffers` | number | Number of sellers/offers                     |
| `url`            | string | Direct product page URL                      |
| `thumbnail`      | string | Product thumbnail image URL                  |
| `rating`         | number | Average star rating (0-5)                    |
| `reviewsCount`   | number | Total number of reviews                      |
| `scrapedAt`      | string | ISO timestamp when data was scraped          |

## Output Example

```json
[
  {
    "position": 1,
    "category": "Amazon Best Sellers: Best Electronics",
    "categoryUrl": "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/",
    "name": "Amazon Fire TV Stick 4K, brilliant 4K streaming quality, TV and smart home controls, free and live TV",
    "asin": "B08XVYZ1Y5",
    "price": 22.99,
    "currency": "$",
    "numberOfOffers": 1,
    "url": "https://www.amazon.com/dp/B08XVYZ1Y5",
    "thumbnail": "https://images-na.ssl-images-amazon.com/images/I/41GYmjbeVSL._AC_UL600_SR600,400_.jpg",
    "rating": 4.5,
    "reviewsCount": 125432,
    "scrapedAt": "2026-01-26T12:00:00.000Z"
  },
  {
    "position": 2,
    "category": "Amazon Best Sellers: Best Electronics",
    "categoryUrl": "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/",
    "name": "Apple AirTag",
    "asin": "B0933BVK6T",
    "price": 28.99,
    "currency": "$",
    "numberOfOffers": 1,
    "url": "https://www.amazon.com/dp/B0933BVK6T",
    "thumbnail": "https://images-na.ssl-images-amazon.com/images/I/713xuNx00oS._AC_UL600_SR600,400_.jpg",
    "rating": 4.7,
    "reviewsCount": 98234,
    "scrapedAt": "2026-01-26T12:00:00.000Z"
  }
]
```

## ☝️ Tips and Tricks

- **Pagination**: Amazon shows up to 50 items per page, with a maximum of 100 items per category (2 pages). The scraper automatically handles both pages.

- **Subcategory Crawling**: Enable `scrapeSubcategories` to get products from all subcategories. Use `maxSubcategoryDepth` to control how deep to crawl. Be aware this significantly increases run time and results.

- **Rate Limiting**: The default 2-second delay between requests helps avoid detection. Increase `rateLimitDelay` if you encounter issues.

- **Proxy Selection**: Use `AUTO` to automatically select the best proxy based on the Amazon domain. This ensures better success rates.

## 📦 How Many Results?

- Each category can return up to **100 products** (the maximum shown on Amazon)
- With subcategory scraping enabled, you can collect **thousands of products** depending on the category depth
- Results may vary based on category, location, and Amazon's current listings

## ❓ FAQ

### Do I need proxies to scrape Amazon?

For reliable results, the scraper uses Apify Proxy by default. You can also use custom HTTP or SOCKS5 proxy servers by specifying them in the proxy configuration.

### Can I integrate Amazon Best Sellers Scraper with other apps?

Yes! You can integrate with Make, Zapier, LangChain, Slack, Airbyte, GitHub, Google Sheets, Google Drive, and more through the Apify platform.

### Can I use Amazon Best Sellers Scraper with API?

Yes, you can use the Apify API to programmatically run this scraper, schedule runs, and fetch results. Use the `apify-client` NPM package for Node.js or the `apify-client` PyPI package for Python.

### What can I do with Amazon Best Sellers data?

- **Market Research**: Track trending products and categories
- **Competitive Analysis**: Monitor competitor products and pricing
- **Product Discovery**: Find hot-selling items for your e-commerce business
- **Price Monitoring**: Track price changes of top products
- **Trend Analysis**: Identify emerging product trends

## Resources

- [Apify Platform Documentation](https://docs.apify.com/)
- [Amazon Scraping Guide](https://blog.apify.com/how-to-scrape-amazon/)
- [Web Scraping Legal Guide](https://blog.apify.com/is-web-scraping-legal/)

## Feedback

Found a bug or have suggestions? Please create an issue on the Actor's Issues tab in Apify Console.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/amazon-bestseller-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
