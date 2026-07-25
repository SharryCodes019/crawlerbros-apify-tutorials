# Goodreads Book Scraper Tutorial: Run This Apify Actor with Python

Extract book data from Goodreads: titles, authors, ratings, reviews, genres, ISBN, publisher, and more. HTTP-based, no proxy required.

This repository shows how to run [Goodreads Book Scraper](https://apify.com/crawlerbros/goodreads-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/goodreads-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/goodreads-scraper](https://apify.com/crawlerbros/goodreads-scraper)
- **SEO title:** Goodreads Book Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract book data from Goodreads: titles, authors, ratings, reviews, genres, ISBN, publisher, and more. HTTP-based, no proxy required.

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

# Goodreads Book Scraper

Extract structured book data from Goodreads.com. Get titles, authors, author profile URLs, ratings, reviews, genres, ISBN, publisher, and more. No proxy required.

## Features

- Extract book details from direct Goodreads URLs
- Search Goodreads by keyword and scrape matching books
- **19 output fields** including ratings, genres, ISBN, publisher, author URLs
- HTTP-based (no browser) — fast and reliable
- No proxy, cookies, or authentication needed
- Works with any public Goodreads book page

## Input

| Field | Type | Description |
|-------|------|-------------|
| `bookUrls` | Array | Direct Goodreads book URLs |
| `searchQueries` | Array | Search terms to find books |
| `maxResultsPerQuery` | Integer | Max books per search (default 10) |

### Example Input

```json
{
    "bookUrls": [
        "https://www.goodreads.com/book/show/4671.The_Great_Gatsby",
        "https://www.goodreads.com/book/show/23692271-sapiens"
    ],
    "maxResultsPerQuery": 5
}
```

## Output

| Field | Type | Description |
|-------|------|-------------|
| `title` | String | Book title |
| `url` | String | Goodreads book URL |
| `bookId` | String | Goodreads book ID |
| `authors` | Array | Author names |
| `authorUrls` | Array | Author profile URLs on Goodreads |
| `description` | String | Book description |
| `isbn` | String | ISBN-10 |
| `isbn13` | String | ISBN-13 |
| `averageRating` | Number | Average rating (0-5) |
| `ratingsCount` | Integer | Number of ratings |
| `reviewsCount` | Integer | Number of reviews |
| `pagesCount` | Integer | Number of pages |
| `publishedYear` | Integer | Year of publication |
| `publisher` | String | Publisher name |
| `language` | String | Language |
| `format` | String | Paperback, Hardcover, etc. |
| `genres` | Array | List of genres |
| `coverImage` | String | Cover image URL |
| `scrapedAt` | String | ISO timestamp |

## Use Cases

- Book database enrichment
- Literature research and analysis
- Author bibliography collection
- Reading recommendation systems
- Publishing industry research

## FAQ

### Is a proxy required?

No. Goodreads' public pages are accessible without a proxy. The scraper uses httpx for direct HTTP requests.

### How does the scraper work?

It parses the JSON-LD structured data and `__NEXT_DATA__` embedded in Goodreads book pages, extracting all metadata reliably.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/goodreads-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
