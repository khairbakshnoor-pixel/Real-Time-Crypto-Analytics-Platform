# 🚀 Real-Time Crypto Analytics Platform

A complete **Real-Time Cryptocurrency Analytics Platform** built using **Python, PostgreSQL, ETL Pipeline, APScheduler, and API Integration**. This project automatically extracts live crypto market data, transforms it, stores it in a database, and updates analytics and dashboards in real-time.

---

# 🎯 Project Objective

The goal of this project is to build a fully automated ETL pipeline that:

* Extracts live cryptocurrency market data from CoinGecko API
* Transforms and cleans the data
* Loads data into PostgreSQL database
* Runs automatically using a scheduler
* Performs real-time data analysis
* Supports live dashboard updates

This project demonstrates real-world **Data Engineering and Analytics workflow**.

---

# 🏗️ System Architecture

```
CoinGecko API
      ↓
Extract Layer (extract.py)
      ↓
Transform Layer (transform.py)
      ↓
Load Layer (load.py)
      ↓
PostgreSQL Database
      ↓
Analysis Layer (analysis.py)
      ↓
Dashboard (Streamlit)
```

---

# 📡 Data Source

Public API used:

CoinGecko API
https://api.coingecko.com/api/v3/coins/markets

Example parameters:

```
vs_currency=usd
order=market_cap_desc
per_page=20
page=1
sparkline=false
```

No API key required.

---

# 📁 Project Structure

```
crypto-analytics-platform/
│
├── database.py          # Database connection and table creation
├── extract.py           # Extract crypto data from API
├── transform.py         # Clean and transform data
├── load.py              # Load data into PostgreSQL
├── etl_pipeline.py     # ETL pipeline orchestrator
├── analysis.py         # Data analysis queries
├── dashboard.py        # Streamlit dashboard
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

# ⚙️ Technologies Used

* Python 3.10+
* PostgreSQL
* pgAdmin 4
* APScheduler
* Pandas
* Requests
* Psycopg2
* Streamlit
* SQL

---

# 🗄️ Database Schema

Table: crypto_market

| Column           | Type               |
| ---------------- | ------------------ |
| id               | SERIAL PRIMARY KEY |
| coin_id          | TEXT               |
| symbol           | TEXT               |
| name             | TEXT               |
| current_price    | FLOAT              |
| market_cap       | BIGINT             |
| total_volume     | BIGINT             |
| price_change_24h | FLOAT              |
| market_cap_rank  | INTEGER            |
| extracted_at     | TIMESTAMP          |

Indexes:

* Index on coin_id
* Index on extracted_at

---

# 🔄 ETL Pipeline Workflow

## Extract

* Fetch live crypto data using CoinGecko API
* Validate API response
* Parse JSON data

File: `extract.py`

---

## Transform

* Remove null values
* Convert numeric fields
* Add volatility score
* Add timestamp

File: `transform.py`

---

## Load

* Insert data into PostgreSQL
* Use batch inserts
* Handle transactions

File: `load.py`

---

## ETL Scheduler

Automatically runs ETL every 5 minutes using APScheduler.

File: `etl_pipeline.py`

Example:

```
python etl_pipeline.py
```

---

# 📊 Analysis Features

The platform performs real-time analysis including:

* Top 5 gainers
* Top 5 coins by market cap
* Average market cap
* Total crypto market value
* Most volatile coins

File: `analysis.py`

---

# 📈 Dashboard Features

Built using Streamlit.

Dashboard includes:

### KPI Cards

* Total Market Cap
* Highest Gainer
* Most Volatile Coin
* Average Price

### Charts

* Market Cap Chart
* Price Change Chart
* Volume Comparison
* Volatility Ranking

Dashboard auto-refreshes every 60 seconds.

Run dashboard:

```
streamlit run dashboard.py
```

---

# ⚡ Installation Guide

## Step 1: Clone repository

```
git clone https://github.com/yourusername/crypto-analytics-platform.git
cd crypto-analytics-platform
```

---

## Step 2: Install dependencies

```
pip install -r requirements.txt
```

---

## Step 3: Setup PostgreSQL

Create database:

```
crypto_db
```

Update database credentials in `database.py`

---

## Step 4: Run ETL pipeline

```
python etl_pipeline.py
```

---

## Step 5: Run Dashboard

```
streamlit run dashboard.py
```

---

# 📊 Example Output

* Live crypto data stored in PostgreSQL
* Automatic updates every 5 minutes
* Real-time dashboard analytics

---

# 🧠 Key Concepts Demonstrated

* ETL Pipeline Design
* API Integration
* PostgreSQL Integration
* Data Transformation
* Connection Pooling
* Task Scheduling
* Real-Time Analytics
* Dashboard Development

---

# 🚀 Future Improvements

* Docker support
* Cloud deployment
* FastAPI integration
* Historical trend analysis
* Anomaly detection

---

# 👨‍💻 Author

Khair Baksh Noor

GitHub: https://github.com/yourusername

---

# ⭐ Conclusion

This project demonstrates a complete real-world **Data Engineering pipeline** including data extraction, transformation, loading, analysis, and real-time dashboard visualization.

---

If you like this project, give it a ⭐ on GitHub!
