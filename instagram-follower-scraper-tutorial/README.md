# Instagram Followers & Following Scraper Tutorial: Run This Apify Actor with Python

Scrape Instagram followers and following lists. Extract username, display name, verification status, privacy flag, and profile picture for every account. Supports followers, following, or both modes across multiple profiles with configurable limits.

This repository shows how to run [Instagram Followers & Following Scraper](https://apify.com/crawlerbros/instagram-follower-scraper) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/instagram-follower-scraper`
- **Apify Store:** [https://apify.com/crawlerbros/instagram-follower-scraper](https://apify.com/crawlerbros/instagram-follower-scraper)
- **SEO title:** Instagram Followers & Following Scraper Tutorial: Run This Apify Actor with Python
- **Description:** Scrape Instagram followers and following lists. Extract username, display name, verification status, privacy flag, and profile picture for every account. Supports followers, following, or both modes across multiple profiles with configurable limits.

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

## Instagram Followers & Following Scraper

Scrape **Instagram** followers and following lists from any public profile. Enter one or more usernames (or full profile URLs), choose whether you want followers, following, or both, and get structured records with username, display name, verification status, privacy flag, and profile picture. Enable full-profile enrichment to additionally pull follower counts, bio, post count, business category, and external link. Supports unlimited pagination — every user in the list is captured until complete.

### What this actor does

- **Three scrape modes:** `followers`, `following`, or `both` lists in a single run
- **Multiple profiles:** process any number of Instagram accounts in one run, each capped independently
- **Reliable pagination:** captures every user in the list without duplicates or missed pages
- **Flexible username input:** accepts plain usernames (`natgeo`), `@natgeo` format, or full profile URLs (`https://www.instagram.com/natgeo/`)
- **Non-existent profiles handled gracefully** — a record is still output with a `status` field set to `"This profile doesn't exist"` so no input is silently dropped

### Authentication

This actor requires Instagram session cookies to access follower and following lists (Instagram does not expose these to logged-out users). You can either:

1. **Paste your own cookies** — export from a logged-in browser session using a tool such as [Cookie-Editor](https://cookie-editor.cgagnier.ca/) and paste the JSON into the `cookies` field.
2. **Leave the cookies field blank** — the actor will automatically use a managed pool of shared Instagram sessions. This is the recommended option for most users.

If your cookies expire mid-run, re-export them from your browser and restart the actor.

### Output per follower / following record

**Always present**

- `username` — Instagram handle
- `user_id` — numeric Instagram user ID
- `full_name` — display name on the profile
- `is_verified` — `true` if the account has a blue verification badge
- `is_private` — `true` if the account is private
- `profile_pic_url` — CDN URL of the profile picture
- `profile_pic_id` — internal media ID for the profile picture (`""` when not available)
- `profile_url` — URL of the source profile being scraped
- `profile_username` — username of the source profile being scraped
- `scrape_type` — `"followers"` or `"following"`
- `scraped_at` — ISO 8601 timestamp of when the record was collected
- `status` — `"success"` for valid records; `"This profile doesn't exist"` when the username was not found on Instagram

### Input

| Field | Type | Default | Description |
|---|---|---|---|
| `usernames` | array | `["instagram"]` | Usernames, `@username` handles, or full Instagram profile URLs |
| `scrapeType` | string | `followers` | `followers` — followers only; `following` — following only; `both` — both lists |
| `maxFollowersPerProfile` | integer | `100` | Maximum users to return per profile per list. `0` = unlimited |
| `cookies` | string | – | Instagram cookies in JSON format. Leave blank to use the managed session pool |
| `sessionName` | string | – | Key-value store key for a previously saved session (advanced use) |

#### Example: scrape followers of a single account

```json
{
  "usernames": ["natgeo"],
  "scrapeType": "followers",
  "maxFollowersPerProfile": 200
}
````

#### Example: multiple profiles, following only

```json
{
  "usernames": ["natgeo", "nasa", "instagram"],
  "scrapeType": "following",
  "maxFollowersPerProfile": 100
}
```

#### Example: full crawl with your own cookies

```json
{
  "usernames": ["natgeo"],
  "scrapeType": "followers",
  "maxFollowersPerProfile": 0,
  "cookies": "[{\"name\":\"sessionid\",\"value\":\"YOUR_SESSION_ID\",...}]"
}
```

### Example output

```json
{
  "username": "john_doe",
  "user_id": "1234567890",
  "full_name": "John Doe",
  "is_verified": false,
  "is_private": false,
  "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/avatar.jpg",
  "profile_pic_id": "3852537424986049577",
  "profile_url": "https://www.instagram.com/natgeo/",
  "profile_username": "natgeo",
  "scrape_type": "followers",
  "scraped_at": "2026-07-03T07:00:00.000Z",
  "status": "success"
}
```

### Use cases

- **Competitor analysis** — see who follows your competitors and identify potential customers or brand advocates
- **Influencer research** — audit an influencer's audience before a collaboration: privacy ratio, verification density, account categories
- **Lead generation** — extract follower lists from niche community accounts to build outreach lists
- **Community mapping** — understand the overlap between two brands' audiences by scraping both following lists
- **Market research** — identify business accounts following a target profile using the `is_business` and `category` fields
- **Account monitoring** — track follower growth or churn by comparing periodic scrapes of the same profile

### FAQ

**Do I need an Instagram account to use this actor?**
The actor accesses Instagram as a logged-in user because Instagram hides follower/following lists from logged-out visitors. You can either provide your own cookies or leave the field blank and use the built-in managed session pool.

**Will this work on private accounts?**
The logged-in session used must follow the private account in order to see its followers or following list. If the session does not follow the account, the actor will return zero results for that profile.

**How many followers can I scrape per run?**
There is no hard limit — set `maxFollowersPerProfile` to `0` for an unlimited crawl. Very large accounts (100K+ followers) will take longer to complete.

**Why does the scraped follower count differ from the number shown on the profile?**
Instagram's displayed follower count includes deactivated, suspended, and deleted accounts that do not appear in the actual followers list. It is normal for the scraped count to be somewhat lower than the displayed figure.

**What happens if a username doesn't exist?**
The actor still outputs a record for that username with all string fields set to `""`, boolean fields to `false`, and `status` set to `"This profile doesn't exist"`. No input is silently dropped.

**How fresh is the data?**
Data is scraped live at the time of the run. Instagram follower lists reflect the current state of the account at the moment of scraping.

**Is this actor affiliated with Instagram or Meta?**
No. This is an independent third-party tool that automates interaction with the public Instagram website. It is not endorsed by or affiliated with Meta Platforms, Inc.

### Other Instagram Scrapers

Want to get other data from Instagram? Check out our complete suite of Instagram scrapers:

| Actor | Description |
|---|---|
| [Instagram Post Scraper](https://apify.com/crawlerbros/instagram-post-scraper) | Scrape public posts, reels, IGTV, and carousel posts from direct URLs — no login or cookies required |
| [Instagram Comment Scraper](https://apify.com/crawlerbros/instagram-comment-scraper) | Scrape comments from any Instagram post or reel |
| [Instagram Profile Scraper](https://apify.com/crawlerbros/instagram-profile-scraper) | Extract profile data, bio, follower counts, and more |
| [Instagram Tagged Posts Scraper](https://apify.com/crawlerbros/instagram-tagged-posts-scraper) | Collect posts where a user has been tagged |
| [Instagram Hashtag Scraper](https://apify.com/crawlerbros/instagram-hashtag-scraper) | Scrape posts and profiles by hashtag |
| [Instagram Story Downloader](https://apify.com/crawlerbros/instagram-story-downloader) | Download stories from Instagram profiles |
| [Instagram Downloader API](https://apify.com/crawlerbros/instagram-downloader-api) | Download photos, videos, and reels from Instagram |
| [Instagram Keyword Scraper](https://apify.com/crawlerbros/instagram-keyword-scraper) | Search and scrape posts by keyword |
| [Instagram Keyword Search Scraper](https://apify.com/crawlerbros/instagram-keyword-search-scraper) | Search Instagram accounts and posts by keyword |
| [Instagram Transcript Scraper](https://apify.com/crawlerbros/instagram-transcript-scraper) | Extract transcripts from Instagram video content |

# Actor input Schema

## `usernames` (type: `array`):

Enter Instagram usernames to scrape (e.g., 'natgeo', 'nasa'). You can also use full profile URLs.

## `scrapeType` (type: `string`):

Choose to scrape followers, following, or both lists from each profile.

## `maxFollowersPerProfile` (type: `integer`):

Maximum number of followers/following to extract per profile. Instagram typically allows 100-200 per session. Set to 0 for unlimited.

## `cookies` (type: `string`):

Instagram authentication cookies in JSON format. Optional — if not provided, authentication is handled automatically. Format: \[{"name":"sessionid","value":"...","domain":".instagram.com"}, ...]

## `sessionName` (type: `string`):

If you've saved cookies to key-value storage, enter the session name here instead of pasting cookies.

## Actor input object example

```json
{
  "usernames": [
    "natgeo",
    "nasa",
    "instagram"
  ],
  "scrapeType": "followers",
  "maxFollowersPerProfile": 100,
  "cookies": "[{\"name\":\"sessionid\",\"value\":\"your_session_id\",\"domain\":\".instagram.com\",\"path\":\"/\",\"secure\":true,\"httpOnly\":true}]"
}
```

# Actor output Schema

## `results` (type: `string`):

No description

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
    "usernames": [
        "instagram"
    ]
};

// Run the Actor and wait for it to finish
const run = await client.actor("crawlerbros/instagram-follower-scraper").call(input);

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
run_input = { "usernames": ["instagram"] }

# Run the Actor and wait for it to finish
run = client.actor("crawlerbros/instagram-follower-scraper").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
print("💾 Check your data here: https://console.apify.com/storage/datasets/" + run["defaultDatasetId"])
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# 📚 Want to learn more 📖? Go to → https://docs.apify.com/api/client/python/docs/quick-start

```

## CLI example

```bash
echo '{
  "usernames": [
    "instagram"
  ]
}' |
apify call crawlerbros/instagram-follower-scraper --silent --output-dataset

```

## MCP server setup

```json
{
    "mcpServers": {
        "apify": {
            "command": "npx",
            "args": [
                "mcp-remote",
                "https://mcp.apify.com/?tools=crawlerbros/instagram-follower-scraper",
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
        "title": "Instagram Followers & Following Scraper",
        "description": "Scrape Instagram followers and following lists. Extract username, display name, verification status, privacy flag, and profile picture for every account. Supports followers, following, or both modes across multiple profiles with configurable limits.",
        "version": "1.0",
        "x-build-id": "Jgtoz68jBBWLtaDLW"
    },
    "servers": [
        {
            "url": "https://api.apify.com/v2"
        }
    ],
    "paths": {
        "/acts/crawlerbros~instagram-follower-scraper/run-sync-get-dataset-items": {
            "post": {
                "operationId": "run-sync-get-dataset-items-crawlerbros-instagram-follower-scraper",
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
        "/acts/crawlerbros~instagram-follower-scraper/runs": {
            "post": {
                "operationId": "runs-sync-crawlerbros-instagram-follower-scraper",
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
        "/acts/crawlerbros~instagram-follower-scraper/run-sync": {
            "post": {
                "operationId": "run-sync-crawlerbros-instagram-follower-scraper",
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
                "required": [
                    "usernames"
                ],
                "properties": {
                    "usernames": {
                        "title": "Instagram Usernames",
                        "type": "array",
                        "description": "Enter Instagram usernames to scrape (e.g., 'natgeo', 'nasa'). You can also use full profile URLs.",
                        "items": {
                            "type": "string"
                        }
                    },
                    "scrapeType": {
                        "title": "What to Scrape",
                        "enum": [
                            "followers",
                            "following",
                            "both"
                        ],
                        "type": "string",
                        "description": "Choose to scrape followers, following, or both lists from each profile.",
                        "default": "followers"
                    },
                    "maxFollowersPerProfile": {
                        "title": "Max Users Per Profile",
                        "minimum": 0,
                        "maximum": 10000,
                        "type": "integer",
                        "description": "Maximum number of followers/following to extract per profile. Instagram typically allows 100-200 per session. Set to 0 for unlimited.",
                        "default": 100
                    },
                    "cookies": {
                        "title": "Instagram Cookies (Optional)",
                        "type": "string",
                        "description": "Instagram authentication cookies in JSON format. Optional — if not provided, authentication is handled automatically. Format: [{\"name\":\"sessionid\",\"value\":\"...\",\"domain\":\".instagram.com\"}, ...]"
                    },
                    "sessionName": {
                        "title": "Saved Session Name (Optional)",
                        "type": "string",
                        "description": "If you've saved cookies to key-value storage, enter the session name here instead of pasting cookies."
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

- [Run this actor on Apify](https://apify.com/crawlerbros/instagram-follower-scraper)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
