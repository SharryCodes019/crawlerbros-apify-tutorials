# Google Earth Scraper Tutorial: Run This Apify Actor with Python

Advanced Google Earth Scraper. Extracts precise 3D coordinates (Latitude, Longitude, Altitude), Place IDs, Addresses, and metadata from Google Earth.

This repository shows how to run [Google Earth Scraper](https://apify.com/crawlerbros/google-earth-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/google-earth-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/google-earth-scraper](https://apify.com/crawlerbros/google-earth-scraper)
- **SEO title:** Google Earth Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Advanced Google Earth Scraper. Extracts precise 3D coordinates (Latitude, Longitude, Altitude), Place IDs, Addresses, and metadata from Google Earth.

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

# Google Earth Location Scraper

A robust Apify Actor that scrapes location data directly from Google Earth.

## Features

-   **Direct Google Earth Scraping**: Extracts data from Google Earth's internal Search API.
-   **Headless Support**: Uses Xvfb and SwiftShader to render Google Earth's 3D interface in a headless Docker environment.
-   **No API Keys Required**: Does not require a Google Maps API key.
-   **Detailed Data**: Extracts latitude, longitude, place name, description, and other metadata.

## Input

The actor accepts the following input options:

| Field | Type | Default | Description |
|---|---|---|---|
| `searchQueries` | array | `['Eiffel Tower']` | List of location names or addresses to search for. |
| `minDelayBetweenRequests` | integer | `2` | Minimum delay (in seconds) between search requests. |
| `maxDelayBetweenRequests` | integer | `5` | Maximum delay (in seconds) between search requests. |

### Example Input

```json
{
    "searchQueries": [
        "Eiffel Tower",
        "Statue of Liberty",
        "Burj Khalifa"
    ],
    "minDelayBetweenRequests": 2,
    "maxDelayBetweenRequests": 5
}
```

## Output

The actor outputs the scraped data to the default dataset. Each result includes:

-   `search_query`: The query used to find the location.
-   `place_name`: The name of the place found.
-   `latitude`: Latitude coordinate.
-   `longitude`: Longitude coordinate.
-   `description`: Brief description (if available).
-   `google_place_id`: Google's internal place ID.
-   `url`: The Google Earth URL for the location.
-   `scraped_at`: Timestamp of extraction.

### Example Output

```json
{
    "search_query": "Eiffel Tower",
    "place_name": "Eiffel Tower",
    "latitude": 48.85837,
    "longitude": 2.294481,
    "description": "Tower in Paris, France",
    "google_place_id": "0x47e66e2964e34e2d:0x8ddca9ee380ef7e0",
    "url": "https://earth.google.com/web/search/Eiffel+Tower/...",
    "data_source": "search_api",
    "scraped_at": "2025-11-28T12:00:00.000000"
}
```

## Technical Details

This scraper runs a headless Chromium browser with **Xvfb** (Virtual Framebuffer) to support WebGL rendering, which is required for Google Earth to load. It intercepts network traffic to capture the raw data returned by Google's Search API.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/google-earth-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
