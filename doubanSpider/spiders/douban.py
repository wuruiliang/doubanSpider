import scrapy

from doubanSpider.items import DoubanspiderItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']
    start_urls = []
    max_page = 50
    search_str_list = []
    proxy = None
    count = 0
    cookies = None

    def __init__(self, start_url=None, max_page=None, search_strs=None, proxy=None, cookies=None, *args, **kwargs):
        super(DoubanSpider, self).__init__(*args, **kwargs)
        if start_url is None:
            start_url = 'https://www.baidu.com'
        self.start_urls = [start_url]
        self.max_page = max_page
        self.search_str_list = search_strs.split(",") if search_strs is not None else None
        self.proxy = proxy
        self.cookies = cookies

    def parse(self, response):
        if self.start_urls is None or self.max_page is None or self.search_str_list is None or not self.search_str_list:
            print("参数错误！！！")
            return None
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
            self.count = self.count + 1
            yield item
        nexturl = response.xpath('//*/span[@class="next"]/a/@href').extract_first()
        cur_page = response.xpath('//*/span[@class="thispage"]/text()').extract_first()
        if nexturl and cur_page and int(cur_page) < int(self.max_page):
            yield scrapy.Request(url=nexturl, callback=self.parse, meta={})
        else:
            return None
