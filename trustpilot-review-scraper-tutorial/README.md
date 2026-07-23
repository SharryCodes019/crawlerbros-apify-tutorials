# Trustpilot Review Scraper Tutorial: Run This Apify Actor with Python

Extract reviews from Trustpilot for any company. Get review text, ratings, dates, reviewer info, verification status, company replies, and trust scores.

This repository shows how to run [Trustpilot Review Scraper](https://apify.com/crawlerbros/trustpilot-review-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/trustpilot-review-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/trustpilot-review-scraper](https://apify.com/crawlerbros/trustpilot-review-scraper)
- **SEO title:** Trustpilot Review Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract reviews from Trustpilot for any company. Get review text, ratings, dates, reviewer info, verification status, company replies, and trust scores.

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

# Trustpilot Review Scraper

Extract reviews from Trustpilot for any company — get review text, star ratings, reviewer details, verification status, company replies, and trust scores.

## What is Trustpilot Review Scraper?

A fast and free tool that extracts review data from [Trustpilot](https://www.trustpilot.com/). Provide company review page URLs and get structured data for each review including ratings, reviewer information, dates, and company responses.

Perfect for competitive analysis, reputation monitoring, customer sentiment research, and lead generation.

## What data can you extract?

**Review details:**
- Review title and full text
- Star rating (1-5)
- Published date, experience date, updated date
- Language, likes/useful count, source
- Direct review URL

**Reviewer info:**
- Reviewer name, country, and ID
- Total reviews by this reviewer
- Verification status and level

**Company response:**
- Reply text and date (when available)

**Business info:**
- Company name, domain, and Trustpilot ID
- Trust score and total review count
- Website URL

## Input

### Company URLs

Provide Trustpilot company review page URLs. Go to [trustpilot.com](https://www.trustpilot.com/), search for a company, and copy the URL.

**Example:** `https://www.trustpilot.com/review/amazon.com`

### Options

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| startUrls | array | — | Trustpilot company review page URLs (required) |
| maxReviews | integer | `100` | Max reviews per company (up to 200) |
| filterStars | string | All | Filter by star rating (1-5) |
| filterLanguage | string | `"all"` | Filter by language (ISO code, e.g. "en", "de") |
| onlyVerified | boolean | `false` | Only include verified purchase reviews |
| onlyWithReplies | boolean | `false` | Only include reviews with company replies |

At least one URL must be provided in `startUrls`.

## Output

Each item in the dataset represents one review:

```json
{
    "businessName": "Notion",
    "businessDomain": "notion.so",
    "businessId": "5bdd0af10000ff0004ee214a",
    "trustScore": 3.2,
    "totalReviews": 1842,
    "businessUrl": "http://www.notion.so",
    "reviewId": "65a1b2c3d4e5f6a7b8c9d0e1",
    "reviewUrl": "https://www.trustpilot.com/reviews/65a1b2c3d4e5f6a7b8c9d0e1",
    "title": "Great productivity tool",
    "text": "Notion has transformed how our team manages projects...",
    "rating": 5,
    "language": "en",
    "authorName": "John D.",
    "authorId": "5f1234567890abcdef123456",
    "authorCountry": "US",
    "authorReviewCount": 12,
    "isVerified": false,
    "verificationLevel": "not-verified",
    "publishedDate": "2025-01-12T14:30:00.000Z",
    "experiencedDate": "2025-01-10T00:00:00.000Z",
    "updatedDate": null,
    "replyText": null,
    "replyDate": null,
    "likes": 3,
    "source": "Organic",
    "reviewsOnSameDomain": 1,
    "scrapedAt": "2025-03-16T12:00:00.000000+00:00"
}
```

### Output Fields

| Field | Type | Description |
|-------|------|-------------|
| businessName | string | Company display name |
| businessDomain | string | Domain name on Trustpilot |
| businessId | string | Trustpilot business unit ID |
| trustScore | number | Company trust score (1.0-5.0) |
| totalReviews | integer | Total review count for the company |
| businessUrl | string | Company website URL |
| reviewId | string | Unique review identifier |
| reviewUrl | string | Direct link to the review |
| title | string | Review title/headline |
| text | string | Full review text |
| rating | integer | Star rating (1-5) |
| language | string | Detected review language (ISO code) |
| authorName | string | Reviewer display name |
| authorId | string | Reviewer Trustpilot ID |
| authorCountry | string/null | Reviewer country code (e.g. "US", "GB") |
| authorReviewCount | integer | Total reviews by this reviewer |
| isVerified | boolean | Whether purchase was verified |
| verificationLevel | string | Verification level detail |
| publishedDate | string | When the review was published (ISO 8601) |
| experiencedDate | string | When the experience occurred (ISO 8601) |
| updatedDate | string/null | When review was last updated, if ever |
| replyText | string/null | Company reply text |
| replyDate | string/null | When company replied (ISO 8601) |
| likes | integer | Number of "useful" votes |
| source | string | Review source (e.g. "Organic") |
| reviewsOnSameDomain | integer | Reviewer's review count for this company |
| scrapedAt | string | When the data was scraped (ISO 8601) |

## How to use

### Quick start

1. Go to [Trustpilot](https://www.trustpilot.com/) and find a company
2. Copy the URL (e.g. `https://www.trustpilot.com/review/amazon.com`)
3. Paste into the **Company URLs** field
4. Click **Save & Start**

### Filter by rating

1. Add company URLs
2. Set **Filter by Stars** to your desired rating
3. This filters reviews server-side for accurate results

### Multiple companies

Add multiple URLs to scrape reviews from several companies in a single run. Each company is processed sequentially with rate limiting.

## Limitations

- **Maximum 200 reviews per company**: Trustpilot limits unauthenticated access to 10 pages (20 reviews per page)
- **Sort order**: Reviews are always returned in recency order (newest first)
- **Star filtering**: When filtering by stars, the 200-review limit applies to the filtered set

## Frequently Asked Questions

### How many reviews can I extract?

Up to 200 reviews per company per run. This is a Trustpilot platform limitation for unauthenticated access. You can extract more by filtering different star ratings in separate runs.

### Can I filter reviews by star rating?

Yes. Use the **Filter by Stars** dropdown to select a specific star rating. This filter is applied server-side, so you get up to 200 reviews of that specific rating.

### Can I filter by language?

Yes. Enter a language ISO code (e.g. "en" for English, "de" for German, "fr" for French) in the **Filter Language** field. Use "all" for all languages.

### Why are some fields null?

- `replyText` and `replyDate` are null when the company hasn't replied to the review
- `updatedDate` is null when the review has never been edited
- `authorCountry` may be null if the reviewer hasn't set their location

### Can I scrape multiple companies at once?

Yes. Add multiple URLs to the **Company URLs** field. Each company is processed in sequence with appropriate delays.

### Does this require a proxy?

No. This scraper works without any proxy or authentication. Trustpilot review pages are publicly accessible.

### Is it legal to scrape Trustpilot reviews?

Trustpilot review pages are publicly accessible. Scraping public data is generally legal, but consult legal counsel for your specific use case and jurisdiction.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/trustpilot-review-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
