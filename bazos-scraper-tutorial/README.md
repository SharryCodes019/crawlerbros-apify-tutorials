# Bazos.cz / Bazos.sk / Bazos.at / Bazos.pl Scraper Tutorial: Run This Apify Actor with Python

Search the Bazos classifieds marketplace across CZ (bazos.cz), SK (bazos.sk), AT (bazos.at), and PL (bazos.pl) by keyword. Extract title, price + currency (CZK/EUR/PLN), locality, posted date, listing URL, thumbnail, category, description length. Optional minPrice/maxPrice filter.

This repository shows how to run [Bazos.cz / Bazos.sk / Bazos.at / Bazos.pl Scraper](https://apify.com/crawlerbros/bazos-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/bazos-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/bazos-scraper](https://apify.com/crawlerbros/bazos-scraper)
- **SEO title:** Bazos.cz / Bazos.sk / Bazos.at / Bazos.pl Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Search the Bazos classifieds marketplace across CZ (bazos.cz), SK (bazos.sk), AT (bazos.at), and PL (bazos.pl) by keyword. Extract title, price + currency (CZK/EUR/PLN), locality, posted date, listing URL, thumbnail, category, description length. Optional minPrice/maxPrice filter.

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

# Bazos Classifieds Scraper

Search the [Bazos](https://www.bazos.cz/) classifieds marketplace by keyword and extract every matching listing — title, price, locality, description, photos, and direct listing URL. Supports the Czech (`bazos.cz`), Slovak (`bazos.sk`), Austrian (`bazos.at`), and Polish (`bazos.pl`) variants. HTTP-only — no proxy, no login, no API key.

## What it does

You provide one or more search keywords; the actor runs each as a search on Bazos and returns deduplicated listings across all of them. Per listing it captures:

- **Title** — the headline of the ad
- **Price** — parsed numeric value + currency (CZK or EUR)
- **Locality** — city / district where the seller is based
- **Posted date** — the human-readable date Bazos shows on the listing
- **Description** — the snippet shown on the search-results card
- **Category** — auto-detected from the URL subdomain (`auto`, `mobil`, `reality`, `prace`, `elektro`, …)
- **Listing URL** — direct link to the full ad
- **Thumbnail** — first photo from the listing card

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `keywords` | array of strings (required) | `["iphone"]` | One or more search terms. Each runs as a separate Bazos search; results are deduped by listing URL across keywords. |
| `countryVariant` | enum: `CZ` / `SK` / `AT` / `PL` | `CZ` | Which Bazos to query. CZ → bazos.cz (CZK), SK → bazos.sk (EUR), AT → bazos.at (EUR), PL → bazos.pl (PLN). |
| `maxItems` | integer | `50` (1–1000) | Hard cap on total unique listings emitted across all keywords. |
| `maxPagesPerKeyword` | integer | `5` (1–50) | Per-keyword pagination cap. Each Bazos result page has ~20 listings. |
| `minPrice` | integer (optional) | – | Drop listings priced below this number (client-side filter). Listings without a parsed price are kept. |
| `maxPrice` | integer (optional) | – | Drop listings priced above this number. Listings without a parsed price are kept. |

### Example input

```json
{
  "keywords": ["iphone 15", "macbook pro"],
  "countryVariant": "CZ",
  "maxItems": 100,
  "maxPagesPerKeyword": 5
}
```

## Output

One record per unique listing. Empty fields are omitted (no nulls).

```json
{
  "title": "iPhone 15 Pro 256GB Titanium",
  "description": "Záruka 2 roky, top stav, originální balení.",
  "descriptionLength": 41,
  "price": 24500,
  "currency": "CZK",
  "locality": "Praha 5",
  "postedText": "15.4. 2024",
  "category": "mobil",
  "listingId": "217954459",
  "listingUrl": "https://mobil.bazos.cz/inzerat/217954459/apple-iphone-15-plus-256gb-black.php",
  "thumbnailUrl": "https://mobil.bazos.cz/img/217954459-thumb.jpg",
  "countryVariant": "CZ",
  "matchedKeyword": "iphone 15",
  "scrapedAt": "2024-12-16T14:23:11+00:00"
}
```

### Output fields

- **`title`** — headline of the ad.
- **`description`** — snippet shown on the search-results card (Bazos shows the first ~150 characters of the listing body).
- **`descriptionLength`** — derived character count of `description` (handy for filtering out near-empty listings).
- **`price`** — integer amount; absent when the seller selected "Dohodou" (negotiable) or "Zdarma" (free).
- **`currency`** — `"CZK"` for bazos.cz, `"EUR"` for bazos.sk and bazos.at, `"PLN"` for bazos.pl; absent when `price` is absent.
- **`locality`** — seller's city / district as shown on Bazos.
- **`postedText`** — Bazos's human-readable post date (e.g. `"15.4. 2024"`).
- **`category`** — Bazos's subdomain category: `auto`, `mobil`, `reality`, `prace`, `elektro`, `dum`, `hudba`, etc. Derived from the listing URL.
- **`listingId`** — Bazos's stable numeric ID for the listing.
- **`listingUrl`** — direct URL of the full ad.
- **`thumbnailUrl`** — first photo from the listing card (when present).
- **`countryVariant`** — `"CZ"`, `"SK"`, `"AT"`, or `"PL"`, matching the input.
- **`matchedKeyword`** — the search term that surfaced this listing.
- **`scrapedAt`** — ISO-8601 timestamp of extraction.

## Use cases

- **Lead generation** — track second-hand iPhone / car / property listings as they appear.
- **Price intelligence** — monitor average asking prices for a category across a marketplace.
- **Inventory enrichment** — populate a price-comparison or aggregator with Bazos's reach across CZ and SK.
- **Reseller research** — find listings whose locality matches your operating area.

## FAQ

**Does it need cookies, login, or proxy?**
No. Bazos search results are public; the actor uses a Chrome User-Agent and connects directly.

**How does pagination work?**
Bazos serves ~20 listings per page using a `crz` offset (page 2 = `crz=20`, page 3 = `crz=40`, etc.). The actor walks pages 1 through `maxPagesPerKeyword` for each keyword, stopping early if a page returns no new listings.

**What if my keyword has no results?**
The actor emits a single record `{"type": "bazos_scraper_error", "reason": "no_listings_found"}` and the run completes successfully (empty datasets aren't treated as failures). Try a broader keyword or switch the country variant.

**Can I search multiple Bazos variants in one run?**
Run the actor once per variant (CZ / SK / AT / PL). The data shapes are identical; you can merge the resulting datasets in your pipeline.

**Why are some listings missing prices?**
Bazos lets sellers list "Dohodou" (price negotiable) or "Zdarma" (free) instead of a number. In those cases `price` and `currency` are omitted from the record (per the omit-empty contract).

**Why don't I see the seller's phone number?**
Bazos requires a click-through and a CAPTCHA-like reveal step on the detail page; this scraper only walks the search-results page, which is fast and reliable. Contact details are out of scope.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/bazos-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
