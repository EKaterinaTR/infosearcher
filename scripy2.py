import scrapy
from scrapy.crawler import CrawlerProcess
import json


class DownloadDocsSpider(scrapy.Spider):
    start_urls = []
    name = 'docs'
    index = 0
    def __init__(self):
        self.start_urls = []
        with open('links.jsonl') as f:
            for line in f:
                data = json.loads(line)
                for i in data:
                    self.start_urls.append(data[i])


    def parse(self, response):
        yield {
            f'{self.index}': response.xpath('//body').get()
        }
        self.index += 1

##Debag

if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(DownloadDocsSpider)
    process.start()
