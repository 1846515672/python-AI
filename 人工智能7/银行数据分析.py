import pandas as pd
import numpy as np


data = pd.read_csv(r'loan.csv', engine='python')
num = data['好坏客户'].count()
k = data['好坏客户'] == 1
id = data.loc[k, '好坏客户'].index
# print(h/num)
# isna = data.isnull()
# df = data[isna.any(axis=1)]
# df1 = data[isna[['月收入']].any(axis=1)]
# print(data.fillna('未知'))
# huai = data.loc[k, '年龄']
df3 = data.loc[id, '年龄'].mean()
print(df3)