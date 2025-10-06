import pandas as pd

def calculate_rsi(prices, window=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

if __name__ == "__main__":
    df = pd.read_csv('data/eth_prices.csv')
    df['RSI'] = calculate_rsi(df['price'])
    df.to_csv('data/eth_prices_with_rsi.csv', index=False)
    print("RSI calculated and saved to data/eth_prices_with_rsi.csv")
