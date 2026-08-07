# Facebook Ads Scraper Pro Tutorial: Run This Apify Actor with Python

Extract Facebook ads data from the Ad Library. Search by keywords or page names, filter by country, status, ad type, and media type. Get ad text, page info, media URLs, dates, CTA buttons, landing page links, and more - no login required.

This repository shows how to run [Facebook Ads Scraper Pro](https://apify.com/crawlerbros/facebook-ads-scraper-pro) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/facebook-ads-scraper-pro`
- **Apify Store:** [https://apify.com/crawlerbros/facebook-ads-scraper-pro](https://apify.com/crawlerbros/facebook-ads-scraper-pro)
- **SEO title:** Facebook Ads Scraper Pro Tutorial: Run This Apify Actor with Python
- **Description:** Extract Facebook ads data from the Ad Library. Search by keywords or page names, filter by country, status, ad type, and media type. Get ad text, page info, media URLs, dates, CTA buttons, landing page links, and more - no login required.

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

# Facebook Ads Scraper Pro

Extract ads from the [Facebook Ad Library](https://www.facebook.com/ads/library/) at scale — ad copy, media, CTA, landing page, page info, and more. No login, no cookies, no manual clicking. Just pass in keywords or page names and get structured ad data back.

Perfect for marketers, competitive analysts, agencies, and researchers who need to track what brands are advertising on Facebook and Instagram.

## Features

- **Search by keywords or page names** — one actor, any kind of query
- **Filter by country, status, ad type, and media type** — narrow down to exactly the ads you want
- **Extracts everything** — ad text, page info, media URLs, start/end dates, platforms, CTA buttons, landing page URLs
- **No login required** — the Facebook Ad Library is public; this actor does not need cookies or Facebook accounts
- **Works with all ad categories** — regular, political & issue, housing, employment, credit
- **Clean structured output** — one row per ad, ready to import into your analytics stack

## Input

| Field | Type | Required | Description | Default |
|-------|------|----------|-------------|---------|
| `searchTerms` | string[] | Yes | Keywords or page names to search. Each term is searched separately. | — |
| `country` | string | No | 2-letter country code (`US`, `GB`, `DE`, `IN`, …) or `ALL` | `ALL` |
| `adActiveStatus` | string | No | `all`, `active`, or `inactive` | `active` |
| `adType` | string | No | `all`, `political_and_issue_ads`, `housing`, `employment`, `credit` | `all` |
| `mediaType` | string | No | `all`, `image`, `video`, `meme`, `none` | `all` |
| `resultsPerSearch` | integer | No | Max ads per search term (1–500) | 50 |
| `proxyConfiguration` | object | Yes | Proxy settings — residential proxy recommended | Apify residential |

### Example input

```json
{
  "searchTerms": ["nike", "adidas"],
  "country": "US",
  "adActiveStatus": "active",
  "adType": "all",
  "mediaType": "all",
  "resultsPerSearch": 50
}
```

## Output

Each row in the dataset represents one ad from the Facebook Ad Library.

| Field | Type | Description |
|-------|------|-------------|
| `ad_id` | string | Unique Facebook ad archive ID |
| `page_name` | string | Name of the Facebook page running the ad |
| `page_id` | string | Facebook page ID |
| `ad_text` | string | Ad creative text / copy |
| `ad_snapshot_url` | string | Direct link to view the ad in the Facebook Ad Library |
| `start_date` | string | When the ad started running |
| `end_date` | string | When the ad stopped (if inactive) |
| `status` | string | `active` or `inactive` |
| `platforms` | string[] | Platforms where the ad runs (Facebook, Instagram, Messenger, Audience Network) |
| `media_type` | string | `image`, `video`, `meme`, or `none` |
| `media_url` | string | Direct URL to the ad media asset |
| `cta_text` | string | Call-to-action button text (e.g. "Shop Now", "Learn More") |
| `link_url` | string | Landing page URL the ad sends users to |
| `search_term` | string | The input search term that found this ad |
| `scraped_at` | string | ISO-8601 timestamp of when the ad was scraped |

### Example output row

```json
{
  "ad_id": "1234567890123456",
  "page_name": "Nike",
  "page_id": "15087023444",
  "ad_text": "Just Do It. New Air Max drops this week.",
  "ad_snapshot_url": "https://www.facebook.com/ads/library/?id=1234567890123456",
  "start_date": "2026-01-10",
  "status": "active",
  "platforms": ["facebook", "instagram"],
  "media_type": "video",
  "media_url": "https://scontent.fxxx.fbcdn.net/v/...",
  "cta_text": "Shop Now",
  "link_url": "https://www.nike.com/air-max",
  "search_term": "nike",
  "scraped_at": "2026-01-15T12:34:56.789000+00:00"
}
```

## Use cases

- **Competitive analysis** — see exactly what ads your competitors are running, when they started, and on which platforms
- **Creative research** — build swipe files of winning ad copy, formats, and CTAs in your niche
- **Agency reporting** — track the ad cadence of clients and their competitors for monthly decks
- **Brand monitoring** — catch spoof or imposter ads using your brand name
- **Political & issue ad tracking** — audit political advertising spend, messaging, and reach
- **Market research** — spot trends across categories, countries, and media types

## FAQ

**Do I need a Facebook account or cookies?**
No. The Facebook Ad Library is public. This actor scrapes it without any authentication.

**Do I need a residential proxy?**
Yes — Facebook's CDN blocks data-center IPs on the Ad Library. A residential proxy is pre-configured by default and you can leave it as-is.

**What's the difference between "search by keyword" and "search by page name"?**
The same input field handles both. If you enter a page name like `nike`, the actor surfaces ads from that page. If you enter a keyword like `running shoes`, the actor surfaces ads whose text matches the keyword across many pages.

**Can I search for ads in a specific country?**
Yes. Set `country` to a 2-letter ISO code (e.g. `US`, `GB`, `DE`, `IN`). Use `ALL` to search globally.

**Do you scrape political and issue-based ads?**
Yes. Set `adType` to `political_and_issue_ads`, `housing`, `employment`, or `credit` to target those categories. Political ads include extra disclosure information from Facebook.

**What if an ad has no media?**
Text-only ads (where `mediaType` is `none`) are still returned with `ad_text`, `cta_text`, `link_url`, and metadata — the `media_url` is simply omitted.

**How fresh is the data?**
Each run fetches the latest ads currently in the Ad Library. Facebook updates the library in near real-time for active ads.

**Can I export results to Google Sheets / CSV / Excel?**
Yes. Apify exports the dataset in JSON, CSV, Excel, HTML, XML, and RSS — all available via the dataset API or the Apify Console.

**Does it work for Instagram ads too?**
Yes. The Facebook Ad Library covers both Facebook and Instagram. Ads that run on Instagram will have `"instagram"` in the `platforms` array.

## Limitations

- **Facebook may throttle very large runs** — the actor uses a residential proxy and adds delays to stay within limits, but for multi-thousand-ad runs expect occasional retries
- **Some older inactive ads** may have reduced media quality or missing CTA data
- **Ad creative impressions and spend** are only available for political & issue ads in countries where Facebook discloses them
- **Location targeting data** is not included — the Ad Library does not expose advertiser targeting parameters

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/facebook-ads-scraper-pro)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
