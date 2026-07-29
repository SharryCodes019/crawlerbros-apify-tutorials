# Resident Advisor (RA) Scraper Tutorial: Run This Apify Actor with Python

Scrape Resident Advisor (ra.co) with upcoming events by city, artist profiles, and venue/club profiles. No auth required.

This repository shows how to run [Resident Advisor (RA) Scraper](https://apify.com/crawlerbros/resident-advisor-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/resident-advisor-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/resident-advisor-scraper](https://apify.com/crawlerbros/resident-advisor-scraper)
- **SEO title:** Resident Advisor (RA) Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Resident Advisor (ra.co) with upcoming events by city, artist profiles, and venue/club profiles. No auth required.

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

## Resident Advisor (RA) Scraper

Extract event listings, complete artist line-ups, and venue/club profiles from [Resident Advisor](https://ra.co) — the world's leading platform for electronic music with 800 000+ events across 130+ countries.

No login, cookies, or proxy required. Data is sourced directly from Resident Advisor's public API.

---

### What you can scrape

| Mode | What you get |
|---|---|
| **Events by city** | Upcoming events for any city worldwide — full line-up, venue, genres, ticket link, flyer, date & time |
| **Artist profile** | Biography, social links, follower count, and upcoming/recent events for any artist |
| **Venue / club profile** | Address, capacity, description, follower count, and recent events for any club |

---

### Input

| Field | Type | Required | Description | Example |
|---|---|---|---|---|
| `mode` | Select | No | What to scrape. Default: `eventsByCity` | `eventsByCity`, `artistProfile`, `venueProfile` |
| `countryCode` | Select | No | Country for event search (mode=`eventsByCity`). Default: `gb` | `gb`, `de`, `us`, `nl`, `fr` |
| `city` | Text | No | City name or slug. Default: `london` | `london`, `berlin`, `new-york`, `amsterdam` |
| `dateFrom` | Text | No | Fetch events from this date (YYYY-MM-DD). Defaults to today | `2026-07-01` |
| `dateTo` | Text | No | Fetch events up to this date (YYYY-MM-DD). Leave empty for no upper bound | `2026-07-31` |
| `artistName` | Text | No* | Artist slug or name (required for `artistProfile` mode) | `aphex-twin`, `bicep`, `peggy-gou` |
| `venueSlug` | Text | No* | Venue name or search term (required for `venueProfile` mode) | `fabric`, `berghain`, `xoyo` |
| `maxItems` | Integer | No | Maximum records to return (1–200). Default: `20` | `50` |

*Required when the corresponding mode is selected.

#### Example inputs

**Events by city**
```json
{
  "mode": "eventsByCity",
  "countryCode": "gb",
  "city": "london",
  "dateFrom": "2026-07-01",
  "dateTo": "2026-07-31",
  "maxItems": 50
}
````

**Artist profile**

```json
{
  "mode": "artistProfile",
  "artistName": "bicep",
  "maxItems": 10
}
```

**Venue profile**

```json
{
  "mode": "venueProfile",
  "venueSlug": "fabric",
  "maxItems": 10
}
```

***

### Output

#### Events by city

One record per event. Fields are omitted when data is unavailable for an event — no null or empty values are ever returned.

```json
{
  "eventId": "2182764",
  "title": "GALA'26",
  "eventUrl": "https://ra.co/events/2182764",
  "date": "2026-05-22",
  "startTime": "14:00",
  "endTime": "22:30",
  "venue": "Peckham Rye Park",
  "venueUrl": "https://ra.co/clubs/143848",
  "city": "London",
  "country": "United Kingdom",
  "artists": ["Objekt", "Or:la", "Pariah"],
  "unlinkedArtists": ["Clipz", "Darren Jay", "MC Rage"],
  "allArtists": ["Objekt", "Or:la", "Clipz", "Darren Jay", "Pariah", "MC Rage"],
  "lineupText": "Objekt\nOr:la\nClipz\nDarren Jay\nPariah\nMC Rage",
  "genres": ["Techno", "House"],
  "isTicketed": true,
  "ticketUrl": "https://tickets.ra.co/events/2182764",
  "cost": "£25",
  "flyerUrl": "https://static.ra.co/images/events/flyers/2026/05/...",
  "recordType": "event",
  "scrapedAt": "2026-06-14T10:00:00+00:00"
}
```

**Line-up fields explained:**

| Field | Description |
|---|---|
| `artists` | Artists with a linked Resident Advisor profile |
| `unlinkedArtists` | Artists listed in the line-up who do **not** have an RA profile (plain-text names) |
| `allArtists` | The complete line-up in order — both linked and unlinked artists combined |
| `lineupText` | The full line-up as a plain-text string, preserving the original layout (one slot per line) |

> **Why four artist fields?** RA stores two types of artist references: structured links (with profile pages) and plain-text names. Using only `artists` misses any act without an RA profile. Use `allArtists` for the complete line-up, `unlinkedArtists` if you only need the previously-missing names, and `lineupText` if you want to parse the raw layout yourself.

***

#### Artist profile

One record per run.

```json
{
  "artistId": "828",
  "name": "Aphex Twin",
  "artistUrl": "https://ra.co/dj/aphextwin",
  "imageUrl": "https://static.ra.co/images/profiles/aphextwin.jpg",
  "biography": "Aphex Twin, aka Richard D. James, is one of the most influential...",
  "country": "United Kingdom",
  "region": "South + East",
  "discogs": "https://www.discogs.com/artist/Aphex+Twin",
  "soundcloud": "https://soundcloud.com/aphex-twin",
  "instagram": "https://www.instagram.com/aphextwin",
  "followerCount": 109890,
  "upcomingEventsCount": 2,
  "upcomingEvents": [
    {
      "eventId": "2345678",
      "title": "Aphex Twin Live",
      "date": "2026-09-12",
      "startTime": "21:00",
      "eventUrl": "https://ra.co/events/2345678",
      "venue": "Roundhouse",
      "venueUrl": "https://ra.co/clubs/9999",
      "genres": ["IDM", "Ambient"]
    }
  ],
  "recordType": "artist",
  "scrapedAt": "2026-06-14T10:00:00+00:00"
}
```

Social link fields (`facebook`, `instagram`, `twitter`, `soundcloud`, `discogs`, `bandcamp`, `website`) are only included when the artist has set them on their RA profile.

***

#### Venue / club profile

One record per run.

```json
{
  "venueId": "237",
  "name": "fabric",
  "venueUrl": "https://ra.co/clubs/237",
  "address": "77a Charterhouse St, Clerkenwell, London EC1M 6HJ, United Kingdom",
  "phone": "020 7336 8898",
  "website": "http://www.fabriclondon.com",
  "description": "fabric is one of London's premier venues for electronic music...",
  "capacity": "1600",
  "city": "London",
  "country": "United Kingdom",
  "followerCount": 38792,
  "recentEvents": [
    {
      "eventId": "2413816",
      "title": "Field Day Afterparty",
      "date": "2026-05-23",
      "startTime": "23:00",
      "eventUrl": "https://ra.co/events/2413816",
      "artists": ["Duskus", "Eliza Rose"],
      "genres": ["House"]
    }
  ],
  "recordType": "venue",
  "scrapedAt": "2026-06-14T10:00:00+00:00"
}
```

***

### Supported countries

35 of the most active RA markets are available via the country code selector:

United Kingdom · Germany · United States · Netherlands · France · Australia · Japan · Belgium · Italy · Spain · Portugal · Sweden · Denmark · Norway · Finland · Brazil · Mexico · Canada · South Africa · India · Singapore · Austria · Switzerland · Ireland · Poland · Czech Republic · Hungary · Greece · Romania · Argentina · Colombia · Chile · New Zealand · South Korea · Thailand

***

### Frequently Asked Questions

**Does this require login, cookies, or a proxy?**
No. All scraped data is publicly accessible from Resident Advisor's official API without any authentication. No proxy is needed.

**How do I find the right city slug?**
Go to [ra.co/events](https://ra.co/events), select your city, and look at the URL — it shows the format `ra.co/events/gb/london`. Use `london` as the city and `gb` as the country code. Multi-word cities use hyphens: `new-york`, `los-angeles`, `buenos-aires`.

**What formats does the `artistName` field accept?**
Both the hyphenated slug from the RA URL (e.g. `aphex-twin` from `ra.co/dj/aphex-twin`) and the plain artist name (e.g. `Aphex Twin`) are supported. The scraper tries both variants automatically.

**What formats does the `venueSlug` field accept?**
You can enter the venue's common name (`fabric`, `berghain`), a partial name (`fabric london`), or the full name. The scraper searches RA's venue index and returns the best match.

**Why do some events have `unlinkedArtists` and others don't?**
`unlinkedArtists` only appears when the event's line-up includes artists who don't have an RA profile page — their names are listed as plain text rather than profile links. Events where every act has an RA profile will only have `artists`. Events with no confirmed line-up will have neither.

**What's the difference between `artists` and `allArtists`?**
`artists` contains only acts with a linked RA profile. `allArtists` is the complete line-up in order — it merges `artists` and `unlinkedArtists` so you get every act on the bill in a single list. For most automation use cases (Airtable, Make.com, Zapier pipelines), `allArtists` is the field you want.

**Can I filter events by date range?**
Yes. Use `dateFrom` and `dateTo` in `YYYY-MM-DD` format. You can set either or both — `dateFrom` alone returns everything from that date onwards, `dateTo` alone returns everything up to that date.

**How many events can I get per run?**
Up to 200 events per run via `maxItems`. For larger volumes, run multiple times with different date ranges.

**What if a city returns no results?**
The city slug must match RA's format (e.g. `new-york` not `newyork`, `sao-paulo` not `saoplo`). Some smaller markets may have few or no upcoming events — try widening your date range or using a nearby larger city.

**Does this work globally?**
Yes. RA covers 130+ countries. This scraper supports 35 of the most active markets via the country dropdown, covering the major electronic music scenes worldwide.

**How is `lineupText` formatted?**
It is the raw plain-text version of the line-up block with all HTML tags removed: one line per slot, with performers on the same stage sharing a line separated by `+`. You can parse it yourself to reconstruct stage/time splits if needed.

***

### Data source

All data is sourced from [Resident Advisor's](https://ra.co) official public API, which powers their website. No unofficial scraping techniques are used.

# Actor input Schema

## `mode` (type: `string`):

What to scrape from Resident Advisor.

## `countryCode` (type: `string`):

Country for event search (mode=eventsByCity). Two-letter code.

## `city` (type: `string`):

City name for event search (mode=eventsByCity). Examples: london, berlin, new-york, amsterdam, paris.

## `dateFrom` (type: `string`):

Fetch events from this date onwards. Defaults to today if empty. Format: YYYY-MM-DD.

## `dateTo` (type: `string`):

Fetch events up to this date. Leave empty for no upper bound. Format: YYYY-MM-DD.

## `artistName` (type: `string`):

Artist slug or name for artist profile (mode=artistProfile). Example: aphex-twin, bicep, peggy-gou.

## `venueSlug` (type: `string`):

Venue slug or name for venue profile (mode=venueProfile). Example: fabric, berghain, panorama-bar.

## `maxItems` (type: `integer`):

Maximum number of records to return.

## Actor input object example

```json
{
  "mode": "eventsByCity",
  "countryCode": "gb",
  "city": "london",
  "maxItems": 20
}
```

# Actor output Schema

## `events` (type: `string`):

Dataset containing all scraped Resident Advisor events, artist profiles, or venue profiles.

# API

You can run this Actor programmatically using our API. Below are code examples in JavaScript, Python, and CLI, as well as the OpenAPI specification and MCP server setup.

## JavaScript example

```javascript
import { ApifyClient } from 'apify-client';

// Initialize the ApifyClient with your Apify API token
// Replace the '<YOUR_API_TOKEN>' with your token
const client = new ApifyClient({
    token: '<YOUR_API_TOKEN>',
});

// Prepare Actor input
const input = {
    "mode": "eventsByCity",
    "countryCode": "gb",
    "city": "london",
    "maxItems": 20
};

// Run the Actor and wait for it to finish
const run = await client.actor("crawlerbros/resident-advisor-scraper").call(input);

// Fetch and print Actor results from the run's dataset (if any)
console.log('Results from dataset');
console.log(`💾 Check your data here: https://console.apify.com/storage/datasets/${run.defaultDatasetId}`);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
items.forEach((item) => {
    console.dir(item);
});

// 📚 Want to learn more 📖? Go to → https://docs.apify.com/api/client/js/docs

```

## Python example

```python
from apify_client import ApifyClient

# Initialize the ApifyClient with your Apify API token
# Replace '<YOUR_API_TOKEN>' with your token.
client = ApifyClient("<YOUR_API_TOKEN>")

# Prepare the Actor input
run_input = {
    "mode": "eventsByCity",
    "countryCode": "gb",
    "city": "london",
    "maxItems": 20,
}

# Run the Actor and wait for it to finish
run = client.actor("crawlerbros/resident-advisor-scraper").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
print("💾 Check your data here: https://console.apify.com/storage/datasets/" + run["defaultDatasetId"])
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# 📚 Want to learn more 📖? Go to → https://docs.apify.com/api/client/python/docs/quick-start

```

## CLI example

```bash
echo '{
  "mode": "eventsByCity",
  "countryCode": "gb",
  "city": "london",
  "maxItems": 20
}' |
apify call crawlerbros/resident-advisor-scraper --silent --output-dataset

```

## MCP server setup

```json
{
    "mcpServers": {
        "apify": {
            "command": "npx",
            "args": [
                "mcp-remote",
                "https://mcp.apify.com/?tools=crawlerbros/resident-advisor-scraper",
                "--header",
                "Authorization: Bearer <YOUR_API_TOKEN>"
            ]
        }
    }
}

```

## OpenAPI specification

```json
{
    "openapi": "3.0.1",
    "info": {
        "title": "Resident Advisor (RA) Scraper",
        "description": "Scrape Resident Advisor (ra.co) with upcoming events by city, artist profiles, and venue/club profiles. No auth required.",
        "version": "1.0",
        "x-build-id": "guf0qgkBhGeJJyNdY"
    },
    "servers": [
        {
            "url": "https://api.apify.com/v2"
        }
    ],
    "paths": {
        "/acts/crawlerbros~resident-advisor-scraper/run-sync-get-dataset-items": {
            "post": {
                "operationId": "run-sync-get-dataset-items-crawlerbros-resident-advisor-scraper",
                "x-openai-isConsequential": false,
                "summary": "Executes an Actor, waits for its completion, and returns Actor's dataset items in response.",
                "tags": [
                    "Run Actor"
                ],
                "requestBody": {
                    "required": true,
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/inputSchema"
                            }
                        }
                    }
                },
                "parameters": [
                    {
                        "name": "token",
                        "in": "query",
                        "required": true,
                        "schema": {
                            "type": "string"
                        },
                        "description": "Enter your Apify token here"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK"
                    }
                }
            }
        },
        "/acts/crawlerbros~resident-advisor-scraper/runs": {
            "post": {
                "operationId": "runs-sync-crawlerbros-resident-advisor-scraper",
                "x-openai-isConsequential": false,
                "summary": "Executes an Actor and returns information about the initiated run in response.",
                "tags": [
                    "Run Actor"
                ],
                "requestBody": {
                    "required": true,
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/inputSchema"
                            }
                        }
                    }
                },
                "parameters": [
                    {
                        "name": "token",
                        "in": "query",
                        "required": true,
                        "schema": {
                            "type": "string"
                        },
                        "description": "Enter your Apify token here"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/runsResponseSchema"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/acts/crawlerbros~resident-advisor-scraper/run-sync": {
            "post": {
                "operationId": "run-sync-crawlerbros-resident-advisor-scraper",
                "x-openai-isConsequential": false,
                "summary": "Executes an Actor, waits for completion, and returns the OUTPUT from Key-value store in response.",
                "tags": [
                    "Run Actor"
                ],
                "requestBody": {
                    "required": true,
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/inputSchema"
                            }
                        }
                    }
                },
                "parameters": [
                    {
                        "name": "token",
                        "in": "query",
                        "required": true,
                        "schema": {
                            "type": "string"
                        },
                        "description": "Enter your Apify token here"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK"
                    }
                }
            }
        }
    },
    "components": {
        "schemas": {
            "inputSchema": {
                "type": "object",
                "properties": {
                    "mode": {
                        "title": "Mode",
                        "enum": [
                            "eventsByCity",
                            "artistProfile",
                            "venueProfile"
                        ],
                        "type": "string",
                        "description": "What to scrape from Resident Advisor.",
                        "default": "eventsByCity"
                    },
                    "countryCode": {
                        "title": "Country code",
                        "enum": [
                            "gb",
                            "de",
                            "us",
                            "nl",
                            "fr",
                            "au",
                            "jp",
                            "be",
                            "it",
                            "es",
                            "pt",
                            "se",
                            "dk",
                            "no",
                            "fi",
                            "br",
                            "mx",
                            "ca",
                            "za",
                            "in",
                            "sg",
                            "at",
                            "ch",
                            "ie",
                            "pl",
                            "cz",
                            "hu",
                            "gr",
                            "ro",
                            "ar",
                            "co",
                            "cl",
                            "nz",
                            "kr",
                            "th"
                        ],
                        "type": "string",
                        "description": "Country for event search (mode=eventsByCity). Two-letter code.",
                        "default": "gb"
                    },
                    "city": {
                        "title": "City",
                        "type": "string",
                        "description": "City name for event search (mode=eventsByCity). Examples: london, berlin, new-york, amsterdam, paris."
                    },
                    "dateFrom": {
                        "title": "Date from (YYYY-MM-DD)",
                        "type": "string",
                        "description": "Fetch events from this date onwards. Defaults to today if empty. Format: YYYY-MM-DD."
                    },
                    "dateTo": {
                        "title": "Date to (YYYY-MM-DD)",
                        "type": "string",
                        "description": "Fetch events up to this date. Leave empty for no upper bound. Format: YYYY-MM-DD."
                    },
                    "artistName": {
                        "title": "Artist name / slug",
                        "type": "string",
                        "description": "Artist slug or name for artist profile (mode=artistProfile). Example: aphex-twin, bicep, peggy-gou."
                    },
                    "venueSlug": {
                        "title": "Venue slug or search term",
                        "type": "string",
                        "description": "Venue slug or name for venue profile (mode=venueProfile). Example: fabric, berghain, panorama-bar."
                    },
                    "maxItems": {
                        "title": "Max items",
                        "minimum": 1,
                        "maximum": 200,
                        "type": "integer",
                        "description": "Maximum number of records to return.",
                        "default": 20
                    }
                }
            },
            "runsResponseSchema": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string"
                            },
                            "actId": {
                                "type": "string"
                            },
                            "userId": {
                                "type": "string"
                            },
                            "startedAt": {
                                "type": "string",
                                "format": "date-time",
                                "example": "2025-01-08T00:00:00.000Z"
                            },
                            "finishedAt": {
                                "type": "string",
                                "format": "date-time",
                                "example": "2025-01-08T00:00:00.000Z"
                            },
                            "status": {
                                "type": "string",
                                "example": "READY"
                            },
                            "meta": {
                                "type": "object",
                                "properties": {
                                    "origin": {
                                        "type": "string",
                                        "example": "API"
                                    },
                                    "userAgent": {
                                        "type": "string"
                                    }
                                }
                            },
                            "stats": {
                                "type": "object",
                                "properties": {
                                    "inputBodyLen": {
                                        "type": "integer",
                                        "example": 2000
                                    },
                                    "rebootCount": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "restartCount": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "resurrectCount": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "computeUnits": {
                                        "type": "integer",
                                        "example": 0
                                    }
                                }
                            },
                            "options": {
                                "type": "object",
                                "properties": {
                                    "build": {
                                        "type": "string",
                                        "example": "latest"
                                    },
                                    "timeoutSecs": {
                                        "type": "integer",
                                        "example": 300
                                    },
                                    "memoryMbytes": {
                                        "type": "integer",
                                        "example": 1024
                                    },
                                    "diskMbytes": {
                                        "type": "integer",
                                        "example": 2048
                                    }
                                }
                            },
                            "buildId": {
                                "type": "string"
                            },
                            "defaultKeyValueStoreId": {
                                "type": "string"
                            },
                            "defaultDatasetId": {
                                "type": "string"
                            },
                            "defaultRequestQueueId": {
                                "type": "string"
                            },
                            "buildNumber": {
                                "type": "string",
                                "example": "1.0.0"
                            },
                            "containerUrl": {
                                "type": "string"
                            },
                            "usage": {
                                "type": "object",
                                "properties": {
                                    "ACTOR_COMPUTE_UNITS": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "DATASET_READS": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "DATASET_WRITES": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "KEY_VALUE_STORE_READS": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "KEY_VALUE_STORE_WRITES": {
                                        "type": "integer",
                                        "example": 1
                                    },
                                    "KEY_VALUE_STORE_LISTS": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "REQUEST_QUEUE_READS": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "REQUEST_QUEUE_WRITES": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "DATA_TRANSFER_INTERNAL_GBYTES": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "DATA_TRANSFER_EXTERNAL_GBYTES": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "PROXY_RESIDENTIAL_TRANSFER_GBYTES": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "PROXY_SERPS": {
                                        "type": "integer",
                                        "example": 0
                                    }
                                }
                            },
                            "usageTotalUsd": {
                                "type": "number",
                                "example": 0.00005
                            },
                            "usageUsd": {
                                "type": "object",
                                "properties": {
                                    "ACTOR_COMPUTE_UNITS": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "DATASET_READS": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "DATASET_WRITES": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "KEY_VALUE_STORE_READS": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "KEY_VALUE_STORE_WRITES": {
                                        "type": "number",
                                        "example": 0.00005
                                    },
                                    "KEY_VALUE_STORE_LISTS": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "REQUEST_QUEUE_READS": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "REQUEST_QUEUE_WRITES": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "DATA_TRANSFER_INTERNAL_GBYTES": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "DATA_TRANSFER_EXTERNAL_GBYTES": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "PROXY_RESIDENTIAL_TRANSFER_GBYTES": {
                                        "type": "integer",
                                        "example": 0
                                    },
                                    "PROXY_SERPS": {
                                        "type": "integer",
                                        "example": 0
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
```

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/resident-advisor-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
