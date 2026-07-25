# Google Maps MCP Tutorial: Run This Apify Actor with Python

Unified Apify MCP server for Google Maps. Search for businesses and extract comprehensive data including ratings, reviews, contact info, and more. Scrape detailed reviews from any Google Maps place.

This repository shows how to run [Google Maps MCP](https://apify.com/crawlerbros/google-maps-mcp) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-maps-mcp`
- **Apify Store:** [https://apify.com/crawlerbros/google-maps-mcp](https://apify.com/crawlerbros/google-maps-mcp)
- **SEO title:** Google Maps MCP Tutorial: Run This Apify Actor with Python
- **Description:** Unified Apify MCP server for Google Maps. Search for businesses and extract comprehensive data including ratings, reviews, contact info, and more. Scrape detailed reviews from any Google Maps place.

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

# Google Maps MCP Server

A unified Apify MCP (Model Context Protocol) server for comprehensive Google Maps scraping. This actor provides a single interface to search for businesses and scrape reviews using browser automation with Playwright.

## 🚀 Features

### Multi-Mode Scraping

This MCP server supports two scraping modes:

1. **Search Mode** - Search and scrape business listings from Google Maps
2. **Reviews Mode** - Scrape reviews from a specific Google Maps business

### Key Capabilities

✅ **Unified Interface** - Single actor for all Google Maps scraping needs
✅ **Browser Automation** - Reliable scraping using Playwright
✅ **No API Key Required** - Scrape public content without authentication
✅ **Comprehensive Data** - Extract all relevant business details and reviews
✅ **Automatic Pagination** - Load multiple results and reviews automatically
✅ **Structured Output** - Clean JSON data ready for AI consumption

## 📋 Input Parameters

### Common Parameters

| Parameter | Type   | Required | Description                              |
| --------- | ------ | -------- | ---------------------------------------- |
| `mode`    | string | Yes      | Scraping mode: `search` or `reviews`     |

### Search Mode Parameters

| Parameter     | Type    | Default | Description                                    |
| ------------- | ------- | ------- | ---------------------------------------------- |
| `searchQuery` | string  | -       | What to search for (e.g., "restaurant")        |
| `location`    | string  | `""`    | Where to search (e.g., "New York, NY")         |
| `maxResults`  | integer | `20`    | Maximum number of businesses to scrape (1-100) |

### Reviews Mode Parameters

| Parameter    | Type    | Default | Description                                   |
| ------------ | ------- | ------- | --------------------------------------------- |
| `placeUrl`   | string  | -       | Google Maps place URL                         |
| `maxReviews` | integer | `50`    | Maximum number of reviews to scrape (1-1000)  |

## 📝 Input Examples

### Example 1: Search for Businesses

```json
{
  "mode": "search",
  "searchQuery": "pizza restaurant",
  "location": "New York, NY",
  "maxResults": 20
}
```

### Example 2: Scrape Reviews

```json
{
  "mode": "reviews",
  "placeUrl": "https://www.google.com/maps/place/Joe's+Pizza/@40.7308314,-73.9973325,17z",
  "maxReviews": 100
}
```

## 📊 Output Format

### Search Mode Output

Each business includes:

```json
{
  "index": 1,
  "name": "Joe's Pizza",
  "category": "Pizza restaurant",
  "rating": 4.5,
  "review_count": 1234,
  "price_level": "$$",
  "address": "7 Carmine St, New York, NY 10014",
  "phone": "+1 212-366-1182",
  "website": "https://www.joespizzanyc.com",
  "url": "https://www.google.com/maps/place/Joe's+Pizza/@40.7308314,-73.9973325,17z",
  "place_id": "ChIJxxx...",
  "latitude": 40.7308314,
  "longitude": -73.9973325,
  "scraped_at": "2025-11-02T20:30:00"
}
```

### Reviews Mode Output (Flattened Format)

**One review per row** for easy analysis - each dataset item represents a single review with place metadata:

```json
{
  "place_metadata": {
    "place_url": "https://www.google.com/maps/place/...",
    "scraped_at": "2025-11-02T20:30:00",
    "business_name": "Joe's Pizza",
    "rating": 4.5,
    "total_reviews": 1234,
    "category": "Pizza restaurant",
    "address": "7 Carmine St, New York, NY 10014"
  },
  "review_id": "ChZDSUhNMG9nS0VJQ0FnSUQ...",
  "reviewer_name": "John Smith",
  "reviewer_avatar": "https://lh3.googleusercontent.com/...",
  "rating": 5.0,
  "review_text": "Best pizza in NYC! The crust is perfect and the sauce is amazing...",
  "review_date": "2 months ago",
  "likes": 42
}
```

**Benefits of Flattened Format:**
- ✅ Each row is one review (perfect for CSV export and data analysis)
- ✅ Easy to query, filter, and aggregate in databases
- ✅ Compatible with pandas DataFrames and SQL tables
- ✅ Place metadata included in every row (no joins needed)
- ✅ Simplified data pipeline integration

## 🎯 Use Cases

### Business Intelligence

- **Market Research** - Analyze competitor locations and ratings
- **Location Planning** - Find optimal areas for new business locations
- **Competitive Analysis** - Track competitor reviews and ratings
- **Customer Insights** - Understand what customers value in your industry

### Data Analysis & Research

- **Sentiment Analysis** - Analyze customer sentiment from reviews
- **Trend Detection** - Identify popular locations and emerging trends
- **Service Quality** - Compare service quality across locations
- **Price Analysis** - Study pricing patterns across regions

### AI & ML Applications

- **Training Data** - Build datasets for recommendation systems
- **RAG Systems** - Feed business and review data to AI models
- **Chatbot Training** - Use reviews for customer service bots
- **Content Generation** - Analyze successful business descriptions

## 🛠️ Local Development

### Prerequisites

```bash
pip install -r requirements.txt
playwright install chromium
```

### Create Input File

Create `storage/key_value_stores/default/INPUT.json`:

**For Search Mode:**
```json
{
  "mode": "search",
  "searchQuery": "coffee shop",
  "location": "San Francisco, CA",
  "maxResults": 10
}
```

**For Reviews Mode:**
```json
{
  "mode": "reviews",
  "placeUrl": "https://www.google.com/maps/place/Blue+Bottle+Coffee/@37.7749295,-122.4194155,17z",
  "maxReviews": 50
}
```

### Run Locally

```bash
cd Google/mcp
apify run
```

### Check Results

Results are saved in:
- `storage/datasets/default/` - Individual records
- `storage/key_value_stores/default/OUTPUT.json` - Complete output

## 🚀 Deployment

### Using Apify CLI

```bash
# Login to Apify
apify login

# Push to Apify platform
apify push
```

### Manual Upload

1. Create a new actor on [Apify Console](https://console.apify.com/)
2. Upload all files including `Dockerfile`, `requirements.txt`, and `.actor/` directory
3. Configure input parameters
4. Run the actor

## 📚 API Integration

### JavaScript/Node.js

```javascript
const { ApifyClient } = require("apify-client");

const client = new ApifyClient({ token: "YOUR_API_TOKEN" });

// Search for businesses
const searchInput = {
  mode: "search",
  searchQuery: "sushi restaurant",
  location: "Los Angeles, CA",
  maxResults: 25
};

const run = await client.actor("YOUR_ACTOR_ID").call(searchInput);
const { items } = await client.dataset(run.defaultDatasetId).listItems();

console.log(`Found ${items.length} businesses`);
```

### Python

```python
from apify_client import ApifyClient

client = ApifyClient('YOUR_API_TOKEN')

# Scrape reviews
reviews_input = {
    'mode': 'reviews',
    'placeUrl': 'https://www.google.com/maps/place/...',
    'maxReviews': 100
}

run = client.actor('YOUR_ACTOR_ID').call(run_input=reviews_input)

for item in client.dataset(run['defaultDatasetId']).iterate_items():
    print(f"Review: {item['review_text']}")
    print(f"Rating: {item['rating']}")
```

## ⚡ Performance Tips

### Optimize Speed

- Start with lower `maxResults`/`maxReviews` for testing
- Use specific search queries for better results
- Limit location scope for faster searches
- Process fewer businesses per run for faster completion

### Best Practices

- Add delays between requests (built-in)
- Don't scrape the same content repeatedly
- Respect Google's servers - use reasonable limits
- Consider batching requests across multiple runs

## ⚠️ Limitations

- **Public Content Only** - Cannot access restricted or private data
- **No Authentication** - Requires public access to content
- **Rate Limits** - Google may throttle excessive requests
- **Browser-Based** - Slower than direct API but more reliable
- **Dynamic Content** - Some features may change if Google updates layout

## 🐛 Troubleshooting

### No Results Returned

- Verify search query and location are correct
- Check if the place URL is valid and accessible
- Try with smaller `maxResults`/`maxReviews` values first
- Review logs for specific error messages

### Timeout Errors

- Content may be loading slowly
- Try with fewer items or smaller limits
- Check if Google Maps is accessible from your location

### Missing Data Fields

- Some fields may be null if not available
- Not all businesses have all information
- Reviews may vary in completeness

## 📄 License

This actor is provided as-is for scraping public Google Maps data in accordance with Google's terms of service.

## 🔗 Related Actors

- [Google Maps Scraper](../google-maps/) - Dedicated business search scraper
- [Google Maps Reviews Scraper](../google-maps-reviews/) - Dedicated reviews scraper

## 💡 Notes

- This MCP server uses browser automation to access Google Maps public interface
- Always respect Google's robots.txt and terms of service
- Use responsibly and avoid overwhelming Google's servers
- Consider implementing additional rate limiting for large-scale scraping
- The actor works best with the Apify platform's infrastructure

## 🆘 Support

For issues, questions, or feature requests, please open an issue in the repository or contact support.

---

**Made with ❤️ for the AI community | Powered by Apify**

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-maps-mcp)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
