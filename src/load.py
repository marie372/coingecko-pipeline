import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return conn

def load_crypto_data(df):
    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO crypto_prices (coin_id, symbol, name, current_price, market_cap, total_volume, price_change_24h)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            row["coin_id"],
            row["symbol"],
            row["name"],
            row["current_price"],
            row["market_cap"],
            row["total_volume"],
            row["price_change_24h"]
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Loaded {len(df)} records into PostgreSQL.")

if __name__ == "__main__":
    from extract import fetch_crypto_data
    from transform import transform_crypto_data
    raw = fetch_crypto_data()
    df = transform_crypto_data(raw)
    load_crypto_data(df)