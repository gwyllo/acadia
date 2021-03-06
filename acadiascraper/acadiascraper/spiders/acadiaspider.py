# -*- coding: utf-8 -*-
from acadiascraper.items import *
import scrapy
 
class ArchdailySpider(scrapy.Spider):
	name = "archdaily-spider"
	def start_requests(self):
		for page in range(0,1):
			yield self.make_requests_from_url('https://www.archdaily.com/projects/page/%d'%page)
	#start_urls = ["http://www.archdaily.com/projects/page/1","http://www.archdaily.com/projects/page/2","http://www.archdaily.com/projects/page/3"]
	
	def parse(self, response):
		# get all of the projects on the page based on the markup
		for href in response.xpath("//div[contains(@class, 'afd-post-stream')]/h3/a"):
			if href is not None:
				urlpath = response.urljoin(href.xpath("@href").extract_first())
				#call the parse_project function
				yield scrapy.Request(urlpath, self.parse_project)
		
		# Alternatively, if your site doesnt support page numbers in the url, 
		# you can extract the 'Next' link from the pagination, load it and parse it
		#next = response.css("div.pagination").xpath("a[contains(., 'next')]")
		#if next is not None:
			#yield scrapy.Request(next.xpath("@href").extract_first(), self.parse)


	def parse_project(self, response):
		#Lets try to grab some images. We can even check to markup to only get certain
		# types of images. Here we can check if image is a drawing
		img = response.xpath("//img[contains(@alt, 'elevation') or contains(@alt, 'Elevation') or contains(@alt, 'plan') or contains(@alt, 'Plan') or contains(@alt, 'section') or contains(@alt, 'Section')]/@data-src").extract()
		#photographs are identified with the © symbol
		#img = response.xpath(u"//img[contains(@alt, '©')]/@data-src").extract()
		#all images
		#img = response.xpath("//img/@data-src").extract()
		#store the result 
		imageURL = [response.urljoin(i) for i in img]
		
		# grab the title and publication date of the current issue
		title = ' '.join(s.rstrip().lstrip() for s in response.css("header.article-header h1::text").extract())
		tags = response.css(".single-tags-cats a::text").extract()
 		body = ' '.join(s.rstrip() for s in response.css(".afd-post-content p::text").extract() if len(s.rstrip())>0)
		
		# Check if we got any images. One way of parsing the scrape is to only 
		# yield projects that have certain tags e.g. 
		# if imgURL is not None and ("Houses" in tags):
		if imageURL is not None:
			yield AcadiascraperItem(title=title, tags=tags, body = body, file_urls=imageURL)
			
		
