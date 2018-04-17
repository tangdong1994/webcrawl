#第一种的爬虫
'''
class QuoteSpider(scrapy.Spider):
	name="quotes"
	"""
	可以使用一个包含网址列表的start_urls类属性，
	这个列表将被默认的start_requests（）用来为我们的spider创建初识请求
	start_urls=[
		'http://quotes.toscrape.com/page/1/',
		'http://quotes.toscrape.com/page/2/',
	]	
	"""
	def start_requests(self):
		urls=[
			'http://quotes.toscrape.com/page/1/',
			'http://quotes.toscrape.com/page/2/',
		]
		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)

	def parse(self,response):
		page=response.url.split("/")[-2]
		filename='quote-%s.html' % page
		with open(filename,'wb') as f:
			f.write(response.body)
		self.log("Saved file %s" % filename)
'''
#第二种爬虫
import scrapy
class QuotesSpider(scrapy.Spider):
	name="quotes"

	def start_requests(self):
		url='http://quotes.toscrape.com/'
		tag=getattr(self,'tag',None)
		if tag is not None:
			url=url+'tag/'+tag
		yield scrapy.Request(url,self.parse)

	def parse(self,response):
		for quote in response.css('div.quote'):
			yield{
				'text':quote.css('span.text::text').extract_first(),
				'author':quote.css('small.author::text').extract_first(),
			}

		next_page=response.css('li.next a::attr(href)').extract_first()
		if next_page is not None:
			yield response.follow(next_page,self.parse)