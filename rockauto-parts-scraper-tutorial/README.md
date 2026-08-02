# RockAuto Parts Scraper Tutorial: Run This Apify Actor with Python

Search RockAuto.com, the largest free public US auto-parts catalogue by keyword or part number. Returns manufacturer, part number, category, price, core charge, pack size, and Info-page URL per listing. HTTP-only, no proxy, no API key, no login.

This repository shows how to run [RockAuto Parts Scraper](https://apify.com/crawlerbros/rockauto-parts-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/rockauto-parts-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/rockauto-parts-scraper](https://apify.com/crawlerbros/rockauto-parts-scraper)
- **SEO title:** RockAuto Parts Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Search RockAuto.com, the largest free public US auto-parts catalogue by keyword or part number. Returns manufacturer, part number, category, price, core charge, pack size, and Info-page URL per listing. HTTP-only, no proxy, no API key, no login.

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

# RockAuto Parts Scraper

Search [RockAuto.com](https://www.rockauto.com) — the largest free public US auto-parts catalogue — by keyword or part number. Each query returns up to ~50 listings with manufacturer, part number, category, price, core charge, total, pack size, and Info-page URL. HTTP-only with automatic Apify residential-proxy fallback when RockAuto's bot-protection CAPTCHA fires (no proxy input needed).

## What it does

You provide one or more search queries; the actor:

1. Submits each query to `rockauto.com/en/partsearch/` and parses the result page.
2. Auto-detects RockAuto's CAPTCHA challenge page and retries the request through Apify residential proxy with a fresh session — eliminates the false-empty results that would otherwise come from datacenter-IP throttling.
3. Filters by manufacturer / category / price range (client-side).
4. Dedupes across queries by `(manufacturer, partNumber)` so no part appears twice.

Each part is one record. Empty fields are omitted (no nulls).

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `queries` | array of strings (required) | `["brake pads"]` | Search terms — part numbers, brand names, category keywords. E.g. `BREMBO P28004`, `oil filter`, `brake pads`. Each runs as a separate RockAuto search. |
| `manufacturerFilter` | string | – | Only emit records whose manufacturer matches this substring (case-insensitive). E.g. `BOSCH`. |
| `categoryFilter` | string | – | Only emit records whose category matches this substring (case-insensitive). E.g. `Brake Pad`, `Oil Filter`. |
| `minPrice` | number | – | Drop records with price below this amount (USD). Records without a parsed price are kept. |
| `maxPrice` | number | – | Drop records with price above this amount. Records without a parsed price are kept. |
| `maxResults` | integer | `50` (1–500) | Hard cap on parts emitted across all queries (after dedup + filtering). |
| `enrichWithPartDetails` | boolean | `false` | When true, fetch each part's RockAuto detail page (`moreInfoUrl`) and add a `details` block (specs, fitment notes, image URLs). Adds ~1 extra HTTP request per part — slower but richer. |
| `vehicleMake` | string | – | Vehicle-mode: append a make to each query (e.g. `Toyota`). |
| `vehicleModel` | string | – | Vehicle-mode: model (e.g. `Camry`). |
| `vehicleYear` | integer | – | Vehicle-mode: model year (e.g. `2020`). |
| `vehicleEngine` | string | – | Vehicle-mode: engine spec (e.g. `2.5L L4`, `5.7L V8`). |
| `startUrls` | array of strings | `[]` | Paste full RockAuto partsearch URLs (e.g. `https://www.rockauto.com/en/partsearch/?partnum=brake+pads`). Each URL's `partnum` becomes a query. |

### Example input

```json
{
  "queries": ["brake pads", "oil filter"],
  "manufacturerFilter": "BOSCH",
  "categoryFilter": "Brake",
  "minPrice": 5,
  "maxPrice": 100,
  "maxResults": 100
}
```

## Output

One record per unique part. Empty fields are omitted (no nulls).

```json
{
  "manufacturer": "BETTER BRAKE PARTS",
  "partNumber": "5473K",
  "category": "Brake Pad Retaining Clip / Spring",
  "priceUSD": 2.15,
  "totalUSD": 2.15,
  "packSize": 1,
  "moreInfoUrl": "https://www.rockauto.com/en/moreinfo.php?pk=12345&cc=0",
  "notes": "For 2018-2020 Toyota Camry, Front, OEM 5473K",
  "inputQuery": "brake pads",
  "scrapedAt": "2024-12-16T14:23:11+00:00"
}
```

### Output fields

- **`manufacturer`** — brand / manufacturer (e.g. `BREMBO`, `BOSCH`, `MOTORCRAFT`).
- **`partNumber`** — manufacturer's part number.
- **`category`** — RockAuto's part-category label (e.g. `Brake Pad`, `Oil Filter`, `ABS Wheel Speed Sensor`).
- **`priceUSD`** — listing price in USD; absent when RockAuto hides the price (rare).
- **`coreChargeUSD`** — core charge / refundable deposit (USD); absent when 0.
- **`totalUSD`** — `priceUSD + coreChargeUSD`. Always present alongside `priceUSD`.
- **`packSize`** — units per listing (e.g. `4` for a "pack of 4 brake pads"). Defaults to `1` when not specified.
- **`moreInfoUrl`** — direct link to the part's RockAuto detail page (specs, fitment, warranty).
- **`notes`** — fitment / position / OEM cross-reference notes (e.g. `"For 2020 Toyota Camry, Front Left"`).
- **`details`** — (only when `enrichWithPartDetails: true`) nested `{specs, images[], notes}` block parsed from the moreinfo page. Specs is a snake_cased key/value dict (e.g. `{position: "Front", material: "Ceramic", oem_part_number: "5L8Z-2001-AA"}`); `images` is up to 10 product image URLs.
- **`inputQuery`** — the search query that surfaced this part.
- **`scrapedAt`** — ISO-8601 UTC timestamp.

## Use cases

- **Price comparison** — pull every brake-pad listing for a query and compare across brands.
- **Inventory enrichment** — feed your retail / repair-shop tool with RockAuto's catalogue (price, brand, category) for cross-reference.
- **Brand sourcing** — find every part by a specific manufacturer (e.g. `BREMBO`, `MOTORCRAFT`).
- **Category audits** — pull all `Oil Filter` results and analyse price distribution across brands.
- **Part-number lookup** — bulk-resolve 100+ exact part numbers to find current pricing on RockAuto.

## FAQ

**Does it need a proxy?**
Not as input — the actor automatically uses Apify residential proxy as a CAPTCHA fallback. Strategy:

1. **Direct fetch** with realistic Chrome headers (Referer, Accept-Language, Sec-Fetch-*) from Apify's datacenter.
2. **User-supplied premium proxies** (`customProxyUrls` input) — tried sequentially BEFORE Apify's pool. Most useful when RockAuto's WAF has flagged Apify's shared residential IPs for high-traffic keywords.
3. **Apify residential proxy** with up to 5 fresh sessions, each with its own per-session warmup and a jittered 1.5–4.0s delay between attempts.

**Why does my keyword (`headlight`, `alternator`, etc.) sometimes return zero results?**
RockAuto's WAF aggressively CAPTCHAs certain high-traffic single-token keywords across the entire request fingerprint — IP, headers, timing — regardless of how realistic the request looks. The actor tries plural + suffixed variants (`headlight` → `headlights` → `headlight assembly` → `headlight kit` → `headlight bulb`) and rotates through 5 fresh proxy sessions per variant. Some keywords still fail because RockAuto has flagged the entire shared residential block.

**Workarounds when a keyword consistently fails:**

1. **Use a 2-token query directly.** `brake pads`, `oil filter`, `BOSCH headlight assembly`, `air filter` — all reliable.
2. **Supply your own residential proxy** via `customProxyUrls` (premium services like BrightData, Oxylabs, SmartProxy that aren't on RockAuto's blocklist).
3. **Use vehicle-mode** with `vehicleMake` set — appends a make to your query so it's always 2+ tokens.

The actor emits a diagnostic sentinel `{type: "rockauto_scraper_error", reason: "no_results", variantsAttempted: [...]}` listing every variant it tried, so you can see exactly what was attempted.

**How many results per query?**
Up to ~50 per query — RockAuto caps the per-search-page count. For more results, run multiple narrower queries (e.g. `brake pads BMW`, `brake pads Toyota`) instead of one broad one.

**Can I search by vehicle (make / model / year)?**
Yes — set `vehicleMake`, `vehicleModel`, `vehicleYear`, and/or `vehicleEngine`. The actor appends those values to each query in `queries` and tries the most-specific search first, **automatically falling back to progressively shorter queries** if the full query CAPTCHAs or returns no results.

Example with `queries=["brake pads"]`, `vehicleMake="Toyota"`, `vehicleModel="Camry"`, `vehicleYear=2020`, `vehicleEngine="2.5L L4"` — fallback chain:

1. `"brake pads Toyota Camry 2020 2.5L L4"` (full)
2. `"brake pads Toyota Camry 2020"` (drop engine)
3. `"brake pads Toyota Camry"` (drop year)
4. `"brake pads Toyota"` (drop model)
5. `"brake pads"` (drop make — last resort)

The first variant that returns a parseable result page wins. RockAuto's keyword search frequently CAPTCHAs 3+ token queries, so the fallback typically lands at variant 4 (`brake pads Toyota`). The record's `inputQuery` field shows which variant actually matched. This is a keyword-search overlay, not a catalog walker; it works HTTP-only and reuses our partsearch endpoint.

**Why is the price sometimes missing?**
RockAuto hides the price on a small fraction of listings (often discontinued or special-order parts). The `priceUSD` field is omitted in those cases (omit-empty contract).

**What if zero parts match?**
The actor emits a single sentinel record `{type: "rockauto_scraper_error", reason: "no_results"}` so the dataset is non-empty. The run still completes successfully.

**Can I scrape the part detail page?**
This actor focuses on search results. Use the `moreInfoUrl` field with a downstream actor for the part's detail page (specs, photos, warranty terms).

**Are prices in USD?**
Yes. RockAuto's US site (`/en/`) is USD-only. International variants would require a different scraper.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/rockauto-parts-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
