import pandas as pd
import numpy as np

df = pd.read_csv("Nasdaq100_daily_1985-2024.csv")
df = df.iloc[::-1].reset_index(drop=True)

is_end_of_data = False
day_index = 0

account = 1

while not is_end_of_data:
  day_index += 1

  if day_index > len(df):
    is_end_of_data = True
  else:
    if day_index > 199:
      ma200 = np.mean(df["Close"][day_index-200:day_index])

  close = df["Close"][day_index]

  if close > ma200:
    account = account/close

