import jieba
import numpy as np
import pandas as pd

#a、停用词清洗
with open('stopwords.txt', 'r', encoding='utf-8')as f:
    stopwords = f.readlines()#按行读取数据

# print(stopwords)

#b、去掉重复，并且去掉首尾空字符
stopwords_list = list(map(lambda word: word.strip(), stopwords))
# print(stopwords_list)

#c、利用集合去掉重复
stopwords_list = set(stopwords_list)
# print(stopwords_list)

#2、处理文本
data = pd.read_csv('data.csv', encoding='gbk', engine='python')
# print(data.columns)
col = data['内容 ']
arrs = data['评价']

#(1)分词
comment_list = []
for comment in col:
    #分词
    seg_list = jieba.cut(comment, cut_all=False)
    print(seg_list)
    #去除停用词
    final = ''
    for seg in seg_list:
        if seg not in stopwords_list:
            final += seg
    comment_list.append(final)
print(comment_list)

#计算词频：
from sklearn.feature_extraction.text import CountVectorizer
vector = CountVectorizer()
#a、计算每个关键词出现的次数：词频统计
X = vector.fit_transform(comment_list)
# print(X)
#b、查看关键字
words = vector.get_feature_names()
# print(words)
#c、转换为词频矩阵
# print(X.toarray())
#4、贝叶斯分类
#（1）将训练集与测试集分割
x_train = X.toarray()[:10]
x_text = X.toarray()[10:]

#(2)处理标签
#方法一：
# def get_values(value):
#     if value == '好评':
#         value = 1
#     else:
#         value = 0
#     return value
# print(arrs.transform(get_values))

#方法二：
y = list(map(lambda x: 1 if x == '好评'else 0, arrs))
y_train = y[:10]
y_test = y[10:]

#算法实现：
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(x_train, y_train)

#预测：
y_predict = clf.predict(x_text)
# print(y_predict)
# print(y_test)