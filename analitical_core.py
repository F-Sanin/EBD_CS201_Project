import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

ford_data = yf.download(tickers="F", start='2022-01-01', end='2026-01-01')
print(ford_data.head())


ford_data["SMA_short"] = ford_data["Close"].rolling(20).mean()
ford_data["SMA_long"] = ford_data["Close"].rolling(50).mean()
ford_data.dropna(inplace=True)


ford_data["Position"] = np.where(ford_data["SMA_short"] > ford_data["SMA_long"], 1 ,0)
ford_data["Signal"] = ford_data["Position"]- ford_data["Position"].shift(1)


ford_data["Market_Returns"] = ford_data["Close"].pct_change()
ford_data["Strategy_Returns"] = ford_data["Market_Returns"]*ford_data["Position"].shift(1).fillna(0)
ford_data["Cumulative_Market"] = (1+ford_data["Market_Returns"]).cumprod()
ford_data["Cumulative_Strategy"] = (1+ford_data["Strategy_Returns"]).cumprod()


buy_signal = ford_data[ford_data["Signal"] == 1]
sell_signal = ford_data[ford_data["Signal"] == -1]

plt.figure(figsize = (12,6))
plt.plot(ford_data.index, ford_data["Close"], color="red", label="Close price")
plt.plot(ford_data.index, ford_data["SMA_short"], color="purple", label="SMA (20)")
plt.plot(ford_data.index, ford_data["SMA_long"], color="orange", label="SMA (50)")

plt.scatter(buy_signal.index,buy_signal["SMA_short"], marker="^", color="green", label="Buy",s=100)
plt.scatter(sell_signal.index, sell_signal["SMA_short"], marker="v", color="red", label="Sell",s=100)
plt.legend(loc="upper left")
plt.title("Market strategy for Ford Motor Company")
plt.show()

plt.figure(figsize=(12, 4))
plt.plot(ford_data.index, ford_data["Cumulative_Market"], color="gray", label="Buy & Hold")
plt.plot(ford_data.index, ford_data["Cumulative_Strategy"], color="green", label="Product strategy")
plt.legend(loc="upper left")
plt.title("Cumulative Returns: Strategy vs Market")
plt.show()



