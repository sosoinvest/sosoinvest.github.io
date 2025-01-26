from matplotlib.pyplot import tight_layout
from backtester import tester100
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator
from data import etf_list
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False
noise_list = []
cagr_list = []
K = 0.5
for tikr in etf_list.etf_list.values():

  filepath = f"C:/Users/GP/OneDrive/바탕 화면/sosoinvest-github-blog/sosoinvest.github.io/python-code/vol-brk-out/data/{tikr}.KS_2024-01-23_2025-01-23_interval=1d.csv"
  does_save = False
  my_tester = tester100.Backtester(filename=filepath,
                                   tikr=tikr,
                                   does_save=does_save,
                                   fee=0.0036396*0.01, tax=0.0, slippage=0.0*0.01, leverage=1,
                                   losscut=5*0.01,
                                   deposit_cash=10000,
                                   strategy="VolBrkOut_ohlc",
                                   params={"K": K},
                                   window=1)
  my_tester.run()
  noise_list.append(my_tester.strategy.noise)
  cagr_list.append(my_tester.analyzer.analysis_result["CAGR"])
  input("")

  # BLOCK
  filename = f"Backtest_Result_{tikr}_Vol_Brk_Out_K={K}.csv"
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

  plt.title(f'{tikr} ({df["Day"].iloc[0].replace("-",".")} - {df["Day"].iloc[-1].replace("-",".")})',
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
  # plt.show()

  plt.tight_layout()
  if does_save:
    plt.savefig(f"{filename}_figure.png", dpi=300)

dict = {
  "Code": [],
  "Noise": [],
  "CAGR": []
}
# df = pd.DataFrame(etf_list.etf_list)
# code = df.iterrows()
# print(code)

for i in range(len(noise_list)):
  print(noise_list[i])
for i in range(len(noise_list)):
  print(cagr_list[i][0])



