
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

import re

class ValidationPipeline:
    def process_item(self, item, spider):
        if not item['id'] :
            raise DropItem('Missing ID')
        if not item['url']:
            raise DropItem('Missing URL')
        
        return item



