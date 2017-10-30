from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler

google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
	storage={'root_dir': 'your_image_dir'})
google_crawler.crawl(keyword='brick facade', offset=0, max_num=1000,
	date_min=None, date_max=None,
	min_size=(200,200), max_size=None)
