# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        # res1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item = dict()
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["title"] = li.xpath(".//h4/text()").extract_first()
            yield item
