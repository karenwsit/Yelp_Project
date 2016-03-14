from scrapy.spider import BaseSpider

from scraper_app.items import YelpReview

class YelpSpider(BaseSpider):
    """Spider for regularly updated yelp.com site"""

    name = 'yelp'
    allowed_domains = ['yelp.com']
    start_urls = ['https://www.yelp.com/biz/']

    deals_list_xpath = '//div[@class="review review--with-sidebar"]/'

    items = {
    'review_id': './/@data-review-id',
    'text': './div[@class="review-wrapper"]/div[@class="review-content"]/p[@itemprop="description"]',
    'rating': './/div[@class="review-wrapper"]/div[@class="review-content"]/div[@class="biz-rating biz-rating-very-large clearfix"]/div[@itemprop="reviewRating"]/div[@class="rating-very-large"]/meta/@content',
    'date': './/div[@class="review-wrapper"]/div[@class="review-content"]/div[@class="biz-rating biz-rating-very-large clearfix"]/span[@class="rating-qualifier"]/meta/@content',
    'reviewer_location': './/div[@class="review-sidebar"]/div[@class="review-sidebar-content"]/div[@class="ypassport media-block"]/div[@class="media-story"]/ul[@class="user-passport-info"]/li[@class="user-location"]/text()',
    'restaurant_id': '//div[@class="review-sidebar"]/div[@class="review-sidebar-content"]/div[@class="ypassport media-block"]/div[@class="media-story"]/ul[@class="user-passport-info"]/li[@class="user-location"]/b/text()'
    }