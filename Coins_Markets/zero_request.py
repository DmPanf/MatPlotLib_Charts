import requests
import json

def fetch_top_cryptos(n=5):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': n,
        'page': 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f"Failed to get data: {response.status_code}")
        return None

  print(fetch_top_cryptos(5))
