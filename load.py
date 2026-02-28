import sqlite3

def load_data(transformed_data):
    if not transformed_data:
        print("❌ No data to load")
        return

    connection = None
    try:
        connection = sqlite3.connect('crypto.db') 
        cursor = connection.cursor()

        # Positional placeholders (?) are more stable in SQLite
        insert_query = """
        INSERT INTO crypto_market (
            coin_id, symbol, name, current_price, market_cap, 
            total_volume, price_change_24h, market_cap_rank, 
            volatility_score, extracted_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(coin_id) DO UPDATE SET
            current_price = excluded.current_price,
            market_cap = excluded.market_cap,
            total_volume = excluded.total_volume,
            price_change_24h = excluded.price_change_24h,
            market_cap_rank = excluded.market_cap_rank,
            volatility_score = excluded.volatility_score,
            extracted_at = excluded.extracted_at;
        """

        # Dictionary ko Tuple mein convert karna lazmi hai positional placeholders ke liye
        data_to_insert = [
            (
                d['coin_id'], d['symbol'], d['name'], d['current_price'],
                d['market_cap'], d['total_volume'], d['price_change_24h'],
                d['market_cap_rank'], d['volatility_score'], d['extracted_at']
            ) for d in transformed_data
        ]

        cursor.executemany(insert_query, data_to_insert)
        connection.commit()
        print(f"✅ Data loaded into SQLite successfully ({len(data_to_insert)} rows)")

    except Exception as e:
        print("❌ Load failed:", e)
    finally:
        if connection:
            connection.close()