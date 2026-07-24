# Behance + Dribbble Scraper Tutorial: Run This Apify Actor with Python

Scrape designer profiles from Behance and Dribbble with display name, location, occupation, avatar, follower stats, project/shot counts, work-experience history, social links, and current availability flag.

This repository shows how to run [Behance + Dribbble Scraper](https://apify.com/crawlerbros/behance-dribbble-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/behance-dribbble-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/behance-dribbble-scraper](https://apify.com/crawlerbros/behance-dribbble-scraper)
- **SEO title:** Behance + Dribbble Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape designer profiles from Behance and Dribbble with display name, location, occupation, avatar, follower stats, project/shot counts, work-experience history, social links, and current availability flag.

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

# Behance + Dribbble Scraper

Scrape designer profiles, individual projects/shots, search results, trending lists, and creative-field categories from **Behance** (Adobe-owned, deeper data) and **Dribbble** (lighter data — JS-rendered). Single actor with a `mode` + `platform` switch. No login required.

## Modes

| Mode | What it does |
| --- | --- |
| `designerProfile` | Look up one or more designers by username (or full profile URL) — display name, occupation, location, follower stats, work history, social links, availability flag |
| `projectByUrl` | Fetch a single Behance gallery (`/gallery/<id>/<slug>`) or Dribbble shot (`/shots/<id>-<slug>`) by full URL |
| `projectSearch` | Search projects/shots by free-text query, optionally filtered by Behance creative field, tool, or sort order |
| `trendingProjects` | Pull popular galleries from Behance (`/galleries`) or popular shots from Dribbble (`/shots/popular`, by timeframe) |
| `byCategory` | Browse projects in a Behance creative-field taxonomy (e.g. `ui-ux`, `branding`) or a Dribbble tag |

## What you get

### Designer records (`recordType=designer`)

Common fields (both platforms):

| Field | Description |
| --- | --- |
| `platform` | `behance` or `dribbble` |
| `username` | Designer handle |
| `id` | Same as `username` (or numeric Behance ID) |
| `url` | Public profile URL |
| `displayName` | Display name |
| `bio` | Profile bio (Dribbble) / occupation (Behance) |
| `avatarUrl` | Avatar image URL |
| `scrapedAt` | ISO 8601 UTC timestamp |

Behance-only fields:

| Field | Description |
| --- | --- |
| `firstName`, `lastName` | Given / family name |
| `occupation` | Job title |
| `city`, `country` | Location |
| `bannerImageUrl` | Profile banner image URL |
| `followersCount`, `followingCount` | Follower / following counts |
| `appreciationsCount` | Total appreciations across projects |
| `viewsCount` | Total project views |
| `projectsCount` | Total published projects |
| `webLinks` | Array of `{url, title}` external links |
| `socialLinks` | Array of `{service, url, username}` social profiles |
| `workExperience` | Array of `{company, position, startDate, endDate, currentlyWorking}` |
| `availableForHire` | `true` if the designer flagged availability |
| `workType` | `Freelance` / `FullTime` |
| `isFeaturedFreelancer` | Behance "Featured Freelancer" badge |
| `isCreatorPro` | Behance Creator Pro flag |
| `createdOn` | ISO 8601 account-creation timestamp |

Empty fields are dropped from every record at every depth.

### Project / shot records (`recordType=project` for Behance, `recordType=shot` for Dribbble)

| Field | Description |
| --- | --- |
| `id` | Behance gallery ID / Dribbble shot ID |
| `name` | Project / shot title |
| `slug` | URL slug |
| `url` | Public URL |
| `description` | Project description (or Dribbble shot description) |
| `coverImageUrl` | Cover image URL |
| `appreciationsCount`, `viewsCount`, `commentsCount` | Engagement counts (Behance) |
| `tags` | Free-form keyword tags |
| `creativeFields` | Behance creative-field taxonomy labels |
| `tools` | Tools listed on the project (Photoshop, Figma, …) |
| `owners` | Array of `{username, displayName, url}` |
| `publishedOn` / `modifiedOn` | Timestamps (Behance integer, Dribbble ISO string) |

## Input

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `mode` | Enum | `projectByUrl` | `designerProfile` / `projectByUrl` / `projectSearch` / `trendingProjects` / `byCategory` |
| `platform` | Enum | `behance` | `behance` or `dribbble` (used by every mode except `projectByUrl`, where the URL itself encodes the platform) |
| `usernames` | Array | `["michaelsallit"]` | Handles or full profile URLs (`mode=designerProfile`) |
| `urls` | Array | sample gallery URL | Behance gallery or Dribbble shot URLs (`mode=projectByUrl`) |
| `query` | String | — | Free-text search query (`mode=projectSearch`) |
| `behanceField` | Enum | — | Behance creative-field slug (e.g. `ui-ux`, `logo-design`). Used in `projectSearch` + `byCategory` |
| `behanceTool` | Enum | — | Filter Behance projects by tool (`figma`, `photoshop`, …) |
| `behanceSort` | Enum | — | Behance sort order (`appreciations` / `views` / `comments` / `published_date` / `featured_date`) |
| `dribbbleTimeframe` | Enum | — | Dribbble trending window (`now` / `week` / `month` / `year` / `ever`) |
| `dribbbleTag` | String | — | Dribbble tag slug (`mode=byCategory` on Dribbble) |
| `minFollowers` | Integer | — | Drop profiles below this follower count (`mode=designerProfile`, Behance only) |
| `availableForHireOnly` | Boolean | `false` | Drop Behance profiles without an availability flag |
| `maxItems` | Integer | `50` | Hard cap on emitted records (1-1000) |
| `autoEscalateOnBlock` | Boolean | `true` | Engage Apify Proxy on first 403 block |

### Example input — Behance batch with hire filter

```json
{
  "platform": "behance",
  "usernames": ["alexcoven", "matiasdeangelis", "annaholiday"],
  "availableForHireOnly": true,
  "minFollowers": 1000,
  "maxItems": 100
}
```

### Example input — Dribbble lookup

```json
{
  "platform": "dribbble",
  "usernames": ["aaron", "simple", "MBKHD"]
}
```

## Example output (Behance)

```json
{
  "recordType": "designer",
  "platform": "behance",
  "id": "12345678",
  "username": "alexcoven",
  "url": "https://www.behance.net/alexcoven",
  "displayName": "Alex Covenn",
  "occupation": "Award Winning Logo Designer",
  "avatarUrl": "https://pps.services.adobe.com/api/profile/image/.../276",
  "followersCount": 1500,
  "followingCount": 200,
  "appreciationsCount": 5000,
  "viewsCount": 120000,
  "projectsCount": 12,
  "availableForHire": true,
  "workType": "Freelance",
  "webLinks": [
    { "url": "https://x.com/user", "title": "Twitter" }
  ],
  "workExperience": [
    { "company": "Acme", "position": "Designer", "startDate": "2020", "currentlyWorking": true }
  ],
  "scrapedAt": "2026-05-06T07:01:18Z"
}
```

## Use cases

- **Recruiting / staffing** — Build a designer-talent database with availability + skill tags.
- **Lead generation** — Identify designers with N+ followers who are open to freelance work.
- **Competitive research** — Track top designers in a niche (logo, illustration, UX, …).
- **CRM enrichment** — Augment designer leads with public Behance/Dribbble stats.
- **Industry analysis** — Snapshot the designer-platform follower / project ecosystems.

## FAQ

**Do I need an Adobe / Dribbble account?**
No. Both platforms serve their public profile pages anonymously.

**Why does Behance return more data than Dribbble?**
Behance's profile pages embed a server-side-rendered JSON blob (`beconfig-store_state`) with full structured data — stats, work history, social links, availability flag. Dribbble's pages are JS-rendered; without executing JS we can only extract OG meta tags (display name, bio, avatar). For richer Dribbble data, we'd need Playwright (heavier to run); this v1 keeps the actor lightweight.

**Why TLS impersonation?**
Both Behance (Adobe Edge CDN) and Dribbble (Cloudflare) fingerprint the TLS handshake. We use `curl_cffi` Chrome-131 impersonation so the actor passes through both WAFs without proxy or session warmup.

**What if a username doesn't exist?**
The actor logs a warning and continues to the next username. Final status message lists how many records were emitted.

**How current is the data?**
Live — every run hits the platform at request time. Schedule the actor for daily / weekly refreshes to track follower growth.

**Do I need a proxy?**
No. Both platforms accept datacenter IPs as long as the TLS fingerprint is real (which Chrome-131 impersonation provides).

**What if the platform does block me?**
The actor has built-in auto-escalation: on the first HTTP 403 / anti-bot block it lazily engages Apify Proxy (datacenter group first, residential as a second-stage fallback) and retries the failed URL transparently. All subsequent fetches in the same run continue through the proxied session. To disable, set `autoEscalateOnBlock=false`. To force a specific group set, populate `proxyGroups`.

## Limitations

- Dribbble profiles return only display name, bio, and avatar (the rest of the page is JS-rendered).
- Behance projects (the actual portfolio items) aren't included in this version — only the profile metadata.
- Both platforms periodically update their HTML; if a future redesign breaks `beconfig-store_state`, we'll bump the actor.
- TLS-fingerprint maintenance: `curl_cffi` updates Chrome impersonation profiles regularly; we follow upstream.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/behance-dribbble-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
