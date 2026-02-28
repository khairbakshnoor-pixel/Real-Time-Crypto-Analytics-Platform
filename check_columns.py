import sqlite3
conn = sqlite3.connect('crypto.db')
cursor = conn.cursor()
cursor.execute('PRAGMA table_info(crypto_market)')
columns = [col[1] for col in cursor.fetchall()]
print('Columns:', columns)

# Show all data
cursor.execute('SELECT * FROM crypto_market')
rows = cursor.fetchall()
print(f'\nTotal rows: {len(rows)}')
print('\nFirst row:')
for col, val in zip(columns, rows[0]):
    print(f'  {col}: {val}')

conn.close()
