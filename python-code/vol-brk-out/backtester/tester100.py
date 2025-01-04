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

    self.df = pd.read_json(filename)

    if strategy == "VolBrkOut":
      self.strategy = trading_strategy.VolBrkOut_(df=self.df,
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
  def run(self):
    self.strategy.run()
