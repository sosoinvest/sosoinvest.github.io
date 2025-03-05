import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import tear_sheet

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

positions = pd.Series(np.where(data["Short_MA"] > data["Long_MA"], 1, 0), index=data.index)
signals = positions.diff().fillna(0)

data["Position"] = np.nan
data.loc[signals==1, "Position"] = 1
data.loc[signals==-1, "Position"] = 0
data["Position"] = data["Position"].ffill()
data["Position"] = data["Position"].replace(np.nan, 0)

data["Signal"] = data["Position"].diff().fillna(0)

prices = data["Close"].values
prices = [value[0] for value in prices]

data["Buy_Price"] = np.where(data["Signal"]==1, prices, np.nan)
data["Sell_Price"] = np.where(data["Signal"]==-1, prices, np.nan)

data["Daily_Return"] = np.where(data["Position"].shift()==1, [value[0] for value in data["Close"].pct_change().values], 0)
data["Cumulative_Return"] = (1+data["Daily_Return"]).cumprod()
final_cum_return = data["Cumulative_Return"].iloc[-1] - 1
print(f"Final cumulative return of the strategy: {100*final_cum_return:.2f}%")
tear_sheet.tear_sheet1(data)
input("")

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