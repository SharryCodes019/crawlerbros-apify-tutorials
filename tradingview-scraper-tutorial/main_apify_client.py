"""Run the crawlerbros/tradingview-scraper Apify actor with the official Apify Python client."""

from __future__ import annotations

import json
import os
from pathlib import Path

from apify_client import ApifyClient

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


HERE = Path(__file__).parent
INPUT_FILE = HERE / "input.json"
INPUT_EXAMPLE_FILE = HERE / "input.example.json"
ACTOR_ID = os.getenv("ACTOR_ID", "crawlerbros/tradingview-scraper")


def load_env() -> None:
    if load_dotenv:
        load_dotenv(HERE / ".env")


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
    client = ApifyClient(token=token)

    run = client.actor(ACTOR_ID).call(run_input=actor_input)
    if run is None:
        raise SystemExit("Actor run did not return run metadata.")

    dataset_id = run.get("defaultDatasetId") or run.get("default_dataset_id")
    if not dataset_id:
        raise SystemExit("Actor run did not return a default dataset ID.")

    items = client.dataset(dataset_id).list_items().items
    print(json.dumps(items, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
