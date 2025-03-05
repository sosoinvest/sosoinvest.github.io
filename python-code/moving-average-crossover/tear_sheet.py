import pandas as pd
import numpy as np

def tear_sheet1(data):
  trading_period = len(data)/252
  print(f"Trading Period: {trading_period:1f} years")

  buy_and_hold = data["Close"].iloc[-1].values[0]/data["Close"].iloc[0].values[0]-1
  final_cum_return = data["Cumulative_Return"].iloc[-1] - 1
  print(f"Final cumulative return of the strategy:"
        f"{100*final_cum_return:.2f}%, "
        f"Buy&Hold:{100*buy_and_hold:.2f}%")

  CAGR_strategy = (data["Cumulative_Return"].iloc[-1])**(1/trading_period)-1
  CAGR_benchmark = (buy_and_hold)**(1/trading_period)-1
  print(f"Strategy CAGR:{100*CAGR_strategy:.2f}, "
        f"Benchmark CAGR:{100*CAGR_benchmark:.2f}")

  risk_free_rate = 0.3*0.01
  strategy_daily_return = data["Cumulative_Return"].pct_change().fillna(0)
  mean_return = strategy_daily_return.mean()*252
  std_return = strategy_daily_return.std()*np.sqrt(252)
  sharpe_ratio = (mean_return-risk_free_rate)/std_return
  print(f"Sharpe Ratio:{sharpe_ratio:.2f}")

  data["Cumulative_Max"] = data["Cumulative_Return"].cummax()
  data["Drawdown"] = data["Cumulative_Return"]/data["Cumulative_Max"]-1
  max_drawdown = data["Drawdown"].min()
  cumulative_returns = (1+data["Close"].pct_change()).cumprod()
  running_max = cumulative_returns.cummax()
  drawdown = cumulative_returns/running_max-1
  mdd_benchmark = drawdown.min().values[0]
  print(f"Strategy MDD:{100*max_drawdown:.2f}%, "
        f"Benchmark MDD:{100*mdd_benchmark:.2f}%")

  buy_signals = data[data["Signal"] == 1].index
  sell_signals = data[data["Signal"] == -1].index
  returns = []
  holding_periods = []
  for buy_date in buy_signals:
    sell_dates = sell_signals[sell_signals>buy_date]
    if not sell_dates.empty:
      sell_date = sell_dates[0]
      buy_price = data.loc[buy_date, "Close"].values[0]
      sell_price = data.loc[sell_date, "Close"].values[0]
      return_pct = sell_price/buy_price-1
      returns.append(return_pct)
      holding_period = np.busday_count(buy_date.date(), sell_date.date())
      holding_periods.append(holding_period)

  profitable_trades = len([r for r in returns if r>0])
  loss_trades = len([r for r in returns if r <=0])
  total_trades = len(returns)
  win_rate = profitable_trades/total_trades if total_trades>0 else 0
  print(f"Number of Profitable Trades:{profitable_trades}, "
        f"Number of Loss Trades:{loss_trades}, Wind Rate:{100*win_rate:.2f}%")

  if holding_periods:
    average_holding_period = np.mean(holding_periods)
  else:
    average_holding_period = 0
  print(f"Avergage Holding Period:{average_holding_period:.1f}days")

  if profitable_trades>0:
    average_profit = np.mean([r for r in returns if r>0])
  else:
    average_profit = 0

  if loss_trades>0:
    average_loss = np.mean([r for r in returns if r<=0])
  else:
    average_loss = 0
  print(f"Avg ROR/trade in profitable trades:{average_profit:.3f}%,"
        f"Avg ROR/trade in loss trades:{average_loss:.3f}%")

  if average_loss!=0:
    profit_loss_ratio = average_profit/abs(average_loss)
  else:
    profit_loss_ratio = np.inf

  print(f"Profit/Loss Ratio:{profit_loss_ratio:.2f}")


