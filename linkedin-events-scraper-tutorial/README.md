# LinkedIn Events Scraper Tutorial: Run This Apify Actor with Python

Scrape LinkedIn Events by keyword search or direct event URLs. Extract event name, date, format, organizer, attendee count, and description. Great for event research, lead generation, and competitive intelligence.

This repository shows how to run [LinkedIn Events Scraper](https://apify.com/crawlerbros/linkedin-events-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/linkedin-events-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/linkedin-events-scraper](https://apify.com/crawlerbros/linkedin-events-scraper)
- **SEO title:** LinkedIn Events Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape LinkedIn Events by keyword search or direct event URLs. Extract event name, date, format, organizer, attendee count, and description. Great for event research, lead generation, and competitive intelligence.

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

# LinkedIn Events Scraper

Scrape LinkedIn Events by **keyword search** or directly from **event page URLs**. Extract event name, dates, format (online/in-person/hybrid), organizer, attendee count, speakers, venue address, cover image, and full description — all in one structured dataset.

## What It Does

- **Keyword search**: Find events matching any topic (e.g., "AI conference 2025", "marketing summit", "AWS re:Invent") using the LinkedIn Voyager API
- **Direct URL scraping**: Provide specific LinkedIn Event URLs to extract full event details
- **Filter by format**: Virtual, In-Person, or Hybrid
- **Filter by date**: Upcoming, this week, this month, past events, or recency (last 24h / week / month)
- **Filter by language**: English, Spanish, French, German, Portuguese, Italian, Dutch, Chinese, Japanese
- **Filter by location**: Free-text location filter appended to the search
- **Pagination**: Automatically pages through results up to your configured maximum

## Use Cases

- **Event research**: Discover industry events and conferences in any field
- **Lead generation**: Find events where your prospects gather
- **Competitive intelligence**: Track events organized by competitors or partners
- **Market research**: Understand event trends in a specific vertical
- **Recruitment**: Identify tech talks, meetups, and career fairs

## Input

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `searchQuery` | String | Yes* | Keyword to search for LinkedIn Events (e.g., "AI conference 2025") |
| `eventUrls` | Array | Yes* | Direct LinkedIn Event URLs to scrape |
| `maxEvents` | Integer | No | Max events to collect (default: 50, max: 500) |
| `datePosted` | Enum | No | Filter by posting recency: any time, past 24h, past week, past month |
| `eventType` | Enum | No | Filter by format: VIRTUAL, IN_PERSON, or HYBRID |
| `dateRange` | Enum | No | Filter by timing: UPCOMING, THIS_WEEK, THIS_MONTH, or PAST |
| `location` | String | No | Filter by location (e.g., "New York", "London", "Remote") |
| `language` | Enum | No | Filter by event language (en, es, fr, de, pt, it, nl, zh, ja) |
| `cookie` | String | Yes** | Your LinkedIn session cookie (li_at or full JSON export) |
| `proxyConfiguration` | Object | No | Apify proxy settings |

\* At least one of `searchQuery` or `eventUrls` is required.
\** Required when using `searchQuery`. Optional for direct URL scraping.

### Accepted Event URL Formats

```
https://www.linkedin.com/events/6234567890123456789/
https://www.linkedin.com/events/ai-summit-2025-123456789/
```

### Cookie Setup

1. Log in to LinkedIn in your browser
2. Open Developer Tools → Application → Cookies → `www.linkedin.com`
3. Copy the `li_at` cookie value
4. Paste it into the `cookie` field

For best results, export all LinkedIn cookies as a JSON array using a browser extension like EditThisCookie or Cookie-Editor. This provides the JSESSIONID as well, which improves session reliability.

## Output

Each scraped event produces one dataset record:

| Field | Type | Description |
|-------|------|-------------|
| `eventName` | String | Full event name |
| `eventUrl` | String | Direct URL to the LinkedIn Event page |
| `eventId` | String | Unique event identifier from the URL |
| `startDate` | String | Event start date/time (ISO 8601, UTC) |
| `endDate` | String | Event end date/time (ISO 8601, UTC) |
| `format` | String | Event format code: `ONLINE`, `IN_PERSON`, or `HYBRID` |
| `eventType` | String | Human-friendly type: `VIRTUAL`, `IN_PERSON`, or `HYBRID` |
| `timezone` | String | Event timezone identifier (e.g., `AMERICA_NEW_YORK`) |
| `organizerName` | String | Name of the event organizer |
| `organizerUrl` | String | LinkedIn URL of the organizer's profile or company page |
| `organizerCompany` | Object | Structured organizer company: `{ name, slug }` |
| `address` | Object | Venue address for in-person events: `{ line1, city, region, country }` |
| `attendeesCount` | Integer | Number of LinkedIn members attending |
| `speakers` | Array | Speaker list: each item has `{ name, profileUrl, title }` |
| `description` | String | Full event description |
| `coverImageUrl` | String | URL of the event's cover/banner image |
| `registrationUrl` | String | External registration link (when present) |
| `streamUrl` | String | Livestream URL for virtual/hybrid events |
| `eventCategory` | String | LinkedIn event category tag |
| `scrapedAt` | String | When this record was scraped (ISO 8601, UTC) |

All fields are omit-empty: only fields with actual values appear in the output.

### Sample Output

```json
{
  "eventName": "AI Summit 2026",
  "eventUrl": "https://www.linkedin.com/events/7012345678901234567/",
  "eventId": "7012345678901234567",
  "startDate": "2026-09-15T09:00:00+00:00",
  "endDate": "2026-09-15T17:00:00+00:00",
  "format": "ONLINE",
  "eventType": "VIRTUAL",
  "timezone": "AMERICA_NEW_YORK",
  "organizerName": "Acme Corp",
  "organizerUrl": "https://www.linkedin.com/company/acme/",
  "organizerCompany": { "name": "Acme Corp", "slug": "acme" },
  "attendeesCount": 5200,
  "speakers": [
    { "name": "Jane Doe", "profileUrl": "https://www.linkedin.com/in/janedoe/", "title": "CTO at Acme Corp" }
  ],
  "description": "Annual summit bringing together AI practitioners...",
  "coverImageUrl": "https://media.licdn.com/dms/image/...",
  "registrationUrl": "https://acme.com/ai-summit-register",
  "scrapedAt": "2026-06-22T10:30:00+00:00"
}
```

### Sentinel Records

When the `cookie` is missing or expired, the actor emits a structured sentinel record instead of failing. This keeps Apify's daily health-check tests green:

```json
{
  "_status": "no_data",
  "_reason": "cookie-invalid",
  "_message": "LinkedIn session expired - export fresh cookies and re-run",
  "_help": "This actor needs a valid LinkedIn session cookie...",
  "scrapedAt": "2026-06-22T10:30:00+00:00"
}
```

## Frequently Asked Questions

**Do I need a LinkedIn account?**
Yes, for keyword search you need a LinkedIn session cookie (`li_at`). Direct URL scraping can work without a cookie but may return limited data for non-public events.

**How many events can I scrape?**
Up to 500 events per run. LinkedIn's search API surfaces the most relevant events first.

**Will my account get flagged?**
The scraper uses LinkedIn's official Voyager API with realistic request pacing. Using a residential proxy (configurable in `proxyConfiguration`) reduces risk further.

**What's the difference between searchQuery and eventUrls?**
`searchQuery` searches across all LinkedIn events by keyword. `eventUrls` scrapes specific events you already know about. Both can be used together in one run.

**Why is `attendeesCount` missing for some events?**
LinkedIn only surfaces attendee counts for events with sufficient visibility settings.

**How do I get the full cookie JSON?**
Install a browser extension like EditThisCookie or Cookie-Editor, navigate to LinkedIn, then export all cookies as a JSON array. Paste the entire JSON into the `cookie` field.

**Does this work for private events?**
Private events require the cookie of an account that has access to the event.

**My cookie expired and the actor shows a sentinel record — what do I do?**
Re-export fresh cookies from a logged-in LinkedIn browser session and update the cookie input. LinkedIn sessions typically last several months.

## Technical Notes

- Uses LinkedIn's Voyager API (`/voyager/api/search/blended` and `/voyager/api/search/dash/clusters`) with `resultType->EVENT` filter
- Automatic fallback chain: Voyager API → LinkedIn HTML search page → DuckDuckGo/Bing → LinkedIn discovery feed
- Automatic rate-limit handling with exponential backoff
- Supports both `li_at` plain token and full browser cookie JSON export
- Filter expressions passed as literal strings (not URL-encoded) per Voyager API requirements
- Expired/missing cookie detection returns structured sentinel records instead of actor failure

## Explore the rest of the LinkedIn suite

Need a different LinkedIn surface? Pair this actor with any of the others in the LinkedIn Suite — all published under the same publisher and built to share the same cookie format and output conventions.

| Actor | What it scrapes |
|---|---|
| [LinkedIn Comments Scraper](https://apify.com/crawlerbros/linkedin-comments-scraper) | All comments + reply threads on a post |
| [LinkedIn Company Employees Scraper](https://apify.com/crawlerbros/linkedin-company-employees-scraper) | Employee list for any company (by URN) |
| [LinkedIn Company Info Scraper](https://apify.com/crawlerbros/linkedin-company-info-scraper) | Company About page (size, HQ, industry, specialties) |
| [LinkedIn Company Posts Scraper](https://apify.com/crawlerbros/linkedin-company-posts-scraper) | Posts published from a company page |
| [LinkedIn Hashtag Posts Scraper](https://apify.com/crawlerbros/linkedin-hashtag-posts-scraper) | Posts ranked under a `#hashtag` |
| [LinkedIn Jobs Scraper](https://apify.com/crawlerbros/linkedin-jobs-scraper) | Job listings via the public jobs-guest API |
| [LinkedIn Jobs Scraper Ultra](https://apify.com/crawlerbros/linkedin-jobs-scraper-ultra) | Same as jobs-scraper + full detail enrichment |
| [LinkedIn Learning Courses Scraper](https://apify.com/crawlerbros/linkedin-learning-courses-scraper) | LinkedIn Learning course catalog by keyword |
| [LinkedIn People Search Scraper](https://apify.com/crawlerbros/linkedin-people-search-scraper) | People search with every LinkedIn facet (role, company, school, location, etc.) |
| [LinkedIn Post Reactions Scraper](https://apify.com/crawlerbros/linkedin-post-reactions-scraper) | Reactors on a post (name, headline, reaction type) |
| [LinkedIn Post Scraper](https://apify.com/crawlerbros/linkedin-post-scraper) | Full post (text, media, engagement counts, author) |
| [LinkedIn Post Search Scraper](https://apify.com/crawlerbros/linkedin-post-search-scraper) | Posts matching a keyword (with date/author/network filters) |
| [LinkedIn Profile Posts Scraper](https://apify.com/crawlerbros/linkedin-profile-posts-scraper) | All posts/reposts/articles for one profile |
| [LinkedIn Profile Scraper](https://apify.com/crawlerbros/linkedin-profile-scraper) | Public profile fields (name, headline, positions, education, skills) |
| [LinkedIn Profile Scraper Pro](https://apify.com/crawlerbros/linkedin-profile-scraper-pro) | Profile fields + extras (recommendations, organizations, languages) |
| [LinkedIn Profile Scraper Pro Ultra](https://apify.com/crawlerbros/linkedin-profile-scraper-pro-ultra) | Pro + premium fields (contact info, followers list when allowed) |
| [LinkedIn Profile Scraper Ultra](https://apify.com/crawlerbros/linkedin-profile-scraper-ultra) | Profile + the full upstream dash-120 surface |
| [LinkedIn Profile Search by Name](https://apify.com/crawlerbros/linkedin-profile-search-by-name) | Search profiles by person name (great for matching CSVs of names) |
| [LinkedIn Schools Alumni Scraper](https://apify.com/crawlerbros/linkedin-schools-alumni-scraper) | Alumni list for any LinkedIn school page |
| [LinkedIn Top Content Scraper](https://apify.com/crawlerbros/linkedin-top-content-scraper) | Trending / top-engagement posts by topic |
| [LinkedIn User Activity Scraper](https://apify.com/crawlerbros/linkedin-user-activity-scraper) | Reactions + comments + posts feed for one profile |

All actors share the same `cookie` input format (plain `li_at` OR full cookies JSON array) and the same omit-empty output convention.
<!-- /linkedin-suite -->

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/linkedin-events-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
