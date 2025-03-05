import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import tear_sheet, time

def mac_strategy1(df, sw, lw):
  short_window = sw
  long_window = lw
  data = df.copy()

  data["Short_MA"] = data["Close"].ewm(span=short_window, adjust=False).mean()
  data["Long_MA"] = data["Close"].ewm(span=long_window, adjust=False).mean()
  data = data[long_window:].copy()

  positions = pd.Series(np.where(data["Short_MA"] > data["Long_MA"], 1, 0), index=data.index)
  signals = positions.diff().fillna(0)

  data["Position"] = np.nan
  data.loc[signals == 1, "Position"] = 1
  data.loc[signals == -1, "Position"] = 0
  data["Position"] = data["Position"].ffill()
  data["Position"] = data["Position"].replace(np.nan, 0)

  data["Signal"] = data["Position"].diff().fillna(0)

  prices = data["Close"].values
  prices = [value[0] for value in prices]

  data["Buy_Price"] = np.where(data["Signal"] == 1, prices, np.nan)
  data["Sell_Price"] = np.where(data["Signal"] == -1, prices, np.nan)

  data["Daily_Return"] = np.where(data["Position"].shift() == 1,
                                  [value[0] for value in data["Close"].pct_change().values], 0)
  data["Cumulative_Return"] = (1 + data["Daily_Return"]).cumprod()
  final_cum_return = data["Cumulative_Return"].iloc[-1] - 1
  print(f"Final cumulative return of the strategy: {100 * final_cum_return:.2f}%")

  return data, final_cum_return

def mac_strategy2a(df, sw, lw, sl, verbose=True):
  stop_loss = sl
  short_window = sw
  long_window = lw
  data = df.copy()

  data["Short_MA"] = data["Close"].ewm(span=short_window, adjust=False).mean()
  data["Long_MA"] = data["Close"].ewm(span=long_window, adjust=False).mean()
  data = data[long_window:].copy()

  positions = pd.Series(np.where(data["Short_MA"] > data["Long_MA"], 1, 0), index=data.index)
  signals = positions.diff().fillna(0)

  cash_init = 10000000
  cash = cash_init
  asset = np.zeros(len(data))
  asset[0] = cash
  pos = 0

  prices = data["Close"].values
  prices = [value[0] for value in prices]
  signals = signals.values
  pos_vec = np.zeros(len(data))

  for i in range(1, len(data)):
    if pos == 0:
      if signals[i] == 1:
        # print("Golden cross")
        pos_vec[i] = 1
        pos = 1
        entry_price = prices[i]
        num = int(cash / entry_price)
        cash -= entry_price * num
        stop_loss_price = entry_price*(1-stop_loss)

    elif pos == 1:
      if prices[i] < stop_loss_price:
        pos = 0
        cash += prices[i]*num
      elif signals[i]==-1:
        pos = 0
        cash += prices[i]*num
      else:
        pos_vec[i]=1
        stop_loss_price = max(stop_loss, prices[i]*(1-stop_loss))

    if pos == 0:
      asset[i] = cash
    elif pos == 1:
      asset[i] = cash + prices[i] * num

  data["Position"] = pos_vec
  data["Signal"] = data["Position"].diff().fillna(0)
  data["Buy_Price"] = np.where(data["Signal"] == 1, prices, np.nan)
  data["Sell_Price"] = np.where(data["Signal"] == -1, prices, np.nan)

  data["Cumulative_Return"] = np.array(asset) / cash_init
  final_cum_return = data["Cumulative_Return"].iloc[-1] - 1

  if verbose:
    print(f"Final cumulative return of the strategy: {100 * final_cum_return:.2f}%")

  return data, final_cum_return

def parameter_optimizer2a(input_df):
  # short_window = list(range(5,22))
  # long_window = list(range(22,43))
  stop_loss = [0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19]
  ret_list = []

  for x1, x2, x3 in [(a,b,c)
                     for a in short_window
                     for b in long_window
                     for c in stop_loss]:
    df = input_df.copy()
    _, ret = mac_strategy2a(df, x1, x2, x3, verbose=False)
    ret_list.append((x1, x2, x3, ret))

  max_ror = max(ret_list, key=lambda x:x[3])[3]
  max_tups = [tup for tup in ret_list if tup[3]==max_ror]
  params1 = [tup[0] for tup in max_tups]
  params2 = [tup[1] for tup in max_tups]
  params3 = [tup[2] for tup in max_tups]
  opt_param1 = int(np.median(params1))
  opt_param2 = int(np.median(params2))
  opt_param3 = np.median(params3)

  optimal_df = pd.DataFrame(ret_list, columns=["short_window", "long_window", "stop_loss", "ror"])

  print(f"Max Tuples:{max_tups}")
  print(f"Optimal Parameters:{opt_param1, opt_param2, opt_param3}, "
        f"Optimized Return:{100*max_ror:.2f}%")

  return (opt_param1, opt_param2, opt_param3), optimal_df

def parameter_optimizer1b(input_df):
  # short_window = list(range(5,22))
  # long_window = list(range(22,43))
  ret_list = []

  for x1, x2 in [(a,b) for a in short_window for b in long_window]:
    df = input_df.copy()
    _, ret = mac_strategy1(df, x1, x2)
    ret_list.append((x1, x2, ret))

  max_ror = max(ret_list, key=lambda x:x[2])[2]
  max_tups = [tup for tup in ret_list if tup[2]==max_ror]
  params1 = [tup[0] for tup in max_tups]
  params2 = [tup[1] for tup in max_tups]
  opt_param1 = int(np.median(params1))
  opt_param2 = int(np.median(params2))

  optimal_df = pd.DataFrame(ret_list, columns=["short_window", "long_window", "ror"])
  print(f"Max Tuples:{max_tups}")
  print(f"Optimal Parameters:{opt_param1, opt_param2}, "
        f"Optimized Return:{100*max_ror:.2f}%")
  return (opt_param1, opt_param2), optimal_df

def parameter_optimizer(input_df):
  # short_window = list(range(5,22))
  # long_window = list(range(22,43))
  ret_list = []

  for x1, x2 in [(a,b) for a in short_window for b in long_window]:
    df = input_df.copy()
    _, ret = mac_strategy1(df, x1, x2)
    ret_list.append((x1, x2, ret))

  optimal_params = max(ret_list, key=lambda x:x[2])
  optimal_df = pd.DataFrame(ret_list, columns=["short_window", "long_window", "ror"])
  print(f"Optimal Parameters:{optimal_params[0], optimal_params[1]}",
        f"Optimized Return:{100*optimal_params[2]:.2f}%")

  return optimal_params, optimal_df

ticker = "TSLA"
start_date = "2019-01-01"
end_date = "2024-01-01"
df = yf.download(ticker, start=start_date, end=end_date)
print(df)
short_window = list(range(5,17))
long_window = list(range(20,38))

optimal_params, optimal_df = parameter_optimizer2a(input_df=df)
data, ret = mac_strategy2a(df, optimal_params[0], optimal_params[1], optimal_params[2])
tear_sheet.tear_sheet1(data)

# short_grid, long_grid = np.meshgrid(long_window, short_window)
#
# ror = optimal_df["ror"].values
# ror_grid = ror.reshape(len(short_window),len(long_window))
#
# # BLOCK
# fig, ax = plt.subplots(1, 1, figsize=(10,8), subplot_kw={"projection": "3d"})
# ax.plot_surface(short_grid, long_grid, ror_grid, cmap="viridis")
#
# plt.tight_layout()
# plt.show()