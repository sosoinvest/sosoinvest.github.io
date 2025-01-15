import pandas as pd

def make_table(df):
  number = 0
  for row in df.iterrows():
    number += 1

    name = row[1]["종목명"]
    tikr = row[1]["티커"]
    times = row[1]["배율"]
    day_listed = row[1]["상장일"]
    base_index = row[1]["기초지수"]
    market_cap = row[1]["시가총액"].replace("M","") if type(row[1]["시가총액"]) == str else row[1]["시가총액"]
    number_of_assets = row[1]["구성종목수"]
    # print(market_cap)

    if market_cap != 0:
      print(f"|{number}|{tikr}|{name}|{base_index}|{times}|{day_listed}|{market_cap}|")
    else:
      number -= 1


filename = "Leveraged and inverse ETF list - Microsectors.csv"
df = pd.read_csv(filename)
make_table(df)
print(df)


