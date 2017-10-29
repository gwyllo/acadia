# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AcadiascraperItem(scrapy.Item):
    # define the fields for your item here like:
	title = scrapy.Field()
	tags = scrapy.Field()
	body = scrapy.Field()
	file_urls = scrapy.Field()
	files = scrapy.Field()