# Twitter Keywords Scraper Tutorial: Run This Apify Actor with Python

Extract tweets from Twitter/X based on keywords. Scrapes tweet text, usernames, engagement metrics, media, and timestamps for multiple search terms.

This repository shows how to run [Twitter Keywords Scraper](https://apify.com/crawlerbros/twitter-keywords-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/twitter-keywords-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/twitter-keywords-scraper](https://apify.com/crawlerbros/twitter-keywords-scraper)
- **SEO title:** Twitter Keywords Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Extract tweets from Twitter/X based on keywords. Scrapes tweet text, usernames, engagement metrics, media, and timestamps for multiple search terms.

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

# Twitter Keywords Scraper

A powerful Apify actor that scrapes tweets from Twitter/X based on keyword searches. Collect tweets with full engagement metrics, media, hashtags, and more - all with built-in anti-detection measures and human-like behavior simulation.

## 🌟 Features

- **Keyword-Based Search**: Search for any keyword, phrase, or hashtag
- **Rich Data Extraction**: Captures tweet text, author info, timestamps, and engagement metrics
- **Engagement Metrics**: Likes, retweets, replies, bookmarks, and view counts
- **Media Support**: Extracts images, videos, and their thumbnails
- **Hashtag & Mention Extraction**: Automatically identifies hashtags and mentions
- **URL Extraction**: Captures all URLs shared in tweets
- **Anti-Detection**: Built-in stealth mode with browser fingerprint masking
- **Human Behavior Simulation**: Random delays, mouse movements, and scrolling
- **Authenticated Scraping**: Uses cookies for better access and rate limit handling
- **Configurable**: Customizable tweet limits, delays, and behavior settings
- **Apify Integration**: Seamlessly integrates with Apify platform for data export and workflows

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Input Configuration](#-input-configuration)
- [Output Format](#-output-format)
- [Authentication Setup](#-authentication-setup)
- [Usage Examples](#-usage-examples)
- [Best Practices](#-best-practices)
- [Troubleshooting](#-troubleshooting)
- [Local Development](#-local-development)
- [FAQ](#-faq)

## 🚀 Quick Start

### On Apify Platform

1. **Create an account** on [Apify](https://apify.com/)
2. **Deploy this actor** to your account
3. **Configure input** with your keywords
4. **Run the actor** and view results in the dataset

### Minimal Input Example

```json
{
  "keywords": ["artificial intelligence", "machine learning"],
  "maxTweets": 20
}
```

## ⚙️ Input Configuration

### Parameters

| Parameter                 | Type          | Required | Default | Description                              |
| ------------------------- | ------------- | -------- | ------- | ---------------------------------------- |
| `keywords`                | Array[String] | ✅ Yes   | -       | Keywords or phrases to search for        |
| `maxTweets`               | Number        | No       | 20      | Maximum tweets to collect per keyword    |
| `minDelayBetweenRequests` | Number        | No       | 2       | Minimum delay between requests (seconds) |
| `maxDelayBetweenRequests` | Number        | No       | 5       | Maximum delay between requests (seconds) |
| `humanizeBehavior`        | Boolean       | No       | true    | Enable human-like behavior simulation    |

### Full Input Example

```json
{
  "keywords": [
    "web scraping",
    "data mining",
    "#AI",
    "machine learning tutorial"
  ],
  "maxTweets": 50,
  "minDelayBetweenRequests": 3,
  "maxDelayBetweenRequests": 7,
  "humanizeBehavior": true
}
```

### Sample Inputs

Check the `sample-inputs/` directory for pre-configured examples:

- **basic-tech-keywords.json** - Simple tech keywords
- **marketing-brand-monitoring.json** - Brand monitoring
- **crypto-finance.json** - Cryptocurrency topics
- **news-trending.json** - News and trending topics
- **sports-entertainment.json** - Sports monitoring
- **hashtag-monitoring.json** - Hashtag tracking
- And more...

## 📊 Output Format

The actor pushes each tweet to the Apify dataset with the following structure:

```json
{
  "tweet_id": "1234567890123456789",
  "tweet_url": "https://twitter.com/username/status/1234567890123456789",
  "keyword": "artificial intelligence",
  "text": "This is an example tweet about AI and machine learning...",
  "author_name": "John Doe",
  "author_username": "johndoe",
  "timestamp": "2025-11-01T09:15:30.000Z",
  "replies_count": 42,
  "retweets_count": 128,
  "likes_count": 456,
  "bookmarks_count": 23,
  "views_count": 12500,
  "media_urls": [
    {
      "type": "image",
      "url": "https://pbs.twimg.com/media/..."
    }
  ],
  "hashtags": ["AI", "MachineLearning"],
  "mentions": ["elonmusk", "OpenAI"],
  "urls": ["https://example.com/article"],
  "scraped_at": "2025-11-01T09:16:30.123Z"
}
```

### Output Fields

| Field             | Type          | Description                          |
| ----------------- | ------------- | ------------------------------------ |
| `tweet_id`        | String        | Unique identifier for the tweet      |
| `tweet_url`       | String        | Direct URL to the tweet              |
| `keyword`         | String        | Search keyword that found this tweet |
| `text`            | String        | Full tweet text content              |
| `author_name`     | String        | Display name of the tweet author     |
| `author_username` | String        | Twitter username (without @)         |
| `timestamp`       | String        | ISO 8601 timestamp of tweet creation |
| `replies_count`   | Number        | Number of replies                    |
| `retweets_count`  | Number        | Number of retweets/reposts           |
| `likes_count`     | Number        | Number of likes                      |
| `bookmarks_count` | Number        | Number of bookmarks                  |
| `views_count`     | Number        | Number of views                      |
| `media_urls`      | Array         | Media objects with type and URL      |
| `hashtags`        | Array[String] | Hashtags mentioned (without #)       |
| `mentions`        | Array[String] | Users mentioned (without @)          |
| `urls`            | Array[String] | URLs shared in the tweet             |
| `scraped_at`      | String        | ISO 8601 timestamp when scraped      |

### Data Export

The dataset can be exported in multiple formats:

- **JSON** - Full structured data
- **CSV** - Spreadsheet compatible
- **Excel** - .xlsx format
- **HTML** - Web-ready table
- **RSS** - Feed format
- **XML** - Structured markup

## 🔐 Authentication Setup

For better access and to avoid rate limits, you need to provide Twitter authentication cookies.

### Quick Guide

1. **Log in to Twitter/X** in your browser
2. **Open Developer Tools** (F12 or Right-click → Inspect)
3. **Go to Application/Storage** tab
4. **Find Cookies** for `x.com` or `twitter.com`
5. **Update the cookies** in `src/main.py` (see the `HARDCODED_COOKIES` variable)

### Important Cookies

The essential cookies you need:

- `auth_token` - Authentication token
- `ct0` - CSRF token
- `twid` - Twitter ID
- `kdt` - Session token

📖 **Detailed Guide**: See [HOW_TO_GET_COOKIES.md](HOW_TO_GET_COOKIES.md) for step-by-step instructions with screenshots.

### Cookie Maintenance

- Cookies typically expire after 30-60 days
- Update cookies when you see authentication errors
- Use an active Twitter account for better reliability

## 💡 Usage Examples

### Example 1: Tech News Monitoring

Monitor technology trends and discussions:

```json
{
  "keywords": ["ChatGPT", "GPT-4", "OpenAI", "#TechNews"],
  "maxTweets": 30,
  "minDelayBetweenRequests": 3,
  "maxDelayBetweenRequests": 6,
  "humanizeBehavior": true
}
```

### Example 2: Brand Sentiment Analysis

Track brand mentions and customer feedback:

```json
{
  "keywords": ["YourBrand customer service", "YourBrand review", "@YourBrand"],
  "maxTweets": 100,
  "minDelayBetweenRequests": 4,
  "maxDelayBetweenRequests": 8,
  "humanizeBehavior": true
}
```

### Example 3: Quick Research

Fast data collection for research purposes:

```json
{
  "keywords": ["climate change research"],
  "maxTweets": 50,
  "minDelayBetweenRequests": 2,
  "maxDelayBetweenRequests": 4,
  "humanizeBehavior": true
}
```

### Example 4: Hashtag Campaign Tracking

Monitor hashtag campaigns and engagement:

```json
{
  "keywords": ["#YourCampaign2025", "#BrandHashtag"],
  "maxTweets": 200,
  "minDelayBetweenRequests": 5,
  "maxDelayBetweenRequests": 10,
  "humanizeBehavior": true
}
```

## ✅ Best Practices

### Keyword Selection

- **Be Specific**: Use specific phrases instead of single words
  - ✅ Good: "iPhone 15 Pro review"
  - ❌ Too broad: "phone"
- **Use Quotes**: For exact phrase matching (in Twitter search)
- **Include Hashtags**: Add # for hashtag searches
- **Mix Keywords**: Combine different variations of your topic

### Rate Limiting

- **Start Small**: Begin with 1-2 keywords and 10-20 tweets
- **Increase Gradually**: Scale up as you confirm it works
- **Use Delays**: Keep delays between 2-7 seconds
- **Enable Humanization**: Always use `humanizeBehavior: true`
- **Monitor Logs**: Watch for warnings or blocks

### Data Quality

- **Verify Results**: Check a few tweets manually
- **Update Cookies**: Keep authentication fresh
- **Handle Errors**: Log and investigate failed keywords
- **Deduplicate**: Tweet IDs help prevent duplicates

### Performance

- **Parallel Processing**: The actor processes keywords sequentially to avoid detection
- **Optimal Settings**: 20-50 tweets per keyword is usually optimal
- **Time Estimates**: ~30-60 seconds per keyword (depends on settings)

## 🔧 Troubleshooting

### No Tweets Collected

**Possible Causes:**

- Keywords too specific or no recent tweets
- Authentication cookies expired
- Twitter rate limiting

**Solutions:**

1. Try broader keywords
2. Update authentication cookies
3. Increase delays and enable humanization
4. Check Twitter manually for the search results

### Authentication Errors

**Symptoms:**

- "⚠️ Cookies may be expired - not logged in"
- Login page appears

**Solutions:**

1. Follow [HOW_TO_GET_COOKIES.md](HOW_TO_GET_COOKIES.md) to get fresh cookies
2. Update `HARDCODED_COOKIES` in `src/main.py`
3. Ensure cookies are from an active account

### Rate Limiting / Blocks

**Symptoms:**

- "❌ BLOCKED" messages
- "Rate limit exceeded" warnings
- Fewer tweets than expected

**Solutions:**

1. Increase `minDelayBetweenRequests` to 5-10 seconds
2. Increase `maxDelayBetweenRequests` to 10-15 seconds
3. Reduce `maxTweets` per keyword
4. Enable `humanizeBehavior`
5. Wait 15-30 minutes before retrying

### Missing Engagement Metrics

**Symptoms:**

- Tweets extracted but metrics show 0

**Possible Causes:**

- Twitter's HTML structure changed
- Tweets loaded but metrics not rendered

**Solutions:**

1. Increase wait times in the code
2. Report the issue for code updates
3. Tweets will still have text and author info

### Slow Scraping

**Symptoms:**

- Takes longer than expected

**Causes:**

- High delay settings
- Humanization enabled (intentional)
- Many keywords or high `maxTweets`

**Solutions:**

- This is often intentional for safety
- Reduce delays only if necessary (risky)
- Process fewer keywords per run
- Disable humanization for testing (not recommended for production)

## 🖥️ Local Development

### Prerequisites

- Python 3.11+
- pip (Python package manager)

### Installation

1. **Clone the repository**

   ```bash
   cd Twitter-Keywords
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers**

   ```bash
   playwright install firefox
   ```

4. **Update authentication cookies**
   - Edit `src/main.py`
   - Update the `HARDCODED_COOKIES` list with your cookies

### Running Locally

1. **Create input file**

   ```bash
   mkdir -p storage/key_value_stores/default
   ```

2. **Add input.json**

   ```bash
   cp sample-inputs/basic-tech-keywords.json storage/key_value_stores/default/INPUT.json
   ```

3. **Run the actor**

   ```bash
   apify run
   ```

   Or directly with Python:

   ```bash
   python -m src.main
   ```

### Project Structure

```
Twitter-Keywords/
├── .actor/
│   ├── actor.json          # Actor configuration
│   └── input_schema.json   # Input validation schema
├── src/
│   ├── __main__.py         # Entry point
│   └── main.py             # Main scraper logic
├── sample-inputs/          # Example configurations
│   ├── basic-tech-keywords.json
│   ├── marketing-brand-monitoring.json
│   ├── crypto-finance.json
│   └── ... (more examples)
├── storage/                # Local storage for Apify
│   ├── key_value_stores/
│   └── datasets/
├── Dockerfile              # Container configuration
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── QUICKSTART.md          # Quick start guide
└── HOW_TO_GET_COOKIES.md  # Cookie extraction guide
```

## ❓ FAQ

### Q: How many tweets can I scrape?

**A:** Technically unlimited, but practically:

- Start with 10-50 tweets per keyword
- Monitor for rate limiting
- Scale gradually based on results

### Q: Do I need to pay for Twitter API?

**A:** No! This scraper uses web scraping, not the Twitter API. You only need a free Twitter account for authentication cookies.

### Q: How often should I update cookies?

**A:** Cookies typically last 30-60 days. Update when:

- You see authentication errors
- The scraper shows login pages
- After changing your Twitter password

### Q: Can I scrape tweets from specific users?

**A:** Yes! Use keywords like:

- `from:username` - tweets from a specific user
- `to:username` - tweets mentioning a user
- `@username` - tweets mentioning a user

### Q: Will my account get banned?

**A:** Risk is low if you:

- Use reasonable delays (2-7 seconds)
- Enable humanization
- Don't scrape excessively
- Use a genuine account

### Q: Can I scrape historical tweets?

**A:** This scraper focuses on recent/live tweets. Twitter's search is limited to recent content. For historical tweets, you'd need different approaches or Twitter API access.

### Q: What's the difference between `retweets_count` and `likes_count`?

**A:**

- `retweets_count`: How many times the tweet was retweeted/reposted
- `likes_count`: How many users liked/favorited the tweet
- `replies_count`: How many replies the tweet received
- `bookmarks_count`: How many users bookmarked the tweet
- `views_count`: How many times the tweet was viewed

### Q: Can I run multiple scrapers simultaneously?

**A:** Not recommended with the same account cookies. Twitter may detect parallel sessions and block access. Run scrapers sequentially.

### Q: How do I integrate this with my app/workflow?

**A:** Via Apify platform:

- Use webhooks to trigger on completion
- Call via Apify API
- Export data to cloud storage
- Integrate with Zapier, Make, or custom apps

### Q: The scraper is missing some tweets, why?

**A:** Possible reasons:

- Twitter's ranking algorithm (not all tweets shown)
- Rate limiting kicked in
- Tweets deleted/protected while scraping
- `maxTweets` limit reached

### Q: Can I get tweets in languages other than English?

**A:** Yes! Use keywords in any language. The scraper captures text in any language that Twitter supports.

## 📝 Notes

- **Respect Twitter's Terms of Service**: Use this tool responsibly
- **Rate Limiting**: Twitter implements rate limits; respect them
- **Data Privacy**: Be mindful of user privacy when collecting data
- **Commercial Use**: Review Twitter's terms for commercial data usage
- **Maintenance**: Twitter's HTML structure may change, requiring code updates

## 🤝 Contributing

Contributions are welcome! If you find bugs or have feature suggestions:

1. Test your changes locally
2. Update documentation as needed
3. Submit detailed bug reports or feature requests

## 📄 License

This actor is provided as-is for educational and research purposes. Users are responsible for complying with Twitter's Terms of Service and applicable laws.

## 🆘 Support

- **Issues**: Report bugs and request features
- **Documentation**: Check QUICKSTART.md and HOW_TO_GET_COOKIES.md
- **Community**: Share your use cases and tips

---

**Made with ❤️ for the Apify community**

_Last updated: November 2025_

## Files

- `main.py` - minimal Python runner for the Apify API.
- `main_apify_client.py` - equivalent runner using the official Apify Python client.
- `input.example.json` - empty input placeholder; copy it to `input.json` and fill it from the actor README.
- `.env.example` - environment variables used by the runner.
- `.gitignore` - keeps `.env`, `input.json`, and Python cache files out of commits.
- `requirements.txt` - Python dependencies for both runners.
- `LICENSE` - MIT license.

## Links

- [Run this actor on Apify](https://apify.com/crawlerbros/twitter-keywords-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
