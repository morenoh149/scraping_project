# scraping_project
software for scraping some website

## Installation
1. `pipenv shell`
1. `pipenv install`

## Running
Pass in the site as an environment variable. Do not add it to version control
to keep it a secret
1. `HOSTNAME=foo.com scrapy crawl nyc -o questions.csv`
read /site_scraper/spiders/city_spider.py to see how the hostname is used


## Resources
* https://doc.scrapy.org/en/1.5/intro/tutorial.html

## TODO
* store data in a csv
