from matplotlib.pyplot import tight_layout
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator
import etfs
import seaborn as sns
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

does_save = True

#
# for TIKR in etfs.sector_etf["TIKR"]:
#   print(TIKR)
#   filename = f"backtest_result/sector-vol-def/tr/K0{int(K*10)}/Backtest_Result_{TIKR}_Vol_Brk_Out_K={K}.csv"
#   df = pd.read_csv(filename)
#
#   fig, ax = plt.subplots(1, 1, figsize=(8, 6), tight_layout=True)
#
#   ax.plot(df["Day"], (df["Total"]/df["Total"].iloc[0]-1)*100,
#           linestyle="-", linewidth=2, color="#E63946",
#           marker="none", markersize=8, markerfacecolor="white", markevery=100,
#           label=f"Vol. Break-out(K={K})")
#
#   ax.plot(df["Day"], (df["Close"]/df["Close"].iloc[0]-1)*100,
#           linestyle="-", linewidth=2, color="#1D3557",
#           marker="none", markersize=8, markerfacecolor="white", markevery=100,
#           label="Buy and hold")
#   plt.legend(loc="center left")
#   plt.xticks(fontname="Times New Roman", fontsize=12, rotation=15)
#   plt.yticks(fontname="Times New Roman", fontsize=12)
#   ax.grid(True)
#
#   ax2 = ax.twinx()
#   ax2.plot(df["Day"], df["MDD"]*100, linestyle="-", linewidth=1, color="#50514F",
#           marker="none", markersize=8, markerfacecolor="white", markevery=100,
#           label=f"Vol. Break-out(K={K})")
#   ax2.set_ylabel("MDD", color="black", fontsize=14, fontname="Times New Roman")
#   ax2.set_ylim((-100,0))
#
#   plt.title(f'{TIKR} ({df["Day"].iloc[0].replace("-",".")} - {df["Day"].iloc[-1].replace("-",".")})',
#             fontsize=14, color="black", fontname="Times New Roman")
#   ax.set_xlabel("Time",
#                 fontsize=14, color="black", fontname="Times New Roman")
#   ax.set_ylabel("Return [%]",
#                 fontsize=14, color="black", fontname="Times New Roman")
#
#   ax.set_yscale("linear")
#   ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#
#   # ax.set_yscale("log")
#   # plt.show()
#
#   plt.tight_layout()
#   if does_save:
#     plt.savefig(f"{filename}_figure.png", dpi=300)


# K_ = [0.3, 0.5, 0.7]
# fig, ax = plt.subplots(1, 1, figsize=(8, 6), tight_layout=True)
# for K in K_:
#   data_dict = {
#     "TIKR":[],
#     "CAGR":[],
#     "MDD":[],
#   }

K_ = [0.3, 0.5, 0.7]
vol_case = ["high-low","high-open","open-low","tr"]
cagr_list = []
mdd_list = []
for vol in vol_case:
  for K in K_:
    temp_list = []
    temp_list_mdd = []
    for TIKR in etfs.sector_etf["TIKR"]:

      print(TIKR)
      filename = f"backtest_result/sector-vol-def/{vol}/K0{int(K*10)}/Backtest_Result_{TIKR}_Vol_Brk_Out_K={K}.txt"
      # data_dict["TIKR"].append(TIKR)
      with open(filename,"r") as file:
        line = file.readlines()[3]
        cagr = float(line.split("|")[6].replace("%",""))
        mdd = float(line.split("|")[4].replace("%",""))
        # data_dict["CAGR"].append(cagr)
        # data_dict["MDD"].append(mdd)
        temp_list.append(cagr)
        temp_list_mdd.append(mdd)
    cagr_list.append(temp_list)
    mdd_list.append(temp_list_mdd)


  # ax.scatter(data_dict["MDD"], data_dict["CAGR"])

# plt.show()
# print(len(data_dict["CAGR"]))
# print(data_dict["CAGR"])
fig, ax = plt.subplots(1,1, figsize=(8,6))
# xticks = ["117680", "266410", "139290", "227550", "139250", "140710", "139260", "098560", "143860", "139270", "329200"]
xticks = etfs.sector_etf["Name"]
yticks = ["High-Low\n0.3", "0.5", "0.7", "High-Open\n0.3", "0.5", "0.7","Open-Low\n0.3", "0.5", "0.7","True Range\n0.3", "0.5", "0.7",]

sns.heatmap(data = cagr_list, annot=True, cmap="RdYlGn", cbar=False,
            vmin=-50, vmax=100,
            xticklabels=xticks, yticklabels=yticks,
            linewidth=0.5, linecolor="black")
ax.set_xticklabels(xticks, rotation=45)
plt.tight_layout()
plt.savefig("vol-band-cagr.png", dpi=300)
# plt.show()

fig, ax = plt.subplots(1,1, figsize=(8,6))
# xticks = ["117680", "266410", "139290", "227550", "139250", "140710", "139260", "098560", "143860", "139270", "329200"]
xticks = etfs.sector_etf["Name"]
yticks = ["High-Low\n0.3", "0.5", "0.7", "High-Open\n0.3", "0.5", "0.7","Open-Low\n0.3", "0.5", "0.7","True Range\n0.3", "0.5", "0.7",]

sns.heatmap(data = mdd_list, annot=True, cmap="PiYG", cbar=False,
            vmin=-30, vmax=30,
            xticklabels=xticks, yticklabels=yticks,
            linewidth=0.5, linecolor="black")
ax.set_xticklabels(xticks, rotation=45)
plt.tight_layout()
plt.savefig("vol-band-mdd.png", dpi=300)
plt.show()