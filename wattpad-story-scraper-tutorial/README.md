# Wattpad Story Scraper Tutorial: Run This Apify Actor with Python

Scrape Wattpad stories - search by keyword, browse by genre or tag, fetch full story metadata and chapter lists by ID, list a user's stories, or pull full chapter text.

This repository shows how to run [Wattpad Story Scraper](https://apify.com/crawlerbros/wattpad-story-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/wattpad-story-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/wattpad-story-scraper](https://apify.com/crawlerbros/wattpad-story-scraper)
- **SEO title:** Wattpad Story Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Wattpad stories - search by keyword, browse by genre or tag, fetch full story metadata and chapter lists by ID, list a user's stories, or pull full chapter text.

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

# Wattpad Story Scraper

Scrape Wattpad — the world's largest social storytelling platform, home to hundreds of millions of stories across romance, fantasy, fanfiction, horror, and more. Search by keyword, browse by genre or tag, pull full story metadata and chapter lists by ID, list everything a writer has published, or extract full chapter text. No login, no API key, no proxy required.

## What this actor does

- **Six modes:** `search`, `byCategory`, `byTag`, `byIds`, `byUser`, `chapterText`
- **22 genres and 26 languages** exposed as ready-to-pick dropdowns
- **Recently-updated feed** — narrow a genre browse to newly-updated stories via `feed: "new"`
- **Author profile enrichment** — `byUser` results include the author's bio, location, follower/following counts, votes received, and join date
- **Full chapter text extraction** — clean, readable plain text with paragraph breaks preserved
- **Rich filters** — completed-only, free-only, mature-content toggle, minimum votes/reads
- **Client-side sort** — most votes, most reads, most comments, or newest first
- **Empty fields are omitted** — every record only contains data Wattpad actually returned

## Output per story

- `storyId`, `title`, `description`
- `authorUsername`, `authorUrl`, `authorFullname`, `authorAvatarUrl`, `authorVerified` (detail mode)
- `authorBio`, `authorLocation`, `authorGender`, `authorFollowers`, `authorFollowing`, `authorVotesReceived`, `authorNumStoriesPublished`, `authorNumLists`, `authorVerifiedEmail`, `authorAmbassador`, `authorJoinedAt`, `authorWebsite`, `authorFacebook`, `authorBackgroundUrl`, `authorDeeplink` (mode=`byUser` only — from the author's public profile)
- `categories[]` — genre names (e.g. `Romance`, `Werewolf`, `Fanfiction`)
- `tags[]` — free-form community tags
- `language`, `languageId`
- `completed`, `mature`, `isPaywalled`, `paidModel`
- `numParts`, `storyLength`, `voteCount`, `readCount`, `commentCount`
- `coverUrl`, `storyUrl`
- `createdAt`, `modifiedAt`, `lastUpdatedAt`, `firstPublishedAt` (detail mode)
- `chapters[]` — full chapter list with `partId`, `title`, `url`, `length`, `voteCount`, `readCount`, `commentCount` (detail mode, `byIds`)
- `copyrightCode` (detail mode)
- `recordType: "story"`, `scrapedAt`

## Output per chapter (mode=`chapterText`)

- `partId`, `storyId`, `chapterTitle`, `chapterUrl`, `storyUrl`
- `chapterText` — full plain-text chapter body
- `wordCount`, `characterLength`
- `voteCount`, `readCount`, `commentCount`, `draft`
- `publishedAt`, `updatedAt`
- `recordType: "chapter"`, `scrapedAt`

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | string | `search` | `search` / `byCategory` / `byTag` / `byIds` / `byUser` / `chapterText` |
| `searchQuery` | string | `romance` | Free-text query (mode=search) |
| `category` | select | – | Genre filter; required for mode=byCategory |
| `language` | select | – | Language filter |
| `tags` | array | `["werewolf"]` | Tags to browse (mode=byTag) |
| `storyIds` | array | – | Story IDs or URLs (mode=byIds) |
| `username` | string | – | Wattpad username (mode=byUser) |
| `partIds` | array | – | Chapter IDs or URLs (mode=chapterText) |
| `completedOnly` | bool | `false` | Only finished stories |
| `freeOnly` | bool | `false` | Exclude coin-paywalled stories |
| `includeMatureContent` | bool | `true` | Include author-flagged mature stories |
| `minVotes` | int | – | Minimum vote count |
| `minReads` | int | – | Minimum read count |
| `sortBy` | select | `relevance` | `relevance` / `mostVotes` / `mostReads` / `mostCommented` / `newest` |
| `feed` | select | – | mode=byCategory only: blank = Wattpad's default (most-popular) ordering, `new` = recently-updated stories in that genre |
| `maxItems` | int | `20` | Hard cap (1–500) |

### Example: browse a genre, most-voted first

```json
{
  "mode": "byCategory",
  "category": "4",
  "language": "1",
  "sortBy": "mostVotes",
  "maxItems": 50
}
```

### Example: full story detail + chapter list

```json
{
  "mode": "byIds",
  "storyIds": ["358371807", "https://www.wattpad.com/story/105872-a-and-d"]
}
```

### Example: extract a chapter's full text

```json
{
  "mode": "chapterText",
  "partIds": ["1406121589"]
}
```

## Use cases

- **Reading apps** — build genre/tag-based discovery feeds from real Wattpad catalog data
- **Content research** — analyze trending tags, tropes, and genre popularity
- **Fandom / fanfiction analytics** — track fanfiction volume and engagement by fandom tag
- **Archival / backup** — export a story's full chapter text for offline reading or preservation
- **Writer intelligence** — pull an author's full bibliography with engagement metrics
- **NLP / dataset building** — collect long-form narrative text at scale for language research

## FAQ

**Do I need a Wattpad account or cookies?**  No. Search, story metadata, chapter lists, and chapter text are all public and readable without logging in.

**What does the `mature` flag mean?**  It's Wattpad's own author-self-reported content flag, not a moderation verdict. It's exposed as-is and can be filtered out via `includeMatureContent: false`; note it is self-reported and not exhaustive — some explicit stories are not flagged by their authors.

**What happens with mature-gated or removed stories?**  A small share of stories are gated behind Wattpad's in-app mature-content confirmation or have been taken down; these resolve with 0 records for that ID rather than partial/garbage data, and the run reports which IDs were not found.

**Why is `sortBy` applied "client-side"?**  Wattpad's own `sort` search parameter isn't consistently honored by their API, so the actor fetches the requested batch and re-orders it locally by votes/reads/comments/date — giving you a real, working sort instead of a parameter that silently does nothing.

**Can I look up a story from just its URL?**  Yes — `storyIds` and `partIds` both accept full Wattpad URLs as well as bare numeric IDs.

**What's the difference between `byIds` and `search`?**  `byIds` returns full detail (chapter list, author profile fields, copyright code) for exact known stories. `search`/`byCategory`/`byTag` return lighter list-view records for discovery.

**How many chapters can I extract at once?**  Up to `maxItems` (max 500) `partIds` per run — each chapter is a separate output record with full text.

**Will `storyUrl`/`chapterUrl` links open for me?**  Yes, in a normal web browser — Wattpad is one of the most-visited fiction sites in the world and these are its standard canonical links. All actual data extraction in this actor goes through Wattpad's own API host, not the web-app pages the links point to.

**Is content available in languages other than English?**  Yes — 26 languages are supported as a filter, from Spanish and Portuguese to Arabic, Hindi, Vietnamese, and more.

## Limitations

- **No "hot"/trending filter** — Wattpad's own `filter=hot` parameter is a documented no-op that returns the exact same ordering as no filter at all (verified by direct comparison), so it isn't exposed as a separate option. Wattpad's default `byCategory` ordering already is the popularity/"hot" ordering. `feed=new` is the one server-side feed filter that's verified to actually change results.
- **`feed` only applies to `byCategory`** — the `filter` query parameter is silently ignored by Wattpad's search endpoint (used by `search` and `byTag`), confirmed by comparing identical result sets with and without it. Applying it there would silently do nothing, so it's scoped to `byCategory` only, where it's confirmed effective.
- **No comments extraction** — every public comments endpoint tried (`/v4/story_parts/{id}/comments`, `/v5/...`, `/api/v3/story_parts/{id}/comments`) returns 400/404 without an authenticated session; `commentCount` is still exposed on every story/chapter, but comment text itself isn't reliably retrievable without login.
- **No curated reading lists** — Wattpad's "lists" feature (`/v4/story-lists`, `/api/v3/lists`) requires an authenticated session (returns 400 anonymously) and isn't exposed.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/wattpad-story-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
