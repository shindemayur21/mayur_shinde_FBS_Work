import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# List of Nifty 50 tickers on Yahoo Finance
tickers = [
    "ADANIENT.NS", "ADANIPORTS.NS", "ASIANPAINT.NS", "AXISBANK.NS", "BAJAJ-AUTO.NS",
    "BAJFINANCE.NS", "BAJAJFINSV.NS", "BHARTIARTL.NS", "BRITANNIA.NS", "CIPLA.NS",
    "COALINDIA.NS", "DIVISLAB.NS", "DRREDDY.NS", "EICHERMOT.NS", "GRASIM.NS",
    "HCLTECH.NS", "HDFCBANK.NS", "HDFCLIFE.NS", "HEROMOTOCO.NS", "HINDALCO.NS",
    "HINDUNILVR.NS", "ICICIBANK.NS", "IOC.NS", "INDUSINDBK.NS", "INFY.NS",
    "ITC.NS", "JSWSTEEL.NS", "KOTAKBANK.NS", "LT.NS", "M&M.NS",
    "MARUTI.NS", "NESTLEIND.NS", "NTPC.NS", "ONGC.NS", "POWERGRID.NS",
    "RELIANCE.NS", "SBILIFE.NS", "SHREECEM.NS", "SBIN.NS", "SUNPHARMA.NS",
    "TATACONSUM.NS", "TCS.NS", "TATASTEEL.NS", "TECHM.NS", "TITAN.NS",
    "ULTRACEMCO.NS", "UPL.NS", "WIPRO.NS", "HDFC.NS", "ASIANPAINT.NS"
    # Add remaining tickers as needed
]

end_date = datetime.today()
start_date = end_date - timedelta(days=1)  # last 3 months

all_data = []

for ticker in tickers:
    data = yf.download(ticker, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    data['Ticker'] = ticker
    data['Prev Close'] = data['Close'].shift(1)
    data = data.reset_index()
    data = data[['Date', 'Open', 'High', 'Low', 'Prev Close', 'Close', 'Volume', 'Ticker']]
    data.rename(columns={
        'Date': 'DATE',
        'Open': 'OPEN',
        'High': 'HIGH',
        'Low': 'LOW',
        'Close': 'CLOSE',
        'Volume': 'VOLUME'
    }, inplace=True)
    # LTP is same as CLOSE in daily data
    data['LTP'] = data['CLOSE']
    # VWAP not available here, leave blank or fill with NaN
    data['VWAP'] = None
    all_data.append(data)

final_df = pd.concat(all_data)
print(final_df.head())

# Save to CSV if needed
final_df.to_csv("nifty50_3months_data_1.csv", index=False)
