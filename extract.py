import json
from datetime import datetime, timezone
from pathlib import Path

import requests

API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd", "order": "market_cap_desc",
    "per_page": 20, "page": 1, "sparkline": "false",
}


def extract_data(save_raw=True):
    response = requests.get(API_URL, params=PARAMS, timeout=20)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, list) or not data or not all(isinstance(coin, dict) for coin in data):
        raise ValueError("CoinGecko returned an empty or invalid market response")
    if save_raw:
        directory = Path(__file__).resolve().parent / "raw_data"
        directory.mkdir(exist_ok=True)
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S_%f")
        (directory / f"crypto_raw_{timestamp}.json").write_text(
            json.dumps(data, indent=2), encoding="utf-8"
        )
    return data


if __name__ == "__main__":
    extract_data()
