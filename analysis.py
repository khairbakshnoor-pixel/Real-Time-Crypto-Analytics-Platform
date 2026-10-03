from database import get_connection
import pandas as pd

# Database file ka naam


# 1️⃣ Top 5 Gainers (24h) [cite: 96]
def top_5_gainers():
    query = """
    SELECT name, price_change_24h
    FROM crypto_market
    ORDER BY price_change_24h DESC
    LIMIT 5;
    """
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# 2️⃣ Top 5 by Market Cap [cite: 97]
def top_5_market_cap():
    query = """
    SELECT name, market_cap
    FROM crypto_market
    ORDER BY market_cap DESC
    LIMIT 5;
    """
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# 3️⃣ Average Market Cap [cite: 98]
def average_market_cap():
    query = "SELECT AVG(market_cap) AS avg_market_cap FROM crypto_market;"
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# 4️⃣ Total Market Cap [cite: 99]
def total_market_cap():
    query = "SELECT SUM(market_cap) AS total_market_cap FROM crypto_market;"
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# 5️⃣ Volatility Ranking [cite: 100]
def volatility_ranking():
    # Volatility score humne transform layer mein calculate kiya tha [cite: 67]
    query = """
    SELECT name, volatility_score
    FROM crypto_market
    ORDER BY volatility_score DESC
    LIMIT 5;
    """
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# 6️⃣ All Raw Market Data
def all_market_data():
    query = """
    SELECT 
        name, 
        symbol, 
        current_price, 
        market_cap, 
        total_volume,
        price_change_24h,
        market_cap_rank,
        volatility_score,
        extracted_at
    FROM crypto_market
    ORDER BY market_cap_rank;
    """
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df
