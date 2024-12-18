# BLOCK: Import modules
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


TIKR = "SPY"
interval = "1d"
ticker = yf.Ticker(TIKR)
# start = datetime.today() - timedelta(730)
# end = datetime.today()
start = datetime(1985, 1, 1)
end = datetime.today()

price_data = ticker.history(start=start, end=end, period="1d", interval=interval)
print(price_data)
does_save = True

# csv 파일로 저장
filename = f"{TIKR}_{start.strftime("%Y-%m-%d")}_{end.strftime("%Y-%m-%d")}_interval={interval}.csv"
if does_save:
    price_data.to_csv(filename, index=True)