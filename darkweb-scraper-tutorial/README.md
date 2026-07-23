# Darkweb Scraper Tutorial: Run This Apify Actor with Python

Crawl dark web .onion sites via Tor. Extract links, emails, phone numbers, cryptocurrency wallet addresses, social media handles, and API keys from hidden services.

This repository shows how to run [Darkweb Scraper](https://apify.com/crawlerbros/darkweb-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/darkweb-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/darkweb-scraper](https://apify.com/crawlerbros/darkweb-scraper)
- **SEO title:** Darkweb Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Crawl dark web .onion sites via Tor. Extract links, emails, phone numbers, cryptocurrency wallet addresses, social media handles, and API keys from hidden services.

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

# Darkweb Scraper

Crawl dark web `.onion` sites via Tor and extract sensitive data including emails, phone numbers, cryptocurrency wallet addresses, social media handles, and API keys. Ideal for OSINT, threat intelligence, and security research.

## What is Darkweb Scraper?

Darkweb Scraper is an Apify actor that accesses Tor hidden services (`.onion` sites) and extracts structured data from them. It bundles a Tor daemon internally, so you don't need any special setup or proxy configuration. Just provide a search keyword or direct `.onion` URLs, and the scraper will crawl the dark web and return organized results.

## What can this actor do?

- **Search the dark web** — Enter any keyword and discover relevant `.onion` sites automatically via dark web search engines
- **Crawl .onion sites** — Navigate through dark web pages with configurable crawl depth and page limits
- **Extract emails** — Find email addresses embedded in dark web pages
- **Extract phone numbers** — Detect phone numbers in international formats
- **Extract cryptocurrency addresses** — Identify Bitcoin, Ethereum, Monero, Litecoin, Bitcoin Cash, and Ripple wallet addresses
- **Extract social media handles** — Find Twitter/X, Instagram, and Telegram usernames and links
- **Detect API keys** — Discover exposed AWS keys, Google API keys, and other credentials
- **Keyword matching** — Check whether your search term appears on each crawled page

## Use cases

- **Threat intelligence** — Monitor the dark web for leaked credentials, stolen data, or mentions of your organization
- **Brand protection** — Detect unauthorized use of your brand name or products on hidden services
- **Security research** — Discover exposed API keys, wallet addresses, and sensitive data on `.onion` sites
- **OSINT investigations** — Map dark web site structures, discover linked hidden services, and extract contact information
- **Cryptocurrency tracking** — Find wallet addresses associated with dark web activity

## Input

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| Search Keyword | String | — | Keyword to search dark web search engines. The scraper will find relevant `.onion` sites and crawl them. |
| Start URLs | URL List | — | Direct `.onion` URLs to crawl. Must be valid Tor hidden service addresses. |
| Max Crawl Depth | Integer | 2 | Maximum link depth to follow from seed pages. Set to 0 to only scrape the provided URLs without following links. |
| Max Pages to Crawl | Integer | 50 | Maximum number of pages to fetch during the crawl. Higher values mean longer run time. |
| Max Output Items | Integer | 100 | Maximum number of items to include in the output dataset. |

**Note:** At least one of **Search Keyword** or **Start URLs** must be provided.

### Example input — Search mode

```json
{
    "search": "marketplace",
    "maxDepth": 2,
    "maxPages": 20,
    "maxItems": 20
}
```

### Example input — Direct URL mode

```json
{
    "startUrls": [
        { "url": "http://xjfbpuj56rdazx4iolylxplbvyft2onuerjeimlcqwaihp3s6r4xebqd.onion/" }
    ],
    "maxDepth": 1,
    "maxPages": 10
}
```

## Output

Each crawled page produces one item in the output dataset with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| url | String | The `.onion` page URL that was scraped |
| title | String | The page title extracted from the HTML `<title>` tag |
| links | Array | All links discovered on the page (both `.onion` and clearnet) |
| emails | Array | Email addresses found on the page |
| phones | Array | Phone numbers found on the page |
| cryptoAddresses | Object | Cryptocurrency wallet addresses grouped by type (bitcoin, ethereum, monero, etc.) |
| misc | Object | Social media handles (twitter, instagram, telegram) and API keys |
| searchKeywordFound | Boolean | Whether the search keyword was found on this page |

### Sample output

```json
{
    "url": "http://xjfbpuj56rdazx4iolylxplbvyft2onuerjeimlcqwaihp3s6r4xebqd.onion/",
    "title": "Dark Market - Home",
    "links": [
        "http://xjfbpuj56rdazx4iolylxplbvyft2onuerjeimlcqwaihp3s6r4xebqd.onion/faq/",
        "http://xjfbpuj56rdazx4iolylxplbvyft2onuerjeimlcqwaihp3s6r4xebqd.onion/support/",
        "http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/"
    ],
    "emails": ["contact@darkservice.onion"],
    "phones": ["+1-555-0123"],
    "cryptoAddresses": {
        "bitcoin": ["1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"],
        "monero": ["4AdUndXHHZ6cfufTMvppY6JwXNouMBzSkbLYfpAV5Usx3skxNgYeYTRj5UzqtReoS44qo9mtmXCqY45DJ852K5Jv2684Rge"]
    },
    "misc": {
        "twitter": ["@darkmarket"],
        "telegram": ["@darkmarketgroup"]
    },
    "searchKeywordFound": true
}
```

## How to use

### Search the dark web

1. Enter a keyword in the **Search Keyword** field (e.g., "marketplace", "forum", "leaked data")
2. Set **Max Crawl Depth** to control how deep the crawler follows links (0 = only search results, 2+ = follow links from results)
3. Set **Max Pages** to limit the crawl scope
4. Click **Start** and wait for results

### Crawl specific .onion sites

1. Add one or more `.onion` URLs to the **Start URLs** field
2. Set **Max Crawl Depth** to 0 to only scrape the provided pages, or higher to follow links
3. Click **Start**

### Combine both modes

You can provide both a search keyword and start URLs. The scraper will merge all discovered URLs and crawl them together, removing duplicates.

## Tips

- **Start small** — Use `maxDepth: 0` and `maxPages: 5` for your first run to see how the actor works
- **Dark web sites are unreliable** — Many `.onion` sites go offline frequently. If a site is unreachable, the scraper will skip it and continue with other URLs
- **Tor is slow** — Connecting through the Tor network adds latency. Expect each page to take 5-30 seconds to load
- **No proxy needed** — The actor bundles its own Tor daemon, so you don't need to configure any proxy or pay extra for proxy services
- **Keyword search** — Use specific, relevant keywords for better results. Generic terms may return many unrelated pages

## Limitations

- The actor can only access `.onion` (Tor hidden service) URLs. Regular websites are not crawled
- Dark web search engine results depend on what has been indexed. Not all `.onion` sites are discoverable via search
- Some hidden services use CAPTCHAs or anti-bot measures that may prevent scraping
- Tor circuit establishment takes 10-30 seconds at the start of each run
- The actor does not render JavaScript. Sites that require JavaScript for content display may return incomplete data

## FAQ

**Is it legal to scrape the dark web?**
Accessing the dark web via Tor is legal in most jurisdictions. However, the legality depends on what you do with the data. This tool is intended for security research, OSINT, and threat intelligence. Always comply with applicable laws.

**Do I need a proxy to use this actor?**
No. The actor includes a built-in Tor daemon that handles all network routing automatically. No additional proxy configuration is needed.

**How fast is the scraping?**
Tor connections are inherently slower than regular internet. Expect 5-30 seconds per page depending on the hidden service's responsiveness. A typical run with 10 pages completes in 2-5 minutes.

**Why are some pages not scraped?**
Dark web sites have high failure rates. Sites may be temporarily offline, overloaded, or have moved to a new `.onion` address. The scraper will skip unreachable pages and continue with others.

**What cryptocurrency addresses are detected?**
The scraper identifies Bitcoin (BTC), Ethereum (ETH), Monero (XMR), Litecoin (LTC), Bitcoin Cash (BCH), and Ripple (XRP) wallet addresses.

**Can I scrape a specific .onion site deeply?**
Yes. Add the site URL to **Start URLs**, set **Max Crawl Depth** to 3-5, and increase **Max Pages** to allow thorough crawling of the site's internal pages.

**What happens if Tor fails to connect?**
The actor will wait up to 2 minutes for Tor to establish a connection. If it fails, the run will end with an error message suggesting you retry.

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/darkweb-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
