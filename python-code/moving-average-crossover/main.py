from matplotlib.pyplot import tight_layout
from backtester import tester100
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator
import numpy as np
import seaborn as sns
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# BLOCK: VBO Multi
does_save = False
tikr = "058470"

# my_tester = tester100.Backtester(filename=f"",
#                                  tikr=tikr,
#                                  does_save=does_save,
#                                  fee=0.0036396*0.01, tax=0.18*0.0, slippage=0.0*0.01, leverage=1,
#                                  losscut=5*0.01,
#                                  deposit_cash=10000,
#                                  strategy="MAC",
#                                  params={"Windows": [5,6]},
#                                  window=1)
# my_tester.run()


short_window = list(range(5,20))
long_window = list(range(6,40))
CAGR_list = []
MDD_list = []
for x1, x2 in [(a, b) for a in short_window for b in long_window]:
  my_tester = tester100.Backtester(filename=f"",
                                   tikr=tikr,
                                   does_save=does_save,
                                   fee=0.0036396 * 0.01, tax=0.18 * 0.01, slippage=0.0 * 0.01, leverage=1,
                                   losscut=5 * 0.01,
                                   deposit_cash=10000,
                                   strategy="MAC",
                                   params={"Windows": [x1, x2]},
                                   window=1)
  if x1 < x2:
    my_tester.run()
    CAGR_list.append(float(my_tester.analyzer.analysis_result["CAGR"][0].replace(" %","")))
    MDD_list.append(float(my_tester.analyzer.analysis_result["MDD"][0].replace(" %","")))
  else:
    CAGR_list.append(np.nan)
    MDD_list.append(np.nan)

CAGR_list = np.array(CAGR_list)
MDD_list = np.array(MDD_list)
short_grid, long_grid = np.meshgrid(long_window, short_window)

cagr_grid = CAGR_list.reshape(len(short_window),len(long_window))

# BLOCK
# fig, ax = plt.subplots(1, 1, figsize=(10,8), subplot_kw={"projection": "3d"})
# ax.plot_surface(short_grid, long_grid, cagr_grid, cmap="viridis")
#
# plt.tight_layout()
# plt.show()

# BLOCK
fig, ax = plt.subplots(1,1, figsize=(8,8))

xticks = long_window
yticks = short_window

sns.heatmap(data = cagr_grid, annot=False, cmap="viridis", cbar=True, cbar_kws={"shrink": 0.7},
            xticklabels=xticks, yticklabels=yticks, square=True,
            linewidth=0.5, linecolor="black")
ax.set_xticklabels(xticks, rotation=45)

fontdict={"fontsize": 14, "fontweight": "light", "family": "Times New Roman"}

ax.set_ylabel("Short window",fontdict=fontdict)
ax.set_xlabel("Long window",fontdict=fontdict)
ax.set_title(f"{tikr} CAGR",fontdict=fontdict)

ax.set_xticklabels(ax.get_xticklabels(), fontsize=12, fontweight="light", family="Times New Roman")
ax.set_yticklabels(ax.get_yticklabels(), fontsize=12, fontweight="light", family="Times New Roman")

plt.tight_layout()
plt.savefig("cagr.png", dpi=300)
plt.show()

