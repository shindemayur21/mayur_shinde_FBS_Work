import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

tickers = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"  # Use full Nifty 50 list as needed
]

end_date = datetime.today()
start_date = end_date - timedelta(days=90)  # last 3 months

all_data = []

for ticker in tickers:
    data = yf.download(ticker, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'), progress=False)
    if data.empty:
        continue
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
    data['LTP'] = data['CLOSE']
    data['VWAP'] = None
    all_data.append(data)

final_df = pd.concat(all_data, ignore_index=True)
final_df.rename(columns={'Prev Close': 'PREV. CLOSE'}, inplace=True)
final_df = final_df[['DATE', 'OPEN', 'HIGH', 'LOW', 'PREV. CLOSE', 'LTP', 'CLOSE', 'VWAP', 'VOLUME', 'Ticker']]

# Save to Excel file
final_df.to_excel("nifty50_3months_data.xlsx", index=False)
print("Data saved to nifty50_3months_data.xlsx")
