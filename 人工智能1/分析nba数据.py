import numpy as np
import pandas as pd

data = pd.read_excel('nba.xlsx')
print(data.info())#查看表参数信息
lanban = data['篮板'].str.isspace()#isspace()判断是否为空，是返回True，否返回False
time = data['时间'].str.isspace()
mask = lanban | time
labels = data.index[mask]
print(labels)

# nba_data = data['篮板'].astype(np.float)
# print(nba_data)