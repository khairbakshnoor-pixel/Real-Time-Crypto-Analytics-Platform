import logging

import pandas as pd
import plotly.express as px
import streamlit as st

from analysis import all_market_data
from database import setup_database
from etl_pipeline import run_etl

st.set_page_config(page_title="Crypto Analytics Platform", layout="wide")
st.title("Real-Time Crypto Analytics Platform")
st.sidebar.title("Dashboard Settings")
refresh_interval = st.sidebar.slider("Refresh Interval (seconds)", 10, 120, 60)


@st.cache_data(ttl=300, show_spinner=False)
def refresh_market():
    # Cache failed attempts too, to limit API retries across sessions.
    return run_etl(save_raw=False)


@st.fragment(run_every=refresh_interval)
def render_market():
    try:
        setup_database()
        success, message = refresh_market()
        data = all_market_data()
    except Exception:
        logging.exception("Unable to render market data")
        st.error("Market database is unavailable. Check the application logs.")
        return
    if not success:
        st.warning(message)
    if data.empty:
        st.info("No market data available yet.")
        return

    latest = pd.to_datetime(data["extracted_at"], utc=True, errors="coerce").max()
    st.caption(f"Stored snapshot: {latest} | {len(data)} tracked coins | USD")
    gainers = data.nlargest(5, "price_change_24h")
    top_cap = data.nlargest(5, "market_cap")
    volatility = data.nlargest(5, "volatility_score")
    cols = st.columns(4)
    cols[0].metric("Tracked Market Cap", f"${data['market_cap'].sum():,.0f}")
    cols[1].metric("Highest 24h Change", gainers.iloc[0]["name"],
                   f"{gainers.iloc[0]['price_change_24h']:.2f}%")
    cols[2].metric("Most Volatile", volatility.iloc[0]["name"])
    cols[3].metric("Avg Market Cap", f"${data['market_cap'].mean():,.0f}")
    st.divider()
    left, right = st.columns(2)
    with left:
        st.subheader("Market Cap (Top 5)")
        st.plotly_chart(px.bar(top_cap, x="name", y="market_cap"), use_container_width=True)
    with right:
        st.subheader("Price Change % (24h)")
        st.plotly_chart(px.bar(gainers, x="name", y="price_change_24h"), use_container_width=True)
    st.subheader("Volatility Ranking (Top 5)")
    st.plotly_chart(px.bar(volatility, x="name", y="volatility_score"), use_container_width=True)
    st.dataframe(data, hide_index=True, use_container_width=True)


render_market()
