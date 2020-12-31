# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Game(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    timestamp = scrapy.Field()
    server = scrapy.Field()
    result = scrapy.Field()
    team_1 = scrapy.Field()
    team_2 = scrapy.Field()
    game_length = scrapy.Field()
