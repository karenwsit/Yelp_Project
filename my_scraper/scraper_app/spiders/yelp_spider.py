from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from scraper_app.items import YelpReview

class YelpSpider(BaseSpider):
    """Spider for regularly updated yelp.com site"""

    name = 'yelp'
    allowed_domains = ['yelp.com']
    start_urls = ['https://www.yelp.com/biz/']

    reviews_list_xpath = '//div[@class="review review--with-sidebar"]/'

    items_fields = {
        'review_id': './/@data-review-id',
        'text': './div[@class="review-wrapper"]/div[@class="review-content"]/p[@itemprop="description"]',
        'rating': './/div[@class="review-wrapper"]/div[@class="review-content"]/div[@class="biz-rating biz-rating-very-large clearfix"]/div[@itemprop="reviewRating"]/div[@class="rating-very-large"]/meta/@content',
        'date': './/div[@class="review-wrapper"]/div[@class="review-content"]/div[@class="biz-rating biz-rating-very-large clearfix"]/span[@class="rating-qualifier"]/meta/@content',
        'reviewer_location': './/div[@class="review-sidebar"]/div[@class="review-sidebar-content"]/div[@class="ypassport media-block"]/div[@class="media-story"]/ul[@class="user-passport-info"]/li[@class="user-location"]/text()',
        'restaurant_id': '//div[@class="review-sidebar"]/div[@class="review-sidebar-content"]/div[@class="ypassport media-block"]/div[@class="media-story"]/ul[@class="user-passport-info"]/li[@class="user-location"]/b/text()'
    }

    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses
        """
        #Instantiate a HtmlXPathSelector 
        selector = HtmlXPathSelector(response)

        #Iterate over reviews
        for review in selector.select(self.reviews_list_xpath):
            loader = XPathItemLoader(YelpReview(), selector=review)

            #Define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            #Iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
