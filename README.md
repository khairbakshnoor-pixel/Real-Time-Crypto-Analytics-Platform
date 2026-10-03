# Real-Time Crypto Analytics Platform

CoinGecko data for 20 coins, cleaned with Python, stored in SQLite, and displayed
with Streamlit and Plotly. This implementation does not use PostgreSQL.

## Local Setup

Use Python 3.12 or newer from the repository directory:

```sh
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run dashboard.py
```

The dashboard initializes its database and attempts ETL on first load. Active
sessions refresh at the sidebar interval. API attempts, including failures, are
cached for five minutes across sessions. When an update fails, stored data stays
visible with a warning and timestamp. The bundled database is historical sample data.

For a separate worker, run `python etl_pipeline.py`. It updates every five minutes
and saves raw JSON locally. A separate worker is unnecessary for Streamlit;
in-app updates run only while a session is active.

## Streamlit Community Cloud

1. Push the project files to GitHub.
2. Create a Streamlit Community Cloud app for
   `khairbakshnoor-pixel/Real-Time-Crypto-Analytics-Platform`, branch `main`.
3. Set the entrypoint to `dashboard.py` and select Python 3.12 or newer.
4. Deploy; dependencies are installed from `requirements.txt`.

No secrets are required by this version. The public CoinGecko endpoint may
rate-limit or reject requests; the app reports failures and keeps stored data.
SQLite lives beside database.py, independent of the working directory.
Set CRYPTO_DB_PATH to override it; the parent directory must already exist.
Cloud local storage is ephemeral, so restarts/redeployments may reset data.
Persistent external storage is needed for historical retention.

References:
- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies
- https://docs.streamlit.io/develop/api-reference/execution-flow/st.fragment

## Verification

```sh
python -m unittest discover -s tests -v
python verify_dashboard.py
```

Volatility score is absolute 24-hour percentage change multiplied by volume.
Market cap totals cover tracked coins only, not the entire crypto market.
