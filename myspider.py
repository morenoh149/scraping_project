import scrapy
import os
hostname = os.environ['HOSTNAME']

class Spider(scrapy.Spider):
  name = 'questionsSpider'
  start_urls = [hostname]

  def parse(self, response):
    for title in response.css('.post-header>h2'):
      yield {'title': title.css('a ::text').extract_first()}

    for next_page in response.css('div.prev-post > a'):
      yield response.follow(next_page, self.parse)
