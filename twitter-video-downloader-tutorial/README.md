# Twitter Video Downloader

Download videos from Twitter/X posts

This repository shows how to run [Twitter Video Downloader](https://apify.com/crawlerbros/twitter-video-downloader) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/twitter-video-downloader`
- **Apify Store:** [https://apify.com/crawlerbros/twitter-video-downloader](https://apify.com/crawlerbros/twitter-video-downloader)
- **SEO title:** Twitter Video Downloader
- **Description:** Download videos from Twitter/X posts. Supports direct post URLs and username-based scraping.

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

## Twitter / X Media Downloader

Download videos, photos, and GIFs from any public **Twitter / X** post — no login required for direct post URLs. Paste a link, hit run, and get the file plus a direct download URL that works anywhere.

You can also pass usernames to automatically pull media from a user's recent posts (cookie-authenticated, with a built-in cookie pool fallback).

### What you get

Each downloaded file produces one dataset record:

| Field | Description |
| --- | --- |
| `tweet_url` | Original tweet URL |
| `tweet_id` | Tweet ID |
| `scraped_from` | Username whose profile this post was found on (`null` for direct URLs) |
| `uploader` | Twitter handle of whoever posted the media |
| `is_retweet` | `true` if the post is a retweet |
| `is_quote_tweet` | `true` if the post quotes another tweet |
| `media_origin` | `"self"` = media from the tweet itself, `"quoted"` = media from a quoted tweet |
| `media_type` | `"video"`, `"photo"`, or `"gif"` |
| `media_url` | Original Twitter CDN URL of the media |
| `thumbnail_url` | Preview thumbnail URL (when present) |
| `filename` | Saved file name |
| `filesize_bytes` | File size in bytes |
| `storage_key` | Key used to store the file in the Apify Key-Value Store |
| `download_url` | **Signed direct download URL** — works in any browser or `curl` |
| `download_status` | `"finished"` or `"failed"` |
| `error` | Error message (only when `download_status="failed"`) |
| `downloaded_at` | ISO 8601 UTC timestamp |
| `media_stats` | Resolution, duration, codec, bitrate, aspect ratio (where applicable) |

Empty fields are dropped from each record so the dataset stays clean.

#### `media_stats` fields

| Stat | Applies to | Example |
|---|---|---|
| `width` / `height` | All media | `1920 / 1080` |
| `fps` | Videos / GIFs | `30.0` |
| `duration` | Videos / GIFs | `45.23` (seconds) |
| `video_codec` | Videos / GIFs | `"h264"` |
| `ext` | All media | `"mp4"`, `"png"`, `"jpg"` |
| `filesize_bytes` | All media | `28640256` |
| `total_bitrate_kbps` | Videos | `5064.12` |
| `aspect_ratio` | All media | `1.78` |

### Input

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `postUrls` | Array | `[]` | Tweet/post URLs to download media from. |
| `usernames` | Array | `[]` | Twitter handles to pull recent media from (without `@`). |
| `maxPostsPerUser` | Integer | `10` | Number of recent posts to check per username (1-100). |
| `browserCookies` | String | — | Optional Twitter/X session cookies (JSON). Improves reliability for username scraping; not needed for direct post URLs. |

You can mix `postUrls` and `usernames` in the same run.

#### Example input — single post

```json
{
  "postUrls": ["https://x.com/NASA/status/1234567890"]
}
````

#### Example input — username scrape

```json
{
  "usernames": ["NASA", "SpaceX"],
  "maxPostsPerUser": 25
}
```

#### Example input — mixed

```json
{
  "postUrls": ["https://x.com/elonmusk/status/9876543210"],
  "usernames": ["openai"],
  "maxPostsPerUser": 10
}
```

### Example output

#### Video

```json
{
  "tweet_url": "https://x.com/NASA/status/1234567890",
  "tweet_id": "1234567890",
  "scraped_from": null,
  "uploader": "NASA",
  "is_retweet": false,
  "is_quote_tweet": false,
  "media_origin": "self",
  "media_type": "video",
  "media_url": "https://video.twimg.com/ext_tw_video/.../pu/vid/1280x720/video.mp4",
  "thumbnail_url": "https://pbs.twimg.com/ext_tw_video_thumb/.../img/thumb.jpg",
  "filename": "1234567890_video_1.mp4",
  "filesize_bytes": 28640256,
  "storage_key": "1234567890_video_1.mp4",
  "download_url": "https://api.apify.com/v2/key-value-stores/{STORE_ID}/records/1234567890_video_1.mp4?signature=fDeGdoTU7pRBdtunucWD",
  "download_status": "finished",
  "downloaded_at": "2026-05-05T13:42:18Z",
  "media_stats": {
    "width": 1920,
    "height": 1080,
    "fps": 30.0,
    "duration": 45.23,
    "video_codec": "h264",
    "ext": "mp4",
    "filesize_bytes": 28640256,
    "total_bitrate_kbps": 5064.12,
    "aspect_ratio": 1.78
  }
}
```

#### Photo

```json
{
  "tweet_url": "https://x.com/NASA/status/9876543210",
  "tweet_id": "9876543210",
  "uploader": "NASA",
  "media_type": "photo",
  "media_url": "https://pbs.twimg.com/media/AbCdEf123.png?name=orig",
  "filename": "9876543210_photo_1.png",
  "filesize_bytes": 29387,
  "download_url": "https://api.apify.com/v2/key-value-stores/{STORE_ID}/records/9876543210_photo_1.png?signature=...",
  "download_status": "finished",
  "downloaded_at": "2026-05-05T13:42:18Z",
  "media_stats": {
    "width": 1200,
    "height": 675,
    "ext": "png",
    "filesize_bytes": 29387,
    "aspect_ratio": 1.78
  }
}
```

### Use cases

- **Content archival** — Backup tweets from accounts you care about (your own, journalists, NASA, etc.).
- **Repurposing** — Pull video/image assets for blog posts, presentations, or social repurposing.
- **Compliance** — Preserve evidence of public posts for legal or regulatory archives.
- **Media research** — Build labelled datasets of viral video/image content.
- **Account audit** — Pull every video a user has posted to review or migrate.

### FAQ

**Do I need a Twitter account?**
No. For direct post URLs, the actor downloads from public endpoints without authentication. Username scraping uses an internal cookie pool that works out of the box; supplying your own cookies via `browserCookies` improves reliability for heavy username workloads.

**What media types are supported?**
Videos, photos, and GIFs. The actor detects the type automatically and downloads everything in the tweet — if a post has 3 photos and 1 video, you get all 4 files.

**What about CMAF / fMP4 streaming videos?**
Twitter delivers some videos as fragmented MP4 streams (HLS/m3u8). The actor automatically detects this, picks the highest-quality variant, downloads all segments, and produces a single playable MP4.

**What does `media_origin` mean?**

- `"self"` — the media belongs to the tweet you linked.
- `"quoted"` — the tweet you linked quotes another tweet, and this media comes from that quoted tweet. `uploader` shows the original author.

**What does `scraped_from` mean?**
For username scraping, it tells you which profile the post was found on — useful when the post is a retweet (`uploader` is the original author, `scraped_from` is the user whose timeline produced the URL). For direct `postUrls`, it's `null`.

**Does it download the best quality available?**
Yes. Videos are downloaded at the highest variant Twitter exposes; photos at original (`?name=orig`) resolution.

**Are there any file-size limits?**
No. Files are streamed to disk and uploaded to Apify Key-Value Store, so multi-gigabyte videos work without running out of memory.

**Why is `download_url` signed?**
Apify Key-Value Store records require a signed URL for public access — the signature is appended automatically. You can paste the URL into any browser or `curl` and it will download the file directly.

**Can I download from private / protected accounts?**
Only by supplying cookies from an account that follows the protected profile. The actor cannot bypass Twitter's privacy controls.

**What happens if a download fails?**
Failed downloads still appear in the dataset with `download_status: "failed"` and a clear `error` (e.g. tweet deleted, media URL expired, rate limit). Successful downloads continue regardless.

**How long are the download links valid?**
Apify Key-Value Store retention depends on your plan — typically 7 days on the free tier, longer on paid plans. Re-run the actor or copy the file to your own storage for permanent archival.

**Can I use this on a schedule?**
Yes. Schedule the actor on the Apify platform to automatically pull new media from specific users at regular intervals (hourly, daily, etc.).

### Limitations

- Private / protected accounts require cookies from a follower.
- Tweets that were deleted before the run started cannot be retrieved.
- Twitter rate-limits aggressive crawling; very large username scrapes (50+ users × 100 posts each) may slow down or pause for cool-off.
- Download URLs are valid as long as your Apify storage retention allows.

# Actor input Schema

## `postUrls` (type: `array`):

List of Twitter/X post URLs to download videos from (e.g., https://x.com/username/status/123456)

## `usernames` (type: `array`):

List of Twitter/X usernames to scrape videos from (without @)

## `maxPostsPerUser` (type: `integer`):

Maximum number of posts to scrape per username (only for username mode)

## `browserCookies` (type: `string`):

**Required.** Twitter/X session cookies in JSON format for authenticated scraping. Twitter heavily restricts unauthenticated browsing — a valid session is mandatory. Format: \[{"name":"auth\_token","value":"...","domain":".x.com"}, ...]. Without cookies the run returns a single placeholder record indicating cookies are needed.

## Actor input object example

```json
{
  "postUrls": [
    "https://x.com/CoinMarketCap/status/2030012592282796096"
  ],
  "usernames": [
    "cristiano"
  ],
  "maxPostsPerUser": 3
}
```

# Actor output Schema

## `results` (type: `string`):

Dataset containing downloaded media metadata (tweet URL, uploader, media type, download status, file size, and media stats)

## `mediaFiles` (type: `string`):

Key-value store containing the actual downloaded video, photo, and GIF files

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
    "postUrls": [
        "https://x.com/CoinMarketCap/status/2030012592282796096"
    ],
    "usernames": [
        "cristiano"
    ],
    "maxPostsPerUser": 3,
    "browserCookies": ""
};

// Run the Actor and wait for it to finish
const run = await client.actor("crawlerbros/twitter-video-downloader").call(input);

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
    "postUrls": ["https://x.com/CoinMarketCap/status/2030012592282796096"],
    "usernames": ["cristiano"],
    "maxPostsPerUser": 3,
    "browserCookies": "",
}

# Run the Actor and wait for it to finish
run = client.actor("crawlerbros/twitter-video-downloader").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
print("💾 Check your data here: https://console.apify.com/storage/datasets/" + run["defaultDatasetId"])
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# 📚 Want to learn more 📖? Go to → https://docs.apify.com/api/client/python/docs/quick-start

```

## CLI example

```bash
echo '{
  "postUrls": [
    "https://x.com/CoinMarketCap/status/2030012592282796096"
  ],
  "usernames": [
    "cristiano"
  ],
  "maxPostsPerUser": 3,
  "browserCookies": ""
}' |
apify call crawlerbros/twitter-video-downloader --silent --output-dataset

```

## MCP server setup

```json
{
    "mcpServers": {
        "apify": {
            "command": "npx",
            "args": [
                "mcp-remote",
                "https://mcp.apify.com/?tools=crawlerbros/twitter-video-downloader",
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
        "title": "Twitter Video Downloader",
        "description": "Download videos from Twitter/X posts. Supports direct post URLs and username-based scraping.",
        "version": "1.6",
        "x-build-id": "YeAzr73ok4Dc32z5k"
    },
    "servers": [
        {
            "url": "https://api.apify.com/v2"
        }
    ],
    "paths": {
        "/acts/crawlerbros~twitter-video-downloader/run-sync-get-dataset-items": {
            "post": {
                "operationId": "run-sync-get-dataset-items-crawlerbros-twitter-video-downloader",
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
        "/acts/crawlerbros~twitter-video-downloader/runs": {
            "post": {
                "operationId": "runs-sync-crawlerbros-twitter-video-downloader",
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
        "/acts/crawlerbros~twitter-video-downloader/run-sync": {
            "post": {
                "operationId": "run-sync-crawlerbros-twitter-video-downloader",
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
                    "browserCookies"
                ],
                "properties": {
                    "postUrls": {
                        "title": "Post URLs",
                        "type": "array",
                        "description": "List of Twitter/X post URLs to download videos from (e.g., https://x.com/username/status/123456)",
                        "items": {
                            "type": "string",
                            "pattern": "^https?://(twitter\\.com|x\\.com)/[^/]+/status/\\d+"
                        }
                    },
                    "usernames": {
                        "title": "Usernames",
                        "type": "array",
                        "description": "List of Twitter/X usernames to scrape videos from (without @)",
                        "items": {
                            "type": "string"
                        }
                    },
                    "maxPostsPerUser": {
                        "title": "Max Posts Per User",
                        "minimum": 1,
                        "maximum": 100,
                        "type": "integer",
                        "description": "Maximum number of posts to scrape per username (only for username mode)",
                        "default": 10
                    },
                    "browserCookies": {
                        "title": "Browser Cookies (Required)",
                        "type": "string",
                        "description": "**Required.** Twitter/X session cookies in JSON format for authenticated scraping. Twitter heavily restricts unauthenticated browsing — a valid session is mandatory. Format: [{\"name\":\"auth_token\",\"value\":\"...\",\"domain\":\".x.com\"}, ...]. Without cookies the run returns a single placeholder record indicating cookies are needed."
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

- [Run this actor on Apify](https://apify.com/crawlerbros/twitter-video-downloader)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
