import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

ford_data = yf.download(tickers="F", start='2022-01-01', end='2026-01-01')
print(ford_data.head())

ford_data["SMA_short"] = ford_data["Close"].rolling(20).mean()
ford_data["SMA_long"] = ford_data["Close"].rolling(50).mean()

ford_data["Position"] = np.where(ford_data["SMA_short"] > ford_data["SMA_long"], 1 ,0)
ford_data["Signal"] = ford_data["Position"]- ford_data["Position"].shift(1)
ford_data[ford_data["Signal"].isin([1,-1])]

ford_data["Market_Returns"] = ford_data["Close"].pct_change()
ford_data["Strategy_Returns"] = ford_data["Market_Returns"]*ford_data["Position"].shift(1)
ford_data["Cumulative_Strategy"] = (1+ford_data["Market_Returns"]).cumprod()



