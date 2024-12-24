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
    self.intra_day_generator = 0

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

  def get_intra_day_data(self, filename):
    gen = intraday_generator.IntraDayPreprocessor(filename = filename)
    gen.normalize()
    gen.range_change()
    self.intra_day_generator = gen

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
               file_for_intra_day_patterns,
               K=0.5):
    super().__init__(df=df,
                     account=account, logger=logger, analyzer=analyzer,
                     fee=fee, tax=tax, slippage=slippage,
                     leverage=leverage, losscut=losscut,
                     does_save=does_save, tikr=tikr)
    self.K = K
    self.get_intra_day_data(file_for_intra_day_patterns)

  def get_target_price(self, high_y, low_y, open_t, K):
    price_width = high_y - low_y
    target_price = open_t + K*price_width
    return target_price

  def run(self):
    is_end_of_data = False
    day_index = 0
    normal_factor = 1
    have_position = False
    buy_sign = 0

    while not is_end_of_data:
      day_index += 1

      if day_index > len(self.df) - 1:
        is_end_of_data = True

      else:
        today = self.df["Date"][day_index][0:10]
        print(today)
        print(have_position)
        print(sum(self.account.data["Total"]))

        (open_y, high_y, low_y, close_y) = self.get_price(ind=day_index-1, normal_factor=normal_factor)

        (open_t, high_t, low_t, close_t) = self.get_price(ind=day_index, normal_factor=normal_factor)

        if len(self.account.data["Ticker"]) > 1:
          index = self.account.data["Ticker"].index(self.tikr)
          self.account.update_price(index, open_t)
        else:
          index = 1

        target_price = self.get_target_price(high_y, low_y, open_t, self.K)

        intra_day_price = self.intra_day_generator.generate_intraday_data(open_t, high_t, low_t, close_t, n=3)

        try:
          loss_cut_price = max(self.account.data["Price(bought)"][index], open_t)
        except:
          loss_cut_price = open_t

        continue_trading = True

        intra_day_ind = -1

        for price in intra_day_price:
          intra_day_ind += 1

          if np.mod(intra_day_ind, 100) == 0:
            plt.plot(intra_day_price)
            try:
              plt.axhline(y=self.account.data["Price(bought"][index], color="blue", label="meanprice")
            except:
              pass
            plt.axhline(y=loss_cut_price*(1-self.losscut), color="red", label="losscut")
            plt.axhline(y=target_price, color="black", label="target")
            plt.plot(intra_day_ind, price, marker="o")
            plt.ylim((low_t, high_t))
            plt.legend()
            plt.show()

          if continue_trading:
            if have_position:
              loss_cut_price = max(loss_cut_price, price)
              loss_cut = loss_cut_price * (1-self.losscut)
              if price<loss_cut:
                print("sell operation occurs")
                print(f"loss cut price: {loss_cut} and current price: {price}")

                self.sell_operation(price=price, size="ALL", index=index)
                self.account.data["Price(bought)"][index] = 0
                buy_sign = 0
                have_position = False
                continue_trading = False

            else:
              if buy_sign == 0:
                if price > target_price:
                  print("Buy operation occurs")
                  self.buy_operation(price=price, size=1)
                  buy_sign = 1
              else:
                loss_cut_price = max(self.account.data["Price(bought)"][index], price)
                loss_cut = loss_cut_price * (1-self.losscut)
                if price < loss_cut:
                  print("Loss cut occurs")
                  self.sell_operation(price=price, size="ALL", index=index)
                  self.account.data["Price(bought)"][index] = 0
                  buy_sign = 0
                  have_position = False
                  continue_trading = False
          if buy_sign:
            have_position = True

      # BLOCK: Logging the trading data
      self.logging_data(today=today,
                        open=open_t, close=close_t, high=high_t, low=low_t,
                        target_price=target_price, normal_factor=normal_factor,
                        buy_sign=buy_sign, tag="none")

    self.account.sell_asset(tikr=self.tikr,
                            amount="ALL",
                            price_sell=self.df["Close"].iloc[-1] / normal_factor,
                            fee=self.fee,
                            tax=self.tax,
                            slippage=self.slippage)
    self.logger.print_in_dataframe()

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

class VolBrkOut_intraday2(Strategy):
  def __init__(self, df,
               account, logger, analyzer,
               fee, tax, slippage,
               leverage, losscut,
               does_save,
               tikr,
               file_for_intra_day_patterns,
               K=0.5):
    super().__init__(df=df,
                     account=account, logger=logger, analyzer=analyzer,
                     fee=fee, tax=tax, slippage=slippage,
                     leverage=leverage, losscut=losscut,
                     does_save=does_save, tikr=tikr)
    self.K = K
    self.get_intra_day_data(file_for_intra_day_patterns)

  def get_target_price(self, high_y, low_y, open_t, K):
    price_width = high_y - low_y
    target_price = open_t + K*price_width
    return target_price

  def run(self):
    is_end_of_data = False
    day_index = 0
    normal_factor = 1
    have_position = 0


    while not is_end_of_data:
      # input("")
      day_index += 1

      if day_index > len(self.df) - 1:
        is_end_of_data = True

      else:
        today = self.df["Date"][day_index][0:10]
        print(today)
        print(sum(self.account.data["Total"]))
        if have_position:
          print(f"Open: {np.round(position.price_open,3)} / "
                f"Close: {np.round(position.price_close,3)} / "
                f"High: {np.round(position.price_high,3)}")
        print("\n")

        (open_y, high_y, low_y, close_y) = self.get_price(ind=day_index-1, normal_factor=normal_factor)
        (open_t, high_t, low_t, close_t) = self.get_price(ind=day_index, normal_factor=normal_factor)

        if len(self.account.data["Ticker"]) > 1:
          self.account.update_price(1, open_t)

        target_price = self.get_target_price(high_y, low_y, open_t, self.K)

        intra_day_price = self.intra_day_generator.generate_intraday_data(open_t, high_t, low_t, close_t, n=3)
        intra_day_ind = -1

        cash = self.account.data["Total"][0]
        high_ = 0
        trading_continue = True

        if have_position:
          if open_t < position.price_close:
            position.close_pos(open_t)
            have_position = 0
            print(f"The return is:{np.round(100 * (price - position.price_open) / position.price_open)}")

        for price in intra_day_price:

          # if np.mod(intra_day_ind, 100) == 0:
          #   plt.plot(intra_day_price)
          #   plt.axhline(y=target_price, color="black", label="target")
          #   try:
          #     # plt.axhline(y=self.account.data["Price(bought"][index], color="blue", label="meanprice")
          #     plt.axhline(y=position.price_close, color="red", label="losscut")
          #   except:
          #     pass
          #   plt.plot(intra_day_ind, price, marker="o")
          #   plt.ylim((low_t, high_t))
          #   plt.legend()
            # plt.show()


          intra_day_ind += 1

          # BLOCK: Update the high price
          high_ = max(high_, price)
          if trading_continue:
            if have_position:
              position.price_high = max(position.price_high, high_)
              position.price_close = position.price_open*(1-self.losscut) + 0.9*(position.price_high - position.price_open)
              # print(position.price_open)
              # print(position.price_high)
              # print(f"Updated: {position.price_close}")
              # if position.price_close*(1-0.5*0.01) < price < position.price_close*(1+0.5*0.01):
              if price < position.price_close * (1):
                # print(f"Position close(loss cut) at {np.round(price,2)} / (close target: {np.round(position.price_close,2)}")
                # print(f"Slippage: {np.round(100*(price-position.price_close) / position.price_close,2)}%")
                print(f"The return is:{np.round(100*(price-position.price_open)/position.price_open)}")
                position.close_pos(price)
                have_position = 0
                trading_continue = False
            else:
              # BLOCK: Open position
              if target_price*(1-0.5*0.01) < price < target_price*(1+0.5*0.01) and cash > 0:
                # print(f"Position open at {np.round(price,2)} / (target: {np.round(target_price,2)})")
                # print(f"The close price is: {np.round(price*(1-self.losscut),2)}")
                # print(f"Slippage: {np.round(100*(target_price-price) / target_price,2)}%")
                high_ = price
                position_size = np.floor(cash / price * 100) / 100
                position=Position(tikr=self.tikr,
                                  price_open=price, price_high=price,
                                  amount=position_size, price_close=price*(1-self.losscut),
                                  account=self.account, fee=self.fee, tax=self.tax, slippage=0)
                position.open_pos(price)
                position.price_high = high_
                cash = self.account.data["Total"][0]
                have_position = 1

      # BLOCK: Logging the trading data
      self.logging_data(today=today,
                        open=open_t, close=close_t, high=high_t, low=low_t,
                        target_price=target_price, normal_factor=normal_factor,
                        buy_sign=have_position, tag="none")

    self.account.sell_asset(tikr=self.tikr,
                            amount="ALL",
                            price_sell=self.df["Close"].iloc[-1] / normal_factor,
                            fee=self.fee,
                            tax=self.tax,
                            slippage=self.slippage)
    self.logger.print_in_dataframe()

    self.logger.save_data(filename=f"Backtest_Result_{self.tikr}_Vol_Brk_Out_K={self.K}.csv")
    self.analyzer.filename = f"Backtest_Result_{self.tikr}_Vol_Brk_Out_K={self.K}.csv"
    self.analyzer.report()
    if self.does_save:
      self.analyzer.save_report()


class Position:
  def __init__(self, tikr,
               price_open, price_high, price_close,
               amount,
               account, fee, tax, slippage):
    self.account=account
    self.fee=fee
    self.tax=tax
    self.slippage=slippage
    self.tikr = tikr
    self.price_open = price_open
    self.price_close = price_close
    self.price_high = price_high
    self.amount = amount

  def open_pos(self, price):
    self.account.buy_asset(tikr=self.tikr,
                           amount=self.amount,
                           price_buy=price,
                           fee=self.fee,
                           tax=self.tax,
                           slippage=self.slippage,
                           leverage=1)

  def close_pos(self, price):
    self.account.sell_asset(tikr=self.tikr,
                           amount="ALL",
                           price_sell=price,
                           fee=self.fee,
                           tax=self.tax,
                           slippage=self.slippage)

  def monitor(self):
    data = {
      "TIKR": self.tikr,
      "Amount": self.amount,
      "Price (open)": self.price_open,
      "Price (close)": self.price_close,
      "Price (high)": self.price_high,
    }

    print(data)
    print("\n")
