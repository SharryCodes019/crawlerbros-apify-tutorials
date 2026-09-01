# Udemy Course Scraper Tutorial: Run This Apify Actor with Python

Scrape Udemy courses with search by keyword, browse by category, filter by level/rating/price. Extracts title, rating, reviews, subscribers, instructors, price, and more.

This repository shows how to run [Udemy Course Scraper](https://apify.com/crawlerbros/udemy-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/udemy-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/udemy-scraper](https://apify.com/crawlerbros/udemy-scraper)
- **SEO title:** Udemy Course Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Udemy courses with search by keyword, browse by category, filter by level/rating/price. Extracts title, rating, reviews, subscribers, instructors, price, and more.

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

# Udemy Course Scraper

Scrape **Udemy** course data at scale — search by keyword, browse by category, filter by level, rating, price, and subscriber count. No account or API key required.

## What data do you get?

| Field | Description |
|---|---|
| `courseId` | Udemy internal course ID |
| `title` | Course title |
| `headline` | Short course description/tagline |
| `url` | Full course URL |
| `isPaid` | Whether the course is paid |
| `price` | Price string (e.g. "$12.99") |
| `priceNumeric` | Price as a float |
| `avgRating` | Average rating (0.0–5.0) |
| `numReviews` | Total review count |
| `numSubscribers` | Enrolled student count |
| `numLectures` | Total lecture count |
| `contentLengthMin` | Total video length in minutes |
| `level` | Difficulty level |
| `primaryCategory` | Top-level category |
| `primarySubcategory` | Subcategory |
| `instructors` | List of instructor display names |
| `primaryInstructor` | First instructor name |
| `imageUrl` | Course thumbnail (480×270) |
| `publishedTitle` | URL slug |

## Input

| Field | Type | Description |
|---|---|---|
| `mode` | select | What to fetch (see Modes below) |
| `query` | string | Keyword to search (mode=search) |
| `courseId` | string | Udemy course ID (mode=byCourseId) |
| `instructorId` | string | Udemy instructor user ID (mode=byInstructor) |
| `category` | select | Top-level category filter/browse |
| `subcategory` | string | Subcategory slug (mode=byCategory) |
| `ordering` | select | Sort: relevance, popularity, highest-rated, newest |
| `level` | select | All Levels / Beginner / Intermediate / Expert |
| `freeOnly` | boolean | Only return free courses |
| `minRating` | number | Minimum average rating (0.0–5.0) |
| `minSubscribers` | integer | Minimum enrolled student count |
| `maxItems` | integer | Max courses to return (default 50) |

## Modes

| Mode | Description |
|---|---|
| `search` (default) | Full-text search across all courses |
| `byCourseId` | Fetch a single course by ID |
| `byCategory` | Browse all courses in a category or subcategory |
| `byInstructor` | All courses by a specific instructor |

## Sample Input

```json
{
  "mode": "search",
  "query": "Python programming",
  "ordering": "popularity",
  "minRating": 4.5,
  "maxItems": 20
}
```

## Sample Output

```json
{
  "courseId": 394580,
  "title": "The Complete Python Bootcamp From Zero to Hero in Python",
  "url": "https://www.udemy.com/course/complete-python-bootcamp/",
  "isPaid": true,
  "price": "$12.99",
  "priceNumeric": 12.99,
  "avgRating": 4.65,
  "numReviews": 503591,
  "numSubscribers": 1800000,
  "numLectures": 155,
  "contentLengthMin": 2230,
  "level": "All Levels",
  "primaryCategory": "Development",
  "instructors": ["Jose Portilla"],
  "primaryInstructor": "Jose Portilla",
  "recordType": "course",
  "siteName": "Udemy",
  "scrapedAt": "2026-05-10T12:00:00+00:00"
}
```

## Categories

Development, Business, Finance & Accounting, IT & Software, Office Productivity, Personal Development, Design, Marketing, Lifestyle, Photography & Video, Health & Fitness, Music, Teaching & Academics

## FAQs

**Do I need a Udemy account or API key?**
No. The scraper uses Udemy's public API which does not require authentication for course data.

**How accurate are subscriber counts?**
Subscriber counts are real-time values from the Udemy API. They represent total enrolled students.

**Can I filter for only free courses?**
Yes — set `freeOnly: true`. Free courses have `isPaid: false`.

**What ordering options are available?**
`relevance` (default), `popularity`, `highest-rated`, `newest`.

**How many courses can I scrape?**
Up to 1000 per run using `maxItems`. Pagination is handled automatically.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/udemy-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
