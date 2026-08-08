# Postman API Network Scraper Tutorial: Run This Apify Actor with Python

Scrape the Postman Public API Network - search public collections, workspaces, and API publishers, browse by curated category, or list everything published by a given publisher. No auth, no proxy required.

This repository shows how to run [Postman API Network Scraper](https://apify.com/crawlerbros/postman-api-network-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/postman-api-network-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/postman-api-network-scraper](https://apify.com/crawlerbros/postman-api-network-scraper)
- **SEO title:** Postman API Network Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape the Postman Public API Network - search public collections, workspaces, and API publishers, browse by curated category, or list everything published by a given publisher. No auth, no proxy required.

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

# Postman API Network Scraper

Scrape the [Postman Public API Network](https://www.postman.com/explore) — the directory of publicly shared Postman collections, workspaces, and API publishers (Stripe, PayPal, Twilio, and thousands more). Search by keyword, browse by curated category, or list everything a given publisher has shared. No auth, no proxy, no cookies required.

## What this actor does

- **Three modes:** `search`, `byCategory`, `byPublisher`
- **Search** across collections, workspaces, and publisher profiles by free-text query
- **Sort search results** by relevance, most-viewed, or recently-updated
- **Browse** any of the 12 curated Postman API Network categories (Payments, AI, DevOps, etc.)
- **List** every public collection and workspace published by a given team/publisher handle
- **Fork / view / watch counts** and endpoint counts on every collection
- **Empty fields are omitted**

## Output per item

- `itemType` — `collection`, `workspace`, or `publisher`
- `name`, `summary`, `description`
- `categories[]`
- `publisherName`, `publisherHandle`, `publisherVerified`, `publisherLogo`
- `endpointCount` — number of API requests in the collection (`mode=search` only)
- `forkCount`, `viewCount`, `watchCount`
- `forkCountLast30Days`, `viewCountLast30Days`, `watchCountLast30Days` — trailing-30-day engagement (`byCategory`/`byPublisher` modes only)
- `collectionCount`, `workspaceCount`, `apiCount` — child-entity counts on workspace/publisher records (`mode=search` only)
- `workspaceName` (`mode=search` only), `workspaceSlug`
- `tags[]`
- `updatedAt`, `createdAt`
- `sourceUrl` — canonical postman.com detail page
- `recordType: "postmanApiNetworkItem"`, `scrapedAt`

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | string | `search` | `search` / `byCategory` / `byPublisher` |
| `searchQuery` | string | `stripe` | Free-text query (mode=search) |
| `contentType` | string | `all` | Restrict search to `collection` / `workspace` / `publisher` |
| `sortBy` | string | `relevance` | `relevance` / `mostViewed` / `recentlyUpdated` (mode=search only) |
| `category` | string | `payments` | Curated category slug (mode=byCategory) |
| `publisherHandle` | string | – | Publisher/team handle, e.g. `apilayer` (mode=byPublisher) |
| `minForkCount` | int | – | Drop items with fewer forks than this. Only applies to `collection`/`workspace` items — `publisher` items (teams) have no fork count on Postman's platform and always pass this filter |
| `maxItems` | int | `30` | Hard cap (1–500) |

### Example: search for weather APIs

```json
{
  "mode": "search",
  "searchQuery": "weather",
  "contentType": "collection",
  "maxItems": 50
}
```

### Example: browse the Payments category

```json
{
  "mode": "byCategory",
  "category": "payments",
  "maxItems": 50
}
```

### Example: everything APILayer has published

```json
{
  "mode": "byPublisher",
  "publisherHandle": "apilayer",
  "maxItems": 100
}
```

## Use cases

- **API discovery** — find ready-to-fork Postman collections for a third-party API before writing an SDK
- **Competitive intelligence** — track how many collections/forks/views a competitor's API workspace has
- **Developer relations** — audit what your organization has published to the API Network and how it's trending
- **Category research** — see which providers dominate a vertical (Payments, AI, Travel, etc.)
- **Documentation aggregation** — bulk-collect collection descriptions and endpoint counts for a market map

## FAQ

**What's the Postman API Network?** A public directory where teams publish Postman collections/workspaces so other developers can fork them and start calling an API immediately. See [postman.com/explore](https://www.postman.com/explore).

**Do I need a Postman account or API key?** No. All data comes from Postman's own public, unauthenticated JSON endpoints — the same ones the postman.com website itself calls.

**What's the difference between a collection, a workspace, and a publisher?** A *collection* is a set of API requests (the "endpoints"). A *workspace* is a container that groups one or more collections plus docs/environments. A *publisher* is the team/organization account that owns them.

**Why do some items have no `endpointCount`?** Request counts are only returned by `mode=search`'s collection results; the category/publisher listing endpoints don't include them. `mode=search`'s workspace and publisher-profile results instead expose `collectionCount`/`workspaceCount`/`apiCount`.

**How do I find a publisher's handle?** It's the first path segment of their postman.com URL — e.g. `postman.com/apilayer` → handle `apilayer`. You can also discover handles from the `publisherHandle` field of `search` or `byCategory` results.

**How fresh is the data?** Real-time — every mode reads directly from Postman's live API, the same data the website shows.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/postman-api-network-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
