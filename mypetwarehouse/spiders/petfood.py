# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PetfoodSpider(CrawlSpider):
    name = 'petfood'
    allowed_domains = ['mypetwarehouse.com.au']

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://www.mypetwarehouse.com.au/dog-food', headers={
            'User-Agent': self.user_agent
        })

    rules = (
        #Rule(LinkExtractor(restrict_xpaths="(//div[@class ='item-grid col-xs-12 col-sm-6 col-md-4 col-lg-3']/div/a"), callback='parse_item', follow=True)
        Rule(LinkExtractor(restrict_xpaths="//div[@class ='list-item-grid col-xs-6 col-sm-4 col-md-3']/div/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="(//td[@valign ='top'])[4]/a"), callback='parse_item', follow=True),
        #Rule(LinkExtractor(restrict_xpaths="//span[@class='button-text'])[last()]")),
    )

    def parse_item(self, response):
        yield {
            'Product': response.xpath("//h1/text()").get(),
            'price': response.xpath("//span[@class ='text-price']/text()").get(),
            'product_url': response.url,
            
        }