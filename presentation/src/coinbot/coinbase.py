# coinbase.py
import requests

def get_price(currency, fiat='USD', type='spot'):
    url = f'https://api.coinbase.com/v2/prices/{currency}-{fiat}/{type}'
    resp = requests.get(url, timeout=5)
    return float(resp.json()['data']['amount'])
