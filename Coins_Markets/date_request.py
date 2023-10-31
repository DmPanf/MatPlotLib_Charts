from datetime import datetime

def fetch_historical_data(crypto_id, from_date="2023-09-01", to_date="2023-09-30"):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart/range"
    params = {
        'vs_currency': 'usd',
        'from': datetime.strptime(from_date, "%Y-%m-%d").timestamp(),
        'to': datetime.strptime(to_date, "%Y-%m-%d").timestamp()
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f"Failed to get data: {response.status_code}")
        return None

  print(fetch_historical_data("bitcoin", from_date="2023-09-01", to_date="2023-09-30"))
