import requests
import numpy as np
import pandas as pd
# from lxml import etree
# for i in range(75):
#     url = f'http://www.stat-nba.com/query.php?page={i}&QueryType=all&AllType=season&AT=avg&order=1.txt&crtcol=pts&PageNum=60#label_show_result'
#     response = requests.get(url=url).content.decode('utf-8')
#     # with open('篮球赛.html', 'w', encoding='utf-8')as f:
#     #     f.write(response)
#     # print(response)
#     html = etree.HTML(response)
#     trees = html.xpath('//*[@id="label_show_result"]/div[2]/table/tbody')
#     # print(trees)
#     for new in trees:
#         # print(new)
#         # 球员姓名
#         names = new.xpath('./tr/td[2]/a/text()')
#         name = ",".join(names)
#         # print(name)
#         #时间
#         times = new.xpath('./tr/td[5]/text()')
#         time = ",".join(names)
#         # print(time)
#         # 篮板
#         backboards = new.xpath('./tr/td[15]/text()')
#         backboard = ",".join(backboards)
#         # print(backboard)
#         #助攻
#         assists = new.xpath('./tr/td[18]/text()')
#         assist = ",".join(assists)
#         # print(assist)
#         #得分
#         scores = new.xpath('./tr/td[last()-2]/text()')
#         score = ",".join(scores)
#         print(score)

# data = pd.read_excel(r"C:\Users\Administrator\Desktop\作业\老师的资料\数据分析\meal_order_detail.xlsx")
# data = pd.read_excel(r"C:\Users\Administrator\Desktop\作业\数据分析作业\nb.xls")
data = pd.read_excel(r"C:\Users\Administrator\Desktop\nba.xlsx")#数据库导出时需要选择xlsx格式的类型表导出，否则打不开表！！
columns = ['ID', '球员姓名', '时间', '篮板', '助攻', '得分']
datas = pd.DataFrame(data=data.values, columns=columns)
print(datas)