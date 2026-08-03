# Meetup + Lu.ma Events Scraper Tutorial: Run This Apify Actor with Python

Scrape events from Meetup.com and Lu.ma, title, date, venue, organizer, attendee count, photo, RSVP status, and discovery feeds (search, by group, by calendar, nearby).

This repository shows how to run [Meetup + Lu.ma Events Scraper](https://apify.com/crawlerbros/meetup-luma-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/meetup-luma-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/meetup-luma-scraper](https://apify.com/crawlerbros/meetup-luma-scraper)
- **SEO title:** Meetup + Lu.ma Events Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape events from Meetup.com and Lu.ma, title, date, venue, organizer, attendee count, photo, RSVP status, and discovery feeds (search, by group, by calendar, nearby).

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

# Meetup + Lu.ma Events Scraper

Scrape events from **Meetup.com** and **Lu.ma** in a single actor — search for events near you, browse calendars, fetch events by URL, or discover trending gatherings worldwide. Returns event title, date, venue, organizer, attendee count, photo, RSVP info, and ticket details.

No login required. No cookies. Works out of the box.

## Use cases

- Build event-discovery dashboards across Meetup + Lu.ma in one feed
- Find local tech meetups in a city
- Track new events posted by a community / calendar / organizer
- Aggregate conference and networking events for a region
- Build a "what's happening this weekend" CRM
- Compare Lu.ma vs Meetup ecosystems by topic

## Platforms

Pick `platform=meetup` for community RSVP events, or `platform=luma` for the modern conference / community calendar ecosystem.

## Modes by platform

| Mode | Meetup | Lu.ma |
|---|---|---|
| `searchEvents` | Yes (find search) | Yes (city + keyword) |
| `byEvent` | Yes (event ID) | Yes (event slug) |
| `byGroup` / `byOrganizer` | Yes | — |
| `groupEvents` | Yes (upcoming events for a group) | — |
| `byCalendar` | — | Yes (community calendar) |
| `discoverNearby` | — | Yes (lat/lng or city) |
| `discoverTrending` | — | Yes (featured cities) |
| `byUrl` | Yes (auto-routed) | Yes (auto-routed) |

## Input

| Field | Type | Description |
|---|---|---|
| `platform` | enum | `meetup` or `luma`. |
| `mode` | enum | What to scrape (see modes). |
| `query` | string | Free-text keyword for search. |
| `location` | string | City + state/country (Meetup search, Luma city resolver). |
| `country` | enum | ISO 3166-1 country (Meetup search). |
| `category` | enum | Meetup topic (`tech`, `social-activities`, `music`, ...). |
| `eventType` | enum | `physical`, `online`, or `any`. |
| `sortBy` | enum | `relevance`, `best`, `newest`, `soonest`. |
| `luma_period` | enum | `upcoming`, `past`, `all`. |
| `urls` | list | Full URLs (auto-routed). |
| `slugs` | list | Event/group/calendar slugs. |
| `eventIds` | list | Meetup event IDs (paired with `slugs`). |
| `lat`, `lng` | number | Latitude/longitude (Lu.ma nearby). |
| `lumaCity` | enum | Lu.ma featured city (San Francisco, Tokyo, ...). |
| `freeOnly` | bool | Drop paid events. |
| `minAttendees` | int | Drop events with fewer than this many RSVPs. |
| `maxItems` | int | Hard cap (1-1000). |
| `autoEscalateOnBlock` | bool | Auto-engage Apify Proxy on 403. |

## Examples

### Search Meetup events (default daily-test)

```json
{
  "platform": "meetup",
  "mode": "searchEvents",
  "query": "tech",
  "location": "san francisco",
  "category": "tech",
  "maxItems": 10
}
```

### Lu.ma events in San Francisco

```json
{
  "platform": "luma",
  "mode": "discoverNearby",
  "lumaCity": "sf",
  "luma_period": "upcoming",
  "maxItems": 50
}
```

### Lu.ma calendar (community page)

```json
{
  "platform": "luma",
  "mode": "byCalendar",
  "slugs": ["sf"],
  "maxItems": 30
}
```

### Meetup group's upcoming events

```json
{
  "platform": "meetup",
  "mode": "groupEvents",
  "slugs": ["meetup-group-englishkoreanexchange"],
  "maxItems": 20
}
```

### Auto-routed URLs (mixed Meetup + Lu.ma)

```json
{
  "platform": "meetup",
  "mode": "byUrl",
  "urls": [
    "https://www.meetup.com/meetup-group-englishkoreanexchange/events/314367217/",
    "https://lu.ma/h85fumdt"
  ]
}
```

## Output

Each record is an event with these fields (`null`/empty values are omitted):

```json
{
  "platform": "meetup",
  "id": "314367217",
  "name": "Asian Appreciation BBQ Party at the Park",
  "url": "https://www.meetup.com/meetup-group-englishkoreanexchange/events/314367217/",
  "startAt": "2026-05-16T12:00:00-07:00",
  "eventType": "PHYSICAL",
  "rsvpState": "JOIN_APPROVAL",
  "guestCount": 100,
  "isFree": true,
  "imageUrl": "https://secure.meetupstatic.com/photos/event/...",
  "group": {
    "id": "36704443",
    "name": "Los Angeles Korean-English Language Exchange Group",
    "urlname": "meetup-group-englishkoreanexchange",
    "url": "https://www.meetup.com/meetup-group-englishkoreanexchange",
    "rating": 4.92,
    "ratingCount": 1350
  },
  "groupName": "Los Angeles Korean-English Language Exchange Group",
  "groupUrlname": "meetup-group-englishkoreanexchange",
  "venueName": "...",
  "city": "Los Angeles",
  "country": "US",
  "scrapedAt": "2026-05-09T20:51:08.123456+00:00"
}
```

Lu.ma records use the same flat schema with `platform: "luma"` and Lu.ma-specific fields like `calendar.id`, `ticketCount`, `requireApproval`, `featured_city`, etc.

## FAQs

**Q: Do I need a Meetup or Lu.ma account?**
A: No. The actor scrapes public pages only.

**Q: How does Lu.ma search work? They don't have a search bar.**
A: We use Lu.ma's `/discover` endpoint to enumerate featured cities, fetch each city's upcoming events via the public `api.lu.ma/discover/get-paginated-events` API, then filter client-side by your `query`.

**Q: Can I get events farther in the future / past?**
A: Set `luma_period=past` for past events. Meetup only exposes upcoming events on its public find page.

**Q: Why is `description` sometimes missing?**
A: Meetup's search-page Apollo cache only includes the first 100-200 chars of each description. To get the full description, fetch the event detail (mode=byEvent) — that page includes the full body.

**Q: How do you parse a Lu.ma URL?**
A: `lu.ma/<slug>` could be either an event or a calendar; the actor probes the page's `__NEXT_DATA__.initialData.kind` to disambiguate, then routes to the right record builder.

**Q: Are Meetup events worldwide?**
A: Yes — Meetup search supports any country (US, UK, DE, FR, IN, BR, JP, ...). Set `country` to narrow.

**Q: Are Lu.ma cities pre-defined?**
A: Lu.ma's discover page lists ~40 featured cities globally. The `lumaCity` enum mirrors that list. To find a non-featured location, use `lat` + `lng` and the actor picks the closest featured city.

**Q: What about RSVPs / attendees?**
A: We expose `guestCount` (Meetup `rsvps.totalCount`, Lu.ma `guest_count`). The full attendee list is only visible to logged-in users on both platforms.

## Limitations

- **Meetup attendee names** are private to each event's host; only counts are returned.
- **Lu.ma free-text search** is implemented client-side over discover-fetched events (no server-side keyword search exists publicly).
- **Past events** on Meetup are not indexed by the public find page; use `byUrl` with the specific event link if you have it.
- **RSVP / register actions** are read-only; the actor does not RSVP or register.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/meetup-luma-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
