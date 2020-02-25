from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem, PhpBingItem, PhpBing1Item


class CnBing(BasePortiaSpider):
    name = "cn.bing.com"
    allowed_domains = ['cn.bing.com']
    start_urls = ['https://cn.bing.com/search?q=php&qs=n&form=QBLH&sp=-1&pq=&sc=0-0&sk=&cvid=9514D5C380364C2A86F3788E00631681&rdr=1&rdrig=53F149590DF046029D0C5F7FAF9E1035']
    rules = [
        Rule(
            LinkExtractor(
                allow=(),
                deny=('.*')
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[Item(PhpBing1Item, None, '.b_title > h2', [Field(
        'title_url', 'a::attr(href)', []), Field('title', 'a *::text', [])])]]
