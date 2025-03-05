class Position:
  def __init__(self, tikr, day_open, price_open, price_close, quantity, losscut, account):
    self.tikr = tikr
    self.day_open= day_open
    self.day_close = "0"
    self.price_open = price_open
    self.price_close = 0
    self.quantity = quantity
    self.losscut = losscut
    self.account = account
    self.status = "Open"

  def close_position(self, day_close, price_close, fee, tax, slippage):
    self.day_close = day_close
    self.price_close = price_close
    self.status = "Close"
    self.account.sell_asset(tikr=self.tikr,
                            amount=self.quantity,
                            price_sell=price_close,
                            fee=fee,
                            tax=tax,
                            slippage=slippage)