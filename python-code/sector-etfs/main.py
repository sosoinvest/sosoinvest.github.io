import pandas as pd

filename = "data.txt"
code_list = []
with open("codes.txt","r", encoding="utf-8") as file:

  while True:
    line = file.readline().replace("\n","")

    if not line:
      break
    else:
      code_list.append(line)

line_list = []
with open(filename,"r", encoding="utf-8") as file:
  while True:
    line = file.readline().replace("\n", "")

    if not line:
      break
    else:
      line_list.append(line)
del line_list[0]
del line_list[0]

ind = 0
for line in line_list:
  url = f"http://m.stock.naver.com/domestic/stock/{code_list[ind]}"
  line2 = line.split("|")
  line2[3] = f"[{line2[3]}]({url})"

  print(f"{line2[0]}|{line2[1]}|{line2[2]}|{line2[3]}|{code_list[ind]}|{line2[4]}|{line2[5]}|{line2[6]}|{line2[7]}|{line2[8]}")

  ind+=1
