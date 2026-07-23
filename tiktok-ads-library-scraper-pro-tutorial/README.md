# TikTok Ads Library Scraper Pro Tutorial: Run This Apify Actor with Python

Scrape TikTok's public ad transparency library by query, advertiser, region, and date range. Pulls ad text, video URL, advertiser, impression buckets, and per-region/age/gender targeting. Pro filters: regionFilter, industryFilter, minImpressions, daysActive derived field.

This repository shows how to run [TikTok Ads Library Scraper Pro](https://apify.com/crawlerbros/tiktok-ads-library-scraper-pro) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tiktok-ads-library-scraper-pro`
- **Apify Store:** [https://apify.com/crawlerbros/tiktok-ads-library-scraper-pro](https://apify.com/crawlerbros/tiktok-ads-library-scraper-pro)
- **SEO title:** TikTok Ads Library Scraper Pro Tutorial: Run This Apify Actor with Python
- **Description:** Scrape TikTok's public ad transparency library by query, advertiser, region, and date range. Pulls ad text, video URL, advertiser, impression buckets, and per-region/age/gender targeting. Pro filters: regionFilter, industryFilter, minImpressions, daysActive derived field.

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

# TikTok Ads Library Scraper Pro

Search and extract ads from TikTok's public Ads Transparency Library at ads.tiktok.com/transparency. Supports keyword search, advertiser name search, and direct ad ID lookup. Filters by EU/EEA country, region, industry, language, call-to-action, date range, and impression count. Returns ad metadata, creative media URLs, targeting breakdowns, and compliance status. No TikTok account, login, or cookies are required — the transparency library is publicly accessible.

## What this actor does

- Searches TikTok's official DSA transparency database by keyword, advertiser name, or direct ad ID
- Filters results by region (EU/EEA, UK, Switzerland, Turkey), industry, language, CTA text, and impression range
- Returns full advertiser identity including registered business name, country, and linked TikTok account
- Provides per-region targeting breakdowns: impressions, age buckets, and gender selection
- Includes compliance and audit status fields (`approved`, `rejected`, `in_review`, `removed`)
- Supports quick search mode (listing card data only) and full detail mode (per-ad detail page with complete targeting)
- Derives calculated fields: `daysActive` and `avgImpressionsPerDay`
- Empty fields are omitted

## Output per ad

- `adId` — TikTok's internal ad ID
- `adTitle` — ad headline or creative title
- `brandName` — brand name as shown on the ad card
- `advertiserName` — advertiser display name
- `advertiserId` — TikTok advertiser business ID
- `industry` — advertiser industry classification
- `countryCode` — advertiser's registered country code
- `impressionRange` — TikTok's impression bucket (e.g. `10K-100K`, `1M-10M`)
- `startDate` — first-shown date (`YYYY-MM-DD`)
- `endDate` — last-shown date (`YYYY-MM-DD`)
- `region` — region(s) where the ad was shown
- `language` — detected language(s) of the ad creative
- `adLinkUrl` — landing page URL the ad links to
- `callToAction` — CTA button label (e.g. `Shop Now`, `Learn More`)
- `creativeType` — `video` or `image`
- `mediaType` — granular format: `single_video`, `carousel`, `spark_ad`, `image`
- `mediaUrl` — direct URL to the primary video or image creative
- `thumbnailUrl` — cover/thumbnail image URL
- `adText` — ad copy text
- `reportDate` — date this ad was reported to the transparency database
- `scrapedAt` — ISO 8601 timestamp when the row was collected

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `query` | string | — | Free-text keyword search — company name, domain, or ad text. Leave empty to browse all ads. |
| `adIds` | array of strings | — | Direct list of TikTok ad IDs. Bypasses search and fetches each ad directly. |
| `advertiserName` | string | — | Filter by advertiser name (substring match). |
| `region` | string | `"all"` | EU/EEA ad region code. Options: `all`, `AT`, `BE`, `BG`, `CH`, `CY`, `CZ`, `DE`, `DK`, `EE`, `ES`, `FI`, `FR`, `GB`, `GR`, `HR`, `HU`, `IE`, `IS`, `IT`, `LI`, `LT`, `LU`, `LV`, `MT`, `NL`, `NO`, `PL`, `PT`, `RO`, `SE`, `SI`, `SK`, `TR`. |
| `dateFrom` | string | 1 year ago | Earliest ad start date (`YYYY-MM-DD`). |
| `dateTo` | string | today | Latest ad end date (`YYYY-MM-DD`). |
| `sortBy` | string | `"last_shown_date,desc"` | Sort order: `last_shown_date`, `create_time`, or `impression` combined with `asc` or `desc`. |
| `quickSearch` | boolean | `true` | When true, skip per-ad detail fetches (faster). When false, enriches each row with full targeting breakdowns. |
| `minImpressions` | integer | — | Drop ads below this many impressions. |
| `maxImpressions` | integer | — | Drop ads above this many impressions. |
| `language` | string | — | Filter ads by detected language code (e.g. `en`, `de`, `fr`). |
| `industry` | string | — | Filter ads by industry substring. |
| `proxyConfiguration` | object | Apify proxy | Proxy settings for routing requests. |

### Example: Technology keyword search

```json
{
  "query": "technology",
  "quickSearch": true,
  "region": "all"
}
```

### Example: Filter by advertiser name and region

```json
{
  "advertiserName": "Temu",
  "region": "DE",
  "quickSearch": false
}
```

### Example: Direct ad ID lookup

```json
{
  "adIds": ["1863424159438849", "1863615078571137"]
}
```

### Example: Surgical filter — health ads with high impressions

```json
{
  "query": "supplements",
  "region": "all",
  "industry": "health",
  "language": "en",
  "minImpressions": 50000,
  "quickSearch": false
}
```

## Use cases

- **Competitive intelligence** — track every ad your competitors run across Europe, including their targeting strategy and impression volumes
- **Creative research** — download competitor creative assets, study CTA choices, formats, and language strategies across markets
- **Compliance monitoring** — audit rejected or in-review ads, flag DSA compliance issues, and track audit-reason codes for regulatory research
- **Market sizing** — aggregate impression buckets per industry, region, and age group to estimate advertising spend in a vertical
- **Sponsorship and agency mapping** — identify which agencies place ads on behalf of which brands using the advertiser sponsor field
- **Influencer due diligence** — inspect which brands run paid amplification on a creator's content via the linked TikTok account field

## FAQ

**Q: Which regions are covered?**  
A: The TikTok Ads Transparency Library is a DSA (EU Digital Services Act) mandate. Coverage includes all EU/EEA countries plus the UK, Switzerland, and Turkey. Non-EU regions are not available in this database.

**Q: Do I need a proxy?**  
A: Proxy rotation is enabled by default because TikTok rate-limits cloud datacenter IPs. If you encounter rate limiting, reduce the request rate or retry after the cooldown window.

**Q: What is the difference between quickSearch true and false?**  
A: `quickSearch: true` returns listing card data only — faster (one request per 50 ads) but omits targeting breakdowns, advertiser registry details, and audience flags. `quickSearch: false` makes one additional detail request per ad for the complete dataset.

**Q: How fresh is the data?**  
A: TikTok's transparency library refreshes within minutes of an ad being shown. The `startDate` and `endDate` fields reflect the current display window.

**Q: Why do some ads have no media URL?**  
A: Ads with `auditStatus: rejected` or `removed` are still listed in the transparency database but have their creative assets stripped. Those rows still contain advertiser identity and targeting metadata.

**Q: Can I search for spark ads?**  
A: Yes. Spark ads (organic-style promoted posts) appear in the library with `mediaType: spark_ad`. Search by keyword or advertiser name to find them.

**Q: What impression ranges does TikTok report?**  
A: TikTok uses bucketed ranges such as `<1K`, `1K-10K`, `10K-100K`, `100K-1M`, and `1M-10M`. Exact counts are not published for all ads.

**Q: Can I filter to a specific date range?**  
A: Yes. Use `dateFrom` and `dateTo` (both in `YYYY-MM-DD` format) to narrow results to ads active within that window.

## Related TikTok Scrapers

Build a complete TikTok data pipeline with our full suite:

| Scraper | URL |
|---|---|
| TikTok Post Scraper | https://apify.com/crawlerbros/tiktok-post-scraper |
| TikTok Profile Scraper | https://apify.com/crawlerbros/tiktok-profile-scraper |
| TikTok Comments Scraper | https://apify.com/crawlerbros/tiktok-comments-scraper |
| TikTok Search Scraper | https://apify.com/crawlerbros/tiktok-search-scraper |
| TikTok Hashtag Scraper | https://apify.com/crawlerbros/tiktok-hashtag-scraper |
| TikTok Music Scraper | https://apify.com/crawlerbros/tiktok-music-scraper |
| TikTok Transcript Scraper | https://apify.com/crawlerbros/tiktok-transcript-scraper |
| TikTok Followers Scraper | https://apify.com/crawlerbros/tiktok-followers-scraper |
| TikTok Mention Scraper | https://apify.com/crawlerbros/tiktok-mention-scraper |
| TikTok Profile Mention Scraper | https://apify.com/crawlerbros/tiktok-profile-mention-scraper |
| TikTok Playlist Scraper | https://apify.com/crawlerbros/tiktok-playlist-scraper |
| TikTok Explore Scraper | https://apify.com/crawlerbros/tiktok-explore-scraper |
| TikTok For You Scraper | https://apify.com/crawlerbros/tiktok-for-you-scraper |
| TikTok Downloader | https://apify.com/crawlerbros/tiktok-downloader-api |
| TikTok Top Ads Scraper | https://apify.com/crawlerbros/tiktok-top-ads-scraper |
| TikTok Hashtag Trends Scraper | https://apify.com/crawlerbros/tiktok-hashtag-trends-scraper |
| TikTok LIVE Scraper | https://apify.com/crawlerbros/tiktok-live-scraper |

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/tiktok-ads-library-scraper-pro)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
