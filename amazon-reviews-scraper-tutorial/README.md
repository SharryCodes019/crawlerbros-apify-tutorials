# Amazon Reviews Scraper Tutorial: Run This Apify Actor with Python

Extract customer reviews from any Amazon product with filtering by star rating, verified purchases, and sorting options. Returns structured data including review text, ratings, helpful counts, dates, sentiment hints, images, and more across 19+ Amazon domains.

This repository shows how to run [Amazon Reviews Scraper](https://apify.com/crawlerbros/amazon-reviews-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/amazon-reviews-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/amazon-reviews-scraper](https://apify.com/crawlerbros/amazon-reviews-scraper)
- **SEO title:** Amazon Reviews Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract customer reviews from any Amazon product with filtering by star rating, verified purchases, and sorting options. Returns structured data including review text, ratings, helpful counts, dates, sentiment hints, images, and more across 19+ Amazon domains.

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

# Amazon Reviews Scraper

Extract customer reviews from any Amazon product across **19+ Amazon
domains** worldwide. Returns structured review data including text, star
rating, helpful count, date, location, sentiment hint, images, variant,
and reviewer profile (optional, GDPR-aware).

This actor runs in **cookie-free public-data mode** and ships with a
mandatory Apify residential proxy. There is nothing for you to log into
or maintain — give it product URLs, get reviews back.

> **Proxy note:** Amazon blocks all datacenter IPs. This actor requires a
> US residential proxy, which is included in the **Apify Starter plan or
> above**. Free-plan accounts will not return results.

## Features

- **Multi-product support**: Scrape reviews from many Amazon products in one run
- **19 Amazon domains**: amazon.com, .co.uk, .de, .fr, .it, .es, .ca, .com.au, .co.jp, .in, .com.br, .com.mx, .nl, .sg, .ae, .sa, .pl, .se, .com.tr
- **Smart filtering**: filter by star rating (1-5)
- **Flexible sorting**: most helpful or most recent
- **GDPR aware**: optional inclusion of reviewer name / profile / avatar
- **Image extraction**: optional capture of reviewer-uploaded images
- **Stealth + residential proxy**: Chromium with anti-detection scripts and
  sticky-session residential routing
- **Built-in retries**: up to 3 fresh-session retries on transient blocks

## Output Schema

Each review is returned with the following structure (omit-empty: any field
that the source did not populate is dropped, never returned as `null`).

```json
{
  "productAsin": "B09X7MPX8L",
  "ratingScore": 5,
  "reviewTitle": "Amazing product!",
  "reviewUrl": "https://www.amazon.com/gp/customer-reviews/R1234567890",
  "reviewReaction": "123 people found this helpful",
  "reviewedIn": "Reviewed in the United States on January 15, 2024",
  "reviewDescription": "This is the full review text...",
  "isVerified": true,
  "variant": "Size: Large, Color: Blue",
  "reviewImages": ["https://images-na.ssl-images-amazon.com/..."],
  "position": 1,
  "reviewId": "R1234567890",
  "helpfulCount": 123,
  "reviewDate": "2024-01-15T00:00:00",
  "reviewLocation": "United States",
  "sentimentHint": "positive",
  "wordCount": 150,
  "hasImages": true,
  "imageCount": 2,
  "scrapedAt": "2024-01-20T10:30:00Z",
  "sourceUrl": "https://www.amazon.com/dp/B09X7MPX8L"
}
```

`reviewerName`, `reviewerProfile`, and `reviewerAvatar` are returned **only**
when `includeGdprSensitive` is set to `true`.

## Input Configuration

| Field                  | Type    | Description                                           | Default          |
| ---------------------- | ------- | ----------------------------------------------------- | ---------------- |
| `productUrls`          | array   | Amazon product URLs (required)                        | -                |
| `proxyConfiguration`   | object  | Apify residential proxy (required)                    | RESIDENTIAL      |
| `maxReviews`           | integer | Reviews per product (1–15, capped by inline render)   | 15               |
| `sortBy`               | enum    | `helpful` or `recent`                                 | `helpful`        |
| `filterByStar`         | enum    | `""`, `"1"`, `"2"`, `"3"`, `"4"`, `"5"`               | `""` (all)       |
| `includeImages`        | boolean | Extract reviewer-uploaded images                       | `true`           |
| `includeGdprSensitive` | boolean | Include reviewer name / profile / avatar               | `false`          |
| `country`              | enum    | Amazon domain (19 supported)                          | `amazon.com`     |
| `maxConcurrency`       | integer | Concurrent pages (1-5)                                | `1`              |
| `requestTimeout`       | integer | Per-page timeout in seconds (30–180)                  | `60`             |
| `retryCount`           | integer | Fresh-session retries on blocks (1–10)                | `3`              |

### Example input

```json
{
  "productUrls": [
    "https://www.amazon.com/dp/B09X7MPX8L"
  ],
  "maxReviews": 15,
  "sortBy": "helpful",
  "filterByStar": "",
  "includeImages": true,
  "includeGdprSensitive": false,
  "country": "amazon.com",
  "proxyConfiguration": {
    "useApifyProxy": true,
    "apifyProxyGroups": ["RESIDENTIAL"]
  }
}
```

## Cookie-Free Public-Data Mode

This actor never logs in to Amazon and never carries authenticated session
cookies. That choice keeps it simple to run, but it imposes hard limits
that are dictated by Amazon — not by the scraper itself.

**What you get:**
- Up to **~8–13 "top reviews" per ASIN** — Amazon's inline review block on
  the `/dp/{ASIN}` product page
- All public review fields (text, rating, date, location, helpful count,
  images, variant)

**What is not supported:**
- **Pagination beyond the inline block.** Amazon now redirects every
  anonymous `/product-reviews/{ASIN}` request to `/ap/signin`, regardless
  of country, TLS fingerprint, or warmup pattern (verified across 6
  mitigation strategies in May 2026). Reviews are therefore extracted
  from the inline block on the product detail page, which renders 8–13
  reviews and has no "next page".
- **Star-rating filter at fetch time.** The `filterByStar` input still
  works, but is applied client-side to the inline block — expect 0–5
  reviews per star.
- **The verified-purchase filter** (`reviewerType=avp_only_reviews`)
  requires an authenticated session and is therefore not exposed as an
  input. The `isVerified` flag IS still populated per review.

**Why a residential proxy is required:**
Amazon aggressively blocks anonymous datacenter IPs within seconds. The
`proxyConfiguration` field is therefore `required` in the input schema
and the actor exits cleanly with a typed status message if missing.
Residential proxies are available on the **Apify Starter plan or above**.

## Supported Amazon Domains

| Domain        | Country        |
| ------------- | -------------- |
| amazon.com    | United States  |
| amazon.co.uk  | United Kingdom |
| amazon.de     | Germany        |
| amazon.fr     | France         |
| amazon.it     | Italy          |
| amazon.es     | Spain          |
| amazon.ca     | Canada         |
| amazon.com.au | Australia      |
| amazon.co.jp  | Japan          |
| amazon.in     | India          |
| amazon.com.br | Brazil         |
| amazon.com.mx | Mexico         |
| amazon.nl     | Netherlands    |
| amazon.sg     | Singapore     |
| amazon.ae     | UAE            |
| amazon.sa     | Saudi Arabia   |
| amazon.pl     | Poland         |
| amazon.se     | Sweden         |
| amazon.com.tr | Turkey         |

## GDPR Compliance

When `includeGdprSensitive=false` (the default) the scraper omits:
- Reviewer names
- Reviewer profile links
- Reviewer avatars

Set it to `true` only if you have a lawful basis to process that data.

## FAQs

**Can I get more than ~13 reviews per product?**
No. In cookie-free public-data mode, anonymous `/product-reviews/` pages
redirect to a sign-in wall, so reviews come from the inline block on the
`/dp/` product page — Amazon renders **~8-13 "top reviews" per ASIN**
there, with no "next page". Higher caps require authenticated sessions,
which this actor intentionally does not support.

**Why is my run returning 0 reviews?**
The most common causes are:
1. `proxyConfiguration` was omitted or set to something other than `RESIDENTIAL` — check the run log for a `Residential proxy required` message.
2. The product ASIN is discontinued or the URL is invalid — the actor returns 0 reviews gracefully in this case.
3. `filterByStar` is set to a low star value (1–3) — Amazon's top-helpful inline block is almost exclusively 4–5 star reviews; filtering below 4 stars typically returns 0.

**Can I scrape reviews translated into other languages?**
Yes — pick the corresponding domain in `country` (e.g. `amazon.de` for
German). Reviews are returned in the language of the chosen storefront.

**Do you support reviews from a specific verified-purchase filter?**
No. That filter requires an authenticated Amazon session. The `isVerified`
field on each review is still populated, so you can filter the output
yourself in your downstream pipeline.

**How is the data deduplicated?**
Reviews are deduplicated by `reviewId` across products in a single run
(there is no per-page pagination in cookie-free mode, so pagination
duplicates cannot occur).

**Are you respecting Amazon's robots.txt?**
Yes. This actor only fetches `/dp/{ASIN}` product pages, which Amazon's
robots.txt does not disallow for `User-agent: *`. There is no
`Crawl-delay` directive on amazon.com; the actor still paces requests
via `requestTimeout` and a default 2 s inter-product delay.

## Limitations

- **~8-13 reviews per ASIN** in cookie-free mode (Amazon's inline `/dp/`
  block ceiling). Anonymous `/product-reviews/` pages redirect to
  sign-in.
- Verified-purchase pre-filtering is unavailable; `isVerified` is still set per review.
- Run-to-run review counts can vary by +/- 10% as Amazon shuffles the
  order of "Most helpful" reviews.
- A residential Apify proxy is required; running without one exits cleanly
  with a typed status message and produces no records.

## Integration

```bash
# Get results via API
curl "https://api.apify.com/v2/datasets/{datasetId}/items?token={apiToken}"
```

Output formats supported by Apify: JSON, CSV, Excel, RSS, HTML table.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/amazon-reviews-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
