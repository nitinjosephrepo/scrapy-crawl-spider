# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PetfoodSpider(CrawlSpider):
    name = 'petfood'
    allowed_domains = ['mysetwarehouse.com.au']

    ##User_agent can also be definted from the setting file
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'

    def start_requests(self):
        ##to prevent abuse, domain crawled has been intentionally modified
        yield scrapy.Request(url='https://www.mysetwarehouse.com.au/dog-food', headers={
            'User-Agent': self.user_agent
        })

    rules = (
        #link extractors below uses Xpath to identify the elements on the page and extract the link and then follow
        Rule(LinkExtractor(restrict_xpaths="//div[@class ='list-item-grid col-xs-6 col-sm-4 col-md-3']/div/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="(//td[@valign ='top'])[4]/a"), callback='parse_item', follow=True),

    )

    def parse_item(self, response):
        yield {
            'Product': response.xpath("//h1/text()").get(),
            'price': response.xpath("//span[@class ='text-price']/text()").get(),
            'product_url': response.url,
            
        }