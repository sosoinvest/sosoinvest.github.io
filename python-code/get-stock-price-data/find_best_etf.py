# BLOCK: Import modules
import yfinance as yf
from datetime import datetime, timedelta
import etf_list2
from tabulate import tabulate

def get_data_from_yfinance(TIKR,start,end):
  interval = "1d"
  ticker = yf.Ticker(TIKR)

  daily_data = ticker.history(start=start, end=end, period="1d", interval=interval)
  return daily_data

trading_money_list = {
  "Code": [],
  "Trading money": [],
}

for data in etf_list2.etf_list.values():
  start = datetime.today() - timedelta(days=30)
  end = datetime.today()
  daily_data = get_data_from_yfinance(data+".KS", start, end)
  trading_money = daily_data["Volume"]*daily_data["Close"]
  trading_money_list["Code"].append(data)
  trading_money_list["Trading money"].append(trading_money.median())

# print(trading_money_list["Trading money"].index(max(trading_money_list["Trading money"])))
trading_money_list["Trading money"] = trading_money_list["Trading money"]

sorted_money_list, sorted_code_list = zip(*sorted(zip(trading_money_list["Trading money"], trading_money_list["Code"]),reverse=True))
trading_money_list["Trading money"] = sorted_money_list
trading_money_list["Code"] = sorted_code_list

print(datetime.now())
print(tabulate(trading_money_list))