import scrapy


class Crawling(scrapy.Spider):
    name = 'test'
    # allowed_domains = 'vnexpress.net'
    start_urls = ['https://vnexpress.net/tom-cruise-duoc-hai-quan-my-vinh-danh-4178310.html']

    def parse(self, response):
        yield{
            'content' : response.xpath("//div[@class='container']//p[@class='Normal']//text()").extract()
        }


