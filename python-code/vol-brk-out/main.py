from matplotlib.pyplot import tight_layout
from backtester import tester100
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

K = 0.3
TIKR = "091160"

# # BLOCK: Intraday
# does_save = False
# my_tester = tester100.Backtester(filename=f"E:/intraday-data/{TIKR}.json",
#                                  tikr=TIKR,
#                                  does_save=does_save,
#                                  fee=0.07*0.01, tax=0.0, slippage=0.0*0.01, leverage=1,
#                                  losscut=5*0.01,
#                                  deposit_cash=10000,
#                                  strategy="VolBrkOut_intraday",
#                                  params={"K": K},
#                                  window=1)
# my_tester.run()

# BLOCK: VBO OHLC
# does_save = True
# my_tester = tester100.Backtester(filename=f"{TIKR}.csv", #f"E:/{TIKR}.csv",
#                                  tikr=TIKR,
#                                  does_save=does_save,
#                                  fee=0.0036396*0.01, tax=15.4*0.0, slippage=0.0*0.01, leverage=1,
#                                  losscut=5*0.01,
#                                  deposit_cash=10000,
#                                  strategy="VolBrkOut_ohlc",
#                                  params={"K": K},
#                                  window=1)
# my_tester.run()

# BLOCK: VBO Multi
does_save = False
# tikr_list = ["117460", "091160", "091180", "266360", "305720", "466920", "244580" ,"449450", "143860", "139260", "228790", "091170"]
tikr_list = ["117460", "091160", "091180", "266360", "305720", "466920", "244580" ,"449450", "143860", "228790"]
# tikr_list = ["005930", "005380", "012450", "207940", "329180", "373220"]

my_tester = tester100.Backtester(filename=f"",
                                 tikr=tikr_list,
                                 does_save=does_save,
                                 fee=0.0036396*0.01, tax=0.18*0.0, slippage=0.0*0.01, leverage=1,
                                 losscut=5*0.01,
                                 deposit_cash=10000,
                                 strategy="VolBrkOut_ohlc_multi",
                                 params={"K": K},
                                 window=1)
my_tester.run()

# BLOCK: Plot the result
# filename = f"Backtest_Result_{TIKR}_Vol_Brk_Out_K={K}.csv"
filename = "Backtest_Result_['117460', '091160', '091180', '266360', '305720', '466920', '244580', '449450', '143860', '228790']_Vol_Brk_Out_K=0.3.csv"
df = pd.read_csv(filename)

fig, ax = plt.subplots(1, 1, figsize=(8, 6), tight_layout=True)

ax.plot(df["Day"], (df["Total"]/df["Total"].iloc[0]-1)*100,
        linestyle="-", linewidth=2, color="#E63946",
        marker="none", markersize=8, markerfacecolor="white", markevery=100,
        label=f"Vol. Break-out(K={K})")
ax.plot(df["Day"], (df["Close"]/df["Close"].iloc[0]-1)*100,
        linestyle="-", linewidth=2, color="#1D3557",
        marker="none", markersize=8, markerfacecolor="white", markevery=100,
        label="Buy and hold")

plt.title(f'{TIKR} ({df["Day"].iloc[0].replace("-",".")} - {df["Day"].iloc[-1].replace("-",".")})',
          fontsize=14, color="black", fontname="Times New Roman")
ax.set_xlabel("Time",
              fontsize=14, color="black", fontname="Times New Roman")
ax.set_ylabel("Return [%]",
              fontsize=14, color="black", fontname="Times New Roman")
plt.legend()
ax.set_yscale("linear")
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.xticks(fontname="Times New Roman", fontsize=12, rotation=15)
plt.yticks(fontname="Times New Roman", fontsize=12)
ax.grid(True)

# ax.set_yscale("log")
plt.show()

plt.tight_layout()
# if does_save:
  # plt.savefig(f"{filename}_figure.png", dpi=300)