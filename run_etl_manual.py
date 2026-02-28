from extract import extract_data
from transform import transform_data
from load import load_data
import json

# Load raw data from file
with open('raw_data/crypto_raw_20260301_005535.json') as f:
    raw_data = json.load(f)

print(f'Extracted {len(raw_data)} coins from raw file')

# Transform
transformed = transform_data(raw_data)
print(f'Transformed {len(transformed)} coins')

# Load
load_data(transformed)
print('ETL Complete!')
