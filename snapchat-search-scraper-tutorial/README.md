# Snapchat Search Scraper Tutorial: Run This Apify Actor with Python

Scrape Snapchat search results - spotlight videos, AR lenses, topics, users, publisher editions, places, and more.

This repository shows how to run [Snapchat Search Scraper](https://apify.com/crawlerbros/snapchat-search-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/snapchat-search-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/snapchat-search-scraper](https://apify.com/crawlerbros/snapchat-search-scraper)
- **SEO title:** Snapchat Search Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Snapchat search results - spotlight videos, AR lenses, topics, users, publisher editions, places, and more.

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

## Snapchat Search Scraper

Search Snapchat's public explore pages by keyword and extract results across all content types — Spotlight videos with direct media URLs, AR lenses, topics, user profiles, Snap Pro business profiles, publisher episodes, shows, and physical places. No login, no cookies, no browser required.

For each keyword you provide, the actor fetches the Snapchat explore page, decodes the embedded search response, and returns one structured record per result with type-specific fields.

### What You Get

- **Spotlight videos** with direct bolt/CDN video URLs, creator info, dimensions, and duration
- **AR lenses** with icon, preview images, unlock URL, and creator info
- **Topics** (hashtags) with snap counts and thumbnails
- **User profiles** with display name, avatar, and verified status
- **Snap Pro business profiles** with contact details, address, logo, and subscriber count
- **Publisher editions** (show episodes) with title, publish date, and deep link
- **Publisher/show pages** with subscriber counts and show metadata
- **Places** with coordinates, category, bounding box, and story preview
- All 8 section types in one run per keyword

### Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `keywords` | string\[] | Yes | — | Search keywords (e.g. `food`, `new york`, `selenagomez`) |
| `resultTypes` | string\[] | No | All 8 types | Section types to include: `spotlight`, `lens`, `topic`, `user`, `snapProEntity`, `publisherEdition`, `publisher`, `place` |
| `maxResultsPerQuery` | integer | No | `100` | Maximum records to return per keyword across all result types (max 500) |
| `includeSpotlightDetails` | boolean | No | `true` | Enrich spotlight results with direct video URL, dimensions, duration, and creator info from the card map |
| `proxyConfiguration` | object | No | — | Optional proxy settings |

### Output Fields

Every record includes these common fields:

| Field | Type | Description |
|-------|------|-------------|
| `query` | string | The keyword that produced this result |
| `resultType` | string | Section type: `spotlight`, `lens`, `topic`, `user`, `snapProEntity`, `publisherEdition`, `publisher`, or `place` |
| `rank` | integer | Position in combined results (1-based, across all types) |
| `scrapedAt` | string | ISO 8601 UTC scrape timestamp |

#### Spotlight Fields (`resultType: "spotlight"`)

| Field | Type | Description |
|-------|------|-------------|
| `storyId` | string | Hex story identifier |
| `rawSnapId` | string | Base64-style snap identifier used for card map lookups |
| `thumbnailUrl` | string | Preview thumbnail URL |
| `mediaUrl` | string | Direct video URL from search result |
| `boltVideoUrl` | string | Watermarked bolt CDN video URL (higher quality, from card map) |
| `flatVideoUrl` | string | Unencrypted flat CDN video URL (from card map) |
| `creatorUsername` | string | Creator's Snapchat username |
| `creatorDisplayName` | string | Creator's display name |
| `teaserText` | string | Caption preview text |
| `snapDescription` | string | Full caption/description text |
| `caption` | string | Caption field from card map |
| `postedAt` | string | ISO 8601 post timestamp |
| `durationSeconds` | number | Video length in seconds |
| `width` | integer | Video width in pixels |
| `height` | integer | Video height in pixels |

#### Lens Fields (`resultType: "lens"`)

| Field | Type | Description |
|-------|------|-------------|
| `lensId` | string | Lens numeric identifier |
| `lensName` | string | Lens display name |
| `creatorName` | string | Creator's display name |
| `creatorIsOfficial` | boolean | Whether the creator is an official Snap partner |
| `iconUrl` | string | Lens icon thumbnail URL |
| `deeplinkUrl` | string | URL to unlock/open the lens in Snapchat app |
| `thumbnailUrl` | string | Preview thumbnail URL |
| `thumbnailSequence` | object | Animated thumbnail sequence (`urlPattern`, `numThumbnails`, `animationIntervalMs`) |

#### Topic Fields (`resultType: "topic"`)

| Field | Type | Description |
|-------|------|-------------|
| `topicText` | string | Hashtag or topic text |
| `numSnaps` | integer | Number of snaps tagged with this topic |
| `topicType` | any | Topic type identifier from Snapchat |
| `thumbnailUrl` | string | Topic thumbnail URL |
| `iconUrl` | string | Topic icon URL |
| `conversationId` | string | Internal conversation/topic ID |

#### User Fields (`resultType: "user"`)

| Field | Type | Description |
|-------|------|-------------|
| `userId` | string | User ID |
| `username` | string | Snapchat username |
| `displayName` | string | Display name |
| `snapProId` | string | Snap Pro profile ID (if applicable) |
| `profileLogoUrl` | string | Profile avatar URL |
| `isPopular` | boolean | Whether Snapchat marks this user as popular |
| `isOfficial` | boolean | Whether this is a verified/official account |
| `emoji` | string | Emoji associated with the profile |
| `contextHint` | string | Context hint text shown in search results |

#### Snap Pro Entity Fields (`resultType: "snapProEntity"`)

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Business profile ID |
| `title` | string | Business name |
| `description` | string | Business description |
| `logoUrl` | string | Business logo URL |
| `heroImageUrl` | string | Hero/banner image URL |
| `phoneNumber` | string | Contact phone number |
| `address` | string | Physical address |
| `emailAddress` | string | Contact email |
| `whatsappNumber` | string | WhatsApp contact number |
| `websiteUrl` | string | Business website URL |
| `profileDeeplinkUrl` | string | Deep link to open this profile in Snapchat |
| `hostAccountUsername` | string | Snapchat username of the host account |
| `category` | any | Business category enum |
| `subcategory` | any | Business subcategory enum |
| `tier` | any | Profile tier |
| `subscriberCount` | integer | Number of subscribers |
| `isOfficialAccount` | boolean | Whether this is an official account |
| `isBrandProfile` | boolean | Whether this is a brand profile |
| `hasLenses` | boolean | Whether the business has published lenses |

#### Publisher Edition Fields (`resultType: "publisherEdition"`)

| Field | Type | Description |
|-------|------|-------------|
| `editionId` | string | Edition identifier |
| `storyDocId` | string | Story document ID in `namespace/id` format |
| `title` | string | Episode/edition title |
| `publishedAt` | string | ISO 8601 publish timestamp |
| `thumbnailUrl` | string | Episode thumbnail URL |
| `deeplinkUrl` | string | Deep link to open in Snapchat app |
| `publisher` | object | Publisher metadata (id, displayName, iconUrl, approxSubscriptionCount, etc.) |

#### Publisher Fields (`resultType: "publisher"`)

| Field | Type | Description |
|-------|------|-------------|
| `publisherId` | string | Publisher identifier |
| `businessProfileId` | string | Associated business profile ID |
| `displayName` | string | Publisher/show display name |
| `description` | string | Publisher description |
| `iconUrl` | string | Publisher icon URL |
| `deeplinkUrl` | string | Deep link to open in Snapchat app |
| `primaryColor` | string | Brand primary color hex |
| `isShow` | boolean | Whether this is a Snapchat Show |
| `showId` | string | Show identifier (if isShow) |
| `latestEditionId` | string | Most recent episode ID |
| `approxSubscriptionCount` | integer | Approximate subscriber count |

#### Place Fields (`resultType: "place"`)

| Field | Type | Description |
|-------|------|-------------|
| `placeId` | string | Place UUID |
| `displayName` | string | Place name |
| `locality` | string | City or locality name |
| `centerLat` | number | Latitude of the place centroid |
| `centerLng` | number | Longitude of the place centroid |
| `categoryName` | string | Place category (e.g. "Tour Provider", "Restaurant") |
| `categoryIconUrl` | string | Category icon URL |
| `isFavorited` | boolean | Whether the current user has favorited this place |
| `favoriteCount` | integer | Total number of favorites |
| `boundingBox` | object | Bounding box with `p1` and `p2` lat/lng coordinates |
| `storyPreview` | object | Story preview info (`numSnaps`, `firstSnapId`, `thumbnailUrl`, etc.) |

### Example Input

```json
{
  "keywords": ["tbilisi", "food"],
  "resultTypes": ["spotlight", "lens", "place", "user"],
  "maxResultsPerQuery": 50,
  "includeSpotlightDetails": true
}
```

### Example Output

**Spotlight record:**

```json
{
  "query": "tbilisi",
  "resultType": "spotlight",
  "rank": 1,
  "scrapedAt": "2026-06-27T18:03:16.397008+00:00",
  "storyId": "463f0c002d6c40cfe953aaa0c6a5c7d1",
  "thumbnailUrl": "https://cf-st.sc-cdn.net/d/O9P7RBTPbIWB5E3Z0QL5w.1025?...",
  "mediaUrl": "https://bolt-gcdn.sc-cdn.net/z/O9P7RBTPbIWB5E3Z0QL5w.27.IRZXSOY?...",
  "rawSnapId": "W7_EDlXWTBiXAEEniNoMPwAAYa3RxdnBoc2dpAZ6bxm40AZ6bxmItAAAAAw",
  "creatorUsername": "s_saruh24",
  "creatorDisplayName": "Sar Nn",
  "snapDescription": "#tbilisi #georgia #🇬🇪 #georgiatbilisi",
  "postedAt": "2026-06-06T07:12:10.285000+00:00",
  "boltVideoUrl": "https://bolt-gcdn.sc-cdn.net/z/O9P7RBTPbIWB5E3Z0QL5w.27.IRZXSOY?...",
  "flatVideoUrl": "https://cf-st.sc-cdn.net/d/O9P7RBTPbIWB5E3Z0QL5w.1034.IRZXSOY?...",
  "width": 540,
  "height": 960,
  "durationSeconds": 8.23
}
```

**Place record:**

```json
{
  "query": "tbilisi",
  "resultType": "place",
  "rank": 30,
  "scrapedAt": "2026-06-27T18:03:16.397747+00:00",
  "placeId": "a9cd7a06-9993-11e8-8dc3-bb0bdff21005",
  "displayName": "Tbilisi Hack Free Tours",
  "locality": "Freedom Square, Tbilisi",
  "centerLat": 41.692909240722656,
  "centerLng": 44.801605224609375,
  "categoryName": "Tour Provider",
  "isFavorited": false,
  "favoriteCount": 51,
  "boundingBox": {
    "p1": { "lat": 41.692859240722655, "lng": 44.80155522460937 },
    "p2": { "lat": 41.69295924072266, "lng": 44.80165522460938 }
  },
  "storyPreview": {
    "numSnaps": 6,
    "firstSnapId": "W7_EDlXWTBiXAEEniNoMPwAAYaWtvZ3Jycm12AZsU16NfAZsU16J9AAAAAQ",
    "thumbnailUrl": "https://cf-st.sc-cdn.net/d/5bU09jU4HvZuI3nZ2euXo.256.IRZXSOY?..."
  }
}
```

### FAQ

**Does this require login or cookies?**
No. Snapchat's explore pages are fully public and accessible without authentication.

**How many results can I get per keyword?**
Snapchat's page embeds a fixed set per section — typically 3–20 results per type. The `maxResultsPerQuery` cap applies across all combined types. Maximum is 500.

**What is `includeSpotlightDetails` and when should I enable it?**
When enabled, spotlight results are enriched with a second data source embedded in the page — the spotlight card map. This adds direct `boltVideoUrl`, `flatVideoUrl`, `width`, `height`, `durationSeconds`, full `snapDescription`, and better creator info. It is enabled by default.

**Can I filter to just one result type?**
Yes — set `resultTypes` to `["spotlight"]` (or any subset) and only those sections will be extracted.

**Can I scrape multiple keywords at once?**
Yes. Add multiple values to the `keywords` list. Each keyword produces its own set of results identified by the `query` field.

**Why does a search for a common word return lenses but not users?**
Snapchat only includes a section in the page when it has matching content. If no user profiles match a keyword, the user section is absent — this is expected behavior.

**What is a `snapProEntity`?**
It is Snapchat's business profile type — companies and brands that have registered a Snap Pro account. These profiles contain contact information, address, category, and subscriber counts.

***

### Other Snapchat Scrapers

Explore the full Snapchat scraper suite on Apify:

| Actor | Description |
|-------|-------------|
| [Snapchat Profile Scraper](https://apify.com/crawlerbros/snapchat-profile-scraper) | Full profile metadata, highlights, lenses, and spotlight data |
| [Snapchat Hashtag Scraper](https://apify.com/crawlerbros/snapchat-hashtag-scraper) | Spotlight videos by hashtag or topic with AI metadata |
| [Snapchat User Stories Scraper](https://apify.com/crawlerbros/snapchat-user-stories-scraper) | Curated highlights and active story snaps |
| [Snapchat Spotlight Video Downloader](https://apify.com/crawlerbros/snapchat-spotlight-video-downloader) | Download Spotlight videos with AI metadata, transcripts, and comments |
| [Snapchat Search Scraper](https://apify.com/crawlerbros/snapchat-search-scraper) | Search across videos, lenses, users, places, and shows |
| [Snapchat Lens Scraper](https://apify.com/crawlerbros/snapchat-lens-scraper) | AR lens metadata, trending lenses, and creator info |
| [Snapchat Publisher Scraper](https://apify.com/crawlerbros/snapchat-publisher-scraper) | Discover publisher pages, shows, episodes, and spotlights |
| [Snapchat Ads Gallery Scraper](https://apify.com/crawlerbros/snapchat-ads-gallery-scraper) | EU/UK ad transparency library — ads and sponsored content |
| [Snapchat Spotlight Comments Scraper](https://apify.com/crawlerbros/snapchat-spotlight-comments-scraper) | Comment threads from Spotlight videos |
| [Snapchat Topic Scraper](https://apify.com/crawlerbros/snapchat-topic-scraper) | Spotlight videos by topic with related tags |
| [Snapchat Snapcode Scraper](https://apify.com/crawlerbros/snapchat-snapcode-scraper) | Download Snapcode images (SVG/PNG) for any username |
| [Snapchat Snap Map Scraper](https://apify.com/crawlerbros/snapchat-snap-map-scraper) | Public Snap Map places and their latest snaps |
| [Snapchat Discover Scraper](https://apify.com/crawlerbros/snapchat-discover-scraper) | Shows and stories from Snapchat's Discover feed |

# Actor input Schema

## `keywords` (type: `array`):

Keywords to search on Snapchat. Examples: food, selenagomez, new york

## `resultTypes` (type: `array`):

Which section types to include in output

## `maxResultsPerQuery` (type: `integer`):

Maximum results to return per keyword (across all result types)

## `includeSpotlightDetails` (type: `boolean`):

Enrich spotlight results with video URL, dimensions, and creator info from the spotlight card map. Enabled by default.

## `proxyConfiguration` (type: `object`):

Proxy settings (optional)

## Actor input object example

```json
{
  "keywords": [
    "food",
    "travel"
  ],
  "resultTypes": [
    "spotlight",
    "lens",
    "topic",
    "user"
  ],
  "maxResultsPerQuery": 100,
  "includeSpotlightDetails": true
}
```

# API

You can run this Actor programmatically using our API. Below are code examples in JavaScript, Python, and CLI, as well as the OpenAPI specification and MCP server setup.

## JavaScript example

```javascript
import { ApifyClient } from 'apify-client';

// Initialize the ApifyClient with your Apify API token
// Replace the '<YOUR_API_TOKEN>' with your token
const client = new ApifyClient({
    token: '<YOUR_API_TOKEN>',
});

// Prepare Actor input
const input = {
    "keywords": [
        "food",
        "travel"
    ],
    "resultTypes": [
        "spotlight",
        "lens",
        "topic",
        "user"
    ],
    "includeSpotlightDetails": true
};

// Run the Actor and wait for it to finish
const run = await client.actor("crawlerbros/snapchat-search-scraper").call(input);

// Fetch and print Actor results from the run's dataset (if any)
console.log('Results from dataset');
console.log(`💾 Check your data here: https://console.apify.com/storage/datasets/${run.defaultDatasetId}`);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
items.forEach((item) => {
    console.dir(item);
});

// 📚 Want to learn more 📖? Go to → https://docs.apify.com/api/client/js/docs

```

## Python example

```python
from apify_client import ApifyClient

# Initialize the ApifyClient with your Apify API token
# Replace '<YOUR_API_TOKEN>' with your token.
client = ApifyClient("<YOUR_API_TOKEN>")

# Prepare the Actor input
run_input = {
    "keywords": [
        "food",
        "travel",
    ],
    "resultTypes": [
        "spotlight",
        "lens",
        "topic",
        "user",
    ],
    "includeSpotlightDetails": True,
}

# Run the Actor and wait for it to finish
run = client.actor("crawlerbros/snapchat-search-scraper").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
print("💾 Check your data here: https://console.apify.com/storage/datasets/" + run["defaultDatasetId"])
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# 📚 Want to learn more 📖? Go to → https://docs.apify.com/api/client/python/docs/quick-start

```

## CLI example

```bash
echo '{
  "keywords": [
    "food",
    "travel"
  ],
  "resultTypes": [
    "spotlight",
    "lens",
    "topic",
    "user"
  ],
  "includeSpotlightDetails": true
}' |
apify call crawlerbros/snapchat-search-scraper --silent --output-dataset

```

## MCP server setup

```json
{
    "mcpServers": {
        "apify": {
            "command": "npx",
            "args": [
                "mcp-remote",
                "https://mcp.apify.com/?tools=crawlerbros/snapchat-search-scraper",
                "--header",
                "Authorization: Bearer <YOUR_API_TOKEN>"
            ]
        }
    }
}

```

## OpenAPI specification

Download the OpenAPI definition: https://api.apify.com/v2/actors/l0IJF1Q8GRTyYx5uu/builds/UAbVP5iy9Xm0PRV4u/openapi.json

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/snapchat-search-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
