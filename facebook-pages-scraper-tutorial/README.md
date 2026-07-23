# Facebook Pages Scraper Tutorial: Run This Apify Actor with Python

Discover Facebook pages through search engines and extract structured page data including IDs, names, categories, addresses, follower counts, phone numbers, emails, websites, business hours, ratings, and media.

This repository shows how to run [Facebook Pages Scraper](https://apify.com/crawlerbros/facebook-pages-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/facebook-pages-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/facebook-pages-scraper](https://apify.com/crawlerbros/facebook-pages-scraper)
- **SEO title:** Facebook Pages Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Discover Facebook pages through search engines and extract structured page data including IDs, names, categories, addresses, follower counts, phone numbers, emails, websites, business hours, ratings, and media.

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

# Facebook Pages Scraper

Discover and extract structured data from Facebook Pages at scale. This actor discovers relevant Facebook Pages via Facebook's own search (most reliable, requires session cookies) plus DuckDuckGo and Google as supplementary sources, then extracts business details, engagement metrics, contact info, and more — all using residential IPs for reliability.

## What You'll Get

Each discovered page is returned as a structured row with fields including:

- **Page identity**: name, ID, canonical URL, categories
- **Engagement**: follower count, likes, check-ins, talking-about
- **Contact**: email, phone, address, website, Messenger link
- **Media**: profile picture, cover photo
- **Business info**: price range, business hours, rating, ad library reference

## Features

- **Search-powered discovery**: finds pages via Facebook's own search (when cookies are provided) plus DuckDuckGo and Google as supplementary sources
- **Scale to 1K+ results**: combine multiple search terms × locations and increase `maxItems` (each combination adds up to ~40 pages to the pool)
- **Residential IPs always**: all Facebook page requests use Apify residential proxy — no need to configure proxy settings
- **Cookie authentication**: when you provide session cookies the scraper bypasses most login-wall blocks
- **Smart fallback chain**: HTTP → Playwright browser → Playwright with cookies (each step only activates when the previous one fails)
- **Dual extraction**: regex over JSON-LD, Open Graph, inline scripts, and intro cards for maximum field coverage
- **Error rows**: unavailable/deleted pages appear as structured error rows instead of being silently dropped

## Input

| Field         | Type             | Default      | Description                                                                                       |
| ------------- | ---------------- | ------------ | ------------------------------------------------------------------------------------------------- |
| `searchTerms` | Array of strings | _(required)_ | Plain search terms for page discovery (e.g. `["Coffee Shop", "Bakery"]`)                          |
| `locations`   | Array of strings | `[]`         | Optional locations combined with each search term (e.g. `["London", "Manchester"]`)               |
| `maxItems`    | Integer          | `10`         | Maximum number of page rows to output                                                             |
| `cookies`     | String           | `""`         | Facebook session cookies — **strongly recommended**. See [Cookies](#cookies-authentication) below |

### Example Input

```json
{
  "searchTerms": ["Coffee Shop", "Cafe", "Bakery"],
  "locations": ["London", "Manchester", "Birmingham"],
  "maxItems": 300,
  "cookies": "..."
}
```

That single input produces 9 search combinations (3 terms × 3 cities), each yielding up to ~40 discovered URLs — giving a pool of up to ~360 candidates to fill 300 results from.

### Cookies (Authentication)

**Strongly recommended for any run.**

Without session cookies, Facebook serves a compact login-wall stub for many discovered pages — you'll get some data but contact fields (phone, address, website) are gated. Providing cookies lets the scraper retry login-wall pages with an authenticated browser, dramatically increasing field coverage and yield.

**How to export cookies from your browser:**

1. Log in to Facebook in Chrome or Firefox
2. Open DevTools → Application → Cookies → `facebook.com`
3. Export the cookies for `.facebook.com` using a browser extension like [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg) (export as JSON) or [Cookie Quick Manager](https://addons.mozilla.org/en-US/firefox/addon/cookie-quick-manager/) on Firefox
4. Paste the exported JSON array into the `cookies` field

**Minimum cookies needed:** `c_user`, `xs`, `datr`, `fr`, `sb`.

**Accepted formats:**

1. **JSON array** (recommended — export directly from your browser extension):

   ```json
   [
     { "name": "c_user", "value": "100074...", "domain": ".facebook.com", "path": "/", "expires": 1815212390, "httpOnly": false, "secure": true },
     { "name": "xs", "value": "8%3A2vaT...", "domain": ".facebook.com", "path": "/", "httpOnly": true, "secure": true },
     { "name": "datr", "value": "7JhPar...", "domain": ".facebook.com", "path": "/", "httpOnly": true, "secure": true }
   ]
   ```

2. **Cookie header string:** `"c_user=100074...; xs=8%3A...; datr=7JhP..."`

Cookies expire (typically 90 days). If you see high skip rates, refresh your cookies.

## Scaling to 1K+ Results

The actor is designed to scale — here is the fastest path to large datasets:

1. **Use multiple search terms and locations.** Each `(term, location)` pair runs its own discovery pass. Example: 5 terms × 10 cities = 50 combinations × up to ~40 pages each = up to ~2,000 candidates in the pool.

2. **Set `maxItems` to your target.** The actor over-discovers ~2× `maxItems` URLs to absorb login-walls and fetch failures without leaving you short.

3. **Provide session cookies.** This is essential at scale — cookies enable Facebook's own search as the primary discovery source (far more reliable than external search engines) and let login-wall pages be retried with an authenticated browser.

4. **Vary your search terms.** Generic terms (e.g. `"Restaurant"`) produce many duplicate pages across locations. More specific terms (e.g. `"Italian Restaurant"`, `"Sushi Bar"`) yield more unique pages.

**Example for 1K results:**

```json
{
  "searchTerms": ["Restaurant", "Cafe", "Bar", "Pub", "Bistro"],
  "locations": ["London", "Manchester", "Birmingham", "Glasgow", "Leeds", "Bristol", "Edinburgh", "Liverpool", "Sheffield", "Cardiff"],
  "maxItems": 1000,
  "cookies": "..."
}
```

50 search combinations, each yielding up to ~40 unique URLs — enough to fill 1K+ results (with cookies provided).

## Output

### Page Identity

| Field        | Type           | Description                              |
| ------------ | -------------- | ---------------------------------------- |
| `facebookUrl` | String        | Facebook page URL                        |
| `pageUrl`    | String         | Normalized page URL                      |
| `pageName`   | String         | Page name or slug                        |
| `pageId`     | String or null | Facebook page identifier                 |
| `facebookId` | String or null | Facebook ID (usually matches `pageId`)   |
| `title`      | String or null | Full page title with context             |

### Classification

| Field      | Type          | Description                              |
| ---------- | ------------- | ---------------------------------------- |
| `categories` | Array or null | Page categories                        |
| `category` | String or null | Primary category                         |
| `info`     | Array or null  | Short info lines from the page           |
| `intro`    | String or null | Page introduction or description         |

### Contact & Business

| Field        | Type           | Description                              |
| ------------ | -------------- | ---------------------------------------- |
| `phone`      | String or null | Public phone number                      |
| `email`      | String or null | Public contact email                     |
| `messenger`  | String or null | Messenger link                           |
| `address`    | String or null | Address or coordinates                   |
| `addressUrl` | String or null | Google Maps link for the address         |
| `website`    | String or null | Primary linked website                   |
| `websites`   | Array or null  | All detected website links               |
| `priceRange` | String or null | Price range (e.g. `"££"`)               |

### Engagement

| Field             | Type           | Description                     |
| ----------------- | -------------- | ------------------------------- |
| `followers`       | Number or null | Follower count                  |
| `likes`           | Number or null | Like count                      |
| `followings`      | Number or null | Following count                 |
| `checkins`        | Number or null | Check-in count ("were here")    |
| `talkingAboutCount` | Number or null | Talking-about count           |

### Media

| Field               | Type           | Description               |
| ------------------- | -------------- | ------------------------- |
| `profilePictureUrl` | String or null | Profile picture URL       |
| `coverPhotoUrl`     | String or null | Cover photo URL           |

### Business Details

| Field            | Type            | Description                                                      |
| ---------------- | --------------- | ---------------------------------------------------------------- |
| `business_hours` | String or null  | Business hours info                                              |
| `ratingOverall`  | Number or null  | Overall rating score                                             |
| `ratingCount`    | Number or null  | Review/rating count                                              |
| `ratingText`     | String or null  | Human-readable rating text                                       |
| `pageAdLibrary`  | Object or null  | Ad library metadata or link                                      |

### Sample Output

```json
{
  "facebookUrl": "https://www.facebook.com/ozonecoffeeuk",
  "pageUrl": "https://www.facebook.com/ozonecoffeeuk",
  "pageName": "ozonecoffeeuk",
  "pageId": "191234567",
  "facebookId": "191234567",
  "title": "Ozone Coffee Roasters | Facebook",
  "categories": ["Coffee Shop"],
  "category": "Coffee Shop",
  "info": null,
  "intro": "Specialty coffee roaster and cafe in London.",
  "phone": null,
  "email": null,
  "messenger": "https://m.me/191234567",
  "priceRange": null,
  "address": null,
  "addressUrl": null,
  "website": null,
  "websites": null,
  "followers": 9100,
  "followings": 12,
  "checkins": null,
  "talkingAboutCount": null,
  "profilePictureUrl": "https://scontent.xx.fbcdn.net/v/...",
  "coverPhotoUrl": "https://scontent.xx.fbcdn.net/v/...",
  "ratingOverall": null,
  "ratingCount": null,
  "ratingText": null,
  "business_hours": null,
  "pageAdLibrary": "https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id=191234567&search_type=page"
}
```

### Error Rows

When a page is unavailable or deleted:

```json
{
  "url": "https://www.facebook.com/pages/OldPage/163665216985663",
  "error": "not_available",
  "errorDescription": "This content isn't available..."
}
```

## Use Cases

- **Local business discovery**: find businesses in specific cities or regions
- **Competitive intelligence**: build datasets of competitor pages in your industry
- **Lead generation**: collect pages with contact info for outreach
- **Market research**: survey the Facebook page landscape for a category
- **Monitoring**: run repeatedly to track new pages for a search term

## FAQ

### Do I need a Facebook account to use this?

No, but it's strongly recommended. Without cookies the scraper falls back to DuckDuckGo/Google discovery and extracts public HTML only. Providing session cookies from a logged-in Facebook account enables the most reliable discovery method (Facebook's own search), unlocks retry capability for login-wall pages, and gives access to contact fields that aren't in the public HTML.

### Why are some fields null?

A null field means Facebook did not expose that information in the page's public HTML, the page owner did not fill it in, or the field layout for that page type doesn't include it. Fields like `phone`, `address`, and `website` are only populated when the page owner has listed them on their Facebook page. Adding cookies increases the chance of extracting these for login-gated pages.

### Why did I get fewer results than `maxItems`?

The most common reasons:

- **Login walls**: Facebook gates some pages behind a login session. Without cookies, these are skipped. Provide session cookies to retry login-wall pages with an authenticated browser.
- **No cookies provided**: without session cookies, discovery relies solely on DuckDuckGo/Google, which are less reliable than Facebook's own search — add cookies for the best results.
- **Narrow search terms**: each `(term, location)` pair yields a limited pool. Add more search terms or locations.

### Can I get 1,000+ results?

Yes — see [Scaling to 1K+ Results](#scaling-to-1k-results) above. The short version: combine multiple search terms × multiple locations and set `maxItems` to your target. The actor handles all pagination and over-discovers URLs automatically.

### How often do I need to refresh my cookies?

Facebook session cookies typically last 90 days. If you notice a sudden drop in results or many login-wall skips in the logs, export fresh cookies from your browser.

### Does this work for Facebook Groups or personal profiles?

No. The scraper targets public Facebook Pages (business pages, community pages, public figures). Facebook Groups and personal profiles have different URL structures and content restrictions.

### Is residential proxy required?

Residential proxy is used automatically for all Facebook page fetches and is already included — you do not need to configure or pay for it separately. The proxy cost is covered by your Apify usage credits.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/facebook-pages-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
