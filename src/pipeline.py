from extract import fetch_crypto_data
from transform import transform_crypto_data
from load import load_crypto_data

def run_pipeline():
    print("Starting CoinGecko pipeline...")
    raw = fetch_crypto_data()
    df = transform_crypto_data(raw)
    load_crypto_data(df)
    print("Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()