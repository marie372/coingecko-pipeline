import requests

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        print("Data fetched successfully!")
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return []

if __name__ == "__main__":
    data = fetch_crypto_data()
    for coin in data:
        print(coin["name"], "-", coin["current_price"])