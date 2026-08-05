# LinkedIn Profile Scraper Ultra Tutorial: Run This Apify Actor with Python

Scrape detailed LinkedIn profiles - work history, education, skills, languages, certifications, follower counts, and more. Supports URLs, usernames, and bulk input.

This repository shows how to run [LinkedIn Profile Scraper Ultra](https://apify.com/crawlerbros/linkedin-profile-scraper-ultra) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/linkedin-profile-scraper-ultra`
- **Apify Store:** [https://apify.com/crawlerbros/linkedin-profile-scraper-ultra](https://apify.com/crawlerbros/linkedin-profile-scraper-ultra)
- **SEO title:** LinkedIn Profile Scraper Ultra Tutorial: Run This Apify Actor with Python
- **Description:** Scrape detailed LinkedIn profiles - work history, education, skills, languages, certifications, follower counts, and more. Supports URLs, usernames, and bulk input.

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

# LinkedIn Profile Scraper

Extract public data from LinkedIn profiles at scale. Get names, headlines, work experience, education, skills, followers, recent posts and articles — clean, structured, ready to use.

Feed the actor a list of profile URLs (or handles) and it returns one row per profile with everything your workflow needs: enrichment, lead generation, recruiting, research, or competitive analysis.

## Features

- **Fast** — HTTP-only scraping, no browser overhead, profiles returned in seconds
- **Flexible input** — accepts full URLs, `linkedin.com/in/username`, `in/username`, or bare handles
- **Public + authenticated** — works without a cookie for public / influencer profiles, optionally use a cookie for richer data on regular profiles
- **Structured output** — normalized positions, education, articles, and more
- **No nulls** — only fields that were actually populated are included in each row
- **Resilient** — automatic fallbacks (Voyager API → JSON-LD → auth wall meta tags) so you always get something back

## Input

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `profileUrls` | string[] | Yes | LinkedIn profile URLs or usernames to scrape |
| `cookie` | string | No | Your LinkedIn session cookie. Needed for regular (non-public) profiles |

### Supported profile formats

All of these work — the actor normalizes them automatically:

- `https://www.linkedin.com/in/williamhgates`
- `linkedin.com/in/williamhgates`
- `in/williamhgates`
- `williamhgates` (handle only)

### LinkedIn cookie (optional)

Without a cookie, the actor can still extract data for **public / influencer profiles** such as Bill Gates, Satya Nadella, Reid Hoffman, etc. To scrape regular profiles, provide your LinkedIn session cookie in one of two formats:

- **Plain `li_at` value** — copy the value of the `li_at` cookie from your browser's DevTools (Application → Cookies → `https://www.linkedin.com`)
- **Full cookies JSON array** — exported from a browser extension like EditThisCookie or Cookie-Editor. This format gives the best results because the full session is replayed.

Your cookie is stored as a secret and is only used for requests to LinkedIn.

### Example input

```json
{
  "profileUrls": [
    "https://www.linkedin.com/in/williamhgates",
    "satyanadella",
    "in/reidhoffman"
  ],
  "cookie": "AQEDAT..."
}
```

## Output

Each row in the dataset represents one LinkedIn profile. Fields that could not be extracted are omitted — there are no `null` values in the output.

### Profile fields

| Field | Type | Example |
|-------|------|---------|
| `name` | string | `"Bill Gates"` |
| `headline` | string | `"Chair, Gates Foundation and Founder, Breakthrough Energy"` |
| `location` | string | `"Seattle, Washington, United States"` |
| `summary` | string | About / bio text |
| `profileUrl` | string | `"https://www.linkedin.com/in/williamhgates"` |
| `profilePicture` | string | Profile photo URL |
| `currentTitle` | string | Current job title |
| `allTitles` | string[] | All job titles listed on the profile |
| `currentPositions` | object[] | Current work positions |
| `pastPositions` | object[] | Past work positions |
| `education` | object[] | Education history |
| `skills` | string[] | Listed skills |
| `languages` | object[] | Spoken languages with proficiency |
| `certifications` | object[] | Certifications |
| `industryName` | string | Industry |
| `followersCount` | integer | Followers count |
| `recentArticles` | object[] | Recent posts / articles with title, URL, publish date, likes |
| `extractionSource` | string | `"voyager-api"` or `"json-ld"` — tells you how this row was sourced |
| `inputUrl` | string | The URL/handle you supplied |
| `order` | integer | Index of this result in the input list |
| `scrapedAt` | string | ISO-8601 timestamp |

### Position sub-fields

`company`, `title`, `companyUrl`, `startDate`, `endDate`, `location`, `description`

### Education sub-fields

`school`, `schoolUrl`, `degree`, `fieldOfStudy`, `startDate`, `endDate`

### Example output row

```json
{
  "name": "Bill Gates",
  "headline": "Chair, Gates Foundation and Founder, Breakthrough Energy",
  "location": "Seattle, Washington, United States",
  "summary": "Chair of the Gates Foundation. Founder of Breakthrough Energy...",
  "profileUrl": "https://www.linkedin.com/in/williamhgates",
  "profilePicture": "https://media.licdn.com/dms/image/...",
  "currentTitle": "Co-chair",
  "allTitles": ["Co-chair", "Founder", "Co-founder"],
  "currentPositions": [
    {"company": "Gates Foundation", "companyUrl": "https://www.linkedin.com/company/gates-foundation", "startDate": 2000}
  ],
  "education": [
    {"school": "Harvard University", "schoolUrl": "https://www.linkedin.com/school/harvard-university/", "startDate": 1973, "endDate": 1975}
  ],
  "followersCount": 40186465,
  "extractionSource": "json-ld",
  "inputUrl": "williamhgates",
  "order": 0,
  "scrapedAt": "2026-01-15T12:34:56.789000+00:00"
}
```

## Use cases

- **Lead generation & sales prospecting** — enrich LinkedIn URLs with contact context, current role, and recent activity
- **Recruiting** — build candidate lists, verify work history, surface skills
- **Talent research** — track moves, positions, and career history at scale
- **Competitive intelligence** — monitor key people at target companies
- **CRM enrichment** — append profile data to existing contact records
- **Academic / market research** — analyze career trajectories and industry trends

## FAQ

**Do I need a LinkedIn cookie?**
No. Public and influencer profiles work without a cookie. For regular (non-public) profiles you'll need to provide your `li_at` session cookie.

**Which profiles can I scrape without a cookie?**
Any profile with an `og:description` / JSON-LD public preview — typically influencer / creator / celebrity profiles (Bill Gates, Satya Nadella, Reid Hoffman, etc.). Most regular profiles require a cookie.

**What's the difference between the plain `li_at` and the full cookies JSON?**
Both work. The plain `li_at` is simpler to grab. The full cookies array (exported via an extension) replays the full session — `JSESSIONID`, `bcookie`, etc. — and tends to be more reliable for authenticated API calls.

**Will my cookie get banned?**
The actor uses normal request patterns with delays between profiles and rotates proxy sessions. As with any LinkedIn automation, using a throwaway account is safer than a primary account.

**What if a profile is private / not accessible?**
The actor will fall back through multiple extraction strategies (Voyager API → JSON-LD → meta tags). If none work, the profile is logged as failed and the run continues with the rest of your input.

**Can I get email addresses or phone numbers?**
No. LinkedIn does not expose contact info on public profile pages and this actor only extracts data that is visible on the profile page.

**How many profiles can I scrape per run?**
There is no hard limit. For large runs, the actor adds a randomized delay between profiles and rotates the proxy every few profiles to stay below LinkedIn's rate limits.

**Does this scraper work in every country?**
Yes. The actor uses a US proxy by default when available; you can configure a different region via Apify Proxy settings.

**Why are some fields missing from my output row?**
Fields that could not be extracted are omitted entirely rather than returned as `null`. This keeps the dataset clean — if a profile has no certifications, the `certifications` field simply won't appear on that row.

## Limitations

- **Contact info is never returned** — email, phone, and private messages are never exposed by LinkedIn on the profile page
- **Cookie accounts have soft quotas** — LinkedIn may temporarily limit very high-volume scraping. Use a throwaway account for large runs.
- **Private profiles require authentication** — profiles that are not public and not connected to your account will only return the data visible on the auth-wall (typically name and headline)
- **Recent articles** depend on what LinkedIn exposes on the profile — not every profile has posts

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

- [Run this actor on Apify](https://apify.com/crawlerbros/linkedin-profile-scraper-ultra)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
