import sqlite3
import pandas as pd

conn = sqlite3.connect('crypto.db')

# Check row count
cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM crypto_market')
count = cursor.fetchone()[0]
print(f"Row count: {count}")

if count > 0:
    # Show sample data
    df = pd.read_sql("SELECT name, market_cap FROM crypto_market LIMIT 5", conn)
    print("\nSample data:")
    print(df)
    
    # Check total market cap
    df_total = pd.read_sql("SELECT SUM(market_cap) as total FROM crypto_market", conn)
    print(f"\nTotal market cap: {df_total['total'].iloc[0]}")
else:
    print("Database is empty!")

conn.close()
