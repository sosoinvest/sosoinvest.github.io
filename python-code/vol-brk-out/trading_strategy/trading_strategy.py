#BLOCK: Import modules
import numpy as np
import pandas as pd
from datetime import datetime
from utils import intraday_generator
from matplotlib import pyplot as plt
from tabulate import tabulate
import gc

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

  def get_price(self, ind, normal_factor):
    open = self.df["Open"][ind] / normal_factor
    high = self.df["High"][ind] / normal_factor
    low = self.df["Low"][ind] / normal_factor
    close = self.df["Close"][ind] / normal_factor

    return open, high, low, close

  def logging_data(self,
                   today,
                   open, close, high, low,
                   target_price,
                   normal_factor,
                   buy_sign,
                   tag):
    self.logger.log_data("Day", today)
    self.logger.log_data("Cash", self.account.data["Total"][0])
    self.logger.log_data("Portfolio", sum(self.account.data["Total"][1:]))
    self.logger.log_data("Total", sum(self.account.data["Total"][:]))
    self.logger.log_data("Open", open * normal_factor)
    self.logger.log_data("Close", close * normal_factor)
    self.logger.log_data("High", high * normal_factor)
    self.logger.log_data("Low", low * normal_factor)
    self.logger.log_data("Buy sign", buy_sign)
    self.logger.log_data("Target price", target_price * normal_factor)
    self.logger.log_data("Tag", tag)

# BLOCK: VBO OHLC Single
class VolBrkOut_ohlc(Strategy):
  def __init__(self,
               df,
               account, logger, analyzer,
               fee, tax, slippage,
               leverage, losscut,
               does_save,
               tikr,
               K=0.5):
    super().__init__(df=df,
                     account=account, logger=logger, analyzer=analyzer,
                     fee=fee, tax=tax, slippage=slippage,
                     leverage=leverage, losscut=losscut,
                     does_save=does_save, tikr=tikr)
    self.K = K

  def check_buy_sign(self, high_y, low_y, high_t, open_t, K):
    price_width = high_y - low_y
    target_price = open_t + K*price_width
    buy_sign = 1 if high_t > target_price else 0
    return target_price, buy_sign

  def run(self):
    is_end_of_data = False
    day_index = 0
    normal_factor = self.df["Open"][0] if not(np.isnan(self.df["Open"][0])) else self.df["Open"][1]
    buy_sign = 0

    while not is_end_of_data:
      day_index += 1

      if day_index > len(self.df) - 1:
        is_end_of_data = True

      else:
        today = self.df["Date"][day_index][0:10]

        (open_y, high_y, low_y, close_y) = self.get_price(ind=day_index - 1, normal_factor=normal_factor)
        (open_t, high_t, low_t, close_t) = self.get_price(ind=day_index, normal_factor=normal_factor)

        # BLOCK: Sell operation
        if buy_sign:
          buy_sign = self.sell_operation(open_t=open_t)

        noise = (close_y-open_y)/(high_y-low_y)

        if noise>0.:
          buy_sign  = self.buy_operation(high_y=high_y, low_y=low_y, high_t=high_t, open_t=open_t)


        # BLOCK: Logging the trading data
        self.logging_data(today=today,
                          open=open_t, close=close_t, high=high_t, low=low_t,
                          target_price=0, normal_factor=normal_factor,
                          buy_sign=buy_sign, tag=0)

    self.noise = noise
    self.account.sell_asset(tikr=self.tikr,
                            amount="ALL",
                            price_sell=self.df["Close"].iloc[-1]/normal_factor,
                            fee=self.fee,
                            tax=self.tax,
                            slippage=self.slippage)
    # self.logger.print_in_dataframe()

    self.logger.save_data(filename=f"Backtest_Result_{self.tikr}_Vol_Brk_Out_K={self.K}.csv")
    self.analyzer.filename = f"Backtest_Result_{self.tikr}_Vol_Brk_Out_K={self.K}.csv"
    self.analyzer.report()
    if self.does_save:
      self.analyzer.save_report()

  def sell_operation(self, open_t):

    self.account.sell_asset(tikr=self.tikr,
                            amount="ALL",
                            price_sell=open_t,
                            fee=self.fee,
                            tax=self.tax,
                            slippage=self.slippage)

    return 0

  def buy_operation(self,
                    high_y, low_y,
                    high_t, open_t):

    target_price, buy_sign = self.check_buy_sign(high_y=high_y, low_y=low_y,
                                                 high_t=high_t, open_t=open_t,
                                                 K=self.K)

    if buy_sign:
      # print(f"Buy sign occurs at {day_index}")
      cash = self.account.data["Total"][0]
      size_to_buy = 1
      amount_to_buy = np.floor(size_to_buy * cash / target_price * 100)/100

      if amount_to_buy > 1:
        self.account.buy_asset(tikr=self.tikr,
                               amount=amount_to_buy,
                               price_buy=target_price,
                               fee=self.fee,
                               tax=self.tax,
                               slippage=self.slippage,
                               leverage=self.leverage)
    return buy_sign

# BLOCK: VBO OHLC Intraday
class VolBrkOut_intraday(Strategy):
  def __init__(self, df,
               account, logger, analyzer,
               fee, tax, slippage,
               leverage, losscut,
               does_save,
               tikr,
               K=0.5):

    super().__init__(df=df,
                     account=account, logger=logger, analyzer=analyzer,
                     fee=fee, tax=tax, slippage=slippage,
                     leverage=leverage, losscut=losscut,
                     does_save=does_save, tikr=tikr)
    self.K = K

  def get_atr(self, day_index, window):
    tr_list = []
    for day in range(day_index-window, day_index):
      A = self.df["High(Day)"][day] - self.df["Close(Day)"][day-1]
      B = self.df["Close(Day)"][day-1] - self.df["Open(Day)"][day]
      C = self.df["High(Day)"][day] - self.df["Low(Day)"][day]
      tr = max(A,B,C)
      tr_list.append(tr)

  def get_target_price(self, high_y, low_y, open_t, K):
    price_width = high_y - low_y
    target_price = open_t + K*price_width
    return target_price

  def run(self):
    is_end_of_data = False
    day_index = 0
    buy_sign = 0
    positions = []
    position_history = []
    position_number = 0

    day_index_init = 1
    money_init = sum(self.account.data["Total"])
    year_return_filter = True

    while not is_end_of_data:
      day_index += 1

      if day_index > len(self.df) - 1:
        is_end_of_data = True

      else:
        today = self.df["Day"][day_index]
        year1 = self.df["Day"][day_index][:4]
        year2 = self.df["Day"][day_index-1][:4]
        new_year = year2!=year1
        annual_return = (sum(self.account.data["Total"]) - money_init) / money_init

        if new_year:
          money_init = sum(self.account.data["Total"])
          year_return_filter = True
        elif annual_return <-0.3:
          year_return_filter = False

        print(today)
        print(sum(self.account.data["Total"]))

        open_y = self.df["Open(Day)"][day_index - 1]
        high_y = self.df["High(Day)"][day_index - 1]
        low_y = self.df["Low(Day)"][day_index - 1]
        close_y = self.df["Close(Day)"][day_index - 1]

        pctrange = (high_y-low_y)/open_y

        open_t = self.df["Open(Day)"][day_index]
        high_t = self.df["High(Day)"][day_index]
        low_t = self.df["Low(Day)"][day_index]
        close_t = self.df["Close(Day)"][day_index]

        if len(self.account.data["Ticker"]) > 1:
          index = self.account.data["Ticker"].index(self.tikr)
          self.account.update_price(index, open_t)
        else:
          index = 1

        target_price = self.get_target_price(high_y, low_y, open_t, self.K*0.6)
        intraday_price = self.df["Close"][day_index]

        position_ind = 0
        for position in positions:
          if position.high < open_t or not year_return_filter:
            self.account.sell_asset(tikr=self.tikr,
                                    amount=position.size,
                                    price_sell=open_t,
                                    fee=self.fee,
                                    tax=self.tax,
                                    slippage=self.slippage)
            position.day_exit = today
            position.price_exit = open_t
            del positions[position_ind]
            buy_sign=0
          position_ind += 1

        high = intraday_price[0]

        intra_day_ind = -1
        for price in intraday_price:
          intra_day_ind += 1
          high = max(high, price)

          if pctrange > 0.075 or not year_return_filter:
            continue_trading = False
          else:
            continue_trading = True

          if continue_trading:
            if target_price*(1-0.125*0.01*2) < price < target_price*(1 + 0.125*0.01*2):
              if target_price < self.get_target_price(high_y, low_y, open_t, self.K * 0.8):
                target_price = self.get_target_price(high_y, low_y, open_t, self.K * 0.8)

              elif target_price < self.get_target_price(high_y, low_y, open_t, self.K * 1):
                target_price = self.get_target_price(high_y, low_y, open_t, self.K * 1)

              else:
                target_price = target_price*100

              cash = self.account.data["Total"][0]
              amount_to_buy = np.floor(0.5*cash/price*100)/100 if cash > 0 else 0

              if amount_to_buy > 1:
                position_number += 1
                new_position = Position(position_number, today,
                                        price,
                                        amount_to_buy,
                                        high,
                                        price*(1-self.losscut),
                                        self.account)
                positions.append(new_position)
                position_history.append(new_position)

                self.buy_operation(price=price, size=0.5)
                buy_sign = 1

          position_ind = 0
          for position in positions:
            if position.day != today and price < position.losscut:
              self.account.sell_asset(tikr = self.tikr,
                                     amount = position.size,
                                     price_sell = price,
                                     fee = self.fee,
                                     tax = self.tax,
                                     slippage = self.slippage)
              position.day_exit = today
              position.price_exit = price
              del positions[position_ind]

            elif position.day != today and (price-position.price)/position.price>0.2:
              self.account.sell_asset(tikr=self.tikr,
                                      amount=position.size,
                                      price_sell=price,
                                      fee=self.fee,
                                      tax=self.tax,
                                      slippage=self.slippage)
              position.price_exit = price
              position.day_exit = today
              del positions[position_ind]

              # elif position.day == today:
            else:
              position.high = max(position.high, high)
              position.losscut = position.high*(1-self.losscut)
              # position.losscut += position.high - position.price

            position_ind += 1

      # BLOCK: Logging the trading data
      self.logging_data(today=today,
                        open=open_t, close=close_t, high=high_t, low=low_t,
                        target_price=target_price, normal_factor=1,
                        buy_sign=buy_sign, tag="none")


    self.account.sell_asset(tikr=self.tikr,
                                  amount="ALL",
                                  price_sell=close_t,
                                  fee=self.fee,
                                  tax=self.tax,
                                  slippage=self.slippage)
    # self.logger.print_in_dataframe()
    df = self.position_to_dataframe(position_history)

    number_of_win = sum(np.array(df["Return"]) > 0)
    number_of_trade = sum(np.array(df["Return"]) > 0) + sum(np.array(df["Return"]) < 0)
    print(number_of_win/number_of_trade)
    input("")


    df.to_csv(f"Positions_{self.tikr}_Vol_Brk_Out_K={self.K}.csv", index=False)
    self.logger.save_data(filename=f"Backtest_Result_{self.tikr}_Vol_Brk_Out_K={self.K}.csv")
    self.analyzer.filename = f"Backtest_Result_{self.tikr}_Vol_Brk_Out_K={self.K}.csv"
    self.analyzer.report()

    if self.does_save:
      self.analyzer.save_report()

  def position_to_dataframe(self, position_history):
    df = {
      "Number": [],
      "Day(in)": [],
      "Day(out)": [],
      "Price(in)": [],
      "Price(out)": [],
      "Amount": [],
      "Return": [],
    }
    for position in position_history:
      df["Number"].append(position.number)
      df["Day(in)"].append(position.day)
      df["Day(out)"].append(position.day_exit)
      df["Price(in)"].append(position.price)
      df["Price(out)"].append(position.price_exit)
      df["Amount"].append(position.size)
      df["Return"].append((position.price_exit-position.price)/position.price*100)
    df = pd.DataFrame(df)
    return df

  def buy_operation(self, price, size):
    cash = self.account.data["Total"][0]
    amount_to_buy = np.floor(size * cash / price *100)/100
    self.account.buy_asset(tikr=self.tikr,
                           amount=amount_to_buy,
                           price_buy=price,
                           fee=self.fee,
                           tax=self.tax,
                           slippage=self.slippage,
                           leverage=self.leverage)

  def sell_operation(self, price, size, index):
    if size != "ALL":
      amount_to_sell = self.account.data["Amount"][index]*size
    else:
      amount_to_sell = size
      self.account.sell_asset(tikr=self.tikr,
                              amount=amount_to_sell,
                              price_sell=price,
                              fee=self.fee,
                              tax=self.tax,
                              slippage=self.slippage)

# BLOCK: VBO OHLC Multi
class VolBrkOut_ohlc_multi(Strategy):
  def __init__(self,
               df,
               account, logger, analyzer,
               fee, tax, slippage,
               leverage, losscut,
               does_save,
               tikr,
               K=0.5):
    super().__init__(df=df,
                     account=account, logger=logger, analyzer=analyzer,
                     fee=fee, tax=tax, slippage=slippage,
                     leverage=leverage, losscut=losscut,
                     does_save=does_save, tikr=tikr)
    self.K = K

  def check_buy_sign(self, high_y, low_y, high_t, open_t, K):
    price_width = high_y - low_y
    target_price = open_t + K*price_width
    buy_sign = 1 if high_t > target_price else 0
    return target_price, buy_sign

  def get_volume_money(self, df, day, days):
    date_list = [value[:10] for value in list(df["Date"])]

    today_ind = date_list.index(day)
    volume = []
    money_volume = []

    for ind in range(today_ind-days, today_ind):
      volume.append(df["Volume"][ind])
      money_volume.append(df["Close"][ind]*df["Volume"][ind])

    return volume, money_volume

  def get_price_multi(self, df, day):
    date_list = [value[:10] for value in list(df["Date"])]

    today_ind = date_list.index(day)
    open_y = df["Open"][today_ind-1]
    high_y = df["High"][today_ind - 1]
    low_y = df["Low"][today_ind - 1]
    close_y = df["Close"][today_ind - 1]

    open_t = df["Open"][today_ind]
    high_t = df["High"][today_ind]
    low_t = df["Low"][today_ind]
    close_t = df["Close"][today_ind]

    return open_y, high_y, low_y, close_y, open_t, high_t, low_t, close_t

  def run(self):
    is_end_of_data = False

    # Set date
    tikr_index = 0
    for tikr in self.df:
      if tikr_index != 0:
        date_list = pd.concat([date_list, self.df[tikr]["Date"]]).drop_duplicates().reset_index(drop=True)
      else:
        date_list = self.df[tikr]["Date"]
      tikr_index += 1

    date_list = pd.to_datetime(date_list)
    date_list = list(date_list.sort_values())
    date_list = [str(value.date()) for value in date_list]

    day_index = 0
    buy_sign = 0

    while not is_end_of_data:
      day_index += 1

      if day_index > len(date_list) - 1:
        is_end_of_data = True

      else:
        # Get the trading target
        today = date_list[day_index]
        print(today)
        print(sum(self.account.data["Total"]))

        # List up codes to trade
        tikr_list = []
        for tikr in self.df:
          day_init = self.df[tikr]["Date"][0]
          if (datetime(year=int(day_init[:4]),month=int(day_init[5:7]),day=int(day_init[8:10]))
            <datetime(year=int(today[:4]),month=int(today[5:7]),day=int(today[8:]))):
            tikr_list.append(tikr)

        # Get the best codes to trade, with the biggest money volume traded
        if day_index < 20:
          (open_y, high_y, low_y, close_y,
           open_t, high_t, low_t, close_t) = self.get_price_multi(self.df[tikr_list[0]], today)
          tikr_new = tikr_list[0]
        else:
          volume_list = []
          money_volume_list = []

          # Get the money volume
          for tikr in tikr_list:
            try:
              volume, money_volume = self.get_volume_money(self.df[tikr], today, 20)
              volume_list.append(np.median(volume))
              money_volume_list.append(np.median(money_volume))
            except:
              pass

          # Get the prices of the codes to trade
          tikr_index = money_volume_list.index(max(money_volume_list))
          tikr_new = tikr_list[tikr_index]
          try:
            (open_y, high_y, low_y, close_y,
             open_t, high_t, low_t, close_t) = self.get_price_multi(self.df[tikr_new], today)
          except:
            for tikr_index in range(0, len(tikr_list)):
              date_list = [value[:10] for value in list(self.df[tikr_list[tikr_index]]["Date"])]

              if today in date_list:
                tikr_new = tikr_list[tikr_index]
                (open_y, high_y, low_y, close_y,
                 open_t, high_t, low_t, close_t) = self.get_price_multi(self.df[tikr_new], today)

        # BLOCK: Sell operation
        if buy_sign:
          if tikr_new == tikr_old:
            buy_sign = self.sell_operation(open_t=open_t)
          else:
            (open_y, high_y, low_y, close_y,
             open_t, high_t, low_t, close_t) = self.get_price_multi(self.df[tikr_old], today)
            buy_sign = self.sell_operation(open_t=open_t)

        # BLOCK: Buy operation
        (open_y, high_y, low_y, close_y,
         open_t, high_t, low_t, close_t) = self.get_price_multi(self.df[tikr_new], today)

        noise = (close_y-open_y)/(high_y-low_y)

        if noise>0. or True:
          buy_sign  = self.buy_operation(high_y=high_y, low_y=low_y, high_t=high_t, open_t=open_t)

        # BLOCK: If the max volume code did not buy
        if buy_sign != 1 and day_index>=20:
          money_volume_list, tikr_index_list = zip(*sorted(zip(money_volume_list, list(range(len(money_volume_list)))), reverse=True))
          count = 0
          for tikr_index2 in tikr_index_list:
            count += 1
            if buy_sign != 1 and count < 4:
              tikr_new = tikr_list[tikr_index2]
              try:
                (open_y, high_y, low_y, close_y,
                 open_t, high_t, low_t, close_t) = self.get_price_multi(self.df[tikr_new], today)

                noise = (close_y - open_y) / (high_y - low_y)

                if noise > 0. or True:
                  buy_sign = self.buy_operation(high_y=high_y, low_y=low_y, high_t=high_t, open_t=open_t)
              except:
                pass

        # BLOCK: Logging the trading data
        self.logging_data(today=today,
                          open=open_t, close=close_t, high=high_t, low=low_t,
                          target_price=0, normal_factor=1,
                          buy_sign=buy_sign, tag=0)
        tikr_old = tikr_new
        print(tikr_new)

    self.noise = noise
    self.account.sell_asset(tikr=self.tikr,
                            amount="ALL",
                            price_sell=close_t,
                            fee=self.fee,
                            tax=self.tax,
                            slippage=self.slippage)
    # self.logger.print_in_dataframe()

    self.logger.save_data(filename=f"Backtest_Result_{self.tikr}_Vol_Brk_Out_K={self.K}.csv")
    self.analyzer.filename = f"Backtest_Result_{self.tikr}_Vol_Brk_Out_K={self.K}.csv"
    self.analyzer.report()
    if self.does_save:
      self.analyzer.save_report()

  def sell_operation(self, open_t):

    self.account.sell_asset(tikr=self.tikr,
                            amount="ALL",
                            price_sell=open_t,
                            fee=self.fee,
                            tax=self.tax,
                            slippage=self.slippage)

    return 0

  def buy_operation(self,
                    high_y, low_y,
                    high_t, open_t):

    target_price, buy_sign = self.check_buy_sign(high_y=high_y, low_y=low_y,
                                                 high_t=high_t, open_t=open_t,
                                                 K=self.K)

    if buy_sign:
      # print(f"Buy sign occurs at {day_index}")
      cash = self.account.data["Total"][0]
      size_to_buy = 1
      amount_to_buy = np.floor(size_to_buy * cash / target_price * 100)/100

      if amount_to_buy > 1 or True:
        self.account.buy_asset(tikr=self.tikr,
                               amount=amount_to_buy,
                               price_buy=target_price,
                               fee=self.fee,
                               tax=self.tax,
                               slippage=self.slippage,
                               leverage=self.leverage)
    return buy_sign

# BLOCK: Position class
class Position:
  def __init__(self, number, day, price, size, high, losscut, account):
    self.number = number
    self.day = day
    self.price = price
    self.size = size
    self.high = high
    self.losscut = losscut
    self.account = account
    self.price_exit = 0
    self.day_exit = 0

  def sell(self, price):
    self.account.sell_asset(tikr=self.tikr,
                            amount=self.size,
                            price_sell=price,
                            fee=self.fee,
                            tax=self.tax,
                            slippage=self.slippage)