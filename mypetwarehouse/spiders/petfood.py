# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PetfoodSpider(CrawlSpider):
    name = 'petfood'
    allowed_domains = ['mypetwarehouse.com.au']
    start_urls = ['https://www.mypetwarehouse.com.au/dog-food']

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
            ##'book_url': response.url,
            #'book_category':response.xpath("//ul[@class='breadcrumb']/li[3]/a/text()").get(),
        }