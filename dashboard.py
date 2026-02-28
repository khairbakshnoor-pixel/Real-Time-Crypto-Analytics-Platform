import streamlit as st
import pandas as pd
import plotly.express as px
import time
from analysis import (
    top_5_gainers, 
    top_5_market_cap, 
    total_market_cap, 
    volatility_ranking,
    average_market_cap
)

# 1. Page Configuration
st.set_page_config(page_title="Crypto Analytics Platform", layout="wide")

# 2. Header Section
st.title("🚀 Real-Time Crypto Analytics Platform")
st.markdown("""
This dashboard displays live cryptocurrency data extracted via our ETL pipeline. 
It updates automatically every 60 seconds to reflect the latest market trends.
""")

# 3. Sidebar for Settings
st.sidebar.title("Dashboard Settings")
refresh_interval = st.sidebar.slider("Refresh Interval (seconds)", 10, 120, 60)

# 4. Data Fetching and Handling Empty Database
try:
    df_gainers = top_5_gainers()
    df_top_cap = top_5_market_cap()
    df_volatility = volatility_ranking()
    
    total_cap_df = total_market_cap()
    total_cap_val = total_cap_df.iloc[0, 0] if not total_cap_df.empty else 0
    
    avg_cap_df = average_market_cap()
    avg_cap_val = avg_cap_df.iloc[0, 0] if not avg_cap_df.empty else 0
    
    # Fill None values with 0 for formatting
    total_cap_val = total_cap_val if total_cap_val is not None else 0
    avg_cap_val = avg_cap_val if avg_cap_val is not None else 0

except Exception as e:
    st.error(f"Error fetching data: {e}")
    st.stop()

# 5. KPI Cards (Task 7)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Market Cap", f"${total_cap_val:,.0f}")

with col2:
    if not df_gainers.empty:
        gainer = df_gainers.iloc[0]
        st.metric("Highest Gainer", gainer['name'], f"{gainer['price_change_24h']:.2f}%")
    else:
        st.metric("Highest Gainer", "No Data")

with col3:
    if not df_volatility.empty:
        volatile = df_volatility.iloc[0]
        st.metric("Most Volatile", volatile['name'])
    else:
        st.metric("Most Volatile", "No Data")

with col4:
    st.metric("Avg Market Cap", f"${avg_cap_val:,.0f}")

st.divider()

# 6. Interactive Charts (Task 7)
row1, row2 = st.columns(2)

with row1:
    st.subheader("Market Cap (Top 5)")
    if not df_top_cap.empty:
        fig_cap = px.bar(df_top_cap, x='name', y='market_cap', color='market_cap', template="plotly_dark")
        st.plotly_chart(fig_cap, use_container_width=True)
    else:
        st.info("Waiting for ETL to load data...")

with row2:
    st.subheader("Price Change % (24h)")
    if not df_gainers.empty:
        fig_price = px.line(df_gainers, x='name', y='price_change_24h', markers=True, template="plotly_dark")
        st.plotly_chart(fig_price, use_container_width=True)
    else:
        st.info("Waiting for ETL to load data...")

# 7. Volatility & Data Table
st.subheader("Volatility Ranking (Top 5)")
if not df_volatility.empty:
    fig_vol = px.pie(df_volatility, names='name', values='volatility_score', hole=0.3)
    st.plotly_chart(fig_vol, use_container_width=True)

# 8. Auto-Refresh Logic
time.sleep(refresh_interval)
st.rerun()