import requests
import json
from datetime import datetime

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 20,
    "page": 1,
    "sparkline": "false"
}

def extract_data():
    try:
        response = requests.get(API_URL, params=PARAMS)
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Data extracted successfully")

            # Save raw JSON
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"raw_data/crypto_raw_{timestamp}.json"

            with open(filename, "w") as f:
                json.dump(data, f, indent=4)

            print(f"✅ Raw data saved to {filename}")
            return data

        else:
            print("❌ API Error:", response.status_code)
            return None

    except Exception as e:
        print("❌ Extraction failed:", e)
        return None


if __name__ == "__main__":
    extract_data()