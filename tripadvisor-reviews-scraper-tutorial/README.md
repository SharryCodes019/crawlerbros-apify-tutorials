# Tripadvisor Reviews Scraper Tutorial: Run This Apify Actor with Python

Extract reviews from TripAdvisor places. Get review text, ratings, dates, reviewer info, owner responses, helpful votes, and place details.

This repository shows how to run [Tripadvisor Reviews Scraper](https://apify.com/crawlerbros/tripadvisor-reviews-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tripadvisor-reviews-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/tripadvisor-reviews-scraper](https://apify.com/crawlerbros/tripadvisor-reviews-scraper)
- **SEO title:** Tripadvisor Reviews Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract reviews from TripAdvisor places. Get review text, ratings, dates, reviewer info, owner responses, helpful votes, and place details.

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

# TripAdvisor Reviews Scraper

Extract reviews from TripAdvisor hotels, restaurants, and attractions. Get review text, ratings, dates, reviewer details, owner responses, and place metadata. Supports pagination to collect hundreds of reviews per place.

## What can this scraper do?

- **Extract reviews** — Get full review text, title, rating, travel date, and trip type from any TripAdvisor place
- **Scrape multiple places** — Process a list of TripAdvisor URLs in a single run
- **Collect reviewer info** — Get reviewer name, location, contribution count, and helpful votes
- **Capture owner responses** — Extract management responses to reviews when available
- **Paginate automatically** — Collect up to 1,000 reviews per place across multiple pages
- **Get place metadata** — Each review includes the place name, category, rating, address, and overall review count

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `startUrls` | string[] | Yes | — | TripAdvisor place URLs to scrape reviews from |
| `maxReviews` | integer | No | 100 | Maximum reviews per place (1-1,000) |
| `reviewsSort` | enum | No | `recent` | Sort order: `recent` or `relevance` |
| `proxyConfiguration` | object | No | — | Proxy settings (residential proxy recommended) |

### Supported URL formats

- Hotels: `https://www.tripadvisor.com/Hotel_Review-g...-d...-Reviews-...`
- Restaurants: `https://www.tripadvisor.com/Restaurant_Review-g...-d...-Reviews-...`
- Attractions: `https://www.tripadvisor.com/Attraction_Review-g...-d...-Reviews-...`

### Example inputs

**Scrape 20 recent reviews from a hotel:**
```json
{
    "startUrls": ["https://www.tripadvisor.com/Hotel_Review-g60763-d675616-Reviews-The_Plaza_New_York-New_York_City_New_York.html"],
    "maxReviews": 20,
    "reviewsSort": "recent"
}
```

**Scrape reviews from multiple places with proxy:**
```json
{
    "startUrls": [
        "https://www.tripadvisor.com/Hotel_Review-g60763-d675616-Reviews-The_Plaza_New_York-New_York_City_New_York.html",
        "https://www.tripadvisor.com/Restaurant_Review-g60763-d457808-Reviews-Daniel-New_York_City_New_York.html"
    ],
    "maxReviews": 50,
    "proxyConfiguration": {
        "useApifyProxy": true,
        "apifyProxyGroups": ["RESIDENTIAL"]
    }
}
```

## Output

Each row in the dataset represents one review, enriched with place metadata.

### Output fields

| Field | Description | Example |
|-------|-------------|---------|
| `placeName` | Place name | `"The Plaza New York"` |
| `placeUrl` | TripAdvisor place URL | `"https://www.tripadvisor.com/Hotel_Review-..."` |
| `placeCategory` | Place type | `"hotel"` |
| `placeRating` | Overall place rating (0-5) | `"4.5"` |
| `placeReviewCount` | Total number of reviews | `"5309"` |
| `placeAddress` | Full place address | `"5th Avenue, New York City, NY 10019"` |
| `reviewId` | Unique review identifier | `"675616_0"` |
| `reviewTitle` | Review title/headline | `"Absolutely stunning experience"` |
| `reviewText` | Full review text | `"We stayed for three nights and..."` |
| `reviewRating` | Review rating (1-5) | `"5.0"` |
| `reviewDate` | When the review was written | `"February 2026"` |
| `travelDate` | Date of stay/visit | `"January 2026"` |
| `tripType` | Trip type | `"Couples"` |
| `reviewerName` | Reviewer display name | `"JohnD123"` |
| `reviewerLocation` | Reviewer home location | `"San Francisco, California"` |
| `reviewerContributions` | Number of contributions | `"42"` |
| `helpfulVotes` | Number of helpful votes | `"8"` |
| `ownerResponse` | Owner/management response | `"Dear John, Thank you for..."` |
| `ownerResponseDate` | Response date | `"February 15, 2026"` |
| `reviewUrl` | Link to the review page | `"https://www.tripadvisor.com/Hotel_Review-..."` |
| `reviewLanguage` | Review language | `"en"` |
| `scrapeTimestamp` | ISO timestamp of scrape | `"2026-03-10T12:00:00+00:00"` |

### Sample output

```json
{
    "placeName": "The Plaza New York - A Fairmont Managed Hotel",
    "placeUrl": "https://www.tripadvisor.com/Hotel_Review-g60763-d675616-Reviews-The_Plaza_New_York-New_York_City_New_York.html",
    "placeCategory": "hotel",
    "placeRating": "4.5",
    "placeReviewCount": "5309",
    "placeAddress": "5th Avenue At Central Park South, New York City, NY 10019",
    "reviewId": "675616_0",
    "reviewTitle": "Absolutely stunning experience",
    "reviewText": "We stayed for three nights and every moment was memorable. The rooms are beautifully decorated...",
    "reviewRating": "5.0",
    "reviewDate": "February 2026",
    "travelDate": "January 2026",
    "tripType": "Couples",
    "reviewerName": "JohnD123",
    "reviewerLocation": "San Francisco, California",
    "reviewerContributions": "42",
    "helpfulVotes": "8",
    "ownerResponse": "",
    "ownerResponseDate": "",
    "reviewUrl": "https://www.tripadvisor.com/Hotel_Review-g60763-d675616-Reviews-The_Plaza_New_York-New_York_City_New_York.html",
    "reviewLanguage": "en",
    "scrapeTimestamp": "2026-03-10T12:00:00.000000+00:00"
}
```

## How it works

1. **Place metadata** — Fetches place details (name, rating, address) via TripAdvisor's public Location API (fast, no browser needed)
2. **Review pages** — Opens each review page in a browser to extract review data from the rendered page
3. **Pagination** — Automatically navigates through review pages (10 reviews per page) until the desired count is reached
4. **Anti-bot handling** — Includes retry logic for TripAdvisor's DataDome protection with exponential backoff

## Tips for best results

- **Use residential proxy** — TripAdvisor uses DataDome anti-bot protection. Residential proxy significantly improves success rate
- **Start small** — Test with 10-20 reviews first to verify the setup works with your proxy configuration
- **Multiple URLs** — Process multiple places in a single run to amortize browser startup time
- **Rate limiting** — The scraper adds random delays between pages to avoid triggering rate limits

## Frequently Asked Questions

**Do I need a TripAdvisor account?**
No. This scraper does not require any login credentials or API keys.

**Does it need a proxy?**
Residential proxy is recommended for best results. TripAdvisor uses DataDome anti-bot protection that may block requests from datacenter IPs.

**How many reviews can I scrape per place?**
Up to 1,000 reviews per place. TripAdvisor displays 10 reviews per page, so 100 reviews requires loading 10 pages.

**What place types are supported?**
Hotels, restaurants, attractions, and vacation rentals — any TripAdvisor page with a review section.

**Which URL format should I use?**
Use the standard TripAdvisor place page URL containing `-Reviews-` in the path. You can copy it directly from your browser.

**Are the reviews in English only?**
By default, the scraper extracts English-language reviews as displayed on the page. The review language depends on the TripAdvisor page locale.

**Can I sort reviews?**
Yes. Choose between `recent` (most recent first) and `relevance` (most relevant first) using the `reviewsSort` input.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/tripadvisor-reviews-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
