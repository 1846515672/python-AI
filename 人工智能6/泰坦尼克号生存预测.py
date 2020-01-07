import pandas as pd
import numpy as np

titan = pd.read_csv('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt')
# print(titan.info())

x = titan[['pclass', 'age', 'sex']]
y = titan['survived']

x['age'].fillna(x['age'].mean(), inplace=True)
# print(x['age'].isnull().sum())
# print(x)
#哑变量处理
# print(pd.get_dummies(x['sex']))

#
x.to_dict(orient='records')#将其转为子典格式
# print(x.to_dict(orient='records'))、
from sklearn.feature_extraction import DictVectorizer
dict = DictVectorizer(sparse=False)
x = dict.fit_transform(x.to_dict(orient='records'))
# print(x)
# print(dict.get_feature_names())

#分割测试集与训练集
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)

from sklearn.tree import DecisionTreeClassifier


dc = DecisionTreeClassifier(criterion='entropy', max_depth=5)
dc.fit(x_train, y_train)
# print(dc.predict(x_train))
print('模型精度:',dc.score(x_test, y_test))

#决策树导出：
from sklearn import tree

tree.export_graphviz(dc, 'tree.dot')