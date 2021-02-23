# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DoubanspiderPipeline:
    file_name = "output.html"

    def process_item(self, item, spider):
        open(self.file_name, 'a').write('<a href="'+item['url'] + '">' + item['title'] + '</a></br>\n')
        return item

    def open_spider(self, spider):
        with open(self.file_name, 'a') as f:
            f.seek(0)
            f.truncate()

    def close_spider(self, spider):
        with open(self.file_name, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write("<html>\n<b>共 " + str(spider.count) + " 条匹配的数据:</b></br>\n" + content + "</html>")
