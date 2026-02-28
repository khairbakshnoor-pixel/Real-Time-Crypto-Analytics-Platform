from apscheduler.schedulers.blocking import BlockingScheduler
from extract import extract_data
from transform import transform_data
from load import load_data
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_etl():
    try:
        print("🚀 Running ETL...")
        logging.info("ETL Started")

        raw = extract_data()
        transformed = transform_data(raw)
        load_data(transformed)

        logging.info("ETL Completed Successfully")
        print("✅ ETL Completed")

    except Exception as e:
        logging.error(f"ETL Failed: {e}")
        print("❌ ETL Failed:", e)


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(run_etl, 'interval', minutes=5)

    print("⏳ ETL Scheduler started (runs every 5 minutes)")
    run_etl()  # run immediately once
    scheduler.start()