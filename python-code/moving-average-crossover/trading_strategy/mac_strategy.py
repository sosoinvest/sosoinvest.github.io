#BLOCK: Import modules
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from utils import intraday_generator
from matplotlib import pyplot as plt
from tabulate import tabulate
import gc, math
from trading_strategy.trading_strategy import Strategy
from trading_strategy.position import Position

# BLOCK: MAC
class MovAvgCrs(Strategy):
  def __init__(self,
               df,
               account, logger, analyzer,
               fee, tax, slippage,
               leverage, losscut,
               does_save,
               tikr, windows):
    super().__init__(df=df,
                     account=account, logger=logger, analyzer=analyzer,
                     fee=fee, tax=tax, slippage=slippage,
                     leverage=leverage, losscut=losscut,
                     does_save=does_save, tikr=tikr)
    self.window = windows

  def run(self):
    is_end_of_data = False

    # Get moving average
    self.df["Short_MA"] = self.df["Close"].ewm(span=self.window[0], adjust=True).mean()
    self.df["Long_MA"] = self.df["Close"].ewm(span=self.window[1], adjust=True).mean()
    self.df = self.df[self.window[1]:].copy()

    # Get signal
    positions = pd.Series(np.where(self.df["Short_MA"] > self.df["Long_MA"], 1, 0), index=self.df.index)
    signals = positions.diff().fillna(0)

    self.df["Position"] = np.nan
    self.df.loc[signals == 1, "Position"] = 1
    self.df.loc[signals == -1, "Position"] = 0
    self.df["Position"] = self.df["Position"].ffill()
    self.df["Position"] = self.df["Position"].replace(np.nan, 0)
    self.df["Signal"] = self.df["Position"].diff().fillna(0)

    day_index = self.window[1]
    position = 0

    while not is_end_of_data:
      day_index += 1

      if day_index > len(self.df["Date"]) - 1:
        is_end_of_data = True

      else:
        today = self.df.iloc[day_index]["Date"]

        # print(today)
        # print(f"Account total: {sum(self.account.data["Total"])}\n")

        open_t = self.df.iloc[day_index]["Open"]
        high_t = self.df.iloc[day_index]["High"]
        low_t = self.df.iloc[day_index]["Low"]
        close_t = self.df.iloc[day_index]["Close"]

        # BLOCK: Check signal
        signal = self.df.iloc[day_index]["Signal"]

        if  position == 0 and signal == 1: # Golden cross
          position = 1
          self.buy_operation(price=close_t)

        elif position == 1 and signal == -1: # Dead cross
          position = 0
          self.sell_operation(price=open_t)
        elif position == 1:
          self.account.update_price(1,close_t)

        # BLOCK: Logging the trading data
        self.logging_data(today=today,
                          open=open_t, close=close_t, high=high_t, low=low_t,
                          target_price=close_t, normal_factor=1,
                          buy_sign=signal, tag=0, mdd=0)

    self.account.sell_asset(tikr=self.tikr,
                            amount="ALL",
                            price_sell=close_t,
                            fee=self.fee,
                            tax=self.tax,
                            slippage=self.slippage)
    # self.logger.print_in_dataframe()

    self.logger.save_data(filename=f"MAC_{self.tikr}_Window=({self.window[0]},{self.window[1]}).csv")
    self.analyzer.filename = f"MAC_{self.tikr}_Window=({self.window[0]},{self.window[1]}).csv"
    self.analyzer.report()
    if self.does_save:
      self.analyzer.save_report()

  def sell_operation(self, price):
    self.account.sell_asset(tikr=self.tikr,
                            amount="ALL",
                            price_sell=price,
                            fee=self.fee,
                            tax=self.tax,
                            slippage=self.slippage)

    return 0

  def buy_operation(self, price):
    # print(f"Buy sign occurs at {day_index}")
    cash = self.account.data["Total"][0]
    size_to_buy = 1.0
    amount_to_buy = np.floor(size_to_buy * cash / price * 100)/100 if cash > 0 else 0

    if amount_to_buy > 1 or True:
      self.account.buy_asset(tikr=self.tikr,
                             amount=amount_to_buy,
                             price_buy=price,
                             fee=self.fee,
                             tax=self.tax,
                             slippage=self.slippage,
                             leverage=self.leverage)
    return 1
