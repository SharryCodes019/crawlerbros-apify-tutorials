# Crexi Real Estate Scraper Tutorial: Run This Apify Actor with Python

Scrapes commercial real estate listings from Crexi.com including property details, pricing, location, images, and investment metrics.

This repository shows how to run [Crexi Real Estate Scraper](https://apify.com/crawlerbros/crexi-real-estate-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/crexi-real-estate-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/crexi-real-estate-scraper](https://apify.com/crawlerbros/crexi-real-estate-scraper)
- **SEO title:** Crexi Real Estate Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrapes commercial real estate listings from Crexi.com including property details, pricing, location, images, and investment metrics.

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

# Crexi Real Estate Scraper

This Apify actor scrapes publicly available commercial real estate data from Crexi.com, automating the extraction of key property listings and market details. The scraper outputs structured data for analysis, reporting, or integration with other systems.

## Features

- **Automated Scraping**: Navigate through Crexi's property listings and extract relevant details
- **Pagination Handling**: Automatically process multiple pages to ensure comprehensive data collection
- **Structured Output**: Export scraped data in JSON format for easy analysis
- **Configurable Extraction**: Easily customize the fields to extract based on your specific needs
- **Rate Limiting & Header Customization**: Prevent overloading the server by adjusting request intervals and headers
- **HTML Debugging**: Saves HTML content for selector analysis during development

## Input Parameters

| Parameter        | Type    | Default | Description                                       |
| ---------------- | ------- | ------- | ------------------------------------------------- |
| `maxProperties`  | Integer | 50      | Maximum number of properties to scrape            |
| `scrapeDetails`  | Boolean | true    | Whether to scrape detailed property pages         |
| `propertyTypes`  | Array   | []      | List of property types to filter by               |
| `locations`      | Array   | []      | List of locations to filter by                    |
| `minPrice`       | Integer | null    | Minimum price filter                              |
| `maxPrice`       | Integer | null    | Maximum price filter                              |
| `rateLimitDelay` | Integer | 2       | Delay between requests in seconds (rate limiting) |

## Data Extracted

For each property listing available on Crexi, the scraper extracts:

### Basic Information

- `property_id`: Unique identifier for the property
- `name`: The title or name of the property
- `property_type`: Classification (e.g., Office, Retail, Industrial, Multifamily, etc.)
- `property_url`: Direct link to the detailed property page

### Location

- `address`: Full street address
- `city`: City name
- `state`: State abbreviation (e.g., CA, NY)
- `zip_code`: ZIP code

### Financial Information

- `price`: Sale price or asking price
- `lease_rate`: Rental rates or lease information
- `investment_metrics`: Object containing:
  - `cap_rate`: Capitalization rate
  - `noi`: Net Operating Income
  - `cash_on_cash`: Cash on cash return

### Physical Details

- `square_footage`: Total area or leasable space
- `lot_size`: Land area or lot size
- `specifications`: Object containing:
  - `year_built`: Year the building was constructed
  - `units`: Number of units (for multifamily properties)
  - `parking`: Parking spaces or parking information
  - `building_class`: Building classification (Class A, B, C)
  - `zoning`: Zoning information

### Description & Features

- `description`: Summary description from listing page
- `full_description`: Detailed description from property detail page
- `highlights`: Array of property highlights or key features
- `features`: Array of property features
- `amenities`: Array of building amenities

### Media & Documents

- `image_url`: Primary image URL from listing
- `images`: Array of all property images with URLs and alt text
- `documents`: Array of documents/brochures with URLs and names

### Status & Metadata

- `availability`: Property availability status
- `listing_date`: Date the property was listed
- `scraped_at`: Timestamp when data was scraped
- `source`: Source website (crexi.com)

### Detailed Information (if scrapeDetails=true)

- `agent_info`: Object containing:
  - `name`: Listing agent name
  - `company`: Brokerage company
  - `phone`: Contact phone number
  - `email`: Contact email
- `similar_properties`: Array of similar property listings
- `metadata`: Additional metadata including structured data

## Output Data

Each property record is a JSON object containing all the fields listed above. Example:

```json
{
  "property_id": "12345",
  "name": "Downtown Office Building",
  "property_type": "Office",
  "address": "123 Main Street",
  "city": "San Francisco",
  "state": "CA",
  "zip_code": "94102",
  "price": "$5,500,000",
  "square_footage": "15000",
  "property_url": "https://www.crexi.com/properties/12345",
  "scraped_at": "2025-10-30T12:00:00.000Z",
  "source": "crexi.com"
}
```

## Usage Examples

### Basic Usage

```json
{
  "maxProperties": 25,
  "scrapeDetails": true
}
```

### Filtered by Property Type and Location

```json
{
  "maxProperties": 100,
  "scrapeDetails": true,
  "propertyTypes": ["Office", "Retail"],
  "locations": ["San Francisco", "New York"]
}
```

### Quick Scraping (No Details)

```json
{
  "maxProperties": 200,
  "scrapeDetails": false
}
```

### With Price Range and Rate Limiting

```json
{
  "maxProperties": 50,
  "scrapeDetails": true,
  "minPrice": 1000000,
  "maxPrice": 10000000,
  "rateLimitDelay": 3
}
```

## Development Features

### HTML Debugging

During development, the scraper saves HTML content to the key-value store for selector analysis:

- `crexi_initial_page_html`: Contains the HTML content of the initial search page
- `crexi_page_1_html`, `crexi_page_2_html`, etc.: HTML content for each paginated page
- `debug_crexi_html`: Contains HTML when standard selectors fail to find listings

This allows you to analyze the page structure and refine selectors without making repeated requests.

### Error Handling

- Comprehensive error handling with detailed logging
- Graceful handling of missing elements
- Continues processing even if individual properties fail
- Validates and cleans data before pushing to output

### Browser Automation

- Uses Playwright for reliable browser automation
- Handles dynamic content loading
- Implements proper delays and waits
- Anti-detection measures to avoid bot detection

### Rate Limiting

- Configurable delay between requests (`rateLimitDelay` parameter)
- Default 2-second delay to be respectful to the server
- Separate delays for listing pages and detail pages

## Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Install Playwright browsers:

```bash
playwright install chromium
```

3. Run the scraper:

```bash
python -m src
```

## Docker Usage

```bash
docker build -t crexi-scraper .
docker run -e APIFY_TOKEN=your_token crexi-scraper
```

## Apify Platform Usage

1. Create a new actor on the Apify platform
2. Upload all files from this directory
3. Configure input parameters in the actor's input schema
4. Run the actor and retrieve results from the dataset

## Notes

- The scraper respects rate limits and implements delays between requests
- HTML content is saved for debugging purposes during development
- The scraper handles various property listing layouts and structures
- All URLs are properly resolved and normalized
- Data is validated and cleaned before being pushed to the output
- The scraper will continue even if some properties fail to load
- For production use, consider increasing `rateLimitDelay` to 3-5 seconds

## Limitations

- Requires active internet connection
- May be affected by website structure changes
- Some data fields may not be available for all properties
- Respects robots.txt and terms of service

## Support

For issues, questions, or feature requests, please contact the development team or create an issue in the repository.

## License

This scraper is provided as-is for educational and research purposes. Ensure you comply with Crexi's terms of service when using this tool.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/crexi-real-estate-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
