import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

ford_data = yf.download(tickers="F", start='2022-01-01', end='2026-01-01')
print(ford_data.head())

ford_data["SMA_short"] = ford_data["Close"].rolling(20).mean()
ford_data["SMA_long"] = ford_data["Close"].rolling(50).mean()
