# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re

class DoubanspiderPipeline:
    file_name = "output.html"
    count_pattern = '<span id="count">\s*[0-9]*\s*</span>'

    def process_item(self, item, spider):
        with open(self.file_name, 'r+') as f:
            content = f.read()
            content = re.sub(self.count_pattern, '<span id="count"> ' + str(spider.count) + ' </span>', content)
            f.seek(0, 0)
            f.write(content + '<a href="'+item['url'] + '">' + item['title'] + '</a></br>\n')
        return item

    def open_spider(self, spider):
        with open(self.file_name, 'a') as f:
            f.seek(0)
            f.truncate()
            f.write('<html>\n<b>共<span id="count"> ' + str(spider.count) + ' </span> 条匹配的数据:</b></br>\n')

    def close_spider(self, spider):
        with open(self.file_name, 'a') as f:
            f.write("</html>")
            f.close()
