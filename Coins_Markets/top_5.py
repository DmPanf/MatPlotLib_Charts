def fetch_top_cryptos(page_number=1, per_page=5):
    url = f"https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': per_page,
        'page': page_number
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()[:5]  # Возвращаем только первые 5 результатов
    else:
        print(f"Failed to get data: {response.status_code}")
        return None

top_5_cryptos = fetch_top_cryptos()

if top_5_cryptos:
    for i, crypto in enumerate(top_5_cryptos):
        print(f"{i+1}. {crypto['name']} ({crypto['symbol'].upper()}) - Market Cap: {crypto['market_cap']}")


top_5_cryptos = fetch_top_cryptos(page_number=2, per_page=5)

if top_5_cryptos:
    for i, crypto in enumerate(top_5_cryptos):
        print(f"{i+1}. {crypto['name']} ({crypto['symbol'].upper()}) - Market Cap: {crypto['market_cap']}")
