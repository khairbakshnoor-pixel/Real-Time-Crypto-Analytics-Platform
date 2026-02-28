import sqlite3
import pandas as pd
from analysis import top_5_gainers, top_5_market_cap, total_market_cap, volatility_ranking, average_market_cap

print("Testing analysis functions:")
print("="*50)

# Test total_market_cap
total = total_market_cap()
print(f"\n1. Total Market Cap:")
print(f"   DataFrame: {total}")
if not total.empty:
    print(f"   Value: ${total.iloc[0,0]:,.0f}")

# Test average_market_cap
avg = average_market_cap()
print(f"\n2. Average Market Cap:")
print(f"   DataFrame: {avg}")
if not avg.empty:
    print(f"   Value: ${avg.iloc[0,0]:,.0f}")

# Test top_5_market_cap
top_cap = top_5_market_cap()
print(f"\n3. Top 5 by Market Cap:")
print(top_cap)

# Test top_5_gainers
gainers = top_5_gainers()
print(f"\n4. Top 5 Gainers:")
print(gainers)

# Test volatility_ranking
volatility = volatility_ranking()
print(f"\n5. Volatility Ranking:")
print(volatility)

print("\n" + "="*50)
print("All tests completed!")
