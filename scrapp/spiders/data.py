import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy import Request
import time
from scrapy.http import FormRequest, TextResponse
from datetime import date

class Super(scrapy.Spider):
	name = "dspim"
	start_urls = ['https://www.dspim.com/about-us/mandatory-disclosure/portfolio-disclosures']
	def __init__(self, keyword=None, **kwargs):
		self.keyword = keyword
		self.driver = webdriver.Chrome()
	def parse(self,response):
		self.driver.get(response.url)
		time.sleep(1)
		
		selector = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
		click = self.driver.find_elements_by_xpath('//div[@class="sfContentBlock"]/p/a')
		for each in click:
			each.click()
			time.sleep(2)
