import scrapy


class japanesesnacks(scrapy.Spider):
 	name='japanesesnacks'
 	start_urls=['https://www.bokksu.com/collections/japanese-snack-market/snack','https://www.bokksu.com/collections/japanese-snack-market/snack?page=2','https://www.bokksu.com/collections/japanese-snack-market/snack?page=3','https://www.bokksu.com/collections/japanese-snack-market/snack?page=4','https://www.bokksu.com/collections/japanese-snack-market/snack?page=5','https://www.bokksu.com/collections/japanese-snack-market/snack?page=6']
 	
 	def parse(self, response):
 		for products in response.css('div.product-item__inner'):
 	 		yield {
	 	 		'name': products.css('span a::text').get().replace('\n',''),
	 			'price': products.css('span.money::text').get().replace('\n',''),
	 			'link': products.css('span a').attrib['href'],
	 				 	 		}