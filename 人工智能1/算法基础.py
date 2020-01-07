import pandas as pd
import numpy as np


def kmeans(center):

    # (2)聚类：
    df = pd.DataFrame()
    for i in range(3):
        d = np.sqrt(((train - center[i, :])**2).sum(axis=1))
        df[i] = d

    #(3)分类结果：
    index1 = np.argsort(df, axis=1)[0]

    #(4)更新类中心：
    new_center = np.zeros((3, 2))

    for i in range(3):
        mask = index1 == i
        x_y = train.loc[mask, :].mean(axis=0)
        new_center[i, :] = x_y
        print(new_center)
        return new_center

if __name__ == '__main__':
    data = pd.read_csv('company.csv', encoding='gbk', engine='python')
    train = data.loc[:, ['平均每次消费金额', '平均消费周期（天）']]

    # (1.txt)给出初始中心：
    center = np.array([[100, 10], [200, 20], [300, 30]])
    new_center = kmeans(center)

    while True:
        if np.all(center == new_center):
            break
    center = new_center.copy()
    new_center = kmeans(center)

