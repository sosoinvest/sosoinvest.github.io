import pandas as pd
from matplotlib import pyplot as plt
import scipy
import numpy as np
import data

def get_merged_dataframe(filename):
  df = pd.read_csv(filename + ".csv")
  ind = 0
  is_loop_on = True

  while is_loop_on:
    print(ind)
    ind += 1
    try:
      new_df = pd.read_csv(f"{filename} ({ind}).csv")
      df = pd.merge(df, new_df, how="outer")
    except:
      is_loop_on = False

    df.to_csv("merged.csv", index=0)
    print(df)

def remove_no_data(filename):
  df = pd.read_csv(filename)
  ind = 0
  index_list = []
  for time in df["Time"]:
    if time[:4] == "Down":
      index_list.append(ind)
    ind += 1
  df = df.drop(index=index_list)
  print(df)
  df.to_csv(filename, index=0)

def data_to_dict(filename):
  df = pd.read_csv(filename)

  data_dict = {
    "Day": [],
    "Time": [],
    "Open": [],
    "High": [],
    "Low": [],
    "Close": [],
    "Change": [],
    "%Chg": [],
    "Volume": [],
  }

  time_list = []
  open_list = []
  high_list = []
  low_list = []
  close_list = []
  change_list = []
  pchange_list = []
  volume_list = []

  day = df["Time"][0][:10].replace(" ", "")

  for i in range(len(df["Time"])):
    if day == df["Time"][i][:10].replace(" ", ""):
      time = df["Time"][i][10:].replace(" ", "")

      open = df["Open"][i]
      high = df["High"][i]
      low = df["Low"][i]
      close = df["Last"][i]
      change = df["Change"][i]
      pchange = df["%Chg"][i]
      volume = df["Volume"][i]

      time_list.append(time)
      open_list.append(open)
      high_list.append(high)
      low_list.append(low)
      close_list.append(close)
      change_list.append(change)
      pchange_list.append(pchange)
      volume_list.append(volume)

    else:
      data_dict["Day"].append(day)
      data_dict["Time"].append(time_list)
      data_dict["Open"].append(open_list)
      data_dict["High"].append(high_list)
      data_dict["Low"].append(low_list)
      data_dict["Close"].append(close_list)
      data_dict["Change"].append(change_list)
      data_dict["%Chg"].append(pchange_list)
      data_dict["Volume"].append(volume_list)

      time = df["Time"][i][10:].replace(" ", "")

      open = df["Open"][i]
      high = df["High"][i]
      low = df["Low"][i]
      close = df["Last"][i]
      change = df["Change"][i]
      pchange = df["%Chg"][i]
      volume = df["Volume"][i]

      time_list = [time]
      open_list = [open]
      high_list = [high]
      low_list = [low]
      close_list = [close]
      change_list = [change]
      pchange_list = [pchange]
      volume_list = [volume]

      day = df["Time"][i][:10].replace(" ", "")

    print(i)

  df2 = pd.DataFrame(data_dict)
  df2.to_json(f"{filename.replace(".csv", ".json")}")

# filename = f"data/SOXL_intraday_data/soxl_intraday-1min_historical-data-download-12-24-2024"
# get_merged_dataframe(filename)

remove_no_data("merged_SOXL.csv")
data_to_dict("merged_SOXL.csv")