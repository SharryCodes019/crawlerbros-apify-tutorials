# Snapchat Profile Scraper Tutorial: Run This Apify Actor with Python

Scrape public profile metadata from Snapchat user profiles. Provide usernames or profile URLs and get display name, verification status, subscriber count, bio, avatar, story highlights, related accounts, and external links with one record per username.

This repository shows how to run [Snapchat Profile Scraper](https://apify.com/crawlerbros/snapchat-profile-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/snapchat-profile-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/snapchat-profile-scraper](https://apify.com/crawlerbros/snapchat-profile-scraper)
- **SEO title:** Snapchat Profile Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape public profile metadata from Snapchat user profiles. Provide usernames or profile URLs and get display name, verification status, subscriber count, bio, avatar, story highlights, related accounts, and external links with one record per username.

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

# Snapchat Profile Scraper

Extract complete public profile data from Snapchat — no login, no API key, no manual effort. Get subscriber counts, bio, profile images, Snapcodes, curated highlights, Spotlight videos, AR lenses, active story snaps, related accounts, and AI-generated metadata in one automated run.

Ideal for influencer research, brand monitoring, competitor analysis, marketing intelligence, and social media audits.

---

## What You Get

- Full public profile metadata: display name, bio, subscriber count, verification status, category, website, Snapcode image, business profile ID, and more
- Curated highlight albums with per-snap media URLs and types
- Spotlight highlights with view counts, engagement stats, hashtags, creator info, and AI descriptions
- Active public story snaps with media URLs, geolocation, post timestamps, and sponsorship flags
- AR lenses created by the profile with preview images, unlock URLs, and creator tags
- Embedded Spotlight comments (optional) with reaction counts and commenter details
- Related accounts suggested by Snapchat
- Works on public profiles — no Snapchat account or API key required

---

## Input

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `usernames` | string[] | Yes | — | Snapchat usernames or profile URLs. Accepts: bare username (`brentrivera`), `@brentrivera`, `https://www.snapchat.com/add/brentrivera`, or `https://www.snapchat.com/@brentrivera` |
| `includeLenses` | boolean | No | `true` | Include AR lenses created by the profile owner |
| `includeSpotlightMeta` | boolean | No | `true` | Include rich Spotlight highlight metadata (views, engagement, hashtags, AI title/description) |
| `includeActiveStory` | boolean | No | `true` | Include currently active public story snaps (ephemeral, changes frequently) |
| `includeComments` | boolean | No | `false` | Decode and include Spotlight comments embedded in the profile page |
| `maxRelatedAccounts` | integer | No | *(no limit)* | Cap the number of related accounts returned. Set to `0` to exclude entirely |
| `maxHighlightsPerUser` | integer | No | *(no limit)* | Cap the number of highlights (curated and Spotlight) per profile. Set to `0` to exclude |
| `proxyConfiguration` | object | No | — | Apify proxy settings. Public profiles work without proxy; use for resilience at scale |

### Example Input

```json
{
  "usernames": ["brentrivera", "https://www.snapchat.com/@khaby.lame"],
  "includeLenses": true,
  "includeSpotlightMeta": true,
  "includeActiveStory": true,
  "includeComments": false,
  "maxRelatedAccounts": 5,
  "maxHighlightsPerUser": 10
}
```

---

## Output

Each scraped username produces one record. The schema below lists every possible field; fields that are absent or empty in the source data are omitted from the record.

### Core Profile Fields

| Field | Type | Description |
|-------|------|-------------|
| `username` | string | Snapchat username |
| `displayName` | string | Public display name |
| `accountType` | string | `"public"` or `"private"` |
| `isVerified` | boolean | Whether the account has a verification badge |
| `subscriberCount` | integer | Total subscriber / follower count |
| `bio` | string | Profile bio text |
| `profileUrl` | string | Full Snapchat profile URL |
| `profilePictureUrl` | string | Profile picture URL |
| `snapcodeImageUrl` | string | Snapcode image URL |
| `squareHeroImageUrl` | string | Square hero image for the profile |
| `websiteUrl` | string | External website linked on the profile |
| `category` | string | Primary content category (e.g. `"ENTERTAINMENT"`) |
| `subcategory` | string | Sub-category string ID |
| `publisherType` | string | Publisher type identifier |
| `businessProfileId` | string | Business profile identifier |
| `hostUserId` | string | Host user ID |
| `shouldHideUsername` | boolean | Whether Snapchat hides the username in UI |
| `address` | string | Physical address (creator/business profiles) |
| `mutableName` | string | Mutable display name |
| `primaryColor` | string | Hex color code for profile theming |
| `hasStory` | boolean | Whether the profile has an active story |
| `hasCuratedHighlights` | boolean | Whether the profile has saved highlight albums |
| `hasSpotlightHighlights` | boolean | Whether the profile has Spotlight videos |
| `createdAt` | string | Account creation timestamp (ISO 8601 UTC) |
| `lastUpdatedAt` | string | Last profile update timestamp (ISO 8601 UTC) |
| `sameAsLinks` | array | Cross-platform profile links (raw API array) |
| `scrapedAt` | string | Scrape timestamp (ISO 8601 UTC) |

### Curated Highlights (`curatedHighlights[]`)

Populated when `hasCuratedHighlights` is true.

| Field | Type | Description |
|-------|------|-------------|
| `highlightId` | string | Unique highlight album ID |
| `storyTitle` | string | Album title |
| `thumbnailUrl` | string | Album thumbnail image URL |
| `snapCount` | integer | Number of snaps in the album |
| `firstSnapUrl` | string | Media URL of the first snap |
| `firstSnapType` | string | `"video"` or `"image"` |

### Spotlight Highlights (`spotlightHighlights[]`)

Populated when `hasSpotlightHighlights` is true.

| Field | Type | Description |
|-------|------|-------------|
| `highlightId` | string | Unique Spotlight story ID |
| `storyTitle` | string | Spotlight story title |
| `thumbnailUrl` | string | Thumbnail image URL |
| `snapCount` | integer | Number of snaps in the story |
| `firstSnapUrl` | string | Media URL of the first snap |
| `firstSnapType` | string | `"video"` or `"image"` |

### AR Lenses (`lenses[]`)

Populated when `includeLenses` is true and the profile has created lenses.

| Field | Type | Description |
|-------|------|-------------|
| `scannableUuid` | string | Unique scannable UUID for the lens |
| `lensName` | string | Lens display name |
| `lensCreatorDisplayName` | string | Creator display name |
| `lensCreatorUsername` | string | Creator Snapchat username |
| `lensId` | string | Internal lens ID |
| `lensPreviewImageUrl` | string | Static preview image URL |
| `lensPreviewVideoUrl` | string | Animated preview video URL |
| `iconUrl` | string | Lens icon URL |
| `unlockUrl` | string | Deep link to unlock/open the lens |
| `userProfileUrl` | string | Creator profile URL |
| `lensCreatorSearchTags` | string[] | Searchable tags for the lens |
| `isOfficialSnapLens` | boolean | Whether this is an official Snapchat lens |
| `lastUpdatedAt` | string | Last update timestamp (ISO 8601 UTC) |
| `lensUrl` | string | Public lens page URL |

### Spotlight Metadata (`spotlightMetadata[]`)

Populated when `includeSpotlightMeta` is true and the profile has Spotlight videos.

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Video name/title |
| `thumbnailUrl` | string | Thumbnail image URL |
| `contentUrl` | string | Video content URL |
| `uploadedAt` | string | Upload timestamp (ISO 8601 UTC) |
| `durationMs` | integer | Video duration in milliseconds |
| `width` | integer | Video width in pixels |
| `height` | integer | Video height in pixels |
| `keywords` | string[] | Keyword tags from video metadata |
| `viewCount` | integer | Total view count |
| `shareCount` | integer | Total share count |
| `embeddedTextCaption` | string | Text overlaid on the video |
| `creatorUsername` | string | Creator's Snapchat username |
| `creatorDisplayName` | string | Creator's display name |
| `creatorFollowerCount` | integer | Creator's follower count |
| `creatorWebsiteUrl` | string | Creator's website URL |
| `engagementViewCount` | integer | Engagement-level view count |
| `engagementShareCount` | integer | Engagement-level share count |
| `engagementCommentCount` | integer | Engagement-level comment count |
| `engagementBoostCount` | integer | Engagement-level boost count |
| `engagementRecommendCount` | integer | Engagement-level recommend count |
| `llmDescription` | string | AI-generated description |
| `llmTitle` | string | AI-generated title |
| `llmKeywords` | string[] | AI-generated keywords |
| `textMetadataKeywords` | string[] | Keywords extracted from video text |
| `hashtags` | string[] | Hashtags associated with the video |
| `s2iTags` | string[] | Scene-to-interest tags |
| `contextCards` | object[] | Context card objects (links, locations, etc.) |
| `detectedLanguages` | object[] | Detected language scores |

### Active Story Snaps (`activeStorySnaps[]`)

Populated when `includeActiveStory` is true and the profile has an active story.

| Field | Type | Description |
|-------|------|-------------|
| `snapIndex` | integer | Position index of the snap in the story |
| `snapId` | string | Unique snap ID |
| `mediaUrl` | string | Direct media URL (video or image) |
| `mediaPreviewUrl` | string | Low-resolution preview URL |
| `mediaType` | string | `"video"` or `"image"` |
| `postedAt` | string | Snap post timestamp (ISO 8601 UTC) |
| `snapTitle` | string | Snap title/caption |
| `lat` | number | Latitude (if geotagged) |
| `lng` | number | Longitude (if geotagged) |
| `hasAttachment` | boolean | Whether the snap has an external link attachment |
| `audioTranscriptionObjectUrl` | string | URL to audio transcription object |
| `isSponsored` | boolean | Whether the snap is sponsored content |
| `storySource` | string | Always `"activeStory"` for this section |

### Spotlight Comments (`spotlightComments[]`)

Populated when `includeComments` is true and comments are embedded in the page.

| Field | Type | Description |
|-------|------|-------------|
| `commentId` | string | Unique comment ID (highBits-lowBits format) |
| `snapId` | string | The snap this comment belongs to |
| `replyText` | string | Comment text |
| `reactionCounts` | object[] | Array of `{reactTypeId, count}` objects |
| `commenterDisplayName` | string | Commenter's display name |
| `commenterBitmojiAvatarId` | string | Commenter's Bitmoji avatar ID |
| `commenterBitmojiSelfieId` | string | Commenter's Bitmoji selfie ID |
| `commenterProfileLogoUrl` | string | Commenter's profile image URL |
| `approvalState` | integer | Approval/moderation state |
| `postedAt` | string | Comment timestamp (ISO 8601 UTC) |
| `rankingScore` | number | Comment ranking score |
| `threadedReplyCount` | integer | Number of threaded replies |
| `reportCount` | integer | Number of reports on the comment |

### Related Accounts (`relatedAccounts[]`)

Snapchat-suggested accounts similar to the scraped profile.

| Field | Type | Description |
|-------|------|-------------|
| `username` | string | Snapchat username |
| `displayName` | string | Display name |
| `profileUrl` | string | Full profile URL |
| `profilePictureUrl` | string | Profile picture URL |
| `isVerified` | boolean | Verification badge status |
| `subscriberCount` | integer | Subscriber count |
| `bio` | string | Bio text |
| `snapcodeImageUrl` | string | Snapcode image URL |
| `category` | string | Content category |
| `websiteUrl` | string | External website URL |
| `hasStory` | boolean | Whether the account has an active story |
| `hasCuratedHighlights` | boolean | Whether the account has highlight albums |
| `hasSpotlightHighlights` | boolean | Whether the account has Spotlight videos |
| `subscribeLink` | object | Subscribe deep-link URLs (`oneLinkBaseUrl`, `deepLinkUrl`, `iosAppStoreUrl`) |

### Pagination Cursors (`cursors`)

| Field | Type | Description |
|-------|------|-------------|
| `curatedHighlightsCursor` | string | Cursor for fetching more curated highlights |
| `spotlightHighlightsCursor` | string | Cursor for fetching more Spotlight highlights |
| `lensCursor` | string | Cursor for fetching more lenses |

### Error Records

When a username cannot be scraped, an error record is pushed instead.

| Field | Type | Description |
|-------|------|-------------|
| `inputUsername` | string | The original input value that failed |
| `error` | string | Human-readable error description |
| `scrapedAt` | string | Timestamp of the failed attempt (ISO 8601 UTC) |

---

## Example Output

```json
{
  "username": "brentrivera",
  "displayName": "Brent Rivera",
  "accountType": "public",
  "isVerified": true,
  "subscriberCount": 15200000,
  "bio": "Content creator, filmmaker, and entertainer.",
  "profileUrl": "https://www.snapchat.com/@brentrivera",
  "profilePictureUrl": "https://cf-st.sc-cdn.net/img/dr/brentrivera.jpg",
  "snapcodeImageUrl": "https://app.snapchat.com/web/deeplink/snapcode?username=brentrivera&type=SVG",
  "websiteUrl": "https://brentrivera.com",
  "category": "ENTERTAINMENT",
  "hasStory": true,
  "hasCuratedHighlights": true,
  "hasSpotlightHighlights": true,
  "createdAt": "2015-09-12T14:23:00+00:00",
  "lastUpdatedAt": "2026-06-20T08:10:00+00:00",
  "curatedHighlights": [
    {
      "highlightId": "ab12cd34",
      "storyTitle": "Summer Vlogs",
      "thumbnailUrl": "https://cf-st.sc-cdn.net/thumb/summer.jpg",
      "snapCount": 14,
      "firstSnapUrl": "https://cf-st.sc-cdn.net/video/snap1.mp4",
      "firstSnapType": "video"
    }
  ],
  "spotlightMetadata": [
    {
      "name": "Beach day with the crew",
      "thumbnailUrl": "https://cf-st.sc-cdn.net/thumb/beach.jpg",
      "contentUrl": "https://cf-st.sc-cdn.net/video/beach.mp4",
      "uploadedAt": "2026-06-15T18:30:00+00:00",
      "durationMs": 14500,
      "width": 1080,
      "height": 1920,
      "viewCount": 832400,
      "shareCount": 12300,
      "hashtags": ["summer", "beach"],
      "llmTitle": "Fun beach day with friends",
      "llmDescription": "A creator and friends enjoy a sunny beach afternoon.",
      "llmKeywords": ["beach", "summer", "friends", "fun"]
    }
  ],
  "activeStorySnaps": [
    {
      "snapIndex": 0,
      "snapId": "xyzSnap123",
      "mediaUrl": "https://cf-st.sc-cdn.net/video/story1.mp4",
      "mediaType": "video",
      "postedAt": "2026-06-28T09:00:00+00:00",
      "hasAttachment": false,
      "isSponsored": false,
      "storySource": "activeStory"
    }
  ],
  "relatedAccounts": [
    {
      "username": "lexi",
      "displayName": "Lexi Rivera",
      "profileUrl": "https://www.snapchat.com/@lexi",
      "isVerified": true,
      "subscriberCount": 9800000,
      "hasStory": false,
      "hasCuratedHighlights": true,
      "hasSpotlightHighlights": true
    }
  ],
  "scrapedAt": "2026-06-28T12:00:00+00:00"
}
```

---

## FAQ

**Do I need a Snapchat account or API key?**
No. The scraper fetches public profile pages using standard HTTP requests. No login, cookies, or Snapchat API credentials are required.

**Can I scrape private profiles?**
Private profiles return a minimal record with `accountType: "private"`, `username`, and `displayName` only. Highlights, lenses, and story snaps are not available for private accounts.

**How many profiles can I scrape per run?**
You can pass dozens or hundreds of usernames in a single run. Each profile is fetched concurrently with automatic retries for reliability.

**Are video and image URLs permanent?**
Media URLs (story snaps, highlight thumbnails, Spotlight video content) are served from Snapchat's CDN and may contain expiring tokens. Download or cache media promptly after scraping.

**What does `includeSpotlightMeta` add?**
When enabled, each Spotlight video gets enriched with view counts, share counts, engagement stats, AI-generated titles and descriptions, detected hashtags, scene-to-interest tags, and context cards. This data comes from Snapchat's server-rendered metadata embedded in the profile page.

**What is the `activeStoryMeta` object on a record?**
Some profiles include story-level metadata such as `storyTitle`, `storySubtitle`, `emoji`, and `canonicalUrlSuffix`. These are injected as an `activeStoryMeta` object at the top level of the profile record when present.

**Why are some fields missing from certain records?**
The scraper only outputs fields that contain actual data. Fields that are empty, null, or absent in the source page are omitted. This keeps records clean and avoids sentinel values.

---

## Other Snapchat Scrapers

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

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/snapchat-profile-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
