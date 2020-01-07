# -*- coding: utf-8 -*-
# @Time    : 2019/12/28 9:04
# @Author  : SongYajiao
# @File    : 18.电影行情分析.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt

credit= pd.read_csv(r'tmdb_5000_credits.csv') # 4803
movies= pd.read_csv(r'tmdb_5000_movies.csv')  # 4803
print(credit.info())
print(movies.info())

#(1)主键合并两张表：注意：不能只通过电影名称合并，因为有重名电影
data = pd.merge(credit, movies, left_on='movie_id', right_on='id', how='outer')
# print(data.shape)

# print(data.info())

def get_movie_type(values):
    movie_type_list = json.loads(values)
    type_list = []
    for mtype in movie_type_list:
        movie_type = mtype.get('name')
        type_list.append(movie_type)


    return type_list



genres = data['genres'].transform(get_movie_type)
# print(genres)
data['release_date'] = pd.to_datetime(data['release_date'])
release_year = data['release_date'].dt.year

df_type_time = pd.DataFrame({'genres':genres, 'release_date':release_year})
# print(df_type_time)

retime_groupby = df_type_time.groupby(by='release_date').sum().reset_index()
retime_groupby_DF = retime_groupby['genres'].apply(pd.Series)
year = retime_groupby['release_date'].astype('int')
# print(year)


##（1）求每年发行最多的电影类型：
# describe_type = (retime_groupby_DF.T).describe()
# movie_top = describe_type.loc['top', :]
# movie_freq = describe_type.loc['freq', :]
# print((retime_groupby_DF.T).mode())
# print(movie_top)

#柱状图：
# orientation  # 字符串，两种值供选择{'vertical'垂直,'horizontal'水平}

# plt.figure()
# x= np.linspace(1,295 ,90)
# plt.bar(x, movie_freq)
# for x, y, z in zip(x, movie_freq, movie_top):
#     plt.text(x, y, z )
# plt.show()

# 1912——2017 喜剧片数量走势：
# （2）统计各个类型每年发行的电影数量：
# print(retime_groupby_DF)

##一、电影类型随时间推移的变化
type_arr = retime_groupby_DF.astype('object').fillna('无').values
movies_type = np.unique(type_arr)[:-1]
print(movies_type)

plt.figure()
plt.rcParams['font.sans-serif'] = 'SimHei' #修改默认字体；
plt.rcParams['axes.unicode_minus'] = False #正常显示符号，解决显示为方块的问题
for i in movies_type:
    print(i)
    x = np.linspace(1, 179, 90)
    x1 = np.linspace(1, 179, 46)
    y_number = (type_arr == i).sum(axis=1)
    plt.plot(x, y_number)

plt.legend(movies_type)
plt.xticks(x1, year[:92:2], rotation=45)
plt.title('电影类型随时间推移的变化')
plt.show()