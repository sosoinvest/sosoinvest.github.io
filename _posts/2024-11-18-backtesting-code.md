---
layout: single
title:  "퀀트 백테스팅 파이썬 코드"
description: 파이썬으로 작성한 퀀트 투자용 백테스팅 코드
categories: 투자
tag: [주식,퀀트,백테스트,파이썬]
toc: true
author_profile: false
header:
 teaser: /images/2024-11-18-backtesting-code/code-structure.webp
 og_image: /images/2024-11-18-backtesting-code/code-structure.webp
# sidebar:
#     nav: "docs"
# search: true
---

# 코드의 구조
<p align="center">   
    <img src="/images/2024-11-18-backtesting-code/code-structure.webp" alt="코드의 구조">
    <br>
   <span style="font-style: italic; color: #FFFFFF;">Fig. 1 백테스팅 코드의 구조</span>
</p>

- [래리 윌리엄스의 변동성 돌파전략 (파이썬 코드 있음)](/투자/volatility-break-out-strategy/)
- [절대로 지지않는 롱 전략](/투자/never-losing-long-strategy)
- [곱버스를 우상향시키는 방법](/투자/upward-sloping-inverse-double)

# 백테스팅 코드
```python
# BLOCK: Import modules
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from tabulate import tabulate
import math

class Account:
    """
    The account class manage the assets.
    It can buy and sell assets and monitor current status of each asset.
    """
    def __init__(self):
        """
        data: [Dictionary], including lists of ticker, amount,
                price(bought), price(now), total value, revenue, and return
        """
        self.data = {
            "Ticker": ["Cash"],
            "Amount": [0],
            "Price(bought)": [np.nan],
            "Price(now)": [np.nan],
            "Total": [0],
            "Revenue": [np.nan],
            "Return": [np.nan],
        }

    def monitor(self):
        """
        It monitors current status of the account.
        :return:
        """
        print("The account is updated.")
        print(tabulate(self.data, headers="keys", tablefmt="pretty"))
        print("\n")

    def deposit_cash(self, cash_amount):
        """
        It deposits cash in the account.
        :param cash_amount: The amount of the cash to deposit in the account.
        :return:
        """
        self.data["Amount"][0] += np.round(cash_amount, 2)
        self.data["Total"][0] = self.data["Amount"][0]
        print(f"{cash_amount} cash is deposited. Now the cash is {self.data["Amount"][0]}.\n")

    def withdraw_cash(self, cash_amount):
        """
        It withdraws cash from the account.
        :param cash_amount: The amount of the cash to withdraw from the account.
        :return:
        """
        self.data["Amount"][0] -= np.round(cash_amount, 2)
        self.data["Total"][0] = self.data["Amount"][0]
        print(f"{cash_amount} cash is withdrawn. Now the cash is {self.data["Amount"][0]}.\n")

    def buy_asset(self, tikr, amount, price_buy):
        """
        Buy asset in the account.
        :param tikr: Ticker of the asset
        :param amount: Amount to buy
        :param price_buy: Price to buy
        :return:
        """
        # BLOCK: Call lists of the data
        tikr_list = self.data["Ticker"]
        amount_list = self.data["Amount"]
        price_buy_list = self.data["Price(bought)"]
        price_now_list = self.data["Price(now)"]
        revenue_list = self.data["Revenue"]
        total_list = self.data["Total"]
        return_list = self.data["Return"]
        cash = amount_list[0]

        # BLOCK: Buy an asset in the account
        if tikr in tikr_list:
            # Buy asset which is in the account
            index = tikr_list.index(tikr)

            # Check if the cash is enough
            if (amount*price_buy) < cash:
                # Save the old data
                amount_old = amount_list[index]
                price_buy_old = price_buy_list[index]

                # Compute the new data
                amount_new = amount_old + amount
                price_buy_new = ((amount_old * price_buy_old + amount * price_buy)
                                 / amount_new)
                revenue_new = (price_buy - price_buy_new)*amount_new
                total_new = amount_new*price_buy_new
                return_new = f"{np.round((price_buy - price_buy_new)
                                         /price_buy_new * 100, 2)}%"

                # Update the account
                self.update(index, tikr, amount_new,
                            price_buy_new, price_buy, revenue_new,
                            total_new, return_new)

                self.withdraw_cash(amount * price_buy)
            else:
                print("Not enough cash. cannot buy the asset.\n")

        else:
            # Buy new asset
            self.withdraw_cash(amount * price_buy)

            # Buy new asset
            total_new = amount * price_buy
            return_new = f"{0.00}%"

            # Update the data dictionary
            self.update(0, tikr, amount,
                        price_buy, price_buy, 0,
                        total_new, return_new)

        print(f"You bought. \nTIKR: {tikr} / Amount: {amount} / Price: {price_buy} ")

        # Monitor current account
        # self.monitor()

    def update(self, index, tikr, amount, price_buy, price_now, revenue, total, return_data):
        """
        Update the current status of the account.
        :param index: Index of the asset in the account.
        :param tikr: Ticker of the asset to update
        :param amount: Amount of the asset to update
        :param price_buy: Price buy of the asset to update
        :param price_now: Price now of the asset to update
        :param revenue: Revenue of the asset to update
        :param total: Total value of the asset to update
        :param return_data: Return of the asset to update
        :return:
        """
        if index: # Update with the index of the asset which is already in the account
            self.data["Amount"][index] = amount
            self.data["Price(bought)"][index] = price_buy
            self.data["Price(now)"][index] = price_now
            self.data["Revenue"][index] = revenue
            self.data["Total"][index] = total
            self.data["Return"][index] = return_data
        else: # Update new asset
            self.data["Ticker"].append(tikr)
            self.data["Amount"].append(amount)
            self.data["Price(bought)"].append(price_buy)
            self.data["Price(now)"].append(price_now)
            self.data["Revenue"].append(revenue)
            self.data["Total"].append(total)
            self.data["Return"].append(return_data)

    def sell_asset(self, tikr, amount, price_sell):
        """
        Sell asset from the account.
        :param tikr: Ticker of the asset to sell.
        :param amount: Amount to sell
        :param price_sell: Price to sell
        :return:
        """
        tikr_list = self.data["Ticker"]
        amount_list = self.data["Amount"]
        price_buy_list = self.data["Price(bought)"]
        price_now_list = self.data["Price(now)"]
        revenue_list = self.data["Revenue"]
        total_list = self.data["Total"]
        return_list = self.data["Return"]

        if tikr in list(tikr_list):
            index = tikr_list.index(tikr)

            if amount in ["ALL", "All"]:
                amount = amount_list[index]

            if amount > amount_list[index]:
                print(f"Cannot sell more than in the account\n")
            else:
                # Add to cash
                amount_list[0] += price_sell * amount
                total_list[0] = amount_list[0]

                # Compute the new data
                amount_new = amount_list[index] - amount
                revenue_new = (price_sell - price_buy_list[index])*amount_new
                total_new = amount_new * price_sell
                return_new = f"{np.round((price_sell - price_buy_list[index])
                                         /price_buy_list[index] * 100, 2)}%"

                # Save into the data dictionary
                self.update(index, tikr, amount_new,
                            price_sell, price_sell, revenue_new,
                            total_new, return_new)
                print(f"You sold. \nTIKR: {tikr} / Amount: {amount} / Price: {price_sell} ")
        else:
            print("Cannot sell what is not in the account\n")

        # self.monitor()


class Trader:
    """
    Trader manages trading.
    It checks the sign for buying and selling.
    """
    def __init__(self, K):
        """
        buy_sign: [0,1] 1 if the buying sign occurs, 0 if there is no sign.
        K: Parameter for the volatility break-out strategy
        target_price: Price for making the buying sign, i.e., Open+(High_y-Low_y)*K
        :param K:
        """
        self.buy_sign = 0
        self.K = K
        self.target_price = 0

    def check_buy_sign(self, price_now, price_open, price_width):
        """
        Check if buy sign occurs or not.
        :param price_now: Current price
        :param price_open: Open price
        :param price_width: Price width (High-Low) of yesterday
        :return:
        """
        target_price = price_open + self.K*price_width

        if price_now > target_price:
            self.buy_sign = 1
            return target_price
        else:
            self.buy_sign = 0
            return 0

    def check_sell_sign(self):
        """
        Check if sell sign occurs or not.
        :return:
        """
        if self.buy_sign == 1:
            return 1
        else:
            return 0


class Logger:
    """
    Logger is logging the trading data.
    """
    def __init__(self):
        """
        data_dict: [Dictoinary], trading data storagy
        """
        self.data_dict = {}

    def log_data(self, key, data):
        """
        Log data
        :param key: Key to store in the dictionary
        :param data: Data matching with the key
        :return:
        """
        if key in self.data_dict.keys():
            self.data_dict[key].append(data)
        else:
            self.data_dict[key] = [data]

    def save_data(self, filename):
        """
        Convert data into dataframe and save the dataframe as a csv file.
        :param filename: Name of the file to save.
        :return:
        """
        df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in self.data_dict.items()]))
        df.to_csv(filename)

    def print_in_dataframe(self):
        """
        Convert data into dataframe and print it.
        :return:
        """
        df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in self.data_dict.items()]))
        print(df)


class Analyzer:
    """
    Analyze the trading data.
    It computes evaluating value of the trading.
    """
    def __init__(self, filename):
        """
        df: Dataframe loaded from the file
        daily_return: Daily return computed from the trading data
        analysis_result: [Dictionary] Storagy sacing the result of the analysis

        :param filename: Name of the trading data file to import
        """
        self.df = pd.read_csv(filename)
        self.daily_return, self.daily_return_bnh = self.compute_daily_return()
        self.analysis_result = {}
        self.filename = filename

    def save_report(self):
        """
        Save the analysis data as a text file.
        :return:
        """
        filename = self.filename.replace(".csv", ".txt")
        with open(filename, "w") as data_file:
            data_file.write(tabulate(self.analysis_result, headers="keys", tablefmt="pretty"))

    def compute_daily_return(self):
        """
        Compute daily return of the trading.
        It also computes the daily return of the buy and hold strategy.
        :return:
        """
        daily_total = list(self.df["Total"])
        daily_bnh = list(self.df["Close"])
        return np.round(np.diff(daily_total)/daily_total[1:]*100, 2), np.round(np.diff(daily_bnh)/daily_bnh[1:]*100, 2)

    def report(self):
        """
        Report the analysis data.
        :return:
        """
        self.num_of_days()
        self.final_return()
        self.buy_and_hold_return()
        self.mdd()
        self.cagr()
        self.num_of_trades()
        self.num_wins()
        self.win_percent()
        self.sharp_ratio(case="Portfolio")
        self.sharp_ratio(case="Buy and hold")
        self.mean_return()

        print(tabulate(self.analysis_result, headers="keys", tablefmt="pretty"))
        print(self.analysis_result)

    def buy_and_hold_return(self):
        """
        Compute the final return of buy and hold strategy
        :return:
        """
        initial = self.df["Close"].iloc[0]
        terminal = self.df["Close"].iloc[-1]
        final_return = np.round((terminal - initial) / initial * 100, 2)
        self.analysis_result["Buy and hold return"] = [f"{final_return} %"]

    def final_return(self):
        """
        Compute the final return of trading strategy.
        :return:
        """
        initial = self.df["Total"].iloc[0]
        terminal = self.df["Total"].iloc[-1]
        final_return = np.round((terminal-initial)/initial*100, 2)
        self.analysis_result["Final return"] = [f"{final_return} %"]

    def mdd(self):
        """
        Compute MDD(Maximum Draw Down)
        :return:
        """
        max_run = 0
        mdd = 0
        for money in self.df["Total"]:
            max_run = max(money, max_run)
            mdd = min(mdd, (money-max_run)/max_run)
        mdd *= 100
        self.analysis_result["MDD"] = [f"{np.round(mdd, 2)} %"]

    def cagr(self):
        """
        Compute CAGR(Cumulative Annual Growth Rate)
        :return:
        """
        cagr = 1
        for daily_return in self.daily_return:
            cagr *= (daily_return * 0.01 + 1)
        cagr = cagr ** (1/len(self.daily_return)) - 1
        cagr = (1 + cagr) ** 252 - 1
        cagr = np.round(cagr*100, 2)
        self.analysis_result["CAGR"] = [f"{cagr} %"]

    def num_of_trades(self):
        """
        Compute the number of trades.
        :return:
        """
        self.analysis_result["# of trades"] = [int(sum(list(self.df["Buy sign"])))]

    def num_of_days(self):
        """
        Compute the number of days between the terminal and initial day of the trading.
        :return:
        """
        start_day = self.df["Day"].iloc[0]
        terminal_day = self.df["Day"].iloc[-1]
        date_format = "%Y-%m-%d"
        start_day = datetime.strptime(start_day, date_format)
        terminal_day = datetime.strptime(terminal_day, date_format)
        difference = terminal_day-start_day
        self.analysis_result["Days"] = [difference.days]

    def num_wins(self):
        """
        Compute the number of winning of the trading.
        :return:
        """
        daily_return = list(self.daily_return)
        count = sum(1 for x in daily_return if x > 0)
        self.analysis_result["# of wins"] = [count]

    def win_percent(self):
        """
        Compute the percent of winning of the trading.
        :return:
        """
        daily_return = list(self.daily_return)
        count = sum(1 for x in daily_return if x > 0)
        trades = int(sum(list(self.df["Buy sign"])))
        self.analysis_result["Winning %"] = [f"{np.round(count/trades*100, 2)} %"]

    def sharp_ratio(self, case):
        """
        Compute the sharp ratior of the trading
        :param case: Select the case between portfolio or buy and hold
        :return:
        """
        if case in ["Portfolio", "Buy and hold"]:
            key_name = "Sharp ratio(Portfolio)"
            if case == "Portfolio":
                # daily_returns = self.daily_return
                daily_returns = [x for x in self.daily_return if
                                isinstance(x, (int, float)) and not (isinstance(x, float) and math.isnan(x))]
                daily_returns = np.array(daily_returns)

            elif case == "Buy and hold":
                # daily_returns = self.daily_return
                daily_returns = [x for x in self.daily_return_bnh if
                                isinstance(x, (int, float)) and not (isinstance(x, float) and math.isnan(x))]
                daily_returns = np.array(daily_returns)
                key_name = "Sharp ratio(Buy and hold)"

            mean_return = 1
            for daily_return in daily_returns:
                mean_return *= (daily_return * 0.01 + 1)
            mean_return = mean_return ** (1 / len(daily_returns)) - 1
            mean_return = (1 + mean_return) ** 252 - 1

            daily_return = daily_returns*0.01
            std_return = np.std(daily_return)
            std_return = std_return * np.sqrt(252)

            sharp_ratio = np.round(mean_return/std_return, 2)
            self.analysis_result[key_name] = [sharp_ratio]
        else:
            print("No matching case for sharp ratio computation")

    def mean_return(self):
        """
        Compute the mean return for the case of win and lose.
        It also compute the RR(Reward-Risk) ratio
        :return:
        """
        daily_return = self.daily_return
        mean_return_win = np.round(daily_return[daily_return > 0].mean(), 2)
        mean_return_lose = np.round(daily_return[daily_return < 0].mean(), 2)
        self.analysis_result["Mean return win"] = [f"{mean_return_win}%"]
        self.analysis_result["Mean return lose"] = [f"{mean_return_lose}%"]
        self.analysis_result["RR ratio"] = [f"{np.round(mean_return_win/abs(mean_return_lose),2)}"]

``` 