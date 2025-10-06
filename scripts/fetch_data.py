import requests
import pandas as pd

def fetch_eth_market_data(days=180):
    url = 'https://api.coingecko.com/api/v3/coins/ethereum/market_chart'
    params = {'vs_currency': 'usd', 'days': str(days)}
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

if __name__ == "__main__":
    df = fetch_eth_market_data()
    df.to_csv('data/eth_prices.csv', index=False)
    print("ETH market data saved to data/eth_prices.csv")
