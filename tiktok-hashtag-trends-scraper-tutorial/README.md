# TikTok Hashtag Trends Scraper Tutorial: Run This Apify Actor with Python

Track trending TikTok hashtags from the Creative Center. Returns rank, post count, video views, popularity curve, and top creators for each trending hashtag.

This repository shows how to run [TikTok Hashtag Trends Scraper](https://apify.com/crawlerbros/tiktok-hashtag-trends-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/tiktok-hashtag-trends-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/tiktok-hashtag-trends-scraper](https://apify.com/crawlerbros/tiktok-hashtag-trends-scraper)
- **SEO title:** TikTok Hashtag Trends Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Track trending TikTok hashtags from the Creative Center. Returns rank, post count, video views, popularity curve, and top creators for each trending hashtag.

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

# TikTok Hashtag Trends Scraper

Track trending TikTok hashtags from the Creative Center at ads.tiktok.com/business/creativecenter/hashtag. Returns ranked hashtags with post count, total video views, and a time-series popularity curve showing trend momentum. Supports any country available in TikTok Creative Center. Note: the public unauthenticated endpoint caps results at 3 hashtags per request.

## What this actor does

- Fetches trending hashtags from TikTok's Creative Center trends API
- Returns rank position, post count, video views, and a popularity curve per hashtag
- Filters by country (any ISO 2-letter code supported by Creative Center) and time period
- Records `observedCountry` and `observedPeriod` on each row for dataset provenance
- Exits cleanly with a log message if TikTok restricts access from the current IP — no crash or error rows
- Empty fields are omitted

## Output per hashtag

- `hashtagId` — TikTok's internal hashtag identifier
- `hashtagName` — hashtag text without the `#` symbol
- `publishCnt` — number of videos published using this hashtag in the observed period
- `rankIndex` — rank position in the trending list (1 = most trending)
- `popularityCurve` — array of `{ time, value }` data points showing trend momentum over the period
- `vv` — total video views on content using this hashtag
- `observedCountry` — country code used for this query
- `observedPeriod` — time period in days used for this query
- `scrapedAt` — ISO 8601 timestamp of collection

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `country` | string | `"US"` | ISO 2-letter country code (e.g. `US`, `GB`, `JP`, `KR`, `BR`). Country-specific results depend on a matching proxy IP being available. |
| `period` | string | `"7"` | Trend observation window: `"7"` (recent spikes), `"30"` (sustained trends), or `"180"` (long-term). |
| `maxRanks` | integer | `3` | Maximum number of trending hashtags to return. TikTok's public unauthenticated endpoint caps this at 3. |

### Example: Top 3 trending hashtags in the US this week

```json
{
  "country": "US",
  "period": "7",
  "maxRanks": 3
}
```

### Example: 30-day trends in the UK

```json
{
  "country": "GB",
  "period": "30",
  "maxRanks": 3
}
```

### Example: Long-term trends in Japan

```json
{
  "country": "JP",
  "period": "180",
  "maxRanks": 3
}
```

### Example: Weekly trends in Brazil

```json
{
  "country": "BR",
  "period": "7",
  "maxRanks": 3
}
```

## Use cases

- **Content strategy** — identify the hashtags driving the most views right now in your target market and incorporate them into upcoming posts
- **Campaign timing** — monitor the popularity curve to catch hashtags at the start of their upward trend before they peak
- **Market research** — compare trending hashtags across countries to understand regional audience interests and cultural moments
- **Influencer briefing** — provide creators with a weekly top-3 list of trending hashtags in their niche or geography
- **Competitor benchmarking** — track whether your brand or category hashtags appear in the trending list over time

## FAQ

**Q: Why does the actor only return 3 hashtags?**  
A: TikTok's public Creative Center endpoint caps unauthenticated requests at 3 hashtags per query. This is a platform-level limit, not an actor limitation.

**Q: What countries are supported?**  
A: Any country code recognized by TikTok Creative Center, including US, GB, JP, KR, BR, DE, FR, ID, TH, VN, PH, AU, CA, MX, and many more.

**Q: How often should I run this actor?**  
A: For daily trend monitoring, run once per day. TikTok updates Creative Center trends on a daily cycle.

**Q: How do I monitor multiple countries?**  
A: Run the actor once per country. Each run is fast (only 3 results), so monitoring 10–20 countries daily is practical.

**Q: What is the `popularityCurve` field?**  
A: An array of `{ time, value }` data points that shows how the hashtag's popularity score changed over the selected period. Use it to determine whether a hashtag is rising, peaked, or declining.

**Q: What is `publishCnt` vs `vv`?**  
A: `publishCnt` is the number of new videos posted with the hashtag during the period. `vv` is the total view count accumulated on those videos. A hashtag with low `publishCnt` but high `vv` indicates high per-video virality.

**Q: What happens if no data is returned?**  
A: TikTok occasionally restricts Creative Center API access from certain datacenter IP ranges. When this occurs, the actor logs a clear message and exits cleanly without pushing error rows.

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
| TikTok Ads Library Scraper | https://apify.com/crawlerbros/tiktok-ads-library-scraper-pro |
| TikTok Top Ads Scraper | https://apify.com/crawlerbros/tiktok-top-ads-scraper |
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

- [Run this actor on Apify](https://apify.com/crawlerbros/tiktok-hashtag-trends-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
