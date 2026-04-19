import pandas as pd

def transform_crypto_data(raw_data):
    df = pd.DataFrame(raw_data)

    df = df[[
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h"
    ]]

    df = df.rename(columns={
        "id": "coin_id",
        "price_change_percentage_24h": "price_change_24h"
    })

    df = df.dropna()
    df["current_price"] = df["current_price"].astype(float)
    df["market_cap"] = df["market_cap"].astype(float)
    df["total_volume"] = df["total_volume"].astype(float)
    df["price_change_24h"] = df["price_change_24h"].astype(float)

    print(f"Transformed {len(df)} records.")
    return df

if __name__ == "__main__":
    from extract import fetch_crypto_data
    raw = fetch_crypto_data()
    df = transform_crypto_data(raw)
    print(df)