# 17Track Package Tracking Scraper Tutorial: Run This Apify Actor with Python

Multi-carrier package tracking via 17track.net - track packages from FedEx, UPS, USPS, DHL, Amazon, and 2,300+ carriers worldwide. Get tracking events, status, estimated delivery, and carrier information.

This repository shows how to run [17Track Package Tracking Scraper](https://apify.com/crawlerbros/seventeen-track-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/seventeen-track-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/seventeen-track-scraper](https://apify.com/crawlerbros/seventeen-track-scraper)
- **SEO title:** 17Track Package Tracking Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Multi-carrier package tracking via 17track.net - track packages from FedEx, UPS, USPS, DHL, Amazon, and 2,300+ carriers worldwide. Get tracking events, status, estimated delivery, and carrier information.

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

# 17Track Package Tracking Scraper

Track packages from 2,300+ carriers worldwide using [17track.net](https://www.17track.net/). Get full tracking event timelines, delivery status, estimated delivery dates, and carrier information for USPS, FedEx, UPS, DHL, Amazon, and hundreds more carriers.

## Features

- **Track single package** — full tracking history for one tracking number
- **Bulk track** — track multiple packages in a single run
- **Carrier search** — browse 40+ supported major carriers with details and websites

## Input

| Field | Type | Description |
|-------|------|-------------|
| `mode` | select | `trackPackage`, `bulkTrack`, `carrierSearch` |
| `trackingNumbers` | array | Tracking numbers to track |
| `carrier` | select | Optional carrier hint for faster lookup (e.g. `fedex`, `ups`, `usps`) |
| `query` | string | Search term for `carrierSearch` mode |
| `maxItems` | integer | Maximum records (default: 10) |

## Output (Tracking Records)

| Field | Description |
|-------|-------------|
| `trackingNumber` | Package tracking number |
| `carrier` | Carrier name |
| `carrierCode` | Carrier code |
| `status` | Current tracking status |
| `lastEvent` | Most recent tracking event description |
| `lastLocation` | Most recent location |
| `lastEventDate` | Date/time of last event |
| `estimatedDelivery` | Estimated delivery date |
| `originCountry` | Origin country |
| `destinationCountry` | Destination country |
| `events` | Full list of tracking events (date, description, location) |
| `trackingUrl` | Direct link to tracking on 17track.net |
| `scrapedAt` | ISO timestamp |

## Supported Carriers (selection)

| Carrier | Code |
|---------|------|
| USPS | `usps` |
| FedEx | `fedex` |
| UPS | `ups` |
| DHL | `dhl` |
| Amazon Logistics | `amazon` |
| Royal Mail | `royal-mail` |
| Canada Post | `canada-post` |
| Deutsche Post | `deutsche-post` |
| Australia Post | `australia-post` |
| Japan Post | `japan-post` |
| SF Express | `sf-express` |
| Cainiao | `cainiao` |

## Example Input

```json
{
  "mode": "bulkTrack",
  "trackingNumbers": ["92001902358200000000000006", "1Z999AA10123456784"],
  "carrier": "usps"
}
```

## Example Output

```json
{
  "trackingNumber": "92001902358200000000000006",
  "carrier": "United States Postal Service (USPS)",
  "carrierCode": "usps",
  "status": "In Transit",
  "lastEvent": "In Transit to Next Facility",
  "lastLocation": "Memphis, TN",
  "estimatedDelivery": "2026-06-03",
  "events": [
    {
      "date": "2026-06-01T14:32:00",
      "description": "In Transit to Next Facility",
      "location": "Memphis, TN"
    }
  ],
  "trackingUrl": "https://www.17track.net/en/track#92001902358200000000000006",
  "scrapedAt": "2026-06-02T10:00:00+00:00"
}
```

## FAQs

**How many carriers does 17track support?**
17track.net supports 2,300+ carriers worldwide including all major couriers and postal services.

**Do I need a 17track API key?**
The scraper attempts to use the public 17track API. For high-volume commercial tracking, you may need a 17track API key (available at https://www.17track.net/en/apiservice).

**How do I find my carrier code?**
Use `mode=carrierSearch` to search for carriers by name and find their codes.

**What tracking number formats are supported?**
All standard tracking number formats: USPS (e.g. 9200...006), UPS (1Z...), FedEx (12-15 digits), DHL (10 digits), and more.

**Why might my tracking show 'Lookup via 17track website'?**
If the API doesn't return live data, use the provided `trackingUrl` link to check the status directly on 17track.net.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/seventeen-track-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
