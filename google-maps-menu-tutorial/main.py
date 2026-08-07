"""Run the crawlerbros/google-maps-menu Apify actor and print dataset items."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


HERE = Path(__file__).parent
INPUT_FILE = HERE / "input.json"
INPUT_EXAMPLE_FILE = HERE / "input.example.json"
ACTOR_ID = os.getenv("ACTOR_ID", "crawlerbros/google-maps-menu")


def load_env() -> None:
    if load_dotenv:
        load_dotenv(HERE / ".env")


def run_actor(token: str, actor_id: str, actor_input: dict) -> list | dict:
    actor_api_id = actor_id.replace("/", "~")
    query = urllib.parse.urlencode({"token": token})
    url = f"https://api.apify.com/v2/acts/{actor_api_id}/run-sync-get-dataset-items?{query}"
    body = json.dumps(actor_input).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=300) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> None:
    load_env()
    token = os.getenv("APIFY_TOKEN", "").strip()
    if not token:
        raise SystemExit("APIFY_TOKEN is missing. Copy .env.example to .env and add your token.")
    if not INPUT_FILE.is_file():
        raise SystemExit(
            "input.json is missing. Copy input.example.json to input.json and fill it using the actor README."
        )
    actor_input = json.loads(INPUT_FILE.read_text(encoding="utf-8"))
    items = run_actor(token, ACTOR_ID, actor_input)
    print(json.dumps(items, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
