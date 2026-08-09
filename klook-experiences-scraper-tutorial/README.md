# Klook Experiences & Activities Scraper Tutorial: Run This Apify Actor with Python

Scrape Klook travel experiences and activities, search activities, browse by city or category, or enrich specific activity URLs. Extracts title, price, rating, reviews, city, category, highlights, cancellation policy, and more.

This repository shows how to run [Klook Experiences & Activities Scraper](https://apify.com/crawlerbros/klook-experiences-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/klook-experiences-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/klook-experiences-scraper](https://apify.com/crawlerbros/klook-experiences-scraper)
- **SEO title:** Klook Experiences & Activities Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Klook travel experiences and activities, search activities, browse by city or category, or enrich specific activity URLs. Extracts title, price, rating, reviews, city, category, highlights, cancellation policy, and more.

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

# Klook Experiences & Activities Scraper

Extract travel experiences and activities from [Klook](https://www.klook.com) — search by keyword, browse by city, or enrich specific activity URLs. Ideal for travel researchers, price trackers, and anyone building travel comparison tools.

## What It Scrapes

Klook lists millions of activities, tours, theme park tickets, and travel experiences across thousands of destinations worldwide. This actor retrieves structured activity data including title, price, rating, review count, city, category, and booking tags.

## Input

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `mode` | Select | `byCity`, `searchActivities`, or `byActivityUrls` | `byCity` |
| `city` | Text | City/destination name (mode=byCity), e.g. Tokyo, Paris | `Tokyo` |
| `searchQuery` | Text | Keyword search (mode=searchActivities), e.g. snorkeling | `Tokyo` |
| `sortBy` | Select | Sort order for results | `most_relevant` |
| `minRating` | Number | Minimum rating filter (0.0–5.0) | — |
| `minPrice` | Integer | Minimum price in USD | — |
| `maxPrice` | Integer | Maximum price in USD | — |
| `startUrls` | List | Klook activity URLs to enrich (mode=byActivityUrls) | — |
| `maxItems` | Integer | Maximum activities to return (1–5000) | `50` |

### Sort Options

| Value | Description |
|-------|-------------|
| `most_relevant` | Most relevant (default) |
| `top_picks` | Klook top picks |
| `price_asc` | Price: low to high |
| `price_desc` | Price: high to low |
| `rating` | Highest rated |
| `newest` | Newest listings |

## Output

Each record contains:

| Field | Type | Description |
|-------|------|-------------|
| `activityId` | String | Unique Klook activity ID |
| `title` | String | Activity name |
| `url` | String | Full Klook activity URL |
| `thumbnailUrl` | String | Cover image URL |
| `city` | String | City where activity takes place |
| `category` | String | Activity category (e.g. Theme parks) |
| `price` | Float | Current selling price (USD) |
| `originalPrice` | Float | Original/market price before discount |
| `discountPercent` | Integer | Discount percentage (if applicable) |
| `currency` | String | Currency code (`USD`) |
| `rating` | Float | Average rating out of 5 |
| `reviewCount` | Integer | Total number of reviews |
| `tags` | Array | Activity tags (e.g. Instant confirmation, Free cancellation) |
| `isSoldOut` | Boolean | Whether activity is currently sold out |
| `recordType` | String | Always `klookActivity` |
| `scrapedAt` | String | ISO 8601 scrape timestamp |

### Example Output

```json
{
  "activityId": "695",
  "title": "Tokyo Disney Resort - Tokyo Disneyland & Tokyo DisneySea Park Tickets",
  "url": "https://www.klook.com/en-US/activity/695-tokyo-disney-resort-1-day-pass-tokyo/",
  "thumbnailUrl": "https://res.klook.com/image/upload/activities/frrnxyfrq6uzs1kapdct.jpg",
  "city": "Tokyo",
  "category": "Theme parks",
  "price": 52.35,
  "currency": "USD",
  "rating": 4.8,
  "reviewCount": 95464,
  "tags": ["Book now for tomorrow", "Instant confirmation"],
  "isSoldOut": false,
  "recordType": "klookActivity",
  "scrapedAt": "2026-05-15T12:00:00+00:00"
}
```

## FAQ

**Q: Do I need a Klook account or API key?**
A: No. The scraper uses Klook's public search API which requires no authentication.

**Q: How many activities can I scrape per run?**
A: Up to 5,000 activities per run.

**Q: What cities are supported?**
A: Any city that Klook covers — Tokyo, Paris, New York, London, Bangkok, Bali, Dubai, and thousands more worldwide. Just enter the city name in the `city` field.

**Q: Are prices in USD?**
A: Yes, all prices are normalized to USD. Klook serves multiple currencies; this actor requests USD pricing.

**Q: What does `discountPercent` mean?**
A: If an activity has a promotional discount, this shows the percentage off the original price. For example, if `originalPrice=50` and `price=35`, `discountPercent=30`.

**Q: Can I filter by minimum rating?**
A: Yes — set `minRating` to any value from 0.0 to 5.0. Only activities at or above that rating will be returned.

**Q: Why do some activities have no `originalPrice`?**
A: `originalPrice` is only included when a discount is active (market price higher than selling price). If there's no active discount, only `price` is shown.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/klook-experiences-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
