# VesselFinder Scraper Tutorial: Run This Apify Actor with Python

Scrape real-time AIS vessel tracking data from VesselFinder.com - search by vessel name, look up by IMO or MMSI number, or find vessels near a port. Returns vessel type, flag, dimensions, position, speed, destination, and more.

This repository shows how to run [VesselFinder Scraper](https://apify.com/crawlerbros/vessel-finder-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/vessel-finder-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/vessel-finder-scraper](https://apify.com/crawlerbros/vessel-finder-scraper)
- **SEO title:** VesselFinder Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape real-time AIS vessel tracking data from VesselFinder.com - search by vessel name, look up by IMO or MMSI number, or find vessels near a port. Returns vessel type, flag, dimensions, position, speed, destination, and more.

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

# VesselFinder Scraper

Extract real-time AIS vessel tracking data from [VesselFinder.com](https://www.vesselfinder.com/) — the free public vessel tracking platform powered by the global Automatic Identification System (AIS).

## What This Scraper Does

This actor searches and retrieves vessel information including vessel identity, type, flag, physical dimensions, current position, speed, destination, and ETA. It supports four operating modes to suit different use cases.

## Use Cases

- **Maritime intelligence** — track specific vessels by IMO or MMSI
- **Fleet monitoring** — search all vessels matching a carrier name (e.g. "MSC", "Maersk")
- **Port analytics** — find vessels associated with a specific port
- **Shipping research** — collect AIS metadata for bulk vessel datasets

## Input

| Field | Type | Description |
|-------|------|-------------|
| `mode` | string | Operating mode: `search`, `byIMO`, `byMmsi`, or `byPort` |
| `searchQuery` | string | Vessel name or partial name (mode=search) |
| `imoNumbers` | array | List of IMO numbers (mode=byIMO) |
| `mmsiNumbers` | array | List of MMSI numbers (mode=byMmsi) |
| `portName` | string | Port name to search nearby vessels (mode=byPort) |
| `maxItems` | integer | Max records to emit (1–200, default 10) |

### Example Input

```json
{
  "mode": "search",
  "searchQuery": "MSC",
  "maxItems": 5
}
```

## Output

Each record contains:

| Field | Description |
|-------|-------------|
| `vesselName` | Official vessel name |
| `imoNumber` | IMO identification number |
| `mmsi` | MMSI radio identifier |
| `vesselType` | Ship type (e.g. Container Ship, Tanker) |
| `flag` | Country of registration |
| `callSign` | Radio call sign |
| `length` | Length overall in metres |
| `width` | Beam in metres |
| `grossTonnage` | Gross tonnage (GT) |
| `deadweight` | Deadweight tonnage (DWT) |
| `draught` | Current draught in metres |
| `speed` | Current speed in knots |
| `course` | Current course in degrees |
| `destination` | Reported destination port |
| `eta` | Estimated time of arrival |
| `status` | AIS navigation status |
| `lastSeen` | When position was last received |
| `posLat` | Latitude |
| `posLon` | Longitude |
| `imageUrl` | Ship photo URL |
| `vesselUrl` | VesselFinder vessel page URL |
| `sourceUrl` | URL scraped |
| `scrapedAt` | ISO timestamp |
| `recordType` | Always `vessel` |

### Example Output

```json
{
  "vesselName": "MSC AAYA",
  "imoNumber": "9927263",
  "mmsi": "636021770",
  "vesselType": "Container Ship",
  "flag": "Liberia",
  "callSign": "5LFP3",
  "length": 366.0,
  "width": 51.0,
  "grossTonnage": 150783,
  "deadweight": 180428,
  "vesselUrl": "https://www.vesselfinder.com/vessels/details/9927263",
  "recordType": "vessel"
}
```

## Frequently Asked Questions

**What is AIS data?**
AIS (Automatic Identification System) is a maritime tracking system that broadcasts vessel position, identity, and voyage data. VesselFinder aggregates this public AIS data.

**Is authentication required?**
No. VesselFinder's public vessel pages are freely accessible.

**How fresh is the data?**
VesselFinder updates vessel positions as AIS signals are received — typically every few minutes for vessels in coverage areas.

**What vessel types are covered?**
All vessel types: container ships, tankers, bulk carriers, ferries, fishing vessels, yachts, and more.

**How do I find a vessel's IMO number?**
Use `mode=search` with the vessel name to find its IMO/MMSI, then use `mode=byIMO` for direct lookup.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/vessel-finder-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
