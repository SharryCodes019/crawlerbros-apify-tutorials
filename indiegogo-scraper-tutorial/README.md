# Indiegogo Scraper Tutorial: Run This Apify Actor with Python

Scrape Indiegogo crowdfunding campaigns with funding goal, raised amount, backers, currency, deadline, creator, category, tags, image, and discovery feeds (trending, ending soon, by category, search).

This repository shows how to run [Indiegogo Scraper](https://apify.com/crawlerbros/indiegogo-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/indiegogo-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/indiegogo-scraper](https://apify.com/crawlerbros/indiegogo-scraper)
- **SEO title:** Indiegogo Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Indiegogo crowdfunding campaigns with funding goal, raised amount, backers, currency, deadline, creator, category, tags, image, and discovery feeds (trending, ending soon, by category, search).

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

# Indiegogo Scraper

Scrape Indiegogo crowdfunding campaigns at scale — discover trending or ending-soon campaigns, browse by category, search by keyword, or fetch one or more campaigns by URL/slug. Returns funding goal, raised amount, backers, currency, deadline, creator, category, tags, image, and the full project story.

No login required. No cookies. Works out of the box.

## Use cases

- Track competitor crowdfunding campaigns in your niche
- Build leaderboards of the most-funded campaigns by category
- Monitor new launches in tech, design, film, music, and more
- Power crowdfunding analytics dashboards
- Build email outreach lists of founders raising on Indiegogo
- Study what makes a campaign succeed (goal vs. raised vs. backers)

## Modes

| Mode | What it does |
|---|---|
| `discoverTrending` | Popular campaigns right now (default) |
| `discoverEndingSoon` | Campaigns about to close — fund-now urgency |
| `discoverNewest` | Newest campaigns |
| `discoverMostFunded` | Highest raised amount |
| `discoverCategory` | Browse a category (Tech, Creative, Community, Gaming) |
| `searchCampaigns` | Free-text keyword search |
| `byCampaign` | One or more campaign slugs (`witchcraft-the-lanterne-of-light`) |
| `byUrl` | One or more full Indiegogo campaign URLs |

## Input

| Field | Type | Description |
|---|---|---|
| `mode` | enum | What to scrape (see modes table). |
| `query` | string | Search keyword (mode=searchCampaigns). |
| `category` | enum | `tech`, `creative`, `community`, or `gaming`. |
| `subCategory` | enum | Specific tag (audio, film, drones, gaming, etc.). |
| `sortBy` | enum | `trending`, `newest`, `ending_soon`, `most_funded`. |
| `projectType` | enum | `any`, `campaign` (default — live crowdfunding), `marketplace`. |
| `status` | enum | `any`, `live`, `ended`, `in_demand` (post-campaign sales). |
| `slugs` | list | Campaign slugs (mode=byCampaign). |
| `urls` | list | Full Indiegogo URLs (mode=byUrl). |
| `minBackers` | int | Drop campaigns with fewer backers than this. |
| `minRaised` | int | Drop campaigns that raised less than this (native currency). |
| `fundedOnly` | bool | Drop campaigns that haven't reached their goal. |
| `maxItems` | int | Hard cap on emitted records (1-1000). |
| `autoEscalateOnBlock` | bool | Auto-engage Apify Proxy on Cloudflare 403. |

## Example input

```json
{
  "mode": "discoverTrending",
  "category": "tech",
  "maxItems": 10
}
```

```json
{
  "mode": "searchCampaigns",
  "query": "headphones",
  "sortBy": "most_funded",
  "fundedOnly": true,
  "maxItems": 50
}
```

```json
{
  "mode": "byUrl",
  "urls": [
    "https://www.indiegogo.com/projects/witchcraft-the-lanterne-of-light"
  ]
}
```

## Output

Each record is an Indiegogo campaign with these fields (`null`/empty values are omitted):

```json
{
  "platform": "indiegogo",
  "id": 244299,
  "slug": "Witchcraft-The-Lanterne-of-Light",
  "name": "Witchcraft: The Lanterne of Light",
  "shortDescription": "When a paranormal crew discovers a cursed lantern...",
  "url": "https://www.indiegogo.com/en/projects/andrewpierson-37875854/witchcraft-the-lanterne-of-light",
  "imageUrl": "https://cdn.images.indiegogo.com/...",
  "campaignGoal": 5000,
  "fundsGathered": 14230.0,
  "backersCount": 16,
  "followersCount": 54,
  "currencySymbol": "$",
  "currencyCode": "USD",
  "campaignStart": "2026-05-01T14:00:00Z",
  "campaignEnd": "2026-06-16T13:00:00Z",
  "publishedDate": "2026-04-24T03:55:18.137Z",
  "campaignDay": 8,
  "fundedAt": "2026-05-01T21:10:46.083Z",
  "phase": 10,
  "phaseLabel": "live",
  "categoryId": 56,
  "categoryName": "Film",
  "tags": ["horror", "indie", "film"],
  "creator": {
    "id": 1821148,
    "name": "Andrew Pierson",
    "urlName": "andrewpierson-37875854",
    "url": "https://www.indiegogo.com/creators/andrewpierson-37875854"
  },
  "creatorName": "Andrew Pierson",
  "creatorUrlName": "andrewpierson-37875854",
  "stretchGoals": [
    {"goalAmount": 10000, "title": "Goal #1: Production starts"}
  ],
  "tabUrls": {
    "project": "https://www.indiegogo.com/en/projects/.../witchcraft...",
    "rewards": "https://www.indiegogo.com/en/projects/.../rewards",
    "comments": "https://www.indiegogo.com/en/projects/.../comments",
    "updates": "https://www.indiegogo.com/en/projects/.../updates"
  },
  "storyHtml": "<div><b>WITCHCRAFT: THE LANTERNE OF LIGHT...",
  "storyText": "WITCHCRAFT: THE LANTERNE OF LIGHT A Feature Film...",
  "scrapedAt": "2026-05-09T20:51:08.123456+00:00"
}
```

Search/discover cards include the same core fields. Detail records (mode=`byUrl` / `byCampaign`) additionally include `storyHtml` / `storyText` and `tabUrls`.

## FAQs

**Q: Do I need cookies, an API key, or a proxy?**
A: No. The actor works directly from datacenter IPs via TLS impersonation (curl_cffi Chrome 131). If Indiegogo's Cloudflare blocks your run, the actor automatically escalates to Apify Proxy (RESIDENTIAL on second block).

**Q: Why don't I see updates / comments?**
A: Indiegogo loads its Updates and Comments tabs via XHR after the campaign page renders, so neither the SSR HTML nor a public API exposes them. The actor surfaces the tab URLs (`tabUrls.updates`, `tabUrls.comments`) so you can navigate to them in a browser, but it does not paginate update/comment content. Story HTML, goal, raised, backers, dates, creator, category and stretch-goals are all returned.

**Q: What does "InDemand" mean?**
A: After a campaign closes, the creator can re-list the product on Indiegogo's InDemand marketplace for ongoing pre-orders. We expose this via `status=in_demand` and `phase=40`.

**Q: Why does `currencyCode` sometimes differ from `currencySymbol`?**
A: Some campaigns are listed in currencies whose symbol overlaps with USD (`$` for USD, AUD, CAD, HKD). The numeric `currencyCode` is the authoritative ISO code.

**Q: How many results per page?**
A: Indiegogo's search/discover endpoint returns 12-24 cards per page; the actor paginates automatically up to `maxItems`.

**Q: Can I filter by language / country?**
A: Indiegogo does not expose locale-based filters in search. The actor ships English (`/en/projects/search`) by default. Add `language` / `country` to your input to request — currently the upstream API doesn't support it.

**Q: Why does my run sometimes return zero records?**
A: The most likely cause is an over-restrictive filter combo (e.g., `minBackers=10000 + minRaised=1000000 + fundedOnly=true`). Try with fewer filters first, then narrow.

## Limitations

- **Updates / comments are not extracted** (XHR-rendered, no SSR data; see FAQ above).
- **Campaign rewards** are summarised on the detail page but not paginated separately — the actor returns whatever is in the SSR.
- **Currency conversion** is not performed — `fundsGathered` is in the campaign's native currency.
- **Cloudflare blocks** are auto-escalated to Apify Proxy; if RESIDENTIAL is also blocked the run will surface a typed error record per failed URL.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/indiegogo-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
