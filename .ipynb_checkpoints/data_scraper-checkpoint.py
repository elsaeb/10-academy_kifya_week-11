import yfinance as yf
import pandas as pd
import os

#tickers and date range
tickers = ["TSLA", "BND", "SPY"]
start_date = "2015-01-01"
end_date = "2024-10-31"

data = yf.download(tickers, start=start_date, end=end_date, group_by="ticker")

# Create a directory for saving data if it doesn't exist
data_dir = "Data"
os.makedirs(data_dir, exist_ok=True)

data["TSLA"].to_csv(f"{data_dir}/TSLA_data.csv")
data["BND"].to_csv(f"{data_dir}/BND_data.csv")
data["SPY"].to_csv(f"{data_dir}/SPY_data.csv")

print("Data saved in the /Data directory.")
