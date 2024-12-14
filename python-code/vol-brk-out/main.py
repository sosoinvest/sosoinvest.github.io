
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')



import tester_100

# my_tester = tester_100.Backtester(filename=f"{etfs.sector_etf["TIKR"][-3]}.csv",
#                                   tikr=f"{etfs.sector_etf["Name"][-3]}",
#                                   K=0.5, does_save=False, window=1,
#                                   fee=0.015*0.01, tax=0)
my_tester = tester_100.Backtester(filename=f"data/143860.KS.csv",
                                  tikr="TIGER HEALTH",
                                  K=0.5, does_save=False, window=1,
                                  fee=0.015*0.01, tax=0.0, slippage=0.1*0.01, leverage=3)
my_tester.run_vb()


# # BLOCK: Import modules for plot
# from matplotlib import pyplot as plt
# from matplotlib.ticker import MaxNLocator
# plt.rcParams["font.family"] ="Malgun Gothic"
# plt.rcParams["axes.unicode_minus"] = False
#
# filename = f"Backtest_Result_{TIKR}_Vol_Brk_Out_K={K}.csv"
# df = pd.read_csv(filename)
#
# # Create a figure object
# fig, ax = plt.subplots(1, 1, figsize=(8, 6), tight_layout=True)
#
# # Plot the data
# ax.plot(df["Day"], (df["Total"]/df["Total"].iloc[0]-1)*100,
#         linestyle="-", linewidth=2, color=my_colors.color[0],
#         marker="none", markersize=8, markerfacecolor="white", markevery=10,
#         label="Vol. Break-out")
# ax.plot(df["Day"], (df["Close"]/df["Close"].iloc[0]-1)*100,
#         linestyle="-", linewidth=2, color=my_colors.color[4],
#         marker="none", markersize=8, markerfacecolor="white", markevery=10,
#         label="Buy and hold")
#
# # Set legend and axis
# plt.legend() # Show the legends
# ax.xaxis.set_major_locator(MaxNLocator(integer=True)) # Limit the xtick labels
# plt.xticks(fontname="Times New Roman", fontsize=12, rotation=15)  # Rotate the xticks by 15 degree
# plt.yticks(fontname="Times New Roman", fontsize=12) # Set the yticks
# ax.grid(True) # Show grids
#
# # Add texts
# plt.text(500, 100, "ì¶ì²: sosoinvest.github.io", fontsize=18, color="gray", ha="center")
# plt.title(f"{etfs.sector_etf["Name"][ind]}",  fontdict={"fontsize":16, "fontweight": "normal"})
# # plt.title(f"{etfs.sector_etf["Name"][ind]}", fontdict={"fontsize": 16, "fontweight": "normal", "family": "Times New Roman"})
# plt.xlabel("Time", fontsize=16, color="black", fontname="Times New Roman")
# plt.ylabel("Return [%]", fontsize=16, color="black", fontname="Times New Roman")
#
# # Save figure and show
# plt.tight_layout() # Tight layout
# if does_save:
#     plt.savefig(f"{filename}_figure.png", dpi=300)
# # plt.show()

# # BLOCK: Import modules for plot
# from matplotlib import pyplot as plt
# from matplotlib.ticker import MaxNLocator
# plt.rcParams["font.family"] ="Malgun Gothic"
# plt.rcParams["axes.unicode_minus"] = False
#
# TIKR_list = []
# for ind in range(0, 11):
#     TIKR_list.append(etfs.sector_etf["TIKR"][ind])
#
# TIKR_name_list = ["ìì¬", "íììë¹ì¬", "ê²½ê¸°ìë¹ì¬", "ì°ìì¬",
#                   "ìëì§", "ì í¸ë¦¬í°", "IT", "íµì ìë¹ì¤", "í¬ì¤ì¼ì´",
#                   "ê¸ìµ", "ë¶ëì°"]
# df_list = []
# KK = 0.5
#
# for TIKR in TIKR_list:
#     filename = f"Backtest_Result_{TIKR}_Vol_Brk_Out_K={KK}.csv"
#     df = pd.read_csv(filename)
#     df.rename(columns={"Unnamed: 0": "Day"})
#     df.index = df["Day"]
#
#     df_list.append(df)
#     # KK+=0.1
#
# # Re-indexing
# combined_index = df_list[0].index
# for df in df_list:
#     combined_index = combined_index.union(df.index)
#
# count = 0
# for df in df_list:
#     df = df.reindex(combined_index)
#     df.ffill(inplace=True)
#     df_list[count] = df
#     count += 1
#
# # Create a figure object
# fig, ax = plt.subplots(1, 1, figsize=(8, 6), tight_layout=True)
#
# # Plot the data
# count = 0
# marker_list = ["o", "s", "^", "v", "D", "*", "none", "none", ]
#
# for df in df_list:
#
#     # ax.plot(df.index, (df["Total"]/df["Total"].iloc[0]-1)*100,
#     ax.plot(df.index, (df["Total"] / 10000 - 1) * 100,
#         linestyle="-", linewidth=2, label=TIKR_name_list[count],
#         marker="none", markevery=100, markersize=6,markerfacecolor="white")
#     count += 1
#
# # ax.plot(df["Day"], (df["Close"]/df["Close"].iloc[0]-1)*100,
# #             linestyle="-", linewidth=2, color=my_colors.color[4],
# #             marker="none", markersize=8, markerfacecolor="white", markevery=10,
# #             label="Buy and hold")
#
# # Set legend and axis
# plt.legend() # Show the legends
# ax.xaxis.set_major_locator(MaxNLocator(integer=True)) # Limit the xtick labels
# plt.xticks(fontname="Times New Roman", fontsize=12, rotation=15)  # Rotate the xticks by 15 degree
# plt.yticks(fontname="Times New Roman", fontsize=12) # Set the yticks
# ax.grid(True) # Show grids
#
# # Add texts
# plt.text(450, 500, "ì¶ì²: sosoinvest.github.io", fontsize=18, color="gray", ha="center")
# # plt.title(f"HANG SENG (China)", fontdict={"fontsize": 16, "fontweight": "normal", "family": "Times New Roman"})
# plt.xlabel("Time", fontsize=16, color="black", fontname="Times New Roman")
# plt.ylabel("Return [%]", fontsize=16, color="black", fontname="Times New Roman")
#
# # Save figure and show
# plt.tight_layout() # Tight layout
# plt.savefig(f"sector-total.png", dpi=300)
# plt.show()