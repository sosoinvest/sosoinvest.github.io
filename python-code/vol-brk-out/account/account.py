import numpy as np
from tabulate import tabulate


class Account:
  """
  The account_manager class manages the assets.
  It can buy and sell assets and monitors current status of each asset.
  """

  def __init__(self):
    """
    data: [Dictionary], including lists of ticker, amount,
            price(bought), price(now), total value, revenue, and return
    Ticker [str]
    Amount [float]
    Price(bought) [float]
    Price(now) [float]
    Total [float]
    Revenue [float]
    Return [str] in percent
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
    self.net_input = 0

  def monitor(self):
    """
    It monitors current status of the account_manager.
    :return:
    """
    print("The account_manager is updated.")
    print(tabulate(self.data, headers="keys", tablefmt="pretty"))
    print(f"The total value of the account is {sum(self.data["Total"])}")
    print("\n")

  def deposit_cash(self, cash_amount):
    """
    It deposits cash in the account manager.
    :param cash_amount: The amount of the cash to deposit in the account manager.
    :return:
    """
    self.data["Amount"][0] += np.round(cash_amount, 2)  # It rounds off the amount of cash upto 2nd digits.
    self.data["Total"][0] = self.data["Amount"][0]  # The total value of the cash equals to the amount of cash.
    self.net_input += cash_amount
    print(f"{cash_amount} cash is deposited. Now the cash is {self.data["Amount"][0]}.\n")

  def withdraw_cash(self, cash_amount):
    """
    It withdraws cash from the account_manager.
    :param cash_amount: The amount of the cash to withdraw from the account_manager.
    :return:
    """
    self.data["Amount"][0] -= np.round(cash_amount, 2)  # It rounds off the amount of cash upto 2nd digits.
    self.data["Total"][0] = self.data["Amount"][0]  # The total value of the cash equals to the amount of cash.
    self.net_input -= cash_amount
    # print(f"{cash_amount} cash is withdrawn. Now the cash is {self.data["Amount"][0]}.\n")

  def buy_asset(self, tikr, amount, price_buy, fee, tax, slippage, leverage):
    """
    Buy asset in the account_manager.
    :param tikr: Ticker of the asset
    :param amount: Amount to buy
    :param price_buy: Price to buy
    :param fee: Fee paid when buy
    :param tax: Tax paid when buy
    :param slippage: Slippage paid when buy
    :param leverage: Leverage applied when buy
    :return:
    """
    # BLOCK: Call lists of the data
    tikr_list = self.data["Ticker"]
    amount_list = self.data["Amount"]
    price_bought_list = self.data["Price(bought)"]
    price_now_list = self.data["Price(now)"]
    revenue_list = self.data["Revenue"]
    total_list = self.data["Total"]
    return_list = self.data["Return"]
    cash = amount_list[0]  # Total cash having now

    # BLOCK: Apply slippage
    price_buy = price_buy * (1 + slippage)

    # BLOCK: Apply leverage
    amount = amount * leverage
    # print(f"The amount is {amount} considering the leverage ratio of {leverage}.")

    # BLOCK: Buy an asset in the account manager already
    if tikr in tikr_list:
      # Buy asset which is in the account manager
      index = tikr_list.index(tikr)

      # Check if the cash is enough ***** Now, checking if the cash is enough is not done, it may be needed to be fixed in the future.
      # if (amount*price_buy) < cash:
      if True:
        # Save the old data
        amount_old = amount_list[index]
        price_bought_old = price_bought_list[index]

        # Computes the new data
        amount_new = amount_old + amount
        price_bought_new = ((amount_old * price_bought_old + amount * price_buy)
                            / amount_new)
        revenue_new = (price_buy - price_bought_new) * amount_new
        total_new = amount_new * price_bought_new
        return_new = f"{np.round((price_buy - price_bought_new) / price_bought_new * 100, 2)}%"

        # Updates the account manager
        self.update(index, tikr, amount_new,
                    price_bought_new, price_buy, revenue_new,
                    total_new, return_new)

        # Withdraws cash from the account
        self.withdraw_cash(amount * price_buy * (1 + fee))

      else:
        print("Not enough cash. cannot buy the asset.\n")

    else:
      # Buy new asset
      price_bought_new = price_buy
      total_new = amount * price_bought_new
      revenue_new = 0
      return_new = f"{0.00}%"

      # Update the data dictionary
      self.update(0, tikr, amount,
                  price_bought_new, price_bought_new, revenue_new,
                  total_new, return_new)

      # Withdraws cash from the account
      self.withdraw_cash(amount * price_bought_new * (1 + fee))

    # print(f"You bought. \nTIKR: {tikr} / Amount: {amount} / Price: {price_bought_new} ")

    # Monitor current account_manager
    # self.monitor()

  def sell_asset(self, tikr, amount, price_sell, fee, tax, slippage):
    """
    Sell asset from the account_manager.
    :param tikr: Ticker of the asset to sell.
    :param amount: Amount to sell
    :param price_sell: Price to sell
    :param fee: Fee paid when sells
    :param tax: Tax paid when sells
    :param slippage: Slippage paid when sells
    :return:
    """
    tikr_list = self.data["Ticker"]
    amount_list = self.data["Amount"]
    price_bought_list = self.data["Price(bought)"]
    price_now_list = self.data["Price(now)"]
    revenue_list = self.data["Revenue"]
    total_list = self.data["Total"]
    return_list = self.data["Return"]

    # BLOCK: Apply slippage
    price_sell = price_sell * (1 - slippage)

    if tikr in list(tikr_list):  # Check if tikr in the tikr_list
      index = tikr_list.index(tikr)
      # print(self.data)
      # print(index)
      # print(tikr_list)
      # print(price_bought_list)
      price_bought = price_bought_list[index]

      if amount in ["ALL", "All"]:  # If amount equals to all, sell all the assets in the account
        amount = amount_list[index]

      if amount > amount_list[index]:  # Check if the amount to sell is larger than amount having in the account
        print(f"Cannot sell more than in the account\n")

      else:
        # Add selling money to cash
        if price_bought < price_sell:  # If price_bought is smaller than price to sell, tax is charged.
          # The tax is charged to the total income of selling.
          # Note amount_list[0] equals to the cash.
          amount_list[0] += ((price_sell * amount) * (1 - fee)
                             - (price_sell - price_bought) * amount * tax)
        else:
          amount_list[0] += (price_sell * amount) * (1 - fee)
        total_list[0] = amount_list[0]

        # Computes the new data
        amount_new = amount_list[index] - amount
        revenue_new = (price_sell - price_bought) * amount_new
        total_new = amount_new * price_sell
        return_new = f"{np.round((price_sell - price_bought) / price_bought * 100, 2)}%"

        # Save into the data dictionary
        self.update(index, tikr, amount_new,
                    price_bought, price_sell, revenue_new,
                    total_new, return_new)
        # print(f"You sold. \nTIKR: {tikr} / Amount: {amount} / Price: {price_sell} ")
    else:
      print("Cannot sell what is not in the account_manager\n")

    # self.monitor()

  def update(self, index, tikr, amount, price_bought, price_now, revenue, total, return_data):
    """
    Updates the current status of the account_manager.
    :param index: Index of the asset in the account manager.
    :param tikr: Ticker of the asset to update
    :param amount: Amount of the asset to update
    :param price_bought: Price buy of the asset to update
    :param price_now: Price now of the asset to update
    :param revenue: Revenue of the asset to update
    :param total: Total value of the asset to update
    :param return_data: Return of the asset to update
    :return:
    """
    if index:  # Updates with the index of the asset which is already in the account manager
      self.data["Amount"][index] = amount
      self.data["Price(bought)"][index] = price_bought
      self.data["Price(now)"][index] = price_now
      self.data["Revenue"][index] = revenue
      self.data["Total"][index] = total
      self.data["Return"][index] = return_data
    else:
      self.data["Ticker"].append(tikr)
      self.data["Amount"].append(amount)
      self.data["Price(bought)"].append(price_bought)
      self.data["Price(now)"].append(price_now)
      self.data["Revenue"].append(revenue)
      self.data["Total"].append(total)
      self.data["Return"].append(return_data)

  def update_price(self, index, price):
    """
    Update only the price
    """
    price_bought = self.data["Price(bought)"][index]
    amount = self.data["Amount"][index]

    self.data["Price(now)"][index] = price
    self.data["Revenue"][index] = (price - price_bought) * amount
    self.data["Total"][index] = price * amount
    self.data["Return"][index] = f"{np.round((price - price_bought) / price_bought * 100, 2)}%"