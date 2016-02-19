# -*- coding: utf-8 -*-

from scrapy import Item, Field


class Article(Item):

	titre = Field()
	key = Field()
	content = Field()

class Lien(Item):

	titre = Field()
	lien = Field()
