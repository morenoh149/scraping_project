# scraping_project
software for scraping some website

## Installation
1. `pipenv shell`
1. `pipenv install`

## Running
Pass in the site as an environment variable. Do not add it to version control
to keep it a secret
1. `HOSTNAME=<site url> scrapy crawl nyc -o questions.csv`

## Resources
* https://doc.scrapy.org/en/1.5/intro/tutorial.html

## TODO
* store data in a csv
