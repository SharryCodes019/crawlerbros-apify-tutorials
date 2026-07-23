# Propwire Real Estate Leads Scraper Tutorial: Run This Apify Actor with Python

Extract US real estate leads from propwire.com with 11M+ properties with owner info, equity, MLS data, lead-type flags (absentee owner, vacant, pre-foreclosure, cash buyer, high equity, etc.), and tax records.

This repository shows how to run [Propwire Real Estate Leads Scraper](https://apify.com/crawlerbros/propwire-leads-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/propwire-leads-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/propwire-leads-scraper](https://apify.com/crawlerbros/propwire-leads-scraper)
- **SEO title:** Propwire Real Estate Leads Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract US real estate leads from propwire.com with 11M+ properties with owner info, equity, MLS data, lead-type flags (absentee owner, vacant, pre-foreclosure, cash buyer, high equity, etc.), and tax records.

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

# Propwire Real Estate Leads Scraper

Extract US real estate leads from **propwire.com** — 11M+ properties with owner info, estimated equity, MLS status, tax records, and 40+ lead-type flags (absentee owner, high-equity, free-and-clear, vacant, pre-foreclosure, cash buyer, etc.). Ideal for wholesalers, investors, and real-estate pros looking for motivated sellers.

## Features

- **45 output fields** per property — complete flat schema with typed defaults (zero nulls)
- **11M+ properties indexed** — nationwide US coverage
- **40+ lead-type flags** — filter or post-filter by `absentee_owner`, `high_equity`, `vacant_home`, `cash_buyer`, `preforeclosure`, `free_and_clear`, `out_of_state_owner`, and more
- **Owner details** — owner name(s), mailing address (for wholesaling / direct mail campaigns)
- **Valuation data** — estimated market value, equity, LTV, price per square foot, tax assessed values
- **Ownership history** — last sold price + date, months/years of ownership
- **Search by city, state, or ZIP** — mix any combination of locations per run
- **No proxy, no cookies, no login** — uses an anonymous JWT issued by Propwire's public free-skip-trace landing page
- **Zero nulls** — every field has a typed default for predictable downstream processing

## Input

| Field | Type | Description |
|---|---|---|
| `locations` | Array of strings | US locations: city + state (`"Miami, FL"`), state code (`"FL"`), or ZIP (`"33142"`). Mix any combination. |
| `leadTypes` | Array of strings | Optional lead-type filter. Common: `absentee_owner`, `high_equity`, `free_and_clear`, `vacant_home`, `cash_buyer`, `preforeclosure`, `bank_owned`, `out_of_state_owner`, `low_equity`, `flipped_property`, `tired_landlord`, `empty_nester`. Leave empty for all types. |
| `maxItems` | Integer | Max properties to return across all locations (default 50, max 1000). |

### Example Input

```json
{
    "locations": ["Miami, FL", "Austin, TX", "90210"],
    "leadTypes": ["high_equity", "absentee_owner"],
    "maxItems": 100
}
```

State-level search:

```json
{
    "locations": ["FL"],
    "leadTypes": ["vacant_home"],
    "maxItems": 500
}
```

## Output

Each property has **45 fields**. All fields are always present — empty string, zero, `false`, or empty array as typed defaults, never `null`.

### Identity & Location
| Field | Type | Description |
|---|---|---|
| `id` | Integer | Propwire property ID |
| `url` | String | Propwire property-details URL |
| `address` | String | Street address |
| `city` | String | City |
| `state` | String | State code (2 letters) |
| `zip` | String | ZIP code |
| `latitude` | Number | Latitude |
| `longitude` | Number | Longitude |

### Property Specs
| Field | Type | Description |
|---|---|---|
| `propertyType` | String | `SFR`, `MFR`, `Condo`, `Land`, etc. |
| `bedrooms` | Integer | Bedroom count |
| `bathrooms` | Number | Bathroom count |
| `livingAreaSf` | Integer | Living area sq ft |
| `buildingAreaSf` | Integer | Total building area sq ft |
| `lotSizeSf` | Integer | Lot size in sq ft |
| `lotSizeAcres` | Number | Lot size in acres |
| `yearBuilt` | Integer | Year built |
| `units` | Integer | Number of units (multi-family) |

### Valuation
| Field | Type | Description |
|---|---|---|
| `estimatedValue` | Integer | Estimated market value (USD) |
| `estimatedEquity` | Integer | Estimated equity (USD) |
| `estimatedEquityPercentage` | Integer | Equity as % of value |
| `estimatedLtv` | Number | Loan-to-value ratio |
| `estimatedPricePerSf` | Number | $/sqft |
| `lastSoldDate` | String | Last sale date (YYYY-MM-DD) |
| `lastSoldPrice` | Integer | Last sale price (USD) |
| `monthsOfOwnership` | Integer | Months current owner has held the property |
| `yearsOfOwnership` | Integer | Years of ownership (rounded) |

### Owner
| Field | Type | Description |
|---|---|---|
| `ownerName` | String | Owner name(s), comma-joined if multiple |
| `ownerOccupied` | Boolean | Whether owner lives in the property |
| `ownerMailingAddress` | String | Owner mailing street address |
| `ownerMailingCity` | String | Owner mailing city |
| `ownerMailingState` | String | Owner mailing state |
| `ownerMailingZip` | String | Owner mailing ZIP |
| `companyOwned` | Boolean | Whether owned by a company/LLC |
| `individualOwned` | Boolean | Whether owned by individual |
| `trustOwned` | Boolean | Whether owned by a trust |

### MLS Status
| Field | Type | Description |
|---|---|---|
| `mlsListPrice` | Integer | MLS list price if active |
| `mlsListDate` | String | MLS list date |
| `mlsStatus` | String | Current MLS status |
| `mlsPhotoUrl` | String | First MLS photo URL |
| `daysOnMarket` | Integer | Days on market |

### Tax & Leads
| Field | Type | Description |
|---|---|---|
| `taxAssessedTotal` | Integer | Total tax-assessed value |
| `taxAssessedYear` | Integer | Tax assessment year |
| `leadTypes` | Array | Active lead-type flags (array of strings: e.g. `["high_equity", "absentee_owner"]`) |
| `auctionDate` | String | Auction date if scheduled |

### Metadata
| Field | Type | Description |
|---|---|---|
| `scrapedAt` | String | ISO 8601 scrape timestamp |

### Example Output

```json
{
    "id": 88459,
    "url": "https://propwire.com/realestate/1914-nw-49th-st-miami-fl-33142/88459",
    "address": "1914 Nw 49th St",
    "city": "Miami",
    "state": "FL",
    "zip": "33142",
    "latitude": 25.819639,
    "longitude": -80.228871,
    "propertyType": "SFR",
    "bedrooms": 1,
    "bathrooms": 1,
    "livingAreaSf": 862,
    "lotSizeSf": 4796,
    "lotSizeAcres": 0.110101,
    "yearBuilt": 1952,
    "estimatedValue": 369175,
    "estimatedEquity": 308897,
    "estimatedEquityPercentage": 84,
    "lastSoldDate": "2006-07-20",
    "lastSoldPrice": 175000,
    "yearsOfOwnership": 18,
    "ownerName": "1914 RENTAL LLC",
    "ownerOccupied": false,
    "ownerMailingAddress": "7901 4TH ST N STE 300",
    "ownerMailingCity": "ST PETERSBURG",
    "ownerMailingState": "FL",
    "companyOwned": true,
    "taxAssessedTotal": 266265,
    "taxAssessedYear": 2025,
    "leadTypes": ["absentee_owner", "high_equity"],
    "scrapedAt": "2026-04-11T12:40:00+00:00"
}
```

## Lead Type Flags

Every property has 40+ boolean flags. The scraper collects active ones in the `leadTypes` array:

**Equity-based:** `high_equity`, `low_equity`, `negative_equity`, `free_and_clear`
**Ownership-based:** `absentee_owner`, `out_of_state_owner`, `empty_nester`, `tired_landlord`, `intrafamily_transfer`
**Financial distress:** `preforeclosure`, `bank_owned`, `auction`, `lien_tax`, `lien_misc`, `bankruptcy`, `divorce`
**Property condition:** `vacant_home`, `vacant_lot`, `zombie_property`, `abandoned_homes`, `code_violation`
**Deal types:** `cash_buyer`, `flipped_property`, `bargain_properties`, `creative_financing`, `sub_to_mls`, `sub_to_off_market`
**MLS status:** `mls_active`, `mls_pending`, `mls_failed`, `mls_sold`
**Loan types:** `adjustable_loan`, `assumable_loan`, `private_lender`

## FAQ

**Q: Do I need a proxy?**
No. The scraper uses an anonymous JWT obtained from Propwire's public `free-skip-trace` landing page — no login required. Works directly from Apify datacenter IPs.

**Q: How does the authentication work?**
Propwire issues a 2-hour JWT to any visitor of their free-skip-trace lead magnet page (this is how they support anonymous "try before you sign up" skip-tracing). The scraper fetches a fresh token at the start of each run and uses it for all `POST /api/property_search` calls.

**Q: How many results per request?**
The API returns 10 properties per request. The scraper paginates via `result_index` until `maxItems` is reached or results run out.

**Q: What lead types can I filter by?**
All 40+ types listed above. You can pass any subset in `leadTypes` and the API will filter server-side. For finer-grained post-filtering, all active flags are also returned in each property's `leadTypes` array.

**Q: How fresh is the data?**
Propwire's Elasticsearch cluster is updated continuously. Data reflects their live index — the same data you'd see if you logged into propwire.com.

**Q: Is phone number / email included?**
No. Contact info (skip-trace data) requires a paid Propwire account. This scraper returns only the public search data. You can use the `ownerMailingAddress` fields for direct-mail campaigns.

**Q: What's the largest search I can run?**
The scraper caps `maxItems` at 1,000 per run. For larger datasets, split by location or lead type and run multiple times.

**Q: Will this work long-term?**
The anonymous JWT pattern is publicly documented as Propwire's "free skip trace" feature. Propwire could change the flow at any time, but as long as the `/lm/free-skip-trace/search` landing page issues anonymous tokens, this scraper will continue to work.

## Use Cases

- **Wholesaling** — find motivated sellers (absentee + high-equity + out-of-state)
- **Direct mail campaigns** — export owner mailing addresses for postcard campaigns
- **Investment analysis** — filter by equity % and last-sold year to find hold candidates
- **Rental market analysis** — find `tired_landlord` properties in target markets
- **Pre-foreclosure deals** — `preforeclosure` + `auction` flags for distressed-property leads
- **Flip targets** — `vacant_home` or `bargain_properties` in specific cities
- **Data pipelines** — feed structured JSON into CRMs (Podio, REISift, InvestorFuse) without post-processing

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/propwire-leads-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
