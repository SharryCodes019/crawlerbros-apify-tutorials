# eBay Motors Vehicle & Parts Scraper Tutorial: Run This Apify Actor with Python

Scrape eBay Motors listings for cars, trucks, motorcycles, boats, RVs, ATVs, and parts. Search by keyword, vehicle type, condition, price range, and year. Returns full listing details including price, mileage, specs, seller info, and images.

This repository shows how to run [eBay Motors Vehicle & Parts Scraper](https://apify.com/crawlerbros/ebay-motors-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/ebay-motors-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/ebay-motors-scraper](https://apify.com/crawlerbros/ebay-motors-scraper)
- **SEO title:** eBay Motors Vehicle & Parts Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape eBay Motors listings for cars, trucks, motorcycles, boats, RVs, ATVs, and parts. Search by keyword, vehicle type, condition, price range, and year. Returns full listing details including price, mileage, specs, seller info, and images.

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

# eBay Motors Vehicle & Parts Scraper

Extract vehicle listings, parts & accessories from eBay Motors — prices, specs, mileage, seller info, images, and more.

## What You Can Scrape

- **Vehicle listings** — cars, trucks, motorcycles, boats, RVs, ATVs, commercial trucks
- **Parts & accessories** — car parts, motorcycle parts, boat parts, ATV parts
- **Individual listings** — enrich specific eBay Motors item URLs with full detail
- **Pricing data** — asking price, auction bids, shipping costs
- **Vehicle specs** — year, make, model, trim, mileage, body style, fuel type, transmission, drivetrain, color
- **Seller info** — seller name, feedback score, positive percentage
- **Media** — primary image, full image gallery URLs
- **Listing metadata** — condition, listing type (Buy It Now / Auction / Best Offer), watch count, time remaining

## Input

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `mode` | Select | `searchVehicles` | `searchVehicles` — search by keyword and vehicle type; `searchParts` — search parts & accessories; `byListingUrls` — scrape specific listing URLs |
| `searchQuery` | Text | `toyota camry` | Keyword(s) to search for (e.g., "honda civic", "ford mustang gt") |
| `vehicleType` | Select | `cars-trucks` | Vehicle category for `searchVehicles` mode: Cars & Trucks, Motorcycles, Boats, RVs & Campers, ATVs, Commercial Trucks, Other |
| `partCategory` | Select | `car-truck-parts` | Parts category for `searchParts` mode: Car & Truck Parts, Motorcycle Parts, Boat Parts, ATV Parts, Other |
| `condition` | Select | `all` | Filter by condition: All, New, Used, Certified Pre-Owned, For Parts/Not Working |
| `sortBy` | Select | `best-match` | Sort order: Best Match, Price Lowest, Price Highest, Newly Listed, Ending Soonest, Distance Nearest |
| `minPrice` | Integer | — | Minimum listing price in USD |
| `maxPrice` | Integer | — | Maximum listing price in USD |
| `minYear` | Integer | — | Minimum model year (e.g., 2015) |
| `maxYear` | Integer | — | Maximum model year (e.g., 2024) |
| `startUrls` | List | — | eBay Motors listing URLs for `byListingUrls` mode |
| `maxItems` | Integer | `50` | Maximum number of listings to return (1–5000) |

## Output

Each record in the dataset contains:

| Field | Type | Description |
|-------|------|-------------|
| `listingId` | String | eBay item ID |
| `title` | String | Full listing title |
| `url` | String | Canonical eBay listing URL |
| `price` | Float | Numeric price in USD |
| `priceFormatted` | String | Formatted price (e.g., "$22,500") |
| `originalPrice` | Float | Original price before discount (if on sale) |
| `condition` | String | Listing condition (e.g., "Used", "New") |
| `mileage` | Integer | Vehicle mileage (if available) |
| `year` | Integer | Model year |
| `make` | String | Vehicle make (e.g., "Toyota") |
| `model` | String | Vehicle model (e.g., "Camry") |
| `trim` | String | Trim level (e.g., "SE", "XLE") |
| `bodyStyle` | String | Body style (e.g., "Sedan", "SUV") |
| `fuelType` | String | Fuel type (e.g., "Gasoline", "Electric") |
| `transmission` | String | Transmission type |
| `drivetrain` | String | Drivetrain (e.g., "FWD", "AWD", "4WD") |
| `exteriorColor` | String | Exterior color |
| `sellerName` | String | Seller username |
| `sellerUrl` | String | Seller profile URL |
| `sellerFeedbackScore` | Integer | eBay feedback score |
| `sellerPositivePercent` | Float | Positive feedback percentage |
| `shippingCost` | Float | Shipping cost in USD (0.0 = free) |
| `shippingType` | String | Shipping type: "Free", "Calculated", "Freight" |
| `location` | String | Seller location (city, state) |
| `imageUrl` | String | Primary listing image URL |
| `images` | List | All listing image URLs |
| `listingType` | String | "BuyItNow", "Auction", or "BestOffer" |
| `timeRemaining` | String | Time remaining on auction |
| `bids` | Integer | Number of bids (auction listings) |
| `watchCount` | Integer | Number of watchers |
| `viewCount` | Integer | Number of views |
| `vehicleType` | String | Vehicle category (e.g., "cars-trucks") |
| `partType` | String | Part category (for parts listings) |
| `recordType` | String | Always `"ebayMotorsListing"` |
| `scrapedAt` | String | ISO 8601 timestamp when scraped |

## Example Output

```json
{
  "listingId": "256789012345",
  "title": "2020 Toyota Camry SE Sedan 4D — Clean Title",
  "url": "https://www.ebay.com/itm/256789012345",
  "price": 22500.0,
  "priceFormatted": "$22,500",
  "condition": "Used",
  "mileage": 45000,
  "year": 2020,
  "make": "Toyota",
  "model": "Camry",
  "trim": "SE",
  "bodyStyle": "Sedan",
  "fuelType": "Gasoline",
  "transmission": "Automatic",
  "drivetrain": "FWD",
  "exteriorColor": "Midnight Black",
  "sellerName": "auto_dealership_la",
  "sellerFeedbackScore": 2847,
  "sellerPositivePercent": 99.2,
  "shippingType": "Free",
  "shippingCost": 0.0,
  "location": "Los Angeles, CA",
  "imageUrl": "https://i.ebayimg.com/images/g/abcdef/s-l1600.jpg",
  "images": ["https://i.ebayimg.com/images/g/abcdef/s-l1600.jpg"],
  "listingType": "BuyItNow",
  "watchCount": 42,
  "vehicleType": "cars-trucks",
  "recordType": "ebayMotorsListing",
  "scrapedAt": "2026-05-15T10:30:00+00:00"
}
```

## FAQ

**Q: What vehicle types can I search?**
A: The scraper supports Cars & Trucks, Motorcycles, Boats, RVs & Campers, ATVs/UTVs/Snowmobiles, Commercial Trucks, and Other Vehicles. Select the appropriate `vehicleType` in `searchVehicles` mode.

**Q: Can I search for parts and accessories?**
A: Yes, set `mode` to `searchParts` and pick the `partCategory` (Car & Truck Parts, Motorcycle Parts, Boat Parts, ATV Parts, or Other).

**Q: How do I scrape a specific listing I found on eBay Motors?**
A: Set `mode` to `byListingUrls` and add the eBay item URLs (like `https://www.ebay.com/itm/123456789`) to the `startUrls` field.

**Q: Can I filter by price range and model year?**
A: Yes. Use `minPrice`/`maxPrice` for price filtering and `minYear`/`maxYear` to restrict by model year. All filters can be combined.

**Q: How many listings can I scrape?**
A: Up to 5,000 listings per run by setting `maxItems`. eBay paginates at 25 listings per page, so larger runs require multiple page fetches.

**Q: Does this scrape auction listings?**
A: Yes. Auction listings include `bids`, `timeRemaining`, and `listingType: "Auction"` in the output.

**Q: What data is available for parts listings?**
A: Parts listings return the same fields as vehicle listings where applicable (title, price, condition, seller info, images, shipping) plus a `partType` field identifying the parts category.

**Q: Why might some fields be missing?**
A: Not every listing includes all fields — for example, a private seller may not list mileage, or a parts listing won't have year/make/model. The scraper only outputs fields it can reliably extract; null/empty fields are omitted.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/ebay-motors-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
