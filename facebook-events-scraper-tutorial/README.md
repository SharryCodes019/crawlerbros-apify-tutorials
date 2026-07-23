# Facebook Events Scraper Tutorial: Run This Apify Actor with Python

Scrape public Facebook event data without cookies or authentication. Extract event name, description, date, time, location, coordinates, hosts, photos, ticket URLs, and attendee counts.

This repository shows how to run [Facebook Events Scraper](https://apify.com/crawlerbros/facebook-events-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/facebook-events-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/facebook-events-scraper](https://apify.com/crawlerbros/facebook-events-scraper)
- **SEO title:** Facebook Events Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape public Facebook event data without cookies or authentication. Extract event name, description, date, time, location, coordinates, hosts, photos, ticket URLs, and attendee counts.

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

# Facebook Events Scraper

Extract detailed data from public Facebook events without login or cookies. Get event name, description, date, time, location with coordinates, hosts, cover photos, ticket URLs, attendee counts, and more.

## Features

- Scrape public Facebook events by URL or event ID
- Extract events from Facebook page event listings
- No login, cookies, or authentication required
- Full event details: name, description, dates, location, hosts, photos
- GPS coordinates for event locations
- Attendee/interested counts
- Online event support (type, third-party URLs)
- Canceled event detection
- Export to JSON, CSV, Excel, or XML

## Input

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Event URLs | string[] | Yes | Facebook event URLs, page event listing URLs, or bare event IDs |
| Proxy Configuration | object | No | Optional proxy settings for blocked IPs |

### Supported URL Formats

- **Single event**: `https://www.facebook.com/events/1234567890`
- **Page events**: `https://www.facebook.com/PageName/events`
- **Bare event ID**: `1234567890`

### Example Input

```json
{
    "eventUrls": [
        "https://www.facebook.com/events/1855253805343101",
        "https://www.facebook.com/events/1084489187170885"
    ]
}
```

## Output

Each event record contains the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `event_id` | string | Facebook event ID |
| `name` | string | Event name/title |
| `description` | string | Full event description |
| `url` | string | Facebook event URL |
| `start_timestamp` | integer | Unix timestamp of event start |
| `end_timestamp` | integer | Unix timestamp of event end |
| `start_date` | string | ISO 8601 start date |
| `end_date` | string | ISO 8601 end date |
| `formatted_date` | string | Human-readable date from Facebook |
| `timezone` | string | Event timezone (e.g., "UTC+02") |
| `is_online` | boolean | Whether the event is online |
| `is_canceled` | boolean | Whether the event is canceled |
| `location_name` | string | Venue or location name |
| `location_address` | string | Street address |
| `location_city` | string | City name |
| `latitude` | number | Location latitude |
| `longitude` | number | Location longitude |
| `photo_url` | string | Cover photo direct URL |
| `video_url` | string | Cover video URL (if available) |
| `hosts` | array | Event hosts (name, URL, type) |
| `categories` | array | Event categories |
| `ticket_url` | string | External ticket purchase URL |
| `online_type` | string | Online event type (MESSENGER_ROOM, THIRD_PARTY, etc.) |
| `users_responded` | integer | Number of people who responded |
| `input_url` | string | The input URL that found this event |
| `scraped_at` | string | ISO 8601 timestamp of when data was scraped |

### Example Output

```json
{
    "event_id": "1855253805343101",
    "name": "SZIGET FESTIVAL 2026 - Official Event",
    "description": "The story continues. Stronger, freer, and more ours than ever...",
    "url": "https://www.facebook.com/events/1855253805343101/",
    "start_timestamp": 1786428000,
    "end_timestamp": 1786874400,
    "start_date": "2026-08-11T06:00:00+00:00",
    "end_date": "2026-08-16T10:00:00+00:00",
    "formatted_date": "11 Aug at 08:00 - 16 Aug at 12:00 CEST",
    "timezone": "UTC+02",
    "is_online": false,
    "is_canceled": false,
    "location_name": "Sziget Festival Official (Default)",
    "location_address": "",
    "location_city": "Budapest",
    "latitude": 47.553047718642,
    "longitude": 19.054233735845,
    "photo_url": "https://scontent.xx.fbcdn.net/v/...",
    "video_url": "",
    "hosts": [
        {
            "name": "Sziget Festival Official",
            "url": "https://www.facebook.com/SzigetFestival",
            "type": "User"
        }
    ],
    "categories": [],
    "ticket_url": "http://szigetfestival.com/",
    "online_type": "",
    "users_responded": 9051,
    "input_url": "https://www.facebook.com/events/1855253805343101",
    "scraped_at": "2026-03-25T12:00:00+00:00"
}
```

## Use Cases

- **Event monitoring**: Track upcoming events from specific venues or organizers
- **Market research**: Analyze event attendance and engagement trends
- **Location intelligence**: Map events by geographic coordinates
- **Content aggregation**: Collect event data for calendars and listings
- **Competitive analysis**: Monitor competitor events and attendance

## Limitations

- **Public events only**: Private or restricted events cannot be accessed
- **Login wall**: Some events may be blocked from datacenter IPs. Enable proxy if this happens.
- **No search**: This actor scrapes specific event URLs. It does not search for events by keyword.
- **Rate limits**: Facebook may rate-limit requests. The actor uses delays between requests to avoid blocks.

## FAQ

**Does this require a Facebook account?**
No. This actor works without any login, cookies, or authentication. It only accesses publicly available event data.

**Why are some events not returned?**
The event may be private, deleted, or restricted to logged-in users. The actor only works with public events.

**Can I search for events by keyword?**
No. You need to provide specific event URLs or page event listing URLs. You can find event URLs by browsing Facebook in your browser and copying the URLs.

**How do I get events from a Facebook page?**
Use the page events URL format: `https://www.facebook.com/PageName/events`. The actor will extract all listed events from that page.

**Do I need a proxy?**
Usually not. Facebook event pages are publicly accessible. However, if you're running from a datacenter IP that Facebook blocks, enabling a residential proxy may help.

**How many events can I scrape?**
There is no hard limit. The actor processes each URL sequentially with delays to avoid rate limiting.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/facebook-events-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
