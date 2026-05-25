import requests
import pandas as pd
from datetime import datetime

# -----------------------------------
# CONFIGURATION
# -----------------------------------

URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    "vs_currency": "usd",
    "category": "meme-token",
    "order": "market_cap_desc",
    "per_page": 20,
    "page": 1,
    "sparkline": False,
    "price_change_percentage": "24h"
}

# -----------------------------------
# API REQUEST
# -----------------------------------

response = requests.get(URL, params=PARAMS)

# Check API status
if response.status_code != 200:
    print("API Request Failed")
    print(response.status_code)
    exit()

data = response.json()

# -----------------------------------
# EXTRACT REQUIRED FIELDS
# -----------------------------------

memecoin_list = []

for coin in data:

    coin_data = {
        "coin_id": coin.get("id"),
        "symbol": coin.get("symbol"),
        "coin_name": coin.get("name"),
        "current_price": coin.get("current_price"),
        "market_cap": coin.get("market_cap"),
        "market_cap_rank": coin.get("market_cap_rank"),
        "total_volume": coin.get("total_volume"),
        "high_24h": coin.get("high_24h"),
        "low_24h": coin.get("low_24h"),
        "price_change_24h": coin.get("price_change_24h"),
        "price_change_percentage_24h":
            coin.get("price_change_percentage_24h"),
        "circulating_supply": coin.get("circulating_supply"),
        "last_updated": coin.get("last_updated"),
        "ingestion_timestamp": datetime.now()
    }

    memecoin_list.append(coin_data)

# -----------------------------------
# CREATE DATAFRAME
# -----------------------------------

df = pd.DataFrame(memecoin_list)

# -----------------------------------
# SAVE CSV
# -----------------------------------

file_name = f"data/raw/memecoin_data_{datetime.now().date()}.csv"

df.to_csv(file_name, index=False)

# -----------------------------------
# OUTPUT
# -----------------------------------

print("Data Ingestion Successful")
print(df.head())
print(f"\nCSV Saved: {file_name}")