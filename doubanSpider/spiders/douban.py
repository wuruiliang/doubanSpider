import scrapy

from doubanSpider.items import DoubanspiderItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']
    start_urls = ['http://www.douban.com/group/26926/discussion']
    max_page = 2
    search_str_list = ['6号线', '十号线']

    def parse(self, response):
        items = []
        for each in response.xpath('//*/table[@class="olt"]/tr'):
            url = each.xpath('td[1]/a/@href').extract_first()
            title = each.xpath('td[1]/a/@title').extract_first()
            time = each.xpath('td[4][@class="time"]/text()').extract_first()
            if url is None or title is None or time is None or not any(str in title for str in self.search_str_list):
                continue
            item = DoubanspiderItem()
            item['url'] = url
            item['title'] = title
            item['time'] = time
            items.append(item)
            yield item
        nexturl = response.xpath('//*/span[@class="next"]/a/@href').extract_first()
        cur_page = response.xpath('//*/span[@class="thispage"]/text()').extract_first()
        if nexturl and cur_page and int(cur_page) < self.max_page:
            yield scrapy.Request(url=nexturl, callback=self.parse, meta={})
        else:
            return None
