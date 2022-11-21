# question 3
import os 
import logging
import scrapy
from scrapy.crawler import CrawlerProcess

# question 4
class imdb_spider(scrapy.Spider):
    # Name of your spider
    name = "imdb"

    # Url to start your spider from 
    start_urls = [
        'https://www.imdb.com/chart/top',
    ]

    # Callback function that will be called when starting your spider
    # It will get text, author and tags of the first <div> with class="quote"
    def parse(self, response):
        return {
            "ranking": response.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[1]/td[2]/text()').get()
            ,
            "title": response.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[1]/td[2]/a/text()').get()
            , 
            "url": response.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[1]/td[2]/a').attrib["href"]
            ,
            "crew": response.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[1]/td[2]/a').attrib["title"]
            ,
            "rating": response.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[1]/td[1]/span[2]').attrib["data-value"]
            ,
            "nb_voters": response.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[1]/td[1]/span[4]').attrib["data-value"]            
        }

# Name of the file where the results will be saved
filename = "imdb1.json"

# If file already exists, delete it before crawling (because Scrapy will 
# concatenate the last and new results otherwise)
if filename in os.listdir('01-Become_a_movie_director/'):
        os.remove('01-Become_a_movie_director/' + filename)

# Declare a new CrawlerProcess with some settings
## USER_AGENT => Simulates a browser on an OS
## LOG_LEVEL => Minimal Level of Log 
## FEEDS => Where the file will be stored 
## More info on built-in settings => https://docs.scrapy.org/en/latest/topics/settings.html?highlight=settings#settings
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        '01-Become_a_movie_director/' + filename : {"format": "json"},
    }
})

# Start the crawling using the spider you defined above
process.crawl(imdb_spider)
process.start()