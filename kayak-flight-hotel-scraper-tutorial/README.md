# Kayak Flights, Hotels & Deals Scraper Tutorial: Run This Apify Actor with Python

Scrape flight deals, hotel prices, and explore cheap destinations from Kayak. Search flights between cities, compare prices from hundreds of airlines, and find cheap travel deals

This repository shows how to run [Kayak Flights, Hotels & Deals Scraper](https://apify.com/crawlerbros/kayak-flight-hotel-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/kayak-flight-hotel-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/kayak-flight-hotel-scraper](https://apify.com/crawlerbros/kayak-flight-hotel-scraper)
- **SEO title:** Kayak Flights, Hotels & Deals Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape flight deals, hotel prices, and explore cheap destinations from Kayak. Search flights between cities, compare prices from hundreds of airlines, and find cheap travel deals

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

# Kayak Flights, Hotels & Deals Scraper

Extract flight deals, explore cheap destinations, and compare travel prices from [Kayak](https://www.kayak.com) — one of the world's leading travel search engines. Search flights between cities, compare prices from hundreds of airlines, and discover cheap travel deals from any airport.

## What data does this scraper extract?

| Field | Description |
|-------|-------------|
| `flightId` | Unique flight result identifier |
| `origin` | Origin airport IATA code (e.g., NYC) |
| `destination` | Destination airport IATA code (e.g., LON) |
| `originCity` | Origin city name |
| `destinationCity` | Destination city name |
| `departDate` | Departure date (YYYY-MM-DD) |
| `returnDate` | Return date for round-trips (YYYY-MM-DD) |
| `price` | Best available price (per person) |
| `currency` | Price currency (e.g., USD) |
| `airline` | Primary airline name |
| `airlines` | All airlines involved (for multi-leg flights) |
| `stops` | Number of stops (0 = direct) |
| `duration` | Outbound flight duration (e.g., "7h 30m") |
| `departTime` | Departure datetime (ISO 8601) |
| `arrivalTime` | Arrival datetime (ISO 8601) |
| `cabinClass` | Cabin class (economy/business/etc.) |
| `tripType` | one-way or round-trip |
| `deepLink` | Direct booking URL on Kayak |
| `recordType` | Always "kayakFlight" |
| `scrapedAt` | Timestamp of scraping |

## Input Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `mode` | Select | Scraping mode: searchFlights, searchHotels, exploreDeals, byUrls | `exploreDeals` |
| `origin` | Text | Origin airport IATA code or city (e.g., "NYC", "JFK", "New York") | `NYC` |
| `destination` | Text | Destination IATA code or city (optional for exploreDeals) | — |
| `departDate` | Text | Departure date YYYY-MM-DD | 30 days from now |
| `returnDate` | Text | Return date YYYY-MM-DD | 37 days from now |
| `tripType` | Select | one-way or round-trip | `round-trip` |
| `cabinClass` | Select | economy, premium-economy, business, first | `economy` |
| `adults` | Integer | Number of passengers (1–9) | `1` |
| `maxBudget` | Integer | Max price filter in USD (for exploreDeals) | — |
| `sortBy` | Select | Sort: price, duration, departure, arrival | `price` |
| `startUrls` | List | Kayak search URLs for byUrls mode | — |
| `maxItems` | Integer | Maximum results (1–500) | `50` |

## Modes

### `exploreDeals` (default)
Explore cheap flights from any origin city. Discover hundreds of destinations sorted by price. Perfect for finding travel inspiration and the cheapest places to fly.

### `searchFlights`
Search for specific flights between two cities. Returns a ranked list of flight options with prices from all airlines, including number of stops, duration, and direct booking links.

### `searchHotels`
Search for hotels at a destination. Returns available hotel options with pricing data intercepted from Kayak's internal hotel search API.

### `byUrls`
Scrape specific Kayak search result URLs. Provide pre-built Kayak URLs and extract flight data from those searches.

## Example Input

```json
{
  "mode": "searchFlights",
  "origin": "NYC",
  "destination": "LON",
  "departDate": "2026-08-01",
  "returnDate": "2026-08-15",
  "tripType": "round-trip",
  "cabinClass": "economy",
  "adults": 1,
  "sortBy": "price",
  "maxItems": 50
}
```

## Example Output (Flight)

```json
{
  "flightId": "d83f4b084af600d06a3f8872a5c2351d",
  "origin": "NYC",
  "destination": "LON",
  "originCity": "New York",
  "destinationCity": "London",
  "departDate": "2026-08-01",
  "returnDate": "2026-08-15",
  "price": 543.00,
  "currency": "USD",
  "airline": "British Airways",
  "airlines": ["British Airways"],
  "stops": 0,
  "duration": "6h 55m",
  "departTime": "2026-08-01T19:00:00",
  "arrivalTime": "2026-08-02T07:55:00",
  "cabinClass": "economy",
  "tripType": "round-trip",
  "deepLink": "https://www.kayak.com/book/flight?code=...",
  "recordType": "kayakFlight",
  "scrapedAt": "2026-05-15T10:30:00+00:00"
}
```

## Example Output (Explore Deal)

```json
{
  "flightId": "NYC-CDG",
  "origin": "NYC",
  "destination": "CDG",
  "originCity": "NYC",
  "destinationCity": "Paris",
  "price": 450.00,
  "currency": "USD",
  "country": "France",
  "latitude": 48.8566,
  "longitude": 2.3522,
  "tripType": "round-trip",
  "cabinClass": "economy",
  "recordType": "kayakFlight",
  "scrapedAt": "2026-05-15T10:30:00+00:00"
}
```

## Frequently Asked Questions

**Q: Why does the scraper need to wait 10–15 seconds per page?**
A: Kayak loads flight results asynchronously via a polling API. The scraper intercepts this API call, which typically fires within 10–15 seconds after the page loads. This is normal behavior.

**Q: What is the IATA code format?**
A: IATA codes are 3-letter airport codes (e.g., JFK = John F. Kennedy, LAX = Los Angeles, LHR = London Heathrow). City codes (NYC = New York all airports, LON = London all airports) are also supported.

**Q: How current are the prices?**
A: Prices are fetched in real-time from Kayak's search engine. They reflect the best available fare at the time of scraping and may change within minutes.

**Q: Can I search one-way flights?**
A: Yes. Set `tripType` to `one-way` and provide only `departDate` (no `returnDate` needed).

**Q: What does the `stops` field mean?**
A: `0` = direct flight (nonstop), `1` = one connection, `2` = two connections, etc.

**Q: Can I search flights for multiple passengers?**
A: Yes. Set the `adults` parameter to the number of passengers (1–9). Prices in the output will reflect the per-person fare.

**Q: What is exploreDeals mode best for?**
A: Travel inspiration and finding the cheapest destinations to fly from your city. Set a `maxBudget` to filter destinations within your price range.

**Q: Does this scraper work without a proxy?**
A: For datacenter IPs, Kayak may limit results or require more time to load. A residential proxy is recommended for production use to ensure consistent results.

## Legal Notice

This scraper is intended for legitimate travel research, price monitoring, and data analysis. Please comply with Kayak's Terms of Service when using this tool.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/kayak-flight-hotel-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
