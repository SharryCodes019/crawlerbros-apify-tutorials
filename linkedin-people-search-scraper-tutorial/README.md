# LinkedIn People Search Scraper Tutorial: Run This Apify Actor with Python

Search LinkedIn for people by name, title, or keyword. Filter by location, company, school, or connection degree. Returns profile URLs, headlines, and contact details.

This repository shows how to run [LinkedIn People Search Scraper](https://apify.com/crawlerbros/linkedin-people-search-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/linkedin-people-search-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/linkedin-people-search-scraper](https://apify.com/crawlerbros/linkedin-people-search-scraper)
- **SEO title:** LinkedIn People Search Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Search LinkedIn for people by name, title, or keyword. Filter by location, company, school, or connection degree. Returns profile URLs, headlines, and contact details.

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

# LinkedIn People Search Scraper

Search LinkedIn for people by name, job title, keyword, or any combination. Filter results by location, company, school, and connection degree. Returns structured profile data including name, headline, location, connection degree, profile URL, and profile picture.

## What It Does

This actor calls LinkedIn's Voyager search API (the same API your browser uses) with your session cookie to return people search results. It supports pagination to retrieve up to 100 profiles per run.

**Key capabilities:**
- Search by any keyword: name, title, skills, company, industry
- Filter by connection degree (1st, 2nd, 3rd+)
- Append location, company, or school terms to refine results
- Returns profile URLs, headlines, locations, connection degree, and profile pictures
- Deduplicates results across pages

---

## Input

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `searchQuery` | String | Yes | Keywords to search for. E.g. `"software engineer"`, `"John Smith"`, `"product manager Google"` |
| `cookie` | String | Yes | Your LinkedIn session cookie. See [Cookie Setup](#cookie-setup) below |
| `location` | String | No | Location to filter by. E.g. `"San Francisco Bay Area"`, `"United Kingdom"` |
| `currentCompany` | String | No | Filter by current company name. E.g. `"Google"`, `"Microsoft"` |
| `pastCompany` | String | No | Filter by past company name |
| `school` | String | No | Filter by school/university. E.g. `"Stanford University"`, `"MIT"` |
| `connectionDegree` | Select | No | Filter by connection degree: Any / 1st degree / 2nd degree / 3rd+ degree |
| `maxResults` | Number | No | Maximum number of profiles to return (1–100, default: 25) |
| `proxyConfiguration` | Object | No | Apify proxy configuration (optional) |

---

## Output

Each profile in the dataset contains:

| Field | Type | Description |
|-------|------|-------------|
| `name` | String | Full name of the person |
| `headline` | String | Professional headline / job title |
| `location` | String | Location shown on LinkedIn profile |
| `connectionDegree` | String | Connection degree to your account (`"1st"`, `"2nd"`, `"3rd+"`) |
| `profileUrl` | String | Full LinkedIn profile URL |
| `profilePicture` | String | Profile picture URL (when available) |
| `mutualConnections` | String | Mutual connections text (e.g. `"5 mutual connections"`) |
| `scrapedAt` | String | ISO 8601 UTC timestamp of when the record was scraped |

### Example Output

```json
[
  {
    "name": "Alice Johnson",
    "headline": "Senior Software Engineer at Stripe",
    "location": "San Francisco Bay Area",
    "connectionDegree": "2nd",
    "profileUrl": "https://www.linkedin.com/in/alicejohnson/",
    "profilePicture": "https://media.licdn.com/dms/image/C4E03AQ.../200_200/photo.jpg",
    "mutualConnections": "12 mutual connections",
    "scrapedAt": "2026-06-08T12:00:00+00:00"
  },
  {
    "name": "Bob Williams",
    "headline": "Product Manager at Notion",
    "location": "New York City Metropolitan Area",
    "connectionDegree": "3rd+",
    "profileUrl": "https://www.linkedin.com/in/bobwilliams/",
    "scrapedAt": "2026-06-08T12:00:01+00:00"
  }
]
```

---

## Cookie Setup

LinkedIn requires authentication for search. The actor uses your existing LinkedIn session cookie — **your credentials are never sent anywhere except LinkedIn's own servers**.

### Method 1: Copy the `li_at` token (simplest)

1. Open [linkedin.com](https://www.linkedin.com) and sign in
2. Open **DevTools** (F12 or Cmd+Option+I)
3. Go to **Application** → **Cookies** → `https://www.linkedin.com`
4. Find the cookie named `li_at`
5. Copy the **Value** column
6. Paste it into the `cookie` field

### Method 2: Export full cookie JSON (more reliable)

1. Install the [EditThisCookie](https://www.editthiscookie.com/) browser extension
2. Visit [linkedin.com](https://www.linkedin.com) while signed in
3. Click the extension icon → **Export** (copies a JSON array to clipboard)
4. Paste the full JSON array into the `cookie` field

The actor accepts either format automatically.

> **Important:** Your cookie is a sensitive credential. Use `isSecret: true` in Apify UI (the field is already marked secret in this actor's schema). Never share your `li_at` token.

---

## Filter Combinations with Examples

### Search by keyword + location
```json
{
  "searchQuery": "data scientist",
  "cookie": "<your cookie>",
  "location": "London"
}
```

### Find 1st-degree connections at a specific company
```json
{
  "searchQuery": "product manager",
  "cookie": "<your cookie>",
  "currentCompany": "Airbnb",
  "connectionDegree": "F"
}
```

### Find alumni from a school
```json
{
  "searchQuery": "software engineer",
  "cookie": "<your cookie>",
  "school": "MIT"
}
```

### Narrow 2nd-degree connections by location and company
```json
{
  "searchQuery": "VP Engineering",
  "cookie": "<your cookie>",
  "location": "New York",
  "currentCompany": "Goldman Sachs",
  "connectionDegree": "S"
}
```

### Search for a specific person
```json
{
  "searchQuery": "John Smith product manager",
  "cookie": "<your cookie>",
  "maxResults": 10
}
```

---

## Notes and Limitations

- **Authentication required:** LinkedIn search is only accessible to logged-in users. The actor requires a valid `li_at` session cookie.
- **Results vary by account:** LinkedIn personalises search results based on your network, location, and account type. Identical searches from different accounts may return different results.
- **Connection degree filter:** Filtering by connection degree (1st, 2nd, 3rd+) uses LinkedIn's native `network` filter and respects your actual network graph.
- **Rate limiting:** The actor paces requests with 2–5 second delays to avoid triggering LinkedIn's rate limits. For large result sets (100 profiles), expect runs of 3–5 minutes.
- **Maximum results:** LinkedIn's Voyager search API supports a maximum of 1,000 results per query (100 pages × 10 per page). This actor is capped at 100 for reliability.
- **Cookie expiry:** LinkedIn session cookies typically expire after 1 year, but LinkedIn may invalidate them sooner. If you get an auth error, refresh your cookie.
- **Location / company filters:** These terms are appended to the keyword search because LinkedIn's blended search API does not accept separate structured filter parameters for them (unlike the dedicated `/people` search endpoint which requires entity IDs). Results are highly accurate for well-known company names and locations.

---

## FAQs

**Q: Does this store or share my LinkedIn cookie?**
A: No. Your cookie is used only to authenticate requests to LinkedIn's API during the run. It is stored in Apify's encrypted input store and is marked as a secret field (not shown in logs).

**Q: Will LinkedIn detect or block this scraper?**
A: The actor uses LinkedIn's official Voyager API (the same endpoints your browser uses) and paces requests to avoid rate limits. However, very aggressive usage from a single account may trigger LinkedIn's abuse detection. Use reasonable `maxResults` values and don't run multiple concurrent instances on the same account.

**Q: Can I scrape profiles without a cookie?**
A: No. LinkedIn's people search requires authentication. Without a valid session cookie, all search API calls return 401.

**Q: Why is `connectionDegree` empty for some profiles?**
A: LinkedIn only shows connection degree for profiles that appear in your network graph. Profiles outside your network (e.g. some 3rd-degree connections) may not have a degree badge.

**Q: Why do some profiles not have a profile picture?**
A: LinkedIn users can set their profile picture to be visible only to connections. The actor extracts the picture URL when it is returned by the search API; it does not attempt to access pictures restricted to connections.

**Q: Can I search for people at a specific company?**
A: Yes — use the `currentCompany` filter for current employees or `pastCompany` for alumni. For best results, use the exact company name as it appears on LinkedIn.

**Q: What is the difference between connection degree values?**
A: `F` = 1st degree (direct connections), `S` = 2nd degree (connections of connections), `O` = 3rd degree and beyond. Leave blank to search all degrees.

---

## Data Source

This actor uses LinkedIn's Voyager API — the private JSON API that powers LinkedIn's web application. It is the same data source your browser accesses when you perform a people search on linkedin.com.

## Explore the rest of the LinkedIn suite

Need a different LinkedIn surface? Pair this actor with any of the others in the LinkedIn Suite — all published under the same publisher and built to share the same cookie format and output conventions.

| Actor | What it scrapes |
|---|---|
| [LinkedIn Comments Scraper](https://apify.com/crawlerbros/linkedin-comments-scraper) | All comments + reply threads on a post |
| [LinkedIn Company Employees Scraper](https://apify.com/crawlerbros/linkedin-company-employees-scraper) | Employee list for any company (by URN) |
| [LinkedIn Company Info Scraper](https://apify.com/crawlerbros/linkedin-company-info-scraper) | Company About page (size, HQ, industry, specialties) |
| [LinkedIn Company Posts Scraper](https://apify.com/crawlerbros/linkedin-company-posts-scraper) | Posts published from a company page |
| [LinkedIn Events Scraper](https://apify.com/crawlerbros/linkedin-events-scraper) | Events by keyword/URL with full event detail |
| [LinkedIn Hashtag Posts Scraper](https://apify.com/crawlerbros/linkedin-hashtag-posts-scraper) | Posts ranked under a `#hashtag` |
| [LinkedIn Jobs Scraper](https://apify.com/crawlerbros/linkedin-jobs-scraper) | Job listings via the public jobs-guest API |
| [LinkedIn Jobs Scraper Ultra](https://apify.com/crawlerbros/linkedin-jobs-scraper-ultra) | Same as jobs-scraper + full detail enrichment |
| [LinkedIn Learning Courses Scraper](https://apify.com/crawlerbros/linkedin-learning-courses-scraper) | LinkedIn Learning course catalog by keyword |
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

- [Run this actor on Apify](https://apify.com/crawlerbros/linkedin-people-search-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
