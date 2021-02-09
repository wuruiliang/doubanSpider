# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DoubanspiderPipeline:
    file_name = "output.html"

    def process_item(self, item, spider):
        open(self.file_name, 'a').write('<a>' + item['url'] + '</a> ，' + item['title'] + '</br>\n')
        return item
