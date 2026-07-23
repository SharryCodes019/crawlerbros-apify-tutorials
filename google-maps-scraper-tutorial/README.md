# Google Maps Scraper Tutorial: Run This Apify Actor with Python

Extract business data from Google Maps including ratings, reviews, contact info, prices, coordinates, and images. Fast scraper with automatic pagination for any location or search query.

This repository shows how to run [Google Maps Scraper](https://apify.com/crawlerbros/google-maps-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-maps-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/google-maps-scraper](https://apify.com/crawlerbros/google-maps-scraper)
- **SEO title:** Google Maps Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract business data from Google Maps including ratings, reviews, contact info, prices, coordinates, and images. Fast scraper with automatic pagination for any location or search query.

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

# Google Maps Scraper

An Apify Actor that scrapes business listings from Google Maps based on search queries and location. This actor extracts comprehensive business information including contact details, reviews, ratings, and more.

## Features

- **Location-based Search**: Search for businesses in specific locations
- **Multiple Search Terms**: Support for multiple search queries in one run
- **Comprehensive Data Extraction**: Extract business names, addresses, phone numbers, websites, ratings, reviews
- **Business Hours**: Extract operating hours for each business
- **Reviews & Ratings**: Scrape customer reviews and ratings
- **Coordinates**: Extract latitude and longitude coordinates
- **Amenities**: Extract business amenities and features
- **Flexible Configuration**: Customizable search parameters and data extraction options

## Input Configuration

The actor accepts the following input parameters:

```json
{
  "includeWebResults": false,
  "language": "en",
  "locationQuery": "New York, USA",
  "maxCrawledPlacesPerSearch": 50,
  "maxImages": 0,
  "maximumLeadsEnrichmentRecords": 0,
  "scrapeContacts": false,
  "scrapeDirectories": false,
  "scrapeImageAuthors": false,
  "scrapePlaceDetailPage": false,
  "scrapeReviewsPersonalData": true,
  "scrapeTableReservationProvider": false,
  "searchStringsArray": ["restaurant"],
  "skipClosedPlaces": false
}
```

### Input Parameters

- **searchStringsArray** (array, required): List of search terms to look for (e.g., ["restaurant", "hotel", "cafe"])
- **locationQuery** (string, required): Location to search in (e.g., "New York, USA", "London, UK")
- **maxCrawledPlacesPerSearch** (number, optional): Maximum number of places to scrape per search term (default: 50)
- **language** (string, optional): Language for search results (default: "en")
- **includeWebResults** (boolean, optional): Include web search results (default: false)
- **scrapeContacts** (boolean, optional): Extract contact information (default: false)
- **scrapeReviewsPersonalData** (boolean, optional): Extract review data (default: true)
- **skipClosedPlaces** (boolean, optional): Skip businesses that are currently closed (default: false)

## Output Data

The actor outputs an array of business objects with the following structure:

```json
{
  "index": 0,
  "scraped_at": "2024-01-15T10:30:00",
  "name": "Joe's Pizza",
  "rating": 4.5,
  "review_count": 1234,
  "address": "123 Main St, New York, NY 10001",
  "phone": "+1 (555) 123-4567",
  "website": "https://joespizza.com",
  "category": "Pizza restaurant",
  "price_level": "$$",
  "latitude": 40.7128,
  "longitude": -74.006,
  "hours": {
    "monday": "11:00 AM – 10:00 PM",
    "tuesday": "11:00 AM – 10:00 PM",
    "wednesday": "11:00 AM – 10:00 PM",
    "thursday": "11:00 AM – 10:00 PM",
    "friday": "11:00 AM – 11:00 PM",
    "saturday": "11:00 AM – 11:00 PM",
    "sunday": "12:00 PM – 9:00 PM"
  },
  "reviews": [
    {
      "reviewer_name": "John Doe",
      "rating": 5,
      "text": "Great pizza and friendly service!",
      "date": "2 weeks ago"
    }
  ],
  "amenities": ["Delivery", "Takeout", "Dine-in"],
  "description": "Family-owned pizza restaurant serving authentic New York style pizza"
}
```

### Output Fields

- **index**: Sequential index of the business in the results
- **scraped_at**: ISO timestamp of when the data was scraped
- **name**: Business name
- **rating**: Average rating (1-5 stars)
- **review_count**: Number of reviews
- **address**: Full business address
- **phone**: Phone number
- **website**: Business website URL
- **category**: Business type/category
- **price_level**: Price range indicator ($, $$, $$$, $$$$)
- **latitude**: GPS latitude coordinate
- **longitude**: GPS longitude coordinate
- **hours**: Operating hours for each day of the week
- **reviews**: Array of recent customer reviews
- **amenities**: List of business amenities and features
- **description**: Business description

## Usage

### Local Development

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Install Playwright browsers:

```bash
playwright install chromium
```

3. Run the actor:

```bash
python -m src
```

### Docker

1. Build the Docker image:

```bash
docker build -t google-maps-scraper .
```

2. Run the container:

```bash
docker run -it google-maps-scraper
```

### Apify Platform

1. Deploy the actor to your Apify account
2. Configure the input parameters
3. Run the actor

## Technical Details

### Browser Automation

The actor uses Playwright with Chromium to automate Google Maps navigation. It includes:

- Anti-detection measures to avoid Google's bot detection
- Custom user agent and headers
- Viewport configuration for consistent rendering
- Automatic handling of dynamic content loading

### Data Extraction

The actor uses multiple strategies for data extraction:

- **CSS Selectors**: Target specific Google Maps elements
- **Text Parsing**: Extract and clean text content
- **Attribute Extraction**: Get data from HTML attributes
- **Pattern Matching**: Use regex to extract structured data

### Rate Limiting

The actor includes built-in rate limiting:

- Delays between searches
- Respectful scrolling behavior
- Anti-detection measures

## Limitations

- **Google's Anti-Bot Measures**: Google may block or limit automated access
- **Rate Limiting**: Google has strict rate limits for automated requests
- **Content Availability**: Some business information may not be publicly available
- **Dynamic Content**: Google Maps' dynamic loading may affect data extraction
- **Terms of Service**: Ensure compliance with Google's Terms of Service

## Troubleshooting

### Common Issues

1. **No Results Found**:

   - Verify search terms and location format
   - Check if the location has businesses of that type
   - Try different search terms

2. **Rate Limiting**:

   - Reduce the number of places per search
   - Increase delays between requests
   - Use proxy rotation if available

3. **Incomplete Data**:
   - Some businesses may not have all information available
   - Google may limit certain data for privacy reasons
   - Try refreshing or running the search again

### Debug Information

The actor provides detailed logging for troubleshooting:

- Search progress and results count
- Data extraction status
- Error messages and warnings
- Performance metrics

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:

- Check the troubleshooting section
- Review the Apify documentation
- Open an issue in the repository

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-maps-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
