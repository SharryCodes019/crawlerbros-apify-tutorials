# Google Maps Reviews Scraper Tutorial: Run This Apify Actor with Python

Extract detailed reviews from any Google Maps business page. This scraper retrieves reviewer information, ratings, review text, dates, likes, and owner responses.

This repository shows how to run [Google Maps Reviews Scraper](https://apify.com/crawlerbros/google-maps-reviews-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-maps-reviews-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/google-maps-reviews-scraper](https://apify.com/crawlerbros/google-maps-reviews-scraper)
- **SEO title:** Google Maps Reviews Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract detailed reviews from any Google Maps business page. This scraper retrieves reviewer information, ratings, review text, dates, likes, and owner responses.

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

# Google Maps Reviews Scraper

Extract reviews from any Google Maps business or place. Get reviewer names, star ratings, full review text, dates, likes, and business details — all in a structured dataset.

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `placeUrl` | string | Yes | — | Google Maps place URL |
| `maxReviews` | integer | No | 50 | Maximum number of reviews to extract |

### Example Input

```json
{
    "placeUrl": "https://www.google.com/maps/place/Joe's+Pizza/@40.7305137,-73.9968643,17z/data=!3m2!4b1!5s0x89c2599bcc4854cd:0xabc03f64af538b40!4m6!3m5!1s0x89c2599bca4854c5:0x48e61b36c6e9e68!8m2!3d40.7305137!4d-73.9942894!16s%2Fg%2F1tfrzlcv",
    "maxReviews": 30
}
```

### How to Get the Place URL

1. Go to [Google Maps](https://www.google.com/maps)
2. Search for the business or place
3. Click on the place to open its details
4. Copy the URL from your browser's address bar

The URL should look like: `https://www.google.com/maps/place/PLACE+NAME/@...`

## Output

Each row in the dataset represents one review. Every row includes both the review data and the business context.

### Sample Output

```json
{
    "review_id": "ChZDSUhNMG9nS0VJQ0...",
    "reviewer_name": "John Smith",
    "reviewer_avatar": "https://lh3.googleusercontent.com/a/...",
    "rating": 5,
    "review_text": "Best pizza in NYC! The classic slice is perfection.",
    "review_date": "2 weeks ago",
    "likes": 3,
    "business_name": "Joe's Pizza",
    "business_rating": 4.5,
    "business_total_reviews": 12847,
    "business_category": "Pizza restaurant",
    "business_address": "7 Carmine St, New York, NY 10014",
    "place_url": "https://www.google.com/maps/place/Joe's+Pizza/...",
    "order": 0,
    "scraped_at": "2026-02-19T12:00:00+00:00"
}
```

### Output Fields

| Field | Type | Description |
|-------|------|-------------|
| `review_id` | string | Unique review identifier |
| `reviewer_name` | string | Name of the reviewer |
| `reviewer_avatar` | string | URL of the reviewer's profile picture |
| `rating` | integer | Star rating (1–5) |
| `review_text` | string | Full review text |
| `review_date` | string | Relative date (e.g., "2 weeks ago") |
| `likes` | integer | Number of likes on the review |
| `business_name` | string | Name of the business |
| `business_rating` | number | Overall business star rating |
| `business_total_reviews` | integer | Total number of reviews for the business |
| `business_category` | string | Business category (e.g., "Pizza restaurant") |
| `business_address` | string | Business street address |
| `place_url` | string | Original Google Maps URL provided as input |
| `order` | integer | Position of the review in results (0-based) |
| `scraped_at` | string | ISO 8601 timestamp of when the data was scraped |

## Tips

- **Restaurants, shops, and hotels** work best — these are the most common use cases
- **Set `maxReviews` wisely** — higher values take longer but give more data
- Reviews are sorted by relevance (Google's default sorting)
- Review dates are relative (e.g., "a month ago"), not absolute calendar dates

## Limitations

- Parks, landmarks, and large public areas may return fewer or no reviews due to Google Maps rendering differences
- Google may occasionally restrict access from data center IPs
- The scraper extracts reviews visible on Google Maps — private or filtered reviews are not accessible

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-maps-reviews-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
