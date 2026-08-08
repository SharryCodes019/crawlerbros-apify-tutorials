# Forebet Football Predictions Scraper Tutorial: Run This Apify Actor with Python

Scrape Forebet (forebet.com) - mathematical football predictions with win/draw/loss probabilities, predicted scores, average goals, and weather conditions for matches worldwide.

This repository shows how to run [Forebet Football Predictions Scraper](https://apify.com/crawlerbros/forebet-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/forebet-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/forebet-scraper](https://apify.com/crawlerbros/forebet-scraper)
- **SEO title:** Forebet Football Predictions Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Forebet (forebet.com) - mathematical football predictions with win/draw/loss probabilities, predicted scores, average goals, and weather conditions for matches worldwide.

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

# Forebet Football Predictions Scraper

Scrape **[Forebet](https://www.forebet.com)** — free mathematical football predictions covering 850+ competitions worldwide. Get home/draw/away win probabilities, predicted scores, and average goals for upcoming matches.

## What You Can Scrape

| Mode | Data |
|------|------|
| `tomorrow` | Tomorrow's football predictions |
| `today` | Today's football predictions |
| `weekend` | Weekend football predictions |

## Input

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `mode` | select | `tomorrow` | Which predictions to fetch |
| `maxItems` | integer | `20` | Maximum predictions to return |

## Output

```json
{
  "homeTeam": "Union Brescia",
  "awayTeam": "Ascoli",
  "matchDate": "2026-06-02",
  "matchDateTime": "02/06/2026 21:15",
  "matchTime": "21:15",
  "country": "Italy",
  "league": "Serie C",
  "predictionHome": 33,
  "predictionDraw": 31,
  "predictionAway": 36,
  "prediction": "2",
  "predictedScore": "0-1",
  "averageGoals": 0.63,
  "matchUrl": "https://www.forebet.com/en/football/matches/union-brescia-ascoli-2464661",
  "mode": "tomorrow",
  "scrapedAt": "2024-01-01T00:00:00+00:00"
}
```

## FAQs

**What do the prediction percentages mean?**
`predictionHome`, `predictionDraw`, and `predictionAway` are the mathematical probability (%) of each outcome based on team statistics.

**What does `prediction` field mean?**
It shows the most likely outcome: "1" (home win), "X" (draw), or "2" (away win).

**How many matches are available?**
Forebet covers 850+ competitions, with typically 30-200 matches predicted per day.

**Is the data free?**
Yes, Forebet provides free predictions publicly accessible without authentication.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/forebet-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
