# Fuel Prices Scraper Tutorial: Run This Apify Actor with Python

Daily US fuel prices (regular, mid-grade, premium, diesel) at national, state, and metro level. HTTP-only, no proxy, no auth. Filters: states allowlist, fuelTypes, minPrice/maxPrice, sortBy. Source: AAA Fuel Gauge.

This repository shows how to run [Fuel Prices Scraper](https://apify.com/crawlerbros/fuel-prices-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/fuel-prices-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/fuel-prices-scraper](https://apify.com/crawlerbros/fuel-prices-scraper)
- **SEO title:** Fuel Prices Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Daily US fuel prices (regular, mid-grade, premium, diesel) at national, state, and metro level. HTTP-only, no proxy, no auth. Filters: states allowlist, fuelTypes, minPrice/maxPrice, sortBy. Source: AAA Fuel Gauge.

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

# Fuel Prices Scraper

Daily US fuel prices from the [AAA Fuel Gauge](https://gasprices.aaa.com/). National, state (50 + DC), and metro/county averages for regular, mid-grade, premium, and diesel — with current/yesterday/week/month/year-ago history. HTTP-only — no cookies, no proxy, no auth.

## What this actor does

- Fetches the public AAA Fuel Gauge pages
- Parses national, state, and metro-level fuel prices
- Returns one record per scope (1 national / 51 state / hundreds of metro records)
- Includes price history (yesterday / week ago / month ago / year ago) and derived change metrics (in cents)
- Pro filters narrow output to specific states, fuel types, price bands, or metro substring matches

## Modes

| Mode | What it does |
|---|---|
| `national` | 1 record — current US national average for all 4 fuel grades |
| `state` (default) | 51 records — current + history for each of 50 states + DC |
| `metro` | Per-state metro/county tables (~200+ records when no state filter is set) |

## Output per record

State / metro records include:

- `scope` (`national` / `state` / `metro`)
- `country` (national only — always `US`)
- `state`, `stateCode` (state and metro records)
- `metro` (metro records only)
- `regular`, `midGrade`, `premium`, `diesel` (USD/gal — only fuels actually published)
- `history` (object — `yesterday` / `weekAgo` / `monthAgo` / `yearAgo` × fuel grade)
- `changeFromYesterday`, `changeFromWeekAgo`, `changeFromMonthAgo`, `changeFromYearAgo` (cents — computed from `primaryFuelType`, default `regular`)
- `recordType: "fuelPrices"`, `scrapedAt`

Empty fields are omitted from the output (no nulls).

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | enum | `state` | `national` / `state` / `metro` |
| `states` | array | `[]` | Two-letter state codes or full names — e.g. `["NY","CA"]` or `["New York","California"]`. Empty = all 50 + DC |
| `fuelTypes` | array | all four | Subset of `regular` / `midGrade` / `premium` / `diesel`. Drops other grades from each record |
| `includeHistory` | bool | `true` | Include yesterday/week-ago/month-ago/year-ago averages |
| `includeChangeMetrics` | bool | `true` | Compute `changeFromYesterday` etc. (in cents) for the primary fuel |
| `minPrice` | number | – | Drop records whose primary fuel is below this price |
| `maxPrice` | number | – | Drop records whose primary fuel is above this price |
| `primaryFuelType` | enum | `regular` | Which fuel grade `minPrice`/`maxPrice`/sort/change use |
| `sortBy` | enum | `state_asc` | `price_asc` / `price_desc` / `state_asc` |
| `metroNameFilter` | array | `[]` | Only emit metro records whose name contains one of these substrings (case-insensitive) |
| `maxItems` | int | `500` | Hard cap on emitted records |

### Example: state averages

```json
{
  "mode": "state",
  "states": [],
  "includeHistory": true,
  "includeChangeMetrics": true,
  "sortBy": "price_asc"
}
```

### Example: metros in NY + CA

```json
{
  "mode": "metro",
  "states": ["NY", "CA"],
  "metroNameFilter": ["new york", "los angeles", "san francisco"]
}
```

### Example: cheapest diesel by state

```json
{
  "mode": "state",
  "primaryFuelType": "diesel",
  "fuelTypes": ["diesel"],
  "sortBy": "price_asc",
  "maxItems": 10
}
```

## Use cases

- **Fleet planning** — compare diesel prices across states for routing
- **News + editorial** — daily "where gas is cheapest" digest, broken out by state and metro
- **Consumer apps** — power a "national fuel price" widget with one daily run
- **Trend tracking** — monitor `changeFromYearAgo` to flag big YoY moves
- **Inflation dashboards** — fuel is a leading retail-inflation indicator

## FAQ

**Does it require a login or cookies?**  No. The AAA Fuel Gauge is fully public.

**Is a proxy needed?**  No. Datacenter IPs work fine.

**Does it cover countries other than the US?**  Not yet. AAA's Fuel Gauge is US-only.

**Why aren't station-level (per-pump) prices included?**  Per-station data sources (e.g. GasBuddy) are heavily rate-limited and blocked from datacenter IPs. State + metro aggregates from AAA are the most reliable, free, datacenter-friendly source.

**How fresh is the data?**  AAA updates daily (overnight). The actor reads the page directly so each run reflects the latest published averages.

**Why do some states miss a fuel grade?**  Some states don't publish every grade. The omit-empty contract drops missing fields rather than emit nulls.

**Why is `changeFromMonthAgo` sometimes missing?**  It's computed only when both current price and the relevant history bucket are present.

**What does `metroNameFilter` match against?**  Case-insensitive substring of the metro/county name as published by AAA (e.g. `Albany-Schenectady-Troy`, `Nassau-Suffolk`).

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/fuel-prices-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
