import sqlite3
import os
from pathlib import Path

DB_PATH = Path(os.environ.get("CRYPTO_DB_PATH", Path(__file__).resolve().parent / "crypto.db"))


def get_connection():
    return sqlite3.connect(DB_PATH, timeout=30)

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Table with volatility_score column
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS crypto_market (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            coin_id TEXT UNIQUE,
            symbol TEXT,
            name TEXT,
            current_price FLOAT,
            market_cap BIGINT,
            total_volume BIGINT,
            price_change_24h FLOAT,
            market_cap_rank INTEGER,
            volatility_score FLOAT,
            extracted_at TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("Database updated successfully!")

if __name__ == "__main__":
    setup_database()
