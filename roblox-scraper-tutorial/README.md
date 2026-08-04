# Roblox Scraper Tutorial: Run This Apify Actor with Python

Scrape Roblox, search games by keyword, fetch game details by universe ID, browse trending games, search catalog UGC items, and get user profiles with their published games.

This repository shows how to run [Roblox Scraper](https://apify.com/crawlerbros/roblox-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/roblox-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/roblox-scraper](https://apify.com/crawlerbros/roblox-scraper)
- **SEO title:** Roblox Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Roblox, search games by keyword, fetch game details by universe ID, browse trending games, search catalog UGC items, and get user profiles with their published games.

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

# Roblox Scraper

Scrape public Roblox data — search games by keyword, fetch game details by universe ID, browse trending games, search catalog UGC items, and retrieve user profiles with their published games. Uses Roblox's free public APIs — no authentication or proxy required.

## What you can scrape

- **Game metadata**: name, description, creator, genre, visit count, concurrent players, favorites, thumbnails, and game URLs
- **Catalog items**: UGC assets with pricing, creator info, and item URLs
- **User profiles**: username, display name, bio, and all published games
- **Trending games**: top games by current popularity (visits/players)

## Supported modes

| Mode | Description |
|---|---|
| `searchGames` | Search games by keyword (e.g. "Adopt Me", "Bloxburg") |
| `byGameId` | Fetch 1–50 specific games by comma-separated universe IDs |
| `searchItems` | Search UGC catalog items (hats, accessories, clothing) |
| `byUserId` | Fetch a user's profile + all their published games |
| `trending` | Browse trending/popular games with no keyword filter |

## Input

| Field | Type | Description |
|---|---|---|
| `mode` | select | Scrape mode (default: `searchGames`) |
| `query` | string | Keyword (modes: searchGames, searchItems) |
| `universeIds` | string | Comma-separated universe IDs (mode: byGameId) |
| `userId` | integer | Roblox numeric user ID (mode: byUserId) |
| `genre` | select | Filter games by genre (All, RPG, Funny, Scary, War, Pirate, Building, Sports, etc.) |
| `minVisits` | integer | Only include games with at least N total visits |
| `minPlaying` | integer | Only include games with at least N concurrent players |
| `maxItems` | integer | Maximum records to emit (default: 50) |

### Example input

```json
{
  "mode": "searchGames",
  "query": "Adopt Me",
  "maxItems": 20
}
```

## Output

Each record includes `recordType`, `siteName` = `"Roblox"`, and `scrapedAt` timestamp.

### Game record

```json
{
  "universeId": 189707,
  "rootPlaceId": 6872265039,
  "name": "Adopt Me!",
  "description": "Adopt and raise cute pets...",
  "creator": {
    "id": 537413528,
    "name": "Uplift Games",
    "type": "Group"
  },
  "playing": 120000,
  "visits": 35000000000,
  "maxPlayers": 40,
  "favoritedCount": 20000000,
  "genre": "RPG",
  "isPrivate": false,
  "isFeatured": true,
  "created": "2017-07-14T17:11:52.483Z",
  "updated": "2024-01-15T08:00:00Z",
  "thumbnailUrl": "https://tr.rbxcdn.com/...",
  "gameUrl": "https://www.roblox.com/games/6872265039",
  "recordType": "game",
  "siteName": "Roblox",
  "scrapedAt": "2026-05-10T12:00:00+00:00"
}
```

### Catalog item record

```json
{
  "itemId": 9988282,
  "itemType": "Asset",
  "assetType": "Hat",
  "name": "Bloxburg Helmet",
  "price": 150,
  "creatorName": "ROBLOX",
  "creatorType": "User",
  "itemUrl": "https://www.roblox.com/catalog/9988282",
  "recordType": "catalogItem",
  "siteName": "Roblox",
  "scrapedAt": "2026-05-10T12:00:00+00:00"
}
```

## FAQs

**Does this require a Roblox account or API key?**
No. All data is fetched from Roblox's public APIs which require no authentication.

**What is a universe ID?**
The universe ID is Roblox's internal game identifier. You can find it in the URL of the Roblox game page or via the search API results.

**Can I filter games by genre?**
Yes — use the `genre` select input. Available genres include: All, Tutorial, Funny, Scary, War, Pirate, RPG, Sci-Fi, Building, Sports, Town and City, Fantasy, Adventure, Horror.

**How many items can I scrape per run?**
Up to 1000 records per run (set via `maxItems`). Roblox's search API returns up to 100 games per page.

**What does `minVisits` do?**
It filters out games with fewer total visits than the specified threshold. Useful for finding only popular, established games.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/roblox-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
