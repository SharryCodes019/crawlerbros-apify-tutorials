# Glassdoor Reviews Scraper Tutorial: Run This Apify Actor with Python

Scrape employee reviews from Glassdoor for any company. Extracts ratings, pros, cons, advice to management, job titles, employment status, and more. Supports sorting by date or relevance.

This repository shows how to run [Glassdoor Reviews Scraper](https://apify.com/crawlerbros/glassdoor-reviews-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/glassdoor-reviews-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/glassdoor-reviews-scraper](https://apify.com/crawlerbros/glassdoor-reviews-scraper)
- **SEO title:** Glassdoor Reviews Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape employee reviews from Glassdoor for any company. Extracts ratings, pros, cons, advice to management, job titles, employment status, and more. Supports sorting by date or relevance.

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

# Glassdoor Reviews Scraper

Scrape employee reviews from Glassdoor for any company. Get ratings, pros, cons, advice to management, job titles, employment status, and more.

## What is Glassdoor Reviews Scraper?

Glassdoor Reviews Scraper is an Apify actor that extracts employee reviews from any company's Glassdoor reviews page. It returns structured review data including overall and sub-category ratings, reviewer job title and location, employment status, and full review text.

## Features

- **Any company** — Scrape reviews from any company on Glassdoor
- **Full review text** — Pros, cons, and advice to management
- **Detailed ratings** — Overall rating plus sub-ratings (work-life balance, culture, compensation, etc.)
- **Reviewer details** — Job title, location, employment status, current/former employee
- **Sort options** — Sort by newest first or most relevant
- **Cookie support** — Provide a Glassdoor session cookie for full pagination (100+ reviews)
- **Works without login** — Scrapes ~3-6 preview reviews without any account

## Use Cases

- **Employer reputation analysis** — Understand employee sentiment at any company
- **Competitive benchmarking** — Compare employee satisfaction across competitors
- **Due diligence** — Research company culture before investing or partnering
- **Hiring intelligence** — Understand what employees value and complain about
- **Trend analysis** — Track review sentiment over time by sorting by date
- **Culture research** — Identify common themes in pros, cons, and management advice

## Input

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| Company Reviews URL | String | **Required** | Glassdoor company reviews page URL (e.g., `https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm`) |
| Maximum Items | Integer | 100 | Max reviews to scrape (1–1000). Without a cookie, limited to ~3-6 reviews. |
| Sort Order | Select | Newest First | How to sort reviews: Newest First or Most Relevant |
| Session Cookie | String | — | Optional Glassdoor session cookie for full pagination. See instructions below. |

### Example input — Without cookie (preview reviews)

```json
{
    "companyUrl": "https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm",
    "maxItems": 10,
    "sort": "DATE"
}
```

### Example input — With cookie (full pagination)

```json
{
    "companyUrl": "https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm",
    "maxItems": 100,
    "sort": "DATE",
    "cookie": "GSESSIONID=abc123; gdId=xyz789"
}
```

### How to get your Glassdoor session cookie

1. Log into Glassdoor in your browser
2. Open DevTools (F12) → Application tab → Cookies → glassdoor.com
3. Copy the full cookie string (all name=value pairs separated by semicolons)
4. Paste it into the **Session Cookie** field

Alternatively, use a browser extension like "EditThisCookie" to export cookies as JSON — the scraper accepts both formats.

## Output

Each review produces one item in the output dataset:

| Field | Type | Description |
|-------|------|-------------|
| reviewId | Integer | Glassdoor's unique review ID |
| reviewDate | String | ISO timestamp when the review was posted |
| title | String | Review headline/summary |
| pros | String | What the reviewer liked about the company |
| cons | String | What the reviewer disliked |
| advice | String | Advice to management (may be empty) |
| ratingOverall | Integer | Overall rating (1–5) |
| ratingWorkLifeBalance | Integer | Work-life balance rating (0 if not provided) |
| ratingCultureAndValues | Integer | Culture & values rating |
| ratingDiversityAndInclusion | Integer | Diversity & inclusion rating |
| ratingSeniorLeadership | Integer | Senior leadership rating |
| ratingCareerOpportunities | Integer | Career opportunities rating |
| ratingCompensationAndBenefits | Integer | Compensation & benefits rating |
| ratingCeo | String | CEO approval (e.g., "APPROVE", "DISAPPROVE", "NO_OPINION") |
| ratingBusinessOutlook | String | Business outlook (e.g., "POSITIVE", "NEGATIVE", "NEUTRAL") |
| ratingRecommendToFriend | String | Recommend to a friend (e.g., "POSITIVE", "NEGATIVE") |
| jobTitle | String | Reviewer's job title |
| location | String | Reviewer's work location |
| employmentStatus | String | Employment status (e.g., "REGULAR", "PART_TIME", "INTERN") |
| isCurrentJob | Boolean | Whether the reviewer currently works there |
| lengthOfEmployment | Integer | Length of employment in months |
| countHelpful | Integer | Number of "helpful" votes |
| countNotHelpful | Integer | Number of "not helpful" votes |
| companyName | String | Company name |
| companyId | Integer | Glassdoor company ID |

### Sample output

```json
{
    "reviewId": 103314593,
    "reviewDate": "2026-03-25T21:58:32.667",
    "title": "Good pay and perks, but work can be dull",
    "pros": "Good Pay, Free Food, Good Office location",
    "cons": "Work can be boring, Performance Reviews are stressful. Promotions are slim.",
    "advice": "",
    "ratingOverall": 5,
    "ratingWorkLifeBalance": 4,
    "ratingCultureAndValues": 4,
    "ratingDiversityAndInclusion": 5,
    "ratingSeniorLeadership": 3,
    "ratingCareerOpportunities": 3,
    "ratingCompensationAndBenefits": 5,
    "ratingCeo": "APPROVE",
    "ratingBusinessOutlook": "POSITIVE",
    "ratingRecommendToFriend": "POSITIVE",
    "jobTitle": "Software Engineer",
    "location": "Tokyo",
    "employmentStatus": "REGULAR",
    "isCurrentJob": false,
    "lengthOfEmployment": 9,
    "countHelpful": 2,
    "countNotHelpful": 0,
    "companyName": "Google",
    "companyId": 9079
}
```

## How to use

### Quick start (without cookie)

1. Go to a company's Glassdoor reviews page in your browser
2. Copy the URL (e.g., `https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm`)
3. Paste it into the **Company Reviews URL** field
4. Click **Start**

This returns ~3-6 preview reviews that Glassdoor shows to non-logged-in visitors.

### Full pagination (with cookie)

1. Log into your Glassdoor account in a browser
2. Export your cookies (see instructions above)
3. Paste the cookie string into the **Session Cookie** field
4. Set **Maximum Items** to your desired number
5. Click **Start**

With a valid session cookie, the scraper can paginate through hundreds of reviews.

## How many reviews can I scrape?

| Mode | Reviews | Speed |
|------|---------|-------|
| Without cookie | ~3-6 | ~60-90 seconds |
| With cookie | Up to 1000+ | ~30 reviews per minute |

Without a cookie, Glassdoor only shows a handful of preview reviews. With a valid session cookie, the scraper can paginate through the full review history.

## Tips

- **Start without a cookie** — Test with a small run first to verify the URL and output format
- **Use a fresh cookie** — Glassdoor session cookies expire; use one from a recent browser session
- **Sort by date** — Newest-first sorting gives you the most recent reviews
- **Large companies have thousands of reviews** — Set a reasonable maxItems to control runtime

## FAQ

**Do I need a Glassdoor account?**
Not for preview reviews (~3-6 per company). For full pagination, you need a Glassdoor session cookie from a logged-in account.

**Why only 3-6 reviews without a cookie?**
Glassdoor requires login to view more than a few reviews. This is a Glassdoor business model limitation, not a scraper limitation.

**Why does the scraper use residential proxy?**
Glassdoor uses DataDome anti-bot protection. Residential proxy is required to bypass this. The proxy is automatically configured on Apify.

**Why are sub-ratings zero?**
Preview reviews (without cookie) often have limited data. Sub-ratings are fully available when using a session cookie.

**What if the scraper returns 0 reviews?**
Glassdoor's anti-bot protection blocks some sessions. The scraper retries with new browser sessions automatically (up to 8 attempts). If it consistently fails, try again later for a fresh IP rotation.

**Is my cookie stored securely?**
Yes. The cookie field is marked as a secret in the input schema and is not logged or stored in the output.

**What cookie format is accepted?**
Both plain cookie strings (`name1=value1; name2=value2`) and JSON arrays from browser extensions are accepted.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/glassdoor-reviews-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
