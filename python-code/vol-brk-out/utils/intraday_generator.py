# BLOCK: Import modules
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import random

from matplotlib.pyplot import tight_layout

"""
Written: 24.12.19
Revised:
"""

class IntraDayPreprocessor:
  def __init__(self, filename):
    self.df = pd.read_csv(filename)
    self.intraday_data = []
    self.candle_data = []
    self.intraday_candle_data()
    self.get_intraday_data()

  def intraday_candle_data(self):
    df = self.df
    is_end_of_data = False
    ind = 0
    day = df["Datetime"][ind][0:10]

    open_list = []
    close_list = []
    high_list = []
    low_list = []

    new_data = {
      "Day": [],
      "Open": [],
      "High": [],
      "Low": [],
      "Close": [],
    }

    while not is_end_of_data:
      if ind > len(df["Datetime"]) - 1:
        is_end_of_data = True
      else:
        new_day = day != df["Datetime"][ind][0:10]

        if new_day:
          new_data["Day"].append(day)
          new_data["Open"].append(open_list)
          new_data["High"].append(high_list)
          new_data["Low"].append(low_list)
          new_data["Close"].append(close_list)

          day = df["Datetime"][ind][0:10]
          open_list = [df["Open"][ind]]
          high_list = [df["High"][ind]]
          low_list = [df["Low"][ind]]
          close_list = [df["Close"][ind]]

        else:
          open_list.append(df["Open"][ind])
          high_list.append(df["High"][ind])
          low_list.append(df["Low"][ind])
          close_list.append(df["Close"][ind])
      ind += 1
    self.candle_data = new_data

  def get_intraday_data(self):
    for _ in range(len(self.candle_data["Day"])):
      data = self.candle_data["Close"][_]
      data[0] = self.candle_data["Open"][_][0]
      self.intraday_data.append(DailyData(data))

  def normalize(self):
    for obj in self.intraday_data:
      obj.price = obj.price / obj.price[0]

  def range_change(self):
    for obj in self.intraday_data:
      daily_range = (max(obj.price) - min(obj.price))/obj.price[0]
      daily_change = (obj.price[-1] - obj.price[0])/obj.price[0]
      obj.range = daily_range
      obj.change = daily_change

  def search_nearest_data(self, input_range, input_change, n=3):
    daily_range = []
    daily_change = []

    for obj in self.intraday_data:
      daily_range.append(obj.range)
      daily_change.append(obj.change)

    daily_range = np.array(daily_range)
    daily_change = np.array(daily_change)

    indices = np.argsort(abs(daily_range - input_range) + 5*abs(daily_change - input_change))
    return indices[:n]

  def generate_intraday_data(self, open, high, low, close, n=3):
    indices = self.search_nearest_data(input_range = (high-low)/open,
                                       input_change = (close-open)/open,
                                       n=n)

    index = random.choice(indices)
    pattern = self.intraday_data[index].price

    normalized_pattern = (pattern - min(pattern)) / (max(pattern) - min(pattern))
    scaled_pattern = normalized_pattern * (high-low) + low
    noise = np.random.normal(0, (high-low) * (1/195), len(scaled_pattern))
    scaled_pattern += noise

    scaled_pattern[0] = open
    scaled_pattern[-1] = close

    scaled_pattern = np.clip(scaled_pattern, low, high)

    return scaled_pattern

class DailyData:
  def __init__(self, price):
    self.range = 0
    self.change = 0
    self.price = price

# filename = f"intraday_data/TQQQ_2024-10-19_2024-12-18_interval=2m.csv"
# gen = IntraDayPreprocessor(filename = filename)
# gen.normalize()
# gen.range_change()
#
# open = 10.40
# high = 10.59
# low = 8.49
# close = 8.59
#
# gen_price = gen.generate_intraday_data(open, high, low, close, n=3)
# fig, ax = plt.subplots(1,1, figsize=(8,6), tight_layout=True)
# ax.plot([0, len(gen_price)-1], [open, close], marker="o", linestyle = "none")
# for _ in range(10):
#   gen_price = gen.generate_intraday_data(open, high, low, close, n=3)
#   ax.plot(gen_price)
# ax.axhline(y=high, linestyle="--", color="#E63946", label="High")
# ax.axhline(y=low, linestyle="--", color="#247BA0", label="Low")
# plt.show()
#
#
