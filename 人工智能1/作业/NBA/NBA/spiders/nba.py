# -*- coding: utf-8 -*-
import scrapy
from ..items import NbaItem

class NbaSpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ['stat-nba.com']
    start_urls = []
    for i in range(75):
        url = f'http://www.stat-nba.com/query.php?page={i}&QueryType=all&AllType=season&AT=avg&order=1&crtcol=pts&PageNum=60#label_show_result'
        start_urls.append(url)

    def parse(self, response):
        trees = response.xpath('//*[@id="label_show_result"]/div[2]/table/tbody/tr')
        # print(trees)
        for new in trees:
            item = NbaItem()
            # print(new)
            # 球员姓名
            names = new.xpath('./td[contains(@class,"normal player_name_out change_color")]/a/text()').extract()
            name = names[0] if names else ''
            item['name'] = name
            print(name)
            # 时间
            times = new.xpath('./td[contains(@class,"normal mp change_color")]/text()').extract()
            time = times[0] if times else ''
            item['time'] = time
            print(time)
            # 篮板
            backboards = new.xpath('./td[contains(@class,"normal trb change_color")]/text()').extract()
            backboard = backboards[0] if backboards else ''
            item['backboard'] = backboard
            print(backboard)
            # 助攻
            assists = new.xpath('./td[contains(@class,"normal ast change_color")]/text()').extract()
            assist = assists[0] if assists else ''
            item['assist'] = assist
            print(assist)
            # 得分
            scores = new.xpath('./td[contains(@class,"current pts change_color")]/text()').extract()
            score = scores[0] if scores else ''
            item['score'] = score
            print(score)
            yield item
