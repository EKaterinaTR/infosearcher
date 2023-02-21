import scrapy
from scrapy.crawler import CrawlerProcess
import json

from itemadapter import ItemAdapter


class JsonWriterPipeline:

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        line = ItemAdapter(item).asdict()
        for key in line.keys():
            with open(f'doc2/{key}_doc.txt', 'w', encoding='utf-8') as f:
                line = ItemAdapter(item).asdict()[f'{key}']
                f.write(line)
        return item


class DownloadDocsSpider(scrapy.Spider):
    start_urls = []
    dic_url = {}
    name = 'docs'

    def __init__(self):
        self.start_urls = []
        self.dic_url = {}
        with open('links.jsonl') as f:
            for line in f:
                data = json.loads(line)
                for i in data:
                    self.dic_url[data[i]] = f'{i}'
                    self.start_urls.append(data[i])

    def parse(self, response):
        yield {
            f'{self.dic_url[response.url]}': response.text
        }

        

if __name__ == '__main__':
    settings = {"ITEM_PIPELINES": {'sc4.JsonWriterPipeline': 300}}
    process = CrawlerProcess(settings)
    process.crawl(DownloadDocsSpider)
    process.start()
