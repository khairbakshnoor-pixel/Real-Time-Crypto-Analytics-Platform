import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from extract import extract_data
from transform import transform_data
from load import load_data

logger = logging.getLogger(__name__)


def run_etl(save_raw=True):
    try:
        transformed = transform_data(extract_data(save_raw=save_raw))
        if not transformed:
            raise ValueError("No valid market records to load")
        load_data(transformed)
        return True, "Market data updated"
    except Exception:
        logger.exception("ETL failed")
        return False, "Market update failed. Previously stored data is shown, if available."


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    scheduler = BlockingScheduler()
    scheduler.add_job(run_etl, "interval", minutes=5, max_instances=1)
    run_etl()
    scheduler.start()
