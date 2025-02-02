import pandas as pd
import numpy as np

tikr = "466920"
filename = f"{tikr} 과거 데이터.csv"
df = pd.read_csv(filename)
df = df[::-1]

date = list(df["날짜"])
date = [value.replace(" ","") for value in date]

open_ = list(df["시가"])
open_ = [value.replace(",","") for value in open_]
high_ = list(df["고가"])
high_ = [value.replace(",","") for value in high_]
low_ = list(df["저가"])
low_ = [value.replace(",","") for value in low_]
close_ = list(df["종가"])
close_ = [value.replace(",","") for value in close_]

volume = list(df["거래량"])
new_volume = []
for vol in volume:
  if type(vol) == str:
    if "K" in vol:
      vol = float(vol.replace("K",""))*1000

    elif "M" in vol:
      vol = float(vol.replace("M",""))*1000000
  new_volume.append(vol)
volume = new_volume

new_df = pd.DataFrame()
new_df["Date"] = date
new_df["Open"] = open_
new_df["High"] = high_
new_df["Low"] = low_
new_df["Close"] = close_
new_df["Volume"] = volume

index_list = []
for ind in range(0, len(date)):
  if open_[ind] == high_[ind] and open_[ind] == low_[ind]:
    print(open_[ind])
    print(high_[ind])
    index_list.append(ind)
    print(date[ind])
  ind+=1

new_df = new_df.drop(index_list).reset_index(drop=True)

new_df.to_csv(f"{tikr}.csv", index=False)