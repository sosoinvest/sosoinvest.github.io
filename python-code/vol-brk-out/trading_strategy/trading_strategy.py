#BLOCK: Import modules
import numpy as np
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

class VolBrkOut(Strategy):
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
      mean_price = 0

      if day_index > len(self.df) - 1:
        is_end_of_data = True

      else:
        today = self.df["Date"][day_index][0:10]

        (open_y, close_y, high_y, low_y) = self.get_price(ind=day_index - 1, normal_factor=normal_factor)
        (open_t, close_t, high_t, low_t) = self.get_price(ind=day_index, normal_factor=normal_factor)

        if len(self.account.data["Ticker"]) > 1:
          index = self.account.data["Ticker"].index(self.tikr)
          self.account.update_price(index, close_t)
        else:
          index = 1

        # BLOCK: Sell operation
        if buy_sign:
          buy_sign, tag = self.sell_operation(index=index, day_index=day_index,
                                               open_t=open_t, close_t=close_t, high_t=high_t, low_t=low_t,
                                               high_y=high_y, low_y=low_y)
        else:
          buy_sign, tag  = self.buy_operation(day_index = day_index,
                                               high_y=high_y, low_y=low_y,
                                               high_t=high_t, open_t=open_t, close_t=close_t)
        if tag:
          mean_price = self.account.data["Price(bought)"][index]

        # BLOCK: Logging the trading data
        self.logging_data(today=today,
                          open=open_t, close=close_t, high=high_t, low=low_t,
                          target_price=mean_price, normal_factor=normal_factor,
                          buy_sign=buy_sign, tag=tag)

    self.account.sell_asset(tikr=self.tikr,
                            amount="ALL",
                            price_sell=self.df["Close"].iloc[-1]/normal_factor,
                            fee=self.fee,
                            tax=self.tax,
                            slippage=self.slippage)
    self.logger.print_in_dataframe()

    self.logger.save_data(filename=f"Backtest_Result_{self.tikr}_Vol_Brk_Out_K={self.K}.csv")
    self.analyzer.filename = f"Backtest_Result_{self.tikr}_Vol_Brk_Out_K={self.K}.csv"
    self.analyzer.report()
    if self.does_save:
      self.analyzer.save_report()

  def sell_operation(self,
                     index, day_index,
                     open_t, close_t, high_t, low_t,
                     high_y, low_y):
    mean_price = self.account.data["Price(bought)"][index]

    if open_t < mean_price:
      self.account.sell_asset(tikr=self.tikr,
                              amount="ALL",
                              price_sell=open_t,
                              fee=self.fee,
                              tax=self.tax,
                              slippage=self.slippage)

      buy_sign, tag = self.buy_operation(day_index=day_index,
                                          high_y=high_y, low_y=low_y,
                                          high_t=high_t, open_t=open_t, close_t=close_t)
      tag="SOLC"

    else:
      if low_t <= open_t * (1 - self.losscut):
        self.account.sell_asset(tikr=self.tikr,
                                amount="ALL",
                                price_sell=open_t*(1 - self.losscut),
                                fee=self.fee,
                                tax=self.tax,
                                slippage=self.slippage)
        buy_sign = 0
        tag="SLLC"

      elif open_t < close_t and close_t > high_t*(1 - self.losscut):
        buy_sign = 1
        tag = "HOLD"

      elif open_t < close_t <= high_t*(1 - self.losscut):
        self.account.sell_asset(tikr=self.tikr,
                                amount="ALL",
                                price_sell = 0.5*(high_t + open_t)*(1 - self.losscut),
                                fee=self.fee,
                                tax=self.tax,
                                slippage=self.slippage)
        buy_sign = 0
        tag="SH"

      elif close_t <= open_t:
        self.account.sell_asset(tikr=self.tikr,
                                amount="ALL",
                                price_sell=0.5 * (close_t + open_t) * (1 - self.losscut),
                                fee=self.fee,
                                tax=self.tax,
                                slippage=self.slippage)
        buy_sign = 0
        tag="SHC"

    return buy_sign, tag

  def buy_operation(self,
                    day_index,
                    high_y, low_y,
                    high_t, open_t, close_t):

    target_price_high, buy_sign = self.check_buy_sign(high_y=high_y, low_y=low_y,
                                                      high_t=high_t, open_t=open_t,
                                                      K=self.K)

    target_price_mid, buy_sign = self.check_buy_sign(high_y=high_y, low_y=low_y,
                                                      high_t=high_t, open_t=open_t,
                                                      K=self.K * 0.8)

    target_price_low, buy_sign = self.check_buy_sign(high_y=high_y, low_y=low_y,
                                                      high_t=high_t, open_t=open_t,
                                                      K=self.K * 0.6)
    tag = None
    if buy_sign:
      print(f"Buy sign occurs at {day_index}")
      cash = self.account.data["Total"][0]
      size_to_buy = 1/3
      amount_to_buy = np.floor(size_to_buy * cash / target_price_low * 100)/100
      loss_cut_price = target_price_low * (1 - self.losscut)
      mean_price = target_price_low

      self.account.buy_asset(tikr=self.tikr,
                             amount=amount_to_buy,
                             price_buy=target_price_low,
                             fee=self.fee,
                             tax=self.tax,
                             slippage=self.slippage,
                             leverage=self.leverage)
      tag = "BL"

      if high_t > target_price_mid:
        size_to_buy = 1/3
        amount_to_buy = np.floor(size_to_buy * cash / target_price_mid*100)/100
        loss_cut_price = target_price_mid * (1 - self.losscut)
        mean_price = (target_price_low*1/3 + target_price_mid*1/3)/(2/3)

        self.account.buy_asset(tikr=self.tikr,
                               amount=amount_to_buy,
                               price_buy=target_price_mid,
                               fee=self.fee,
                               tax=self.tax,
                               slippage=self.slippage,
                               leverage=self.leverage)
        tag = "BM"

        if high_t >= target_price_high:
          size_to_buy = 1/3
          amount_to_buy = np.floor(size_to_buy * cash / target_price_high*100)/100
          loss_cut_price = target_price_high * (1 - self.losscut)
          mean_price = (target_price_low*1/3 + target_price_mid*1/3 + target_price_high*1/3)

          self.account.buy_asset(tikr=self.tikr,
                                 amount=amount_to_buy,
                                 price_buy=target_price_high,
                                 fee=self.fee,
                                 tax=self.tax,
                                 slippage=self.slippage,
                                 leverage=self.leverage)
          tag = "BH"

      if close_t < loss_cut_price:
        loss_cut_price = 0.5*(mean_price + high_t) * (1 - self.losscut)
        self.account.sell_asset(tikr=self.tikr,
                                amount="ALL",
                                price_sell=loss_cut_price,
                                fee=self.fee,
                                tax=self.tax,
                                slippage=self.slippage)
        buy_sign = 0
        tag = "BLC"

    return buy_sign, tag

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


  def get_target_price(self, high_y, low_y, open_t, K):
    price_width = high_y - low_y
    target_price = open_t + K*price_width
    return target_price

  def run(self):
    is_end_of_data = False
    day_index = 0
    buy_sign = 0
    positions = []

    while not is_end_of_data:
      day_index += 1

      if day_index > len(self.df) - 1:
        is_end_of_data = True

      else:
        today = self.df["Day"][day_index]
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

        continue_trading = True

        position_ind = 0
        for position in positions:
          if position.high < open_t:
            self.account.sell_asset(tikr=self.tikr,
                                    amount=position.size,
                                    price_sell=open_t,
                                    fee=self.fee,
                                    tax=self.tax,
                                    slippage=self.slippage)
            del positions[position_ind]
            buy_sign=0
          position_ind += 1

        high = intraday_price[0]

        intra_day_ind = -1
        for price in intraday_price:
          intra_day_ind += 1
          high = max(high, price)

          if pctrange > 0.1:
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
                new_position = Position(today,
                                        price,
                                        amount_to_buy,
                                        high,
                                        price*(1-self.losscut),
                                        self.account)
                positions.append(new_position)

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
              del positions[position_ind]

            elif position.day == today:
              position.high = max(position.high, high)
              position.losscut = position.high*(1-self.losscut)

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

    self.logger.save_data(filename=f"Backtest_Result_{self.tikr}_Vol_Brk_Out_K={self.K}.csv")
    self.analyzer.filename = f"Backtest_Result_{self.tikr}_Vol_Brk_Out_K={self.K}.csv"
    self.analyzer.report()

    if self.does_save:
      self.analyzer.save_report()

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

class Position:
  def __init__(self, day, price, size, high, losscut, account):
    self.day = day
    self.price = price
    self.size = size
    self.high = high
    self.losscut = losscut
    self.account = account

  def sell(self, price):
    self.account.sell_asset(tikr=self.tikr,
                            amount=self.size,
                            price_sell=price,
                            fee=self.fee,
                            tax=self.tax,
                            slippage=self.slippage)