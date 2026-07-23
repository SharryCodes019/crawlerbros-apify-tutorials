# Facebook Marketplace Scraper Tutorial: Run This Apify Actor with Python

Extract data from Facebook Marketplace listings. Scrape items for sale, apartments, categories, search results with prices, locations, seller info, and more. Export data in JSON, CSV, or Excel.

This repository shows how to run [Facebook Marketplace Scraper](https://apify.com/crawlerbros/facebook-marketplace-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/facebook-marketplace-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/facebook-marketplace-scraper](https://apify.com/crawlerbros/facebook-marketplace-scraper)
- **SEO title:** Facebook Marketplace Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract data from Facebook Marketplace listings. Scrape items for sale, apartments, categories, search results with prices, locations, seller info, and more. Export data in JSON, CSV, or Excel.

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

# Facebook Marketplace Scraper

Extract data from [Facebook Marketplace](https://www.facebook.com/marketplace/) listings — items for sale, apartments, vehicles, categories, and search results with prices, locations, and more.

## Features

- Scrape by location, category, or search query
- Extract listing details: title, price, photos, location, seller info, delivery types
- Optional detail page enrichment for 70+ additional fields
- No login or cookies required
- Anti-detection with stealth browser settings
- Residential proxy support for best results

## Input

| Field                   | Type    | Description                                        | Default           |
| ----------------------- | ------- | -------------------------------------------------- | ----------------- |
| `startUrls`             | array   | Facebook Marketplace URLs to scrape                | (required)        |
| `resultsLimit`          | integer | Maximum number of listings per URL                 | 50                |
| `includeListingDetails` | boolean | Visit each listing's detail page for enriched data | false             |
| `proxyConfiguration`    | object  | Proxy settings (residential recommended)           | Apify residential |

### Supported URL Types

The scraper accepts three types of Facebook Marketplace URLs:

- **Location**: `https://www.facebook.com/marketplace/sanfrancisco/`
- **Category**: `https://www.facebook.com/marketplace/sanfrancisco/instruments`
- **Search query**: `https://www.facebook.com/marketplace/sanfrancisco/search/?query=crane`

## Output

Each listing in the dataset contains the following core fields:

| Field                                              | Description                                                                          |
| -------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `facebookUrl`                                      | The source Marketplace URL that was scraped                                          |
| `listingUrl`                                       | Direct URL to the listing's detail page                                              |
| `id`                                               | Unique Facebook listing ID                                                           |
| `marketplace_listing_title`                        | Listing title                                                                        |
| `listing_price`                                    | Price object with `formatted_amount`, `amount`, and `amount_with_offset_in_currency` |
| `strikethrough_price`                              | Original price if item is on sale                                                    |
| `primary_listing_photo`                            | Main photo with image URI                                                            |
| `location`                                         | City, state, and display name                                                        |
| `marketplace_listing_category_id`                  | Category ID                                                                          |
| `marketplace_listing_seller`                       | Seller name and ID (requires authentication)                                         |
| `delivery_types`                                   | Delivery options (e.g., `IN_PERSON`, `SHIPPING`, `PUBLIC_MEETUP`)                    |
| `is_hidden` / `is_live` / `is_pending` / `is_sold` | Listing status flags                                                                 |
| `listing_video`                                    | Video info if the listing has a video                                                |

### Enriched Fields (when `includeListingDetails` is enabled)

With detail page enrichment, each listing gains 50+ additional fields including:

| Field                  | Description                                 |
| ---------------------- | ------------------------------------------- |
| `redacted_description` | Full listing description text               |
| `creation_time`        | Unix timestamp when the listing was created |
| `item_location`        | Precise latitude and longitude              |
| `attribute_data`       | Condition, brand, and other attributes      |
| `commerce_badges_info` | Seller badges and ratings                   |
| `cross_post_info`      | Cross-posting details                       |
| `share_uri`            | Shareable listing URL                       |
| `shipping_offered`     | Whether shipping is available               |
| `search_pivots`        | Related search terms                        |

## Example Input

```json
{
  "startUrls": [
    { "url": "https://www.facebook.com/marketplace/nyc/search/?query=laptop" }
  ],
  "resultsLimit": 20,
  "includeListingDetails": false,
  "proxyConfiguration": {
    "useApifyProxy": true,
    "apifyProxyGroups": ["RESIDENTIAL"]
  }
}
```

## Example Output

```json
{
  "facebookUrl": "https://www.facebook.com/marketplace/nyc/search/?query=laptop",
  "listingUrl": "https://www.facebook.com/marketplace/item/772594759027016",
  "id": "772594759027016",
  "primary_listing_photo": {
    "__typename": "ProductImage",
    "image": {
      "uri": "https://scontent.xx.fbcdn.net/v/..."
    },
    "id": "1289962259761841"
  },
  "listing_price": {
    "formatted_amount": "$130",
    "amount_with_offset_in_currency": "13000",
    "amount": "130.00"
  },
  "strikethrough_price": null,
  "comparable_price": null,
  "comparable_price_type": null,
  "location": {
    "reverse_geocode": {
      "city": "New York",
      "state": "NY",
      "city_page": {
        "display_name": "New York, New York",
        "id": "108424279189115"
      }
    }
  },
  "is_hidden": false,
  "is_live": true,
  "is_pending": false,
  "is_sold": false,
  "is_viewer_seller": false,
  "min_listing_price": null,
  "max_listing_price": null,
  "marketplace_listing_category_id": "1792291877663080",
  "marketplace_listing_title": "HP 14\" HD Laptop, Intel Processor N150",
  "custom_title": null,
  "custom_sub_titles_with_rendering_flags": [],
  "origin_group": null,
  "listing_video": null,
  "parent_listing": null,
  "marketplace_listing_seller": {
    "__typename": "User",
    "name": "",
    "id": ""
  },
  "delivery_types": ["IN_PERSON"]
}
```

## Known Limitations

- **Seller data**: Facebook does not expose seller names/IDs to logged-out users. The `marketplace_listing_seller` fields will be empty unless authenticated cookies are provided.
- **Geo-restrictions**: Results depend on the proxy/IP location. Using a residential proxy in the target region yields the best results.
- **Rate limiting**: Facebook may temporarily block requests if too many are made in a short period. The scraper handles this gracefully with retries and status messages.

## FAQ

### Does Facebook Marketplace have an API?

Facebook Marketplace does not have a public API for retrieving listing data. This scraper provides an alternative way to programmatically access Marketplace data.

### How much does it cost to scrape Facebook Marketplace?

The actor runs on the Apify platform where you pay for compute units consumed. With the free tier, you get $5/month in credits. Enabling `includeListingDetails` increases cost since it visits each listing's detail page individually.

### What proxy should I use?

Residential proxies are recommended for best results. The scraper includes residential proxy as the default configuration. Datacenter proxies may work but are more likely to be blocked.

### Is it legal to scrape Facebook Marketplace?

This scraper only extracts publicly available data. It does not access any private user information. However, you should ensure your use case complies with applicable laws and Facebook's terms of service. Consult legal counsel if unsure.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/facebook-marketplace-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
