import matplotlib.pyplot as plt
from wordcloud import WordCloud

with open('danmu.txt', 'r', encoding='utf-8') as fp:
    f = fp.read()

# print(f)
backgroup_img = plt.imread(r'3.jpg')#二值化图片路径！


#2、词云
cloud = WordCloud(
    background_color='white',
    # contour_color='red',
    mask = backgroup_img,
    font_step=1,
    font_path='ZhengQingKeJingYaTi-ShouBan-2.ttf',
    width=1000, #宽度
    height=800, #高度
    margin=1, #边缘空白处
    min_font_size=1, #最小字体
).generate(f)
plt.imshow(cloud)
plt.axis('off')
plt.show()