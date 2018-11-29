import scrapy
import os
hostname = os.environ['HOSTNAME']


class NYCSpider(scrapy.Spider):
    name = "nyc"

    def start_requests(self):
        urls = [
'https://{}/Interview/new-york-city-data-scientist-interview-questions-SRCH_IL.0,13_IM615_KO14,28.htm'.format(hostname),
#'https://{}/Interview/new-york-city-data-scientist-interview-questions-SRCH_IL.0,13_IM615_KO14,28_IP2.htm'.format(hostname),
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.css(".row"):
            if row.css('.questionText::text').extract_first():
                yield {
                    'author': row.css('.authorInfo > a::text').extract_first(),
                    'question': row.css('.questionText::text').extract_first(),
                }
        next_page = response.css('.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
'''
        page = response.url.split("/")[-1]
        filename = 'questions-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
'''
