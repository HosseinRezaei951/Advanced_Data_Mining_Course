import os
import pandas as pd

result_path = 'results/'
if os.path.isdir(result_path) == False:
    os.mkdir(result_path) 

data = pd.read_csv (r'data/market_basket_dataset.csv')

items = [x for x in range(1, 41)]
for item in items:
    tmp_hasItem = []
    for i in range(1000):
        tmp_items = data["transactions"][i].split(",")
        if str(item) in tmp_items:
            tmp_hasItem.append("Yes")
        else:
            tmp_hasItem.append("No")
    data[item] = tmp_hasItem
data = data.drop(columns=["transactions"])

data.to_csv(result_path + 'new_data.csv', index=False)