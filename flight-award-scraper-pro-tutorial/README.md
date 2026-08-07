# Flight Award Mileage Chart Scraper Tutorial: Run This Apify Actor with Python

Look up published award redemption rates (miles + taxes) between any two regions across major frequent-flyer programs (Aeroplan, British Airways Avios, LifeMiles, United, Flying Blue, etc.). Returns real chart values from each issuer's public page.

This repository shows how to run [Flight Award Mileage Chart Scraper](https://apify.com/crawlerbros/flight-award-scraper-pro) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/flight-award-scraper-pro`
- **Apify Store:** [https://apify.com/crawlerbros/flight-award-scraper-pro](https://apify.com/crawlerbros/flight-award-scraper-pro)
- **SEO title:** Flight Award Mileage Chart Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Look up published award redemption rates (miles + taxes) between any two regions across major frequent-flyer programs (Aeroplan, British Airways Avios, LifeMiles, United, Flying Blue, etc.). Returns real chart values from each issuer's public page.

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

# Flight Award Mileage Chart Scraper

Compare published award redemption rates between world regions across major airline loyalty programs. This actor returns static chart values from public mileage-chart sources - not live seat availability.

## What you get

Each row is a published chart rate, for example:

```json
{
  "recordType": "mileage_chart",
  "issuer": "aeroplan",
  "issuerName": "Air Canada Aeroplan",
  "originRegion": "north_america",
  "destinationRegion": "europe",
  "cabin": "business",
  "miles": 70000,
  "milesOneWay": 35000,
  "isPartner": false,
  "milesNote": "Distance band: Atlantic Zone (NA <-> Europe)",
  "sourceUrl": "https://www.aircanada.com/.../aeroplan-flight-reward-chart.html",
  "scrapedAt": "2026-04-30T14:00:00+00:00"
}
```

Empty fields are omitted.

## Supported issuers

Currently implemented:

- `aeroplan`
- `alaska`
- `american`
- `anaMileage`
- `britishAirways`
- `emirates`
- `flyingBlue`
- `lifemiles`
- `lufthansa`
- `qatar`
- `singaporeKrisflyer`
- `united`
- `virginAtlantic`

Accepted in the input schema but not yet implemented:

- `aeromexico`
- `azul`
- `copa`
- `delta`
- `etihad`
- `finnair`
- `jal`
- `qantas`
- `sas`
- `turkishMilesAndSmiles`

If you include an unsupported issuer, the actor skips it cleanly and emits no placeholder rows for it.

## Input

| Field | Type | Default |
|---|---|---|
| `originRegion` | enum | `north_america` |
| `destinationRegion` | enum | `europe` |
| `cabin` | enum | `business` |
| `issuers` | array | 13 implemented issuers preselected |
| `oneWay` | boolean | `false` |
| `partnerOnly` | boolean | `false` |
| `maxResults` | integer | `100` |

### Example input

```json
{
  "originRegion": "north_america",
  "destinationRegion": "europe",
  "cabin": "business",
  "oneWay": true,
  "partnerOnly": true,
  "issuers": ["aeroplan", "united", "virginAtlantic"]
}
```

## Output fields

- `issuer`, `issuerName`
- `originRegion`, `destinationRegion`
- `cabin`
- `miles`, `milesOneWay`
- `isPartner`, `partnerName`
- `milesNote`
- `taxes_min_usd`, `taxes_max_usd`
- `sourceUrl`
- `scrapedAt`

## FAQ

**Is this live award availability?**  
No. It is the published mileage chart.

**Why did some selected issuers return no rows?**  
Some issuers are still exposed in the input schema before their adapter is implemented. Those issuers are skipped cleanly for now.

**Why include `sourceUrl`?**  
Each row carries the publisher page used for that chart so you can verify the rate against the airline's public source.

**What happens with `partnerOnly=true`?**  
The actor keeps only partner-redemption rows when a program publishes a distinct partner rate.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/flight-award-scraper-pro)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
