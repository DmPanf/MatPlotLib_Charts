#@title Fetch currency data
import requests
import xml.etree.ElementTree as ET
import plotly.graph_objects as go
from datetime import timedelta, date

currency_codes = ['USD', 'EUR', 'GBP', 'AUD', 'CAD', 'HKD', 'NZD', 'SGD', 'CHF', 'BYN', 'BGN']

currency_full_names = {
    'USD': 'United States Dollar',
    'EUR': 'Euro',
    'GBP': 'British Pound Sterling',
    'AUD': 'Australian Dollar',
    'CAD': 'Canadian Dollar',
    'HKD': 'Hong Kong Dollar',
    'NZD': 'New Zealand Dollar',
    'SGD': 'Singapore Dollar',
    'CHF': 'Swiss Franc',
    'BYN': 'Belarusian Ruble',
    'BGN': 'Bulgarian Lev'
}

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

def fetch_currency_data(date):
    url = f"https://cbr.ru/scripts/XML_daily.asp?date_req={date.strftime('%d/%m/%Y')}"
    response = requests.get(url)
    tree = ET.ElementTree(ET.fromstring(response.content))
    root = tree.getroot()

    currencies = {}

    for valute in root.findall('Valute'):
        char_code = valute.find('CharCode').text
        if char_code in currency_codes:
            value = float(valute.find('Value').text.replace(",", "."))
            currencies[char_code] = value

    return currencies

start_date = date(2023, 9, 1)
end_date = date(2023, 9, 30)

currency_data = {code: [] for code in currency_codes}
date_labels = []

for single_date in daterange(start_date, end_date):
    rates = fetch_currency_data(single_date)
    for code in currency_data.keys():
        currency_data[code].append(rates.get(code, None))
    date_labels.append(single_date.strftime('%d/%m/%Y'))

fig = go.Figure()

for code, rates in currency_data.items():
    full_name = currency_full_names.get(code, code)
    trace_name = f"{code} [{full_name}]"
    fig.add_trace(go.Scatter(x=date_labels, y=rates, mode='lines+markers', name=trace_name))

fig.update_layout(
    title={
        'text': 'Exchange rates in September 2023',
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(
            size=24,
            color='darkblue'
        )
    },
    width=1600,
    height=700,
    plot_bgcolor='rgba(240,240,240,0.95)',
    paper_bgcolor='rgba(240,240,240,0.95)',
    xaxis=dict(
        title='Date',
        showline=True,
        showgrid=True,
        gridcolor='rgba(128, 128, 128, 0.2)',
        linecolor='rgba(0,0,0,1)',
        linewidth=2,
        title_font=dict(
            size=18,
            color='darkblue'
        ),
        tickfont=dict(
            size=14,
            color='darkblue'
        )
    ),
    yaxis=dict(
        title='Exchange rate (RUB)',
        showline=True,
        showgrid=True,
        gridcolor='rgba(128, 128, 128, 0.2)',
        linecolor='rgba(0,0,0,1)',
        linewidth=2,
        title_font=dict(
            size=18,
            color='darkblue'
        ),
        tickfont=dict(
            size=14,
            color='darkblue'
        )
    ),
    font=dict(
        family='Courier New, monospace',
        size=16,
        color='darkblue'
    )
)

fig.show()
