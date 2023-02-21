import scrapy
from scrapy.crawler import CrawlerProcess


class DownloadLinksSpider(scrapy.Spider):
    name = 'quotes'
    URL = 'https://ru.wikipedia.org/w/index.php?title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%9F%D0%BE%D0%B8%D1%81%D0%BA&limit=100&offset=0&ns0=1&search=%D0%BF%D1%82%D0%B8%D1%86%D1%8B'
    start_urls = [URL, ]
    domain = 'https://ru.wikipedia.org/'
    NAME_SELECTOR = 'a ::attr(href)'

    def parse(self, response):
        for i, quote in enumerate(response.xpath('//*[@id="mw-content-text"]/div[4]/div[2]/ul/li')):
            yield {
                f'{i}': self.domain + quote.xpath('table/tr/td[2]/div[1]/a').css(self.NAME_SELECTOR).get(),
            }



##Debag

# if __name__ == '__main__':
#     process = CrawlerProcess()
#     process.crawl(DownloadLinksSpider, category="electronics")
#     process.start()
