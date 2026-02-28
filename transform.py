from datetime import datetime

def transform_data(raw_data):
    if not raw_data:
        print("❌ No data to transform")
        return None

    transformed = []

    for coin in raw_data:
        try:
            # Remove nulls safely using .get()
            coin_id = coin.get("id")
            symbol = coin.get("symbol")
            name = coin.get("name")
            current_price = float(coin.get("current_price", 0))
            market_cap = int(coin.get("market_cap", 0))
            total_volume = int(coin.get("total_volume", 0))
            price_change_24h = float(coin.get("price_change_percentage_24h", 0))
            market_cap_rank = coin.get("market_cap_rank", 0)

            # Feature engineering
            volatility_score = abs(price_change_24h) * total_volume

            extracted_at = datetime.now()

            # Return as dictionary for compatibility with load.py
            transformed.append({
                'coin_id': coin_id,
                'symbol': symbol,
                'name': name,
                'current_price': current_price,
                'market_cap': market_cap,
                'total_volume': total_volume,
                'price_change_24h': price_change_24h,
                'market_cap_rank': market_cap_rank,
                'volatility_score': volatility_score,
                'extracted_at': extracted_at
            })

        except Exception as e:
            print("⚠ Skipping coin due to error:", e)

    print("✅ Data transformed successfully")
    return transformed
