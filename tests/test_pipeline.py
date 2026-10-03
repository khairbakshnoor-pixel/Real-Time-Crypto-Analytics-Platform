import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import database
from analysis import all_market_data, total_market_cap
from etl_pipeline import run_etl
from load import load_data
from extract import extract_data
from transform import transform_data


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        override = patch.object(database, "DB_PATH", Path(self.temp.name) / "test.db")
        override.start()
        self.addCleanup(override.stop)

    def test_fresh_database_and_upsert(self):
        rows = transform_data([{"id": "bitcoin", "name": "Bitcoin", "market_cap": 100,
                                "price_change_percentage_24h": None, "total_volume": None}])
        load_data(rows)
        rows[0]["market_cap"] = 200
        load_data(rows)
        self.assertEqual(len(all_market_data()), 1)
        self.assertEqual(total_market_cap().iloc[0, 0], 200)
        self.assertEqual(rows[0]["price_change_24h"], 0)

    def test_api_failure_preserves_snapshot(self):
        load_data(transform_data([{"id": "bitcoin", "name": "Bitcoin"}]))
        with patch("etl_pipeline.extract_data", side_effect=TimeoutError("offline")):
            success, _ = run_etl(save_raw=False)
        self.assertFalse(success)
        self.assertEqual(len(all_market_data()), 1)

    def test_load_failure_is_reported(self):
        with patch("etl_pipeline.extract_data", return_value=[{"id": "bitcoin"}]), \
             patch("etl_pipeline.load_data", side_effect=RuntimeError("read-only")):
            self.assertFalse(run_etl()[0])

    def test_extraction_validates_response_and_sets_timeout(self):
        with patch("extract.requests.get") as get:
            get.return_value.json.return_value = {"error": "rate limited"}
            with self.assertRaises(ValueError):
                extract_data(save_raw=False)
            self.assertEqual(get.call_args.kwargs["timeout"], 20)
            get.return_value.raise_for_status.assert_called_once()

    def test_dashboard_empty_and_populated(self):
        from streamlit.testing.v1 import AppTest
        app_path = Path(__file__).resolve().parents[1] / "dashboard.py"
        with patch("etl_pipeline.run_etl", return_value=(False, "Offline")):
            app = AppTest.from_file(str(app_path)).run(timeout=20)
            self.assertEqual(len(app.exception), 0)
            self.assertEqual(len(app.info), 1)
            load_data(transform_data([{"id": "bitcoin", "name": "Bitcoin", "market_cap": 100}]))
            app.run(timeout=20)
            self.assertEqual(len(app.exception), 0)
            self.assertEqual(len(app.metric), 4)
            self.assertEqual(len(app.warning), 1)
            app.sidebar.slider[0].set_value(30).run(timeout=20)
            self.assertEqual(len(app.exception), 0)


if __name__ == "__main__":
    unittest.main()
