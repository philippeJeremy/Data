from scrapy import Selector
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "imdb2"
    start_urls = [
        'https://www.imdb.com/chart/top',
    ]

    def parse(self, response):
        
        urls = str(response.css('td.titleColumn a::attr(href)').extract())
        
        with open('url list.txt','w') as f:
            f.seek(0)
            f.write(urls.split("\n"))