# Google Flights Scraper Tutorial: Run This Apify Actor with Python

Scrape Google Flights search results with price, airline, departure/arrival times, duration, stops. One-way + round-trip + cabin class + airline filters: maxLayoverMinutes, directOnly, excludeBasicEconomy.

This repository shows how to run [Google Flights Scraper](https://apify.com/crawlerbros/google-flights-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-flights-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/google-flights-scraper](https://apify.com/crawlerbros/google-flights-scraper)
- **SEO title:** Google Flights Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Google Flights search results with price, airline, departure/arrival times, duration, stops. One-way + round-trip + cabin class + airline filters: maxLayoverMinutes, directOnly, excludeBasicEconomy.

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

# Google Flights Scraper

Search Google Flights and emit one structured record per flight option — price, airline, departure/arrival times, duration, and stop count. One-way and round-trip in 4 cabin classes. Pro filters narrow the result set to exactly the flights you want.

## What this actor does

- Builds a Google Flights search URL from your airports + dates + cabin class
- Drives a headless Chromium (Playwright) through Apify residential proxy
- Dismisses cookie banners and "Show more flights" buttons
- Parses each flight option from the rendered DOM aria-labels
- Applies Pro filters (airline, stops, layover, duration, fare type)
- Emits one record per flight option

## Output per flight option

- `price` (integer, normalised to your `currency` input), `currency`
- `airline` (display name), `airlineCode` (IATA, when resolvable)
- `flightNumber` (when extractable)
- `departureAirport` (IATA), `departureTime`
- `arrivalAirport` (IATA), `arrivalTime`
- `durationMinutes`, `pricePerHour` (derived)
- `stops`
- `cabin`, `outboundDate`, `returnDate` (echoed from input)
- `priceBelowThreshold` — only when `priceAlertThresholdUsd` is set
- `recordType: "flight"`, `scrapedAt`

Empty fields are omitted from the output (no nulls).

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `originAirport` | string | `JFK` | Origin IATA (3 letters) |
| `destinationAirport` | string | `LHR` | Destination IATA |
| `outboundDate` | string | 30 days ahead | Departure date `YYYY-MM-DD` |
| `returnDate` | string | – | Return date — empty for one-way |
| `adults` | int | `1` | Adult passengers (1–9) |
| `children` | int | `0` | Child passengers (0–9) |
| `infants` | int | `0` | Infant passengers (0–9) |
| `cabinClass` | enum | `economy` | `economy` / `premium_economy` / `business` / `first` |
| `currency` | enum | `USD` | Display currency |
| `language` | enum | `en` | Google Flights UI language |
| `country` | enum | `US` | `gl` country code |
| `maxStops` | enum | `any` | `any` / `nonstop` / `one_stop` / `two_or_fewer` |
| `airlines` | array | `[]` | IATA airline allowlist (e.g. `["UA","DL"]`) |
| `excludeAirlines` | array | `[]` | IATA airline blocklist |
| `maxResults` | int | `50` | Hard cap on emitted records |
| `minPrice` | int | – | Drop flights below this price (in chosen `currency`) |
| `maxPrice` | int | – | Drop flights above this price |
| `directOnly` | bool | `false` | Alias for `maxStops=nonstop` |
| `maxLayoverMinutes` | int | – | Drop connections with a layover longer than this |
| `maxDurationMinutes` | int | – | Drop flights longer than this many minutes |
| `excludeBasicEconomy` | bool | `false` | Drop fares labelled Basic / Light / Saver |
| `priceAlertThresholdUsd` | number | – | Tag flights at-or-below this price with `priceBelowThreshold: true` |
| `useApifyProxy` | bool | `true` | Route through Apify residential proxy (recommended) |

### Example: cheapest round-trip JFK → LHR

```json
{
  "originAirport": "JFK",
  "destinationAirport": "LHR",
  "outboundDate": "2026-06-15",
  "returnDate": "2026-06-22",
  "cabinClass": "economy",
  "directOnly": true,
  "maxResults": 25
}
```

### Example: business-class SFO → HND with airline allowlist

```json
{
  "originAirport": "SFO",
  "destinationAirport": "HND",
  "outboundDate": "2026-09-10",
  "returnDate": "2026-09-25",
  "cabinClass": "business",
  "airlines": ["NH", "JL", "UA"],
  "maxLayoverMinutes": 240
}
```

### Example: one-way budget search with price alert

```json
{
  "originAirport": "LAX",
  "destinationAirport": "MEX",
  "outboundDate": "2026-04-30",
  "cabinClass": "economy",
  "maxResults": 50,
  "priceAlertThresholdUsd": 200
}
```

## Use cases

- **Travel-deal alerts** — daily run with `priceAlertThresholdUsd`, push the matched flights to Slack
- **Corporate travel benchmarking** — weekly export of business-class prices on key routes
- **Price-tracking dashboards** — feed each flight option into a time-series store
- **Itinerary planning** — combine with a hotel scraper for end-to-end trip cost
- **Frequent-flyer comparison** — enrich with our `flight-award-scraper-pro` to compare cash vs. miles

## FAQ

**Does it require a login or cookies?**  No.

**Why does it need an Apify residential proxy?**  Google rate-limits cloud datacenter IPs aggressively on Flights URLs — without a residential exit you'll typically hit a 429 or captcha. The actor uses Apify residential by default.

**Why is `airlineCode` sometimes missing?**  Some airlines aren't in our name → IATA lookup yet (we cover ~50 carriers). The display name is always populated when extracted; the code is best-effort.

**Why does the run sometimes return 0 flights?**  Causes (in order of likelihood): (1) Google captcha blocked the page (rotate proxy and retry), (2) the route has no flights on those dates, (3) every flight was filtered out by your Pro filters, (4) Google's DOM changed faster than our extraction. The status message tells you which.

**Are multi-city itineraries supported?**  Not in this MVP. Use multiple separate runs with different origin/destination/date pairs.

**Can I get a direct booking link?**  Booking-deeplink resolution is on the roadmap — Google Flights routes booking through an OTA selector that requires deeper interaction. The current actor returns the price/airline/duration/stops you need to make booking decisions.

**What's the difference between `economy` and `excludeBasicEconomy`?**  `cabinClass=economy` searches the economy cabin (covers Basic, Main, and Premium variants). `excludeBasicEconomy` drops the cheapest fares within that cabin (those labelled Basic / Light / Saver) — useful when you want a reliable Main Cabin baseline.

**Is the price guaranteed?**  No. Google Flights prices are advisory; the actual price is set by the airline / OTA at booking time. We capture the displayed price at scrape time.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-flights-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
