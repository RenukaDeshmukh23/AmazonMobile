# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class MobileSpider(scrapy.Spider):
    name = 'mobile'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/b?node=16382860031&pf_rd_p=fa25496c-7d42-4f20-a958-cce32020b23e&pf_rd_r=1H6DJY8RHX1QKECRD760']

    def parse(self, response):
        URL=response.xpath('//*[@id="mainResults"]//a/@href').extract()
        for url in URL:
            #yield{"URL":url}
            yield Request(url, callback=self.parse_Info)

    def parse_Info(self,response):
        Ratings=response.xpath('//*[@class="a-icon-alt"]/text()').extract_first()
        Title=response.xpath('//*[@id="productTitle"]/text()').extract_first().strip()
        #Title = Title.strip("\n")
        Price= response.xpath('//*[@id="priceblock_ourprice"]/text()').extract_first()
        InStock=response.xpath('//*[@class="a-size-medium a-color-success"]/text()').extract_first().strip()
        #InStock = InStock.strip("\n")

        yield{'Title':Title,
            'Ratings':Ratings,
            'Price':Price,
            'Availability':InStock}
