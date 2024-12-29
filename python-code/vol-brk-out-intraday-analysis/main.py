import pandas as pd
from matplotlib import pyplot as plt

def time_to_normalize_index(time):
  time = time.split(":")
  return int(time[0])*60 + int(time[1])

filename =  "C:/Users/GP/OneDrive/바탕 화면/intraday-data/merged_TQQQ.json"
df = pd.read_json(filename)

# time_init = 60*9 + 30
# normal_time_list = []
# for ind in range(len(df)):
#   print(ind)
#   # time_init = time_to_normalize_index(df["Time"][ind][0])
#   # time_term = time_to_normalize_index(df["Time"][ind][-1])
#   normal_time = []
#   for time in df["Time"][ind]:
#       normal_time.append(time_to_normalize_index(time)-time_init)
#   normal_time_list.append(normal_time)
# df["Time(normal)"] = normal_time_list
#
# print(df)
# df.to_json("merged_TQQQ_with_normal_time.json")

filename =  "C:/Users/GP/OneDrive/바탕 화면/intraday-data/merged_TQQQ_with_normal_time.json"
df = pd.read_json(filename)
print(df)

ind = 0
fig, ax = plt.subplots(1, 1, figsize=(8,6))
ax.plot(df["Time(normal)"][ind], df["Open"][ind], marker="o")
ax.plot(df["Time(normal)"][ind+1], df["Open"][ind+1], marker="o")
ax.plot(df["Time(normal)"][ind+2], df["Open"][ind+2], marker="o")
ax.plot(df["Time(normal)"][ind+3], df["Open"][ind+3], marker="o")
ax.plot(df["Time(normal)"][ind+4], df["Open"][ind+4], marker="o")
ax.plot(df["Time(normal)"][ind+100], df["Open"][ind+100], marker="o")
ax.plot(df["Time(normal)"][ind+1000], df["Open"][ind+1000], marker="o")
plt.show()