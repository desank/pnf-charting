# data_fetcher.py

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from config import ALPHA_VANTAGE_API_KEY

def get_stock_data(ticker):
    """Fetches historical stock data from Alpha Vantage."""
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
    try:
        data, meta_data = ts.get_daily(symbol=ticker, outputsize='full')
        data = data.rename(columns={'1. open': 'open', '2. high': 'high', '3. low': 'low', '4. close': 'close', '5. volume': 'volume'})
        return data.sort_index(ascending=True)
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None
