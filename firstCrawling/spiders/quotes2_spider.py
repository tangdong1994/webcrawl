import scrapy

class QuoteSpider(scrapy.Spider):
	name="quotes2"
	start_urls=[
		'http://quotes.toscrape.com/page/1/',
	]

	def parse(self,response):
		for quote in response.css('div.quote'):
			yield {
				'text':quote.css('span.text::text').extract_first(),
				'author':quote.css('small.author::text').extract_first(),
				'tags':quote.css('div.tags a.tag::text').extract(),
			}

		next_page=response.css('li.next a::attr(href)').extract_first()
		if next_page is not None:
			'''
			方法一：使用scrapy.Request
			next_page=response.urljoin(next_page)
			yield scrapy.Request(next_page,callback=self.parse)
			'''
			'''
			方法二：使用response.follow
			yield response.follow(next_age,callback=self.parse)
			'''
			for a in response.css('li.next a'):
				yield response.follow(a,callback=self.parse)