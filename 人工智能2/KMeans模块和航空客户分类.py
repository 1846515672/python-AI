# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 14:02
# @Author  : SongYajiao
# @File    : 13航空客户分类.py
# @Software: PyCharm

#第一：数据清洗：
"""
(1.txt)丢弃票价为空的记录。
(2)保留票价不为 0、平均折扣率不为 0、总飞行千米数大于 0 的记录。

"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = pd.read_csv(r'air_data.csv', engine='python')
print(data.info())
print(data.shape)

#(1.txt)去掉票价为空的值：
mask1 = data['SUM_YR_1'].isnull()
mask2 = data['SUM_YR_2'].isnull()
mask = mask1 | mask2
# print(mask)
label = data.index[mask]
data.drop(labels=label, axis=0, inplace=True)
print(data.shape)

#(2)保留票价不为0、平均折扣率不为 0、总飞行千米数大于0 的记录
index1 = data['SUM_YR_1'] !=0
index2 = data['SUM_YR_2'] !=0
index3 = index1 | index2
index4 = data['avg_discount'] !=0
index5 = data['SEG_KM_SUM']>0

label = index3 & index4 & index5
# print(label)
air_data = data.loc[label, : ]
# print(air_data.shape)

#第二：构建特征值：
#(1.txt) L :入会距离观测窗口的月数：
air_data['L'] = ((pd.to_datetime(air_data['LOAD_TIME']) - pd.to_datetime( air_data['FFP_DATE']))/30).dt.days


#(2)R:最后一次乘机，距离观测窗口结束的时长：
air_data['R'] = air_data['LAST_TO_END']/30

#获取5个特征：
air_feature = air_data.loc[:, ['L', 'R', 'FLIGHT_COUNT', 'SEG_KM_SUM', 'avg_discount']]
air_feature.rename(columns={'FLIGHT_COUNT': 'F', 'SEG_KM_SUM':'M', 'avg_discount':'C'}, inplace=True)
# print(air_feature.columns)

#三、标准化：
from sklearn.preprocessing import StandardScaler
air_std = StandardScaler().fit_transform(air_feature)
print(air_std)

#四、聚类：
from sklearn.cluster import KMeans
kms = KMeans(n_clusters=5)
# print(kms.fit_predict(air_std))
kms.fit(air_std)
print('聚类中心：\n', kms.cluster_centers_)
print('预测类别号：\n', kms.labels_)

#五、雷达图可视化：

y = kms.cluster_centers_
y1 = y[:, 0].reshape(5,1)
y_new = np.concatenate((y,y1 ), axis=1)
print(y_new)

x = np.linspace(0, 2*np.pi, 5, endpoint=False)
x1 = np.array([0])
print(x1)
x_new = np.concatenate((x, x1))
print(x_new)

plt.figure()

for i in range(5):
    plt.polar(x_new, y_new[i, :])
    plt.fill(x_new, y_new[i, :], alpha=0.25) ##填充颜色

plt.xticks(x_new, ['L', 'R', 'F', 'M','C'])
plt.show()
