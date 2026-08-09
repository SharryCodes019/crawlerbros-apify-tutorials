# IAAI Salvage Vehicle Auctions Scraper Tutorial: Run This Apify Actor with Python

Scrape IAAI (Insurance Auto Auctions) salvage and insurance vehicle listings. Search by keyword/VIN/stock #, make/model/year, or browse by damage type, location, and title type - VIN, odometer, damage, sale date, images, and more.

This repository shows how to run [IAAI Salvage Vehicle Auctions Scraper](https://apify.com/crawlerbros/iaai-salvage-vehicle-auctions-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/iaai-salvage-vehicle-auctions-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/iaai-salvage-vehicle-auctions-scraper](https://apify.com/crawlerbros/iaai-salvage-vehicle-auctions-scraper)
- **SEO title:** IAAI Salvage Vehicle Auctions Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape IAAI (Insurance Auto Auctions) salvage and insurance vehicle listings. Search by keyword/VIN/stock #, make/model/year, or browse by damage type, location, and title type - VIN, odometer, damage, sale date, images, and more.

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

# IAAI Salvage Vehicle Auctions Scraper

Scrape [IAAI](https://www.iaai.com) (Insurance Auto Auctions) salvage and insurance vehicle listings — search by keyword, VIN, or stock number; search by make/model/year; or browse by damage type, location, and title type. Get VIN, odometer, primary/secondary damage, loss type, title/sale document type, sale date, actual cash value, images, and more. No login, no cookies, no paid proxy required.

## What this actor does

- **Five modes:** `search` (keyword/VIN/stock #), `byMakeModel` (make/model/year), `byDamageType`, `byLocation` (state/branch), `byTitleType`
- **Combinable filters:** any optional filter (damage type, loss type, title type, state, branch, vehicle type, auction type, buyer eligibility, year range, odometer, actual cash value) can be layered onto any mode
- **Rich per-vehicle data:** VIN, year/make/model/trim, damage, odometer, colors, engine, transmission, drivetrain, body style, branch/location, sale date, current Buy Now price, actual cash value, and photo
- **Empty fields are omitted**

## Output per vehicle

- `lotId`, `stockNumber`, `vin` (see VIN note in Limitations below)
- `year`, `make`, `model`, `trim`, `title`
- `primaryDamage`, `secondaryDamage`, `lossType`, `titleType`
- `odometer`, `odometerUnit` (`mi` or `km` — Canadian-branch listings report kilometers), `odometerDisclosure` (e.g. `Not Actual`, `Not Required/Exempt`, `Exceeds Mechanical Limits` — only present when IAAI flags the reading; absence means a standard actual reading)
- `vehicleType`, `vehicleSubType`, `bodyStyle`, `startCode`, `airbags`, `key`
- `exteriorColor`, `interiorColor`, `engine`, `fuelType`, `cylinders`, `transmission`, `driveLineType`, `countryOfOrigin`
- `branch`, `region`, `market`, `laneRun`, `aisleStall`, `vehicleLocation`
- `actualCashValue`, `buyNowPrice`, `currency` (`USD` or `CAD`)
- `newInventoryDateTime`, `saleDateTime`, `saleListUrl`
- `imageUrl`, `detailUrl`, `sourceUrl`
- `recordType: "vehicle"`, `scrapedAt`

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | string | `search` | `search` / `byMakeModel` / `byDamageType` / `byLocation` / `byTitleType` |
| `searchQuery` | string | `Honda` | Keyword, VIN, or stock number (mode=search) |
| `make` | string | – | Vehicle make (mode=byMakeModel, or extra filter anywhere) |
| `model` | string | – | Vehicle model (narrows `make`) |
| `yearMin` / `yearMax` | int | – | Model-year range |
| `damageType` | select | – | Primary damage taxonomy (mode=byDamageType, or extra filter anywhere) |
| `lossType` | select | – | Insurance loss category |
| `titleType` | select | – | Title/sale document type (mode=byTitleType, or extra filter anywhere) |
| `state` | select | – | US state / Canadian province (mode=byLocation, or extra filter anywhere) |
| `branch` | select | – | Specific IAAI auction branch (mode=byLocation, or extra filter anywhere) |
| `vehicleType` | select | – | High-level vehicle category |
| `auctionType` | select | – | Live / Timed / Buy Now |
| `whoCanBuy` | select | – | Buyer-eligibility category |
| `odometerMax` | int | – | Drop vehicles above this odometer reading |
| `acvMax` | int | – | Drop vehicles above this actual cash value (USD) |
| `maxItems` | int | `20` | Hard cap on emitted records (1–1000) |

### Example: search by keyword

```json
{
  "mode": "search",
  "searchQuery": "Honda Accord",
  "maxItems": 25
}
```

### Example: search by make/model/year

```json
{
  "mode": "byMakeModel",
  "make": "Toyota",
  "model": "Camry",
  "yearMin": 2015,
  "yearMax": 2020,
  "maxItems": 50
}
```

### Example: browse flood-damage vehicles in Texas

```json
{
  "mode": "byDamageType",
  "damageType": "Flood",
  "state": "Texas",
  "maxItems": 50
}
```

### Example: browse a specific auction branch

```json
{
  "mode": "byLocation",
  "branch": "Dallas",
  "maxItems": 50
}
```

### Example: clean-title vehicles only

```json
{
  "mode": "byTitleType",
  "titleType": "Clear",
  "maxItems": 50
}
```

## Use cases

- **Salvage & rebuilder sourcing** — find vehicles by damage type, title status, and location for parts or rebuild
- **Cross-platform arbitrage** — compare IAAI listings against other salvage auction sources
- **Insurance & total-loss research** — analyze damage-type and loss-type distribution by region
- **Export & dealer buying** — filter by buyer-eligibility category and branch to plan pickup logistics
- **Market analysis** — track actual cash value vs. current bid/Buy Now price across makes and model years

## Data Source / Limitations

- IAAI's public search page is scraped directly (no official API is used). All fields shown are those visible to an anonymous, non-logged-in visitor.
- **VIN is partially masked** for anonymous visitors (e.g. `1HGCM55864A******`) — the last several characters are hidden until you register and log in as a bidder on iaai.com. This actor does not use login credentials, so VINs are reported exactly as IAAI displays them publicly.
- **Seller name** is hidden behind a "Please log in as a buyer" prompt for anonymous visitors and is not included in the output.
- Current bid amounts for live/timed auctions in progress are not shown to anonymous visitors; `buyNowPrice` is included when a listing has a Buy Now option.
- Listing availability reflects IAAI's live inventory at scrape time — sold or removed vehicles will no longer appear.
- **Canadian coverage**: native IAAI Canada listings (e.g. Toronto, Montreal, Vancouver, Edmonton branches) are fully supported with correct `km`/`CAD` units. A small share of results filtered by a Canadian **province** (`state`) alone, without a `branch`, keyword, or make/model, come from a third-party auction partner's inventory cross-listed inside IAAI's search UI under a different page template that this actor does not parse (to avoid mixing in another company's catalog) — for reliable Canada-wide coverage, filter by `branch` or combine `state` with a keyword/make.

## FAQ

**Do I need an IAAI account?** No. This actor only reads data visible on the public search page.

**Why is the VIN partially hidden?** IAAI masks part of the VIN for visitors who aren't logged in as a registered bidder. This is a platform limitation, not a scraping issue.

**Can I combine filters, e.g. damage type + state + year range?** Yes — every optional filter field can be combined with any mode. For example, set `mode=byDamageType`, `damageType=Hail`, `state=Texas`, and `yearMin=2018` together.

**What does `titleType` mean?** It reflects the title or sale document IAAI will issue for the vehicle — e.g. `Salvage`, `Clear` (clean), `Non-Repairable`, `Repairable`, or `Bill Of Sale`.

**How many results can I get per run?** Set `maxItems` up to 1000. Larger requests take longer since IAAI serves up to 100 listings per page.

**Does this work outside the US?** Yes — IAAI's `state` filter includes both US states and Canadian provinces, and `branch` includes both US and Canadian auction locations.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/iaai-salvage-vehicle-auctions-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
