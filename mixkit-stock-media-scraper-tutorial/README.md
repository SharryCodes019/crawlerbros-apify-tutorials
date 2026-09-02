# Mixkit Stock Media Scraper Tutorial: Run This Apify Actor with Python

Scrape free stock videos, background music, and sound effects from mixkit.co - no login, no watermark, no attribution required.

This repository shows how to run [Mixkit Stock Media Scraper](https://apify.com/crawlerbros/mixkit-stock-media-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/mixkit-stock-media-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/mixkit-stock-media-scraper](https://apify.com/crawlerbros/mixkit-stock-media-scraper)
- **SEO title:** Mixkit Stock Media Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape free stock videos, background music, and sound effects from mixkit.co - no login, no watermark, no attribution required.

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

# Mixkit Stock Media Scraper

Scrape **mixkit.co** — free stock videos, background music tracks, and sound effects. No login, no watermark, no attribution required, no paid API key. Get direct, ready-to-download media URLs (up to 4K for video, full-quality MP3 for music, full-quality WAV for sound effects) plus rich metadata: tags, genres, moods, instruments, durations, and license info.

## What this actor does

- **Three media types (`mode`):** `video`, `music`, `soundEffect`
- **Video:** browse by 90+ curated categories (nature, business, animals, food, city, abstract...) or any free-text tag, with resolution (HD / Full HD / 4K) and orientation (horizontal / vertical) filters
- **Music:** browse by genre (100+), mood (100+), or featured instrument (28)
- **Sound effects:** browse by 260+ categories (impact, ambience, UI, animals, weapons, nature, household...)
- **Direct download URLs** — every record includes a direct, publicly-accessible media file URL (mp4 / mp3 / wav), no scraping the site again required
- **Duration & keyword filters** apply across all three media types
- **Empty fields are omitted** — every field present in a record is guaranteed to have real data

## Output fields

### Video (`recordType: "video"`)

| Field | Description |
|---|---|
| `videoId` | Mixkit numeric item id |
| `title`, `description` | |
| `tags[]` | Topic tags (e.g. `Tree`, `Ocean`, `Travel`) |
| `durationSeconds`, `duration` | Clip length (seconds and `M:SS`) |
| `uploadDate` | ISO date |
| `license`, `licenseType` | License URL + `free` (commercial use OK) or `restricted` (non-commercial only) |
| `thumbnailUrl` | Static preview image |
| `previewVideoUrl` | Small 360p preview clip |
| `downloadUrl` | Direct MP4 at the highest available resolution |
| `downloadResolution`, `downloadQualityLabel`, `downloadFileSizeMb` | Best-quality details (e.g. `4096x2160`, `4K`, `250.87`) |
| `availableQualities[]` | Quality tiers Mixkit lists for this clip (e.g. `["HD","4K"]`) |
| `maxResolutionTier` | Normalized tier: `hd` / `fullhd` / `4k` |
| `orientation` | `horizontal` / `vertical` / `square` |
| `sourceUrl` | Canonical Mixkit page for the video |

### Music (`recordType: "music"`)

| Field | Description |
|---|---|
| `trackId`, `title`, `artist` | |
| `genres[]`, `moods[]`, `instruments[]`, `tags[]` | Mixkit's music taxonomy |
| `durationSeconds`, `duration` | |
| `downloadUrl` | Direct full-quality MP3 |
| `waveformUrl` | JSON waveform peak data (for building a visual player) |
| `sourceUrl` | The Mixkit listing page the track was found on |

### Sound effect (`recordType: "soundEffect"`)

| Field | Description |
|---|---|
| `sfxId`, `title` | |
| `categories[]` | e.g. `["Whoosh", "Impact"]` |
| `durationSeconds`, `duration` | |
| `previewUrl` | Compressed MP3 preview |
| `downloadUrl` | Direct full-quality WAV |
| `waveformUrl` | JSON waveform peak data |
| `sourceUrl` | The Mixkit listing page the effect was found on |

Every record also has `recordType` and `scrapedAt` (UTC ISO timestamp).

## Input

| Field | Type | Applies to | Description |
|---|---|---|---|
| `mode` | select | all | `video` / `music` / `soundEffect` |
| `searchQuery` | string | all | Full-text search across Mixkit's real site search (title/tags/description), e.g. `coffee shop`, `lofi piano`, `whoosh`. Overrides all category/genre/mood/instrument/tag filters when set — often returns a broader/different result set than category browsing |
| `videoCategory` | select | video | Curated category (90+ options), or `(none)` for latest |
| `customTag` | string | video | Free-text tag override, e.g. `coffee-shop`, `drone-shot` — takes priority over `videoCategory` |
| `resolutionFilter` | select | video | `any` / `hd` / `fullhd` / `4k` — minimum resolution required |
| `orientationFilter` | select | video | `any` / `horizontal` / `vertical` |
| `musicGenre` | select | music | 100+ genres. Takes priority over mood/instrument/tag |
| `musicMood` | select | music | 100+ moods. Used only if genre is `(none)` |
| `musicInstrument` | select | music | 28 instruments. Used only if genre and mood are both `(none)` |
| `musicTag` | string | music | Free-text mood/topic tag override, e.g. `action`, `christmas`, `arabic` — hundreds of options at `/free-stock-music/tag/{tag}/`, a separate browse axis from genre/mood/instrument. Used only if genre, mood, and instrument are all `(none)` |
| `sfxCategory` | select | soundEffect | 260+ categories, or `(none)` for latest |
| `minDurationSeconds` / `maxDurationSeconds` | integer | all | Duration filter |
| `containsKeyword` | string | all | Case-insensitive match against title / description / artist / tags |
| `maxItems` | integer | all | Hard cap on emitted records (1–1000, default 30) |

### Example: 4K vertical nature clips

```json
{
  "mode": "video",
  "videoCategory": "sea",
  "resolutionFilter": "4k",
  "orientationFilter": "vertical",
  "maxItems": 20
}
```

### Example: full-text search across sound effects

```json
{
  "mode": "soundEffect",
  "searchQuery": "whoosh",
  "maxItems": 15
}
```

### Example: upbeat cinematic background music

```json
{
  "mode": "music",
  "musicMood": "uplifting",
  "musicGenre": "cinematic",
  "minDurationSeconds": 60,
  "maxItems": 25
}
```

### Example: explosion / impact sound effects

```json
{
  "mode": "soundEffect",
  "sfxCategory": "explosion",
  "maxItems": 30
}
```

### Example: free-text video tag not in the curated list

```json
{
  "mode": "video",
  "customTag": "coffee-shop",
  "maxItems": 15
}
```

## Use cases

- **Video editors / YouTubers** — bulk-source royalty-free B-roll by category or resolution
- **Podcasters / video creators** — build a music/SFX library by genre and mood without manual browsing
- **App/game developers** — pull sound-effect libraries by category (UI, weapons, impacts)
- **Content pipelines** — feed direct download URLs into an automated video-assembly workflow
- **Media asset cataloging** — mirror Mixkit's tag/genre/mood taxonomy into your own DAM system

## FAQ

**Do I need a Mixkit account or API key?**  No. Everything on Mixkit is free to browse and download without login; this actor doesn't use cookies, an API key, or a paid proxy.

**Can I use the downloads commercially?**  Check the `licenseType` field per video. `free` clips are cleared for commercial use (YouTube, marketing, ads). `restricted` clips are for non-commercial/personal use only. Music and sound effects are royalty-free for both commercial and personal use per Mixkit's audio license. Always double-check [mixkit.co/license](https://mixkit.co/license/) for the current terms.

**Why do some videos have `maxResolutionTier: "hd"` while others reach `4k`?**  Not every Mixkit clip is filmed/exported at 4K. The actor reports whatever the highest resolution Mixkit actually offers for that specific clip is — it never fabricates a resolution.

**What's the difference between `videoCategory`, `customTag`, and `searchQuery`?**  `videoCategory` is a curated dropdown of Mixkit's ~90 official categories. `customTag` lets you target any of Mixkit's thousands of granular tags (e.g. `waterfall`, `night-sky`) that aren't in the curated list — just type the tag as it appears in a Mixkit URL. `searchQuery` hits Mixkit's real full-text search box instead of a category/tag page, and can return a broader or different result set (it matches across titles/descriptions/tags, not just one tag).

**Why does `musicGenre` take priority over `musicMood`/`musicInstrument`?**  Mixkit's site only supports browsing by one taxonomy axis at a time. Set only the one you want to filter by; leave the others as `(none)`.

**How fresh is the data?**  Mixkit adds new videos, tracks, and sound effects continuously. Since this actor scrapes live pages on every run, results always reflect Mixkit's current catalog.

**Are `downloadUrl` links stable / hotlinkable?**  Yes — they point directly at Mixkit's `assets.mixkit.co` CDN and require no authentication, cookies, or special headers to fetch.

## Limitations

- **`resolutionFilter`/`orientationFilter` only match videos with confirmed resolution data.** Mixkit's video detail page occasionally serves a lighter page variant that omits the resolution picker (title/description/tags are unaffected). Rather than guess, the actor excludes any video where resolution/orientation can't be confirmed when you've set one of these filters to something other than "any" — you'll never get a false match, but a narrow combo (e.g. `4k` + `vertical`) can return 0 results if Mixkit doesn't currently have — or momentarily doesn't serve — a confirmed match. Mixkit also publishes very few (if any) 4K **vertical** clips in most categories — most vertical/social-format clips top out at Full HD.
- Vertical/portrait Mixkit videos are almost always capped at Full HD (1080×1920); true 4K is mainly available on horizontal clips.
- Music and sound-effect records don't have a per-item Mixkit detail page, so `sourceUrl` points at the category listing page the track/effect was found on rather than a unique per-item URL.
- Mixkit's on-site "Sort: Popular / Newest" control is client-side only (no query-string parameter changes server-rendered order across `?sort=`, `?facet-sort=`, or Turbo-Frame requests we tested) — the actor returns Mixkit's default listing order for every category, which cannot be reliably overridden without full browser automation.
- **The "latest/all" browse (any mode, with no category/genre/mood/instrument/tag/`searchQuery` set) caps out at a single listing page — ~40 videos, ~36 music tracks, ~46 sound effects.** Confirmed live: `?page=2` on the uncategorised listing for every mode returns the exact same items as `?page=1` — Mixkit's own site doesn't paginate these "no filter" listings. Pick a category/genre/mood/instrument/tag (or `searchQuery`) to browse beyond that first page; category, genre, mood, instrument, tag, and search listings all paginate normally. If you request more than this cap with no filter set, the actor's `statusMessage` explains why the run returned fewer records than `maxItems`.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/mixkit-stock-media-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
