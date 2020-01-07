import jieba
# 全模式
# text = "我来到北京清华大学"
# seg_list = jieba.cut(text, cut_all=True)
# print(u"[全模式]: ", "/ ".join(seg_list))
# # 精确模式
# seg_list = jieba.cut(text, cut_all=False)
# print(u"[精确模式]: ", "/ ".join(seg_list))
# # 默认是精确模式
# seg_list = jieba.cut(text)
# print(u"[默认模式]: ", "/ ".join(seg_list))
# # 搜索引擎模式
# seg_list = jieba.cut_for_search(text)
# print(u"[搜索引擎模式]: ", "/ ".join(seg_list))

#新词识别  “杭研”并没有在词典中,但是也被Viterbi算法识别出来了
# seg_list = jieba.cut("他来到了网易杭研大厦")
# print (u"[新词识别]: ", "/ ".join(seg_list))

# text = "故宫的著名景点包括乾清宫、太和殿和黄琉璃瓦等"
# 全模式
# seg_list = jieba.cut(text, cut_all=True)
# print(u"[全模式]: ", "/ ".join(seg_list))
# # 精确模式
# seg_list = jieba.cut(text, cut_all=False)
# print(u"[精确模式]: ", "/ ".join(seg_list))
# # 搜索引擎模式
# seg_list = jieba.cut_for_search(text)
# print(u"[搜索引擎模式]: ", "/ ".join(seg_list))

# file_name = r'1.txt'
# jieba.load_userdict(file_name) #file_name为自定义词典的路径

# jieba.load_userdict("D:\Program Files\Python36\Lib\site-packages\jieba\mydict.txt")
# text = "故宫的著名景点包括乾清宫、太和殿和黄琉璃瓦等"
# # 全模式
# seg_list = jieba.cut(text, cut_all=True)
# print(u"[全模式]: ", "/ ".join(seg_list))
#
# # 精确模式
# seg_list = jieba.cut(text, cut_all=False)
# print(u"[精确模式]: ", "/ ".join(seg_list))
# # 搜索引擎模式
# seg_list = jieba.cut_for_search(text)
# print(u"[搜索引擎模式]: ", "/ ".join(seg_list))

#精确模式
# text = "故宫的著名景点包括乾清宫、太和殿和午门等。其中乾清宫非常精美，午门是紫禁城的正门，午门居中向阳。"
# seg_list = jieba.cut(text, cut_all=False)
# print (u"分词结果:")
# print ("/".join(seg_list))
# #获取关键词
# tags = jieba.analyse.extract_tags(text, topK=5)
# print (u"关键词:")
# print (" ".join(tags))

# stopwords = {}.fromkeys(['的', '包括', '等', '是'])
# text = "故宫的著名景点包括乾清宫、太和殿和午门等。其中乾清宫非常精美，午门是紫禁城的正门。"# 精确模式
# segs = jieba.cut(text, cut_all=False)
# final = ''
# for seg in segs:
#     if seg not in stopwords:
#             final += seg
# print (final)
#
# seg_list = jieba.cut(final, cut_all=False)
# print ("/ ".join(seg_list))