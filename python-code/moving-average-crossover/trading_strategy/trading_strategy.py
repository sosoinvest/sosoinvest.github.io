#BLOCK: Import modules
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from utils import intraday_generator
from matplotlib import pyplot as plt
from tabulate import tabulate
import gc, math

class Strategy:
  def __init__(self,
               df,
               account, logger, analyzer,
               fee, tax, slippage,
               leverage, losscut,
               does_save,
               tikr):
    self.df = df
    self.account = account
    self.logger = logger
    self.analyzer = analyzer
    self.fee = fee
    self.tax = tax
    self.slippage = slippage
    self.does_save = does_save
    self.leverage = leverage
    self.losscut = losscut
    self.tikr = tikr

  def get_price(self, ind):
    open = self.df["Open"][ind]
    high = self.df["High"][ind]
    low = self.df["Low"][ind]
    close = self.df["Close"][ind]

    return open, high, low, close

  def logging_data(self,
                   today,
                   open, close, high, low,
                   target_price,
                   normal_factor,
                   buy_sign,
                   tag, mdd):
    self.logger.log_data("Day", today)
    self.logger.log_data("Cash", self.account.data["Total"][0])
    self.logger.log_data("Portfolio", sum(self.account.data["Total"][1:]))
    self.logger.log_data("Total", sum(self.account.data["Total"][:]))
    self.logger.log_data("Open", open * normal_factor)
    self.logger.log_data("Close", close * normal_factor)
    self.logger.log_data("High", high * normal_factor)
    self.logger.log_data("Low", low * normal_factor)
    self.logger.log_data("Signal", buy_sign)
    self.logger.log_data("Target price", target_price * normal_factor)
    self.logger.log_data("Tag", tag)
    self.logger.log_data("MDD", mdd)
