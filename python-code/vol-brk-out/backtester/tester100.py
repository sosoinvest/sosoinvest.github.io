import numpy as np
import pandas as pd
from trading_strategy import trading_strategy
from account import account
from utils import analyzer, logger

class Backtester:
  def __init__(self, filename, tikr, does_save,
               fee, tax, slippage, leverage, losscut,
               deposit_cash=10000,
               strategy="VolBrkOut", params= {"K": 0.5}, window=1):
    self.params = params
    self.strategy = strategy
    self.does_save = does_save
    self.filename = filename
    self.tikr = tikr
    self.fee = fee
    self.slippage = slippage
    self.tax = tax
    self.leverage = leverage
    self.losscut = losscut

    self.account = account.Account()
    self.logger = logger.Logger()
    self.analyzer = analyzer.Analyzer()

    self.account.deposit_cash(deposit_cash)

    self.df = pd.read_csv(filename)
    # self.set_window(window=window)

    if strategy == "VolBrkOut":
      self.strategy = trading_strategy.VolBrkOut(df=self.df,
                                                 account=self.account, logger=self.logger, analyzer=self.analyzer,
                                                 fee=self.fee, tax=self.tax, slippage=self.slippage,
                                                 leverage=self.leverage, losscut=self.losscut,
                                                 does_save=self.does_save,
                                                 tikr=self.tikr,
                                                 K=params["K"])
    elif strategy == "VolBrkOut_intraday":
      self.strategy = trading_strategy.VolBrkOut_intraday2(df=self.df,
                                                          account=self.account, logger=self.logger, analyzer=self.analyzer,
                                                          fee=self.fee, tax=self.tax, slippage=self.slippage,
                                                          leverage=self.leverage, losscut=self.losscut,
                                                          does_save=self.does_save,
                                                          tikr=self.tikr,
                                                          file_for_intra_day_patterns = params["file_for_intra_day_patterns"],
                                                          K=params["K"])

  def run(self):
    self.strategy.run()

  def set_window(self, window):
    Date_list = []
    Open_list = []
    High_list = []
    Low_list = []
    Close_list = []
    ind = 0

    while True:
      try:
        date = self.df["Date"][ind + window]
        open = self.df["Open"][ind]
        close = self.df["Close"][ind + window]
        high = max(self.df["High"][ind : ind+window])
        low = min(self.df["Low"][ind: ind + window])

        Date_list.append(date)
        Open_list.append(open)
        Close_list.append(close)
        High_list.append(high)
        Low_list.append(low)
        ind += window

      except:
        self.df = pd.DataFrame({
          "Date": Date_list,
          "Open": Open_list,
          "Close": Close_list,
          "High": High_list,
          "Low": Low_list
        })
        return

