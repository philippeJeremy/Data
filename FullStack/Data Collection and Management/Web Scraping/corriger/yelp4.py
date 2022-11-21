import os
import logging

import scrapy
from scrapy.crawler import CrawlerProcess

import json
file = open("02-Optional_Scraping_Yelp/restaurant_japonais-paris.json")
file = json.load(file)
list_url = ["https://www.yelp.fr/" + element["url"] for element in file]

class YelpSpiderDetail(scrapy.Spider):
    # Name of your spider
    name = "yelp"

    # Starting URL
    start_urls = list_url

    # Parse function for form request
    def parse(self, response):
        name = response.xpath('/html/body/yelp-react-root/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/h1/text()').get()
        stars = response.css("div.i-stars__09f24__foihJ").attrib["aria-label"]
        n_votes = response.xpath('/html/body/yelp-react-root/div[1]/div[3]/div[1]/div[1]/div/div/div[2]/div[2]/span/text()').get()
        address = response.xpath('/html/body/yelp-react-root/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div/section[1]/div/div[2]/div/div[1]/p[2]/text()').get()
        hours = response.xpath('/html/body/yelp-react-root/div[1]/div[4]/div/div/div[2]/div/div[1]/section[1]/div[2]/div[2]/div/div/table')
        hours_full = hours.css('p::text').getall()
        phone = response.xpath('/html/body/yelp-react-root/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div/section[1]/div/div[1]/div/div[1]/p[2]/text').get()
        amenities = response.css('border-color--default__09f24__NPAKY span::text').getall()
        reviews = response.xpath('/html/body/yelp-react-root/div[1]/div[4]/div/div/div[2]/div/div[1]/div[2]/section/div[2]/div/ul/li/div/div[4]/p/span/text()').getall()

        yield {
            "name":name,
            "url":response.url,
            "stars":stars,
            "n_votes":n_votes,
            "address":address,
            "hours":hours_full,
            "phone":phone,
            "amenities":amenities,
            "reviews":reviews
        }

        try:
            next_page = response.css('a.next-link').attrib["href"]
        except KeyError:
            logging.info('No next page. Terminating crawling process.')
        else:
            yield response.follow(next_page, callback=self.parse)

# Name of the file where the results will be saved
filename = "restaurant_japonais-paris_detail" + ".json"

# If file already exists, delete it before crawling (because Scrapy will concatenate the last and new results otherwise)
if filename in os.listdir():
        os.remove(filename)

# Declare a new CrawlerProcess with some settings
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "AUTOTHROTTLE_ENABLED": True,
    "FEEDS": {
        filename: {"format": "json"},
    }
})

# Start the crawling using the spider you defined above
process.crawl(YelpSpiderDetail)
process.start()