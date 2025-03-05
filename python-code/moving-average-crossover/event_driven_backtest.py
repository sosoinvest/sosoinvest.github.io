import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

ticker = "AAPL"
start_date = "2022-08-01"
end_date = "2025-02-18"
df = yf.download(ticker, start=start_date, end=end_date)

short_window = 10
long_window = 20
data = df.copy()

data["Short_MA"] = data["Close"].ewm(span=short_window, adjust=False).mean()
data["Long_MA"] = data["Close"].ewm(span=long_window, adjust=False).mean()
data = data[long_window:].copy()

data["Position"] = np.where(data["Short_MA"] > data["Long_MA"], 1, 0)
data["Signal"] = data["Position"].diff().fillna(0)

cash_init = 1000000
cash = cash_init
asset = np.zeros(len(data))
asset[0] = cash
pos = 0

prices = data["Close"].values
prices = [value[0] for value in prices]
signals = data["Signal"].values

for i in range(1, len(data)):
  if pos == 0:
    if signals[i] == 1:
      # print("Golden cross")
      pos = 1
      entry_price = prices[i]
      num = int(cash/entry_price)
      cash -= entry_price*num

  elif pos == 1:
    if signals[i] == -1:
      # print("Dead cross")
      pos = 0
      cash += prices[i]*num

  if pos == 0:
    asset[i] = cash
  elif pos == 1:
    asset[i] = cash + prices[i]*num

data["Buy_Price"] = np.where(data["Signal"]==1, prices, np.nan)
data["Sell_Price"] = np.where(data["Signal"]==-1, prices, np.nan)
print(data)
data["Cumulative_Return"] = np.array(asset)/cash_init
final_cum_return = data["Cumulative_Return"].iloc[-1] - 1
print(f"Final cumulative return of the strategy: {100*final_cum_return:.2f}%")

# BLOCK
fig, ax = plt.subplots(2, 1, sharex=True, height_ratios=(8,2), figsize=(10,8))
data["Close"].plot(ax=ax[0], label="Close")
data["Short_MA"].plot(ax=ax[0], label="Short MA", linewidth=1)
data["Long_MA"].plot(ax=ax[0], label="Long MA", linewidth=1)
data["Buy_Price"].plot(ax=ax[0], label="Buy", marker="^", color="b", markersize=8)
data["Sell_Price"].plot(ax=ax[0], label="Sell", marker="v", color="r", markersize=8)

ax[0].set_title(f"{ticker} Moving Average Crossover Trades", fontsize=18)
ax[0].set_ylabel("Price($)", fontsize=12)
ax[0].legend(fontsize=12)
ax[0].grid(alpha=0.3)

data["Position"].plot(ax=ax[1])
ax[1].set_xlabel("Date", fontsize=12)
ax[1].set_ylabel("Position", fontsize=12)
ax[1].grid(alpha=0.3)

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()