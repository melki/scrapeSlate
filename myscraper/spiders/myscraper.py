# -*- coding: utf-8 -*-

from scrapy import Spider, Request
from ..items import Article
from ..items import Lien


class MyScraper(Spider):
    name = u'myscraper'


    def start_requests(self):

        urlToVisit = {}
        Request(
            url='http://www.google.fr/',
            callback=self.parse,
        )


    def parse(self, response):
    	
        for i in response:
            yield i