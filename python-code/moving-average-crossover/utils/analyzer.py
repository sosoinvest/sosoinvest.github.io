import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from tabulate import tabulate
import math


class Analyzer:
  """
  Analyzes the trading data.
  It computes evaluating numbers of the trading.
  """

  def __init__(self, filename=""):
    """
    df: [DataFrame] loaded from the file
    daily_return: [float] A list of daily returns computed from the trading data
    daily_return_bnh: [float] A list of daily returns computed from the buy and hold data
    analysis_result: [dictionary] Storagy saving the results of the analysis

    :param filename: Name of the trading data file to import
    """
    self.df = []
    self.daily_return = []
    self.daily_return_bnh = []

    self.analysis_result = {}
    self.filename = filename

  def save_report(self):
    """
    Save the analysis data as a text file.
    :return:
    """
    filename = self.filename.replace(".csv", ".txt")
    with open(filename, "w") as data_file:
      data_file.write(tabulate(self.analysis_result, headers="keys", tablefmt="pretty"))

  def compute_daily_return(self):
    """
    Computes daily return of the trading.
    It also computes the daily return of the buy and hold strategy.
    :return:
    """
    daily_total = list(self.df["Total"])
    daily_bnh = list(self.df["Close"])

    return (np.round(np.diff(daily_total) / daily_total[1:] * 100, 2),
            np.round(np.diff(daily_bnh) / daily_bnh[1:] * 100, 2))

  def report(self):
    """
    Report the analysis data.
    :return:
    """
    self.df = pd.read_csv(self.filename)
    self.daily_return, self.daily_return_bnh = self.compute_daily_return()

    self.num_of_days()
    self.final_return()
    self.buy_and_hold_return()
    self.get_mdd("Portfolio")
    self.get_mdd("Buy and Hold")
    self.get_cagr()
    self.num_of_trades()
    self.num_of_wins()
    self.win_percent()

    self.get_sharp_ratio(case="Portfolio")
    self.get_sharp_ratio(case="Buy and hold")
    self.get_mean_return()

    # self.max_min_return()
    # self.max_serial_win()
    self.annual_analysis()

    print(tabulate(self.analysis_result, headers="keys", tablefmt="pretty"))

  def buy_and_hold_return(self):
    """
    Computes the final return of buy and hold strategy
    :return:
    """
    initial = self.df["Close"].iloc[0]
    terminal = self.df["Close"].iloc[-1]
    final_return = np.round((terminal - initial) / initial * 100, 2)
    self.analysis_result["Buy and hold return"] = [f"{final_return} %"]

  def final_return(self):
    """
    Computes the final return of trading strategy.
    :return:
    """
    initial = self.df["Total"].iloc[0]
    terminal = self.df["Total"].iloc[-1]
    final_return = np.round((terminal - initial) / initial * 100, 2)
    self.analysis_result["Final return"] = [f"{final_return} %"]

  def get_mdd(self, option):
    """
    Computes the MDD(Maximum Draw Down)
    :return:
    """
    max_run = 0
    mdd = 0
    if option != "Buy and Hold":
      for money in self.df["Total"]:
        max_run = max(money, max_run)
        mdd = min(mdd, (money - max_run) / max_run)
      mdd *= 100
      self.analysis_result["MDD"] = [f"{np.round(mdd, 2)} %"]
    else:
      for money in self.df["Close"]:
        max_run = max(money, max_run)
        mdd = min(mdd, (money - max_run) / max_run)
      mdd *= 100
      self.analysis_result["MDD(Buy and Hold)"] = [f"{np.round(mdd, 2)} %"]

  def get_cagr(self):
    """
    Computes the CAGR(Cumulative Annual Growth Rate)
    :return:
    """
    cagr = 1
    # print(self.daily_return)
    for daily_return in self.daily_return:
      cagr *= (daily_return * 0.01 + 1)
    cagr = cagr ** (1 / len(self.daily_return)) - 1  # The geometric mean return of the daily return
    # cagr = (1 + cagr) ** 252 - 1
    cagr = (1 + cagr) ** 250 - 1
    cagr = np.round(cagr * 100, 2)
    self.analysis_result["CAGR"] = [f"{cagr} %"]

  def num_of_trades(self):
    """
    Computes the number of trades.
    :return:
    """
    self.analysis_result["# of trades"] = [sum([1 if value > 0 else 0 for value in self.df["Signal"]])]

  def num_of_days(self):
    """
    Computes the number of days between the terminal and initial day of the trading.
    :return:
    """
    start_day = self.df["Day"].iloc[0]
    terminal_day = self.df["Day"].iloc[-1]
    date_format = "%Y-%m-%d"
    start_day = datetime.strptime(start_day, date_format)
    terminal_day = datetime.strptime(terminal_day, date_format)
    difference = terminal_day - start_day
    self.analysis_result["Days"] = [difference.days]

  def num_of_wins(self):
    """
    Computes the number of winning of the trading.
    :return:
    """
    golden_cross = np.where(self.df["Signal"] == 1)[0]
    dead_cross = np.where(self.df["Signal"] == -1)[0]

    if dead_cross[0] < golden_cross[0]:
      dead_cross = dead_cross[1:]
    count = 0
    for _ in range(min(len(golden_cross), len(dead_cross))):
      if self.df["Open"].iloc[dead_cross[_]] > self.df["Close"].iloc[golden_cross[_]]:
        count+=1
    self.analysis_result["# of wins"] = [count]

  def win_percent(self):
    """
    Computes the percent of winning of the trading.
    :return:
    """
    golden_cross = np.where(self.df["Signal"] == 1)[0]
    dead_cross = np.where(self.df["Signal"] == -1)[0]

    if dead_cross[0] < golden_cross[0]:
      dead_cross = dead_cross[1:]
    count = 0
    for _ in range(min(len(golden_cross), len(dead_cross))):
      if self.df["Open"].iloc[dead_cross[_]] > self.df["Close"].iloc[golden_cross[_]]:
        count+=1

    trades = sum([1 if value > 0 else 0 for value in self.df["Signal"]])

    self.analysis_result["Winning %"] = [f"{np.round(count / trades * 100, 2)} %"]

  def get_sharp_ratio(self, case):
    """
    Computes the sharp ratio of the trading
    :param case: Select the case between portfolio or buy and hold
    :return:
    """
    if case in ["Portfolio", "Buy and hold"]:
      if case == "Portfolio":
        key_name = "Sharp ratio(Portfolio)"

        # daily_returns = self.daily_return
        golden_cross = np.where(self.df["Signal"] == 1)[0]
        dead_cross = np.where(self.df["Signal"] == -1)[0]
        if dead_cross[0] < golden_cross[0]:
          dead_cross = dead_cross[1:]

        daily_returns = np.array([0])
        for _ in range(min(len(golden_cross),len(dead_cross))):
          daily_returns = np.concatenate((daily_returns, self.daily_return[golden_cross[_]:dead_cross[_]]), axis=0)
        daily_returns = daily_returns[1:]

      elif case == "Buy and hold":
        key_name = "Sharp ratio(Buy and hold)"

        # daily_returns = self.daily_return
        daily_returns = [x for x in self.daily_return_bnh if isinstance(x, (int, float))
                         and not (isinstance(x, float) and math.isnan(x))]  # Check if daily return is nan or not
        daily_returns = np.array(daily_returns)

      mean_return = 1
      for daily_return in daily_returns:
        mean_return *= (daily_return * 0.01 + 1)
      mean_return = mean_return ** (1 / len(daily_returns)) - 1
      mean_return = (1 + mean_return) ** 252 - 1  # It equals to the CAGR

      daily_return = daily_returns * 0.01
      std_return = np.std(daily_return)
      std_return = std_return * np.sqrt(252)  # Annualized standard deviation of the daily return

      sharp_ratio = np.round(mean_return / std_return, 2)
      self.analysis_result[key_name] = [sharp_ratio]
    else:
      print("No matching case for the sharp ratio computation")

  def get_mean_return(self):
    """
    Computes the mean return for the case of win and lose.
    It also computes the RR(Reward-Risk) ratio
    :return:
    """
    golden_cross = np.where(self.df["Signal"] == 1)[0]
    dead_cross = np.where(self.df["Signal"] == -1)[0]

    if dead_cross[0] < golden_cross[0]:
      dead_cross = dead_cross[1:]

    mean_return = []
    for _ in range(min(len(golden_cross), len(dead_cross))):
      price_bought =  self.df["Close"].iloc[golden_cross[_]]
      price_sell = self.df["Open"].iloc[dead_cross[_]]
      mean_return.append((price_sell-price_bought)/price_bought)
    mean_return = np.array(mean_return)

    mean_return_win = np.round(np.mean(mean_return[mean_return > 0]*100),2)
    mean_return_lose = np.round(np.mean(mean_return[mean_return < 0]*100),2)

    self.analysis_result["Mean return win"] = [f"{mean_return_win}%"]
    self.analysis_result["Mean return lose"] = [f"{mean_return_lose}%"]
    self.analysis_result["RR ratio"] = [f"{np.round(mean_return_win / abs(mean_return_lose), 2)}"]

  def mean_return(self):
    daily_return = self.daily_return
    mean_return_win = np.round(daily_return[daily_return > 0].mean(), 2)
    mean_return_lose = np.round(daily_return[daily_return <= 0].mean(), 2)
    self.analysis_result["Mean return win"] = [f"{mean_return_win} %"]
    self.analysis_result["Mean return lose"] = [f"{mean_return_lose} %"]
    self.analysis_result["RR ratio"] = [f"{np.round(mean_return_win/abs(mean_return_lose), 2)}"]

  def max_min_return(self):
    signals = list(self.df["Signal"])
    total = list(self.df["Total"])
    returns_per_trading = []
    total_in = 1
    check_in = 0
    for _ in range(len(signals)):
      if signals[_]:
        total_in = total[_]
        check_in = 1
      elif check_in and signals[_]==0:
        total_out = total[_]
        returns_per_trading.append(np.round((total_out-total_in)/total_in*100,2))
        check_in = 0

    self.returns_per_trading = returns_per_trading

    max_return = max(returns_per_trading)
    min_return = min(returns_per_trading)

    self.analysis_result["Max return"] = [np.round(max_return, 2)]
    self.analysis_result["Min return"] = [np.round(min_return, 2)]

  def max_serial_win(self):
    returns_per_trading = self.returns_per_trading
    serial_win_counter = 0
    serial_win_counter_list = []
    serial_lose_counter = 0
    serial_lose_counter_list = []
    for returns in returns_per_trading:
      if returns > 0:
        serial_lose_counter = 0
        serial_win_counter += 1
        serial_win_counter_list.append(serial_win_counter)
      else:
        serial_win_counter = 0
        serial_lose_counter += 1
        serial_lose_counter_list.append(serial_lose_counter)

    self.analysis_result["Max serial win"] = [max(serial_win_counter_list)]
    self.analysis_result["Max serial lose"] = [max(serial_lose_counter_list)]

  def annual_analysis(self):
    index_init = [0]
    index_term = []
    days = self.df["Day"]
    year = self.df["Day"][0][0:4]
    total = list(self.df["Total"])

    for _ in range(len(days)):
      if days[_][0:4] != year:
        index_term.append(_-1)
        index_init.append(_)
        year = days[_][0:4]
    index_term.append(len(days)-1)

    annual_return = []
    for _ in range(len(index_term)):
      total_init = total[index_init[_]]
      total_term = total[index_term[_]]
      annual_return.append(np.round((total_term-total_init)/total_init*100,2))
      self.analysis_result["Annual return"] = [annual_return]





