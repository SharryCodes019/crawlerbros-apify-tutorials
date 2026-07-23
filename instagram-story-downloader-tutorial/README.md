# Instagram Story Downloader Tutorial: Run This Apify Actor with Python

Scrape and optionally download Instagram stories for specified usernames using Playwright. Also obtain metadata for stories, such as story id, publish date, expiry date, mentions, links and etc.

This repository shows how to run [Instagram Story Downloader](https://apify.com/crawlerbros/instagram-story-downloader) from Python. The complete actor README below is the canonical source of truth for inputs, outputs, examples, limits, and behavior.

## Actor Overview

- **Actor:** `crawlerbros/instagram-story-downloader`
- **Apify Store:** [https://apify.com/crawlerbros/instagram-story-downloader](https://apify.com/crawlerbros/instagram-story-downloader)
- **SEO title:** Instagram Story Downloader Tutorial: Run This Apify Actor with Python
- **Description:** Scrape and optionally download Instagram stories for specified usernames using Playwright. Also obtain metadata for stories, such as story id, publish date, expiry date, mentions, links and etc.

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

## Instagram Story Downloader

Scrapes Instagram stories for given usernames. Collects story metadata including media URLs, mentions, hashtags, locations, and music information. Optionally downloads media files to the key-value store.

### Input

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `usernames` | array | Yes | List of Instagram usernames to scrape stories from (max 100) |
| `maxStoriesPerUser` | integer | No | Maximum number of stories to extract per user (default: 20, max: 200) |

#### Example Input

```json
{
  "usernames": ["natgeo", "nasa"],
  "maxStoriesPerUser": 10
}
````

### Output

Each story is saved as a separate item in the dataset with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `story_id` | string | Unique Instagram story ID |
| `shortcode` | string | Instagram shortcode for the story |
| `story_url` | string | Direct URL to the story |
| `profile_id` | string | Instagram profile ID of the user |
| `username` | string | Username of the story owner |
| `uploaded_at` | string | ISO timestamp when the story was uploaded |
| `expires_at` | string | ISO timestamp when the story expires |
| `media_type` | string | Type of media (`video` or `image`) |
| `mentions` | array | List of mentioned usernames |
| `hashtags` | array | List of hashtags used |
| `locations` | array | List of location URLs tagged |
| `music` | array | Music tracks with `track_name` and `artist` |
| `links` | array | External links in the story |
| `attached_posts` | array | Attached post URLs |
| `saved_as` | string | Filename in the key-value store |
| `download_url` | string | URL to download the media file |

#### Example Output

```json
{
  "story_id": "3820032670852205241",
  "shortcode": "DUDe3mIiEq5",
  "story_url": "https://www.instagram.com/stories/natgeo/3820032670852205241/",
  "profile_id": "481904760",
  "username": "natgeo",
  "uploaded_at": "2026-01-28T17:29:59",
  "expires_at": "2026-01-29T17:29:59",
  "media_type": "video",
  "mentions": [],
  "hashtags": [],
  "locations": [],
  "music": [
    {
      "track_name": "Head In The Clouds",
      "artist": "Sugartapes"
    }
  ],
  "links": [],
  "attached_posts": [],
  "saved_as": "DUDe3mIiEq5.mp4",
  "download_url": "https://api.apify.com/v2/key-value-stores/{store_id}/records/DUDe3mIiEq5.mp4"
}
```

# Actor input Schema

## `usernames` (type: `array`):

Usernames whose stories should be processed.

## `maxStoriesPerUser` (type: `integer`):

Maximum number of stories to extract per username.

## Actor input object example

```json
{
  "usernames": [
    "snoopdogg",
    "natgeo"
  ],
  "maxStoriesPerUser": 20
}
```

# Actor output Schema

## `stories` (type: `string`):

Dataset containing all scraped Instagram stories with metadata

## `mediaFiles` (type: `string`):

Key-value store containing downloaded story media files

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
        "snoopdogg",
        "natgeo"
    ]
};

// Run the Actor and wait for it to finish
const run = await client.actor("crawlerbros/instagram-story-downloader").call(input);

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
run_input = { "usernames": [
        "snoopdogg",
        "natgeo",
    ] }

# Run the Actor and wait for it to finish
run = client.actor("crawlerbros/instagram-story-downloader").call(run_input=run_input)

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
    "snoopdogg",
    "natgeo"
  ]
}' |
apify call crawlerbros/instagram-story-downloader --silent --output-dataset

```

## MCP server setup

```json
{
    "mcpServers": {
        "apify": {
            "command": "npx",
            "args": [
                "mcp-remote",
                "https://mcp.apify.com/?tools=crawlerbros/instagram-story-downloader",
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
        "title": "Instagram Story Downloader",
        "description": "Scrape and optionally download Instagram stories for specified usernames using Playwright. Also obtain metadata for stories, such as story id, publish date, expiry date, mentions, links and etc.",
        "version": "1.0",
        "x-build-id": "wlbLLc1qFLKgNliTt"
    },
    "servers": [
        {
            "url": "https://api.apify.com/v2"
        }
    ],
    "paths": {
        "/acts/crawlerbros~instagram-story-downloader/run-sync-get-dataset-items": {
            "post": {
                "operationId": "run-sync-get-dataset-items-crawlerbros-instagram-story-downloader",
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
        "/acts/crawlerbros~instagram-story-downloader/runs": {
            "post": {
                "operationId": "runs-sync-crawlerbros-instagram-story-downloader",
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
        "/acts/crawlerbros~instagram-story-downloader/run-sync": {
            "post": {
                "operationId": "run-sync-crawlerbros-instagram-story-downloader",
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
                        "minItems": 1,
                        "maxItems": 100,
                        "uniqueItems": true,
                        "type": "array",
                        "description": "Usernames whose stories should be processed.",
                        "items": {
                            "type": "string",
                            "pattern": "^[A-Za-z0-9._]+$"
                        },
                        "default": [
                            "snoopdogg",
                            "natgeo"
                        ]
                    },
                    "maxStoriesPerUser": {
                        "title": "Max Stories Per User",
                        "minimum": 1,
                        "maximum": 200,
                        "type": "integer",
                        "description": "Maximum number of stories to extract per username.",
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

- [Run this actor on Apify](https://apify.com/crawlerbros/instagram-story-downloader)
- [CrawlerBros on Apify](https://apify.com/crawlerbros)

## License

MIT
