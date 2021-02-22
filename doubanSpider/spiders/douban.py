import scrapy

from doubanSpider.items import DoubanspiderItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']
    start_urls = ['http://www.douban.com/group/26926/discussion']
    max_page = 5
    search_str_list = ['6号线', '十号线']
    proxy = None
    output_file_name = 'output'

    def __init__(self, start_url=None, max_page=None, search_strs='', proxy=None, output_file_name=None, *args, **kwargs):
        super(DoubanSpider, self).__init__(*args, **kwargs)
        if start_url is None:
            start_url = 'http://www.baidu.com'
        self.start_urls = [start_url]
        self.max_page = max_page
        self.search_str_list = search_strs.split(",")
        self.proxy = proxy
        self.output_file_name = output_file_name

    def parse(self, response):
        if self.start_urls is None or self.max_page is None or self.search_str_list is None or not self.search_str_list:
            return None
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
        if nexturl and cur_page and int(cur_page) < int(self.max_page):
            yield scrapy.Request(url=nexturl, callback=self.parse, meta={})
        else:
            return None
