import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

filenames = ["High-to-low", "Open-to-low", "High-to-open", "TR"]
for filename in filenames:
  with open(filename+".txt") as file:
    text = file.readline()
    text = file.readline()
    text = file.readline()
    text = file.readline()
    text = text.split("|")
    final_return = text[2].replace(" ","")
    buy_and_hold_return = text[3].replace(" ","")
    mdd = text[4].replace(" ","")
    mdd_bnh = text[5].replace(" ","")
    cagr = text[6].replace(" ","")
    n_of_trades = text[7].replace(" ","")
    win_rate = text[9].replace(" ", "")
    mean_plus_return = text[12].replace(" ", "")
    mean_minus_return = text[13].replace(" ", "")
    rr_ratio = text[14].replace(" ","")
    sharp_ratio = text[10].replace(" ","")
    sharp_ratio_bnh = text[11].replace(" ", "")

    # print(f"| |0.{K}|{final_return}|{buy_and_hold_return}|{mdd}|{mdd_bnh}|{cagr}|{n_of_trades}|{win_rate}|{mean_plus_return}|{mean_minus_return}|{rr_ratio}|{sharp_ratio}|{sharp_ratio_bnh}|")
    print(
      f"||{filename}|{final_return}|{mdd}|{cagr}|{n_of_trades}|{win_rate}|{mean_plus_return}|{mean_minus_return}|{rr_ratio}|{sharp_ratio}|")

# BLOCK: Plot the result
K = 0.1
TIKR = 229200
does_save =True

filename = f"high-to-low.csv"
df = pd.read_csv(filename)

fig, ax = plt.subplots(1, 1, figsize=(8, 6), tight_layout=True)

ax.plot(df["Day"], (df["Close"]/df["Close"].iloc[0]-1)*100,
        linestyle="-", linewidth=2, color="#1D3557",
        marker="none", markersize=8, markerfacecolor="white", markevery=100,
        label="Buy and hold")

for filename in filenames:
  df = pd.read_csv(filename+".csv")
  ax.plot(df["Day"], (df["Total"] / df["Total"].iloc[0] - 1) * 100,
          linestyle="-", linewidth=2,
          marker="none", markersize=8, markerfacecolor="white", markevery=100,
          label=f"{filename}")

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

plt.tight_layout()

# if does_save:
#   plt.savefig(f"total_figure.png", dpi=300)
#
# plt.show()