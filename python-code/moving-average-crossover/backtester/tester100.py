import numpy as np
import pandas as pd
from trading_strategy import trading_strategy, mac_strategy
from account import account
from utils import analyzer, logger

class Backtester:
  def __init__(self, filename, tikr, does_save,
               fee, tax, slippage, leverage, losscut,
               deposit_cash=10000,
               strategy="VolBrkOut", params= {"K": 0.5}, window=1):

    # BLOCK: Set parameters
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

    # BLOCK: Get dataframe
    if strategy != "VolBrkOut_multi":
      file_extension = filename[-3:]

      if file_extension == "json":
        self.df = pd.read_json(filename)

      elif file_extension == "csv":
        self.df = pd.read_csv(filename)

    # BLOCK: Set strategy
    if strategy == "VolBrkOut_ohlc":
      self.strategy = trading_strategy.VolBrkOut_ohlc(df=self.df,
                                                 account=self.account, logger=self.logger, analyzer=self.analyzer,
                                                 fee=self.fee, tax=self.tax, slippage=self.slippage,
                                                 leverage=self.leverage, losscut=self.losscut,
                                                 does_save=self.does_save,
                                                 tikr=self.tikr,
                                                 K=params["K"])
    elif strategy == "VolBrkOut_intraday":
      self.strategy = trading_strategy.VolBrkOut_intraday(df=self.df,
                                                  account=self.account, logger=self.logger, analyzer=self.analyzer,
                                                  fee=self.fee, tax=self.tax, slippage=self.slippage,
                                                  leverage=self.leverage, losscut=self.losscut,
                                                  does_save=self.does_save,
                                                  tikr=self.tikr,
                                                  K=params["K"])
    elif strategy == "VolBrkOut_ohlc_multi":
      self.df = {

      }
      for tikr in self.tikr:
        self.df[tikr] = pd.read_csv(f"{tikr}.csv")

      self.strategy = trading_strategy.VolBrkOut_ohlc_multi(df=self.df,
                                                          account=self.account, logger=self.logger,
                                                          analyzer=self.analyzer,
                                                          fee=self.fee, tax=self.tax, slippage=self.slippage,
                                                          leverage=self.leverage, losscut=self.losscut,
                                                          does_save=self.does_save,
                                                          tikr=self.tikr,
                                                          K=params["K"])
    elif strategy == "MAC":
      self.df = {

      }
      self.df = pd.read_csv(f"{tikr}.csv")

      self.strategy = mac_strategy.MovAvgCrs(df=self.df,
                                            account=self.account, logger=self.logger,
                                            analyzer=self.analyzer,
                                            fee=self.fee, tax=self.tax, slippage=self.slippage,
                                            leverage=self.leverage, losscut=self.losscut,
                                            does_save=self.does_save,
                                            tikr=self.tikr,
                                            windows=params["Windows"])
# BLOCK: Run the test
  def run(self):
    self.strategy.run()
