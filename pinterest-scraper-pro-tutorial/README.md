# Pinterest Scraper Pro Tutorial: Run This Apify Actor with Python

Scrape Pinterest pins, board pins, user boards, and user profiles. Modes: search by keyword, pin detail by URL, user pins, user boards, board pins, and user profile. Pro filters: minSaves, imageOnly, excludeAds. No login required.

This repository shows how to run [Pinterest Scraper Pro](https://apify.com/crawlerbros/pinterest-scraper-pro) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/pinterest-scraper-pro`
- **Apify Store:** [https://apify.com/crawlerbros/pinterest-scraper-pro](https://apify.com/crawlerbros/pinterest-scraper-pro)
- **SEO title:** Pinterest Scraper Pro Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Pinterest pins, board pins, user boards, and user profiles. Modes: search by keyword, pin detail by URL, user pins, user boards, board pins, and user profile. Pro filters: minSaves, imageOnly, excludeAds. No login required.

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

# Pinterest Scraper Pro

Scrape Pinterest pins, boards, and user profiles at scale. Search by keyword, fetch pin details directly, browse a user's pins, list a user's boards, pull pins from a specific board, or fetch a public profile summary - all without login cookies or a browser.

## Modes

| Mode | What it does |
|---|---|
| `search` | Keyword search - returns ranked pins matching your query |
| `pinDetail` | Direct pin lookup - fetch metadata for specific pin URLs or numeric pin IDs |
| `userPins` | Pins shown on a public user profile |
| `userBoards` | Public boards belonging to a user |
| `boardPins` | Pins inside a specific public board |
| `userProfile` | Public profile metadata for a user |

## What you get per pin

- `pinId`, `pinUrl`
- `title`, `description`, `altText`, `autoAltText`
- `imageUrl` and `images`
- `mediaType`, `isVideo`, `videoUrl`
- `saves`, `commentCount`, `reactionCount`
- `linkUrl`, `linkDomain`
- `creator`, `creatorFullName`, `creatorAvatar`, `creatorFollowerCount`, `creatorVerified`
- `boardName`, `boardUrl`, `boardPinCount`, `boardFollowerCount`, `boardSectionCount`
- `visualAnnotations`, `dominantColor`
- `richSummaryType`, `richSummarySite`, `richSummaryTitle`
- `isShoppable`, `isPromoted`
- `scrapedAt`

Empty fields are omitted - no nulls in output.

## What you get per profile

- `username`, `profileUrl`
- `fullName`, `bio`, `location`
- `followerCount`, `followingCount`, `pinCount`, `boardCount`, `monthlyViews`
- `avatarUrl`, `websiteUrl`
- `isVerified`
- `scrapedAt`

## What you get per board

Current `userBoards` output is intentionally lightweight and reliable:

- `boardSlug`, `boardName`, `boardUrl`
- `creator`
- `scrapedAt`

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | enum | `search` | `search`, `pinDetail`, `userPins`, `userBoards`, `boardPins`, `userProfile` |
| `keywords` | array | `["python tutorial"]` | Search terms used when `mode=search`. |
| `pinUrls` | array | `[]` | Direct pin URLs or numeric pin IDs used when `mode=pinDetail`. |
| `usernames` | array | `[]` | Pinterest usernames or full profile URLs used when `mode=userPins`, `mode=userBoards`, or `mode=userProfile`. |
| `boardUrls` | array | `[]` | Full board URLs or `username/board-slug` pairs used when `mode=boardPins`. |
| `maxItems` | integer | `50` | Hard cap on emitted records. Range `1-5000`. |
| `maxPages` | integer | `10` | Max result pages per keyword or board. Range `1-20`. |
| `language` | enum | `en` | Pinterest UI language. Affects ranked search results. |
| `minSaves` | integer | unset | Pro filter: drop pins with fewer than N saves. |
| `imageOnly` | boolean | `false` | Pro filter: keep image pins only. |
| `excludeAds` | boolean | `false` | Pro filter: drop promoted pins. |

### Example - keyword search

```json
{
  "mode": "search",
  "keywords": ["minimalist home office", "desk setup ideas"],
  "maxItems": 200,
  "minSaves": 100,
  "excludeAds": true
}
```

### Example - pin detail lookup

```json
{
  "mode": "pinDetail",
  "pinUrls": [
    "https://www.pinterest.com/pin/123456789012345678/",
    "987654321098765432"
  ]
}
```

### Example - board pins

```json
{
  "mode": "boardPins",
  "boardUrls": [
    "https://www.pinterest.com/nasa/hubble-images/",
    "earthlymanorfarm/cooking-recipes-for-dinner"
  ],
  "maxItems": 100
}
```

### Example - user profile

```json
{
  "mode": "userProfile",
  "usernames": ["nasa", "natgeo"]
}
```

## Sample output

### Pin

```json
{
  "recordType": "pin",
  "pinId": "123456789012345678",
  "pinUrl": "https://www.pinterest.com/pin/123456789012345678/",
  "title": "Minimalist Home Office Setup",
  "imageUrl": "https://i.pinimg.com/originals/aa/bb/cc/aabbcc1122334455.jpg",
  "mediaType": "image",
  "creator": "designblog",
  "boardName": "Home Office Ideas",
  "boardUrl": "https://www.pinterest.com/designblog/home-office-ideas/",
  "linkUrl": "https://designblog.example.com/minimalist-office",
  "scrapedAt": "2026-04-30T14:00:00+00:00"
}
```

### Profile

```json
{
  "recordType": "profile",
  "username": "nasa",
  "profileUrl": "https://www.pinterest.com/nasa/",
  "fullName": "NASA",
  "followerCount": 1250000,
  "pinCount": 3400,
  "boardCount": 47,
  "avatarUrl": "https://i.pinimg.com/280x280_RS/.../nasa.jpg",
  "websiteUrl": "https://www.nasa.gov",
  "isVerified": true,
  "scrapedAt": "2026-04-30T14:00:00+00:00"
}
```

### Board

```json
{
  "recordType": "board",
  "boardSlug": "home-office-ideas",
  "boardName": "Home Office Ideas",
  "boardUrl": "https://www.pinterest.com/designblog/home-office-ideas/",
  "creator": "designblog",
  "scrapedAt": "2026-04-30T14:00:00+00:00"
}
```

## Proxy and reliability notes

- The actor is HTTP-only via `curl_cffi`.
- Pinterest may soft-block some datacenter IPs with empty or partial responses.
- On Apify cloud, the actor tries Apify Residential proxy first, then AUTO proxy, then falls back to no proxy if needed.
- `boardPins` and `userProfile` use public HTML fallback when Pinterest blocks the resource endpoint for anonymous access.

## FAQ

**Does it require a login or cookies?**  
No. All six modes use public Pinterest endpoints or public HTML pages.

**Is a proxy recommended?**  
Yes on Apify cloud. Pinterest can return empty or partial results from some datacenter IPs, so the actor prefers Apify Residential proxy and falls back automatically.

**Why might `boardPins` or `userProfile` return fewer fields than `search` or `pinDetail`?**  
Pinterest exposes less data on some public HTML pages than on search/resource responses. The actor still returns a clean record instead of failing.

**Why might `saves` be missing on some pins?**  
Pinterest does not expose save counts on every pin type. When the API does not return a count, the field is omitted.

**What happens if a username, board, or pin does not exist?**  
The actor finishes cleanly. If nothing is found, it sets a status message instead of pushing placeholder rows.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/pinterest-scraper-pro)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
