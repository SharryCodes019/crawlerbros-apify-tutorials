# LinkedIn Schools Alumni Scraper Tutorial: Run This Apify Actor with Python

Find alumni from any university or school on LinkedIn. Enter a school name or LinkedIn school URL to get alumni profiles with name, headline, current company, location, and more.

This repository shows how to run [LinkedIn Schools Alumni Scraper](https://apify.com/crawlerbros/linkedin-schools-alumni-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/linkedin-schools-alumni-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/linkedin-schools-alumni-scraper](https://apify.com/crawlerbros/linkedin-schools-alumni-scraper)
- **SEO title:** LinkedIn Schools Alumni Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Find alumni from any university or school on LinkedIn. Enter a school name or LinkedIn school URL to get alumni profiles with name, headline, current company, location, and more.

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

# LinkedIn Schools Alumni Scraper

Find alumni from any university or school on LinkedIn. Enter a school name or LinkedIn school URL and get alumni profiles with name, headline, location, connection degree, and profile picture.

## What it does

This actor uses LinkedIn's authenticated Voyager API to search for alumni of specific schools. It resolves school names or URLs to LinkedIn's internal school IDs, then uses the `currentSchool` search filter to retrieve matching alumni profiles.

## Why use it?

- **Recruitment**: Find graduates from specific universities for targeted outreach
- **Research**: Map alumni networks and career paths from top schools
- **Lead generation**: Identify alumni of schools matching your customer profile
- **Networking**: Find fellow alumni from your own school

---

## Input

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `schoolUrls` | array | One of these required | LinkedIn school page URLs, e.g. `https://www.linkedin.com/school/mit/` |
| `schoolNames` | array | One of these required | Plain school names, e.g. `"MIT"`, `"Harvard University"` |
| `cookie` | string | Yes | LinkedIn session cookie (li_at value or full JSON array) |
| `maxAlumniPerSchool` | integer | No | Max alumni per school. Default: 100, Max: 1000 |
| `fieldOfStudy` | string | No | Filter by field of study, e.g. `"Computer Science"`, `"MBA"` |
| `graduationYear` | string | No | Filter by graduation year, e.g. `"2020"` |
| `connectionDegree` | string | No | Filter by connection: `F` (1st), `S` (2nd), `O` (3rd+) |
| `proxyConfiguration` | object | No | Apify proxy configuration |

### Getting your LinkedIn cookie

1. Log in to LinkedIn in your browser
2. Open Developer Tools (F12) → Application → Cookies → linkedin.com
3. Copy the value of `li_at`

Or use a browser extension like **Cookie-Editor** or **EditThisCookie** to export all cookies as a JSON array and paste the full JSON into the cookie field.

### Example input

```json
{
  "schoolUrls": ["https://www.linkedin.com/school/mit/"],
  "cookie": "AQEDATVc5uM...",
  "maxAlumniPerSchool": 100,
  "fieldOfStudy": "Computer Science"
}
```

---

## Output

Each alumni profile is stored as one record in the dataset.

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Alumni's full name |
| `profileUrl` | string | LinkedIn profile URL |
| `headline` | string | Profile headline (job title / company) |
| `location` | string | Location shown on LinkedIn |
| `connectionDegree` | string | Connection degree: 1st, 2nd, 3rd+ |
| `profilePicture` | string | Profile photo CDN URL |
| `schoolName` | string | School that produced this result |
| `schoolUrl` | string | LinkedIn school page URL |
| `scrapedAt` | string | ISO 8601 UTC timestamp |

### Example output record

```json
{
  "name": "Jane Doe",
  "profileUrl": "https://www.linkedin.com/in/janedoe/",
  "headline": "Software Engineer at Google",
  "location": "San Francisco Bay Area",
  "connectionDegree": "2nd",
  "profilePicture": "https://media.licdn.com/dms/image/...",
  "schoolName": "Massachusetts Institute of Technology",
  "schoolUrl": "https://www.linkedin.com/school/mit/",
  "scrapedAt": "2026-06-12T10:00:00+00:00"
}
```

---

## Notes on LinkedIn's limits

LinkedIn limits the number of search results visible per session. Typically:
- Up to **1,000 alumni** are surfaced per school depending on your LinkedIn plan
- Results depend on your network connections and LinkedIn's privacy settings
- Alumni who have set their profile to private will not appear

## Frequently Asked Questions

**Do I need a LinkedIn Premium account?**
No — a standard LinkedIn account works. However, Premium accounts may see more results.

**Why do I need to provide a cookie?**
LinkedIn's alumni search is only accessible to authenticated users. The cookie identifies your LinkedIn session and allows the actor to make authenticated API requests on your behalf.

**Is the cookie safe to provide?**
The cookie is marked as `isSecret` and is not stored in run logs. However, sharing your session cookie gives the actor full access to your LinkedIn session. Use a dedicated LinkedIn account if you are concerned.

**How many alumni can I scrape?**
LinkedIn surfaces between 200 and 1,000 alumni per school for most queries. Setting `maxAlumniPerSchool` higher than LinkedIn's visible limit will simply return all available results.

**Can I filter by graduation year?**
Yes — use the `graduationYear` field (e.g. `"2020"`). This adds the year as a keyword to the search, which LinkedIn uses to filter results.

**Can I scrape multiple schools at once?**
Yes — provide multiple URLs in `schoolUrls` and/or multiple names in `schoolNames`. Each school is scraped sequentially.

**Why are some fields missing from certain profiles?**
LinkedIn only returns fields that are publicly visible or visible to your network tier. Profiles with privacy settings may not expose headline, location, or profile picture.

**What happens if a school name cannot be resolved?**
The actor will attempt to look up the school ID using LinkedIn's typeahead API. If the ID cannot be found, it will still search using the school name as a keyword, which may return fewer or less precise results.

**Can I use a proxy?**
Yes — configure the `proxyConfiguration` field. Residential proxies are recommended for best results when scraping at scale.

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

- [Run this actor on Apify](https://apify.com/crawlerbros/linkedin-schools-alumni-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
