from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class SpiderSpider(CrawlSpider):
    name = "spider"
    start_urls = ['https://vnexpress.net/kinh-doanh/quoc-te']
    rules = [
        Rule(LinkExtractor(
            allow=('^https:\/\/vnexpress.net.*\d{7}.html$')
        ),
            callback='parse_item'
        )
    ]

    def parse_item(self, response):
        filename = response.url.split('/')[-1]
        filename = filename.replace('.html', '.csv')
        f = open(filename, 'w', encoding='utf-8')
        title = response.xpath("///h1[@class='title-detail']/text()").get()
        f.write(title+'\n')
        description = response.xpath("//p[@class='description']/text()").get()
        f.write(description+'\n')
        content = response.xpath("//p[@class='Normal']/text()").extract()
        content1 = '\n'.join(content)
        f.write(content1)
        f.close()



