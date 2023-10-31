import requests
import json
import plotly.graph_objects as go


def fetch_crypto_history(crypto_id, vs_currency='usd', days=30):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart?vs_currency={vs_currency}&days={days}"
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)['prices']
    else:
        print(f"Failed to get data: {response.status_code}")
        return None

def plot_crypto_data(crypto_data_dict):
    fig = go.Figure()
    for crypto, data in crypto_data_dict.items():
        timestamps, prices = zip(*data)
        fig.add_trace(go.Scatter(x=timestamps, y=prices, mode='lines', name=crypto))

    fig.update_layout(title='Crypto Prices Over the Last Month',
                      xaxis_title='Time',
                      yaxis_title='Price in USD')

    fig.show()

# предположим, что top_5_cryptos это список с идентификаторами топ-5 криптовалют
top_5_cryptos = ['bitcoin', 'ethereum', 'cardano', 'tether', 'binancecoin']

crypto_data_dict = {}

for crypto in top_5_cryptos:
    crypto_data_dict[crypto] = fetch_crypto_history(crypto)

plot_crypto_data(crypto_data_dict)
