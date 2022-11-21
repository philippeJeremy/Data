from scrapy import Selector
import scrapy

# scrapy crawl imdb1 -o quotes.json


class QuotesSpider(scrapy.Spider):
    name = "imdb1"
    start_urls = [
        'https://www.imdb.com/chart/top',
    ]

    def parse(self, response):
       
        for quote in response.css('tr'):
            yield {
                'classement': quote.css('td.titleColumn::text').get(),
                'title': quote.css('td.titleColumn a::text').get(),
                'url': quote.css('td.titleColumn a::attr(href)').get(),
                'note': quote.css('td.ratingColumn strong::text').get(),
                "l'equipe": quote.css('td.titleColumn a::attr(title)').get(), 
            }
   

            
            

            

 
