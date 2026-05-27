import requests
import pandas as pd
from datetime import datetime
import os

def fetch_memecoin_data():

    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "category": "meme-token",
        "order": "market_cap_desc",
        "per_page": 20,
        "page": 1,
        "sparkline": False,
        "price_change_percentage": "24h"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(
            f"API Request Failed: {response.status_code}"
        )

    data = response.json()

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
            "price_change_percentage_24h":
                coin.get("price_change_percentage_24h"),
            "last_updated": coin.get("last_updated"),
            "ingestion_timestamp": datetime.now()
        }

        memecoin_list.append(coin_data)

    df = pd.DataFrame(memecoin_list)

    os.makedirs("data/raw", exist_ok=True)

    file_name = (
        f"data/raw/memecoin_data_{datetime.now().date()}.csv"
    )

    df.to_csv(file_name, index=False)

    print("CSV Generated Successfully")

    return file_name