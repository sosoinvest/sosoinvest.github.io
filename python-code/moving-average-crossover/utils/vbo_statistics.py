import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.colors as colors

class VBOStatistics:
  def __init__(self, filename, K):
    self.filename = filename
    self.df = pd.read_csv(filename)
    self.K = K
    self.data = {
      "Day":[],
      "Target":[],
      "Buy sign":[],
      "Return":[],
      "%Range":[],
      "%Change":[],
      "%Target to open":[],
    }
    self.stats = {
    }
    self.return_over_days = {
    }

  def get_statistics_data(self):
    day_index = 0
    is_loop_on = True

    while is_loop_on:
      day_index += 1
      if day_index > len(self.df["Date"])-1:
        is_loop_on = False
      else:
        day = self.df["Date"][:11]
        open_ = self.df["Open"][day_index - 1]
        close_ = self.df["Close"][day_index - 1]
        high_ = self.df["High"][day_index - 1]
        low_ = self.df["Low"][day_index - 1]

        open__ = self.df["Open"][day_index]
        close__ = self.df["Close"][day_index]
        high__ = self.df["High"][day_index]
        low__ = self.df["Low"][day_index]

        bandwidth = high_ - low_
        target = open__ + self.K * bandwidth
        return_ = (close__ - target) / target * 100
        pctrange = bandwidth/open_*100
        pctchange = (close_-open_)/open_*100
        pct_target_to_open = (target-open__)/open__*100

        if high__ > target:
          buy_sign = True
        else:
          buy_sign = False

        self.data["Day"].append(day)
        self.data["Target"].append(target)
        self.data["Buy sign"].append(buy_sign)
        self.data["Return"].append(return_)
        self.data["%Range"].append(pctrange)
        self.data["%Change"].append(pctchange)
        self.data["%Target to open"].append(pct_target_to_open)

  def get_terminal_return(self):
    terminal = 1
    for return_ in np.array(self.data["Return"])[self.data["Buy sign"]]:
      terminal *= 1 + return_*0.01
    self.terminal = terminal

    terminal_bnh = (self.df["Close"].iloc[-1] - self.df["Open"].iloc[0])/self.df["Open"].iloc[0]
    self.terminal_bnh = terminal_bnh

    print(f"Termianl return: {terminal}")
    print(f"Termianl return(Buy and hold): {terminal_bnh}")

  def get_stat(self):
    buy_sign_list = self.data["Buy sign"]
    return_list = np.array(self.data["Return"])

    number_of_trades = int(sum(buy_sign_list))
    winning_rate = np.round(int(sum(return_list[buy_sign_list]>0))/number_of_trades,2)

    return_list = return_list[buy_sign_list]
    mean_profit = np.round(np.mean(return_list[return_list>0]),2)
    mean_loss = np.round(np.mean(return_list[return_list<0]),2)
    RR = abs(np.round(mean_profit/mean_loss,2))

    self.stats["# of trades"] = number_of_trades
    self.stats["%Win"] = winning_rate
    self.stats["Mean profit"] = mean_profit
    self.stats["Mean loss"] = mean_loss
    self.stats["RR"] = RR

    print(f"Number of trades: {number_of_trades}")
    print(f"%Win: {winning_rate}")
    print(f"Mean profit: {mean_profit}")
    print(f"Mean loss: {mean_loss}")
    print(f"RR: {RR}")

  def get_return_over_days(self):
    ind = 0
    open_ = self.df["Open"]
    close_ = self.df["Close"]
    buy_sign_list = self.data["Buy sign"]

    day_0_return_list = []
    day_1_return_list = []
    day_2_return_list = []
    day_3_return_list = []
    day_4_return_list = []
    day_5_return_list = []

    for ind in range(len(self.df["Open"])-1):
      target = self.data["Target"][ind]
      try:
        if buy_sign_list[ind]:
          day_0_return = (close_[ind] - target) / target*100
          day_1_return = (close_[ind + 1] - target) / target*100
          day_2_return = (close_[ind + 2] - target) / target * 100
          day_3_return = (close_[ind + 3] - target) / target * 100
          day_4_return = (close_[ind + 4] - target) / target * 100
          day_5_return = (close_[ind + 5] - target) / target * 100

          day_0_return_list.append(day_0_return)
          day_1_return_list.append(day_1_return)
          day_2_return_list.append(day_2_return)
          day_3_return_list.append(day_3_return)
          day_4_return_list.append(day_4_return)
          day_5_return_list.append(day_5_return)

      except:
        pass
      self.return_over_days["Day 0"] = day_0_return_list
      self.return_over_days["Day 1"] = day_1_return_list
      self.return_over_days["Day 2"] = day_2_return_list
      self.return_over_days["Day 3"] = day_3_return_list
      self.return_over_days["Day 4"] = day_4_return_list
      self.return_over_days["Day 5"] = day_5_return_list

    print(f"Return Day+0: {np.mean(day_0_return_list)}")
    print(f"Return Day+1: {np.mean(day_1_return_list)}")
    print(f"Return Day+2: {np.mean(day_2_return_list)}")
    print(f"Return Day+3: {np.mean(day_3_return_list)}")
    print(f"Return Day+4: {np.mean(day_4_return_list)}")
    print(f"Return Day+5: {np.mean(day_5_return_list)}")

  def get_running_simulation(self, over_day):
    day_index = 0

    return_list = []
    is_loop_on = True

    while is_loop_on:
      day_index += 1
      if day_index > len(self.df["Date"]) - 1:
        is_loop_on = False
      else:
        day = self.df["Date"][:11]
        open_ = self.df["Open"][day_index - 1]
        close_ = self.df["Close"][day_index - 1]
        high_ = self.df["High"][day_index - 1]
        low_ = self.df["Low"][day_index - 1]

        open__ = self.df["Open"][day_index]
        close__ = self.df["Close"][day_index]
        high__ = self.df["High"][day_index]
        low__ = self.df["Low"][day_index]

        bandwidth = high_ - low_
        target = open__ + self.K * bandwidth
        buy_sign = True if high__>target else False
        if buy_sign:
          day_index += over_day
          try:
            return_list.append(100*(self.df["Close"][day_index] - target)/target)
          except:
            pass
    return return_list

TIKR = "SOXL"
filename = f"data/{TIKR}.csv"
my_test = VBOStatistics(filename, 0.5)
my_test.get_statistics_data()
my_test.get_terminal_return()
my_test.get_stat()
my_test.get_return_over_days()

# fig, ax = plt.subplots(1, 3, figsize=(12,6))
# norm = colors.Normalize(vmin=-20, vmax=20)
#
# ax[0].scatter(np.array(my_test.data["%Range"])[my_test.data["Buy sign"]],
#           np.array(my_test.data["Return"])[my_test.data["Buy sign"]],
#           c=np.array(my_test.data["Return"])[my_test.data["Buy sign"]],
#           marker="o",
#            cmap="seismic", norm=norm)
# ax[0].set_xlabel("%Range")
# ax[0].set_ylabel("Return [%]")
# ax[0].grid(True)
#
# ax[1].scatter(np.array(my_test.data["%Change"])[my_test.data["Buy sign"]],
#           np.array(my_test.data["Return"])[my_test.data["Buy sign"]],
#           c=np.array(my_test.data["Return"])[my_test.data["Buy sign"]],
#           marker="o",
#            cmap="seismic", norm=norm)
# ax[1].set_xlabel("%Change")
# ax[1].set_ylabel("Return [%]")
# ax[1].grid(True)
#
# ax[2].scatter(np.array(my_test.data["%Target to open"])[my_test.data["Buy sign"]],
#           np.array(my_test.data["Return"])[my_test.data["Buy sign"]],
#           c=np.array(my_test.data["Return"])[my_test.data["Buy sign"]],
#           marker="o",
#            cmap="seismic", norm=norm)
# ax[2].set_xlabel("%Target to open")
# ax[2].set_ylabel("Return [%]")
# ax[2].grid(True)
# plt.show()

fig, ax = plt.subplots(1, 1, figsize=(8,6))
ax.plot(my_test.return_over_days["Day 0"], label="Day +0")
ax.plot(my_test.return_over_days["Day 1"], label="Day +1")
ax.plot(my_test.return_over_days["Day 2"], label="Day +2")
ax.plot(my_test.return_over_days["Day 3"], label="Day +3")
ax.plot(my_test.return_over_days["Day 4"], label="Day +4")
ax.plot(my_test.return_over_days["Day 5"], label="Day +5")
plt.legend()

return_over_day = my_test.get_running_simulation(1)

terminal = 5
for return_ in return_over_day:
  return_ = return_ if return_>-6 else -6
  terminal*=1 + (return_-0.5)*0.01
print(terminal)

# ax.hist(np.array(my_test.data["Return"])[my_test.data["Buy sign"]], bins=30)
# ax.grid(True)
# plt.show()